"""Per-IP rate limit for the hosted demo.

A public URL with an LLM behind it and no auth is a quota-drain waiting to
happen, and the failure lands exactly where it hurts: the key dies mid-review
and the demo looks broken. Stdlib only - a dict of recent timestamps is
enough at demo scale, and a real deployment would put this at the edge
(Cloudflare, an API gateway) rather than in process memory.
"""

import os
import time
from collections import defaultdict

from fastapi import HTTPException, Request

# Generous for a human clicking through a demo, ruinous for a script.
MAX_REQUESTS = int(os.environ.get("RATE_LIMIT_REQUESTS", "20"))
WINDOW_SECONDS = int(os.environ.get("RATE_LIMIT_WINDOW_SECONDS", "3600"))

_hits: dict[str, list[float]] = defaultdict(list)


def enforce_rate_limit(request: Request) -> None:
    """FastAPI dependency. Disabled entirely when RATE_LIMIT_REQUESTS=0."""
    if MAX_REQUESTS <= 0:
        return

    # Render/Railway/Fly all sit behind a proxy, so request.client.host is the
    # proxy - the real caller is the first hop in X-Forwarded-For.
    forwarded = request.headers.get("x-forwarded-for", "")
    caller = forwarded.split(",")[0].strip() or (request.client.host if request.client else "unknown")

    now = time.monotonic()
    recent = [t for t in _hits[caller] if now - t < WINDOW_SECONDS]
    _hits[caller] = recent

    if len(recent) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail=(
                f"Rate limit reached ({MAX_REQUESTS} campaigns per hour). "
                "This is a demo deployment on a shared key - run it locally with your own "
                "key for unlimited use (see README)."
            ),
        )
    _hits[caller].append(now)
