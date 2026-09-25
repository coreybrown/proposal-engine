# Build and run: Next on Wembley

## Bottom line
- **Finding:** Building it is not the problem. Turning the private app into a paid multi-tenant product takes an estimated 26.6–32.7 person-days (Solo, AI-typical), which is 21–26 calendar weeks at an assumed 10 hours a week. Running it is the problem. The conservative cost to serve is **$5.27 per pair-month**, and any price below **$5.29 per pair-month** loses money on every pair before fixed costs. That sits at the top of the visible single-seat tracker band of $3–$5 per month. The kill condition was not fired, because trackers charge per person and this product is sold per pair. It is borderline.
- **Your questions:** Q2: No full workaround exists. A Netflix CSV or browser-extension import plus tracker-file imports can cut setup to about 40 minutes per pair, but Disney+, Prime, Max and Hulu stay manual. That doesn't kill the product on build grounds; whether pairs tolerate it is the test that decides it. Q4 (fees): TMDb commercial is **$149/month flat** under $1M revenue (a TMDb staff post, not a published price page). Whether that covers the JustWatch availability data is unknown, and the fallback is Watchmode at **$349/month**. Q5 (cost): $5.27 per pair-month conservative, of which $2.54 is cash and $2.72 is 2.5 founder minutes. On top of that come $451.85/month fixed ($190.35 cash plus 4 founder hours).
- **Assumptions:** A8 partly holds: the build fits the hours available. The cost part fails: cost to serve is not "well below" tracker-level prices unless a pair pays more than one tracker seat. A2 unproven: imports cover Netflix only (Simkl documents that other streamers have no history API). A6 part-evidenced: TMDb's fee is known, but JustWatch's commercial terms are not.

## Inputs and basis
- **Read:**
  - `research/opportunity-model.md`
  - `inputs/next-on-wembley/idea.md`
  - `sources/`, which is empty (no technical material was uploaded)
  - `docs/team/README.md`, which is `status: empty`, so it is ignored
- **Estimate basis:** "estimated for the described team". That is one solo builder, starting from the existing private Next.js + Prisma + Anthropic + TMDb app. The builder uses AI coding tools (asserted), so **AI-typical is the suggested scenario**.
- **Hours:** Hours per week are unstated. I used **10 hours a week (1.25 working days a week)** as the conservative reading of "nights and weekends".
- **Code not seen:** The code was not available. The multi-tenancy work is sized from the framer's inference: hard-coded partner names, and no signup, invites or billing.
- **Rate for builder time:** No rate was given for the builder's time. I used the US software-developer median of **$135,980/yr (BLS, May 2025)**, which works out to **$523/day** and **$65.38/hour**. The same rate prices build effort, support minutes and maintenance hours. It measures the value of the builder's time, not cash he pays out.
- **Prices:** Every price below was fetched on 2026-09-25.

## Feasibility

**Core capability.** The product needs three things:
- An LLM that ranks a TMDb-retrieved candidate set against two people's combined histories, votes and subscriptions.
- A short "why" for each pick that is grounded and factually correct.
- Current per-country availability data.

All of it has to run at a per-pair cost below the price.

| Part | Status | Evidence |
|---|---|---|
| LLM ranks candidates from a history, with no training | **Proven in general, with known weaknesses.** | Hou et al., ECIR 2024 (https://arxiv.org/abs/2305.08845, fetched 2026-09-25): "LLMs have promising zero-shot ranking abilities" but "struggle to perceive the order of historical interactions" and "can be biased by popularity or item positions in the prompts." |
| Ranking for the **overlap of two** people | **Unproven beyond n = 1.** | Only the builder's household. The "~60% co-watch agreement" figure is asserted and may be a target (opportunity model). I found no published benchmark for two-person LLM ranking. |
| Grounded, accurate "whys" | **Unproven.** | Nothing measured. The mitigation is design, not evidence: rank only TMDb IDs from the candidate set, and generate whys only from the supplied fields. |
| Metadata and per-country providers (CA/US) | **Proven technically. Commercially part-proven.** | TMDb exposes providers per country and requires JustWatch attribution (opportunity model, sourced). Whether TMDb's commercial plan covers commercial rights to the JustWatch data is **unknown** (see Dependencies). |
| Watch-history import | **Proven for Netflix only.** | Simkl docs (fetched 2026-09-25): "Simkl's Chrome extension ("Enhancer") sync with your Netflix and Crunchyroll to capture what you watch." Also: "services like Hulu, Disney+, Amazon Prime, and HBO Max either don't have a history pages or provide no APIs." |
| Cost per recommendation round | **Estimable from fetched prices** (below). | The only observed figure, "$0.07 of a $15 monthly budget", is asserted, and its period is unclear. |

**The spike that proves it.** This is the concierge option below, run unpaid:
- recruit 5–10 non-builder couples
- load each pair's history from the Netflix CSV plus a "popular shows" grid
- produce their co-watch top 10
- **measure:**
  1. the share of top-10 picks both partners Agree with, against a baseline list: TMDb popular titles on their providers, filtered to their shared genres
  2. factual errors in 50 audited whys
  3. actual input and output tokens per round, from the Anthropic `usage` field, which replaces my token estimate
  4. how many pairs are still updating at day 30

**Cost:** about 1.8–3.1 person-days (AI-typical) plus 2–4 weeks of elapsed time.

**Pass bar (suggested):** the co-watch Agree rate clearly beats the baseline, and the whys have close to zero factual errors.

## Q2: Is there a way around manual watch history?
**Short answer: partly. That doesn't kill the product on build grounds, but it caps the product at "useful after about 40 minutes of setup, with ongoing upkeep".**

| Route | What it covers | Build cost (in task table) | Limits and risk |
|---|---|---|---|
| Netflix CSV upload, per profile, fuzzy-matched to TMDb | Netflix history, one time | Task 6 | Manual and per profile. Netflix Help Center says: "Select Profiles, then choose a profile" (opportunity model). The CSV is at episode level and needs matching to series. |
| Browser extension that reads Netflix viewing activity, ongoing | Netflix, continuously | Not in the MVP (it's a separate product surface) | Simkl proves it is technically possible. Desktop-browser only. Breaks when Netflix changes the page. Terms-of-use risk under Netflix's terms is **routed to the regulatory-scout**. |
| Import from tracker export files (Trakt, Simkl) | Whatever the S2 couples already logged | Task 7 | **Rented land:** in August 2026 Trakt reportedly began requiring a paid VIP to create API apps, and existing keys disappeared (ettayeb.fr, secondary). TV Time shut down on 15 July 2026, so its users only have the exports they took beforehand. |
| Cold-start "tap what you've seen" grid of popular series | Every service | Task 5 | Coarse: no ratings or drops until edited. |
| Capture as a by-product of use: picking from the list marks it "watching", and each vote is a signal | Upkeep on every service | Tasks 5 and 10 | Only captures shows chosen *through* the app. |
| Personal-data access requests to streamers | Possibly all | Not built | Slow and manual, and the output format is unknown. Unverified. Not an MVP route. |

**Setup-time estimate (the user's time, not a business cost):**
- **About 20 minutes per partner, 40 minutes per pair** (estimate):
  - a 60-title grid at about 5 minutes
  - searching and adding in-progress, dropped and want-to-watch titles at about 5 minutes
  - downloading and uploading the Netflix CSV and fixing mismatches at about 10 minutes
- **Upkeep** is then a status change whenever a show is started or dropped outside the app.

**Does it kill the product?** Not technically. It is the main adoption risk, and the concierge spike's day-30 measure (above) is what settles it.

## MVP options

| Option | What's real | What's faked | Time to first paying customer (Solo AI-typical, 10 h/wk) | Cost to build (range; kind) |
|---|---|---|---|---|
| **Concierge** | LLM recommendations from the existing app, TMDb data, lists delivered by email; payment by Paddle or Stripe payment link | Signup, pair invite, import (the builder enters each pair's data), self-serve app access, billing automation | 1.4–2.5 weeks of build, plus recruiting. Charging needs the $149/month TMDb plan from day one. | $941–$1,606 AI-typical (range $680–$2,176); estimate |
| **Stitched** | Both partners use the app themselves; one single-tenant deployment per pair behind a vendor auth gate; Netflix CSV import; payment links | Provisioning (done by hand per pair), multi-tenancy, automated entitlement | 5.9–8.0 weeks | $3,870–$5,230 AI-typical (range $2,981–$6,642); estimate |
| **Built** (fully estimated below) | Self-serve signup, pair invite, both-partner onboarding and import, per-pair data isolation, billing, cost controls, recommendations evaluated for arbitrary pairs | Nothing core | 21.3–26.2 weeks | $13,912–$17,102 AI-typical (range $10,826–$21,495); estimate |

**Recommendation:**
- **Run concierge first, unpaid if the TMDb terms allow,** as the spike. It tests A1, A2 and recommendation quality for about 2–3 person-days.
- **Build only if it passes.** "Built" is the first *shippable* version, so it carries the headline build figures.
- **Stitched isn't worth it here.** It saves time on the build, but the builder pays it back in manual provisioning for every pair, and it has to be thrown away later.
- **Concierge doesn't scale on human time.** It costs about 45 builder-minutes per new pair plus about 15 per pair-month (estimate). That is roughly 6 times the Built option's 2.5 minutes a month.

### Built: task table
AI factors from `docs/estimating.md` §4 (house bands, estimate):
- **High:** 0.6 AI-typical, 0.4 AI-leveraged
- **Medium:** 0.8 AI-typical, 0.6 AI-leveraged
- **Low:** 1.0 AI-typical, 0.9 AI-leveraged

All figures are person-days, likely–high.

| # | Task | Role | Cx | What makes it hard | AI | Traditional | AI-typical | AI-leveraged | Critical path |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Multi-tenancy retrofit: Pair entity, user↔pair, scope every Prisma query by pair, remove hard-coded partner names | eng | M | Refactoring existing code the estimator hasn't seen | Med | 3.0–5.0 | 2.4–4.0 | 1.8–3.0 | yes |
| 2 | Auth and signup (magic link, vendor or Auth.js quickstart) | eng | S | Well documented | High | 1.5–2.5 | 0.9–1.5 | 0.6–1.0 | yes |
| 3 | Pair invite: link, accept, second-partner onboarding, pending/solo states | eng/design | M | Two-person state machine | High | 2.0–3.5 | 1.2–2.1 | 0.8–1.4 | yes |
| 4 | Partner privacy and account split: private ratings, leave pair, per-partner export and delete | eng/product | M | Policy choices; shared votes on split | Med | 2.0–3.5 | 1.6–2.8 | 1.2–2.1 | |
| 5 | Fast onboarding: popular-series grid, bulk add, subscriptions and region picker (CA/US) | eng/design | M | UX for low-effort entry | High | 3.0–5.0 | 1.8–3.0 | 1.2–2.0 | |
| 6 | Netflix CSV import: parse per profile, episode→series fuzzy match to TMDb, review UI | eng | M | Match accuracy on messy titles | Med | 3.0–5.0 | 2.4–4.0 | 1.8–3.0 | |
| 7 | Generic tracker-export import (Trakt or Simkl files) | eng | S | Format variety | Med | 1.5–2.5 | 1.2–2.0 | 0.9–1.5 | |
| 8 | Billing: Paddle checkout, webhooks, per-pair entitlement, trial | eng | M | Webhook edge cases | High | 2.0–3.5 | 1.2–2.1 | 0.8–1.4 | yes |
| 9 | LLM cost controls: per-pair rate limit, model lock, prompt caching, usage metering and alerts | eng | S | Measuring real tokens | Med | 1.5–2.5 | 1.2–2.0 | 0.9–1.5 | |
| 10 | Recommendation generalization and evaluation: prompts tuned on one household made to work for any pair; eval set; grounded-why guard (TMDb IDs only) | eng/product | **L** | **New:** quality for other pairs is unmeasured; the eval design itself is new | Low | 4.0–8.0 | 4.0–8.0 | 3.6–7.2 | |
| 11 | TMDb and JustWatch compliance: attribution UI, 6-month cache TTL and refresh job | eng | S | Clear rules | High | 1.0–2.0 | 0.6–1.2 | 0.4–0.8 | |
| 12 | Landing and pricing pages, ToS and privacy pages (template), transactional emails | eng/product | S | Boilerplate | High | 1.5–2.5 | 0.9–1.5 | 0.6–1.0 | |
| 13 | Security and hardening: authorization check on every route (no cross-pair reads), rate limiting, backups, error monitoring | eng | M | Isolation of partner data | Low | 2.0–4.0 | 2.0–4.0 | 1.8–3.6 | |
| 14 | Funnel instrumentation: second-partner activation, day-30 upkeep, retention | eng | S | Standard | High | 1.0–1.5 | 0.6–0.9 | 0.4–0.6 | |
| 15 | End-to-end QA of signup→invite→onboard→recommend→pay, and fixes from a 3–5 pair beta | QA | M | Checking doesn't compress | Low | 3.0–5.0 | 3.0–5.0 | 2.7–4.5 | yes |
| 16 | Mobile-web design pass for couch use | design | M | Designing, not only implementing | Med | 2.0–3.5 | 1.6–2.8 | 1.2–2.1 | |

**Roll-up** (`total_high = total_likely + sqrt(sum of (high − likely)²)`). Overruns are treated as independent. None of these tasks share an unproven vendor except #6 and #7, which are small.

| Scenario | Sum of likely | Sum of (high − likely)² | High |
|---|---|---|---|
| Traditional | 34.0 | 50.25 → √ = 7.09 | **41.1** |
| AI-typical | 26.6 | 37.51 → √ = 6.12 | **32.7** |
| AI-leveraged | 20.7 | 26.54 → √ = 5.15 | **25.9** |

**Calendar.**
- **Solo:** effort ÷ 1.25 days a week (10 h/wk, estimate).
- **Team (default 6.5 FTE):** max(critical path, effort ÷ (6.5 × 0.7 = 4.55)). The critical path is tasks 1→2→3→8→15:
  - AI-typical 8.7 likely, 8.7 + √(1.6² + 0.6² + 0.9² + 0.9² + 2.0²) = 8.7 + 2.92 = 11.6 high
  - Traditional 11.5 → 15.2
  - AI-leveraged 6.7 → 9.1

  In every scenario the critical path is longer than effort ÷ 4.55, so adding people doesn't help. Tasks #1 and #15 set the floor.
- **Cost:** person-days × $523/day (derived from BLS). The same rate is used as the Team blend, stated rather than sourced per role.

### Built: scenario table

| Track | Scenario | Effort (person-days) | FTE-weeks | Team size | Calendar (weeks) | Sprints | Cost (effort × $523) |
|---|---|---|---|---|---|---|---|
| Team | AI-leveraged | 20.7–25.9 | 4.1–5.2 | 6.5 | 1.3–1.8 | 1 | $10,826–$13,546 |
| Team | **AI-typical (suggested)** | 26.6–32.7 | 5.3–6.5 | 6.5 | 1.7–2.3 | 1–2 | $13,912–$17,102 |
| Team | Traditional | 34.0–41.1 | 6.8–8.2 | 6.5 | 2.3–3.0 | 2 | $17,782–$21,495 |
| Solo | AI-leveraged | 20.7–25.9 | 4.1–5.2 | 1 | 16.6–20.7 | — | $10,826–$13,546 |
| **Solo** | **AI-typical (suggested, headline)** | **26.6–32.7** | **5.3–6.5** | 1 | **21.3–26.2** | — | **$13,912–$17,102** |
| Solo | Traditional | 34.0–41.1 | 6.8–8.2 | 1 | 27.2–32.9 | — | $17,782–$21,495 |

Notes on the table:
- **Team cost:** a 6.5-FTE team held for its full calendar would cost more than the effort-based figure. At AI-typical high that is 6.5 × 2.3 weeks × 5 days × $523 = $39,093.
- **Solo at full time:** AI-typical is 5.3–6.5 weeks.
- **In cash:** the builder's own time costs him no cash. Cash spent during the build is his tooling, which is unknown.

**The estimate in one line.** Suggested: solo, AI-typical, 21–26 weeks at 10 h/week (team: 1.7–2.3 weeks). Fastest: team, AI-leveraged, 1.3–1.8 weeks. Slowest: solo, traditional, 27–33 weeks.

### Other options: scenario tables

**Concierge.** Tasks, traditional person-days:
- intake form and payment link, 0.5–1, High
- admin-only "act as pair" data switch in the existing app, 1.5–3, Med
- delivery email and process doc, 0.5–1, High

| Track | Scenario | Effort (pd) | Calendar (weeks) | Cost |
|---|---|---|---|---|
| Team | AI-leveraged / **AI-typical** / Traditional | 1.3–2.2 / **1.8–3.1** / 2.5–4.2 | 0.2–0.4 / **0.3–0.5** / 0.4–0.7 | $680–$1,172 / **$941–$1,606** / $1,308–$2,176 |
| Solo | AI-leveraged / **AI-typical** / Traditional | same | 1.0–1.8 / **1.4–2.5** / 2.0–3.3 | same |

**Stitched.** Tasks, traditional person-days:

| Task | Person-days | AI leverage |
|---|---|---|
| Auth gate | 1–1.5 | High |
| Per-pair provisioning script | 1.5–3 | Med |
| Partner-name config | 0.5–1 | High |
| Payment link and manual entitlement | 0.5–1 | High |
| Netflix CSV import | 3–5 | Med |
| Attribution | 1–2 | High |
| Isolation review and beta QA | 2–3.5 | Low |

| Track | Scenario | Effort (pd) | Calendar (weeks) | Cost |
|---|---|---|---|---|
| Team | AI-leveraged / **AI-typical** / Traditional | 5.7–7.8 / **7.4–10.0** / 9.5–12.7 | 0.7–1.0 / **0.8–1.2** / 1.0–1.4 | $2,981–$4,079 / **$3,870–$5,230** / $4,969–$6,642 |
| Solo | AI-leveraged / **AI-typical** / Traditional | same | 4.6–6.2 / **5.9–8.0** / 7.6–10.2 | same |

### Waits (never counted as effort)

| Wait | Duration | Gates |
|---|---|---|
| TMDb commercial plan sign-up | 0–2 weeks (estimate; staff describe it as a subscription) | the paid launch, and any concierge charging |
| Written answer on JustWatch data rights under that plan (sales@themoviedb.org) | unknown; could be open-ended | launch of the availability features |
| Paddle seller approval | 1–2 weeks (estimate, not sourced) | billing |
| External beta with day-30 upkeep reading | 4 weeks (the framer's named test) | the recommended paid launch |
| Optional lawyer review of ToS and privacy | 1–2 weeks (estimate) | launch |

The waits run in parallel with a 21–26-week solo build, so **the build calendar sets launch**.

### Reference check
ShipFast (https://shipfa.st/, fetched 2026-09-25) is a Next.js boilerplate with auth, payments, emails and a landing page. It advertises "Ship your startup in days, not weeks".

My equivalent tasks (#2, #8, #12) come to 3.0–4.2 person-days AI-typical, which is consistent with "days". The rest of the estimate is work specific to this product that no boilerplate covers:
- the multi-tenancy retrofit
- pair invites
- import and matching
- evaluation
- hardening

It is within 3 times the reference's order of magnitude for the parts the reference covers.

### What swings it most
1. **Builder hours** (unknown). At 20 h/week, Solo AI-typical falls to 10.6–13.1 weeks. At 5 h/week it doubles to 42.6–52.3.
2. **Codebase state** (unseen). If single-household assumptions run through the schema, task #1 could double: +2.4–4.0 person-days.
3. **Recommendation quality for arbitrary pairs.** If the spike shows weak co-watch agreement, task #10 could double: +4–8 person-days. There is no ceiling if the approach itself fails.
4. **Availability data licensing.** If the JustWatch-via-TMDb data can't be used commercially, replacing it with Watchmode adds about 2–4 person-days (estimate) and **$349/month**.

## Cost to serve per unit
**Unit: one pair (household of two partners) for one month of paid use.**

### Token arithmetic (estimate)
Architecture assumed: three LLM calls per recommendation round, one co-watch and two personal. It is not verified against the code.

| Prompt component | Co-watch call | Each personal call |
|---|---|---|
| System prompt, instructions, output schema | 1,500 | 1,500 |
| History: 200 titles per partner × 20 tokens (title, year, status, rating) | 8,000 (both) | 4,000 (own) |
| Past votes: 100 per pair × 15 tokens | 1,500 | 750 (own) |
| Subscriptions and region, mood | 150 | 150 |
| Candidates from TMDb: 80 × 60 tokens (genres, rating, seasons, providers) | 4,800 | 4,800 |
| **Input** | **15,950** | **11,200** |
| Output: 10 picks × 70 tokens (ID, title, score, why) + 200 JSON overhead | 900 | 900 |

- **Per round:** input 15,950 + 2 × 11,200 = **38,350 tokens**. Output 3 × 900 = **2,700 tokens**.
- **Sonnet 5**, the conservative case because model choice is a user setting today, at $2 in and $10 out per MTok: 38,350 × $2/1M + 2,700 × $10/1M = $0.0767 + $0.0270 = **$0.1037 per round**.
- **Haiku 4.5** ($1 / $5): $0.0384 + $0.0135 = $0.0519 per round.
- **Rounds per pair-month: 16** (estimate). That is 4 decision sessions a month, which matches "a few times a month", × 4 regenerations per session after votes or mood changes. Conservative on the high side for cost.
- **LLM per pair-month:** 16 × $0.1037 = **$1.6592**.
- **Not modelled:**
  - extended thinking, which would add output tokens
  - prompt caching (cache reads cost $0.20/MTok on Sonnet 5), which the builder could turn on

**Cross-check against the builder's figure.** The builder's asserted "$0.07" buys 0.7 Sonnet rounds or 1.35 Haiku rounds at these rates. So either the period was short, or the real prompts are much smaller than modelled. Measure it with the spike.

### Line items

| Line | Quantity per unit | Unit price (kind, source) | Cost per unit |
|---|---|---|---|
| LLM tokens (Sonnet 5) | 16 rounds × 38,350 in + 2,700 out | $2 / $10 per MTok (sourced, claude.com/pricing) | **$1.6592** |
| Vercel function memory, LLM calls | 16 × 3 calls × 45 s × 2 GB = 1.2 GB-h | $0.0122/GB-h, Montreal yul1 (sourced, Vercel docs) | $0.0146 |
| Vercel function memory, page and API requests | 300 req × 0.3 s × 2 GB = 0.05 GB-h | $0.0122/GB-h (sourced) | $0.0006 |
| Vercel Active CPU | 16 × 0.5 s + 300 × 0.05 s = 23 s = 0.00639 h | $0.147/CPU-h, yul1 (sourced) | $0.0009 |
| Vercel invocations | 348 | $0.60 per million (sourced) | $0.0002 |
| Vercel CDN requests | ~1,000 | $20 per 10M, from the first paid Flat Rate tier (sourced); Pro includes 1M | $0.0020 |
| Neon storage | 0.01 GB per pair (estimate: 400 titles, votes, cached lists) | $0.35/GB-month (sourced) | $0.0035 |
| Neon compute, incremental | 0.1 CU-h (estimate) | $0.106/CU-h (sourced) | $0.0106 |
| Transactional email | 6 (invites, magic links, receipts) | $20 / 50,000 = $0.0004 each, Resend Pro (sourced; the free tier covers the first 3,000/month) | $0.0024 |
| TMDb API calls and images | ~200 lookups (cached ≤ 6 months) | $0 variable: flat $149/month plan whose only stated restriction is "an IP based rate limit of around 40 requests per second" (sourced) | $0.0000 (the fee is in fixed costs) |
| Streaming-availability data (JustWatch via TMDb) | per lookup | $0 variable under TMDb **if covered** (unknown). Otherwise a $349/month fixed fallback. | $0.0000 |
| Payment processing (Paddle, merchant of record, handles sales tax) | 1 monthly charge at a $5.00 reference price | 5% + $0.50 per transaction (sourced) | $0.7500 |
| Refunds and chargebacks | 2% of a $5.00 charge | estimate | $0.1000 |
| Human: support | 2.0 min (15% of pairs contact × 12 min + 0.2 min billing admin) | $65.38/h (derived from BLS) | $2.1792 |
| Human: review of LLM output and availability errors | 0.5 min | $65.38/h | $0.5448 |
| **Total** | | | **$5.2681** |

**Total, reproduced:**
- Infrastructure: 0.0146 + 0.0006 + 0.0009 + 0.0002 + 0.0020 + 0.0035 + 0.0106 + 0.0024 = **$0.0348**
- Cash before payments: 1.6592 + 0.0348 = **$1.6940**
- Payments and refunds: 0.7500 + 0.1000 = **$0.8500**
- Cash: 1.6940 + 0.8500 = **$2.5440**
- Human: 2.1792 + 0.5448 = **$2.7240**
- **Total: 2.5440 + 2.7240 = $5.2680, which rounds to $5.27 per pair-month**

**At any price P**, cost = 4.4180 + 0.50 + 0.07P = **4.9180 + 0.07P**. Contribution is zero where P = 4.9180 ÷ 0.93 = **$5.29 per pair-month**. Any lower price loses money per pair before fixed costs.

Related lines, not in the headline:
- **Onboarding help:** about 5 builder-minutes per *new* pair (25% of pairs need help × 20 min, estimate) = $5.45 one-off. This belongs in acquisition cost, not the monthly unit.
- **Stripe instead of Paddle:** on a Canadian account, 2.9% + 0.8% international + 0.7% Billing + 2% FX, plus CA$0.30 (US$0.212 at 1.4136). At $5 that is **$0.532**. It is cheaper, but it leaves sales-tax registration and filing to the builder, and Stripe Tax's fee was not fetched.
- **Levers the builder controls, not modelled:**
  - locking paid pairs to Haiku, which halves the LLM line to $0.8296
  - annual billing, which spreads the $0.50 fixed fee across 12 months
  - prompt caching

**Kill check against comparable prices.** Fetched 2026-09-25:
- **Trakt VIP:**
  - "$60 annual price" (alternativeto, May 2025)
  - "$4.99/month" (ettayeb.fr, Aug 2026)
  - "around $3 per month billed yearly" (achriom, Jul 2026)

  That gives a per-person band of $3–$5 per month.
- **TV Time** was free and shut down on 15 July 2026, saying "there was not enough demand for a paid app" (TechCrunch).

The conservative $5.27 per pair **is above the single-seat low end ($3) and about equal to the single-seat high end ($5)**. I did not fire the kill because the unit here is a pair and trackers charge per person, which makes the like-for-like pair price $6–$10. The case survives only if a pair will pay **more than about $5.29 a month**, more than one tracker seat. Nobody has tested that. It is a high-severity risk.

## Fixed running costs (monthly)

| Line | Amount | Kind and source |
|---|---|---|
| TMDb commercial plan (<$1M revenue) | $149.00 | sourced: TMDb staff (Travis Bell), 2026-03-31 forum post. Not on a public price page (themoviedb.org/subscribe needs a login). |
| Vercel Pro (1 seat; includes $20 usage credit, 1M CDN requests, 1 TB) | $20.00 | sourced: vercel.com/pricing and the Flat Rate CDN docs. Hobby is "for personal, non-commercial use." |
| Neon base compute, always-on 0.25 CU × 730 h × $0.106 | $19.35 | derived; the 0.25 CU size is an estimate. Neon has "no monthly minimum." |
| Domain | $2.00 | estimate ($20/yr; replace with the registrar invoice) |
| Resend (free to 3,000 emails/month, about 500 pairs) | $0.00 | sourced; $20/month beyond that |
| Sentry Developer (5k errors, 1 user) | $0.00 | sourced |
| Paddle / Anthropic monthly minimums | $0.00 | Paddle: "no… monthly fees" (sourced). Anthropic: pay-per-token assumed; no minimum fee was shown on the price page. |
| Insurance (cyber / E&O) | unknown | settle with a broker quote. It is not legally required for this product. |
| **Cash subtotal** | **$190.35** | derived: 149 + 20 + 19.35 + 2 |
| Founder upkeep: dependency and model upgrades, TMDb cache job, monitoring, 4 h × $65.38 | $261.50 | estimate |
| **Total fixed** | **$451.85** | derived |
| *If the availability data must be relicensed:* Watchmode Startup (40,000 credits, commercial) | +$349.00 | sourced (api.watchmode.com). Cash would become $539.35. |

**Fixed cost per pair** (derived, $451.85 ÷ N):

| Pairs | Fixed cost per pair-month | Fully loaded (+ $5.27) |
|---|---|---|
| 25 | $18.07 | $23.34 |
| 100 | $4.52 | $9.79 |
| 500 | $0.90 | $6.17 |

## Dependencies and platform risk
- **TMDb is the whole data layer.**
  - The commercial price comes from a staff forum post, not a contract. The terms say any agreement "may be subject to… payment of fees".
  - Caching is capped at 6 months.
  - **If the price or terms change,** the product needs a re-platform to another metadata source, for example Watchmode at $349 or more per month. That would roughly triple cash fixed costs.
- **Availability data (JustWatch, reached through TMDb).**
  - Attribution to JustWatch is mandatory.
  - JustWatch's own API is sold under contract, with a "unique partner token" issued after the contract is signed. Whether TMDb's plan passes on commercial rights is unknown.
  - **If it doesn't,** the core input "active subscriptions with regional availability" goes dark until a fallback (+$349/month) is integrated.
- **Anthropic is a single model vendor.**
  - Price changes, model retirement (Haiku 4.5 and Sonnet 5 will be deprecated at some point) and outages would all hit the product.
  - Prompts tuned for one model need re-evaluating on the next: task #10's evaluation set becomes a recurring cost.
  - **If prices rise,** the LLM line is 31% of the conservative unit cost ($1.66 ÷ $5.27), so it matters.
- **Import sources are rented land.**
  - Netflix's CSV format, and the Netflix page an extension would read, can change without notice.
  - Trakt reportedly paywalled API-app creation in August 2026.
  - TV Time is gone.
  - **If any of these moves,** it breaks the setup path (Q2) and adds manual effort.
- **Paddle.**
  - Paddle asks sellers of products under $10 to "contact us for bespoke pricing", so the 5% + $0.50 fee is not guaranteed at this price point.
  - Moving to Stripe puts CA/US sales-tax compliance on the builder.
- **Vercel and Neon** are low risk: standard Next.js and Postgres, portable to other hosts in days.

## Open questions for the decision-maker
1. How many hours a week can you actually give this? Solo calendar time scales directly with it: at 10 h/week, 21–26 weeks.
2. What do the Anthropic usage logs show for input and output tokens per recommendation round, and how many calls does one round make? Over what period and how many rounds did the "$0.07" cover?
3. Will paid pairs be locked to Haiku? Sonnet costs twice as much per round at the same token counts, and it is the largest cash line.
4. How deep do the single-household assumptions go: schema, queries, prompts? That decides whether task #1 is 2.4 or closer to 8 person-days.
5. Will you email sales@themoviedb.org for written confirmation that the $149 plan covers commercial display of JustWatch-sourced provider data in CA/US? Nothing downstream is safe to build before that answer.
6. Would you run the concierge spike unpaid first, and is a free beta that leads to a paid product "commercial" under TMDb's definition ("primary purpose is to create revenue")? The regulatory-scout should confirm.
7. Monthly or annual billing? On a $5 monthly charge, Paddle's fixed $0.50 is 10% of revenue.

KEY_FIGURES:
  - name: cost_to_serve_per_unit
    value: 5.27
    unit: usd per pair per month
    kind: derived
    formula: llm_cost_per_pair_month (1.6592) + infra_cost_per_pair_month (0.0348) + payment_cost_per_unit (0.75) + refunds_per_unit (0.10) + human_cost_per_unit (2.724); payment and refund lines computed at a 5.00 reference price
  - name: cost_to_serve_cash_per_unit
    value: 2.54
    unit: usd per pair per month
    kind: derived
    formula: cost_to_serve_per_unit (5.268) - human_cost_per_unit (2.724)
  - name: price_floor_conservative
    value: 5.29
    unit: usd per pair per month
    kind: derived
    formula: (llm 1.6592 + infra 0.0348 + human 2.724 + paddle fixed fee 0.50) / (1 - paddle rate 0.05 - refund rate 0.02)
  - name: human_minutes_per_unit
    value: 2.5
    unit: minutes per pair per month
    kind: estimate
    reasoning: "No comparable discloses support load. Assumed 15% of pairs contact support monthly x 12 min = 1.8 min, plus 0.2 min billing admin, plus 0.5 min reviewing reported LLM or availability errors; high end for a two-person, manual-entry product."
    replace_with: "support minutes logged across the first 30 paying pairs"
  - name: human_cost_per_unit
    value: 2.724
    unit: usd per pair per month
    kind: derived
    formula: human_minutes_per_unit (2.5) / 60 x builder_rate_hourly (65.375)
  - name: human_minutes_onboarding_per_new_pair
    value: 5
    unit: minutes per new pair (one-off)
    kind: estimate
    reasoning: "25% of new pairs assumed to need help with invite or Netflix CSV matching, 20 min each."
    replace_with: "onboarding support minutes logged in the concierge spike and beta"
  - name: llm_cost_per_pair_month
    value: 1.6592
    unit: usd per pair per month
    kind: derived
    formula: llm_rounds_per_pair_month (16) x llm_cost_per_round_sonnet (0.1037)
  - name: llm_cost_per_round_sonnet
    value: 0.1037
    unit: usd per recommendation round
    kind: derived
    formula: llm_input_tokens_per_round (38350) x sonnet_input_price (2) / 1e6 + llm_output_tokens_per_round (2700) x sonnet_output_price (10) / 1e6
  - name: llm_cost_per_round_haiku
    value: 0.0519
    unit: usd per recommendation round
    kind: derived
    formula: 38350 x haiku_input_price (1) / 1e6 + 2700 x haiku_output_price (5) / 1e6
  - name: llm_input_tokens_per_round
    value: 38350
    unit: tokens per round
    kind: estimate
    reasoning: "Three calls per round (co-watch 15,950; two personal at 11,200): 1,500 system prompt, 200 titles per partner x 20 tokens, 100 votes x 15, 80 candidates x 60, 150 context."
    replace_with: "Anthropic usage field logged per round in the concierge spike"
  - name: llm_output_tokens_per_round
    value: 2700
    unit: tokens per round
    kind: estimate
    reasoning: "Three lists x (10 picks x 70 tokens + 200 JSON overhead) = 2,700; no extended thinking assumed."
    replace_with: "Anthropic usage field logged per round in the concierge spike"
  - name: llm_rounds_per_pair_month
    value: 16
    unit: recommendation rounds per pair per month
    kind: estimate
    reasoning: "4 decision sessions a month ('a few times a month') x 4 regenerations per session after votes or mood changes; high side for cost."
    replace_with: "rounds per active pair per month from beta instrumentation"
  - name: sonnet_input_price
    value: 2
    unit: usd per million input tokens
    kind: sourced
    source: https://claude.com/pricing
    fetched: 2026-09-25
    quote: "Sonnet 5 Input $2 / MTok"
  - name: sonnet_output_price
    value: 10
    unit: usd per million output tokens
    kind: sourced
    source: https://claude.com/pricing
    fetched: 2026-09-25
    quote: "Sonnet 5 Output $10 / MTok"
  - name: haiku_input_price
    value: 1
    unit: usd per million input tokens
    kind: sourced
    source: https://claude.com/pricing
    fetched: 2026-09-25
    quote: "Haiku 4.5 Input $1 / MTok"
  - name: haiku_output_price
    value: 5
    unit: usd per million output tokens
    kind: sourced
    source: https://claude.com/pricing
    fetched: 2026-09-25
    quote: "Haiku 4.5 Output $5 / MTok"
  - name: infra_cost_per_pair_month
    value: 0.0348
    unit: usd per pair per month
    kind: derived
    formula: vercel memory 0.0146 + 0.0006 + active cpu 0.0009 + invocations 0.0002 + cdn 0.0020 + neon storage 0.0035 + neon compute 0.0106 + email 0.0024; usage quantities are estimates, unit prices sourced
  - name: vercel_memory_price_yul1
    value: 0.0122
    unit: usd per gb-hour
    kind: sourced
    source: https://vercel.com/docs/functions/usage-and-pricing
    fetched: 2026-09-25
    quote: "Montreal, Canada (yul1) | $0.147 | $0.0122"
  - name: neon_compute_price
    value: 0.106
    unit: usd per cu-hour
    kind: sourced
    source: https://neon.com/pricing
    fetched: 2026-09-25
    quote: "$0.106/CU-hour"
  - name: paddle_fee
    value: 0.05
    unit: share of transaction plus 0.50 usd fixed
    kind: sourced
    source: https://www.paddle.com/pricing
    fetched: 2026-09-25
    quote: "5% + 50¢ per Checkout transaction"
  - name: payment_cost_per_unit
    value: 0.75
    unit: usd per pair per month at a 5.00 monthly reference price
    kind: derived
    formula: paddle_fee (0.05) x reference_price (5.00, = competitor_price_high) + 0.50
  - name: refunds_per_unit
    value: 0.10
    unit: usd per pair per month
    kind: estimate
    reasoning: "No source; assumed 2% of a 5.00 charge lost to refunds and chargebacks for a new consumer subscription."
    replace_with: "refund and chargeback rate from the first 3 months of Paddle data"
  - name: stripe_card_fee_canada
    value: 0.029
    unit: share of transaction plus 0.30 cad
    kind: sourced
    source: https://stripe.com/pricing
    fetched: 2026-09-25
    quote: "2.9% + CA$0.30 per successful transaction for domestic cards"
  - name: usd_cad_rate
    value: 1.4136
    unit: cad per usd
    kind: sourced
    source: https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/
    fetched: 2026-09-25
    quote: "USD 2026-09-24 1.4136"
  - name: tmdb_commercial_licence_cost
    value: 149
    unit: usd per month
    kind: sourced
    source: https://www.themoviedb.org/talk/69cbf4f91b914f0e9542a772
    fetched: 2026-09-25
    quote: "If you do less than $1 million in revenue you can subscribe to our 'commercial' plan for $149/mo."
  - name: watchmode_startup_price
    value: 349
    unit: usd per month
    kind: sourced
    source: https://api.watchmode.com/
    fetched: 2026-09-25
    quote: "Startup $349/month 40,000 Monthly Credits Commercial use"
  - name: vercel_pro_price
    value: 20
    unit: usd per month
    kind: sourced
    source: https://vercel.com/pricing
    fetched: 2026-09-25
    quote: "$20/mo."
  - name: neon_base_compute_monthly
    value: 19.35
    unit: usd per month
    kind: derived
    formula: always-on compute size (0.25 cu, estimate) x 730 hours x neon_compute_price (0.106)
  - name: founder_maintenance_hours_monthly
    value: 4
    unit: hours per month
    kind: estimate
    reasoning: "Dependency and model upgrades, TMDb cache refresh checks, monitoring and billing admin for a live multi-tenant app; 1 hour a week."
    replace_with: "hours logged over the first 3 months after launch"
  - name: fixed_costs_monthly
    value: 451.85
    unit: usd per month
    kind: derived
    formula: fixed_costs_monthly_cash (190.35) + founder_maintenance_hours_monthly (4) x builder_rate_hourly (65.375)
  - name: fixed_costs_monthly_cash
    value: 190.35
    unit: usd per month
    kind: derived
    formula: tmdb_commercial_licence_cost (149) + vercel_pro_price (20) + neon_base_compute_monthly (19.35) + domain (2, estimate)
  - name: bls_software_developer_median_wage
    value: 135980
    unit: usd per year
    kind: sourced
    source: https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
    fetched: 2026-09-25
    quote: "The median annual wage for software developers was $135,980 in May 2025."
  - name: builder_rate_daily
    value: 523
    unit: usd per person-day
    kind: derived
    formula: bls_software_developer_median_wage (135980) / 260 working days
  - name: builder_rate_hourly
    value: 65.375
    unit: usd per hour
    kind: derived
    formula: bls_software_developer_median_wage (135980) / 2080 hours
  - name: builder_hours_per_week_assumed
    value: 10
    unit: hours per week
    kind: estimate
    reasoning: "Hours unstated; 'nights and weekends' read conservatively as 10 h/week = 1.25 working days."
    replace_with: "the decision-maker's stated weekly hours"
  - name: build_person_days_mvp
    value: 32.7
    range: [20.7, 41.1]
    unit: person-days
    kind: estimate
    reasoning: "Solo track, AI-typical roll-up high (26.6 + sqrt 37.51) across 16 tasks using estimating.md section 4 house bands (High 0.6, Med 0.8, Low 1.0); range is AI-leveraged likely to traditional high."
    replace_with: "measured velocity from the concierge spike and the first 2 weeks of the build"
  - name: build_weeks_mvp
    value: 26.2
    range: [16.6, 32.9]
    unit: calendar weeks
    kind: estimate
    reasoning: "Solo AI-typical high 32.7 person-days / 1.25 days per week (10 h/week assumed); range AI-leveraged likely 20.7 to traditional high 41.1, same rate."
    replace_with: "measured velocity from a spike, and stated weekly hours"
  - name: build_cost_mvp
    value: 17102
    range: [10826, 21495]
    unit: usd (value of builder time, not cash)
    kind: estimate
    reasoning: "Solo AI-typical high 32.7 person-days x builder_rate_daily 523 (BLS median); range 20.7 to 41.1 person-days at the same rate."
    replace_with: "measured velocity from a spike, and the builder's own rate"
  - name: build_weeks_mvp_team
    value: 2.3
    range: [1.3, 3.0]
    unit: calendar weeks
    kind: estimate
    reasoning: "Default 6.5-FTE team, AI-typical; critical path tasks 1-2-3-8-15 (8.7 likely, 11.6 high person-days) exceeds effort / 4.55, so the critical path sets calendar."
    replace_with: "measured velocity from a spike"
  - name: build_person_days_concierge
    value: 3.1
    range: [1.3, 4.2]
    unit: person-days
    kind: estimate
    reasoning: "Three tasks (intake and payment link, admin pair switch, delivery process), AI-typical roll-up high; same house bands."
    replace_with: "actual time logged running the spike"
  - name: setup_minutes_per_pair
    value: 40
    unit: minutes of user time per pair (one-off)
    kind: estimate
    reasoning: "Per partner: 60-title grid 5 min, adding in-progress, dropped and wanted titles 5 min, Netflix CSV download, upload and fixes 10 min; x2."
    replace_with: "median setup time measured in the concierge spike"
  - name: competitor_price_low
    value: 3
    unit: usd per user per month
    kind: sourced
    source: https://www.achriom.com/blog/simkl-vs-trakt/
    fetched: 2026-09-25
    quote: "around $3 per month billed yearly"
  - name: competitor_price_high
    value: 5
    unit: usd per user per month
    kind: derived
    formula: trakt_vip_annual_price (60, sourced https://alternativeto.net/news/2025/5/trakt-announces-all-vip-renewals-will-switch-to-a-new-standard-rate-doubling-prices/ "will rise to the current $60 annual price") / 12

RISKS:
  - risk: The conservative cost to serve ($5.27 per pair-month, of which $2.72 is 2.5 founder-minutes) means any price below $5.29 per pair loses money on every pair. That is at or above what a single tracker seat visibly costs ($3–$5 a month), so the product only has margin if couples pay more than one tracker subscription, which nobody has tested.
    severity: high
    confidence: medium
    investigate: a named test, a 2-week fake-door pricing page offering pair plans at $6 and $9 a month, measuring click-to-checkout, run alongside the concierge spike
  - risk: With no streamer history API, setup is about 40 minutes per pair. Imports cover only Netflix (by CSV per profile or a browser extension); Disney+, Prime, Max and Hulu stay manual. If the second partner doesn't finish setup or lets upkeep lapse, the co-watch list loses its input.
    severity: high
    confidence: medium
    investigate: a named test, the concierge spike with 5–10 non-builder couples, measuring setup completion for both partners and the share still updating at day 30
  - risk: Recommendation quality for couples other than the builder's is unmeasured. Published work shows LLM rankers are biased by popularity and prompt position, so the co-watch list may do no better than a simple filtered-popular list.
    severity: high
    confidence: medium
    investigate: a named test, in the concierge spike compare the top-10 Agree rate against a TMDb-popular-on-their-providers baseline and audit 50 whys for factual errors
  - risk: TMDb's JustWatch-sourced availability data needs JustWatch attribution, and it is unknown whether the $149/month TMDb commercial plan grants commercial rights to it. If not, the subscription-aware ranking breaks until a fallback such as Watchmode (+$349/month, which roughly triples cash fixed costs) is integrated.
    severity: high
    confidence: medium
    investigate: the decision-maker emails sales@themoviedb.org for written terms covering commercial display of provider data in CA/US before building
  - risk: The TMDb commercial price comes from a staff forum post, not a published price page or contract. TMDb's terms say fees are at its discretion, and the whole data layer depends on it, so a price or terms change would force a re-platform.
    severity: medium
    confidence: medium
    investigate: the decision-maker gets the $149 plan terms in writing (price, revenue and user caps, notice period for changes) before launch
  - risk: The product depends on one model vendor (Anthropic). The LLM line is 31% of the conservative unit cost, and model retirements force prompt re-tuning. A price rise or deprecation directly moves margin and needs a re-run of the evaluation set.
    severity: medium
    confidence: medium
    investigate: a data pull, log tokens and cost per round from the Anthropic usage field during the spike and re-run the eval set on one alternative model
  - risk: At an assumed 10 hours a week, the solo build takes 21–26 weeks, and the builder's hours may shrink. The work would then stall in a half-multi-tenant state, which is the riskiest place to have partner data.
    severity: medium
    confidence: medium
    investigate: the decision-maker states weekly hours and commits to the concierge-first gate before starting the multi-tenant build
  - risk: The only observed cost figure ("$0.07 of a $15 budget") is about 24 times lower than the conservative model's $1.66 LLM cost per pair-month, so either real usage is far lighter or the figure covers a short period. The token model is unverified in both directions.
    severity: low
    confidence: high
    investigate: the decision-maker exports the Anthropic usage log for the private app (tokens per call, calls per round, rounds per month)
  - risk: Import paths from other trackers are rented land. Trakt reportedly paywalled API-app creation and revoked existing keys in August 2026, and TV Time shut down in July 2026 saying there was "not enough demand for a paid app". Onboarding that relies on them can break without notice.
    severity: medium
    confidence: medium
    investigate: the competitive-strategist confirms current Trakt and Simkl export and API terms, and the TV Time shutdown's lesson for paid demand
