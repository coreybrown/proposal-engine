# Estimating build effort

Every agent that estimates build effort follows this file: tech-architect in feature runs, build-cost-analyst in new-product runs. Any other agent that quotes effort cites those numbers and never re-derives them.

The failure this prevents is an estimate that nobody can check and that runs high for work that isn't complex. That happens in four ways:
- effort with no team behind it
- every task priced as hand-written code
- every task's worst case added together
- waiting on lawyers or vendors counted as engineering time

---

## 1. Four dimensions

An estimate varies along four dimensions. Keep them separate so a reader can see which one moves the number.

| Dimension | What it changes | Where it shows up |
|---|---|---|
| **Complexity** | How long a task takes, and how sure you can be | Each task's `likely` and `high` (the `high` includes that task's buffer) |
| **AI leverage** | How much AI coding tools shorten a task | Each task's leverage tag (High, Medium or Low), applied to that task only |
| **Team** | How many people work, and how much can run in parallel | The two tracks: Team and Solo |
| **Waits** | Calendar time nobody can speed up | A separate list, never mixed into effort |

**Use the real team whenever one is described.** The defaults below are a fallback for when nobody has said what the team looks like.

The main source is the team profile in [team/README.md](team/README.md), read under the rule in [risk-contract.md](risk-contract.md). When it is filled in:
- **Team** (profile §1) replaces the default team. Use FTE on new work, not headcount.
- **Stack and shipping process** (§2–3) shape the task list. The team's review, QA and release gates become tasks and waits.
- **AI adoption** (§4) sets which scenario is the suggested estimate.
- **Calibration** (§5) replaces the house bands wherever it gives a measured result: the team's estimate-to-actual ratio, or its measured AI speed-up. Show the adjustment.
- **Partner turnaround** (§6) gives the durations of the waits.

Where the profile is empty, take whatever the inputs say about the team from `idea.md`, uploaded documents or the product model.

Say which basis you used: "estimated for the team profile", "estimated for the described team" or "estimated for the default team". An estimate based on the real team always beats the default.

## 2. Two tracks, three scenarios each

**Team track: the product's team, or by default a scrum team.**
- **Default:** 1 product owner, 1 designer, 4 engineers and 0.5 QA. That is 6.5 FTE, working in 2-week sprints.
- **In feature runs:** use the product's own team if the inputs describe it.

**Solo track: one builder who does everything.** That means product, design, engineering, QA and ops.
- **Always included** in new-product runs. Include it in feature runs when a single builder is plausible.

**Each track has three scenarios.** They differ only in how much AI each task uses, following the bands in section 4:

| Scenario | Who it describes | Role |
|---|---|---|
| **AI-leveraged** | A team fully optimized around AI coding tools | Fast bound |
| **AI-typical** | A forward-looking company that uses AI where it is strong, but hasn't optimized every practice around it | **The suggested estimate** |
| **Traditional** | Standard development practice, with no AI assistance | Slow bound |

If the inputs say how much the team actually uses AI, use that level as the suggested estimate and say so.

**The overall envelope** runs from Team AI-leveraged (the fastest possible build today) to Solo traditional (the slowest). The suggested estimate for the track in question sits inside it.

**AI applies task by task, using the tags in section 4.** It is never a flat discount on the whole estimate. Tasks that AI does poorly keep close to their traditional duration in every scenario.

## 3. Break the work into tasks

Estimate tasks, not workstreams. Each task is one row:

| Task | Role | Complexity | AI leverage | Traditional (person-days, likely–high) | AI-typical | AI-leveraged | Critical path? |
|---|---|---|---|---|---|---|---|

- **Role:** product, design, engineering or QA. The Solo track does every role. The Team track spreads the roles across people who work in parallel.
- **Complexity:** S, M or L, with one line on what makes it hard. An L task names what is new or uncertain about it.
- **Likely and high.** `likely` is your honest central estimate. `high` is `likely` plus that task's buffer, which grows with complexity and novelty. Never use a single number.
- **AI-typical and AI-leveraged columns.** Multiply both traditional values by the scenario's factor for the task's leverage tag (section 4). Show the factors used.
- **Critical path:** mark the tasks that must happen in sequence, because they set the shortest possible calendar time.
- **Size tasks for a competent engineer who knows the stack.** Put a builder's inexperience in the Solo track's notes as a named swing factor. Don't pad every task for it.

## 4. AI leverage bands

These bands are house assumptions, not measured facts. Published evidence on AI coding productivity is mixed: large gains on greenfield work and well-documented APIs, small or even negative gains on unfamiliar large codebases. Where you can fetch evidence for a specific task type, cite it and use it instead. Otherwise use these bands and label the result an estimate.

Each cell is time as a share of the traditional estimate. Traditional is 1.0 for every tag.

| Tag | Typical tasks | AI-typical | AI-leveraged |
|---|---|---|---|
| **High** | Scaffolding, CRUD (create, read, update, delete) screens and endpoints, UI from a design, integrations with well-documented APIs and SDKs (payments, auth, a vendor quickstart), tests, migrations, docs | 0.6 | 0.4 |
| **Medium** | New integrations with thin docs, data pipelines, prompt and persona work, performance work on known patterns | 0.8 | 0.6 |
| **Low** | Latency tuning of real-time systems, evaluation design and accuracy work, security review, compliance controls, debugging third-party behavior, production hardening | 1.0 | 0.9 |

**Review, QA sign-off and waits don't compress.** AI shortens building. It does not shorten checking, approvals or anything outside the team.

## 5. Roll-up

**Effort.** Add up each scenario's person-days, likely and high. **Do not stack worst cases:** the roll-up's high end is not the sum of every task's `high`.
- `total_likely = sum of likely`
- `total_high = total_likely + sqrt(sum of (high − likely)²)`

This assumes task overruns are independent, so not all of them happen at once. Show the arithmetic. If overruns share a cause, say so and add them directly for that group only. For example, several tasks that all depend on an unproven vendor would overrun together.

**Calendar time.**
- **Solo:** calendar days = total effort in person-days ÷ the builder's available days per week, times 5 to convert to working days. Use the stated hours if the idea gives them. Otherwise assume full-time and say so.
- **Team:** calendar days = the larger of:
  - the critical-path length
  - total effort ÷ (people × 0.7)

  The 0.7 is a parallelism-efficiency estimate covering coordination, review and hand-offs.
- **Report the Team track in sprints and weeks.** Say which tasks limit how far adding people can help: work on the critical path doesn't shrink when you add engineers.

**FTEs.** Report effort as FTE-weeks (person-days ÷ 5), and give the team size behind each calendar figure. A reader can then see, for example, "6.5 FTE for 3 weeks" against "1 FTE for 11 weeks".

**Cost.** FTE-weeks × a stated weekly rate for each role:
- the builder's own rate if given
- otherwise a sourced market rate for the role, with the source cited
- for the Team track, a blended rate across the roles

## 6. Waits

List every calendar blocker that isn't engineering work. Examples: legal review, IP clearance, payment-processor underwriting, app-store review, vendor approval, data licensing.

For each, give its expected duration (as a range, sourced where possible) and say whether it gates the start of the build, the launch, or neither. Calendar time to launch is the build calendar or the gating waits, whichever is longer. Never convert a wait into person-days.

## 7. Reference check

Compare the total against at least one real reference point, and cite it. Examples:
- how long the vendor's own quickstart takes to reach a working demo
- a published build story for a similar product
- a comparable open-source project's history

If you can't find one, say so. If your estimate is more than about 3 times what the reference suggests, explain the gap, or revise.

## 8. Output

Every effort estimate delivers:
1. **The task table** (section 3).
2. **The scenario table:**

| Track | Scenario | Effort (person-days, likely–high) | FTE-weeks | Team size | Calendar (weeks, likely–high) | Sprints | Cost |
|---|---|---|---|---|---|---|---|
| Team | AI-leveraged | | | 6.5 | | | |
| Team | **AI-typical (suggested)** | | | 6.5 | | | |
| Team | Traditional | | | 6.5 | | | |
| Solo | AI-leveraged | | | 1 | | — | |
| Solo | **AI-typical (suggested)** | | | 1 | | — | |
| Solo | Traditional | | | 1 | | — | |

   Replace the 6.5 with the real team's size wherever the inputs describe the team.

3. **The estimate in one line.** "Suggested: team, AI-typical, X–Y weeks (solo: X–Y). Fastest: team, AI-leveraged, X–Y weeks. Slowest: solo, traditional, X–Y weeks."
4. **Waits** (section 6) and the **reference check** (section 7).
5. **What swings it most.** Up to 4 factors, each with its direction and rough size.

## 9. New-product runs: which figure is the headline

This refines "longer build" in [new-product-contract.md](new-product-contract.md) §1c.
- **Choose the track that matches the builder.** Use the framer's builder context. If it's unknown, use Solo.
- **The conservative headline** for `build_weeks_mvp`, `build_cost_mvp` and `build_person_days_mvp` is that track's **AI-typical** scenario at its roll-up `high`.
- **If the builder context says how much AI the builder uses, use that level.** For example, if it says no AI coding tools, the traditional `high` is the headline.
- **The `range`** runs from the same track's AI-leveraged `likely` to its traditional `high`.
- **Report the other track too,** as `build_weeks_mvp_team` or `build_weeks_mvp_solo`.
- **Every figure is an `estimate`** whose `reasoning` names the track, scenario and bands used. `replace_with` is measured velocity from a spike.

## 10. Lazy output

An estimate is lazy if it has any of these:
- effort with no team or FTE count
- the default team used when the inputs describe the real one
- workstreams instead of tasks
- one AI discount applied to everything
- a single number per task
- a roll-up that adds up every worst case
- waits folded into engineering weeks
- no reference point
- "top of the range because skill is unknown" applied to every line
