---
tags: [note, social, social-element, interest-rate, money, monetary, price]
qa:
 - A rate is not a price: it needs a base, a period and a risk to mean anything. How much of what is called "the interest rate" is a number with those three things left implicit?
 - The components of a rate — real return, expected inflation, credit risk, maturity — are inferred, never observed. Which inference carries the most weight, and what happens when it is wrong?
 - In a managed system the policy rate is an administered number, not a market price. Does calling it a price make the administration invisible, or does it make it legible?
---

# Interest Rate

> The **interest rate** is the price of money over time: what a borrower pays for the use of funds, expressed as a proportion of the principal per period. It is the price that lets every future value be compared with a present one, which is why it is the single most consequential number in a financial system — and why its composition is disputed more than its level.

> It is not one rate. A policy rate set by a central bank, an interbank rate, a mortgage rate and a ten-year bond yield are all "the interest rate" in ordinary speech and none of them is the same object: each has a different base, a different period, a different credit and a different maturity.

## Composition

| **Component** | **What it pays for** | **How it is known** |
| --- | --- | --- |
| **Real return** | The lender's compensation for giving up consumption now | Inferred, never observed directly |
| **Expected inflation** | Protection of the principal's purchasing power | Measured by surveys or by the spread to inflation-linked bonds — both imperfect |
| **Credit risk** | The chance the borrower does not pay | Priced by the spread over a risk-free benchmark of the same maturity |
| **Maturity premium** | The cost of tying money up for longer | Estimated from the shape of the yield curve |
| **Liquidity premium** | The cost of holding something less tradable than cash | Visible only when liquidity disappears |

The decomposition is the Fisher relation with the frictions added: a **nominal** rate is a **real** rate plus expected inflation, plus the risk and maturity premia. The identity is exact; the components are estimates, which is why two economists can agree on the rate and disagree on everything it means.

## The family

| **Rate** | **Who sets it** | **What it prices** |
| --- | --- | --- |
| **Policy rate** | The central bank, administratively | The price of central-bank liquidity, and the anchor for the rest |
| **Interbank / money market rate** | The market, within the policy corridor | Unsecured and secured short-term funding between banks |
| **Lending and deposit rates** | Banks, constrained by competition and regulation | Credit to households and firms, and the return to savers |
| **Bond yield** | The market | The price of long-term government and corporate debt |
| **Real rate** | Nobody directly | The nominal rate net of inflation — the one that matters for investment decisions |

From the family's shape comes the **yield curve**: the set of yields across maturities for the same issuer. Its level says what the market thinks funding costs now; its slope is read as an expectation of future rates and growth, a term premium, or both — three readings that fit the same curve, which is why the curve is more often interpreted than understood.

## What it does

- **Discounts the future.** Every valuation — a project, a bond, a firm, a forest — is a set of future flows divided by rates. Change the rate and you change which projects exist.
- **Allocates capital over time.** A higher rate moves consumption earlier and investment later, which is the classical account, and the account that organised monetary policy for a century.
- **Rations credit.** Where the rate is capped or administered, credit is allocated by quantity, queue or favour instead — the mechanism that makes interest-rate ceilings produce rationing rather than cheapness.
- **Transmits policy.** The central bank's instrument is this market price, and the transmission runs from the policy rate through the curve to lending and asset prices.
- **Becomes an instrument of the state.** In a directed-credit system the rate is set to favour a sector — subsidised lending, policy banks, preferential rediscount — which is where this note meets [Investment](/view.html?p=notes/social/koinomia/action/domain/finance/investment.md).

## The disputes

- **Is it a price or an administered number?** Market-clearing in the textbook, set by a committee in practice. The honest statement is that the short end is administered and the long end is market-determined, and that the boundary is a policy choice.
- **Negative real rates.** A sustained negative real rate is a transfer from creditors to debtors, and it is normally hidden by the nominal rate being positive. It is also, in a high-debt system, a way of managing the debt — see the corpus's open question on [debt in the national currency](qa-00012).
- **The natural rate.** The rate at which saving and investment balance with stable inflation is inferred, contested, and load-bearing for policy; nobody observes it, and everyone acts as if it were known.
- **Usury limits and caps.** A cap is a distributional decision made in the language of morality: it lowers the price for those who still get credit and excludes the rest, and that exclusion is the cost rarely counted.

## Relation

| **Concept** | **Relation** |
| --- | --- |
| [Money](/view.html?p=notes/social/coordinator/money/money.md) | What the rate is the price of — over time, and across risk |
| [Monetary System](/view.html?p=notes/social/coordinator/money/monetary-system.md) | The system whose policy rate anchors the family |
| [Money Market](/view.html?p=notes/social/coordinator/market/instance/finantial/money-market.md) | The market where the short rates are actually made |
| [Price](/view.html?p=notes/social/coordinator/price-asset/price.md) | The general concept a rate is the temporal form of |
| [Return](/view.html?p=notes/social/relation/economic/return.md) | The realised counterpart: what the rate promised versus what was earned |
| [Investment](/view.html?p=notes/social/koinomia/action/domain/finance/investment.md) | Where the rate becomes an instrument rather than a price |

## References

- Wicksell, K. (1898). *Geldzins und Güterpreise* [Interest and prices]. — the natural rate against the market rate, the distinction everything later inherits
- Fisher, I. (1930). *The theory of interest*. Macmillan. — the nominal/real decomposition, stated as an identity
- Keynes, J. M. (1936). *The general theory of employment, interest and money*. Macmillan. — liquidity preference: the rate as a monetary, not a real, phenomenon
- Tobin, J. (1969). A general equilibrium approach to monetary theory. *Journal of Money, Credit and Banking*, 1(1), 15–29. — the portfolio view, where assets are chosen by risk and return together
- Campbell, J. Y. (1995). Some lessons from the yield curve. *Journal of Economic Perspectives*, 9(3), 129–152. — what the curve does and does not forecast
- Taylor, J. B. (1993). Discretion versus policy rules in practice. *Carnegie-Rochester Conference Series on Public Policy*, 39, 195–214. — the policy rate as a rule rather than a discretion
- Mishkin, F. S. (2019). *The economics of money, banking, and financial markets* (12th ed.). Pearson. — the textbook account of the family and the transmission
- [Interest rate](https://en.wikipedia.org/wiki/Interest_rate)
- [Money](/view.html?p=notes/social/coordinator/money/money.md) · [Monetary System](/view.html?p=notes/social/coordinator/money/monetary-system.md) — what the rate is the price of
- [Money Market](/view.html?p=notes/social/coordinator/market/instance/finantial/money-market.md) — where short rates are made
