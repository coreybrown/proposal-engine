# Run digest: next-on-wembley

Generated 2026-09-25 14:00 by `scripts/digest.py`. Everything below is copied verbatim from the files listed. Read this instead of every file; open a file only to settle a specific question.

## Compliance

| File | Agent | Stage check |
|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | pass |
| `research/problem.md` | problem-validator | pass |
| `research/market-size.md` | market-sizer | pass |
| `research/competition.md` | competitive-strategist | pass [KILL] |
| `research/go-to-market.md` | gtm-researcher | pass |
| `research/build-and-run.md` | build-cost-analyst | pass |
| `research/regulatory.md` | regulatory-scout | pass |

## Bottom lines

### opportunity-framer: `research/opportunity-model.md`

- **Finding:** This is a working personal tool used by one household, the builder's own. It is a candidate consumer web product, and every commercial premise is untested. The idea rests on three behaviours nobody has observed outside that household: two partners both enter and maintain their watch history by hand, the second partner actually joins, and people pay for a tool they reach for only between shows. On top of that, a TMDb commercial agreement is required before charging (confirmed from TMDb's terms), at a cost nobody knows yet.
- **Assumptions:** A1–A6 and A8 are untested, or rest only on the builder's word. A7 is part-evidenced: a TMDb commercial agreement is required, but its price and terms are unknown. A2 is part-evidenced: Netflix's only export is a manual, per-profile CSV.

### problem-validator: `research/problem.md`

- **Finding:** Outside the builder's household, real people complain about the "what should we watch" decision as a couple, and at least five independent teams have built apps to solve exactly that overlap problem — one of them (Matched) has ~170k downloads, a 4.7/5 rating and a paid tier. But every one of those comparable apps solves it with a swipe, not with the manual watch-history, ratings and in-progress logging this idea requires from both partners — and the closest cost analogue for that heavier ask, TV Time (25–26M users, free, manual logging), shut down in July 2026 because, in its own words, "there was not enough demand for a paid app."
- **Your questions:**
  - Q1: Yes, the problem exists beyond one household — organic complaints and five competing apps confirm it — but the only clean willingness-to-pay signal (Matched's $2.99/mo tier) belongs to a lighter-weight swipe product, not to one that asks for manual history entry.
  - Q2: Manual upkeep is tolerated by a minority of enthusiasts (Letterboxd: 30M+ users log manually; Trakt has paying VIP subscribers) but is explicitly named as the reason people abandon TV trackers, and the segment's own biggest free player (TV Time) could not convert scale into paid demand. Tolerance is real but partial, and it degrades the moment logging becomes a per-episode, per-partner chore rather than a one-time swipe session.
  - Q3: Frequency of the underlying "what to watch" decision looks high (a UserTesting survey puts individual decision time at ~110 hours/year), but no source measures how often a couple specifically starts a *new series* together. That figure is unknown, and it is the one this idea most needs.
- **Assumptions:** A1 holds outside the builder's household (organic complaints and five competing apps exist); A2 is contradicted for the heavier design this idea proposes (comparable apps use swiping, not full watch-history entry, and the segment's largest free tracker shut down over the paid version having too little demand).

### market-sizer: `research/market-size.md`

- **Finding:** A real market exists on paper — roughly 38 million US+Canada households are couples who could plausibly use a two-person TV recommender, from sourced census data. But the closest real comparable is negative: a free TV tracker with 20–26 million users (TV Time) shut down in July 2026 because, in its own words, "there was not enough demand for a paid app." No comparable shows a solo, no-budget builder converting this category to paying customers. The conservative 3-year obtainable estimate is ~4,000 paying households (~$203,000/year revenue at the lowest comparable price) — not a guess, but resting on a thin, unverified chain of reasoning, not a direct comparable.
- **Your questions:** Q1: Yes, there is a real market beyond the builder's household — tens of millions of qualifying couple households exist in the US and Canada (sourced). But there is no sourced evidence that couples will *pay* for this specific product category: the nearest comparable (a professionally run, VC-backed TV tracker at 20x+ this idea's target scale) concluded the opposite in the same year as this run.
- **Assumptions:** A7 (market size bounds the business) is part-evidenced: the serviceable market is large and sourced, but the obtainable share and willingness-to-pay are unproven, and the one closest comparable points against it.

### competitive-strategist: `research/competition.md`

- **KILL:** Free or near-free substitutes already do the core job — decide what a couple watches together — with far less setup than this product requires, and the closest scale analog to a logging-heavy tracker (TV Time, 20M+ registered users) shut down in 2026 because, in its own operator's words, "it was no longer sustainable to continue operating the service as a free app, and there was not enough demand for a paid app" (TechCrunch, fetched 2026-09-25). The "for couples" swipe-match niche (Matched, MatchWatch, Shared Watchlist: Couple Match, WeWatch Together, MatchaFilm) is already crowded, occupying exactly the low-effort positioning this product would need to win, while showing weak or negligible traction of its own. Trakt already holds both partners' watch history and a friend graph, and its own users have an unresolved, years-old request for a two-person overlap comparison — the fastest, cheapest path to this feature belongs to an incumbent, not a new entrant.
- **Your questions:** Q1: existing comparable trackers charge $0–$5/month typically (Simkl Supporter $1/mo, Trakt VIP ~$2.50–5/mo equivalent, JustWatch Pro $2.49/mo), and the couple-specific apps found are mostly free or low-traction paid, so no clean evidence anyone pays meaningfully for this exact job. Q2: every live couple-matching app sidesteps the onboarding problem by not requiring imported watch history at all (live swipe sessions or a light want-to-watch list); this is the one clear workaround, but it means abandoning the deep personalization the idea is built around. Q3: the closest low-frequency, logging-heavy analog (TV Time) proved retention/monetization does not survive at that frequency even at 20M+ users; low-cost tracker add-ons ($1–3/mo) or one-time purchases (TV Time's $74.99 lifetime tier) are the only pricing patterns with any signal of tolerance. Q5: the observed price band across comparable trackers and couple apps is roughly $0–$40/year per person (see KEY_FIGURES), well below what a TMDb-licensed, LLM-driven product would likely need to charge to cover its cost to serve.
- **Assumptions:** A5 contradicted — free, purpose-built two-person overlap tools already exist (Matched, MatchWatch, WeWatch Together) and the harder, deeper version of the same idea (persistent watch history + LLM ranking) is a plausible near-term feature add for Trakt or Simkl, who already hold the data and have an open user request for it. A2 partly addressed — workarounds exist industry-wide, but every one of them abandons history-based personalization rather than solving the import problem. A3 evidenced negatively by TV Time's operator-stated shutdown reason.

### gtm-researcher: `research/go-to-market.md`

- **Finding:** No channel is free, and none is cheap at scale. Manual, community-led outreach can plausibly land the first 10-100 pairs at an estimated ~$240/pair in founder time (below the ~$49-60/year comparable price only if lifetime value spans several years, which is unproven). Every channel that could scale past that — paid social, paid search, influencer spend — has an unknown or likely-unaffordable CAC at this price, and the product's own choices (web-only, no app store presence) remove the one channel (app-store search/browse) that the closest comparables actually use to acquire users for free.
- **Assumptions:** A4 mostly contradicted at scale, holds narrowly for a hand-built first cohort — the builder has no paid-acquisition budget or audience, and the one plausible channel (organic community engagement) is bounded by his own hours, not by market size, and by an unsourced pair-completion rate.
- **Kill check:** not a kill — I found no evidence that reaching the segments is categorically impossible at the observed comparable prices — a founder-time-only channel exists for a small first cohort — but I also found no evidence of a channel that both reaches pairs (not just individuals) and scales beyond the builder's personal hours at an affordable CAC. That gap is a high-severity, unresolved risk, not a proven kill.

### build-cost-analyst: `research/build-and-run.md`

- **Finding:** Building it is not the problem. Turning the private app into a paid multi-tenant product takes an estimated 26.6–32.7 person-days (Solo, AI-typical), which is 21–26 calendar weeks at an assumed 10 hours a week. Running it is the problem. The conservative cost to serve is **$5.27 per pair-month**, and any price below **$5.29 per pair-month** loses money on every pair before fixed costs. That sits at the top of the visible single-seat tracker band of $3–$5 per month. The kill condition was not fired, because trackers charge per person and this product is sold per pair. It is borderline.
- **Your questions:** Q2: No full workaround exists. A Netflix CSV or browser-extension import plus tracker-file imports can cut setup to about 40 minutes per pair, but Disney+, Prime, Max and Hulu stay manual. That doesn't kill the product on build grounds; whether pairs tolerate it is the test that decides it. Q4 (fees): TMDb commercial is **$149/month flat** under $1M revenue (a TMDb staff post, not a published price page). Whether that covers the JustWatch availability data is unknown, and the fallback is Watchmode at **$349/month**. Q5 (cost): $5.27 per pair-month conservative, of which $2.54 is cash and $2.72 is 2.5 founder minutes. On top of that come $451.85/month fixed ($190.35 cash plus 4 founder hours).
- **Assumptions:** A8 partly holds: the build fits the hours available. The cost part fails: cost to serve is not "well below" tracker-level prices unless a pair pays more than one tracker seat. A2 unproven: imports cover Netflix only (Simkl documents that other streamers have no history API). A6 part-evidenced: TMDb's fee is known, but JustWatch's commercial terms are not.

### regulatory-scout: `research/regulatory.md`

- **Finding:** No regulator licenses this business — it's an unregulated consumer web app, not a money-transmission, gambling, health, or advice-liability activity. The real gate is contractual, not statutory: **TMDb's terms restrict use of its API "in connection with... a machine learning (ML) or artificial intelligence (AI) based Application"** and name LLMs/chatbots as a use that requires a separate written commercial agreement (TMDb API Terms of Use, fetched 2026-09-25) — and this product's core feature is an LLM generating picks from TMDb data. Whether TMDb will license that use at all, and at what cost, is unknown and untested. A second, separate gate sits behind it: JustWatch's own terms (the source of the streaming-availability data TMDb passes through) separately ban commercial use and scraping of "the Service Content," with no public commercial path stated on JustWatch's own terms page.
- **Your questions:**
  - Q4: TMDb requires a written commercial agreement for any paid app, explicitly calls out LLM/chatbot use as needing one, caps caching at 6 months, and requires logo attribution; cost and AI-use approval are both unconfirmed. JustWatch's own terms add a second, separately unresolved licensing question for the streaming-availability data. Anthropic's terms permit commercial use of outputs with no product-category restriction found. See Licenses and IP and liability below.
  - Q2 (contributing): No safe terms-of-use workaround exists to auto-capture watch history. Netflix's Terms of Use (fetched 2026-09-25) ban "any robot, spider, scraper or other automated means," "data mining, data gathering or extraction," and any use "in connection with... training... any machine learning tool" — this covers a browser extension or scraper built to read a user's own logged-in Netflix history page. Other major streamers were not individually checked in this pass but commonly carry similar anti-automation clauses; treat that as unverified, not assumed-safe. This does not by itself kill the product (manual entry and tracker-app imports remain open), but it forecloses the most obvious way to reduce onboarding friction.
  - **Assumptions:** A6 (opportunity model) remains unproven and is now more specifically located: it isn't just "TMDb requires a commercial agreement," it's "TMDb's terms single out AI-based apps as requiring one, and it's unknown whether they grant it to a solo builder." A2 is reinforced: manual/import-based history capture isn't just the only option because no API exists — it's also because automated capture would breach at least Netflix's ToS.

## What must be true (from opportunity-model.md)

Ranked by importance times uncertainty. IDs follow the ranking.

| ID | Assumption | Lens | Why the idea depends on it | Evidence status | Tested by |
|---|---|---|---|---|---|
| A1 | Outside the builder's household, a meaningful share of S1 couples report that choosing the next shared series is a recurring problem. It costs them noticeable time or friction, and they would try a dedicated tool rather than their current workaround (one partner decides, word of mouth, the streamer's home screen). | Problem | If couples settle this quickly with free habits, there is no product, only a personal tool. | Asserted in idea ("people ask about" the co-watch list). Anecdote of unknown size. Otherwise untested. | problem-validator |
| A2 | Enough pairs will complete setup for **both** partners (history, ratings, subscriptions) and keep it current by hand or via a partial import (e.g. the Netflix per-profile CSV, or export from an existing tracker). Recommendations need that to stay useful. | Build & run | With no streamer API, all input data comes from user effort. If the second partner never logs, or logging lapses after the first show, the co-watch list degrades to guesswork. | Part-evidenced: Netflix's only export is a manual, per-profile CSV (Netflix Help Center, see the claims table). That other streamers have no API is asserted. Tolerance for the burden is untested. | build-cost-analyst (workarounds); problem-validator (tolerance) |
| A3 | A product used a few times a month (between shows) keeps pairs subscribed, or supports a one-time price, at a level above the cost to serve. | Economics | Low frequency usually means high churn on subscriptions. If retention collapses between uses, no price covers acquisition. | Untested. The builder names this as a risk. | venture-strategist (model); problem-validator (how often the decision happens) |
| A4 | A solo builder with no audience and no capital can acquire pairs through organic or low-cost channels at a cost below what the price supports, **and** the invite step (the second partner joining) doesn't cut conversion so much that paid pairs become too costly. | Go-to-market | Every signup needs two activations. The builder has no distribution. | Untested | gtm-researcher |
| A5 | No free or incumbent product (trackers, availability guides, streamers' household features) already gives couples a satisfying two-person overlap recommendation. The overlap is also hard enough that an incumbent can't add it as a quick feature. | Competition | If the differentiator is already a free feature, or trivially copyable by apps that hold the history, there's no wedge. | Untested | competitive-strategist |
| A6 | Commercial use of TMDb metadata and provider data, the JustWatch-sourced availability data, and Anthropic-generated text is permitted in Canada and the US on terms and at a cost the economics can bear. Caching and attribution limits must also be workable. | Legal & trust | TMDb is the data layer for the whole product. Replacing it could mean re-platforming. | Part-evidenced: TMDb requires a written commercial agreement for paid apps and caps caching at 6 months, and its provider data must be attributed to JustWatch (both sourced below). Price, availability to a solo builder, and the JustWatch and Anthropic terms are untested. | regulatory-scout |
| A7 | Canada and the US together hold enough S1/S2 couples who would pay to sustain at least a solo-sized business, after removing couples who don't co-watch serialized TV or who share a single streaming profile. | Market | Market size bounds everything else. | Untested (no figures provided) | market-sizer |
| A8 | At multi-household scale, the variable cost per pair (LLM calls, TMDb and provider data, hosting, support time) stays well below any viable price. The builder can also turn the private app into a secure multi-tenant web product (signup, pair invite, partner-data separation, billing, import) in the hours available. | Economics | The asserted single-household LLM spend doesn't show what an arbitrary household would cost. Any licence fee is fixed cost a small subscriber base must cover. | Asserted on the project page ($0.07 against a $15 monthly budget, one household, period unclear). Untested at scale. | build-cost-analyst |

**Lens coverage:**
- Problem: A1
- Market: A7
- Competition: A5
- Economics: A3, A8
- Go-to-market: A4
- Build & run: A2
- Legal & trust: A6

All seven lenses are load-bearing. Trust issues are routed to ethics-trust-safety through RISKS:
- the privacy of each partner's ratings from the other
- how an account splits when a relationship ends
- the accuracy of LLM "whys"

## Question routing (from opportunity-model.md)

| Q# | Question (verbatim) | Owner agent | Contributing agents |
|---|---|---|---|
| Q1 | Is there a real market of households who'd pay for a two-person recommender, or does this only work for us? | market-sizer | problem-validator (does the problem exist beyond one household, and is there any willingness-to-pay signal); competitive-strategist (what comparable trackers charge, and whether anyone pays) |
| Q2 | Watch history isn't available from the streamers, so setup and upkeep fall on the user. Is there any way around that, and if not, does it kill the product? | build-cost-analyst | competitive-strategist (how existing trackers solve onboarding and import); problem-validator (whether users tolerate manual upkeep); regulatory-scout (terms risk of scraping, browser-extension capture or third-party tracker APIs) |
| Q3 | It's a low-frequency product: you only need it between shows. Can something used a few times a month hold users or justify a price? | venture-strategist | problem-validator (how often couples face the decision); competitive-strategist (retention and pricing of comparable low-frequency consumer apps); unit-economics-auditor (breakeven churn) |
| Q4 | What are the licensing and terms-of-use limits on TMDb, streaming-availability data and LLM-generated recommendations if this goes commercial? | regulatory-scout | build-cost-analyst (licence fees in the cost to serve) |
| Q5 | What would it cost to run per household, and what could it charge? | unit-economics-auditor | build-cost-analyst (cost to serve: LLM, data licence, hosting, support); competitive-strategist (price band); venture-strategist (the price decision) |

## Drift check

- Not run yet: there is no business case.

## Figures by name

### bls_software_developer_median_wage

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 135980 | usd per year | sourced | https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm |

### build_cost_mvp

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 17102 | usd (value of builder time, not cash) | estimate | Solo AI-typical high 32.7 person-days x builder_rate_daily 523 (BLS median); range 20.7 to 41.1 person-days at the same rate. |

### build_person_days_concierge

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 3.1 | person-days | estimate | Three tasks (intake and payment link, admin pair switch, delivery process), AI-typical roll-up high; same house bands. |

### build_person_days_mvp

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 32.7 | person-days | estimate | Solo track, AI-typical roll-up high (26.6 + sqrt 37.51) across 16 tasks using estimating.md section 4 house bands (High 0.6, Med 0.8, Low 1.… |

### build_weeks_mvp

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 26.2 | calendar weeks | estimate | Solo AI-typical high 32.7 person-days / 1.25 days per week (10 h/week assumed); range AI-leveraged likely 20.7 to traditional high 41.1, sam… |

### build_weeks_mvp_team

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 2.3 | calendar weeks | estimate | Default 6.5-FTE team, AI-typical; critical path tasks 1-2-3-8-15 (8.7 likely, 11.6 high person-days) exceeds effort / 4.55, so the critical … |

### builder_cowatch_agreement_top10

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | 0.6 | share of co-watch top-10 picks both partners agree on (one household; target or actual unclear) | sourced | https://coreywbrown.com/projects/next-on-wembley/ |

### builder_hourly_opportunity_cost

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/go-to-market.md` | gtm-researcher | 80 | usd per hour | sourced | https://www.bls.gov/news.release/ocwage.t01.htm |

### builder_hours_per_week

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | None | hours per week | unknown | the decision-maker states available nights-and-weekends hours |

### builder_hours_per_week_assumed

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 10 | hours per week | estimate | Hours unstated; 'nights and weekends' read conservatively as 10 h/week = 1.25 working days. |

### builder_llm_budget_monthly

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | 15 | usd per month for one household | sourced | https://coreywbrown.com/projects/next-on-wembley/ |

### builder_llm_spend_observed

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | 0.07 | usd per budget period for one household (period unstated) | sourced | https://coreywbrown.com/projects/next-on-wembley/ |

### builder_rate_daily

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 523 | usd per person-day | derived | bls_software_developer_median_wage (135980) / 260 working days |

### builder_rate_hourly

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 65.375 | usd per hour | derived | bls_software_developer_median_wage (135980) / 2080 hours |

### builder_watch_through_top20

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | 0.5 | share of top-20 recommendations watched (one household; target or actual unclear) | sourced | https://coreywbrown.com/projects/next-on-wembley/ |

### cac

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/go-to-market.md` | gtm-researcher | 240 | usd per activated pair (community-led organic channel, primary/first-cohort channel) | estimate | 3 hours of founder time per activated pair (finding a fit, engaging authentically, onboarding one partner, following up until the second par… |

### cac_influencer

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/go-to-market.md` | gtm-researcher | None | usd per activated pair | unknown | book 1-2 TikTok micro-influencers ($200-$800/video, sourced range) and measure click-to-signup and second-partner-activation rates directly |

### cac_paid_search

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/go-to-market.md` | gtm-researcher | None | usd per paying customer | unknown | an accessible, dated keyword-volume/CPC source (e.g. a Google Ads account or a licensed keyword-research tool) for terms like "what to watch… |

### cac_paid_social

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/go-to-market.md` | gtm-researcher | None | usd per activated pair | unknown | a 2-week landing page plus $300 of paid social, measuring cost per activated pair (the test already named in the opportunity model's risk re… |

### ccpa_consumer_count_threshold

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/regulatory.md` | regulatory-scout | 100000 | california residents or households whose personal information is bought, sold, or shared per year (one of three independent CCPA-applicability triggers) | sourced | https://www.oag.ca.gov/privacy/ccpa |

### ccpa_revenue_threshold_usd

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/regulatory.md` | regulatory-scout | 25000000 | usd annual gross revenue (one of three independent CCPA-applicability triggers) | sourced | https://www.oag.ca.gov/privacy/ccpa |

### comparable_app_installs

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | 170000 | cumulative app installs (Matched, all platforms, estimate from a secondary aggregator) | sourced | https://www.appbrain.com/app/matched-movie-app-for-couples/io.taste.matched |

### comparable_app_rating

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | 4.7 | stars out of 5 (281 ratings) | sourced | https://apps.apple.com/us/app/matched-movie-app-for-couples/id1623287922 |

### competitor_price_high

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | 19.99 | usd per year (Matched Premium annual) | sourced | https://apps.apple.com/us/app/matched-movie-app-for-couples/id1623287922 |
| `research/market-size.md` | market-sizer | 60 | usd per year | sourced | https://www.neowin.net/news/trakt-vip-receives-up-to-300-price-hike-going-back-on-promise-to-honor-legacy-subs/ |
| `research/competition.md` | competitive-strategist | 30.37 | usd per month (derived from a weekly price) | derived | shared_watchlist_weekly_price (6.99 usd/week) x average_weeks_per_month (4.345) |
| `research/go-to-market.md` | gtm-researcher | 60 | usd per year, per individual | sourced | https://alternativeto.net/news/2025/5/trakt-announces-all-vip-renewals-will-switch-to-a-new-standard-rate-doubling-prices/ |
| `research/build-and-run.md` | build-cost-analyst | 5 | usd per user per month | derived | trakt_vip_annual_price (60, sourced https://alternativeto.net/news/2025/5/trakt-announces-all-vip-renewals-will-switch-to-a-new-standard-rat… |

### competitor_price_low

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | 2.99 | usd per month (Matched Premium) | sourced | https://apps.apple.com/us/app/matched-movie-app-for-couples/id1623287922 |
| `research/market-size.md` | market-sizer | 49.99 | usd per year | sourced | https://www.sofahq.com/pricing |
| `research/competition.md` | competitive-strategist | 0 | usd per month | sourced | https://apps.apple.com/us/app/wewatch-together/id6755074651 |
| `research/go-to-market.md` | gtm-researcher | 49 | usd per year, per individual | sourced | https://letterboxd.com/about/pro/ |
| `research/build-and-run.md` | build-cost-analyst | 3 | usd per user per month | sourced | https://www.achriom.com/blog/simkl-vs-trakt/ |

### cost_to_serve_cash_per_unit

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 2.54 | usd per pair per month | derived | cost_to_serve_per_unit (5.268) - human_cost_per_unit (2.724) |

### cost_to_serve_per_unit

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | None | usd per pair per month | unknown | build-cost-analyst model of LLM tokens per recommendation round x rounds per month, plus TMDb commercial licence fee spread per pair, hostin… |
| `research/build-and-run.md` | build-cost-analyst | 5.27 | usd per pair per month | derived | llm_cost_per_pair_month (1.6592) + infra_cost_per_pair_month (0.0348) + payment_cost_per_unit (0.75) + refunds_per_unit (0.10) + human_cost_… |

### couple_new_series_decision_frequency

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | None | new shared series started per couple per month | unknown | the 10-15-couple concierge test described in 'What would validate this', logging actual decision events over 2-4 weeks |

### fixed_costs_monthly

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 451.85 | usd per month | derived | fixed_costs_monthly_cash (190.35) + founder_maintenance_hours_monthly (4) x builder_rate_hourly (65.375) |

### fixed_costs_monthly_cash

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 190.35 | usd per month | derived | tmdb_commercial_licence_cost (149) + vercel_pro_price (20) + neon_base_compute_monthly (19.35) + domain (2, estimate) |

### founder_maintenance_hours_monthly

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 4 | hours per month | estimate | Dependency and model upgrades, TMDb cache refresh checks, monitoring and billing admin for a live multi-tenant app; 1 hour a week. |

### haiku_input_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 1 | usd per million input tokens | sourced | https://claude.com/pricing |

### haiku_output_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 5 | usd per million output tokens | sourced | https://claude.com/pricing |

### households_using_product

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | 1 | households | sourced | inputs/next-on-wembley/idea.md |

### human_cost_per_unit

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 2.724 | usd per pair per month | derived | human_minutes_per_unit (2.5) / 60 x builder_rate_hourly (65.375) |

### human_minutes_onboarding_per_new_pair

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 5 | minutes per new pair (one-off) | estimate | 25% of new pairs assumed to need help with invite or Netflix CSV matching, 20 min each. |

### human_minutes_per_unit

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 2.5 | minutes per pair per month | estimate | No comparable discloses support load. Assumed 15% of pairs contact support monthly x 12 min = 1.8 min, plus 0.2 min billing admin, plus 0.5 … |

### individual_decide_what_to_watch_hours_per_year

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | 110 | hours per year an individual reports spending deciding what to watch (not couple-specific; mismatch noted) | sourced | https://www.usertesting.com/resources/reports/stream-fatigue-goes-global |

### infra_cost_per_pair_month

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.0348 | usd per pair per month | derived | vercel memory 0.0146 + 0.0006 + active cpu 0.0009 + invocations 0.0002 + cdn 0.0020 + neon storage 0.0035 + neon compute 0.0106 + email 0.00… |

### justwatch_commercial_licence_cost

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/regulatory.md` | regulatory-scout | None | usd per year | unknown | direct written query to JustWatch (their own terms state personal/non-commercial use only and don't publish a commercial-licensing path) |

### justwatch_monthly_users

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 10000000 | monthly users | sourced | https://www.streamtvinsider.com/online-video/start-up-justwatch-which-bills-itself-as-streaming-search-engine-now-boasts-10m-users |

### justwatch_pro_monthly_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 2.49 | usd per month | sourced | https://www.justwatch.com |

### letterboxd_patron_annual_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 49 | usd per year | sourced | https://letterboxd.com/pro/ |

### llm_cost_per_pair_month

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 1.6592 | usd per pair per month | derived | llm_rounds_per_pair_month (16) x llm_cost_per_round_sonnet (0.1037) |

### llm_cost_per_round_haiku

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.0519 | usd per recommendation round | derived | 38350 x haiku_input_price (1) / 1e6 + 2700 x haiku_output_price (5) / 1e6 |

### llm_cost_per_round_sonnet

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.1037 | usd per recommendation round | derived | llm_input_tokens_per_round (38350) x sonnet_input_price (2) / 1e6 + llm_output_tokens_per_round (2700) x sonnet_output_price (10) / 1e6 |

### llm_input_tokens_per_round

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 38350 | tokens per round | estimate | Three calls per round (co-watch 15,950; two personal at 11,200): 1,500 system prompt, 200 titles per partner x 20 tokens, 100 votes x 15, 80… |

### llm_output_tokens_per_round

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 2700 | tokens per round | estimate | Three lists x (10 picks x 70 tokens + 200 JSON overhead) = 2,700; no extended thinking assumed. |

### llm_rounds_per_pair_month

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 16 | recommendation rounds per pair per month | estimate | 4 decision sessions a month ('a few times a month') x 4 regenerations per session after votes or mood changes; high side for cost. |

### manual_upkeep_completion_rate

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | None | share of non-builder couples who complete both partner profiles and are still updating them at day 30 | unknown | the same concierge test, measured at day 14 and day 30 |

### market_value_obtainable

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/market-size.md` | market-sizer | 202709 | usd per year | derived | obtainable_customers (4,055) × competitor_price_low (49.99 usd/year) |

### market_value_serviceable

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/market-size.md` | market-sizer | 1899732378 | usd per year | derived | serviceable_customers (38,002,248) × competitor_price_low (49.99 usd/year) |

### market_value_total

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/market-size.md` | market-sizer | 2127123240 | usd per year | derived | total_customers (42,550,975) × competitor_price_low (49.99 usd/year) |

### matched_downloads

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 100000 | downloads (lower bound, "100K+") | sourced | https://play.google.com/store/apps/details?id=io.taste.matched |

### matched_premium_annual_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 19.99 | usd per year | sourced | https://apps.apple.com/us/app/matched-movie-app-for-couples/id1623287922 |

### matched_premium_monthly_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 2.99 | usd per month | sourced | https://apps.apple.com/us/app/matched-movie-app-for-couples/id1623287922 |

### neon_base_compute_monthly

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 19.35 | usd per month | derived | always-on compute size (0.25 cu, estimate) x 730 hours x neon_compute_price (0.106) |

### neon_compute_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.106 | usd per cu-hour | sourced | https://neon.com/pricing |

### obtainable_customers

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/market-size.md` | market-sizer | 4055 | households, within 3 years of launch | estimate | 1% of Trakt's 811,000 15-year monthly-active-user comparable (sourced, PCWorld Apr 2025), taken as a conservative ceiling for a higher-frict… |

### paddle_fee

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.05 | share of transaction plus 0.50 usd fixed | sourced | https://www.paddle.com/pricing |

### payment_cost_per_unit

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.75 | usd per pair per month at a 5.00 monthly reference price | derived | paddle_fee (0.05) x reference_price (5.00, = competitor_price_high) + 0.50 |

### people_per_signup

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | 2 | people per household account | sourced | inputs/next-on-wembley/idea.md |

### price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | None | usd per pair per month | unknown | decision in the business case, informed by the competitive-strategist's observed price band |
| `research/market-size.md` | market-sizer | None | usd per pair per month | unknown | decision in the business case, informed by this file's competitor_price_low/_high band |

### price_floor_conservative

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 5.29 | usd per pair per month | derived | (llm 1.6592 + infra 0.0348 + human 2.724 + paddle fixed fee 0.50) / (1 - paddle rate 0.05 - refund rate 0.02) |

### reddit_subreddits_banning_selfpromo_share

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/go-to-market.md` | gtm-researcher | 0.39 | share of surveyed subreddits that ban self-promotion outright | sourced | https://oneup.today/blogs/reddit-selfpromo-rules-study-2026 |

### refunds_per_unit

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.1 | usd per pair per month | estimate | No source; assumed 2% of a 5.00 charge lost to refunds and chargebacks for a new consumer subscription. |

### serviceable_customers

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/market-size.md` | market-sizer | 38002248 | households (US + Canada, broadband-connected, English-primary where applicable) | derived | total_customers_US (38,005,388) × us_broadband_household_share (0.912, sourced) + total_customers_CA (4,545,587) × us_broadband_household_sh… |

### setup_minutes_per_pair

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 40 | minutes of user time per pair (one-off) | estimate | Per partner: 60-title grid 5 min, adding in-progress, dropped and wanted titles 5 min, Netflix CSV download, upload and fixes 10 min; x2. |

### shared_watchlist_weekly_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 6.99 | usd per week | sourced | https://apps.apple.com/us/app/shared-watchlist-couple-match/id6755390014 |

### simkl_vip_monthly_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 2.99 | usd per month | sourced | https://simkl.com/vip/ |

### sonnet_input_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 2 | usd per million input tokens | sourced | https://claude.com/pricing |

### sonnet_output_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 10 | usd per million output tokens | sourced | https://claude.com/pricing |

### stripe_card_fee_canada

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.029 | share of transaction plus 0.30 cad | sourced | https://stripe.com/pricing |

### tmdb_cache_limit_months

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | 6 | months maximum caching of tmdb data | sourced | https://www.themoviedb.org/api-terms-of-use |
| `research/regulatory.md` | regulatory-scout | 6 | months maximum caching of tmdb data | sourced | https://www.themoviedb.org/api-terms-of-use |

### tmdb_commercial_licence_cost

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/opportunity-model.md` | opportunity-framer | None | usd per year | unknown | written commercial quote requested from TMDb for a paid CA/US web app |
| `research/build-and-run.md` | build-cost-analyst | 149 | usd per month | sourced | https://www.themoviedb.org/talk/69cbf4f91b914f0e9542a772 |
| `research/regulatory.md` | regulatory-scout | None | usd per year | unknown | written commercial quote requested from TMDb, specifically asking whether AI/LLM-based recommendation use is licensable at all (TMDb's Restr… |

### total_customers

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/market-size.md` | market-sizer | 42550975 | households (US + Canada, couples with 2+ paid streaming subscriptions) | derived | us_households (134,790,000, sourced) × us_coupled_household_share (0.532, sourced) × us_households_2plus_subs_share (0.53, sourced) + ca_cou… |

### tracker_vip_price_annual

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | 60 | usd per year (Trakt VIP, after a cited price increase; conservative/higher end of the two figures a reviewer gave) | sourced | https://www.trustpilot.com/review/trakt.tv |

### trakt_vip_annual_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 60 | usd per year | sourced | https://alternativeto.net/news/2025/2/trakt-tv-has-set-stricter-limits-for-free-users-and-raised-vip-subscription-prices-by-100-/ |

### tv_time_lifetime_price_historical

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 74.99 | usd one-time (historical, product now shut down) | sourced | https://apps.apple.com/us/app/television-time/id969714962 |

### tv_time_registered_users

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/problem.md` | problem-validator | 25000000 | registered members (TV Time, free, manual-logging tracker, now shut down) | sourced | https://www.techtimes.com/articles/319583/20260703/tv-time-closes-july-15-26-million-users-face-permanent-watch-history-deletion.htm |

### tv_time_registered_users_peak

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/competition.md` | competitive-strategist | 20000000 | registered users | sourced | https://whipmedia.com/news/tv-time-hits-new-milestone-with-20-million-registered-users/ |

### tv_time_users_at_shutdown

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/go-to-market.md` | gtm-researcher | 26000000 | users | sourced | https://www.techtimes.com/articles/319583/20260703/tv-time-closes-july-15-26-million-users-face-permanent-watch-history-deletion.htm |

### usd_cad_rate

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 1.4136 | cad per usd | sourced | https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/ |

### vercel_memory_price_yul1

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 0.0122 | usd per gb-hour | sourced | https://vercel.com/docs/functions/usage-and-pricing |

### vercel_pro_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 20 | usd per month | sourced | https://vercel.com/pricing |

### watchmode_startup_price

| File | Agent | Value | Unit | Kind | Source / formula / reasoning |
|---|---|---|---|---|---|
| `research/build-and-run.md` | build-cost-analyst | 349 | usd per month | sourced | https://api.watchmode.com/ |

## RISKS blocks

### opportunity-framer: `research/opportunity-model.md`

```yaml
RISKS:
  - risk: The product only works if both partners set up and then keep maintaining their watch history by hand, since no streamer API exists and Netflix's export is per profile and manual. No household other than the builder's has shown it will do this, and if the second partner lapses the co-watch list loses the input it depends on.
    severity: high
    confidence: medium
    investigate: a named test, concierge-onboard 10 non-builder couples (S1 and S2) and measure how many complete both profiles and are still updating at day 30
  - risk: Every signup needs a second person to accept an invite and do setup. That compounds drop-off at each funnel step and roughly doubles the activation work per paying unit, for a builder with no distribution.
    severity: high
    confidence: medium
    investigate: a named test, a 2-week landing page with a pair-invite flow and $300 of paid social, measuring second-partner activation rate and cost per activated pair
  - risk: Use happens only between shows, a few sessions a month. That fits badly with a monthly subscription, and churn between uses could exceed any CAC payback window.
    severity: high
    confidence: medium
    investigate: a data pull, the unit-economics-auditor computes breakeven churn from the Stage 2 cost-to-serve and price band, and the problem-validator measures how often couples actually face the decision
  - risk: The two-person overlap recommendation may be a feature, not a product. Trackers, availability guides or streamers with household profiles, who already hold the viewing history, could offer it or add it cheaply.
    severity: high
    confidence: low
    investigate: a data pull, the competitive-strategist audits the leading TV trackers, availability guides and streamer household features for any shared or couple recommendation and its price
  - risk: Charging for the app requires a written TMDb commercial agreement, and TMDb's provider data must be attributed to JustWatch. If the licence is costly, slow or refused to a solo builder, the core data layer has to be replaced before launch.
    severity: high
    confidence: high
    investigate: the decision-maker requests a commercial quote and terms from TMDb, and the regulatory-scout checks JustWatch's and Anthropic's commercial terms
  - risk: The builder has no audience, no capital and no path to couples. The only reach assets named on his site belong to a former employer, so acquisition would be cold and organic, or paid from personal funds.
    severity: high
    confidence: high
    investigate: a named test, the gtm-researcher prices 2 organic channels (community posts and short-form video) and 1 paid channel for cost per activated pair
  - risk: The only performance and cost figures ($0.07 of a $15 budget, ~50% watch-through, ~60% co-watch agreement) come from the builder's own page for one household, and may be targets rather than measurements. They cannot be treated as evidence of recommendation quality or cost to serve at scale.
    severity: medium
    confidence: high
    investigate: the decision-maker confirms whether the figures are measured, and the build-cost-analyst models cost per pair from token counts rather than this single figure
  - risk: Nights-and-weekends hours are unstated and may shrink. Productizing (multi-tenant auth, pair invites, partner-data separation, billing, import, licence compliance) could take a calendar time that stalls momentum.
    severity: medium
    confidence: medium
    investigate: the decision-maker states weekly hours so the build-cost-analyst can give Solo AI-typical calendar weeks
  - risk: Storing each partner's ratings, drops and history in a shared account creates a partner-privacy and account-separation problem, for example when one partner sees the other's private ratings or the relationship ends. It also creates a trust risk when LLM "whys" invent plot or availability details.
    severity: medium
    confidence: low
    investigate: a named test, the ethics-trust-safety agent reviews the visibility defaults and audits 50 generated "whys" against TMDb data for factual errors
```

### problem-validator: `research/problem.md`

```yaml
RISKS:
  - risk: The closest scaled analogue for this idea's core mechanic — a free, manual-logging TV tracker — shut down in July 2026 with 25-26 million registered users specifically because, per the company, "there was not enough demand for a paid app." This is direct behavioral evidence against monetizing a manual-logging-heavy product, at a scale this idea is unlikely to ever reach.
    severity: high
    confidence: high
    investigate: a named test, the 10-15-couple concierge test (this file, "What would validate this") to see whether a couple-specific angle changes upkeep tolerance and paying intent versus TV Time's single-player logging model
  - risk: Every existing competitor solving the "two-person overlap" problem (Matched, WeWatch Together, Swatched, Shared Watchlist, Watch and Chill) uses lightweight swiping to collect preferences, not full watch-history entry. The market's revealed choice of input method suggests people will not tolerate the heavier logging this idea requires, even though this idea's own answer to Q2 depends on them doing so.
    severity: high
    confidence: medium
    investigate: a named test, interview 5 reviewers of Matched or WeWatch Together on whether they would want, and pay more for, a history-based version instead of swiping
  - risk: No source measures how often a couple actually starts a new shared series. The only frequency data found (110 hours/year deciding what to watch) is an individual, all-viewing proxy, not a couple-specific "new series" cadence, so Q3 (can a few-times-a-month product justify a price) remains unanswered by this research.
    severity: high
    confidence: high
    investigate: a data pull or named test, the 10-15-couple concierge test logging actual decision events over 2-4 weeks
  - risk: The only clean, couple-specific, comparable willingness-to-pay figure found ($2.99/mo or $19.99/yr for Matched Premium) belongs to a materially lighter product than the one proposed. Using it as a price anchor for a heavier, history-based, LLM-generated product would overstate what is actually validated.
    severity: medium
    confidence: medium
    investigate: the decision-maker treats Matched's price as a floor, not a target, pending the venture-strategist's own price decision
  - risk: The Netflix "streaming infidelity" survey (48% watch ahead alone, 18% report arguments) is a vendor-commissioned survey from Netflix's own PR, not an independent study, and measures a related but distinct behavior (watching ahead solo) rather than disagreement over what to start next. It should not be read as direct evidence of the core problem's severity.
    severity: low
    confidence: high
    investigate: a data pull, if this figure is used downstream, look for an independent (non-vendor) replication before it anchors any severity claim
```

### market-sizer: `research/market-size.md`

```yaml
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
```

### competitive-strategist: `research/competition.md`

```yaml
RISKS:
  - risk: Free or near-zero-setup substitutes (MatchWatch, Matched's free tier, Netflix's Play Something and household profiles, general-purpose AI assistants) already address the core couple "what to watch" decision for most of S1 without requiring manual watch-history entry, which weakens the case that this product's heavier setup buys a result worth paying for.
    severity: high
    confidence: medium
    investigate: a named test, run 10 non-builder S1/S2 couples through both a swipe app (e.g. Matched or MatchWatch) and this product's flow for two weeks, and compare completion rate and stated satisfaction
  - risk: TV Time, the closest scale analog for a manual, per-person logging product used between viewing sessions, shut down after reaching 20M+ registered users, with its operator stating plainly there was not enough demand for a paid version. This is direct negative evidence against the assumption that this usage pattern can sustain a price (A3, A8).
    severity: high
    confidence: high
    investigate: the decision-maker weighs whether this product's LLM-personalized "why" is enough to overturn this precedent, informed by a small paid smoke test before further build investment
  - risk: Trakt's own users have an open, unresolved, multi-year feature request for a watched/ratings overlap comparison between two users, and Trakt already holds both users' history plus a following graph. If Trakt or Simkl ship a lightweight "compare with a partner" feature, it undercuts this product's wedge quickly, since the harder half of the data problem is already solved on their side.
    severity: high
    confidence: medium
    investigate: a data pull, monitor Trakt's and Simkl's public changelogs and forums for movement on this feature request before committing further build time
  - risk: The "for couples" swipe-match category (Matched, MatchWatch, Shared Watchlist, WeWatch Together, MatchaFilm) already has at least five live entrants competing on the exact low-setup, purpose-built-for-two positioning that would otherwise be this product's white space; most show weak or unverifiable traction (two of the five have 1–2 App Store ratings despite being live), suggesting the category itself may not be commercially proven rather than that there is room for a sixth entrant.
    severity: medium
    confidence: medium
    investigate: a named test, the gtm-researcher checks whether any of these five apps has disclosed revenue or retention figures beyond app-store ratings
  - risk: Several competitor prices in this file (Trakt, Simkl, Letterboxd, JustWatch) could not be confirmed by directly rendering the primary pricing page in this run, because those pages returned HTTP 403 to the fetch tool; the figures instead come from live web searches during this run that quote or cite the primary page. They should be treated as lower-confidence than the App Store prices, which were fetched directly.
    severity: low
    confidence: high
    investigate: a data pull, re-fetch trakt.tv/vip, simkl.com/vip and letterboxd.com/pro with a tool or browser that isn't blocked before these exact figures are used to set this product's price in the business case
```

### gtm-researcher: `research/go-to-market.md`

```yaml
RISKS:
  - risk: The two well-documented, category-relevant CAC figures found (mobile app-install cost, and B2B SaaS sales-motion thresholds) both fail to match this product on a defining dimension — the mobile figure assumes a native app this product doesn't have, and the SaaS thresholds assume B2B pricing three orders of magnitude above this product's likely price. No channel has a CAC figure that actually matches this product's shape (web-only, consumer, pair-priced), so every paid-channel CAC in this file is `unknown`, not merely uncertain.
    severity: high
    confidence: high
    investigate: "a named test, the $300 paid-social test and a separate small paid-search test, each measuring cost per activated pair directly rather than borrowing a benchmark from an adjacent category"
  - risk: The closest well-distributed incumbent in this exact adjacent category (TV Time, 26M users) shut down in 2026 citing insufficient demand for a paid version of a free tracking product. If this product's audience behaves similarly, no CAC calculation matters because willingness to pay, not acquisition cost, is the binding constraint.
    severity: high
    confidence: medium
    investigate: "the decision-maker treats TV Time's stated shutdown reason as a direct signal for A3 (willingness to pay for a low-frequency tracker) and weighs it alongside the problem-validator's findings before committing to a paid model"
  - risk: The product's data provider, JustWatch, is simultaneously the closest thing to an incumbent "what to watch" audience at scale (50M+ MAU) and a company now launching its own competing consumer streaming product. It is not available as a distribution partner, and its own commercial priorities could shift the terms this product depends on.
    severity: medium
    confidence: medium
    investigate: "a data pull, the regulatory-scout monitors JustWatch's and TMDb's terms pages for changes alongside the commercial-licence quote already requested for A6"
  - risk: Every plausible near-zero-cash channel found (community posts, personal outreach) is bounded by the builder's own hours, which are already flagged elsewhere as unstated — meaning the one channel this file can actually support doesn't scale independent of the builder's calendar.
    severity: high
    confidence: medium
    investigate: "the decision-maker states available weekly hours (already requested by the opportunity model), so this file's launch-sequence pacing can be checked against real capacity"
  - risk: This product's chosen constraint (web-only, no native apps in v1) removes the one channel — app-store search and browse — that its three closest comparables (Trakt, Serializd, and the now-defunct TV Time) actually use for organic discovery, with no offsetting web-only channel of comparable, sourced reach identified.
    severity: medium
    confidence: high
    investigate: "the decision-maker decides whether a native app is worth revisiting post-v1 specifically for the ASO channel, once (or if) the web version proves it can convert pairs at all"
```

### build-cost-analyst: `research/build-and-run.md`

```yaml
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
```

### regulatory-scout: `research/regulatory.md`

```yaml
RISKS:
  - risk: TMDb's API Terms of Use restrict use "in connection with, including for training, a machine learning (ML) or artificial intelligence (AI) based Application" and name LLMs and chatbots as commercial uses requiring a separate written agreement. This product's core feature is an LLM generating picks from TMDb data, so it's unknown whether TMDb will license this use at all, at any price, to a solo builder.
    severity: high
    confidence: high
    investigate: a paid expert or the decision-maker sends a direct written query to TMDb asking specifically whether AI/LLM-based recommendation use is licensable and at what cost, before further build investment
  - risk: JustWatch's own terms of use separately prohibit commercial use and scraping of "the Service Content," with no public commercial-licensing path stated, and it's unconfirmed whether a TMDb commercial agreement covers the JustWatch-sourced provider data TMDb redistributes, or whether a second, separate JustWatch agreement is required for the streaming-availability feature.
    severity: high
    confidence: medium
    investigate: a paid expert or the decision-maker sends a direct written query to JustWatch (contact found in secondary sources, not on JustWatch's own terms page) confirming the licensing path for their data as redistributed via TMDb
  - risk: No safe terms-of-use workaround exists to auto-capture watch history. Netflix's Terms of Use ban automated/bot access, data mining/extraction, and use of the service in connection with training a machine learning tool; a browser extension or scraper built to read a user's own logged-in account would breach this, risking that user's Netflix account and possible unsettled CFAA exposure under Van Buren v. United States, 593 U.S. 374 (2021). Other major streamers weren't individually checked and shouldn't be assumed safer.
    severity: high
    confidence: medium
    investigate: the decision-maker accepts manual entry and tracker-app import as the only viable onboarding paths, and the build-cost-analyst and problem-validator design around that constraint rather than a capture workaround
  - risk: It's unclear whether the Video Privacy Protection Act (18 U.S.C. § 2710), which restricts disclosure of records identifying a person's video viewing, reaches a companion app that stores user-entered watch history and forwards it to a third-party LLM processor (Anthropic), rather than delivering video itself. Courts have read the statute broadly against other video-adjacent services.
    severity: medium
    confidence: low
    investigate: a paid expert, a 1-hour consult with a US privacy attorney, on whether VPPA plausibly applies and what consent language would satisfy it if so
  - risk: PIPEDA and Quebec's Law 25 apply to this business from its first Canadian user, with no revenue or size threshold, and require documented consent for collecting two partners' combined viewing data and disclosing it to service providers (TMDb, Anthropic). No consent flow or privacy policy exists yet.
    severity: medium
    confidence: high
    investigate: a paid expert, a 1-hour consult with a Canadian privacy lawyer, to draft the minimum consent language and privacy-policy disclosures needed before Canadian launch
  - risk: Each recommendation call likely sends both partners' watch history and ratings together to Anthropic's API in a single prompt, which is a disclosure to a third-party processor and a same-account cross-partner visibility question at once; neither the consent-and-disclosure design (regulatory) nor the visibility-default design (trust, routed to ethics-trust-safety) exists yet.
    severity: medium
    confidence: medium
    investigate: a paid expert, the same privacy-lawyer consult above, folds in a review of what the LLM prompt actually contains before any real household's data is sent
  - risk: Anthropic's Commercial Terms of Service were located by search, not fetched and read in full during this pass; the "no product-category restriction" finding is asserted at medium confidence, not independently verified against Anthropic's Usage Policy.
    severity: low
    confidence: medium
    investigate: a data pull, fetch and read Anthropic's Usage Policy and Commercial Terms of Service directly before relying on this finding
  - risk: Stripe's and PayPal's restricted-business lists don't name this business category as prohibited, but neither addresses the real continuity risk here, which is TMDb or JustWatch revoking API access for a terms violation. A processor-clean bill of health doesn't mean the product can keep running.
    severity: low
    confidence: high
    investigate: none needed beyond what's already stated above; noted so the decision-maker doesn't mistake payment-processor clearance for data-licensing clearance
```
