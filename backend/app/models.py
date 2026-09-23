"""Pydantic models: the one place the shape of this system is defined.

FastAPI derives its OpenAPI schema from these, and the frontend generates its
TypeScript types from that schema (openapi-typescript) - so a field added or
renamed here is the only edit needed to keep both sides in sync.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

PriceTier = Literal["budget", "mid", "premium", "luxury"]
BidModel = Literal["CPM", "CPC", "CPA"]


# ---- raw catalog data (data/publishers.json, data/shopper_personas.json) ----


class Audience(BaseModel):
    age_skew: str
    gender_split: dict[str, float]
    top_geos: list[str]
    income_tier: str


class PublisherRecord(BaseModel):
    id: str
    name: str
    category: str
    subcategories: list[str]
    monthly_impressions: int
    avg_order_value_usd: float
    audience: Audience
    notes: str


class PersonaRecord(BaseModel):
    id: str
    name: str
    age_range: str
    gender_skew: str
    description: str
    category_affinities: list[str]
    price_sensitivity: str
    messaging_preferences: list[str]
    disinterested_in: list[str]
    typical_aov_usd: float


# ---- step 1: extraction output ----


class ExtractedFields(BaseModel):
    """What the LLM actually fills in. raw_input is known ground truth, not
    something worth asking the model to echo back."""

    inferred_category: str
    inferred_subcategories: list[str] = []
    # Selected from the catalog's own vocabulary (data.catalog_vocabulary()),
    # not invented. This is what scoring matches on. Empty is meaningful: it
    # means nothing in this catalog relates to the advertiser at all.
    catalog_categories: list[str] = []
    price_tier: PriceTier
    brand_tone: list[str] = []
    # Only set when the advertiser's own words signal it - never guessed to
    # fill the field. None means "no signal", not "unknown/average".
    target_age_range: tuple[int, int] | None = None
    target_gender_lean: Literal["female", "male"] | None = None
    confidence: float = Field(ge=0, le=1)
    ambiguity_notes: list[str] = []


class AdvertiserProfile(ExtractedFields):
    raw_input: str


class CampaignRequest(BaseModel):
    business_description: str
    total_budget_usd: float = 5000.0
    flight_days: int = 14


# ---- steps 2 & 3: deterministic scoring ----


class PublisherScoreBreakdown(BaseModel):
    category_fit: float
    price_fit: float
    audience_fit: float
    tone_fit: float


class PersonaScoreBreakdown(BaseModel):
    affinity_fit: float
    price_fit: float
    messaging_fit: float


class PublisherScore(BaseModel):
    publisher_id: str
    name: str
    score: float
    breakdown: PublisherScoreBreakdown


class PersonaScore(BaseModel):
    persona_id: str
    name: str
    score: float
    breakdown: PersonaScoreBreakdown


# ---- steps 4-6: narration, creative, assembly ----


class PublisherRecommendation(BaseModel):
    publisher_id: str
    name: str
    match_score: float
    breakdown: PublisherScoreBreakdown
    reasoning: str
    budget_allocation_pct: float
    budget_allocation_usd: float
    suggested_bid_model: BidModel
    suggested_bid_range: tuple[float, float]
    # Reach, not just fit: a perfect-fit publisher with 4.8M monthly
    # impressions can't absorb the same spend as one with 62M.
    monthly_impressions: int
    estimated_impressions: int
    inventory_share_pct: float


class ExcludedPublisher(BaseModel):
    publisher_id: str
    name: str
    score: float
    reason: str


class PersonaMatch(BaseModel):
    persona_id: str
    name: str
    fit_score: float
    fit_label: str
    reasoning: str


class Viability(BaseModel):
    """Whether this catalog can serve this advertiser at all - a separate
    question from whether we understood them (that's AdvertiserProfile.
    confidence). "B2B SaaS for dental practices" is a perfectly understood
    input with no viable inventory here."""

    status: Literal["ok", "weak", "no_match"]
    headline: str
    detail: str


class CreativeDraft(BaseModel):
    """Raw LLM output for one persona, before the guardrail check re-tags it
    as a Creative with a known persona_id."""

    headline: str
    body: str


class Creative(BaseModel):
    persona_id: str
    headline: str
    body: str


# ---- step 4: reasoning narration output (lists, not dicts - dynamic-key
# objects are the one JSON-schema shape structured-output APIs handle least
# reliably across providers) ----


class PublisherReasoning(BaseModel):
    publisher_id: str
    reasoning: str


class PersonaReasoning(BaseModel):
    persona_id: str
    reasoning: str


class ReasoningOutput(BaseModel):
    recommended: list[PublisherReasoning]
    excluded: list[PublisherReasoning]
    personas: list[PersonaReasoning]


class Targeting(BaseModel):
    age_range: tuple[int, int] | None
    gender_lean: str | None
    income_tiers: list[str]
    geos: list[str]


class Budget(BaseModel):
    total_usd: float
    daily_usd: float
    flight_days: int


class BidStrategy(BaseModel):
    model: BidModel
    rationale: str


class RunMeta(BaseModel):
    generated_at: str
    pipeline_version: str
    model: str


class CampaignConfig(BaseModel):
    advertiser: AdvertiserProfile
    viability: Viability
    targeting: Targeting
    publishers: list[PublisherRecommendation]
    excluded_publishers: list[ExcludedPublisher]
    personas: list[PersonaMatch]
    creatives: list[Creative]
    budget: Budget
    bid_strategy: BidStrategy
    meta: RunMeta
