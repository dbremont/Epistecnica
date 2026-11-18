---
tags: [note, finance, asset]
---

# Convertible Bond

> A **convertible bond** is a corporate bond that the holder may convert into a fixed number of the issuer's shares. It is a bond with an embedded call option on the equity: the coupon pays the **floor**, the option pays the **upside**.

## Anatomy

| Term | Meaning |
| --- | --- |
| **Conversion ratio** | The number of shares each bond converts into |
| **Conversion price** | Face value divided by the conversion ratio — the effective price paid for the shares |
| **Parity** | The market value of the shares the bond would convert into |
| **Conversion premium** | The bond's price over its parity: what the investor pays for the option |
| **Bond floor** | The value of the same bond as a straight debt instrument at the issuer's credit spread |
| **Call / forced conversion** | The issuer's right to redeem; when parity exceeds the call price, redemption forces holders to convert |

## Why both sides accept it

| Issuer | Investor |
| --- | --- |
| A cheaper coupon than straight debt, because the option is worth something | Equity upside with bond downside: participation in the stock, protected at the floor |
| Deferred dilution — shares issued on conversion, later, and only if the stock rises | **Convexity**: gains accelerate with the share price, losses stop at the bond floor |
| Convertibles are easier to place with growth investors than additional equity | A yield while waiting, and a claim ahead of the equity if the issuer fails |

> The instrument is a compromise on **information**: an issuer whose equity looks cheap does not want to issue shares, and an investor who likes the equity does not want to pay for it outright. The convertible splits the difference, and the premium is the price of the disagreement.

## Pricing

> Bond floor plus option value. The floor comes from the discounting of coupons and principal at the issuer's credit spread; the option is priced on the issuer's equity, with the complication that credit and equity are **correlated** — a falling share price worsens the credit, which lowers the floor exactly when the option loses value. That dependence, not the arithmetic of either component, is what convertible desks model.

## In the asset table

> The instrument is filed as a **debt instrument** in the asset taxonomy, and it belongs there by seniority, but its behaviour is hybrid: below parity it trades like a bond, above parity like equity. That is why it sits at the boundary of [Bond](/view.html?p=notes/technica/production/industry/finance/asset/bond.md) and [Share](/view.html?p=notes/technica/production/industry/finance/asset/share.md), and why its volatility is neither the bond's nor the stock's.

## References

- [Convertible bond — Wikipedia](https://en.wikipedia.org/wiki/Convertible_bond)
- [Bond](/view.html?p=notes/technica/production/industry/finance/asset/bond.md) — the straight instrument whose floor it carries
- [Share](/view.html?p=notes/technica/production/industry/finance/asset/share.md) — the equity it converts into
- [Derivative](/view.html?p=notes/technica/production/industry/finance/asset/derivative.md) — the option embedded in it
