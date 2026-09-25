# Next on Wembley: new-product assessment

**Verdict: Pass**

> 0 of 18 verdict-driving figures verified. The run stopped after Stage 2, so none were fact-checked. The 18 break down as 4 sourced · 2 derived from sourced inputs · 3 derived from estimates · 3 conservative estimates · 6 unknown.

The product's core input, both partners' watch history, has no automated source (there is no streamer API, and scraping it would breach Netflix's terms), so it must be entered by hand indefinitely, while five couple apps, Netflix's Play Something and AI assistants help couples make the same decision without any history. That is the competitive-strategist's KILL. The one scaled manual-logging product, TV Time, got 25M people logging for free and still found "not enough demand for a paid app", and conservative break-even ($5.29 per pair-month) sits above the only couple-specific price anyone pays ($2.99).

*This is a rerun that incorporates `clarifications.md`, and an early exit: you stopped the run after the KILL. There is no business case, economics audit or fact check, so there is no base case. Even a written TMDb yes plus a passed pricing test would lift this only to Validate first.*

**The space.** Worth building in: **unclear**. The couple "what do we watch" problem is real and is the best-evidenced finding in the run. But nothing in the space has shown it can charge: the paid couple apps disclose no revenue, and the one scaled tracker died for lack of paid demand.

**Size class.** **A personal tool** (the synthesizer's call; no audit ran). A second reading is **a feature, not a product**, for whoever already holds both histories: Trakt (which has an open user request for this) or the streamers.

## Your clarification: why manual history didn't lead before, and does now
- **Agents found it.** Five of seven Stage 2 files rated it high severity, and the KILL rests on it ("far less setup than this product requires").
- **Why it wasn't the headline:**
  - You gave it as a known constraint, so agents tried to measure its consequence. None could, because the day-30 upkeep rate is unknown. Each flag was left at medium confidence, which sorts below high-confidence risks.
  - The last synthesis also split this one root cause across four register rows and led the verdict with A3 and A5 rather than the mechanism under A5. That was an editing miss.
- **Now it is register row #1, at high confidence.** The upgrade rests on evidence, not on your view. Netflix's own terms, cited by regulatory-scout, close the extension route that build-and-run.md left open. Simkl's docs say Hulu, Disney+, Prime and Max have no history page or API. No single agent combined these. The burden is certain and permanent; only how many pairs it costs is unknown.
- **Where the evidence is with you:** there is no automated route; the couple decision works without history (the swipe apps); and whoever holds the history is better placed to add the overlap.
- **Where it isn't:**
  - The streamers don't do this job. Netflix recommends per profile and per service, with no pair or cross-service view. The swipe apps already do the job without history, and do it lightly.
  - "Too big a barrier" is unmeasured, and the largest data point cuts the other way. TV Time's 25M and Letterboxd's 30M+ logged by hand for free; what they wouldn't do is pay. Whether a second, less engaged partner will log is untested.
  - Upkeep here is a status change per show, not per episode (build-and-run.md). The heavy parts are setup (~40 min per pair, estimate) and each partner's solo viewing.
- **So** A2 stays Unproven, and the verdict stays Pass, now led by the input burden.

## What this is
- **The product:** a web app tracking each partner's watched, watching, dropped and wanted shows. An LLM ranks a co-watch list and two personal lists, each pick with a "why", and partners vote on the picks.
- **Who it's for:** US and Canadian couples who co-watch serialized TV.
- **The problem:** choosing the next shared series.
- **The bet:** both partners hand-maintain their history, and the result beats free no-history apps by enough that a pair pays more than $5.29 a month for a tool used a few times a month.
- **The proof would be:**
  - at least 6 of 10 non-builder pairs current at day 30
  - a history-based list that beats a no-history version of itself
  - checkouts above break-even

## The math (conservative case: Stage 2 figures only, not audited or fact-checked)
| Row | Value | Kind |
|---|---|---|
| Price | Not set. The only couple-specific paid price observed: Matched Premium, **$2.99/mo**. Tracker seats: $3–$5/mo per person | unknown · sourced |
| Cost to serve | **$5.27 per pair-month** ($2.54 cash plus 2.5 founder-minutes); $5.88 at $80/h | derived from estimates |
| Break-even price | **$5.29**; **$5.94** at $80/h (the conservative rate) | derived from estimates |
| Gross margin at $2.99 | **−71%** (−92% at $80/h). Excluding founder time, +20% before fixed costs | derived from estimates; illustrative price |
| CAC vs CAC ceiling | CAC **~$240 per activated pair** (founder time). Ceiling **$0** below break-even | estimate vs derived |
| Break-even churn | **Unknown.** No observed price clears cost | unknown |
| Break-even customers | **None** below $5.29. ~683 pairs at an untested $6, against $451.85/mo fixed | derived from estimates |
| Capital to break-even | **Unknown.** Build is $13.9k–$17.1k of builder time, 21–26 weeks at an assumed 10 h/wk. The TMDb AI licence is unpriced | unknown · estimate |

## What must be true
The run stopped before the fact check, so no assumption can Hold.

| A# | Status | Evidence that set it |
|---|---|---|
| A1: the problem exists beyond one household | Unproven | Sourced complaints and five couple apps (Matched 100K+ downloads). The strongest assumption, but not fact-checked |
| A2: both partners keep their history current | **Unproven** | *Against:* only Netflix imports (manual CSV); an extension breaches Netflix's terms; all five couple apps avoid history. *For:* 25M TV Time and 30M+ Letterboxd members logged by hand (single-player, free). The pair day-30 rate is unknown |
| A3: low-frequency use supports a price | **Contradicted** | TV Time (20M+ users, used more often than this) closed citing "not enough demand for a paid app". This is by analogy |
| A4: affordable acquisition | Unproven | ~$240 per pair, community outreach (estimate). Scalable-channel CAC is unknown |
| A5: no free or incumbent substitute | **Contradicted** | Free overlap apps exist and need no history. Trakt holds both histories and has an open request for this |
| A6: licensing is workable | Unproven | TMDb names AI/LLM apps as needing a separate agreement, and whether one is available is unknown. JustWatch bans commercial use |
| A7: the market can sustain a business | Unproven | 38.0M serviceable households (derived). The 4,055 obtainable figure is an estimate |
| A8: cost well below price; build fits the hours | Unproven | The cost half fails on estimates ($5.27 against $2.99). The build fits 21–26 weeks (estimate) |

**Why A2 differs from A3 and A5 under the same standard:**
- **A3 and A5:** the evidence speaks directly to the claim. TV Time's operator says people wouldn't pay (A3), and free substitutes are directly observed (A5).
- **A2:** the claim is about user behaviour, and the evidence splits. The case against is builders' design choices. The only mass behaviour on record, millions logging by hand, supports tolerance, though for single players. Nothing measures pairs.

The same TV Time data that contradicts A3 argues against contradicting A2.

**Lens rollup:**
- **Contradicted:** Competition, Economics
- **Unproven:** Problem, Market, Go-to-market, Build & run, Legal & trust

## Your questions, answered
1. **A real market that would pay?** Not shown. There are ~38M serviceable households on paper, but the only couple-specific price is $2.99, on a lighter swipe app, and the nearest scaled comparable died for lack of paid demand. *market-size.md, problem.md.* **Not run:** the business case (price) and the fact check (counts).
2. **Any way around manual history, and does it kill the product?** No full way around it. The Netflix CSV, tracker imports and a title grid bring setup to ~40 min per pair (estimate). Other streamers stay manual, an extension breaches Netflix's terms, and Trakt import is reportedly paywalled. It is now the lead risk. It is fatal in combination with free no-history substitutes and no paid demand; whether it kills the product on its own is unmeasured. *build-and-run.md, regulatory.md, competition.md.*
3. **Can a few-times-a-month product hold users or justify a price?** Probably not on Stage 2 evidence. TV Time failed on this, and how often couples start a new series is unknown. *problem.md, competition.md.* **Not run:** the owner (venture-strategist, Stage 3) and the break-even-churn audit (unit-economics-auditor, Stage 4).
4. **Licensing limits?**
   - **TMDb:** needs a written agreement, singles out AI/LLM apps, caps caching at 6 months and requires attribution. The $149/mo quote doesn't cover the AI clause.
   - **JustWatch:** bans commercial use.
   - **Anthropic:** outputs appear usable commercially (asserted).
   - **Privacy:** PIPEDA and Law 25 apply from the first Canadian user.

   *regulatory.md.* **Not run:** the Stage 4 regulatory audit.
5. **Cost and price?** $5.27 per pair-month plus $451.85/mo fixed (derived from estimates), against an observed band of $0–$5 per person. *build-and-run.md.* **Not run:** the owner (unit-economics-auditor) and the price decision (venture-strategist).

## Top risks
1. **Both partners must hand-feed history that nothing can automate, while free substitutes ask for none** (high/high; five agents, and the root of the KILL).
2. **TV Time:** 25M people logged for free, and there was "not enough demand for a paid app" (high/high).
3. **The TMDb/JustWatch data layer may not be licensable for LLM use** (high/high).

## Disagreements
- **You vs the agents on manual history.** You call it the biggest risk and a kill. build-cost-analyst says tolerance, not the build, decides it, and regulatory-scout says it "does not by itself kill the product". I weight each side on a different part:
  - **Rank:** with you. It is the mechanism of the KILL, and the extension route is closed.
  - **Proof:** with the agents. It is unmeasured, and mass free logging exists.
  - **Whether streamers already do this:** with competition.md, against you. They don't do pairs.
- **A2's status.** problem-validator says Contradicted, build-cost-analyst Unproven. **I set Unproven**, for the reasons above.
- **The weight of upkeep.** problem-validator describes a "per-episode, per-partner chore"; build-and-run.md describes a per-show status change. **I weight build-and-run.md**, which matches the show-level design in idea.md.
- **An unsourced claim.** problem-validator says logging is "a named cause of abandonment", but the reviews it cites complain about Trakt's price. **I discount the claim.**
- **Extension import.** build-and-run.md lists it; regulatory-scout found it breaches Netflix's terms. **I weight regulatory-scout** (primary source).
- **Kill or not.** The competitive-strategist fired a KILL; build-cost-analyst ("borderline") and gtm-researcher (a first cohort only) did not. **I weight the KILL.** Survival needs an untested pair price above $5.29.
- **Pair price.** build-cost-analyst reasons two seats ($6–$10); the observed couple price is $2.99. **I weight the $2.99.**
- **Market value.** market-sizer's $203K/yr assumes all 4,055 pairs pay $49.99. **I weight the lower readings:** it is ~$81K at $19.99, and the founder-hours channel caps out at ~520 pairs in 3 years.
- **TMDb cost.** build-cost-analyst uses $149/mo; regulatory-scout says it's unknown because of the AI clause. **I weight unknown.**
- **Founder rate.** $65.38/h (build-cost-analyst) against $80/h (gtm-researcher), for the same person. **I apply $80/h** as the conservative rate.

## Validation plan (only if you want to contest the Pass)
The thresholds are the synthesizer's; no agent set them. Test 2 is aimed squarely at your concern.

| # | Assumption | Method | Cost and time | Pass | Kill |
|---|---|---|---|---|---|
| 1 | A6 | Email TMDb and JustWatch: is LLM use licensable, at what price, with provider data covered? | $0, ~1 h; reply time unknown | A written yes at ≤ $149/mo, with data covered | A no on AI use, or an unfunded separate licence |
| 2 | A2, A5, A1, rec quality | Unpaid concierge test, 10–15 non-builder couples, 2–4 weeks. Measure each partner's setup and day-30 upkeep. Blind A/B per pair: a full-history list vs a list from a 5-minute title grid only. A swipe-app head-to-head | 1.8–3.1 person-days (estimate) + 2–4 weeks | ≥ 6/10 pairs with both partners current at day 30; the history list gets ≥ 2 more Agrees per 10 than grid-only; preferred to the swipe app | < 4/10 current, or history no better than grid-only (the burden buys nothing), or the swipe app preferred |
| 3 | A3, A4, A8 | 2-week fake-door page with pair plans at $6 and $9, a checkout step and $300 of paid social | $300 + ~1 person-day + 2 weeks | ≤ $34 per checkout-intent pair at $9 (derived from estimates) | > $34 per pair, or no checkouts at $6 |

## Open questions for the decision-maker
1. You expect test 2 to fail. If you won't run it, the Pass stands. Is there any result that would change your mind?
2. Is the goal a paying business, or a portfolio or personal tool? Test 1 applies either way: a free public app may still be "commercial" to TMDb.
3. How many hours a week can you give this? The build time and the ~520-pair channel cap both scale with it.
4. Are the builder figures (60% agreement, 50% watch-through, $0.07 LLM spend) measured, or targets?
5. Would you rather pitch the overlap to Trakt or Simkl, who hold the history?
6. A swipe-first, no-history product removes your concern, but it lands in a crowded, commercially unproven niche. It needs its own run, since an early exit can't award a Pivot.
