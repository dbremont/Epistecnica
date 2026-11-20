---
tags: [note, finance]
---

# Forward

> A **forward** is a bilateral contract to buy or sell an asset at a price agreed now and settled on a fixed future date — no premium changes hands at inception, and both parties are bound.

## Forward vs future

| | Forward | [Future](future.md) |
| --- | --- | --- |
| Venue | OTC, bilateral | Exchange |
| Terms | Bespoke: amount, date, delivery | Standardised |
| Counterparty risk | Yes, the other party may default | Cleared by a central counterparty |
| Settlement | At maturity | Marked to market daily |
| Liquidity | Low; hard to close out | High; can be offset |

The forward is the older and simpler instrument; the future is the forward standardised and cleared so that it can trade.

## Pricing

The forward price is the spot price carried to the delivery date: `F = S × (1 + r − c)`, where `r` is the financing rate and `c` the carry — the income or storage cost of the underlying. For a currency, the same relation is covered interest parity: the forward rate is the spot rate times the interest-rate differential.

At inception the forward has zero value; as the spot moves, one side accrues a claim on the other. That claim is the credit exposure.

## Uses

- **FX hedging** — an exporter with a dollar receivable fixes the euro amount now.
- **Commodity hedging** — an airline fixes the price of jet fuel.
- **Interest-rate hedging** — a borrower fixes the cost of a future loan through a forward rate agreement.
- **Synthetic exposure** — a holder who cannot buy the asset takes the forward instead.

## References

- [Forward contract — Wikipedia](https://en.wikipedia.org/wiki/Forward_contract)
- [Forward rate agreement — Wikipedia](https://en.wikipedia.org/wiki/Forward_rate_agreement)
- [Covered interest parity — Wikipedia](https://en.wikipedia.org/wiki/Interest_rate_parity)
