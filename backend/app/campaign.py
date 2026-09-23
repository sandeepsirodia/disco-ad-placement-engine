"""Step 6: deterministic assembly - targeting, budget split, bid strategy.
No LLM call here; everything is derived from already-computed scores and the
raw catalog records."""

from __future__ import annotations

from datetime import UTC, datetime

from app.models import (
    AdvertiserProfile,
    BidModel,
    BidStrategy,
    Budget,
    CampaignConfig,
    Creative,
    ExcludedPublisher,
    PersonaMatch,
    PersonaScore,
    PublisherRecommendation,
    PublisherRecord,
    PublisherScore,
    ReasoningOutput,
    RunMeta,
    Targeting,
    Viability,
)
from app.scoring import _parse_age_range, fit_label, lowest_component

TOP_PUBLISHERS = 5
TOP_PERSONAS = 5
BUDGET_FLOOR_PCT = 10.0

PERFORMANCE_SIGNALS = ["compete on price", "cheap", "discount", "affordable", "half the cost", "same formulation"]

# Realistic retail-media bands. Deliberately NOT derived linearly from AOV -
# doing that produced an $89 CPM for a $198-AOV publisher, a number no buyer
# would recognize. A publisher's AOV shifts where it sits inside the band; it
# doesn't set the band.
CPM_BAND = (8.0, 35.0)
CPC_BAND = (0.40, 2.50)

# You cannot buy all of a publisher's monthly inventory. Above this share,
# spend is capped and redistributed - the constraint real media planners hit
# first and the one a fit-only scorer never sees.
MAX_INVENTORY_SHARE = 0.20

# Below these, this catalog can't serve the advertiser. Separate axis from
# extraction confidence: "B2B SaaS for dental practices" is understood
# perfectly and still has nothing to buy here.
# Calibrated against the full eval run, not guessed: real matches land 56-80,
# borderline ones 36-48, and genuine non-fits 6-16 (eval/output.md).
VIABILITY_NO_MATCH_SCORE = 25.0
VIABILITY_WEAK_SCORE = 45.0

# Below this, a low score says more about the input than about the catalog.
LOW_CONFIDENCE = 0.4


def allocate_budget_pct(scores: list[float], floor_pct: float = BUDGET_FLOOR_PCT) -> list[float]:
    """Normalize to 100%, with a floor so a decent-but-not-top fit still gets
    tested rather than rounding to zero (docs/plan.md §2)."""
    n = len(scores)
    if n == 0:
        return []
    if n * floor_pct >= 100.0:
        return [round(100.0 / n, 1)] * n

    total = sum(max(s, 0.0) for s in scores) or 1.0
    raw_pct = [max(s, 0.0) / total * 100.0 for s in scores]
    result = [max(p, floor_pct) for p in raw_pct]

    deficit = sum(result) - 100.0
    over_floor_total = sum(r - floor_pct for r in result if r > floor_pct)
    if over_floor_total > 0:
        for i, r in enumerate(result):
            if r > floor_pct:
                result[i] = r - deficit * ((r - floor_pct) / over_floor_total)
    return [round(r, 1) for r in result]


def choose_bid_model(profile: AdvertiserProfile) -> BidModel:
    text = f"{profile.raw_input} {' '.join(profile.brand_tone)}".lower()
    if any(signal in text for signal in PERFORMANCE_SIGNALS):
        return "CPC"
    if profile.price_tier in ("premium", "luxury"):
        return "CPM"
    return "CPM"


def suggested_bid_range(
    model: BidModel, publisher: PublisherRecord, aov_min: float, aov_max: float
) -> tuple[float, float]:
    """Position the publisher inside a realistic band by where its AOV sits in
    the catalog - higher-AOV audiences command more, but within sane bounds."""
    span = max(aov_max - aov_min, 1.0)
    percentile = min(max((publisher.avg_order_value_usd - aov_min) / span, 0.0), 1.0)
    low_edge, high_edge = CPM_BAND if model == "CPM" else CPC_BAND
    midpoint = low_edge + (high_edge - low_edge) * percentile
    return (round(midpoint * 0.85, 2), round(midpoint * 1.15, 2))


def assess_viability(top_score: float, profile: AdvertiserProfile) -> Viability:
    # Extraction picks from the catalog's own vocabulary; returning nothing is
    # it saying outright that no audience here relates to this advertiser.
    # Cheaper and more reliable than inferring the same thing from a score.
    if not profile.catalog_categories:
        return Viability(
            status="no_match",
            headline="Outside this catalog's market",
            detail=(
                f"Nothing in this catalog reaches buyers of a '{profile.inferred_category}' "
                "product. These are consumer-retail publishers; this advertiser needs a "
                "different inventory source entirely. Rankings below are reference only - "
                "do not launch against them."
            ),
        )
    if top_score < VIABILITY_NO_MATCH_SCORE:
        # A vague input and an off-market one both score low, but they need
        # opposite advice: one wants more detail, the other wants a different
        # ad network. Telling "a new kind of thing for moms" that it's outside
        # the catalog's market is simply wrong - the catalog serves parents.
        if profile.confidence < LOW_CONFIDENCE:
            return Viability(
                status="no_match",
                headline="Not enough detail to match",
                detail=(
                    "There isn't enough in this description to place it against the catalog. "
                    "Add what you sell and who buys it - even one more clause usually resolves it."
                ),
            )
        return Viability(
            status="no_match",
            headline="No viable inventory in this catalog",
            detail=(
                f"The best available publisher scores {top_score:.0f}/100 against a "
                f"'{profile.inferred_category}' advertiser. This catalog is consumer-retail "
                "inventory; nothing here reaches this audience. Rankings below are shown for "
                "reference only - do not launch against them."
            ),
        )
    if top_score < VIABILITY_WEAK_SCORE:
        return Viability(
            status="weak",
            headline="Thin match - proceed carefully",
            detail=(
                f"The strongest publisher scores only {top_score:.0f}/100. There's a partial fit "
                "worth testing at low budget, but this catalog isn't built for this advertiser."
            ),
        )
    return Viability(
        status="ok",
        headline="Viable campaign",
        detail=f"Strongest publisher match scores {top_score:.0f}/100 with usable inventory depth.",
    )


def cap_by_inventory(
    allocations: list[float],
    records: list[PublisherRecord],
    bid_ranges: list[tuple[float, float]],
    bid_model: BidModel,
    total_budget_usd: float,
    flight_days: int,
) -> list[float]:
    """Trim any allocation that would demand more impressions than the
    publisher can actually deliver, then hand the freed budget to publishers
    with room. Fit decides who's in; inventory decides how much they get."""
    if bid_model != "CPM":
        return allocations  # CPC spend is click-gated, not impression-gated

    flight_share = min(flight_days / 30.0, 1.0)
    headroom = []
    for record, (bid_low, _) in zip(records, bid_ranges):
        deliverable = record.monthly_impressions * flight_share * MAX_INVENTORY_SHARE
        headroom.append(deliverable / 1000.0 * bid_low)  # max $ this publisher can absorb

    capped = []
    freed = 0.0
    for pct, max_usd in zip(allocations, headroom):
        wanted_usd = total_budget_usd * pct / 100.0
        if wanted_usd > max_usd:
            freed += wanted_usd - max_usd
            capped.append(max_usd / total_budget_usd * 100.0)
        else:
            capped.append(pct)

    if freed <= 0:
        return allocations

    room = [max_usd - total_budget_usd * pct / 100.0 for pct, max_usd in zip(capped, headroom)]
    total_room = sum(r for r in room if r > 0)
    if total_room > 0:
        freed_pct = freed / total_budget_usd * 100.0
        for i, r in enumerate(room):
            if r > 0:
                capped[i] += freed_pct * (r / total_room)
    return [round(p, 1) for p in capped]


def build_targeting(profile: AdvertiserProfile, recommended: list[PublisherRecord]) -> Targeting:
    age_ranges = [r for r in (_parse_age_range(p.audience.age_skew) for p in recommended) if r]
    age_range = (min(a for a, _ in age_ranges), max(b for _, b in age_ranges)) if age_ranges else None
    income_tiers = sorted({p.audience.income_tier for p in recommended})
    geos = sorted({geo for p in recommended for geo in p.audience.top_geos})
    return Targeting(
        age_range=profile.target_age_range or age_range,
        gender_lean=profile.target_gender_lean,
        income_tiers=income_tiers,
        geos=geos,
    )


def assemble_campaign(
    profile: AdvertiserProfile,
    publisher_scores: list[PublisherScore],
    publisher_records: dict[str, PublisherRecord],
    persona_scores: list[PersonaScore],
    reasoning: ReasoningOutput,
    creatives: list[Creative],
    total_budget_usd: float,
    flight_days: int,
) -> CampaignConfig:
    recommended_scores = publisher_scores[:TOP_PUBLISHERS]
    excluded_scores = publisher_scores[TOP_PUBLISHERS:]
    selected_personas = persona_scores[:TOP_PERSONAS]

    reason_by_publisher = {r.publisher_id: r.reasoning for r in reasoning.recommended}
    excluded_reason_by_publisher = {r.publisher_id: r.reasoning for r in reasoning.excluded}
    reason_by_persona = {r.persona_id: r.reasoning for r in reasoning.personas}

    bid_model = choose_bid_model(profile)
    recommended_records = [publisher_records[s.publisher_id] for s in recommended_scores]

    all_aovs = [p.avg_order_value_usd for p in publisher_records.values()]
    aov_min, aov_max = min(all_aovs), max(all_aovs)
    bid_ranges = [suggested_bid_range(bid_model, r, aov_min, aov_max) for r in recommended_records]

    allocations = allocate_budget_pct([s.score for s in recommended_scores])
    allocations = cap_by_inventory(
        allocations, recommended_records, bid_ranges, bid_model, total_budget_usd, flight_days
    )

    publishers = []
    for score, record, pct, bid_range in zip(recommended_scores, recommended_records, allocations, bid_ranges):
        spend = round(total_budget_usd * pct / 100.0, 2)
        impressions = int(spend / bid_range[0] * 1000) if bid_model == "CPM" else 0
        publishers.append(
            PublisherRecommendation(
                publisher_id=score.publisher_id,
                name=score.name,
                match_score=score.score,
                breakdown=score.breakdown,
                reasoning=reason_by_publisher.get(score.publisher_id, ""),
                budget_allocation_pct=pct,
                budget_allocation_usd=spend,
                suggested_bid_model=bid_model,
                suggested_bid_range=bid_range,
                monthly_impressions=record.monthly_impressions,
                estimated_impressions=impressions,
                inventory_share_pct=round(impressions / record.monthly_impressions * 100.0, 2)
                if record.monthly_impressions
                else 0.0,
            )
        )

    excluded = [
        ExcludedPublisher(
            publisher_id=score.publisher_id,
            name=score.name,
            score=score.score,
            reason=excluded_reason_by_publisher.get(
                score.publisher_id, f"Lowest-scoring component: {lowest_component(score.breakdown)}"
            ),
        )
        for score in excluded_scores
    ]

    personas = [
        PersonaMatch(
            persona_id=score.persona_id,
            name=score.name,
            fit_score=score.score,
            fit_label=fit_label(score.score),
            reasoning=reason_by_persona.get(score.persona_id, ""),
        )
        for score in selected_personas
    ]

    return CampaignConfig(
        advertiser=profile,
        viability=assess_viability(recommended_scores[0].score if recommended_scores else 0.0, profile),
        targeting=build_targeting(profile, recommended_records),
        publishers=publishers,
        excluded_publishers=excluded,
        personas=personas,
        creatives=creatives,
        budget=Budget(
            total_usd=total_budget_usd,
            daily_usd=round(total_budget_usd / max(flight_days, 1), 2),
            flight_days=flight_days,
        ),
        bid_strategy=BidStrategy(
            model=bid_model,
            rationale=(
                "Performance-oriented language detected - optimizing for clicks."
                if bid_model == "CPC"
                else "Brand/quality-oriented language - optimizing for reach at a controlled cost per impression."
            ),
        ),
        meta=RunMeta(
            generated_at=datetime.now(UTC).isoformat(),
            pipeline_version="0.1.0",
            model="gemini (via OpenAI-compatible endpoint)",
        ),
    )
