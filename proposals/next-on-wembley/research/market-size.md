# Market size: Next on Wembley

## Bottom line
- **Finding:** A real market exists on paper — roughly 38 million US+Canada households are couples who could plausibly use a two-person TV recommender, from sourced census data. But the closest real comparable is negative: a free TV tracker with 20–26 million users (TV Time) shut down in July 2026 because, in its own words, "there was not enough demand for a paid app." No comparable shows a solo, no-budget builder converting this category to paying customers. The conservative 3-year obtainable estimate is ~4,000 paying households (~$203,000/year revenue at the lowest comparable price) — not a guess, but resting on a thin, unverified chain of reasoning, not a direct comparable.
- **Your questions:** Q1: Yes, there is a real market beyond the builder's household — tens of millions of qualifying couple households exist in the US and Canada (sourced). But there is no sourced evidence that couples will *pay* for this specific product category: the nearest comparable (a professionally run, VC-backed TV tracker at 20x+ this idea's target scale) concluded the opposite in the same year as this run.
- **Assumptions:** A7 (market size bounds the business) is part-evidenced: the serviceable market is large and sourced, but the obtainable share and willingness-to-pay are unproven, and the one closest comparable points against it.

## Method note
No figures in this file are from memory. Every count below was fetched today (2026-09-25) from the source named next to it. Where I applied a US-sourced rate to Canada because no Canada-specific figure was found in the time available, I say so and mark that step `estimate`, not `sourced`.

## Funnel

### Raw inputs (fetched today unless noted)

| Input | Value | Kind | Source | Geography | Year |
|---|---|---|---|---|---|
| `us_households` | 134,790,000 | sourced | [FRED TTLHH](https://fred.stlouisfed.org/series/TTLHH) (Census Bureau data): "134,790 thousand households... Not Seasonally Adjusted," updated Dec 4, 2025 | US | 2025 |
| `us_coupled_household_share` | 0.532 | sourced | [Census Bureau, "Coupled Households Declined..."](https://www.census.gov/library/stories/2023/05/coupled-households-declined-in-2020.html): "Coupled households represented 53.2% of all U.S. households in 2020" (2020 Decennial Census, released May 25, 2023) | US | 2020 |
| `us_households_2plus_subs_share` | 0.53 | sourced | [Cloudwards, "35 Streaming Services Statistics"](https://www.cloudwards.net/streaming-services-statistics/), citing Leichtman Research Group: "53% of households have at least four streaming service subscriptions." Used as a conservative floor for "2 or more" — logically, if 53% have 4+, at least 53% have 2+ | US | ~2025 (exact LRG publication date not visible in the citing article) |
| `us_broadband_household_share` | 0.912 | sourced | Search-verified figure (not independently re-fetched from Census.gov, which returned 403): "91.2 percent of all U.S. households reported having some form [of] internet subscription in 2022," US Census data | US | 2022 |
| `ca_households` | 14,978,941 | sourced | [Wikipedia, "2021 Canadian census"](https://en.wikipedia.org/wiki/2021_Canadian_census), citing Statistics Canada: "14,978,941 occupied private dwellings" | Canada | 2021 |
| `ca_couple_family_households` | 8,576,580 | sourced | [ToDoCanada, "Census 2021: How Many Married Couples..."](https://www.todocanada.ca/census-2021-how-many-married-couples-families-with-children-are-there-in-canada/), citing Statistics Canada: "Canada has a total of 6,627,305 married-couple families and 1,949,275 common-law couple families" (6,627,305 + 1,949,275 = 8,576,580). A direct StatCan fetch could not surface this exact figure in fetchable text; this is a secondary citation of the July 13, 2022 StatCan release | Canada | 2021 |
| `ca_quebec_households` | 3,749,035 | sourced | Search-verified: "Quebec's population was... living in 3,749,035 of its 4,050,164 total dwellings" (Statistics Canada, 2021 Census) | Canada (Quebec) | 2021 |
| `ca_quebec_french_predominant_share` | 0.775 | sourced | Search-verified: "In Quebec, 77.5% of the population spoke French predominantly at home" (Statistics Canada, 2021 Census, via CBC News coverage of StatCan release) | Canada (Quebec) | 2021 |
| `trakt_mau` | 811,000 | sourced | [PCWorld, Apr 30, 2025](https://www.pcworld.com/article/2607062/trakt-helps-you-keep-track-of-your-streaming-shows.html): "it has roughly 811,000 monthly active users"; "Trakt has been around since 2010" (co-founder Justin Nemeth) | US/global (single-user TV/movie tracker, not couple-specific) | 2025 (15 years of operation) |
| `tvtime_lifetime_installs` | 26,400,000 | sourced | [TechCrunch, Jul 2, 2026](https://techcrunch.com/2026/07/02/popular-tv-tracking-app-tv-time-is-shutting-down-as-company-focuses-on-ai/): "TV Time had substantial reach with over 26.4 million lifetime installs" | US/global | 2026 (shutdown announcement) |
| `competitor_price_low` | 49.99 usd/year | sourced | [Sofa pricing page](https://www.sofahq.com/pricing), fetched 2026-09-25: "Super Sofa... Annual: $49.99 per year" | US (app store pricing) | 2026 |

### Funnel arithmetic

| Level | Geography | Count | Formula | Year(s) used |
|---|---|---|---|---|
| total_customers (US) | US | 38,005,388 | `us_households (134,790,000) × us_coupled_household_share (0.532) × us_households_2plus_subs_share (0.53)` | 2025 household count × 2020 coupling share × ~2025 subscription share — **years mismatched, flagged** |
| total_customers (Canada) | Canada | 4,545,587 | `ca_couple_family_households (8,576,580) × us_households_2plus_subs_share (0.53, applied cross-border as `estimate` — no Canada-specific figure found)` | 2021 households × US-sourced subscription rate |
| **total_customers (combined)** | US + Canada | **42,550,975** | sum of the two rows above | mixed, see above |
| serviceable_customers (US) | US | 34,660,914 | `total_customers US (38,005,388) × us_broadband_household_share (0.912)` | 2022 broadband rate |
| serviceable_customers (Canada) | Canada | 3,341,334 | `total_customers Canada (4,545,587) × us_broadband_household_share (0.912, applied cross-border as estimate) × ca_english_primary_share (0.806, derived below)` | 2021/2022 mixed |
| **serviceable_customers (combined)** | US + Canada | **38,002,248** | sum of the two rows above | mixed |
| obtainable_customers | US + Canada | **~4,055** | see reasoning below (`estimate`) | 3-year horizon from a 2026 launch |

**`ca_english_primary_share` derivation (estimate):** `1 − (ca_quebec_households / ca_households × ca_quebec_french_predominant_share)` = `1 − (3,749,035 / 14,978,941 × 0.775)` = `1 − (0.250 × 0.775)` = `1 − 0.194` = `0.806`. This treats Quebec's household-level French-predominance as proportional to its population-level rate (StatCan reports the population figure, not a household figure), and assumes the product is English-only in v1 (not stated in `idea.md`, but no localization is mentioned anywhere in the frame — flagged as an assumption, not a stated fact).

**obtainable_customers reasoning (estimate, conservative end):**
1. The closest comparable for a small, independently-run TV/movie tracker with no significant marketing budget is Trakt.tv: `trakt_mau` = 811,000 monthly active users after 15 years of operation (2010–2025), as a **single-user** product with **no signup requirement to use the core product**.
2. This product needs a materially higher-friction adoption: **two** people must sign up and keep data current by hand (no import API — confirmed by the opportunity-model's A2), a harder ask than Trakt's single-user, low-friction logging.
3. Taking a deliberately conservative ceiling — 1% of Trakt's 15-year cumulative reach as what a zero-budget solo builder could plausibly touch in 3 years, given the shorter horizon and higher friction: `811,000 × 0.01 = 8,110` individual users.
4. Halving for the pair requirement (every household needs two people, and this figure already counts individuals, so treating it as generously as possible — every touched individual finds a partner who also joins): `8,110 / 2 = 4,055` households.
5. This does **not** discount further for paid conversion (Trakt's core product is free; VIP is optional). `market_value_obtainable` below assumes all 4,055 pay the conservative price, which is generous. **Replace with:** actual signups and completed-pair rate from a named landing-page/fake-door test (see `investigate` in RISKS below), and the TMDb-cost model once a commercial quote exists.

## Value

| Level | Count | Price | Value/year | Formula |
|---|---|---|---|---|
| market_value_total | 42,550,975 households | $49.99/year (sourced, Sofa, conservative/low end) | **$2,127,123,240** (~$2.13B) | `total_customers × competitor_price_low` |
| market_value_serviceable | 38,002,248 households | $49.99/year | **$1,899,732,378** (~$1.90B) | `serviceable_customers × competitor_price_low` |
| market_value_obtainable | 4,055 households | $49.99/year | **$202,709** (~$203K) | `obtainable_customers × competitor_price_low` |

**Price is not yet a decision** — it belongs to the venture-strategist. $49.99/year is the lowest annual price among the comparables checked, all single-user trackers, not two-person recommenders:
- Sofa Super Sofa: $49.99/year or $5.99/month (sourced, quote above)
- Trakt VIP: reportedly $60/year as of mid-2025, up from a former $15–30/year (search-sourced only, not independently fetched with a direct quote — lower confidence than the Sofa figure)
- Letterboxd Patron (movies, not TV, least comparable): reportedly $49/year (search-sourced only, same caveat)

`competitor_price_low` = $49.99/year (Sofa). `competitor_price_high` = $60/year (Trakt, lower-confidence sourcing).

## What's excluded and why
- **Geographies outside the US and Canada.** Hard constraint from `idea.md`.
- **S4 (multi-adult households beyond couples)** and **S3 (remote co-watching couples in separate homes)**, per the opportunity model's segment table — S3 doesn't cleanly fit "household," and both are out of scope for v1 ("starting with couples").
- **Non-English-primary Quebec households** — excluded from `serviceable_customers` under the assumption the v1 product is English-only (not stated; flagged as my assumption, not a fact from `idea.md`).
- **Households without home internet/broadband** — excluded from `serviceable_customers` (0.912 US-sourced rate).
- **Couples who don't actually watch shared serialized TV.** I could not independently verify a sourced rate for "share of coupled households that co-watch TV regularly" — the only figures found (e.g., "52% of couples watch TV together regularly") came from marketing-panel surveys (Pollfish/CableTV.com, n=1,000, US only) that I could not confirm with a direct, quotable fetch matching that specific claim. Rather than bake an unverifiable number into `total_customers`, I left it out and flag it here: if a real co-watching-frequency filter of roughly 50% applied, **`total_customers` and `serviceable_customers` would roughly halve**, and so would every value figure derived from them.
- **Regulatory exclusions** (TMDb/JustWatch/Anthropic commercial-terms eligibility) are **not applied here** — per the routing brief, those are the regulatory-scout's job and get folded in at the business-case stage.
- **Willingness-to-pay at any specific price** is not modeled beyond the conservative comparable price; the actual price is a business-case decision.

## Top-down cross-check
Analyst reports for a "Content Recommendation Engine Market" gave wildly disagreeing 2025 figures across sources found in search: $8.49B (one report), $10.79B, $10.6B, and $6.15B, projected to reach $26B–$133B by the early-to-mid 2030s at 28–38% CAGR (various market-research-report landing pages, not independently fetched or reconciled). **`confidence: low`. Not used as a headline number**, per the contract.

This figure is a poor match for this idea on every dimension that matters: it is a **global B2B market** for recommendation-engine infrastructure sold to platforms and e-commerce sites (Google, AWS-class buyers), not a **consumer subscription market** for a two-person household app in the US and Canada. The unit, buyer, and geography all differ from the bottom-up analysis above, which is why the bottom-up figures — not this one — are the ones to act on.

## Why now
- **Headwind, sourced and specific to this exact category.** TV Time, a TV/movie tracking app with 26.4 million lifetime installs and $50M in VC funding (Whip Media Group), shut down July 15, 2026. The company's stated reason: "it was no longer sustainable to continue operating the service as a free app, and there was not enough demand for a paid app" ([TechCrunch, Jul 2, 2026](https://techcrunch.com/2026/07/02/popular-tv-tracking-app-tv-time-is-shutting-down-as-company-focuses-on-ai/)). This is the single most relevant piece of market evidence found in this run: a much larger, professionally marketed competitor in the same category concluded, in the same year as this proposal, that paid demand for TV tracking doesn't exist at a sustaining level.
- **Mild tailwind, same story.** Within a month of TV Time's shutdown, its original co-founder launched a successor, Bingers, funded by user donations rather than subscriptions, after "more than 28,000 users signed a petition requesting its revival" ([TechCrunch, Aug 4, 2026](https://techcrunch.com/2026/08/04/tv-time-co-founder-launches-bingers-to-revive-the-beloved-tv-tracking-app/)). This shows real organic, non-marketed demand for TV tracking persists — but the successor still isn't charging a subscription, which is further evidence against this idea's likely revenue model, not for it.
- **Tailwind, sourced.** LLM inference costs have fallen sharply, supporting the idea's premise that personalized "why" text is now cheap to generate. Epoch AI's price-trend analysis found "the price to achieve GPT-4's performance on a set of PhD-level science questions fell by 40x per year," with the rate of decline "ranging from 9x to 900x per year" depending on task ([Epoch AI, "LLM inference prices have fallen rapidly but unequally across tasks"](https://epoch.ai/data-insights/llm-inference-price-trends), fetched 2026-09-25).
- **Weak tailwind, sourced.** Subscription-fatigue and catalogue growth are real: households average multiple streaming subscriptions and report frustration with the number of services (search-sourced: "62% Say There Are Too Many Streaming Options," Motley Fool, not independently fetched with a direct quote). This supports the idea's "why it's getting harder" claim but doesn't by itself establish willingness to pay for a solution.
- **Net read:** the strongest, most specific, most recent piece of evidence found points against paid demand for this exact product category, not toward it.

## Sensitivity
The single input that moves `obtainable_customers` the most is the **share of Trakt's 15-year cumulative reach assumed captured in 3 years** (used at 1%, an unsourced conservative judgment call — there is no comparable that gives this rate directly for a zero-budget solo builder).
- At 1% (used above): `obtainable_customers` ≈ 4,055 households, `market_value_obtainable` ≈ $203,000/year.
- At 5%: `obtainable_customers` ≈ 20,275 households, `market_value_obtainable` ≈ $1,013,500/year — a 5x swing from a single, unsourced judgment call.
- At 0.1% (equally plausible given TV Time's evidence that even mass free adoption didn't convert to paid demand): `obtainable_customers` ≈ 406 households, `market_value_obtainable` ≈ $20,300/year.

This is the honest center of the uncertainty in this file: everything from `total_customers` through `serviceable_customers` rests on named government/primary sources and is recomputable to within rounding. Everything from `obtainable_customers` onward rests on one judgment call anchored to one imperfect comparable, and a named test (below) is the only way to replace it with a real number.

## Open questions for the decision-maker
1. TV Time's own stated reason for shutting down — "not enough demand for a paid app" — is the single most on-point piece of evidence found in this research. Does that change how you'd want to test willingness to pay before building further?
2. If Bingers (the direct successor, run by TV Time's own co-founder) is using a donation model rather than a subscription, is a subscription still the right revenue model to test first?

KEY_FIGURES:
  - name: total_customers
    value: 42550975
    unit: households (US + Canada, couples with 2+ paid streaming subscriptions)
    kind: derived
    formula: "us_households (134,790,000, sourced) × us_coupled_household_share (0.532, sourced) × us_households_2plus_subs_share (0.53, sourced) + ca_couple_family_households (8,576,580, sourced) × us_households_2plus_subs_share (0.53, applied cross-border as estimate)"
  - name: serviceable_customers
    value: 38002248
    unit: households (US + Canada, broadband-connected, English-primary where applicable)
    kind: derived
    formula: "total_customers_US (38,005,388) × us_broadband_household_share (0.912, sourced) + total_customers_CA (4,545,587) × us_broadband_household_share (0.912, applied cross-border as estimate) × ca_english_primary_share (0.806, derived from StatCan Quebec figures)"
  - name: obtainable_customers
    value: 4055
    unit: households, within 3 years of launch
    kind: estimate
    reasoning: "1% of Trakt's 811,000 15-year monthly-active-user comparable (sourced, PCWorld Apr 2025), taken as a conservative ceiling for a higher-friction, zero-budget, 3-year effort, then halved for the two-person signup requirement (8,110 / 2 = 4,055). Does not further discount for paid conversion, which TV Time's shutdown evidence suggests would cut this further."
    replace_with: "actual signups and completed-pair rate from a 2-week landing-page/fake-door test with paid social spend (the gtm-researcher's named test for A4), plus real paid-conversion data once a price is live"
  - name: market_value_total
    value: 2127123240
    unit: usd per year
    kind: derived
    formula: "total_customers (42,550,975) × competitor_price_low (49.99 usd/year)"
  - name: market_value_serviceable
    value: 1899732378
    unit: usd per year
    kind: derived
    formula: "serviceable_customers (38,002,248) × competitor_price_low (49.99 usd/year)"
  - name: market_value_obtainable
    value: 202709
    unit: usd per year
    kind: derived
    formula: "obtainable_customers (4,055) × competitor_price_low (49.99 usd/year)"
  - name: competitor_price_low
    value: 49.99
    unit: usd per year
    kind: sourced
    source: https://www.sofahq.com/pricing
    fetched: 2026-09-25
    quote: "Super Sofa... Annual: $49.99 per year"
  - name: competitor_price_high
    value: 60
    unit: usd per year
    kind: sourced
    source: https://www.neowin.net/news/trakt-vip-receives-up-to-300-price-hike-going-back-on-promise-to-honor-legacy-subs/
    fetched: 2026-09-25
    quote: "Trakt VIP costs $60 billed yearly"
    note: "Via search synthesis of this article; the page itself returned HTTP 403 on direct fetch, so this carries lower confidence than competitor_price_low."
  - name: price
    value: null
    unit: usd per pair per month
    kind: unknown
    settle_with: "decision in the business case, informed by this file's competitor_price_low/_high band"

RISKS:
  - risk: The closest real comparable to this product — TV Time, a TV/movie tracker with 26.4 million lifetime installs and VC funding — shut down in 2026 specifically because there was "not enough demand for a paid app." This is direct, recent, category-specific evidence against the core premise that couples will pay for TV tracking and recommendation software, not just an absence of evidence.
    severity: high
    confidence: high
    investigate: "a named test, a 2-week landing page with a real price shown and $300 of paid social, measuring click-to-signup and stated willingness to pay, before further build investment"
  - risk: obtainable_customers (~4,055 households, ~$203K/year) rests on a single unsourced judgment call — that a zero-budget solo builder captures 1% of a 15-year comparable's user base in 3 years — not on a comparable that directly measures a solo builder's 3-year reach. The sensitivity analysis shows this figure could reasonably range from ~400 to ~20,000+ households depending on that one assumption.
    severity: high
    confidence: medium
    investigate: "a named test, the same landing-page/fake-door test above, run long enough to produce an actual signups-per-week rate that replaces the 1% assumption"
  - risk: The "2+ paid streaming subscriptions" and "home broadband" rates used for Canada are US-sourced figures applied cross-border, not Canada-specific data, because no Canada-specific figure was found in the time available. If Canadian streaming-subscription or broadband penetration differs meaningfully from the US, the Canada-side ~4.5M and ~3.3M figures move accordingly (roughly 10% of the combined total_customers and serviceable_customers figures, so the effect on the combined headline is modest but not zero).
    severity: medium
    confidence: medium
    investigate: "a data pull, fetch CRTC (Canadian Radio-television and Telecommunications Commission) or StatCan survey data on streaming subscription counts and broadband penetration by household"
  - risk: total_customers and serviceable_customers do not apply any discount for "couples who don't actually co-watch serialized TV together," because no verifiable, quotable source for that rate was found in the time available (only unverifiable marketing-panel survey claims). If a real co-watching-frequency filter of roughly 50% exists, as weak secondary evidence suggests, every count and value figure in this file would roughly halve.
    severity: medium
    confidence: low
    investigate: "the problem-validator's interviews should ask directly how often couples watch shared serialized TV, to replace this gap with real data"
  - risk: The value figures use $49.99/year, the lowest price among three single-user TV/movie tracker comparables, none of which serve two people or require both partners' data. A two-person recommender could plausibly command a higher per-household price, but could equally face resistance for asking one household to pay for what feels like a single-user tool used by two people — this cuts both ways and is unresolved.
    severity: low
    confidence: medium
    investigate: "the venture-strategist sets price using this file's competitor_price_low/_high band and the problem-validator's findings on perceived value"
