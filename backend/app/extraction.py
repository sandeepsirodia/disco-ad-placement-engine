"""Step 1: advertiser text -> structured profile. The only place free text
enters the system."""

from app.data import catalog_vocabulary
from app.llm import generate_structured
from app.models import AdvertiserProfile, ExtractedFields
from app.prompt_loader import load_prompt


def extract_advertiser_profile(raw_input: str) -> AdvertiserProfile:
    system, user_template = load_prompt("01-advertiser-extraction.md")
    user = user_template.format(
        raw_input=raw_input,
        catalog_vocabulary=", ".join(catalog_vocabulary()),
    )
    extracted = generate_structured(system, user, ExtractedFields)

    # The model is told to pick from the vocabulary; enforce it rather than
    # trust it, or one hallucinated term silently becomes a scoring signal.
    allowed = set(catalog_vocabulary())
    extracted.catalog_categories = [c for c in extracted.catalog_categories if c in allowed]

    return AdvertiserProfile(raw_input=raw_input, **extracted.model_dump())
