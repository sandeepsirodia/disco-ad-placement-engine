"""Provider-agnostic LLM access.

"Agnostic" here means: use the interface most providers already speak,
instead of writing an adapter layer to make Claude/Gemini/etc look alike.
The OpenAI SDK's chat.completions API is that interface - Gemini, Groq,
Mistral, DeepSeek, local Ollama, and OpenAI itself all implement it. Switching
providers is a base_url/api_key/model/embed_model change (four env vars, see
backend/env.sample), not a rewrite. If a provider without OpenAI compatibility
is ever needed, only this file and semantic.py change - every caller goes
through generate_structured/generate_text/similarity.
"""

from __future__ import annotations

import os
from functools import lru_cache

from openai import OpenAI
from pydantic import BaseModel

DEFAULT_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
DEFAULT_MODEL = "gemini-flash-latest"


@lru_cache
def _client() -> OpenAI:
    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        raise RuntimeError(
            "LLM_API_KEY is not set. Copy backend/env.sample to backend/.env "
            "and add your key (see README for where to get a Gemini key)."
        )
    return OpenAI(api_key=api_key, base_url=os.environ.get("LLM_BASE_URL", DEFAULT_BASE_URL))


def client_or_none() -> OpenAI | None:
    """For optional paths (embeddings) that degrade rather than fail."""
    try:
        return _client()
    except RuntimeError:
        return None


def _model() -> str:
    return os.environ.get("LLM_MODEL", DEFAULT_MODEL)


def generate_structured[T: BaseModel](system: str, user: str, schema: type[T], temperature: float = 0.0) -> T:
    """One LLM call, forced into `schema`'s shape via the SDK's structured
    output support - no hand-written JSON parsing or repair.

    `temperature` defaults to 0 because most calls here feed the deterministic
    scorer: if extraction picks different catalog terms on two runs, the same
    advertiser gets a different ranking, and the audit trail the whole design
    exists to provide is worthless. Creative generation opts back into warmth -
    that's the one call where variation is the point.
    """
    completion = _client().beta.chat.completions.parse(
        model=_model(),
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        response_format=schema,
        temperature=temperature,
    )
    parsed = completion.choices[0].message.parsed
    if parsed is None:
        raise ValueError(f"Model refused or returned unparseable output: {completion.choices[0].message.content!r}")
    return parsed
