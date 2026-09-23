"""The pipeline, end to end. Lives here rather than in routes.py so the eval
harness runs the exact same code path the API does - an eval that exercises a
parallel reimplementation is worth nothing."""

import asyncio

from app.campaign import TOP_PERSONAS, TOP_PUBLISHERS, assemble_campaign
from app.creative import generate_creative
from app.data import load_personas, load_publishers
from app.extraction import extract_advertiser_profile
from app.models import CampaignConfig
from app.reasoning import generate_reasoning
from app.scoring import score_personas, score_publishers, select_personas
from app.semantic import prime


async def run_pipeline(
    business_description: str,
    total_budget_usd: float = 5000.0,
    flight_days: int = 14,
) -> CampaignConfig:
    # Step 1 - the only step that must finish before the others can start.
    profile = await asyncio.to_thread(extract_advertiser_profile, business_description)

    publishers = load_publishers()
    personas = load_personas()

    # One batched embedding request for every string scoring will compare,
    # instead of ~31 separate ones. Cached for the process, so subsequent runs
    # only pay for the advertiser's own tone.
    tone = ", ".join(profile.brand_tone)
    await asyncio.to_thread(
        prime,
        [tone, *(p.notes for p in publishers), *(", ".join(p.messaging_preferences) for p in personas)],
    )

    # Steps 2 & 3 - deterministic, synchronous, effectively instant.
    publisher_scores = score_publishers(profile, publishers)
    persona_scores = score_personas(profile, personas)

    recommended = publisher_scores[:TOP_PUBLISHERS]
    excluded = publisher_scores[TOP_PUBLISHERS:]
    selected_personas = select_personas(persona_scores, limit=TOP_PERSONAS)
    persona_by_id = {p.id: p for p in personas}

    # Steps 4 & 5 - neither depends on the other, so they share latency
    # instead of stacking it.
    reasoning_task = asyncio.to_thread(generate_reasoning, profile, recommended, excluded, selected_personas)
    creative_tasks = [
        asyncio.to_thread(generate_creative, profile, persona_by_id[s.persona_id]) for s in selected_personas
    ]
    reasoning, *creatives = await asyncio.gather(reasoning_task, *creative_tasks)

    # Step 6 - deterministic assembly.
    return assemble_campaign(
        profile=profile,
        publisher_scores=publisher_scores,
        publisher_records={p.id: p for p in publishers},
        persona_scores=selected_personas,
        reasoning=reasoning,
        creatives=creatives,
        total_budget_usd=total_budget_usd,
        flight_days=flight_days,
    )
