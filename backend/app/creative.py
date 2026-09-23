"""Step 5: one headline+body per persona. Highest-risk step in the pipeline -
see prompts/03-creative-generation.md and docs/plan.md §0 for why.

Deliberately not a self-critique LLM loop (that reintroduces the latency
problem this same risk review flagged) - a cheap deterministic check with one
bounded retry instead.
"""

import re

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

# Two personas anchoring on the same underlying fact tend to produce the same
# clause reordered ("Natural soy wax. Zero synthetic fragrances." vs. "Hand-
# poured in Vermont from natural soy wax.") rather than a genuinely different
# angle - found by reading eval/output.md, not by design.
#
# Word overlap on a 5-8 word headline can't cleanly separate "shares the core
# fact plus a real new angle" (fine) from "shares the core fact and adds
# nothing" (the bug) - measured overlap for both lands in the same 0.30-0.38
# band. Calibrated to over-catch rather than under-catch: a false positive
# costs one extra regeneration, which can only add differentiation, never
# remove it; a false negative is the visible repetition this exists to fix.
HEADLINE_OVERLAP_THRESHOLD = 0.3
_STOPWORDS = {"the", "a", "an", "for", "with", "your", "and", "to", "of", "in", "on", "from"}


def needs_retry(headline: str, body: str, persona: PersonaRecord) -> bool:
    text = f"{headline} {body}".lower()
    hits_cliche = any(phrase in text for phrase in BANNED_PHRASES)
    hits_disinterest = any(term.replace("_", " ") in text for term in persona.disinterested_in)
    return hits_cliche or hits_disinterest


def _content_words(headline: str) -> set[str]:
    words = re.findall(r"[a-zA-Z']+", headline.lower())
    return {w for w in words if w not in _STOPWORDS and len(w) > 2}


def headline_overlap(a: str, b: str) -> float:
    """Jaccard similarity on content words - 1.0 is identical, 0.0 is disjoint."""
    wa, wb = _content_words(a), _content_words(b)
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa | wb)


def generate_creative(profile: AdvertiserProfile, persona: PersonaRecord, avoid_headlines: list[str] | None = None) -> Creative:
    system, user_template = load_prompt("03-creative-generation.md")
    avoid_note = ""
    if avoid_headlines:
        quoted = "; ".join(f'"{h}"' for h in avoid_headlines)
        avoid_note = (
            f"\nOther personas for this same advertiser already used: {quoted}. "
            "Anchor on a different fact from the advertiser's description than those did - "
            "do not just reorder the same clause.\n"
        )
    user = user_template.format(
        advertiser_profile_json=profile.model_dump_json(indent=2),
        persona_json=persona.model_dump_json(indent=2),
        avoid_note=avoid_note,
    )
    draft = generate_structured(system, user, CreativeDraft, temperature=CREATIVE_TEMPERATURE)

    if needs_retry(draft.headline, draft.body, persona):
        retry_user = user + "\n\nYour previous attempt was too generic, or touched on something this persona dislikes. Try again - anchor to a different concrete detail and avoid stock ad phrasing."
        draft = generate_structured(system, retry_user, CreativeDraft, temperature=CREATIVE_TEMPERATURE)

    return Creative(persona_id=persona.id, headline=draft.headline, body=draft.body)


def dedupe_creatives(profile: AdvertiserProfile, creatives: list[Creative], persona_by_id: dict[str, PersonaRecord]) -> list[Creative]:
    """Regenerate any headline that overlaps too heavily with one already kept.

    Generation runs concurrently (pipeline.py), so no single call can see its
    siblings - this is the only place that can catch cross-persona
    repetition, and it has to run after the fact, sequentially, over what's
    usually 3-5 creatives.
    """
    kept: list[Creative] = []
    kept_headlines: list[str] = []

    for creative in creatives:
        if any(headline_overlap(creative.headline, prior) > HEADLINE_OVERLAP_THRESHOLD for prior in kept_headlines):
            creative = generate_creative(profile, persona_by_id[creative.persona_id], avoid_headlines=kept_headlines)
        kept.append(creative)
        kept_headlines.append(creative.headline)

    return kept
