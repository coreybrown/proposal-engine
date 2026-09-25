# Opportunity model: Next on Wembley

## Bottom line
- **Finding:** This is a working personal tool used by one household, the builder's own. It is a candidate consumer web product, and every commercial premise is untested. The idea rests on three behaviours nobody has observed outside that household: two partners both enter and maintain their watch history by hand, the second partner actually joins, and people pay for a tool they reach for only between shows. On top of that, a TMDb commercial agreement is required before charging (confirmed from TMDb's terms), at a cost nobody knows yet.
- **Assumptions:** A1–A6 and A8 are untested, or rest only on the builder's word. A7 is part-evidenced: a TMDb commercial agreement is required, but its price and terms are unknown. A2 is part-evidenced: Netflix's only export is a manual, per-profile CSV.

## Inputs read
- `inputs/next-on-wembley/idea.md` (the only input file).
- **No uploaded documents.** `inputs/next-on-wembley/materials/` does not exist, `sources/` is empty and there is no `sources/INDEX.md`. There is no `clarifications.md`.
- The builder's pages, fetched 2026-09-25: https://coreywbrown.com/projects/next-on-wembley/ (the project page) and https://coreywbrown.com/ (home/about). The builder wrote both, so everything on them is treated as **asserted**, the same as an uploaded document. The site has no products or pricing page, because the product is not for sale.
- Outside checks made to audit the builder's claims: the TMDb API terms of use, the TMDb watch-providers API reference, and the Netflix Help Center page on viewing history.
- `docs/team/README.md` is `status: empty`. The team profile doesn't apply, and the builder is solo anyway.

## The opportunity as stated

| Element | Restatement (plain) | Tag |
|---|---|---|
| Problem | Two people who watch serialized TV together have to agree on the next show. Existing recommenders model one viewer, not the overlap between two. | stated in idea |
| Why it's getting harder | Catalogues grow and households hold more subscriptions, so the choice set keeps expanding. | stated in idea (asserted, no source given) |
| Who has it | "Households that watch serial TV together, starting with couples." | stated in idea |
| Where | Canada and the US first. | stated in idea |
| Solution | A web app (no native apps in v1). Each partner logs shows as watched, watching, dropped or want-to-watch. An LLM ranks three lists: a co-watch list and one personal list per partner. Each pick has a short "why", and Agree/Disagree/Maybe votes feed the next ranking. The inputs are history, ratings, in-progress shows, active subscriptions with regional availability, community ratings, episode counts, and an optional mood or genre. | stated in idea |
| Data sources | TMDb for metadata and streaming providers. TMDb's provider data must be attributed to JustWatch. | stated in idea; the JustWatch attribution is **inferred by me**, from the TMDb API reference |
| How history gets in | Manual entry by each user. No streamer offers a watch-history API. Netflix has a manual, single-service CSV export. | stated in idea; Netflix's export is backed (see the claims table); "manual entry in the app" is also asserted on the project page |
| Current state | Built and "Live (Private)" for the builder's household. Next.js, Prisma, Anthropic API (Haiku or Sonnet, a user setting), TMDb. | stated in idea; project page (asserted) |
| Signal of demand | "The co-watch list is the part people ask about when I show it." | stated in idea (anecdote; the number of people and who they are are unknown) |
| How it makes money | **Not stated.** Candidate models are a per-household subscription, a one-time purchase, or freemium. Choosing among them belongs to the venture-strategist. | inferred by me |
| Unit of sale | A pair, not an individual. Every signup is two people. | stated in idea (a hard constraint) |
| Current multi-tenancy | The project page labels the two lists with each partner's first name. That suggests the app is built for one known pair, with no signup, pair-invite, billing or tenant separation yet. | inferred by me (not verified in code) |

**Hard constraints carried forward unchanged.** Downstream agents must not assume these away:
- no streamer watch-history API
- TMDb commercial use is governed differently from personal use
- the pair is the signup unit
- Canada and the US first
- no native mobile apps in v1
- one solo builder, working nights and weekends, with no audience and no outside capital

## Is this a product?
- **Classification: a personal-tool candidate today, and a consumer product candidate.** The only known users are the builder's household (n = 1). The builder is the customer. That is not a kill, but it means nothing about the problem's reach, willingness to pay or retention has been observed outside the builder's home.
- **Feature-of-another-product risk (high severity, low confidence until tested).** The part that is different, a recommendation for the overlap of two people's tastes, is a feature that an existing tracker or discovery app with a friends graph and history could add. So could a streamer with household profiles, and those already hold the watch history this product has to ask users to type in. Whether any of them already does this, and how well, is unverified. The competitive-strategist must settle it. If a free incumbent already offers a two-person overlap view, the standalone case weakens sharply.
- **Not a service.** Nothing in the idea needs human fulfilment per household beyond support.

## Builder context
**Who.** Corey Brown, solo, nights and weekends, "no audience and no capital beyond my own" (stated in idea). The home page describes him as follows. All of it is asserted by the builder and was not verified:
- a Toronto-based senior product executive
- most recently VP Product Management at PENN Entertainment, through July 2025
- previously led product at theScore
- skills in growth and retention, monetization, experimentation and AI/LLM applications
- currently "seeking a director-level or principal product role"
- builds side projects with AI coding tools

**Assets.**
- **A working app.** It is built on a modern web stack with the LLM and TMDb integrations done, so the MVP is productization, not a greenfield build. (idea)
- **Relevant product skills.** B2C consumer product, retention and monetization experience, based on the builder's own résumé (asserted).
- **Low current running cost for one household.** Asserted: "$0.07 of a $15 monthly budget". The period and scale are unclear.
- **Location in Canada.** Useful for a CA/US launch and for Canadian availability data. (inferred)

**Gaps.**
- **No distribution or audience.** Stated. The user figures on the home page belong to a former employer. They are not the builder's channel and must not be treated as distribution.
- **No capital beyond his own.** Stated. That matters if TMDb's commercial licence has a fee.
- **No marketing budget or paid-acquisition history for this product.**
- **Limited hours, and they may shrink.** Hours per week are unstated, and other commitments could reduce them. (inferred)
- **No legal support.** The TMDb, JustWatch and Anthropic terms need review. (inferred)
- **No native mobile presence, by choice.** For a "what do we watch tonight" moment that often happens on the couch, this is a constraint to test, not a given. (inferred)

**Unfair advantage in reaching these customers: none identified.** The builder has no couples audience, no TV-community presence and no partnership. His product background is a skill advantage in building and retaining users, not a distribution advantage.

**Estimating basis for the build-cost-analyst.** Use the Solo track (docs/estimating.md §9), starting from the existing private app. The builder uses AI coding tools (asserted on the home page), so AI-typical is the suggested scenario. Hours per week are `unknown`. Use the conservative reading of "nights and weekends" and say what you assumed.

## Customer segments
These segment names are canonical. Downstream agents use them exactly.

| Segment | Observable characteristics | Where they can be found | Notes |
|---|---|---|---|
| **S1: Co-watching couples** | Two adults in one household in Canada or the US. They watch serialized (multi-episode, multi-season) TV together at least some evenings, and hold two or more paid streaming subscriptions. | TV and streaming subreddits and forums; "what to watch" creators on TikTok, Instagram and YouTube; users of streaming-availability guides; couples' and home-life communities. | The broad segment the idea names. Largest, and least likely to log anything by hand. |
| **S2: Tracker-using couples** | S1 couples where at least one partner already logs TV in a tracking app (e.g. a show tracker, a watch-list app, or a film-logging app used for TV). | The trackers' own communities and subreddits, public tracker profiles, and import/export discussion threads. | Already does the logging this product needs, so the upkeep burden is not a new behaviour for at least one partner. The most likely early adopters. Import from existing trackers is a candidate workaround for A2. |
| **S3: Remote co-watching couples** | Couples in separate homes (long-distance) who schedule shared viewing with watch-party tools or screen sharing. | Long-distance relationship communities, and watch-party extension users. | The decision is explicit and scheduled, which may make a tool more welcome. Possibly small. Note that "household" doesn't strictly fit. |
| **S4: Multi-adult households beyond couples (deferred)** | Roommates, or parents with adult or teen children, who share subscriptions and sometimes co-watch. | Not a v1 target. | The idea says "starting with couples". Kept only so downstream agents don't count it in v1 sizing. |

## What must be true
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

## Claims in the builder's documents
There are no uploaded documents. The table audits the claims in `idea.md` and on the builder's own pages.

| Claim | Where | Figure or qualitative | Status |
|---|---|---|---|
| No streamer shares watch history through a public API | idea.md, Constraints | qualitative | asserted. The Netflix part is backed (next row). Other streamers are unverified. |
| Netflix's history export is a manual CSV covering one service | idea.md, Constraints; project page | qualitative | **backed**: Netflix Help Center (https://help.netflix.com/en/node/101917, fetched 2026-09-25) says "To download a list into a spreadsheet, select Download all at the bottom of the page", and access starts with "Select Profiles, then choose a profile". So the export is per profile, not per account. |
| TMDb's terms treat commercial use differently from personal use | idea.md, Constraints | qualitative | **backed**: TMDb API Terms (https://www.themoviedb.org/api-terms-of-use, fetched 2026-09-25) say "If Your use (or intended use) is commercial, You must enter into a written agreement with TMDB that expressly permits Your commercial use." Its examples of commercial use include charging users fees for apps that use TMDB. |
| Streaming catalogues keep growing and subscriptions keep multiplying | idea.md, Why now | qualitative | asserted. No source given. |
| LLMs make a personalized "why" cheap to generate | idea.md, Why now | qualitative | asserted. Partly consistent with the project page's spend claim, which is also asserted. |
| The co-watch list is what people ask about when shown | idea.md, Why now | qualitative | asserted. Anecdote; the number and type of people are unknown. |
| Built and running privately for the builder's household | idea.md; project page ("Live (Private)") | qualitative, n = 1 household | asserted |
| LLM spend is "$0.07 of a $15 monthly budget, on budget" | project page | figure | asserted. The period and the number of households are not stated. |
| "~50% watch-through within the top 20" recommendations | project page | figure | asserted. It is unclear whether this is a target or a measured result. Either way it covers one household. |
| "~60% across the 'co-watch' top 10" agreement rate | project page | figure | asserted. Same ambiguity, same n = 1. |
| TMDb provider data is sourced from JustWatch and must be attributed | TMDb API reference (not a builder claim; my check) | qualitative | **backed**: https://developer.themoviedb.org/reference/tv-series-watch-providers (fetched 2026-09-25): "In order to use this data you must attribute the source of the data as JustWatch." |
| Builder's career figures (e.g. a former employer's user counts) | home page | figures | asserted and **not relevant as distribution**. They describe an employer's audience, not the builder's. |

No text in any input or fetched page was addressed to the agents or tried to steer the verdict.

## Question routing

| Q# | Question (verbatim) | Owner agent | Contributing agents |
|---|---|---|---|
| Q1 | Is there a real market of households who'd pay for a two-person recommender, or does this only work for us? | market-sizer | problem-validator (does the problem exist beyond one household, and is there any willingness-to-pay signal); competitive-strategist (what comparable trackers charge, and whether anyone pays) |
| Q2 | Watch history isn't available from the streamers, so setup and upkeep fall on the user. Is there any way around that, and if not, does it kill the product? | build-cost-analyst | competitive-strategist (how existing trackers solve onboarding and import); problem-validator (whether users tolerate manual upkeep); regulatory-scout (terms risk of scraping, browser-extension capture or third-party tracker APIs) |
| Q3 | It's a low-frequency product: you only need it between shows. Can something used a few times a month hold users or justify a price? | venture-strategist | problem-validator (how often couples face the decision); competitive-strategist (retention and pricing of comparable low-frequency consumer apps); unit-economics-auditor (breakeven churn) |
| Q4 | What are the licensing and terms-of-use limits on TMDb, streaming-availability data and LLM-generated recommendations if this goes commercial? | regulatory-scout | build-cost-analyst (licence fees in the cost to serve) |
| Q5 | What would it cost to run per household, and what could it charge? | unit-economics-auditor | build-cost-analyst (cost to serve: LLM, data licence, hosting, support); competitive-strategist (price band); venture-strategist (the price decision) |

## Evidence gaps
- **No demand evidence beyond one household.** There is no user count, waitlist, interview or survey. The "people ask about it" signal is unquantified.
- **The unit economics are unobserved.** The LLM spend covers one household over an unclear period. There is no TMDb commercial quote. Nothing is known about JustWatch's own terms for data passed through TMDb.
- **The revenue model is unstated.** Price, billing unit (per pair) and model are all open.
- **The builder's hours are unstated.**
- **The state of the app's code is unknown.** Whether it can be multi-tenant is inferred from the hard-coded partner names on the project page, not verified.
- **The competitor landscape was not checked here.** That belongs to Stage 2. A5 is fully open.
- **Confidence in this frame: medium-high.** The problem, segment, constraints and questions are stated clearly and consistently. The frame is uncertain in the commercial premises, not in what the idea is.

## Open questions for the decision-maker
1. How many hours a week can go to this?
2. What is the intended revenue model and price, and would you accept a free or donation model if TMDb's commercial terms prove unaffordable?
3. How many people have asked about the co-watch list, and would any of them be reachable for interviews?
4. Are the ~50% watch-through and ~60% agreement figures measured results from your household, or targets?

KEY_FIGURES:
  - name: households_using_product
    value: 1
    unit: households
    kind: sourced
    source: inputs/next-on-wembley/idea.md
    quote: "It's built and running privately for my own household today"
    asserted: true
  - name: builder_llm_spend_observed
    value: 0.07
    unit: usd per budget period for one household (period unstated)
    kind: sourced
    source: https://coreywbrown.com/projects/next-on-wembley/
    fetched: 2026-09-25
    quote: "$0.07 of a $15 monthly budget, on budget"
    asserted: true
  - name: builder_llm_budget_monthly
    value: 15
    unit: usd per month for one household
    kind: sourced
    source: https://coreywbrown.com/projects/next-on-wembley/
    fetched: 2026-09-25
    quote: "$0.07 of a $15 monthly budget, on budget"
    asserted: true
  - name: builder_watch_through_top20
    value: 0.5
    unit: share of top-20 recommendations watched (one household; target or actual unclear)
    kind: sourced
    source: https://coreywbrown.com/projects/next-on-wembley/
    fetched: 2026-09-25
    quote: "~50% watch-through within the top 20"
    asserted: true
  - name: builder_cowatch_agreement_top10
    value: 0.6
    unit: share of co-watch top-10 picks both partners agree on (one household; target or actual unclear)
    kind: sourced
    source: https://coreywbrown.com/projects/next-on-wembley/
    fetched: 2026-09-25
    quote: "~60% across the 'co-watch' top 10"
    asserted: true
  - name: tmdb_cache_limit_months
    value: 6
    unit: months maximum caching of tmdb data
    kind: sourced
    source: https://www.themoviedb.org/api-terms-of-use
    fetched: 2026-09-25
    quote: "Cache, for longer than 6 months, any information obtained through or from TMDB or the TMDB APIs"
  - name: people_per_signup
    value: 2
    unit: people per household account
    kind: sourced
    source: inputs/next-on-wembley/idea.md
    quote: "the main user is a pair, not an individual, so every signup is really two people"
  - name: cost_to_serve_per_unit
    value: null
    unit: usd per pair per month
    kind: unknown
    settle_with: "build-cost-analyst model of LLM tokens per recommendation round x rounds per month, plus TMDb commercial licence fee spread per pair, hosting and support minutes"
  - name: tmdb_commercial_licence_cost
    value: null
    unit: usd per year
    kind: unknown
    settle_with: "written commercial quote requested from TMDb for a paid CA/US web app"
  - name: price
    value: null
    unit: usd per pair per month
    kind: unknown
    settle_with: "decision in the business case, informed by the competitive-strategist's observed price band"
  - name: builder_hours_per_week
    value: null
    unit: hours per week
    kind: unknown
    settle_with: "the decision-maker states available nights-and-weekends hours"

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
