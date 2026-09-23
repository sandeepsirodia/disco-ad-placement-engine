"""Step 4: narrate the scores computed in scoring.py. Never recomputes or
invents a number - only explains ones it was handed."""

from app.llm import generate_structured
from app.models import AdvertiserProfile, PersonaScore, PublisherScore, ReasoningOutput
from app.prompt_loader import load_prompt
from app.scoring import lowest_component


def _publisher_payload(scores: list[PublisherScore], with_reason: bool) -> list[dict]:
    payload = []
    for s in scores:
        entry = {"id": s.publisher_id, "name": s.name, "score": s.score, "breakdown": s.breakdown.model_dump()}
        if with_reason:
            entry["lowest_component"] = lowest_component(s.breakdown)
        payload.append(entry)
    return payload


def _persona_payload(scores: list[PersonaScore]) -> list[dict]:
    return [
        {"id": s.persona_id, "name": s.name, "score": s.score, "breakdown": s.breakdown.model_dump()}
        for s in scores
    ]


def generate_reasoning(
    profile: AdvertiserProfile,
    recommended: list[PublisherScore],
    excluded: list[PublisherScore],
    personas: list[PersonaScore],
) -> ReasoningOutput:
    system, user_template = load_prompt("02-reasoning-narration.md")
    user = user_template.format(
        advertiser_profile_json=profile.model_dump_json(indent=2),
        recommended_publishers_json=_publisher_payload(recommended, with_reason=False),
        excluded_publishers_json=_publisher_payload(excluded, with_reason=True),
        personas_json=_persona_payload(personas),
    )
    return generate_structured(system, user, ReasoningOutput)
