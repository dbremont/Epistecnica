---
tags: [note, social, market, social-element, auction, coordination, price]
qa:
 - An auction can discover the price, allocate to the highest-value use, or raise revenue — and the three do not coincide. Which one is a given auction for, and who decided that?
 - Second-price bidding is strategy-proof in theory and rare in practice. Is the gap ignorance, or does the revealed preference of designers know something the theory does not?
 - When the state auctions a public resource, the highest bidder is the buyer who can extract the most, not necessarily the one who will use it best. What would an auction for use rather than for extraction look like?
---

# Auction

> An **auction** is a sale in which the price is discovered by bidding rather than posted: buyers compete through a rule that decides who wins and what the winner pays. It is used where no price is established, where supply is fixed and the seller wants to find what the good is worth, or where the seller is the state and the object is a scarce public resource.

> It is a **market whose clearing procedure is the product**. An ordinary market has a price and a rule for taking it; an auction has a rule and the price is whatever the rule produces — which is why the design of the rule is the whole of the subject, and why auctions are the one part of economics where theory has been shown to change outcomes directly.

## Forms

| **Form** | **How bidding runs** | **Where it is used** |
| --- | --- | --- |
| **English (ascending, open)** | Bidders raise the price in the open; last bid wins at that price | Art, antiques, livestock |
| **Dutch (descending, open)** | The price starts high and falls until a bidder takes it | Cut flowers, fish, perishables |
| **Sealed-bid, first price** | One sealed bid each; highest wins and pays its bid | Construction, many tenders |
| **Sealed-bid, second price (Vickrey)** | One sealed bid each; highest wins and pays the second-highest bid | Rare in practice, central in theory |
| **Double auction** | Buyers and sellers both submit bids and offers; the market clears where they cross | Stock exchanges, electricity |
| **Clock / simultaneous ascending** | Prices rise on many lots at once; bidders switch among them until no bidder will raise | Spectrum, carbon allowances |
| **Reverse auction** | Sellers compete downward for the buyer's contract | Public procurement |

## What an auction is for

Three objectives, and a design can serve only one of them well:

| **Objective** | **The rule that serves it** | **What it sacrifices** |
| --- | --- | --- |
| **Price discovery** | Open, ascending formats | Revenue, if the reserve is set low to get entry |
| **Efficient allocation** — the good goes to whoever values it most | Second-price, or open ascending with truthful values | Revenue, because the seller gives up the winner's information rent |
| **Revenue** | First-price with a well-set reserve | Participation: high reserves deter entry and can yield less |

The conflict is not a technicalit. The state selling a spectrum licence is not selling a painting: it wants the licence to go to the operator who will use it well, the treasury wants the highest price, and the entrant wants a chance. An auction rule is a decision about which of those the state actually cares about — taken once, in the design, and then out of politics.

## The theory that matters

- **Revenue equivalence.** Under stated assumptions — risk neutrality, independent private values, symmetric bidders — first-price, second-price, English and Dutch auctions yield the *same expected revenue*. The assumptions are what fail in practice, which is why the equivalence is a benchmark rather than a prediction.
- **Strategy-proofness.** In a second-price auction the dominant strategy is to bid your true value, which is why the format is loved in theory; in a first-price auction the bidder must shade, which is why it is loved in practice (it is more robust to collusion and to entry by the seller's friends).
- **The winner's curse.** When the value is common and uncertain — an oil lease, a spectrum licence — the winner is the bidder who most overestimated it, so rational bidders shade and entry falls. Auction design for common-value objects is largely a defence against this.
- **Collusion and entry.** Bidding rings, shill bidding by the seller, and entry costs each change the outcome more than the format does. The design literature's recurring lesson: **who shows up** determines the result before the rule does.

## The cases

- **Spectrum.** The 1994–2001 auctions, and the British 3G sale in particular, are the field's demonstration that design matters: a simultaneous ascending design raised far more than the advisers had predicted, and the same design sold licences to entrants as well as incumbents.
- **Treasury debt.** Regular auctions of government securities: a routine, high-volume application where the format is standardised and the interesting question is the bidder's information.
- **Perishables.** Dutch auctions for flowers and fish exist because the good's value decays with the clock, so the descending format matches the economics of spoilage.
- **Procurement.** Reverse auctions where the state buys: the design problem is quality, not price, and the common failure is a cheap contract that has to be renegotiated.
- **Carbon and electricity.** Clock auctions over many substitutable lots, where the aim is to clear a market rather than to sell one object.

## The pathologies

- **Auctioning to the extractor.** The highest bidder is the buyer who can extract the most, which is not the same as the user who creates the most value — the reason spectrum and land auctions are usually paired with use obligations, and why the pairing is where the politics returns.
- **Collusion.** A bidding ring converts the auction into a negotiation among the ring, with the seller excluded.
- **Reserve prices as policy by stealth.** The reserve decides what does not sell, and it is usually set without debate.
- **Design capture.** The rule is designed by advisers who understand the format better than the seller's principal does, which makes the design itself an object of lobbying.

## Relation

| **Concept** | **Relation** |
| --- | --- |
| [Market](/view.html?p=notes/social/coordinator/market/market.md) | The arena; an auction is one of the procedures by which a market clears |
| [Market System](/view.html?p=notes/social/coordinator/market/market-system.md) | The structure of markets; the auction is the procedural counterpart to it |
| [Price](/view.html?p=notes/social/coordinator/price-asset/price.md) | What the auction exists to discover — its clearing price |
| [Stock](/view.html?p=notes/social/coordinator/market/instance/finantial/stock.md) | A market that clears by continuous double auction |
| [Procurement](/view.html?p=notes/social/collective/action/problem/state/procurement/procurement.md) | The reverse auction: the state as buyer rather than seller |

## References

- Vickrey, W. (1961). Counterspeculation, auctions, and competitive sealed tenders. *The Journal of Finance*, 16(1), 8–37. — the second-price idea, and the beginning of auction theory
- McAfee, R. P., & McMillan, J. (1987). Auctions and bidding. *Journal of Economic Literature*, 25(2), 699–738. — the survey that made the field legible to economists
- Milgrom, P. (1989). Auctions and bidding: A primer. *Journal of Economic Perspectives*, 3(3), 3–22. — the practitioner's account, including the common-value problem
- Klemperer, P. (2004). *Auctions: Theory and practice*. Princeton University Press. — design as engineering, with the spectrum cases
- Binmore, K., & Klemperer, P. (2002). The biggest auction ever: The sale of the British 3G telecom licences. *The Economic Journal*, 112(478), C74–C96. — what happened when the theory met a treasury
- Ausubel, L. M., & Milgrom, P. (2002). Ascending auctions with package bidding. *Frontiers of Theoretical Economics*, 1(1). — the combinatorial design problem
- Roth, A. E. (2002). The economist as engineer: Game theory, experimentation, and computation as tools for design economics. *Econometrica*, 70(4), 1341–1378. — market design as a discipline, of which auction design is the worked case
- [Auction](https://en.wikipedia.org/wiki/Auction)
- [Market](/view.html?p=notes/social/coordinator/market/market.md) · [Market System](/view.html?p=notes/social/coordinator/market/market-system.md) — the arena and its structure
- [Price](/view.html?p=notes/social/coordinator/price-asset/price.md) — the clearing price an auction discovers

- Cattle Auction System
  - https://mylivestock.co.nz/go/home/index
  - https://www.royalfloraholland.com/Entidade
  - Chicago Board of Trade
  - ...
- ...
