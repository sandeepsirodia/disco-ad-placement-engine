"""Step 5: one headline+body per persona. Highest-risk step in the pipeline -
see prompts/03-creative-generation.md and docs/plan.md §0 for why.

Deliberately not a self-critique LLM loop (that reintroduces the latency
problem this same risk review flagged) - a cheap deterministic check with one
bounded retry instead.
"""

from app.llm import generate_structured
from app.models import AdvertiserProfile, Creative, CreativeDraft, PersonaRecord
from app.prompt_loader import load_prompt

CREATIVE_TEMPERATURE = 0.8  # variation is the point here, unlike every other call

BANNED_PHRASES = [
    "revolutionize",
    "game-changer",
    "look no further",
    "elevate your",
    "unlock",
    "in today's fast-paced world",
    "experience the difference",
    "we've got you covered",
]


def needs_retry(headline: str, body: str, persona: PersonaRecord) -> bool:
    text = f"{headline} {body}".lower()
    hits_cliche = any(phrase in text for phrase in BANNED_PHRASES)
    hits_disinterest = any(term.replace("_", " ") in text for term in persona.disinterested_in)
    return hits_cliche or hits_disinterest


def generate_creative(profile: AdvertiserProfile, persona: PersonaRecord) -> Creative:
    system, user_template = load_prompt("03-creative-generation.md")
    user = user_template.format(
        advertiser_profile_json=profile.model_dump_json(indent=2),
        persona_json=persona.model_dump_json(indent=2),
    )
    draft = generate_structured(system, user, CreativeDraft, temperature=CREATIVE_TEMPERATURE)

    if needs_retry(draft.headline, draft.body, persona):
        retry_user = user + "\n\nYour previous attempt was too generic, or touched on something this persona dislikes. Try again - anchor to a different concrete detail and avoid stock ad phrasing."
        draft = generate_structured(system, retry_user, CreativeDraft, temperature=CREATIVE_TEMPERATURE)

    return Creative(persona_id=persona.id, headline=draft.headline, body=draft.body)
