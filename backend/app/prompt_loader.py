"""Loads prompts/*.md at runtime, so the committed files ARE what runs, not a
paraphrase of it (docs/plan.md §0 - this is what "every prompt your system
uses, in prompts/" is supposed to mean)."""

from functools import lru_cache
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parents[2] / "prompts"


@lru_cache
def load_prompt(filename: str) -> tuple[str, str]:
    """Returns (system, user_template) parsed from a file with '## System'
    and '## User Template' section headers."""
    text = (PROMPTS_DIR / filename).read_text()
    _, _, after_system = text.partition("## System")
    system, _, after_template = after_system.partition("## User Template")
    return system.strip(), after_template.strip()
