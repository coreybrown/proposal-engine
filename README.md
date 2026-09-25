# Proposal Engine

A self-serve proposal machine for product managers, built entirely from [Claude Code](https://code.claude.com/docs) subagents. It has two modes:

- **Existing product.** Drop in a feature idea and the product it belongs to (URL, screenshots, or both). You get back a working demo, starter artifacts, and a risk register that tells you where to dig before involving anyone else's time.
- **New product.** Drop in a net-new product idea and any documents you have. You get back an honest business case covering:
  - whether the problem is real
  - how big the market really is
  - who you'd have to beat
  - how you'd reach customers
  - what you could charge vs. what it costs to run
  - where you legally can't operate

  Every number is sourced, derived, a conservative estimate, or marked unknown, and the numbers that drive the verdict are fact-checked.

> **You run it on your own account.** This repo contains no API keys, accounts or hosted services. It's a folder of prompts, contracts and two Python scripts. When you run it, it uses *your* Claude Code login or API key, and the usage is billed to you. Read [What it costs](#what-it-costs-and-who-pays) before your first run.

## The thesis

Product management is shifting from *producing artifacts* to *orchestrating and editing them*. The scarce PM skills are taste, evaluation criteria, and knowing what to kill — not typing PRDs. This pipeline compresses the **zero-to-strawman** phase of feature development from weeks to under an hour. Humans still own **strawman-to-decision**: every artifact here is a starting point formatted for the team that owns that discipline, ending with open questions for them — never a finished deliverable.

## See an example first

[`proposals/next-on-wembley/`](proposals/next-on-wembley/) is a real new-product run on a real idea: a TV-show recommender for couples, built privately by the author for their own household.

- **Verdict: Pass.** The competitive strategist fired a kill at Stage 2, and the run stopped early by choice. So there is no business case, economics audit or fact check. The page says so.
- **The synthesis was rerun once.** After reading the first version, the author argued that manual watch-history entry was the real lead risk. That argument is in [`clarifications.md`](proposals/next-on-wembley/clarifications.md). The rerun weighed it against the evidence, agreed in part, and moved it to the top of the register. It also said where the evidence doesn't support the author.
- **Start with** [`00-summary.md`](proposals/next-on-wembley/00-summary.md), or open [`index.html`](proposals/next-on-wembley/index.html) locally in a browser. GitHub shows HTML as source, so download it or clone the repo.

It's included because it shows the pipeline doing its most useful job: saying no, with reasons.

## Quick start

**You need:**
- [Claude Code](https://code.claude.com/docs) (CLI, desktop app or IDE extension), signed in with a Claude plan or an API key. See [Who pays](#what-it-costs-and-who-pays).
- **Web search available to Claude Code.** Most research agents depend on it. It isn't available on every provider; see [Other providers](#using-other-providers-openrouter-local-and-open-models).
- **Python 3.9+** for the stage-check script:
  ```bash
  pip install -r requirements.txt
  ```
  Only `pyyaml` is required. The rest are for extracting text from uploaded PDFs, Word, PowerPoint and Excel files in new-product runs.

**Run it:**
1. Create an input. Open [`inputs/new-proposal.html`](inputs/new-proposal.html) in Chrome or Edge, fill in the form, and save the run folder into `inputs/`. Or copy [`inputs/_template/idea.md`](inputs/_template/idea.md) (feature) or [`inputs/_template/new-product-idea.md`](inputs/_template/new-product-idea.md) (new product) by hand.
2. From Claude Code, in this directory:
   ```
   /propose inputs/<your-run-folder>
   ```
3. Output lands in `proposals/<slug>/`. `.gitignore` keeps your inputs and runs out of git by default, so a public fork won't publish your ideas by accident.

The input folder looks like this:
```
inputs/<your-run-folder>/
├── idea.md              # The idea (see inputs/_template/)
├── screenshots/         # Existing product, optional: screenshots of the target product
└── materials/           # New product, optional: PDF, Word, PowerPoint, Excel, CSV, Markdown, text, images
```

## What a run produces

### Existing product (feature mode)

```
proposals/<slug>/
├── 00-summary.md        # One-page verdict: what it is, top risks, dig-here-next
├── risk-register.md     # All flagged risks, sorted by severity, with "who to ask"
├── prd.md               # Requirements, user value, metrics, experiments
├── design-spec.md       # UX approach grounded in the product's design language
├── tech-spec.md         # Build plan, effort, schemas, alternatives
├── demo.html            # Interactive prototype styled to match the product
├── research/            # Findings from context + discovery agents
└── index.html           # The proposal page tying it together
```

### New product

```
proposals/<slug>/
├── 00-summary.md        # Verdict, evidence-quality line, size class, the math, your questions answered
├── risk-register.md     # Every material risk, including numeric drift and failed fact checks
├── business-case.md     # Beachhead, positioning, price, go-to-market, MVP, staged validation plan
├── sources/             # Text extracted from your uploaded documents (claims, not evidence)
├── research/            # Framing, the six evidence files, the four audits, and _digest.md
└── index.html           # The assessment page: answer first, then the math, then the detail
```

Verdicts are **Build the MVP**, **Validate first: \<test\>**, **Pivot: \<what\>** or **Pass**.
- **Size class.** Each verdict also names what size of thing this is: venture-scale, sustainable small business, a service, a feature, or a personal tool.
- **The space.** It also says whether the space is worth building in, even if this idea isn't.

## How it works with Claude Code

There is no application code here. The whole pipeline is built from Claude Code's own extension points, and Claude Code is the runtime.

### The pieces

| Piece | Where | What it is |
|---|---|---|
| **The skill** | [`.claude/skills/propose/`](.claude/skills/propose/) | A [project skill](https://code.claude.com/docs/en/skills). Typing `/propose` loads `SKILL.md` into your main Claude Code session, which becomes the **orchestrator**. `new-product.md` sits beside it and holds the new-product stages. |
| **The agents** | [`.claude/agents/*.md`](.claude/agents/) | <!-- auto:agents_total -->27<!-- /auto --> [subagents](https://code.claude.com/docs/en/sub-agents). Each is a Markdown file: YAML frontmatter (`name`, `description`, `tools`, `model`) plus a system prompt with a **Rubric**, **Kill conditions** and an output contract. |
| **The contracts** | [`docs/`](docs/) | Shared rules every agent reads: the risk format ([`risk-contract.md`](docs/risk-contract.md)), number integrity ([`new-product-contract.md`](docs/new-product-contract.md)) and build-effort estimating ([`estimating.md`](docs/estimating.md)). |
| **The team profile** | [`docs/team/`](docs/team/) | Optional. Describe your real delivery team, and the estimating agents use it instead of defaults. It ships empty. |
| **The scripts** | [`scripts/`](scripts/) | `digest.py` checks each agent's file against the contract and builds the digest later stages read. `extract_sources.py` turns uploaded documents into text. The orchestrator runs both, not the agents. |
| **Project instructions** | [`CLAUDE.md`](CLAUDE.md) | Loaded into every session in this folder. The conventions the orchestrator follows. |

### A run, step by step

1. **You type `/propose inputs/<folder>`.** The main session loads the skill, reads `idea.md`, picks the mode from its frontmatter, and creates `proposals/<slug>/` with a `run-state.json`.
2. **The orchestrator launches each stage's subagents.** Agents in the same stage start together in one message, in the background, so they run in parallel. Each subagent gets:
   - its own fresh context window, with no memory of your conversation
   - its own system prompt from `.claude/agents/<name>.md`
   - only the tools its frontmatter lists. Research agents get `WebSearch` and `WebFetch`; writers get only `Read` and `Write`. **No agent gets a shell.**
   - a prompt naming the exact files to read and the one file to write
3. **Agents hand off through files, not conversation.** Each agent writes one Markdown file into the run folder. Only a short final report returns to the orchestrator. Downstream agents read upstream files from disk. That keeps every context window small, and it leaves a readable audit trail.
4. **A script gates every stage.** After a stage, the orchestrator runs `python3 scripts/digest.py --check`. It rejects missing Bottom lines, unlabeled numbers, malformed `KEY_FIGURES` YAML and missing `RISKS:` blocks. A failing agent gets one retry, with the exact errors.
5. **Kills stop the run early.** If any Stage 2 agent writes `KILL:` in its Bottom line, the orchestrator stops and asks you whether to finish with a short verdict or run the full pipeline. The example run stopped here.
6. **The synthesizer does no research.** It reads the digest (every Bottom line, every figure side by side, every risk) and writes the register, the verdict and the page. It surfaces disagreements between agents instead of averaging them away.

### Stages and agents

**Existing product (<!-- auto:feature_agents -->15<!-- /auto --> agents)**
<!-- table:feature -->

| Stage | Agents | Output |
|---|---|---|
| 1. Context | product-analyst, design-language-analyst | Product model + extracted design language |
| 2. Discovery | competitive-researcher, user-researcher | Market + user findings |
| 3. Definition | product-manager, then product-designer ∥ prototyper ∥ tech-architect | PRD, design spec, demo, tech spec |
| 4. Risk sweep | business-viability, legal-compliance, accessibility, ethics-trust-safety, privacy-security, operational-readiness | Findings + flagged risks |
| 5. Synthesis | synthesizer | Risk register + one-page verdict |

**New product (<!-- auto:new_product_agents -->12<!-- /auto --> agents + 2 scripts)**
<!-- table:new-product -->

| Stage | Agents | Output |
|---|---|---|
| 0. Ingest | `scripts/extract_sources.py` | Uploaded PDFs, decks, docs and sheets as text |
| 1. Frame | opportunity-framer | Segments, what must be true (A1–A8), your questions routed |
| 2. Evidence | problem-validator, market-sizer, competitive-strategist, gtm-researcher, build-cost-analyst, regulatory-scout | Problem, market, competition, channels, cost to build and serve, legal map |
| 3. Business case | venture-strategist | The best honest case, from the evidence only |
| 4. Audit | unit-economics-auditor, fact-checker, regulatory-scout, ethics-trust-safety | The math, verified figures, legal conflicts, harm |
| 5. Synthesis | new-product-synthesizer | Register, verdict, index page |
| 6. Optional | smoke-test-builder | A fake-door landing page and test protocol, on request |

Every agent reports risks in the shared format in [`docs/risk-contract.md`](docs/risk-contract.md), including explicit **license to say kill**. The register assembles from those blocks.

## What it costs, and who pays

**You pay, through your own Claude Code account.** Subagent usage bills exactly like your main session ([Claude Code costs](https://code.claude.com/docs/en/costs)):

- **Claude plan (Pro, Max, Team, Enterprise):** no per-run dollar charge. A run uses your plan's usage limits, and a full run is heavy, so a smaller plan can hit its limit mid-run. The orchestrator can resume from `run-state.json`.
- **API key (Console) or a cloud provider:** billed per token at that provider's rates, plus web-search charges where they apply. Anthropic's API currently charges $10 per 1,000 searches, and a full new-product run used about 150.
- **Check your usage** with `/usage` in Claude Code. The [costs docs](https://code.claude.com/docs/en/costs) also cover spend caps: Console workspace limits, and a `--max-budget-usd` flag.

**Measured costs** (September 2026, standard API rates, subagents only; the orchestrating session adds a little on top):

| Run | Subagent cost | Notes |
|---|---|---|
| New product, full (Stages 1–5) | about **$22**, plus about $1.50 in web searches | 13 subagent calls |
| New product, early exit after Stage 2 | less; not measured separately | Stages 3–4 are skipped. The example run is one. |
| Existing product (feature mode) | about **$45–58** | Measured with 7 of the 15 agents on Opus; the prototype is large |

Treat these as a rough guide: model prices change, and so does the length of what agents write. Measure your own first run.

### Cost levers

Most of the cost comes from which model each agent runs on, so that's the first lever. The rest are listed from biggest effect to smallest.

> **A cheaper model setup is untested.** The shipped setup, 12 agents on Opus and 15 on Sonnet, is the only one the author has checked for output quality. You can change it with levers 1 and 2 below. If you do, check the outputs yourself before trusting them. A good test: run an idea whose answer you already know on both setups and compare. Look for:
> - whether the verdict and its reasoning hold up
> - whether the synthesizer still surfaces disagreements between agents rather than averaging them away
> - whether any numbers appear without a label
> - how many files fail the stage check

| Lever | How | Effect | Trade-off |
|---|---|---|---|
| **1. Run everything on Sonnet** | `export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-sonnet-5` before starting Claude Code. Every agent with `model: opus` then resolves to Sonnet, with no file edits. | The biggest cut, largest in feature mode | **Untested; check the outputs** (see the note above). The synthesizers, the prototyper and the unit-economics auditor do the hardest judgment work, so they're the most likely to lose quality. |
| **2. Move selected agents to Sonnet** | Change `model: opus` to `model: sonnet` in individual `.claude/agents/*.md` files. The <!-- auto:opus_count -->12<!-- /auto --> Opus agents are listed below. | A partial cut, at your choosing | A middle path: keep the synthesizers on Opus and move the framers and writers first. **Also untested; check the outputs.** |
| **3. Take the early exit** | When a Stage 2 agent fires a kill, choose "stop" when asked | Skips the business case and all four audits | No business case, economics audit or fact check. The verdict can only be Pass or Validate first. |
| **4. Choose the mode deliberately** | New-product mode costs about half as much as feature mode | Roughly halves the cost | A different product: no demo or specs |
| **5. Skip the optional stage** | Stage 6 (smoke test) only runs if you ask | Avoids one agent call | None |
| **6. Avoid reruns** | Fill in `idea.md` fully; "Questions to answer" routes work to the right agent. Each failed stage check costs one retry, and each synthesis rerun is a full synthesizer call. | Avoids repeat calls | None |
| **7. Cap thinking** | Use `/effort`, or `MAX_THINKING_TOKENS` on models with fixed thinking budgets ([model config](https://code.claude.com/docs/en/model-config)) | A modest cut | Shallower reasoning |
| **8. Orchestrate on a cheaper model** | Set the main session's model with `/model`. Orchestration is light routing, and subagents keep their own `model:`. | Small | Minimal |

**Which agents run on which model** (the `model:` line in each agent file):
<!-- auto:model-list -->
- **Opus (12):** build-cost-analyst, design-language-analyst, new-product-synthesizer, opportunity-framer, product-analyst, product-designer, product-manager, prototyper, synthesizer, tech-architect, unit-economics-auditor, venture-strategist
- **Sonnet (15):** accessibility, business-viability, competitive-researcher, competitive-strategist, ethics-trust-safety, fact-checker, gtm-researcher, legal-compliance, market-sizer, operational-readiness, privacy-security, problem-validator, regulatory-scout, smoke-test-builder, user-researcher
<!-- /auto:model-list -->

**How model selection works.** For each subagent call, Claude Code applies the first of these that is set ([subagent docs](https://code.claude.com/docs/en/sub-agents)):
1. a model named in the orchestrator's call
2. the agent's own `model:` frontmatter
3. `CLAUDE_CODE_SUBAGENT_MODEL`
4. the main session's model

Every agent here sets `model:`, so `CLAUDE_CODE_SUBAGENT_MODEL` has no effect. Use lever 1 or lever 2 instead. The aliases `opus`, `sonnet` and `haiku` resolve through `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_HAIKU_MODEL` ([model config](https://code.claude.com/docs/en/model-config)).

## Using other providers: OpenRouter, local and open models

Claude Code can send its requests to a different endpoint, so you can run this pipeline through OpenRouter, a gateway such as LiteLLM, or a local model server. **Read the caveats first.** They matter more for this pipeline than for everyday coding.

### Caveats

- **Anthropic doesn't support non-Claude models in Claude Code.** Routing through a gateway is documented ([LLM gateways](https://code.claude.com/docs/en/llm-gateway-connect)). Sending Claude Code's requests to non-Claude models isn't supported, and tool use may be unreliable.
- **Web search will probably stop working.** `WebSearch` is an Anthropic server-side tool. It isn't available on Amazon Bedrock, and through a third-party gateway it only works if the gateway implements Anthropic's web-search API. Without it:
  - <!-- auto:websearch_count -->17<!-- /auto --> of the <!-- auto:agents_total -->27<!-- /auto --> agents lose their main way of finding evidence. `WebFetch` still works, but only on URLs the agent already knows.
  - Under the number-integrity rules, unfound evidence becomes `unknown`. Verdicts get weaker, not wrong, but they will be much less useful.
  - **Workaround:** add a search tool through an [MCP server](https://code.claude.com/docs/en/mcp), and add its tool name (`mcp__<server>__<tool>`) to the `tools:` line of each research agent. Some gateways, such as LiteLLM, can also intercept web search themselves.
- **Smaller models struggle with the contracts.** The pipeline relies on agents following long, strict output formats: YAML figures, labelled numbers and risk blocks. Expect more failed stage checks. The one retry per agent won't always rescue them.
- **Map all three aliases.** Agents ask for `opus` or `sonnet`, and Claude Code uses the `haiku` alias for background tasks such as summarising web pages. Set all three to models your endpoint serves.

### OpenRouter

OpenRouter documents a Claude Code setup: [OpenRouter's Claude Code guide](https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration). In outline:

```bash
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="<your OpenRouter key>"
export ANTHROPIC_API_KEY=""   # must be empty so it doesn't override the token

# Map the aliases the agents use to OpenRouter model slugs:
export ANTHROPIC_DEFAULT_OPUS_MODEL="<model slug>"
export ANTHROPIC_DEFAULT_SONNET_MODEL="<model slug>"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="<model slug>"
```

Then start Claude Code in this folder. Billing goes to your OpenRouter account. Check OpenRouter's guide for the current details; third-party setups change.

### Local and open models

Two common routes, neither maintained by Anthropic:
- **Ollama.** Recent versions serve an Anthropic-compatible API. Point `ANTHROPIC_BASE_URL` at your Ollama server (by default `http://localhost:11434`) and map the three aliases to local model names. See Ollama's docs for the exact setup.
- **LiteLLM proxy.** Run [LiteLLM](https://docs.litellm.ai/) in front of any model provider, and point `ANTHROPIC_BASE_URL` at the proxy. Claude Code's [LLM gateway docs](https://code.claude.com/docs/en/llm-gateway-connect) cover gateway requirements.

A local model costs nothing per token. Expect a much weaker run, though: without web search, most agents can't find evidence, and small models often break the output contracts. Run one new-product idea you already know the answer to before trusting it.

## Customizing

- **Tune an agent:** edit its file in `.claude/agents/`. Keep the three load-bearing sections: **Rubric**, **Kill conditions** and the risk-contract output requirement. `CLAUDE.md` lists which rules are duplicated across files and must be changed together.
- **Describe your real team:** fill in `docs/team/`. The estimating agents then size work for your team instead of a default scrum team.
- **Change what the stage check enforces:** see `scripts/digest.py`, with tests in `scripts/test_digest.py` (`python3 scripts/test_digest.py`).

## What's opinionated here (vs. stock agent definitions)

Agent scaffolding is a commodity — anyone can prompt six personas. The judgment layer in this repo is:

1. **Rubrics** — each agent has an explicit definition of *done* and of what lazy output looks like.
2. **Kill conditions** — every agent is licensed (and instructed) to return negative verdicts. A pipeline that never says "don't build this" is a toy.
3. **Handoff contracts** — artifacts end with *open questions for the owning team*, because these are inputs to design/eng/legal collaboration, not replacements for it.
4. **Orchestration decisions** — what runs parallel, what gates what, why the red-team sweep audits the artifacts rather than the idea, and how disagreements between agents surface in the summary rather than getting averaged away.
5. **Number integrity (new-product mode)** — see [docs/new-product-contract.md](docs/new-product-contract.md).
   - Every figure is sourced, derived, a conservative estimate, or unknown.
   - The conservative case drives the verdict, and there is no upside case.
   - A script rejects unlabeled numbers, a drift check catches the business case inflating the evidence, and a fact-checker re-fetches the sources behind every number the verdict depends on.
   - The economics are computed by the skeptic, not the advocate.

## Limits

- **Not advice.** The regulatory agents are issue-spotters, not lawyers. The economics are estimates with their sources shown.
- **Artifacts are starting points.** Every file ends with open questions for the team that owns it.
- **Web research depends on what's publicly reachable.** Many pricing pages block automated fetches, and the agents say so when that happens.

## License

[MIT](LICENSE). Fork it, change it, use it on your own account.
