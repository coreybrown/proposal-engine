# New-product runs: orchestration

Follow this file instead of Stages 1–5 in SKILL.md when idea.md has `mode: new-product`. SKILL.md's Setup (mode, slug, run folder, `run-state.json`) has already run.

The orchestration rules are unchanged. The agents do the work; you route inputs and outputs, and you never write artifact content yourself. The only files you write are:
- `run-state.json`
- `clarifications.md` (the user's own words, when an agent needs input)
- whatever the scripts below generate

The purpose of this mode is an **honest, accurate** answer to "is this worth building towards?" Never nudge an agent toward a friendlier conclusion, and never summarize a finding more gently than the agent wrote it.

## Before Stage 0

- **Create folders.** Add `sources/` next to `research/` in the run folder.
- **Check the uploads.** If idea.md lists "Supporting documents", confirm every listed file is in `<input-folder>/materials/`. If any are missing, tell the user before continuing.

## Every agent prompt includes

- **Mode.** That this is a **new-product** run. The ethics agent switches to its new-product section on this.
- **Paths.** The absolute path of the run folder, the exact file the agent must write, and the upstream files it must read.
- **Rules to follow.** "Follow docs/risk-contract.md and docs/new-product-contract.md. Open your file with a `## Bottom line`; end it with `KEY_FIGURES:` then `RISKS:`."
- **Questions.** The user's questions routed to that agent, taken verbatim from the Question routing table in `research/opportunity-model.md`. This applies from Stage 2 on.
- **Reading scope.** "Read only this run's folder, `<input-folder>`, and `docs/`. Never read other folders under proposals/ or inputs/."

## Launching agents and checking each stage

- **Launch in the background.** Launch every agent with `run_in_background: true`. For a parallel stage, launch all of its agents in one message.
- **Check each stage.** When a stage's agents have finished, run `python3 scripts/digest.py --check proposals/<slug> <each file the stage wrote>` from the repo root.
  - **PASS:** add the stage to `stages_done` in `run-state.json`.
  - **FAIL:** send that agent the exact failures and ask it to fix its file in place. Use SendMessage; if the agent can't be reached, relaunch it with its original prompt plus the failure list.
    - Allow one retry only.
    - If it fails again, continue and tell the user which file is non-compliant. The digest's compliance table carries that forward to the synthesizer.
  - **Missing file:** first confirm the agent is no longer running (its completion notification arrived, or it's gone from the task list). Only then relaunch it. Never run two copies of an agent against the same file.
  - **After an interruption:** a user interruption can kill background agents. Check which expected files exist before assuming anything finished.

## Stage 0: Ingest

If `<input-folder>/materials/` contains files, run:

```
python3 scripts/extract_sources.py <input-folder>/materials proposals/<slug>/sources
```

Read `sources/INDEX.md`. If files were not extracted, tell the user which ones and why (usually "export it to PDF"), then continue with the rest.

## Stage 1: Frame

Launch **opportunity-framer**, which writes `research/opportunity-model.md`. Give it:
- `idea.md`
- `sources/INDEX.md`, which leads to the extracted files, the images and any scanned PDFs
- `clarifications.md`, if it exists

**If the framer needs input.** If its Bottom line starts with `NEEDS INPUT:`:
1. Stop and ask the user exactly what it lists.
2. Write their answer, verbatim, to `proposals/<slug>/clarifications.md`.
3. Relaunch the framer.

## Stage 2: Evidence ∥

Launch all six together. Each reads `research/opportunity-model.md` and `idea.md`:

| Agent | Writes | Also reads |
|---|---|---|
| **problem-validator** | `research/problem.md` | |
| **market-sizer** | `research/market-size.md` | |
| **competitive-strategist** | `research/competition.md` | |
| **gtm-researcher** | `research/go-to-market.md` | |
| **build-cost-analyst** | `research/build-and-run.md` | `sources/`, for any technical material |
| **regulatory-scout**, pass 1 (map) | `research/regulatory.md` | `sources/`, for any legal material |

**Early exit.** After the stage check, look at the `[KILL]` flags in its output. If any file is flagged:
1. Stop and show the user each file's `KILL:` line verbatim.
2. Ask whether to stop here with a short verdict or continue the full run.
   - **Stop:** run the digest (below), then launch **new-product-synthesizer** with the instruction "early exit after Stage 2: there is no business case, economics audit or fact check."
   - **Continue:** go on to Stage 3.

## Stage 3: Business case

Launch **venture-strategist**, which writes `business-case.md`. It reads every Stage 1–2 file listed above.

## Digest

```
python3 scripts/digest.py proposals/<slug>
```

This writes `research/_digest.md`: every Bottom line, the framer's assumption and question tables, all figures side by side, the drift check and every RISKS block. If it reports drift hits, they are expected inputs to Stage 4, not errors for you to fix.

## Stage 4: Audit ∥

Launch all four together:

| Agent | Writes | Reads |
|---|---|---|
| **unit-economics-auditor** | `research/risk-economics.md` | `business-case.md`, `research/build-and-run.md`, `research/go-to-market.md`, `research/competition.md`, `research/market-size.md`, `research/opportunity-model.md`, `research/_digest.md` |
| **fact-checker** | `research/risk-fact-check.md` | `research/_digest.md`, `business-case.md`, and each owning file as needed |
| **regulatory-scout**, pass 2 (audit) | `research/risk-regulatory.md` | its own `research/regulatory.md`, `business-case.md`, `research/go-to-market.md` |
| **ethics-trust-safety** (new-product mode) | `research/risk-ethics-trust-safety.md` | the inputs listed in its New-product mode section |

## Stage 5: Synthesis

1. Run the digest again, so it includes the Stage 4 files.
2. Launch **new-product-synthesizer**. It writes `risk-register.md`, `00-summary.md` and `index.html`.
   - It reads `research/_digest.md`, `business-case.md`, `research/risk-economics.md`, `research/risk-fact-check.md` and `idea.md` in full.
   - It opens other files only to settle a disagreement.

## Wrap up

Report to the user, without pasting whole artifacts into chat:
- the verdict line
- the evidence-quality line
- the size class
- the space call
- the number of high-severity risks
- the path to `index.html`

If the verdict is **Build the MVP**, or **Validate first** where the first test is a demand test, offer the optional smoke-test page.

## Stage 6: Smoke test (only when the user asks)

Launch **smoke-test-builder**, which writes `smoke-test.html` and `research/smoke-test-manifest.md`. Then run the stage check on the manifest and give the user the path to the page.
