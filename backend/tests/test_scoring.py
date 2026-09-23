"""The one required runnable check on the branchy logic (scoring.py).

Uses the real catalog (data/publishers.json, data/shopper_personas.json) so
these numbers are the same ones a reviewer running `pytest` will see - not a
fabricated fixture that could drift from the actual data.
"""

from app.data import load_personas, load_publishers
from app.campaign import PUBLISHER_FIT_FLOOR, assemble_campaign
from app.models import AdvertiserProfile, ReasoningOutput
from app.scoring import is_disinterested, lowest_component, score_personas, score_publishers, select_personas


def senior_dog_food_profile() -> AdvertiserProfile:
    return AdvertiserProfile(
        raw_input=(
            "We sell premium dog food for senior dogs, targeting owners who care "
            "about joint health and longevity. Grain-free, vet-formulated, subscription-based."
        ),
        inferred_category="pet",
        inferred_subcategories=["pet_food", "subscription"],
        catalog_categories=["pet", "pet_food", "pet_health", "subscription"],
        price_tier="premium",
        brand_tone=["premium", "health-conscious"],
        confidence=0.85,
    )


def test_clear_fit_beats_broad_reach_publisher():
    """Pawline's notes name premium + health-conscious positioning directly -
    it should outrank Ruffco (bigger reach, but generic notes) despite Ruffco
    having a closer price_fit."""
    profile = senior_dog_food_profile()
    scores = score_publishers(profile, load_publishers())
    by_name = {s.name: s for s in scores}

    assert by_name["Pawline"].score > by_name["Ruffco"].score
    assert by_name["Pawline"].breakdown.category_fit == 100.0
    assert by_name["Pawline"].breakdown.tone_fit > by_name["Ruffco"].breakdown.tone_fit


def test_clear_exclusion_has_a_named_reason():
    """An off-category publisher should score well below the recommended
    cutoff, and the reason should be a lookup (category_fit), not a
    re-generated excuse."""
    profile = senior_dog_food_profile()
    scores = score_publishers(profile, load_publishers())
    by_name = {s.name: s for s in scores}
    median_score = sorted(s.score for s in scores)[len(scores) // 2]

    velvetline = by_name["Velvetline"]
    assert velvetline.breakdown.category_fit == 0.0
    assert velvetline.score < median_score
    assert lowest_component(velvetline.breakdown) == "category_fit"


def test_persona_disinterest_is_a_hard_filter_not_a_low_score():
    """A persona explicitly disinterested in the advertiser's category should
    be dropped entirely, not merely ranked low."""
    profile = AdvertiserProfile(
        raw_input="Fast fashion trend pieces, new drops every week, under $20.",
        inferred_category="apparel",
        inferred_subcategories=["fast_fashion"],
        catalog_categories=["apparel", "fashion"],
        price_tier="budget",
        brand_tone=["trendy", "novelty"],
        confidence=0.8,
    )
    personas = load_personas()
    sustainability_buyer = next(p for p in personas if p.id == "persona_006")
    assert is_disinterested(profile, sustainability_buyer)

    scores = score_personas(profile, personas)
    assert all(s.persona_id != "persona_006" for s in scores)


def test_pet_parent_is_the_top_persona_for_senior_dog_food():
    profile = senior_dog_food_profile()
    scores = score_personas(profile, load_personas())
    assert scores[0].persona_id == "persona_004"  # The Pet Parent


def test_off_topic_advertiser_scores_near_zero_everywhere():
    """The regression that motivated the relevance gate: a B2B SaaS product
    used to score ~36 against sock and skincare publishers, because price
    proximity and a neutral audience default paid out for nothing."""
    profile = AdvertiserProfile(
        raw_input="B2B SaaS for dental practices. We automate their patient recall workflow.",
        inferred_category="software",
        inferred_subcategories=["b2b_saas", "dental_practice_management"],
        catalog_categories=[],  # nothing in the catalog reaches this buyer
        price_tier="premium",
        brand_tone=["professional", "efficient"],
        confidence=0.75,
    )
    scores = score_publishers(profile, load_publishers())
    assert scores[0].score < 10.0, f"off-topic advertiser still scored {scores[0].score}"


def test_irrelevant_publishers_are_never_funded():
    """Found in production: Velvetline (Gen Z skincare, scoring 11) appeared
    under "Recommended publishers" for a cleaning-products brand with $500
    allocated, because a flat top-5 slice plus the 10% budget floor forced it
    in. Anything below the fit floor must carry no spend."""
    profile = AdvertiserProfile(
        raw_input="Refillable, concentrated cleaning products. Skip the single-use plastic bottles.",
        inferred_category="household",
        inferred_subcategories=["cleaning"],
        catalog_categories=["home", "home_goods", "household", "non_toxic", "refillable_products"],
        price_tier="mid",
        brand_tone=["sustainable", "practical"],
        confidence=0.8,
    )
    publishers = load_publishers()
    campaign = assemble_campaign(
        profile=profile,
        publisher_scores=score_publishers(profile, publishers),
        publisher_records={p.id: p for p in publishers},
        persona_scores=select_personas(score_personas(profile, load_personas()), limit=5),
        reasoning=ReasoningOutput(recommended=[], excluded=[], personas=[]),
        creatives=[],
        total_budget_usd=5000.0,
        flight_days=14,
    )
    for publisher in campaign.publishers:
        if publisher.budget_allocation_usd > 0:
            assert publisher.match_score >= PUBLISHER_FIT_FLOOR, (
                f"{publisher.name} scored {publisher.match_score} but was funded "
                f"${publisher.budget_allocation_usd}"
            )


def test_no_match_campaign_allocates_no_budget():
    """A config whose banner says "do not launch against them" must not also
    hand a downstream system a spend plan."""
    profile = AdvertiserProfile(
        raw_input="B2B SaaS for dental practices.",
        inferred_category="software",
        inferred_subcategories=["b2b_saas"],
        catalog_categories=[],
        price_tier="premium",
        brand_tone=["professional"],
        confidence=0.75,
    )
    publishers = load_publishers()
    campaign = assemble_campaign(
        profile=profile,
        publisher_scores=score_publishers(profile, publishers),
        publisher_records={p.id: p for p in publishers},
        persona_scores=select_personas(score_personas(profile, load_personas()), limit=5),
        reasoning=ReasoningOutput(recommended=[], excluded=[], personas=[]),
        creatives=[],
        total_budget_usd=5000.0,
        flight_days=14,
    )
    assert campaign.viability.status == "no_match"
    assert sum(p.budget_allocation_usd for p in campaign.publishers) == 0


def test_selection_honors_the_briefs_three_variant_minimum():
    """Weak personas are filtered out, but never below the 3 the brief asks
    for - the UI labels the weak ones rather than silently dropping to two."""
    profile = senior_dog_food_profile()
    scores = score_personas(profile, load_personas())
    assert len(select_personas(scores, limit=5)) >= 3
