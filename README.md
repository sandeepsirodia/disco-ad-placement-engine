# Ad Placement Engine

An advertiser describes their business in a sentence. The system returns ranked publishers with per-component reasoning, 3–5 persona-tuned creative variants, and a launchable campaign config — with every number traceable back to how it was computed.

## Run it

You'll need your own Gemini API key — free, instant, no billing setup: **https://aistudio.google.com/apikey**

```bash
cp backend/env.sample backend/.env    # paste your key on the LLM_API_KEY line
make install
make dev                              # backend :8000, frontend :5173
```

`make test` runs the scoring suite. `make types` regenerates the frontend's TypeScript types from the backend's Pydantic models.

The key stays server-side: `backend/.env` is gitignored, every model call happens in FastAPI, and the React bundle contains no key handling of any kind. Swapping providers (OpenAI, Groq, a local Ollama) is three env vars in that same file — `app/llm.py` doesn't change.

**Stack:** React + TypeScript + shadcn/ui · Python + FastAPI + Pydantic · any OpenAI-compatible LLM (defaults to Gemini; switching providers is three env vars, not a code change).

## The one architectural decision everything else follows from

**The LLM does language. A plain scoring function does ranking.** Three LLM calls per run — extraction (text → structured profile), narration (scores → prose), creative (persona → copy). Ranking, budget allocation, and bid selection are deterministic Python with unit tests.

This isn't purity. It's that "why was this publisher excluded?" has to be answerable the same way twice. With named score components (`category_fit`, `price_fit`, `audience_fit`, `tone_fit`), the exclusion reason is a lookup — the lowest-scoring component — not a re-generation that might say something different on the second ask. The narration LLM is handed real computed numbers and explains them; it never invents one.

## What's genuinely hard here

**Easy:** calling an LLM, JSON-shaped output (Pydantic + the SDK's structured-output mode removes all parsing code), rendering the results.

**Hard, and where the real work went:**

1. **Two taxonomies that don't share a vocabulary.** The model extracts free text; the catalog uses fixed labels. It returned `household_goods` for a cleaning brand while the right publishers sat under `home` and `groceries`, and `activewear` for a brand the catalog files under `apparel`. Fuzzy string matching can't bridge that. The fix was to stop matching free text at all: extraction now *selects from the catalog's own vocabulary* (`data.catalog_vocabulary()`), and scoring matches only on those terms.

2. **Irrelevant publishers scoring 36/100.** `price_fit` and a neutral `audience_fit` default paid out ~36 points to publishers with zero category overlap — a sock retailer looked "close on AOV" to a dental SaaS. Price and audience proximity are only meaningful *conditional* on category relevance, so category now gates the composite (`_relevance_gate`). Off-topic advertisers dropped from 36 to 6.

3. **Fit and viability are different axes.** *"B2B SaaS for dental practices"* is a high-confidence extraction with zero viable inventory. Confidence measures whether we understood the input; viability measures whether this catalog can serve it. Conflating them tells a vague-but-servable advertiser ("a new kind of thing for moms") that it's in the wrong market. They're now separate, with separate messaging.

4. **Reach is a constraint, not a tiebreaker.** Fit alone would put 45% of budget on a publisher with 4.8M monthly impressions. Allocation is capped at 20% of deliverable inventory and redistributed (`cap_by_inventory`).

5. **Weak personas make the model lie.** Asked for copy for a persona that doesn't fit, it invents product attributes to bridge the gap — a dog food brand got copy claiming published sourcing data and carbon-minimized shipping, neither stated by the advertiser. That's a compliance problem, not a style one. Fixed at both ends: a fit floor before a persona is selected, and an explicit no-fabrication rule in the prompt.

Every one of these was found by running all 15 sample advertisers (`eval/run_examples.py` → `eval/output.md`), not by reasoning about the code. Four of the five are invisible on the happy-path example.

## Campaign config shape

Defined once as Pydantic models; the frontend's types are generated from the resulting OpenAPI schema, so the contract can't drift. Beyond the obvious fields, it carries `viability` (can this catalog serve them at all), per-publisher `score_breakdown` (why this rank), `inventory_share_pct` (is this spend deliverable), and `fit_label` per persona (so a weak-but-included persona is visibly weak rather than sitting next to a strong one looking equally endorsed).

## What I cut

- **Multi-turn disambiguation** — low-confidence input gets one clear "add detail and re-run" prompt, not a chat loop.
- **Persistence, auth, an LLM-judge eval suite, image creative** — none change what the prototype demonstrates.

## Where the two matching strategies split

Category matching is a **closed set**, so string equality is exactly right — and constraining extraction to the catalog's vocabulary is what makes it work. Tone and messaging are **free prose on both sides**, where literal overlap is the wrong tool entirely: "sustainable" and "eco-motivated buyers" are the same claim with zero shared tokens. Those two signals use embedding similarity (`app/semantic.py`), cached per catalog string since the catalog is static, and falling back to keywords if a provider doesn't serve `/embeddings`.

Measured effect: The Fitness Enthusiast against a sustainable activewear brand moved from `weak · 28` to `moderate · 34`, and genuinely good publisher matches rose across the board (Movewell 80 → 86, Cloudfoot 72 → 81) **while off-topic advertisers stayed pinned at 6–18** — the category gate still does its job, which is the property that mattered.

## Next week

1. **Use the embeddings for retrieval, not just scoring.** They currently re-rank 20 rows in a loop. The same vectors are what candidate generation over a 150M-profile graph would run on — ANN retrieval first, then this exact named-feature re-ranker on top. The shape is already right; only the retrieval step is missing.
2. **A labeled eval set with regression runs per prompt change.** The current script prints 15 outputs for a human to read; it doesn't fail a build. That's the right next investment — every bug above would have been caught earlier by it.
3. **Persist the extraction to make rankings genuinely reproducible.** Extraction runs at `temperature=0`, which narrows run-to-run variance but does not remove it — the same advertiser can still yield a slightly different catalog-term set and therefore a different ranking. For an auditable ad system that's not good enough, and no temperature setting fixes it: reproducibility comes from *storing* the extracted profile against the input and re-scoring from the stored copy, not from hoping the model repeats itself. Same change also cuts the ~18s latency on repeat runs.
4. **Calibrate the weights against outcomes instead of judgment.** `PUBLISHER_WEIGHTS` is currently four numbers I chose. With click/conversion data they should be fit, and the deterministic scorer is exactly the right shape to fit them in.
