---
name: propose
description: Run the proposal pipeline on an idea. Takes a path to an input folder (containing idea.md plus optional screenshots/ or materials/) and produces a package under proposals/<slug>/. Feature runs (an idea for an existing product) get a demo, PRD, design spec, tech spec, risk register and one-page verdict. New-product runs (idea.md frontmatter `mode: new-product`) get a business case, audited unit economics, fact-checked figures, a risk register and a verdict on whether the product is worth building. Use when the user says "run a proposal", "/propose <path>", or wants to evaluate a feature idea or a new product idea.
---

# Propose — pipeline orchestration

You are orchestrating the proposal pipeline. Follow the stages in order. Stages marked ∥ run their agents in parallel (launch in a single message). Do not skip stages, do not merge stages, and do not write artifact content yourself — the agents do the work; you route inputs and outputs.

There are two modes. **Feature** runs follow Stages 1–5 below. **New-product** runs follow [new-product.md](new-product.md) instead of Stages 1–5. Setup decides which.

## Setup

1. Read `<input-folder>/idea.md` (missing → stop and ask the user). **Determine the mode before checking anything else:**
   - **New product.** Frontmatter `mode: new-product` means a new-product run. Finish steps 2–3 of this Setup, then read [new-product.md](new-product.md) and follow it **instead of** Stages 1–5 below.
   - **Feature.** Frontmatter `mode: feature`, or no frontmatter with a real product named under "Target product", means a feature run. Everything below applies unchanged.
   - **Unclear.** If there's no frontmatter and the target product is blank, "none", or a toolkit or platform rather than a product (e.g. "LiveKit or Pipecat"), ask the user whether this is a feature for an existing product or a new product before going further.
2. **Check the required fields for the mode.** A feature run needs what the feature is and what product it's for. A new-product run needs only the idea. If anything required is missing, stop and ask the user.
3. **Choose the slug and create the run directory.**
   - **Slug.** For a feature run, derive a short kebab-case slug from the idea (e.g. `strava-route-stories`). For a new-product run, use the input folder's name.
   - **Existing folder, finished.** If `proposals/<slug>/` has a `00-summary.md`, use the next free suffix (`<slug>-2`, `-3`, …). Never overwrite a finished run.
   - **Existing folder, unfinished.** If it has no `00-summary.md`, ask the user whether to resume it or start a new run.
     - To resume, read its `run-state.json` and continue from the first stage whose outputs are missing or failed.
     - To start new, use the next free suffix.
   - **Create it.** Make `proposals/<slug>/` with `research/` inside, and write `run-state.json`:
     ```json
     {"mode": "feature" | "new-product", "input": "<input-folder>", "slug": "<slug>", "stages_done": []}
     ```
     Append each stage's name to `stages_done` when the stage completes.
4. **Feature runs only.** Note the target product URL and any screenshots in `<input-folder>/screenshots/`. Pass these paths to the context agents verbatim.

Every agent prompt must include:
- The absolute path to the run directory and the exact file it must write
- The paths of the upstream findings files it must read
- A reminder: "Follow docs/risk-contract.md — end your output file with a RISKS: block."

## Stage 1 — Context ∥

Launch together:
- **product-analyst** → writes `research/product-model.md`
- **design-language-analyst** → writes `research/design-language.md`

Wait for both. If the product-analyst reports it could not build a credible product model (inaccessible URL, unusable screenshots), stop and tell the user what's missing — everything downstream would be poisoned.

## Stage 2 — Discovery ∥

Launch together, each given `research/product-model.md`:
- **competitive-researcher** → writes `research/competitive.md`
- **user-researcher** → writes `research/user-research.md`

## Stage 3 — Definition

1. **product-manager** (reads all four research files) → writes `prd.md`. Runs alone first — the other three consume the PRD.
2. Then launch together, each given the PRD + the relevant research files:
   - **product-designer** (+ design-language.md) → writes `design-spec.md`
   - **prototyper** (+ design-language.md, design-spec is NOT ready yet — it works from PRD + design language directly) → writes `demo.html`
   - **tech-architect** → writes `tech-spec.md`

## Stage 4 — Risk sweep ∥

Launch all six together. Each reads the stage-3 artifacts plus the research files and writes findings to `research/risk-<name>.md`:
- **business-viability**, **legal-compliance**, **accessibility** (must also read `demo.html`), **ethics-trust-safety**, **privacy-security**, **operational-readiness**

## Stage 5 — Synthesis

Launch **synthesizer** with the full run directory. It writes:
- `risk-register.md` — every RISKS block merged, deduped, sorted by severity
- `00-summary.md` — the one-page verdict
- `index.html` — the proposal page (summary at top, demo embedded via iframe, links to artifacts)

## Wrap up

Report to the user: the verdict line from `00-summary.md`, the count of high-severity risks, and the path to `index.html`. Do not paste whole artifacts into chat.
