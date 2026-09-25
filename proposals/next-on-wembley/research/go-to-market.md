# Go-to-market: Next on Wembley

## Bottom line
- **Finding:** No channel is free, and none is cheap at scale. Manual, community-led outreach can plausibly land the first 10-100 pairs at an estimated ~$240/pair in founder time (below the ~$49-60/year comparable price only if lifetime value spans several years, which is unproven). Every channel that could scale past that — paid social, paid search, influencer spend — has an unknown or likely-unaffordable CAC at this price, and the product's own choices (web-only, no app store presence) remove the one channel (app-store search/browse) that the closest comparables actually use to acquire users for free.
- **Assumptions:** A4 mostly contradicted at scale, holds narrowly for a hand-built first cohort — the builder has no paid-acquisition budget or audience, and the one plausible channel (organic community engagement) is bounded by his own hours, not by market size, and by an unsourced pair-completion rate.
- **Kill check:** not a kill — I found no evidence that reaching the segments is categorically impossible at the observed comparable prices — a founder-time-only channel exists for a small first cohort — but I also found no evidence of a channel that both reaches pairs (not just individuals) and scales beyond the builder's personal hours at an affordable CAC. That gap is a high-severity, unresolved risk, not a proven kill.

## Where the segments gather
Sizes below are as reported by the community or platform itself (or a tool reading its live count), fetched 2026-09-25. None of these communities are couples-only or co-watching-specific; they are proxies for where individual trackers or TV-obsessives gather, which is the closest observable thing to S1-S3.

| Place | Segment fit | Size | Source |
|---|---|---|---|
| r/trakt | S2 (existing trackers) | ~12,000 members | subredditstats.com, fetched 2026-09-25 |
| r/television | S1 (general TV-watchers, unfiltered for couples) | ~18.1M members | thehiveindex.com / gummysearch.com, fetched 2026-09-25 |
| r/LongDistance | S3 (remote co-watching couples, unfiltered for TV-specific behaviour) | 2,481,980 members | reddapi.dev, fetched 2026-09-25 |
| Serializd (app + #serializd on TikTok) | S2 | Not disclosed by the company in what I could fetch; described as a growing "Letterboxd for TV" community, and it shipped a TV Time data-import in July 2026 to catch that app's users | hobiapp.com and TechCrunch coverage, fetched 2026-09-25; **size unknown**, no user-count disclosure found |
| JustWatch (the product's own data provider) | S1 (broad "what to watch" audience, not couple-specific) | over 50 million monthly users across web and app, 15 million MAU in the US | justwatch.com/us/next-generation-movie-marketing, fetched 2026-09-25 | 
| TV Time (defunct as of 2026-07-15) | S1/S2, historical | 26 million users at shutdown | TechTimes, "TV Time Closes July 15: 26 Million Users Face Permanent Watch History Deletion," fetched 2026-09-25 |

**No community found is couple-specific.** There is no "co-watching couples" subreddit, forum or newsletter with a disclosed size. S1/S2/S3 as canonically defined have to be reached inside general TV communities (where most members are single trackers, not couples) or general relationship communities (where most members aren't TV-focused). Either way, the addressable slice of any community above is an unverified fraction of its total, not the total itself — treat every size above as an audience ceiling, not a segment count.

## Channels

| Channel | Segment fit | CAC range (kind + source) | Time to first customer | Scalability | Restrictions |
|---|---|---|---|---|---|
| **Community-led organic** (genuine participation in r/trakt, r/television, TV-tracker subreddits, r/LongDistance; personal network) | S1/S2 direct, S3 partial | **estimate**: ~$240/activated pair. Reasoning: 3 hours of founder time per activated pair (finding a fit, engaging authentically, walking one partner through setup, following up until the second partner activates — the doubled-activation problem the opportunity model already flags) x $80/hour, the median hourly wage for a US marketing manager, May 2025, BLS Occupational Employment and Wage Statistics (bls.gov/news.release/ocwage.t01.htm, fetched 2026-09-25; $166,790/year median = $80/hour). Replace with: measured hours-per-activated-pair from the first 10 hand-run signups. | Days to weeks — no approval or ad-review cycle | Low. Ceiling is founder hours, not audience size; ~39% of subreddits founders would pitch in ban self-promotion outright and another ~22% cap it (a survey of 49 subreddits, OneUp, "We Checked the Self-Promotion Rules of 49 Subreddits," fetched 2026-09-25), so most posting must be genuine participation, not a repeatable ad buy | Reddit site-wide Rule 2 (no spam/content manipulation); most relevant subreddits ban or cap self-promotion |
| **Paid social** (Meta/Instagram, TikTok ads) | S1/S3 (interest-based targeting on streaming/TV only — relationship status can't be targeted directly, see restrictions) | **unknown**. The only entertainment-app figure found, $1.10 average CPI (Mapendo, "Cost per Install by App Category: 2025 Trends," fetched 2026-09-25), is a mobile-app-install cost and doesn't apply — this product ships no native app. A generic "$180 paid-social CAC" figure surfaced in search results with no dated, named-company source, so it is discarded per the contract. | Days (ad accounts approve quickly) but 120-180 days to fully evaluate paid-social quality per category norms | Uncapped in theory, but untested for this product and this price | Meta's Personal Attributes policy prohibits ad copy that states or implies knowledge of a viewer's relationship status (transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes, fetched 2026-09-25); relationship-status detailed targeting is not available on Meta, so ads must target broad interest categories (streaming, TV shows), which is less precise and likely raises cost | 
| **Paid search** | S1 (people actively searching "what to watch tonight," "TV show tracker") | **unknown**. No accessible, dated keyword-volume or CPC tool was used; a number from memory would violate the number-integrity rule. | Unknown | Unknown | None category-specific found |
| **Influencer/creator sponsorship** (TikTok "what to watch" creators) | S1 | **unknown as CAC**, though the input cost is sourced: TikTok micro-influencers (10K-100K followers) charge roughly $200-$800 per video (Influencer Marketing Hub, "TikTok Influencer Rates in 2026," fetched 2026-09-25). Converting that to CAC needs a click-to-signup rate and a second-partner-activation rate; neither is sourced, so the figure is left `unknown` rather than invented. | Days to weeks to book a creator | Bounded by the small number of TV-recommendation creators and repeat-fatigue | None found specific to this category |
| **Content/SEO** | S1 | Unknown. No accessible search-volume tool used. | Months (SEO is slow by nature) | Low for a solo builder's available hours; competes with JustWatch's own SEO-strength "streaming guide" (50M+ MAU) | None found |
| **Partnerships/integrations** (with existing trackers, date-night newsletters, couples content) | S2 (tracker import), S1/S3 (content partners) | Unknown; no partnership terms sourced. Notable structural fact: **JustWatch, the product's own data source, is itself building a competing consumer product** (JustWatch TV, a streaming service launching across 14 markets, per broadbandtvnews.com, fetched 2026-09-25), which makes it an unlikely acquisition partner even though it is a data dependency. | Unknown | Unknown | The TMDb/JustWatch attribution terms (already flagged by the opportunity model, A6) govern any co-marketing use of their data or branding |
| **Marketplace/app store (ASO)** | S1/S2 (this is how the closest comparables are actually found) | N/A — not usable in v1 | N/A | N/A | **Ruled out by the builder's own constraint**: "no native mobile apps in v1." Trakt, Serializd, and the now-defunct TV Time are all found primarily through app-store search and browse. This product cannot use that channel at all while it remains web-only. |
| **Referral / word of mouth within a pair** | All | Not a customer-acquisition channel for new *pairs* — the product's built-in virality reaches the second half of an already-acquired pair, not a new household. No sourced or plausible mechanism found for one pair referring another pair at scale (co-watching couples don't typically recruit other couples into a shared tracking tool). | N/A | Low, unverified | None found |

## Sales motion and price floor
- The only comparable prices found, both from named companies' own pricing pages/announcements: **Letterboxd Patron $49/year** (letterboxd.com/about/pro, fetched 2026-09-25) and **Trakt VIP $60/year**, standardized May 2025 after a 100%+ price increase from $30/year (alternativeto.net, "Trakt.tv has set stricter limits... raised VIP subscription prices by 100%," and "Trakt announces all VIP renewals will switch to a new standard rate," fetched 2026-09-25). Both are *per individual*, not per pair — this product's unit of sale (a pair) has no direct comparable price found.
- At $49-60/year (roughly $4-5/month per person, and the low end of two comparable products), **only a self-serve motion is affordable.** Sales-assisted and field-sales motions are calibrated to a wholly different price scale: publicly benchmarked SaaS thresholds put sales-assisted motions at annual contract values above roughly $15,000-$25,000 and field sales above $150,000 (Artisan Strategies / Saber, "SaaS Sales Cycle Length Benchmarks 2026" and "ACV... Benchmarks," fetched 2026-09-25). Those figures measure B2B software, not a consumer subscription — the geography, buyer type and price scale don't match this product, so I use them only as an order-of-magnitude floor, not a sourced figure for this case: this product's plausible price is 2-3 orders of magnitude below the point at which any paid human sales touch becomes affordable. **Estimate, conservative reading: self-serve is the only motion this product's price can ever fund; a support inbox, not a sales team, is the ceiling on human involvement.**
- This reinforces, rather than resolves, the opportunity model's A4 and A3: self-serve at ~$50-100/year (accounting for a pair possibly costing more than an individual) has to be funded by a CAC low enough to pay back within a retention period that a low-frequency, "between shows" product has not shown it can sustain.

## Incumbent channels
Evidence found, not asserted:
- **Trakt**: native iOS/Android apps (App Store/Google Play discovery), a public API used by third-party integrations (Kodi, Plex-adjacent tools), and an active subreddit (r/trakt, ~12,000 members) used for support and feature discussion. VIP subscription priced at $60/year as of May 2025, more than double its prior $30/year price — evidence that this exact category can sustain a price increase without collapsing the paying base, but also that early pricing was set low.
- **Serializd**: native iOS/Android apps, a visible TikTok community presence (#serializd), and an opportunistic move to ship a direct TV Time data-import within roughly two weeks of TV Time's July 2026 shutdown announcement — an observed tactic (catching a dying competitor's users at the moment of churn) rather than a steady-state channel.
- **TV Time (defunct)**: was free, reached 26 million users, and according to its own shutdown statement was closed because "it was no longer sustainable to continue operating the service as a free app, and there was not enough demand for a paid app" (TechCrunch, "Popular TV-tracking app TV Time is shutting down as company focuses on AI," fetched 2026-09-25). This is direct, dated evidence bearing on A3 and A8: a well-distributed, venture-backed incumbent in the adjacent category tested a paid conversion and could not sustain it.
- **JustWatch**: this product's own data dependency. 50M+ monthly users, its own "Sponsored Recommendations" native-ad product for studios and streamers, an Xbox app, and (announced 2026-09) its own ad-supported streaming service. It is both the closest thing to an incumbent "what to watch" audience at scale and, per its own recent moves, a company building a directly competing consumer product rather than a distribution partner.
- **Letterboxd** (adjacent category, film not TV, cited as the clearest same-shape precedent): launched web-first and added apps later, which is a real precedent that a web-only launch is viable in this exact kind of tracking/social product category. This run did not find a sourced breakdown of Letterboxd's acquisition spend or channel mix, so its growth mechanism is not claimed as evidence, only its web-first sequencing.

## Gatekeeper restrictions
- **Meta/Instagram ads**: the Personal Attributes policy bars ad copy that states or implies a viewer's relationship status; combined with the removal of relationship-status detailed targeting, ads must be written and targeted around streaming/TV interests generically, not "for couples," which works against precision and likely raises cost per qualified click (transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes, fetched 2026-09-25).
- **Reddit**: site content policy (Rule 2, reddit.com/policies) prohibits spam/content manipulation; a survey found roughly 39% of subreddits founders commonly pitch in ban self-promotion outright and 22% allow only a capped rate (OneUp, "We Checked the Self-Promotion Rules of 49 Subreddits," fetched 2026-09-25). This bounds, but does not eliminate, the community channel.
- **App stores**: not applicable — the product carries no native app in v1 by the builder's own constraint, so Apple/Google review policy is moot for now, but so is the discovery surface those stores provide.
- No category-specific restriction (comparable to gambling, health or financial-services ad certification) was found for a TV-recommendation product on Meta, Google or TikTok's ad policies.

## The builder's distribution
None found. The opportunity model already establishes this and it is confirmed here: the builder's home page lists career and audience figures that belong to a former employer (PENN Entertainment, theScore), not to him; there is no newsletter, no existing user base, no partner list, and no disclosed marketing budget. Every channel above therefore starts at zero owned reach. The one asset that matters for GTM specifically is the builder's own stated skill set ("growth and retention, monetization, experimentation"), which lowers execution risk on running a GTM test well, but is not itself a distribution channel.

## Launch sequence
- **First 10**: hand-recruited, by name. Concretely: the builder's own stated anecdote ("people ask about it when I show it") — follow up with those specific people first, since they are the only named humans who have expressed interest; then 2-3 genuine posts (not ads) in r/trakt and r/television framed as sharing a build, respecting each subreddit's self-promotion rule; then direct outreach in r/LongDistance to couples who mention scheduling shared viewing. Each of these 10 gets concierge onboarding (the builder manually helps both partners complete setup) — this is the "named test" already flagged in the opportunity model's risk register (10 non-builder couples, day-30 completion measured).
- **First 100**: a Product Hunt or Indie Hackers launch as a credibility/awareness event, not a conversion engine — benchmarked expectations are modest: an average indie Product Hunt launch produces roughly 47 signups and fewer than 3 paying customers (shno.co, "Product Hunt Launch Statistics for 2026," and awesome-directories.com, "Indie Hackers Launch Strategy," fetched 2026-09-25; Indie Hackers itself is cited in the same sources as converting several times better, ~23% vs Product Hunt's ~3%, though from a smaller, more engaged audience). Pair this with continued organic community posting and the TikTok "what to watch" creator channel tested with one or two micro-influencer bookings ($200-$800 each) to see if a click-to-signup rate can be measured at all.
- **First repeatable channel**: cannot be named yet. Every channel with a sourced-enough CAC to compare against the ~$49-60/year comparable price either doesn't scale past founder hours (community-led) or has an unknown CAC that a small paid test would have to establish (paid social, influencer, search). The honest launch-sequence conclusion is: prove the community-led motion converts and retains through the first 50-100 pairs by hand, and use that data — not benchmarks from other categories — to decide whether any paid channel can pay back before scaling spend.

## Open questions for the decision-maker
1. Given no channel scales past founder hours without an unknown or likely-unaffordable CAC, is the plan to stay hand-built and small (tens to low hundreds of pairs) rather than to seek a paid-acquisition-scalable business?
2. Is a native mobile app (unlocking app-store discovery, the channel the closest comparables actually use) worth revisiting after v1, given it's the one channel with a somewhat-sourced, comparatively low CAC (via app-install advertising) that this web-only version can't access?
3. Who are the specific people behind "people ask about it when I show it" — are any of them reachable now, for the first 10?
4. Given JustWatch (the data provider) is now building its own competing consumer streaming product, is there a plan if JustWatch's terms or provider-data access change?

KEY_FIGURES:
  - name: cac
    value: 240
    unit: usd per activated pair (community-led organic channel, primary/first-cohort channel)
    kind: estimate
    reasoning: "3 hours of founder time per activated pair (finding a fit, engaging authentically, onboarding one partner, following up until the second partner activates) x $80/hour, the median hourly wage for a US marketing manager, May 2025 (BLS OEWS, bls.gov/news.release/ocwage.t01.htm: median annual wage $166,790 = ~$80/hour). Hours-per-pair is a founder judgment, not measured."
    replace_with: "measured founder hours per activated pair from the first 10 hand-onboarded pairs (the named test already in the opportunity model's risk register)"
  - name: cac_paid_social
    value: null
    unit: usd per activated pair
    kind: unknown
    settle_with: "a 2-week landing page plus $300 of paid social, measuring cost per activated pair (the test already named in the opportunity model's risk register)"
  - name: cac_paid_search
    value: null
    unit: usd per paying customer
    kind: unknown
    settle_with: "an accessible, dated keyword-volume/CPC source (e.g. a Google Ads account or a licensed keyword-research tool) for terms like \"what to watch tonight\" and \"tv show tracker\""
  - name: cac_influencer
    value: null
    unit: usd per activated pair
    kind: unknown
    settle_with: "book 1-2 TikTok micro-influencers ($200-$800/video, sourced range) and measure click-to-signup and second-partner-activation rates directly"
  - name: competitor_price_low
    value: 49
    unit: usd per year, per individual
    kind: sourced
    source: https://letterboxd.com/about/pro/
    fetched: 2026-09-25
    quote: "Patron ... $49 per year"
  - name: competitor_price_high
    value: 60
    unit: usd per year, per individual
    kind: sourced
    source: https://alternativeto.net/news/2025/5/trakt-announces-all-vip-renewals-will-switch-to-a-new-standard-rate-doubling-prices/
    fetched: 2026-09-25
    quote: "Trakt announces all VIP renewals will switch to a new standard rate, doubling prices"
  - name: tv_time_users_at_shutdown
    value: 26000000
    unit: users
    kind: sourced
    source: https://www.techtimes.com/articles/319583/20260703/tv-time-closes-july-15-26-million-users-face-permanent-watch-history-deletion.htm
    fetched: 2026-09-25
    quote: "TV Time Closes July 15: 26 Million Users Face Permanent Watch History Deletion"
  - name: reddit_subreddits_banning_selfpromo_share
    value: 0.39
    unit: share of surveyed subreddits that ban self-promotion outright
    kind: sourced
    source: https://oneup.today/blogs/reddit-selfpromo-rules-study-2026
    fetched: 2026-09-25
    quote: "We Checked the Self-Promotion Rules of 49 Subreddits Founders Pitch In. 61% Ban It."
    note: "The article's own breakdown gives 39% banning self-promotion outright, with a further 22% allowing only a capped rate; the headline '61%' bundles both groups."
  - name: builder_hourly_opportunity_cost
    value: 80
    unit: usd per hour
    kind: sourced
    source: https://www.bls.gov/news.release/ocwage.t01.htm
    fetched: 2026-09-25
    quote: "Marketing Managers ... median annual wage $166,790"
    note: "Used as a proxy for a senior product/marketing professional's opportunity cost; occupation title is a proxy, not an exact match to the builder's role."

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
