"""Deterministic publisher/persona ranking - the part of the pipeline that
isn't allowed to be a black box.

Design invariant this file exists to protect: weights are named constants,
each fit signal is its own small function, and every function returns a
score, never a decision - so tuning a weight or adding a new signal later is
an edit in one place, not a rewrite. See docs/plan.md for why this matters.
"""

from __future__ import annotations

from app.models import (
    AdvertiserProfile,
    PersonaRecord,
    PersonaScore,
    PersonaScoreBreakdown,
    PublisherRecord,
    PublisherScore,
    PublisherScoreBreakdown,
)

PRICE_TIER_MIDPOINT: dict[str, float] = {
    "budget": 25.0,
    "mid": 55.0,
    "premium": 90.0,
    "luxury": 150.0,
}

# The knobs to tune once real output is in front of you (docs/plan.md §0/§1).
PUBLISHER_WEIGHTS: dict[str, float] = {
    "category_fit": 0.40,
    "price_fit": 0.25,
    "audience_fit": 0.20,
    "tone_fit": 0.15,
}

PERSONA_WEIGHTS: dict[str, float] = {
    "affinity_fit": 0.50,
    "price_fit": 0.25,
    "messaging_fit": 0.25,
}

# Below this, a persona isn't plausible for the advertiser, and asking for
# copy anyway makes the model invent product claims to bridge the gap (a real
# observed failure - see docs/plan.md). The brief asks for 3-5 variants, so
# the floor yields to that minimum rather than returning two.
PERSONA_FIT_FLOOR = 30.0
MIN_PERSONAS = 3

_NEUTRAL_AUDIENCE_SCORE = 60.0  # no advertiser demo signal -> don't penalize, don't reward

# How much score survives zero category relevance. 0.15 means an irrelevant
# publisher tops out around 6/100 instead of the 36 it used to score.
GATE_FLOOR = 0.15

# Catalog-term overlaps needed for a full match bonus.
FULL_OVERLAP_AT = 4


def _advertiser_terms(profile: AdvertiserProfile) -> set[str]:
    """Catalog-vocabulary terms drive matching. The model's own free-text
    labels are display-only - matching on them meant "household_goods" missed
    the "home" and "groceries" publishers that were the actual answer."""
    return {c.lower() for c in profile.catalog_categories}


def _relevance_gate(category_score: float) -> float:
    """Category relevance gates everything else.

    Without this, a publisher with zero category overlap still scored ~36:
    price proximity and a neutral audience default handed out points for
    nothing, putting a sock retailer level with a real match. Price and
    audience fit are only meaningful *conditional* on the publisher serving
    the category at all.
    """
    return GATE_FLOOR + (1.0 - GATE_FLOOR) * (category_score / 100.0)


def _parse_age_range(age_skew: str) -> tuple[int, int] | None:
    if "-" not in age_skew:
        return None
    lo, hi = age_skew.split("-", 1)
    try:
        return int(lo), int(hi)
    except ValueError:
        return None


def _overlap_fraction(a: tuple[int, int], b: tuple[int, int]) -> float:
    inter_lo, inter_hi = max(a[0], b[0]), min(a[1], b[1])
    if inter_hi <= inter_lo:
        return 0.0
    union_lo, union_hi = min(a[0], b[0]), max(a[1], b[1])
    return (inter_hi - inter_lo) / max(union_hi - union_lo, 1)


def _fuzzy_overlap_count(advertiser_terms: set[str], catalog_terms: set[str]) -> int:
    """Substring match, not exact-set match: publishers.json says
    "subscription", shopper_personas.json says "subscription_boxes" - the two
    catalogs don't share one taxonomy, so exact equality silently misses real
    overlaps. Good enough at 20/10 rows; graduate to embedding similarity if
    the real catalog's vocabulary turns out messier (docs/plan.md)."""
    return sum(1 for a in advertiser_terms if any(a in t or t in a for t in catalog_terms))


def _overlap_denominator(advertiser_terms: set[str]) -> int:
    """Matching this many catalog terms is already a strong signal. Dividing
    by the raw term count instead punished advertisers whose extraction
    happened to be verbose - 7 terms could never out-score 3."""
    return max(min(len(advertiser_terms), FULL_OVERLAP_AT), 1)


# ---- publisher fit signals ----


def category_fit(profile: AdvertiserProfile, publisher: PublisherRecord) -> float:
    advertiser_terms = _advertiser_terms(profile)
    if not advertiser_terms:
        return 0.0
    publisher_category = publisher.category.lower()
    publisher_terms = {publisher_category, *(s.lower() for s in publisher.subcategories)}

    # Base fires when a selected catalog term names the publisher's own
    # category. Comparing the model's free-text label here instead meant an
    # activewear brand missed Movewell, which the catalog files under
    # "apparel" - correct extraction, wrong vocabulary, zero base.
    category_match = any(
        term == publisher_category or term in publisher_category or publisher_category in term
        for term in advertiser_terms
    )
    base = 60.0 if category_match else 0.0
    overlap_count = _fuzzy_overlap_count(advertiser_terms, publisher_terms)
    subcat_bonus = 40.0 * min(overlap_count / _overlap_denominator(advertiser_terms), 1.0)
    return min(100.0, base + subcat_bonus)


def price_fit(profile: AdvertiserProfile, publisher: PublisherRecord, aov_min: float, aov_max: float) -> float:
    target = PRICE_TIER_MIDPOINT[profile.price_tier]
    span = max(aov_max - aov_min, 1.0)
    distance = abs(target - publisher.avg_order_value_usd)
    return max(0.0, 100.0 - (distance / span) * 100.0)


def audience_fit(profile: AdvertiserProfile, publisher: PublisherRecord) -> float:
    age_score = _NEUTRAL_AUDIENCE_SCORE
    if profile.target_age_range:
        pub_range = _parse_age_range(publisher.audience.age_skew)
        if pub_range:
            age_score = _overlap_fraction(profile.target_age_range, pub_range) * 100.0

    gender_score = _NEUTRAL_AUDIENCE_SCORE
    if profile.target_gender_lean:
        gender_score = publisher.audience.gender_split.get(profile.target_gender_lean, 0.0) * 100.0

    if profile.target_age_range and profile.target_gender_lean:
        return age_score * 0.7 + gender_score * 0.3
    if profile.target_age_range:
        return age_score
    if profile.target_gender_lean:
        return gender_score
    return _NEUTRAL_AUDIENCE_SCORE


def tone_fit(profile: AdvertiserProfile, publisher: PublisherRecord) -> float:
    if not profile.brand_tone:
        return 50.0
    notes = publisher.notes.lower()
    hits = sum(1 for term in profile.brand_tone if term.lower() in notes)
    return min(100.0, 100.0 * hits / len(profile.brand_tone))


def lowest_component(breakdown: PublisherScoreBreakdown) -> str:
    """Which fit signal dragged the score down - the exclusion reason is a
    lookup against this, never a re-generated excuse."""
    dumped = breakdown.model_dump()
    return min(dumped, key=dumped.get)  # type: ignore[arg-type]


def score_publishers(profile: AdvertiserProfile, publishers: list[PublisherRecord]) -> list[PublisherScore]:
    aovs = [p.avg_order_value_usd for p in publishers]
    aov_min, aov_max = min(aovs), max(aovs)

    scores = []
    for publisher in publishers:
        breakdown = PublisherScoreBreakdown(
            category_fit=round(category_fit(profile, publisher), 1),
            price_fit=round(price_fit(profile, publisher, aov_min, aov_max), 1),
            audience_fit=round(audience_fit(profile, publisher), 1),
            tone_fit=round(tone_fit(profile, publisher), 1),
        )
        weighted = sum(getattr(breakdown, key) * weight for key, weight in PUBLISHER_WEIGHTS.items())
        weighted *= _relevance_gate(breakdown.category_fit)
        scores.append(
            PublisherScore(
                publisher_id=publisher.id,
                name=publisher.name,
                score=round(weighted, 1),
                breakdown=breakdown,
            )
        )
    return sorted(scores, key=lambda s: s.score, reverse=True)


# ---- persona fit signals ----


def affinity_fit(profile: AdvertiserProfile, persona: PersonaRecord) -> float:
    advertiser_terms = _advertiser_terms(profile)
    if not advertiser_terms:
        return 0.0
    persona_terms = {a.lower() for a in persona.category_affinities}
    overlap_count = _fuzzy_overlap_count(advertiser_terms, persona_terms)
    return 100.0 * min(overlap_count / _overlap_denominator(advertiser_terms), 1.0)


def persona_price_fit(profile: AdvertiserProfile, persona: PersonaRecord, aov_min: float, aov_max: float) -> float:
    target = PRICE_TIER_MIDPOINT[profile.price_tier]
    span = max(aov_max - aov_min, 1.0)
    distance = abs(target - persona.typical_aov_usd)
    return max(0.0, 100.0 - (distance / span) * 100.0)


def messaging_fit(profile: AdvertiserProfile, persona: PersonaRecord) -> float:
    if not profile.brand_tone:
        return 50.0
    prefs_text = " ".join(persona.messaging_preferences).lower()
    hits = sum(1 for term in profile.brand_tone if term.lower() in prefs_text)
    return min(100.0, 100.0 * hits / len(profile.brand_tone))


def is_disinterested(profile: AdvertiserProfile, persona: PersonaRecord) -> bool:
    """Hard exclusion, not a negative weight - a persona disinterested in the
    advertiser's category is dropped, not just down-ranked.

    Deliberately casts a wider net than scoring does: `disinterested_in` is
    free text ("fast fashion", "luxury positioning"), so it's matched against
    the model's free-text labels too, not just catalog vocabulary. A false
    positive here costs one persona; a false negative writes ad copy for
    someone who explicitly dislikes the category.
    """
    advertiser_terms = {
        t.lower().replace("_", " ")
        for t in (
            profile.inferred_category,
            *profile.inferred_subcategories,
            *profile.catalog_categories,
            *profile.brand_tone,
        )
    }
    disinterests = {d.lower().replace("_", " ") for d in persona.disinterested_in}
    # Direction matters: the disinterest must be at least as specific as the
    # advertiser term. "fast fashion" inside "fast fashion apparel" is a real
    # hit; matching the other way let bare "pet" collide with the fragment in
    # "generic pet brands" and drop The Pet Parent from a dog-food campaign.
    return any(a == d or d in a for a in advertiser_terms for d in disinterests)


def score_personas(profile: AdvertiserProfile, personas: list[PersonaRecord]) -> list[PersonaScore]:
    eligible = [p for p in personas if not is_disinterested(profile, p)]
    aovs = [p.typical_aov_usd for p in personas]
    aov_min, aov_max = min(aovs), max(aovs)

    scores = []
    for persona in eligible:
        breakdown = PersonaScoreBreakdown(
            affinity_fit=round(affinity_fit(profile, persona), 1),
            price_fit=round(persona_price_fit(profile, persona, aov_min, aov_max), 1),
            messaging_fit=round(messaging_fit(profile, persona), 1),
        )
        weighted = sum(getattr(breakdown, key) * weight for key, weight in PERSONA_WEIGHTS.items())
        weighted *= _relevance_gate(breakdown.affinity_fit)
        scores.append(
            PersonaScore(
                persona_id=persona.id,
                name=persona.name,
                score=round(weighted, 1),
                breakdown=breakdown,
            )
        )
    return sorted(scores, key=lambda s: s.score, reverse=True)


def select_personas(scores: list[PersonaScore], limit: int) -> list[PersonaScore]:
    """Which personas actually get creative written for them."""
    plausible = [s for s in scores if s.score >= PERSONA_FIT_FLOOR]
    if len(plausible) < MIN_PERSONAS:
        plausible = scores[:MIN_PERSONAS]
    return plausible[:limit]


def fit_label(score: float) -> str:
    """Surfaced in the UI so a weak-but-included persona is visibly weak,
    rather than sitting next to a strong one looking equally endorsed."""
    if score >= 60.0:
        return "strong"
    if score >= PERSONA_FIT_FLOOR:
        return "moderate"
    return "weak"
