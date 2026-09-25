# Regulatory scout — Pass 1 (the map)

## Bottom line
- **Finding:** No regulator licenses this business — it's an unregulated consumer web app, not a money-transmission, gambling, health, or advice-liability activity. The real gate is contractual, not statutory: **TMDb's terms restrict use of its API "in connection with... a machine learning (ML) or artificial intelligence (AI) based Application"** and name LLMs/chatbots as a use that requires a separate written commercial agreement (TMDb API Terms of Use, fetched 2026-09-25) — and this product's core feature is an LLM generating picks from TMDb data. Whether TMDb will license that use at all, and at what cost, is unknown and untested. A second, separate gate sits behind it: JustWatch's own terms (the source of the streaming-availability data TMDb passes through) separately ban commercial use and scraping of "the Service Content," with no public commercial path stated on JustWatch's own terms page.
- **Your questions:**
  - Q4: TMDb requires a written commercial agreement for any paid app, explicitly calls out LLM/chatbot use as needing one, caps caching at 6 months, and requires logo attribution; cost and AI-use approval are both unconfirmed. JustWatch's own terms add a second, separately unresolved licensing question for the streaming-availability data. Anthropic's terms permit commercial use of outputs with no product-category restriction found. See Licenses and IP and liability below.
  - Q2 (contributing): No safe terms-of-use workaround exists to auto-capture watch history. Netflix's Terms of Use (fetched 2026-09-25) ban "any robot, spider, scraper or other automated means," "data mining, data gathering or extraction," and any use "in connection with... training... any machine learning tool" — this covers a browser extension or scraper built to read a user's own logged-in Netflix history page. Other major streamers were not individually checked in this pass but commonly carry similar anti-automation clauses; treat that as unverified, not assumed-safe. This does not by itself kill the product (manual entry and tracker-app imports remain open), but it forecloses the most obvious way to reduce onboarding friction.
  - **Assumptions:** A6 (opportunity model) remains unproven and is now more specifically located: it isn't just "TMDb requires a commercial agreement," it's "TMDb's terms single out AI-based apps as requiring one, and it's unknown whether they grant it to a solo builder." A2 is reinforced: manual/import-based history capture isn't just the only option because no API exists — it's also because automated capture would breach at least Netflix's ToS.

## Activity classification
Next on Wembley is a consumer recommendation and tracking web app. Checked against the categories in this agent's brief, none of the following apply as currently scoped: money transmission or lending, investment/betting/tipping advice, gambling, health or medical advice or devices, insurance, legal services, employment/hiring, housing or credit, services targeted at minors, telehealth, alcohol/cannabis/firearms, telecom, or data brokerage (no sale or sharing of personal information to third parties for compensation is stated in the idea — see Data rules for what would change that). There is no core-activity licensing bar.

The exposure instead comes from three places: (1) third-party data-provider terms that treat AI-based commercial use differently from ordinary commercial use (TMDb, and possibly JustWatch), (2) streaming platforms' anti-scraping terms, which constrain how watch-history data can ever be captured, and (3) general personal-data law triggered by tracking two named people's private viewing habits and sending that data to a third-party LLM.

## Jurisdiction map

| Market | Status | Governing rule | Link |
|---|---|---|---|
| US — federal, core activity (consumer recommendation app) | clear | Not a regulated activity under any category checked above | — (classification above) |
| US/global — TMDb data layer, standard (non-AI, non-commercial) use | clear | Free tier permitted for non-commercial use | https://www.themoviedb.org/api-terms-of-use (fetched 2026-09-25) |
| US/global — TMDb data layer, this product's actual use (paid app + LLM-generated recommendations) | needs license, outcome unconfirmed | "You must enter into a written agreement with TMDB that expressly permits Your commercial use," and Restrictions bar use "in connection with, including for training, a machine learning (ML) or artificial intelligence (AI) based Application" absent that agreement; commercial-use examples explicitly include "large language models and Chatbots" | https://www.themoviedb.org/api-terms-of-use (fetched 2026-09-25) |
| US/global — JustWatch-sourced streaming-availability data | needs license, path unclear | JustWatch's own terms restrict use to "personal and non-commercial use only" and bar users from using "the Service Content in any way for any public or commercial purpose"; no public commercial-licensing process is stated on JustWatch's own terms page | https://support.justwatch.com/article/just-watchs-terms-of-use (fetched 2026-09-25) |
| US/global — watch-history capture via scraping or a browser extension reading a user's own Netflix account | prohibited (contractually) | Netflix Terms of Use ban automated access/bots, "data mining, data gathering or extraction," and use "in connection with... training... any machine learning tool" | https://help.netflix.com/legal/termsofuse (fetched 2026-09-25) |
| US — federal, video-viewing-record privacy | restricted, unclear scope | Video Privacy Protection Act, 18 U.S.C. § 2710, restricts disclosure of records identifying a person's video viewing by a "video tape service provider"; courts have read this broadly against streaming and video-adjacent services, but it is unsettled whether a companion app that never delivers video itself (and only stores user-entered metadata) qualifies | https://www.law.cornell.edu/uscode/text/18/2710 |
| California | clear now; compliance obligations attach at scale | CCPA/CPRA applies to for-profit businesses that do business in California and either have gross annual revenue over $25,000,000, or buy/sell/share the personal information of 100,000+ California residents/households, or derive 50%+ of revenue from selling personal information — none of which a pre-launch solo product meets yet | https://www.oag.ca.gov/privacy/ccpa (fetched 2026-09-25) |
| Canada — federal | needs compliance from day one (no revenue threshold) | PIPEDA applies to any organization collecting personal information in the course of commercial activity, regardless of size | https://laws-lois.justice.gc.ca/eng/acts/p-8.6/ |
| Quebec | needs compliance from day one, stricter than PIPEDA | Act respecting the protection of personal information in the private sector ("Law 25") imposes privacy-impact-assessment and consent obligations that apply from an organization's first Quebec user, with no small-business carve-out identified in this pass | https://www.quebec.ca/en/gouvernement/politiques-orientations/vie-privee/loi-25 |
| EU / UK | out of scope for v1 | idea.md states "Canada and the US first"; no EU/UK GDPR assessment done here — required before any expansion into those markets | inputs/next-on-wembley/idea.md |

## Licenses

| Requirement | Applies to | Needed for | Cost | Time | Source |
|---|---|---|---|---|---|
| TMDb written commercial agreement | Global (US/Canada launch) | Any commercial use of TMDb metadata and provider data, and specifically any AI/LLM-based use | Unknown — terms say only "may be subject to, among other things, payment of fees," no published rate | Unknown | https://www.themoviedb.org/api-terms-of-use |
| JustWatch commercial permission (possibly separate from TMDb's) | Global | Streaming-availability data, sourced from JustWatch and passed through TMDb's watch-providers endpoint | Unknown; JustWatch's own terms state no public commercial-licensing path | Unknown | https://support.justwatch.com/article/just-watchs-terms-of-use |
| Anthropic API — standard commercial terms | Global | LLM-generated recommendations and "why" text | Standard usage-based API pricing; commercial use of outputs is permitted with no product-category restriction found | N/A — accepted at signup | Anthropic Commercial Terms of Service, https://www.anthropic.com/legal/archive/c87a6bf8-106e-47d8-9b7b-47ae3a0fecbf (per search of Anthropic's published terms, not independently fetched in full this pass — flagged below) |
| Business/sales-tax registration for a CA/US SaaS subscription | Canada, and any US states sold into | Generic to any subscription business; not idea-specific | Not researched — standard startup step, not a differentiator for this idea | — | — |
| Money transmission, gambling, health, insurance, legal, telehealth, alcohol/cannabis/firearms, telecom licenses | — | None apply as scoped | — | — | Activity classification above |
| Data-broker registration (e.g., California's Delete Act registry, Cal. Civ. Code § 1798.99.80; Vermont's data broker law, 9 V.S.A. § 2446) | Not triggered now | Would be triggered only if a future business model sells or shares household viewing PI with third parties for compensation — not stated in the idea | — | — | flagged for future pivots only |

**Note on the Anthropic citation:** the Commercial Terms of Service link above was located via search, not fetched and read in full during this pass. Treat the "no product-category restriction" finding as **asserted, medium confidence**, and confirm by fetching Anthropic's Usage Policy directly before relying on it.

## IP and liability

- **Show titles, artwork, and TMDb/JustWatch-sourced images.** Referring to copyrighted show titles to recommend them is standard nominative fair use (the three-part test from *New Kids on the Block v. News America Publishing, Inc.*, 971 F.2d 302 (9th Cir. 1992)): the show can't be identified without using its title, only as much of the mark is used as needed, and nothing implies sponsorship or endorsement — which is why TMDb's required attribution line ("not endorsed, certified, or otherwise approved by TMDB") matters operationally, not just contractually. Poster and artwork images are licensed through TMDb itself; using them outside a valid TMDb commercial agreement (see Licenses) carries copyright exposure independent of the API terms.
- **LLM-generated "why" text.** An AI-generated explanation that invents plot details, misstates episode counts, or gets availability wrong is a factual-accuracy/consumer-trust problem (routed to ethics-trust-safety per the opportunity model) and a low-probability but real deceptive-advertising exposure if the product ever markets accuracy claims (e.g., the builder's own unverified "~50% watch-through" figure) without substantiation — see the FTC's business guidance on AI-generated content claims, and Canada's Competition Act misleading-representations provisions, for the general standard; neither was fetched in this pass, both flagged as low-confidence/for counsel.
- **Household PII sent to a third-party processor.** Each recommendation call likely sends both partners' combined watch history and ratings to Anthropic's API. That is a disclosure of personal information to a data processor/sub-processor and needs a documented lawful basis and privacy-policy disclosure under PIPEDA, Quebec's Law 25, and (once thresholds are met) CCPA. This is a design/documentation requirement, not a bar to operating.
- **VPPA (US).** See the jurisdiction map — unclear whether it applies to a companion app that stores user-entered watch data rather than delivering video, but the statute exists specifically to restrict disclosure of "a person's video viewing" and this product both stores and forwards that data to a third party (Anthropic). Worth a specific legal question (see Vet before you run) rather than a settled answer either way.

## Data rules

- **PIPEDA (Canada, federal)** and **Quebec's Law 25** apply from the first Canadian user, with no revenue or size threshold. Both require documented consent and disclosure for collecting and processing two people's viewing habits and sharing them with TMDb and Anthropic as service providers.
- **CCPA/CPRA (California)** does not apply yet at pre-launch, solo-builder scale (thresholds: $25M revenue, or 100,000+ consumers' PI, or 50%+ revenue from selling PI — California Attorney General, fetched 2026-09-25). It would begin to apply if the product scales past the 100,000-consumer PI threshold, regardless of revenue.
- **VPPA (US, federal)** — see above; unclear, flag for counsel, don't assume it's out of scope.
- **COPPA, HIPAA, BIPA** — not triggered as scoped. The product isn't marketed to children, doesn't process health information, and (unless a future feature adds biometric identifiers such as face/voice) doesn't process biometric data.
- **GDPR/UK GDPR** — out of scope for v1 per idea.md's stated markets; required before any EU/UK expansion.

## Gatekeepers

- **Stripe.** Its published Restricted Businesses list (fetched 2026-09-25) does not name subscription/consumer-recommendation apps, AI-generated-content services in general, or data-licensing arrangements as restricted or prohibited categories; the list's focus is illegal goods, adult content, gambling, weapons, and regulated financial services, none of which apply here. https://stripe.com/legal/restricted-businesses
- **PayPal.** Its Acceptable Use Policy framework (fetched via search 2026-09-25) was not read in full text in this pass; the general categories found (payment aggregation, credential storage) don't implicate this business, but the full policy should be read directly before relying on this. https://www.paypal.com/us/legalhub/paypal/acceptableuse-full
- **Neither processor's public list addresses the actual risk here** — that TMDb or JustWatch could revoke API access for a terms violation, which would be a business-continuity failure, not a payments-restriction one.
- **App store guidelines.** Not applicable for v1 — idea.md states no native mobile apps in v1. Deferred; would need review (e.g., Apple's third-party-content and IP-rights guidelines) before any native build.
- **Ad platforms (Google Ads, Meta).** Not independently checked in this pass since no revenue or GTM channel model is set yet (per opportunity model, A4 and the revenue model are both open). The product isn't in an obviously restricted category (not alcohol, gambling, dating, or a "personal hardship" category), but if a paid-acquisition plan later builds custom audiences from viewing-preference data, each platform's data-source and personalization policies would need a direct check at that time.

## Vet before you run
Ordered by what each answer blocks.

1. **Paid expert or direct written query to TMDb** (blocks the entire data layer): does TMDb's commercial-agreement path extend to AI/LLM-based recommendation apps at all — given its Restrictions clause names AI/ML-based applications and its commercial-use examples name "large language models and Chatbots" — and if so, at what cost and under what caching/attribution terms? Until this is answered, the product's core data source may not be licensable at any price.
2. **Paid expert or direct written query to JustWatch** (blocks streaming-availability data, a core input to the co-watch feature): does TMDb's commercial agreement cover redistribution of JustWatch-sourced provider data, or does JustWatch require a second, separate commercial agreement given its own terms bar commercial use of "the Service Content"?
3. **1-hour consult with a Canadian privacy/tech lawyer** (blocks privacy-policy and consent-flow design, needed before any Canadian signup): does sending one household's combined viewing data to Anthropic's API require specific standalone consent language under PIPEDA and Quebec's Law 25, beyond a standard privacy policy, and does the VPPA plausibly reach a companion app that never delivers video?
4. **Decision-maker confirmation, informed by this map** (blocks any GTM plan that assumes lower-friction onboarding): accept that no safe technical workaround exists for auto-capturing watch history from a user's own streaming account without risking that user's streamer account and possible ToS-breach exposure, and plan onboarding around manual entry and tracker-app imports only.
5. **Data pull at the time of Stripe/PayPal onboarding** (cheap, low urgency): re-check both processors' current restricted-business lists, since they change, and confirm the business still isn't newly restricted once TMDb/JustWatch licensing terms (and any resulting data-rights disclosures on the Stripe application) are known.

## Open questions for the decision-maker
1. Are you willing to fund a paid consult and a direct written query to TMDb and JustWatch before further build investment, given the core data layer's licensing terms for AI-based use are unconfirmed?
2. If TMDb refuses to license AI-based commercial use, or prices it out of reach, are you willing to evaluate replacing it (a re-platforming cost not yet estimated), or does that end the idea?
3. Given PIPEDA and Quebec's Law 25 apply immediately with no revenue floor, are you prepared to build a compliant consent flow and privacy policy before the first non-builder Canadian household signs up?

KEY_FIGURES:
  - name: tmdb_cache_limit_months
    value: 6
    unit: months maximum caching of tmdb data
    kind: sourced
    source: https://www.themoviedb.org/api-terms-of-use
    fetched: 2026-09-25
    quote: "Cache, for longer than 6 months, any information obtained through or from TMDB or the TMDB APIs"
  - name: tmdb_commercial_licence_cost
    value: null
    unit: usd per year
    kind: unknown
    settle_with: "written commercial quote requested from TMDb, specifically asking whether AI/LLM-based recommendation use is licensable at all (TMDb's Restrictions clause names AI/ML-based applications and its commercial-use examples name LLMs and chatbots)"
  - name: justwatch_commercial_licence_cost
    value: null
    unit: usd per year
    kind: unknown
    settle_with: "direct written query to JustWatch (their own terms state personal/non-commercial use only and don't publish a commercial-licensing path)"
  - name: ccpa_revenue_threshold_usd
    value: 25000000
    unit: usd annual gross revenue (one of three independent CCPA-applicability triggers)
    kind: sourced
    source: https://www.oag.ca.gov/privacy/ccpa
    fetched: 2026-09-25
    quote: "Have a gross annual revenue of over $25 million"
  - name: ccpa_consumer_count_threshold
    value: 100000
    unit: california residents or households whose personal information is bought, sold, or shared per year (one of three independent CCPA-applicability triggers)
    kind: sourced
    source: https://www.oag.ca.gov/privacy/ccpa
    fetched: 2026-09-25
    quote: "Buy, sell, or share the personal information of 100,000 or more California residents or households"

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
