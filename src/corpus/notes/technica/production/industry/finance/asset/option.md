---
tags: [note, finance]
---

# Option

> An **option** is a contract giving its buyer the right, but not the obligation, to buy (**call**) or sell (**put**) an underlying at a fixed **strike** price on or before an expiry date. The buyer pays a **premium**; the seller takes the obligation.

## The four positions

| Position | Right or obligation | Gains when | Loses when |
| --- | --- | --- | --- |
| Long call | Right to buy | The underlying rises above the strike | It stays below; loss capped at the premium |
| Short call | Obligation to sell | The premium is kept | The underlying rises; loss unbounded |
| Long put | Right to sell | The underlying falls below the strike | It stays above; loss capped at the premium |
| Short put | Obligation to buy | The premium is kept | The underlying falls; loss down to zero value |

## Styles and moneyness

- **European** — exercisable only at expiry. **American** — at any time before it. **Bermudan** — on a set of dates.
- **In the money** — exercising now would pay. **At the money** — the strike equals the spot. **Out of the money** — exercising now would not pay.

## Pricing

A premium has two parts: **intrinsic value** (the payoff if exercised now) and **time value** (what the market pays for the chance that the payoff grows). The Black–Scholes–Merton model prices a European option from the spot, the strike, the time to expiry, the risk-free rate, and the **volatility** of the underlying — volatility is the input the market trades.

The **Greeks** measure the sensitivities: delta (to the underlying), gamma (to delta), theta (to time), vega (to volatility), rho (to the rate).

## Uses

Hedging — a put as insurance on a portfolio; income — a covered call against a holding; speculation with a capped loss; and the construction of structured products.

## References

- [Option (finance) — Wikipedia](https://en.wikipedia.org/wiki/Option_(finance))
- [Black–Scholes model — Wikipedia](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
- [Greeks (finance) — Wikipedia](https://en.wikipedia.org/wiki/Greeks_(finance))
