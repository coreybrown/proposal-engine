---
mode: new-product
---

# Product idea

## The idea (required)
Next on Wembley is a TV show tracker and AI recommender for households that watch serial TV together, starting with couples. It settles "what should we watch tonight?" by tracking what each person has watched, is watching, dropped or wants to watch, then generating three ranked lists: a co-watch list for shows both people would enjoy together, and a personal list for each partner. Every pick comes with a short personalized "why," and each partner votes Agree / Disagree / Maybe, which feeds the next round of rankings.

Recommenders today are built for one viewer. The hard part for two people is the overlap in taste, and that's the thing this optimizes for. It uses each partner's watch history and ratings, in-progress shows, active streaming subscriptions (with regional availability), community ratings, episode counts, and an optional mood or genre.

It's built and running privately for my own household today (Next.js, Prisma, Anthropic API, TMDb for metadata and streaming providers). The question is whether it should be a product for other households.

## Who would build it (optional)
Me, solo, nights and weekends. No audience and no capital beyond my own.

- Company URL: https://coreywbrown.com/projects/next-on-wembley/

## Supporting documents (optional)

## Questions to answer (optional)
Is there a real market of households who'd pay for a two-person recommender, or does this only work for us?
Watch history isn't available from the streamers, so setup and upkeep fall on the user. Is there any way around that, and if not, does it kill the product?
It's a low-frequency product: you only need it between shows. Can something used a few times a month hold users or justify a price?
What are the licensing and terms-of-use limits on TMDb, streaming-availability data and LLM-generated recommendations if this goes commercial?
What would it cost to run per household, and what could it charge?

## Why now (optional)
It works for us, and the co-watch list is the part people ask about when I show it. Streaming catalogues keep growing and subscriptions keep multiplying, so the decision gets harder, not easier. LLMs make a personalized "why" cheap to generate, which wasn't true a few years ago.

## Constraints (optional)
Hard constraints I already know about: no streamer shares watch history through a public API (Netflix has a manual, single-service CSV export and that's it), TMDb's terms treat commercial use differently from personal use, and the main user is a pair, not an individual, so every signup is really two people. Don't assume those away. Judge the idea with them in place.
Canada and the US first. I won't build native mobile apps for v1.
