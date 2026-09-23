# Disco Take-Home — Implementation Plan

> **Historical.** This is the plan written *before* building, kept deliberately
> so the reasoning is visible alongside what actually happened. Several calls
> here changed once real output existed — persona scoring dropped to three
> components, embeddings stopped being a 'cut', and viability/reach/fit-floor
> logic didn't exist yet. For the current design see
> [`architecture.md`](./architecture.md).

**Goal:** Advertiser one-liner → ranked publishers (with reasoning) → 3-5 persona-tuned creatives → structured campaign config. Explainable at every step, graceful on messy input, built in a 6-8h budget.

**Architecture:** Hybrid deterministic + LLM pipeline, split across a Python backend and a React frontend. The LLM only ever does language (extraction, narration, copywriting); a plain scoring function — not the LLM — does the actual publisher/persona ranking, because ranking has to be auditable and reproducible, and "ask the model to rank and hope" doesn't survive contact with a real catalog or a compliance review.

**Tech stack:** React + TypeScript (Vite) + shadcn/ui on the frontend. Python + FastAPI on the backend, Pydantic for schema validation and structured LLM output, the Anthropic Python SDK for the model calls. Chosen to mirror how an ad-tech company would actually split this — a Python services layer near the data/ML work, a typed React product surface on top — not just "what I know."

---

## 0. Review pass — hardening against the stated rubric

No plan *guarantees* a callback — but the brief tells you almost exactly what gets scored, so the highest-leverage thing to do is read it as a rubric and close every gap deliberately. Going through it line by line:

| Requirement (from README/GLOSSARY) | Risk if ignored | How this plan closes it |
|---|---|---|
| "A working demo... we can click through it and see it work" | Backend/frontend split can fail to boot with one command | `Makefile` (`make install`, `make dev`) + a hosted build where FastAPI serves the built React app as static files from one process — one URL, one port, no second service to keep alive |
| "The code, in a GitHub repo" | Not yet a git repo | First build step: `git init`, real incremental commits per pipeline stage — not one mega-commit. An ex-PubMatic/Yahoo reviewer reading the repo will look at commit history, not just the final diff |
| "Your prompts, in a `prompts/` directory... every prompt your system uses" | Committing *illustrative* prompts that don't match what actually runs is the single most common way this requirement gets faked, intentionally or not | Prompt templates live in `prompts/*.md` as the source of truth; `extraction.py` / `reasoning.py` / `creative.py` load and `.format()` them at runtime instead of duplicating the text as Python string literals. What's in the repo *is* what ran. |
| "Show *why* each publisher is a fit, and why some were excluded" | LLM-only ranking can't answer "why not" consistently | Named score components (§2) — exclusion reason is a lookup ("lowest-scoring component"), not a re-generation |
| "Handling messy input" | Blocking or erroring on `"idk just try it"` | Confidence tiers (§3) — pipeline always completes, never blocks |
| "Keep the README to one page... if it spills onto a second, cut something" | Writing the README first and padding it as you go | Write it *last*, after the build, against the plan doc's own cut-list (§8) — timeboxed to 0.5h so there's no room to over-write |
| Follow-up: "ask you to make a live change" | A monolithic pipeline file makes a live edit slow and risky in front of the team | Each pipeline stage is its own small, single-responsibility module (§4) — a request like "add a scoring dimension" or "change the budget floor" is a 10-line diff in one file, not a hunt |
| Follow-up: "talk through what production would look like" | Vague hand-waving under time pressure | §6 is written now, before the interview, not improvised live |

Residual risks this plan can't design away, flagged honestly:
- **Latency.** Three sequential LLM calls per run can feel slow live. Mitigate by making the reasoning and creative calls concurrent (`asyncio.gather`) since neither depends on the other's output — both only need the scores.
- **API keys.** All LLM calls happen server-side in FastAPI; the frontend never holds the Anthropic key. `.env` is gitignored, `.env.example` is committed with placeholder values. This is a real judgment call worth stating out loud in the interview, not just a hygiene checkbox.
- **Judgment quality on the deliberately ambiguous examples** (`"we help people feel better"`, `"idk just try it"`) is inherently a taste call — the eval pass (§7) exists specifically to catch outputs that are technically-valid-but-dumb before submission, by actually reading all 15 outputs, not just checking that the pipeline didn't crash.

---

## 1. Pipeline

```
Advertiser text
   │
   ▼
[1] Extraction (LLM, forced tool-call → Pydantic model)
   → AdvertiserProfile { category, subcategories, price_tier, brand_tone[],
      target_demo_signals, confidence 0-1, ambiguity_notes[] }
   │
   ▼
[2] Publisher scoring (deterministic, pure function)
   → for each of 20 publishers: { score 0-100, breakdown{category_fit,
      price_fit, audience_fit, tone_fit} }
   → sort, take top 5 as "recommended", rest as "excluded" with the
      lowest-scoring component named as the reason
   │
   ▼
[3] Persona scoring (deterministic, same shape as [2] against 10 personas)
   → top 3-5 personas
   │
   ▼
[4] Reasoning narration (LLM, grounded in [2]+[3]'s numbers)      ─┐  run
[5] Creative generation (LLM, one call per persona)                │  concurrently
   → headline + body per persona, constrained by that persona's   ─┘  (asyncio.gather)
      messaging_preferences and disinterested_in
   │
   ▼
[6] Campaign config assembly (deterministic)
   → targeting, budget allocation (score-weighted across recommended
      publishers), bid strategy (CPM/CPC/CPA pick + range), flight/pacing
   │
   ▼
CampaignConfig (Pydantic) → JSON → React UI
```

Steps 1, 4, 5 are the only LLM calls. Steps 2, 3, 6 are plain Python functions with pytest coverage — the part that has to be trustworthy is the part that isn't generative.

### Scoring formula (steps 2 & 3)

```
score = 0.40 * category_fit + 0.25 * price_fit + 0.20 * audience_fit + 0.15 * tone_fit
```

- `category_fit`: overlap between advertiser's inferred category/subcategories and the publisher's `category`/`subcategories`.
- `price_fit`: closeness between advertiser's inferred price tier midpoint and publisher `avg_order_value_usd`, normalized against the catalog's AOV range.
- `audience_fit`: age-range overlap + gender-skew alignment.
- `tone_fit`: keyword overlap between advertiser `brand_tone` and publisher `notes` free text.

**Deliberately no pandas/numpy** for this — 20 publishers and 10 personas is a handful of dicts and a `for` loop; pulling in a dataframe library for that would be adding a dependency the problem doesn't need, which cuts against the same "don't build from scratch" instinct in the other direction. Same weighting shape reused for persona scoring, swapping publisher fields for persona `category_affinities` / `price_sensitivity` / `messaging_preferences` / `disinterested_in` — the last one is a hard exclusion filter, not a negative weight.

### Handling messy input

`AdvertiserProfile.confidence` (0-1) drives UI, never pipeline branching:
- **≥ 0.7**: normal flow, no banner.
- **0.4-0.7**: normal flow, UI surfaces the inferred category as a visible assumption.
- **< 0.4** (`"idk just try it"`, `"a new kind of thing for moms"`): still produces a full campaign, but the UI leads with "Low confidence — here's my best guess" plus a re-submit affordance (no multi-turn chat — see cuts).

### Creative guardrail (de-risking the highest-risk failure mode)

Generic copy is the single biggest risk in this whole plan — it's the one output that's graded on taste, not structure, and it's invisible in a "did the pipeline run" check. Two cheap fixes instead of a bigger model or a self-critique LLM pass (which would just re-introduce the latency problem):

1. **Contrastive few-shot in `prompts/03-creative-generation.md`** — one bad/good pair baked into the prompt, not just an instruction to "be specific." See worked example below.
2. **Deterministic post-generation check**, one function, bounded to a single retry:
```python
BANNED = ["revolutionize", "game-changer", "look no further", "elevate your",
          "unlock", "in today's fast-paced world", "experience the difference"]

def needs_retry(headline: str, body: str, persona: Persona) -> bool:
    text = f"{headline} {body}".lower()
    return (any(p in text for p in BANNED)
            or any(t.replace("_", " ") in text for t in persona.disinterested_in))
```
On a hit: regenerate once with "avoid generic phrasing" appended, then accept the result either way — no loop.
3. **Move the check earlier, not just add it.** A 0.5h "prompt spike" happens right after the scoring engine (see build order), not at the eval pass — genericness needs to be caught with hours of runway left, not 30 minutes.

---

## 2. Campaign config shape

```py
class CampaignConfig(BaseModel):
    advertiser: AdvertiserProfile
    targeting: Targeting
    publishers: list[PublisherRecommendation]
    excluded_publishers: list[ExcludedPublisher]
    personas: list[PersonaMatch]
    creatives: list[Creative]
    budget: Budget
    bid_strategy: BidStrategy
    meta: RunMeta

class PublisherRecommendation(BaseModel):
    publisher_id: str
    name: str
    match_score: float                 # 0-100
    score_breakdown: ScoreBreakdown     # category_fit, price_fit, audience_fit, tone_fit
    reasoning: str
    budget_allocation_pct: float
    budget_allocation_usd: float
    suggested_bid: BidSuggestion        # model: CPM|CPC|CPA, range
```

FastAPI generates an OpenAPI schema from these Pydantic models for free. The frontend does **not** hand-duplicate the type as a parallel TS interface — it generates one from that schema (`openapi-typescript`), so the backend's Pydantic models stay the single source of truth and the FE/BE contract can't silently drift.

Budget allocation: normalize `match_score` across the top-5 recommended publishers to 100%, with a 10% floor so a decent-but-not-top fit still gets tested rather than rounding to zero. Bid model: CPM for brand/awareness language (premium/luxury tier, no urgency), CPC/CPA for performance language ("we compete on price") — a heuristic, explicitly not auction modeling, which the glossary itself says is fine.

---

## 3. File structure

```
disco/
  README.md                          # one-page submission doc
  Makefile                           # make install / make dev
  prompts/
    01-advertiser-extraction.md
    02-reasoning-narration.md
    03-creative-generation.md
  data/                               # given, unmodified
  eval/
    run_examples.py                   # runs all 15 example_advertisers.txt through the pipeline, writes eval/output.md
  backend/
    requirements.txt
    app/
      main.py                         # FastAPI app, CORS, mounts frontend/dist in prod
      routes.py                       # POST /api/campaign
      models.py                       # Pydantic: AdvertiserProfile, ScoreBreakdown, CampaignConfig, ...
      data.py                         # loaders for publishers.json / shopper_personas.json
      llm.py                          # Anthropic client + forced tool-call helper
      prompt_loader.py                # reads prompts/*.md, .format(**vars) — one function
      extraction.py                   # step 1
      scoring.py                      # steps 2 & 3, pure functions
      reasoning.py                    # step 4
      creative.py                     # step 5
      campaign.py                     # step 6
    tests/
      test_scoring.py                 # pytest — the required runnable check on the branchy logic
  frontend/
    components.json                   # shadcn config
    vite.config.ts                    # dev proxy: /api -> http://localhost:8000
    src/
      App.tsx
      types/api.ts                    # generated: npx openapi-typescript http://localhost:8000/openapi.json
      lib/api.ts                      # one fetch wrapper
      components/
        ui/                           # shadcn-generated primitives (Card, Badge, Progress, Accordion, Tabs, ...)
        AdvertiserForm.tsx
        PublisherList.tsx              # recommended + collapsible excluded, score breakdown on expand
        PersonaCards.tsx
        CreativeGrid.tsx
        CampaignConfigView.tsx
```

**Libraries doing the work instead of hand-rolled code:**
- **shadcn/ui** (Radix + Tailwind) for every UI primitive — Card, Badge, Progress (score bars), Accordion (excluded publishers, score breakdown), Tabs, Textarea, Button, Skeleton (loading), Separator. `lucide-react` (ships with shadcn) for icons. No hand-built dropdown/accordion/tooltip logic.
- **Pydantic** for validation and for generating the JSON schema handed to Anthropic's forced tool-call, instead of hand-written JSON parsing/repair.
- **Anthropic Python SDK**'s tool-use (`tool_choice={"type": "tool", ...}`) for structured output — the model is forced to return the exact shape, no regex/JSON-extraction-from-prose fallback code to write.
- **`openapi-typescript`** to generate the frontend's `types/api.ts` from FastAPI's auto-generated schema — no hand-duplicated types.
- **`FastAPI`'s `StaticFiles`** to serve the built frontend in production — no separate static file server.
- Explicitly *not* added: pandas/numpy (§1 note), a frontend state library (one page, one POST — `useState` + `fetch` is enough), react-hook-form (one textarea), a process manager like `concurrently`/`honcho` (`Makefile` + shell `&`/`wait` already does it).

---

## 4. Build order (6-8h budget)

| Block | Time | Output |
|---|---|---|
| Scaffold | 0.75h | `vite react-ts` + `shadcn init`, FastAPI skeleton, Pydantic models, Makefile, data loaders |
| Scoring engine | 1.0h | `scoring.py` + `test_scoring.py` — a clear fit and a clear exclusion, both directions |
| **Prompt spike (creative)** | **0.5h** | **hand-test `prompts/03` against 3-4 diverse advertiser/persona pairs before wiring anything else — catch generic copy while there's still runway to fix it** |
| Extraction | 1.0h | `prompts/01`, `extraction.py`, `prompt_loader.py`, confidence tiers |
| Reasoning + creative | 1.0h | `prompts/02`, `reasoning.py`, `creative.py` + `needs_retry` guardrail, run concurrently |
| Campaign assembly | 0.5h | `campaign.py` — budget split, bid heuristic |
| Frontend | 1.5h | shadcn components wired to `/api/campaign`, four sections, expand-for-breakdown |
| Eval pass | 0.5h | run all 15 examples incl. the vague ones, read every output |
| README + polish | 0.5h | one-pager, prompts/ cleanup, `git init` + real commit history if not already |
| Buffer | 0.25h | |

**Explicitly cut** (goes in the README "what I cut" section):
- Multi-turn conversational disambiguation — one re-submit affordance, not a chat loop.
- Embedding similarity for `tone_fit` — keyword match is enough at 20 publishers; named as the v2 upgrade.
- Persisted campaigns / auth / history — stateless, no database.
- Automated LLM-judge eval suite — one script over 15 labeled examples is enough signal for a take-home.
- Image creative — text only, per the glossary's own scope.

---

## 5. Running it

- **Local:** `make install && make dev` — installs `backend/requirements.txt` + `frontend` npm deps, then runs `uvicorn` (port 8000) and `vite dev` (port 5173, proxying `/api`) together via a two-line shell script, no process-manager dependency.
- **Hosted:** `npm run build` in `frontend/` → `backend/app/main.py` mounts `frontend/dist` as static files → one Python process, one port. Deployable as-is to Render/Railway/Fly (`uvicorn app.main:app`), no separate static host needed.

---

## 6. Path to production at Disco's actual scale (for the live follow-up)

The toy version swaps two JSON files for a scoring function. At 150M profiles / real publisher inventory:
- `data.py`'s in-memory JSON load → retrieval against the real shopper graph + publisher inventory — embedding similarity + graph traversal (co-purchase/cohort edges) for candidate generation, with the same kind of explicit, named-feature re-ranker on top rather than an end-to-end black box. The auditability requirement doesn't disappear at scale, it gets more load-bearing.
- One synchronous FastAPI request → offline candidate scoring (batch) + online re-rank (real-time bidding path) — you can't run graph traversal over 150M profiles inside a request.
- One eval script over 15 examples → a real offline eval set with labeled advertiser→publisher fits, regression-tested per prompt/model change.
- No caching → extraction/reasoning/creative calls get cached per advertiser fingerprint, since those are the expensive, non-deterministic part and don't need to be recomputed on every page load.
- Pydantic models at the API boundary stay the pattern — they're already how a real service would validate untrusted input and keep a typed contract with the frontend; nothing here gets thrown away going to production, it gets scaled up.
