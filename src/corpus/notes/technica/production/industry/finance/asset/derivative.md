---
tags: [note, finance]
---

# Derivative

> A **derivative** is a financial instrument whose value is derived from an underlying asset, rate, index, or event — the contract does not carry the asset itself, only an exposure to it.

The underlying can be a security (share, bond), a commodity, a currency, an interest rate, a credit event, or an index. What the contract trades is the *change* in the underlying's value over a defined horizon, settled in cash or by delivery.

## The four families

| Family | Obligation | Traded on | Pays |
| --- | --- | --- | --- |
| [Forward](forward.md) | Both parties are obliged to trade at a fixed future price | OTC, bespoke | The difference between the agreed price and the market at maturity |
| [Future](future.md) | The same obligation, standardised and cleared | Exchange | Marked to market daily through a clearing house |
| [Option](option.md) | The buyer has a right, the seller an obligation | Exchange or OTC | A premium up front; a contingent payoff later |
| [Swap](swap.md) | Both parties exchange cash flows over a schedule | OTC, increasingly cleared | The net difference between the two legs |

Beyond the four: credit derivatives (a credit default swap pays on a default), commodity and weather derivatives, contracts for difference, and warrants.

## What derivatives do

- **Hedge** — transfer a risk the holder does not want: a currency forward on an export receivable, an interest-rate swap on a floating-rate loan.
- **Speculate** — take a directional exposure with leverage, posting a fraction of the notional.
- **Arbitrage** — price the same exposure in two markets and take the difference.
- **Price discovery** — futures prices publish the market's forward view of a commodity or a rate.

## The two structures

Exchange-traded derivatives are standardised, cleared through a central counterparty, and margined daily; OTC derivatives are bespoke, bilateral, and carry counterparty risk. The post-2008 reform pushed the plain-vanilla OTC contracts into clearing houses, leaving the bespoke and the exotic bilateral.

> Leverage is the point and the danger: a small margin controls a large notional, so a small move in the underlying produces a large move in the contract. The 2008 crisis was, in part, a chain of derivatives whose underlying was a pool of mortgages nobody had priced.

## References

- [Derivative (finance) — Wikipedia](https://en.wikipedia.org/wiki/Derivative_(finance))
- [Over-the-counter (finance) — Wikipedia](https://en.wikipedia.org/wiki/Over-the-counter_(finance))
- [Central counterparty clearing — Wikipedia](https://en.wikipedia.org/wiki/Central_counterparty_clearing)
