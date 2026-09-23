"""Runs every advertiser in data/example_advertisers.txt through the real
pipeline and writes a readable report to eval/output.md.

This is the cheapest possible eval: no LLM judge, no scoring rubric, no
framework. It exists so a human reads all 15 outputs before submitting,
because the failure mode that matters here - plausible-but-bad copy, a
confident campaign for an advertiser this catalog can't serve - is invisible
to any assertion and obvious to a human in about ten seconds.

    cd backend && . .venv/bin/activate && python ../eval/run_examples.py
"""

import asyncio
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "backend"))

from dotenv import load_dotenv  # noqa: E402

load_dotenv(REPO_ROOT / "backend" / ".env")

from app.models import CampaignConfig  # noqa: E402
from app.pipeline import run_pipeline  # noqa: E402

EXAMPLES_FILE = REPO_ROOT / "data" / "example_advertisers.txt"
OUTPUT_FILE = REPO_ROOT / "eval" / "output.md"
CONCURRENCY = 3  # keep clear of provider rate limits


def load_examples() -> list[tuple[int, str]]:
    """The file is a numbered list with comment and separator lines."""
    examples = []
    for line in EXAMPLES_FILE.read_text().splitlines():
        match = re.match(r"^(\d+)\.\s+(.*)", line.strip())
        if match:
            examples.append((int(match.group(1)), match.group(2).strip()))
    return examples


def render(index: int, description: str, campaign: CampaignConfig) -> str:
    a = campaign.advertiser
    v = campaign.viability
    persona_names = {p.persona_id: p.name for p in campaign.personas}

    lines = [
        f"## {index}. {description}",
        "",
        f"**Viability:** `{v.status}` - {v.headline}",
        "",
        f"**Extracted:** `{a.inferred_category}` / {', '.join(a.inferred_subcategories) or '-'} "
        f"| {a.price_tier} | tone: {', '.join(a.brand_tone) or '-'} | confidence **{a.confidence:.2f}**",
        "",
    ]
    if a.ambiguity_notes:
        lines += ["**Ambiguity:** " + "; ".join(a.ambiguity_notes), ""]

    lines += ["**Publishers**", "", "| score | publisher | budget | bid | inventory used | why |", "|--:|---|--:|---|--:|---|"]
    for p in campaign.publishers:
        lines.append(
            f"| {p.match_score:.0f} | {p.name} | ${p.budget_allocation_usd:,.0f} "
            f"({p.budget_allocation_pct:.0f}%) | {p.suggested_bid_model} "
            f"${p.suggested_bid_range[0]:.2f}-${p.suggested_bid_range[1]:.2f} | "
            f"{p.inventory_share_pct:.1f}% | {p.reasoning} |"
        )

    lines += ["", "**Excluded (bottom 3)**", ""]
    for e in campaign.excluded_publishers[-3:]:
        lines.append(f"- *{e.name}* ({e.score:.0f}) - {e.reason}")

    lines += ["", "**Personas**", ""]
    for p in campaign.personas:
        lines.append(f"- **{p.name}** ({p.fit_score:.0f}, {p.fit_label}) - {p.reasoning}")

    lines += ["", "**Creative**", ""]
    for c in campaign.creatives:
        lines += [
            f"- *{persona_names.get(c.persona_id, c.persona_id)}*",
            f"  - **{c.headline}**",
            f"  - {c.body}",
        ]

    lines += ["", "---", ""]
    return "\n".join(lines)


async def run_one(sem: asyncio.Semaphore, index: int, description: str) -> str:
    async with sem:
        print(f"  [{index:>2}] {description[:60]}...", flush=True)
        try:
            campaign = await run_pipeline(description)
            return render(index, description, campaign)
        except Exception as exc:  # noqa: BLE001 - a failed example is a result, not a crash
            return f"## {index}. {description}\n\n**FAILED:** `{type(exc).__name__}: {exc}`\n\n---\n"


async def main() -> None:
    examples = load_examples()
    print(f"Running {len(examples)} advertisers through the pipeline...")
    sem = asyncio.Semaphore(CONCURRENCY)
    sections = await asyncio.gather(*(run_one(sem, i, d) for i, d in examples))

    OUTPUT_FILE.write_text(
        "# Eval output\n\n"
        f"All {len(examples)} advertisers from `data/example_advertisers.txt`, "
        "run through the live pipeline.\n\n---\n\n" + "\n".join(sections)
    )
    print(f"\nWrote {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
