"""Embedding similarity for the two soft signals (tone, messaging).

Keyword matching handled the hard signals fine - category vocabulary is a
closed set, so string equality is exactly right there. It fails on the soft
ones, which are free prose on both sides: a sustainable activewear brand
scored The Fitness Enthusiast "weak" because the brand's tone ("sustainable",
"eco-conscious") shares no literal token with that persona's messaging
preferences ("performance claims", "technical fabrics"). Semantically a
strong match; lexically invisible.

The catalog is static, so every publisher/persona string is embedded once at
first use and cached. Only the advertiser's tone is embedded per request.
"""

from __future__ import annotations

import math
import os
from functools import lru_cache

from app.llm import client_or_none

DEFAULT_EMBED_MODEL = "gemini-embedding-001"


def _embed_model() -> str:
    return os.environ.get("LLM_EMBED_MODEL", DEFAULT_EMBED_MODEL)


@lru_cache(maxsize=512)
def _embed(text: str) -> tuple[float, ...] | None:
    """None means "embeddings unavailable" - callers fall back to keywords.

    Not every OpenAI-compatible provider implements /embeddings, and the whole
    point of the provider-agnostic design is that pointing LLM_BASE_URL
    somewhere else doesn't break the app.
    """
    client = client_or_none()
    if client is None or not text.strip():
        return None
    try:
        response = client.embeddings.create(model=_embed_model(), input=text)
    except Exception:  # noqa: BLE001 - provider variance is expected, not exceptional
        return None
    return tuple(response.data[0].embedding)


def _cosine(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm = math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b))
    return dot / norm if norm else 0.0


def similarity(left: str, right: str) -> float | None:
    """0-100 similarity, or None if embeddings aren't available."""
    a, b = _embed(left), _embed(right)
    if a is None or b is None:
        return None
    # Cosine over these models sits roughly in 0.3-0.95 for related prose;
    # rescale so the usable band spans the full 0-100 range instead of
    # compressing every real signal into the top third of it.
    rescaled = (_cosine(a, b) - 0.3) / 0.6
    return round(min(max(rescaled, 0.0), 1.0) * 100.0, 1)
