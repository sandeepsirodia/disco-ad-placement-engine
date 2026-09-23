"""Embedding similarity for the two soft signals (tone, messaging).

Keyword matching handles the hard signals fine - category vocabulary is a
closed set, so string equality is exactly right there. It fails on the soft
ones, which are free prose on both sides: a sustainable activewear brand
scored The Fitness Enthusiast "weak" because the brand's tone ("sustainable",
"eco-conscious") shares no literal token with that persona's messaging
preferences ("performance claims", "technical fabrics"). Semantically a
strong match; lexically invisible.

Texts are embedded in ONE batched request per run and cached for the process.
The first version issued a call per string - ~31 on a cold start, which
tripped the provider's per-minute limit in production and silently fell back
to keywords, so the deployed demo scored every tone_fit at 0 while local runs
(with a warm cache) looked fine. The OpenAI embeddings API accepts a list;
this always should have been one call.
"""

from __future__ import annotations

import logging
import math
import os

from app.llm import client_or_none

DEFAULT_EMBED_MODEL = "gemini-embedding-001"
logger = logging.getLogger(__name__)

_cache: dict[str, tuple[float, ...]] = {}
_unavailable = False  # sticky: stop retrying a provider that can't embed


def _embed_model() -> str:
    return os.environ.get("LLM_EMBED_MODEL", DEFAULT_EMBED_MODEL)


def prime(texts: list[str]) -> None:
    """Embed everything not already cached, in one request."""
    global _unavailable
    if _unavailable:
        return

    pending = sorted({t.strip() for t in texts if t and t.strip()} - _cache.keys())
    if not pending:
        return

    client = client_or_none()
    if client is None:
        _unavailable = True
        return

    try:
        response = client.embeddings.create(model=_embed_model(), input=pending)
    except Exception as exc:  # noqa: BLE001 - degrade to keywords, but say so
        # Loudly: a silent fallback here is exactly what hid this in production.
        logger.warning(
            "Embeddings unavailable (%s: %s) - tone/messaging fit will fall back to "
            "keyword matching, which scores most pairs at 0.",
            type(exc).__name__,
            exc,
        )
        _unavailable = True
        return

    for text, item in zip(pending, response.data):
        _cache[text] = tuple(item.embedding)


def _cosine(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm = math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b))
    return dot / norm if norm else 0.0


def similarity(left: str, right: str) -> float | None:
    """0-100 similarity, or None if embeddings aren't available."""
    a, b = _cache.get(left.strip()), _cache.get(right.strip())
    if a is None or b is None:
        return None
    # Cosine over these models sits roughly in 0.3-0.95 for related prose;
    # rescale so the usable band spans 0-100 instead of compressing every real
    # signal into the top third.
    rescaled = (_cosine(a, b) - 0.3) / 0.6
    return round(min(max(rescaled, 0.0), 1.0) * 100.0, 1)
