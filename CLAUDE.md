# Proposal Engine — project instructions

This repo is a multi-agent pipeline with two modes, both run via `/propose`:

- **Feature** (the default): a feature idea plus a target product become a proposal package: demo, PRD, design spec, tech spec, risk register and one-page verdict.
- **New product** (`mode: new-product` in idea.md's frontmatter): a net-new product idea, plus any uploaded documents, becomes a business case, audited unit economics, fact-checked figures, a risk register and a verdict on whether it's worth building.

## Conventions

- The pipeline is run via the `/propose` skill. Do not run agents ad hoc unless debugging a single agent.
- Every agent's output MUST end with a `RISKS:` block per [docs/risk-contract.md](docs/risk-contract.md). No risks found → `RISKS: none identified` with one sentence on what was checked.
- All run outputs go to `proposals/<slug>/`. Never write run outputs elsewhere. Research findings go to `proposals/<slug>/research/`.
- Artifacts are starting points for human teams, not final deliverables. Each artifact ends with an **Open questions for <owning team>** section (in new-product runs: **for the decision-maker**).
- Agents must ground claims in evidence (the target site, screenshots, web research) and say so when they can't. Fabricated specifics are worse than stated uncertainty.
- Negative verdicts are valued output. "Kill this" or "nothing interesting found" are acceptable, complete answers when the rubric supports them.
- **Build-effort estimates follow [docs/estimating.md](docs/estimating.md)** in both modes (tech-architect, build-cost-analyst). That means tasks tagged by complexity and AI leverage, and two tracks, Team (the default scrum team) and Solo, each shown AI-leveraged, AI-typical (the suggested estimate) and traditional, using the real team whenever the inputs describe it. Waits are kept separate, and worst cases are never added together.
- **New-product agents also follow [docs/new-product-contract.md](docs/new-product-contract.md).** Its number-integrity rule governs that mode:
  - every figure is sourced, derived, a conservative estimate, or unknown
  - the conservative case is the headline
  - there is no upside case
  - `scripts/digest.py --check` enforces these rules after every stage

## Stage order (enforced by /propose)

### Feature

1. Context: product-analyst ∥ design-language-analyst — everything downstream reads these
2. Discovery: competitive-researcher ∥ user-researcher
3. Definition: product-manager (PRD) → then product-designer ∥ prototyper ∥ tech-architect
4. Risk sweep (audits stage-3 artifacts): business-viability ∥ legal-compliance ∥ accessibility ∥ ethics-trust-safety ∥ privacy-security ∥ operational-readiness
5. Synthesis: synthesizer (risk register + 00-summary.md + index.html)

### New product (details in [.claude/skills/propose/new-product.md](.claude/skills/propose/new-product.md))

0. Ingest: `scripts/extract_sources.py` turns uploaded documents in `inputs/<slug>/materials/` into `sources/`
1. Frame: opportunity-framer
2. Evidence: problem-validator ∥ market-sizer ∥ competitive-strategist ∥ gtm-researcher ∥ build-cost-analyst ∥ regulatory-scout (map)
3. Business case: venture-strategist, written only from the Stage 1–2 evidence
4. Audit: unit-economics-auditor ∥ fact-checker ∥ regulatory-scout (audit) ∥ ethics-trust-safety. These read `research/_digest.md`, built by `scripts/digest.py`.
5. Synthesis: new-product-synthesizer (risk register, 00-summary.md, index.html)
6. Optional, on request: smoke-test-builder

## Editing agents

Agent definitions live in `.claude/agents/`. When tuning, preserve the three load-bearing sections: **Rubric**, **Kill conditions**, and the risk-contract output requirement.

- **Duplicated triage rules.** The register triage rules (Output 1) appear in both `synthesizer.md` and `new-product-synthesizer.md`. Tune both together.
- **Shared ethics agent.** `ethics-trust-safety.md` serves both modes. Its "New-product mode" section overrides its inputs and owners for new-product runs.
- **Contract scope.** `docs/risk-contract.md` is read by every agent in both modes. Keep new-product-only rules in `docs/new-product-contract.md`.
- **Team profile.** `docs/team/` holds the real delivery team's profile and one standards file per role. The team owns and fills it; it ships empty (`status: empty`), and agents then fall back to defaults. When you add or rename an agent, update the role-to-agent table in `docs/team/README.md` §7.
