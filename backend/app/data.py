"""Loads the given catalog (data/publishers.json, data/shopper_personas.json).

Validated through the pydantic models on load, not just json.load - if the
catalog shape ever drifts from what scoring.py expects, this fails loudly at
startup instead of silently downstream.
"""

import json
from functools import lru_cache
from pathlib import Path

from app.models import PersonaRecord, PublisherRecord

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"


@lru_cache
def load_publishers() -> list[PublisherRecord]:
    raw = json.loads((DATA_DIR / "publishers.json").read_text())
    return [PublisherRecord.model_validate(p) for p in raw]


@lru_cache
def load_personas() -> list[PersonaRecord]:
    raw = json.loads((DATA_DIR / "shopper_personas.json").read_text())
    return [PersonaRecord.model_validate(p) for p in raw]


@lru_cache
def catalog_vocabulary() -> tuple[str, ...]:
    """Every category term the catalog actually uses.

    Extraction picks from this closed set instead of inventing labels: the
    model used to return "household_goods" for a cleaning brand, which
    string-matched nothing, while the right publishers were sitting under
    "home" and "groceries". Matching a free-text taxonomy against a fixed one
    is a losing game - so constrain the free side.
    """
    terms = set()
    for publisher in load_publishers():
        terms.add(publisher.category)
        terms.update(publisher.subcategories)
    for persona in load_personas():
        terms.update(persona.category_affinities)
    return tuple(sorted(terms))
