---
tags: [note, finance]
---

# Swap

> A **swap** is an agreement between two parties to exchange cash flows over a schedule, computed on a **notional** principal that is usually not exchanged.

## The main families

| Swap | Legs | Used to |
| --- | --- | --- |
| **Interest-rate swap** | Fixed rate against a floating rate (e.g. SOFR) | Convert a fixed-rate liability into floating, or the reverse |
| **Currency swap** | Principal and interest in one currency against another | Hedge foreign-currency funding or investment |
| **Credit default swap** | A premium against a payment on a credit event | Transfer credit risk without selling the bond |
| **Commodity swap** | Fixed price against a floating price for a commodity | Fix input or output prices |
| **Equity swap** | Equity return against a rate | Gain equity exposure without holding the shares |

The plain-vanilla interest-rate swap is the largest segment: a borrower with a floating-rate loan enters a swap paying fixed and receiving floating, and the net cost becomes fixed.

## Mechanics

Only the **net** difference between the legs changes hands on each payment date, which is why the notional can be large relative to the cash that moves. At inception the swap is priced to have zero value; the fixed rate that achieves this is the **swap rate**, and the set of swap rates across maturities is the swap curve.

Counterparty risk is the risk that the other side defaults when the swap has positive value to you. Central clearing and collateral agreements manage it, and the 2008 crisis made clearing mandatory for the standardised contracts.

## References

- [Swap (finance) — Wikipedia](https://en.wikipedia.org/wiki/Swap_(finance))
- [Interest rate swap — Wikipedia](https://en.wikipedia.org/wiki/Interest_rate_swap)
- [Credit default swap — Wikipedia](https://en.wikipedia.org/wiki/Credit_default_swap)
