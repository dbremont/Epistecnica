---
tags: [note, social, social-element, money-market, finance, market-instance, liquidity]
qa:
 - A money market is a market whose product is liquidity and whose price is a rate. Does that make it a market at all, or a utility that markets depend on?
 - The 2008 freeze happened in the one market whose instruments were supposed to be as good as cash. Which assumption failed — the credit risk, the liquidity, or the belief that both could be priced?
 - LIBOR was a survey, and a survey can be a cartel. Now that the benchmarks are transaction-based, what was actually fixed — the manipulation, or the visibility of it?
---

# Money Market

> The **money market** is the wholesale market for short-term debt — instruments of a year or less, issued by governments, banks and large firms, and held by whoever needs a place to park cash without giving up access to it. Its product is **liquidity**: the ability to hold a claim and turn it into money at short notice with little loss.

> Its price is not a quoted amount but a **rate**, which makes it the hinge between the monetary system and the financial system: the central bank sets a policy rate, the money market is where that rate becomes everyone else's funding cost, and when the market stops working the transmission stops with it.

## Instruments

| **Instrument** | **Issuer** | **What it is** |
| --- | --- | --- |
| **Treasury bills** | Government | Short-dated sovereign debt; the benchmark risk-free short rate |
| **Commercial paper** | Large firms | Unsecured short-term borrowing, often to fund working capital |
| **Certificates of deposit** | Banks | Term deposits that can be traded, so the depositor keeps a claim and the bank keeps funding |
| **Repurchase agreements (repo)** | Banks, dealers, funds | A sale with a promise to buy back: collateralised lending, and the market's plumbing |
| **Interbank lending** | Banks | Unsecured lending between banks overnight or for short terms |
| **Bankers' acceptances** | Firms, guaranteed by banks | A bank's promise to pay, used to finance trade |
| **Money market funds** | Investors pooled | Funds that hold the instruments above and offer near-money claims to their holders |

## What distinguishes it

Four features separate it from the capital market next door, and each is a source of both strength and fragility:

- **Short maturity.** The claim matures soon, so its price is insensitive to long-term interest rates — and its holder must roll it over, which is exactly the moment a lender can refuse.
- **Wholesale size.** Participants are institutions, not households, so the market reprices on information faster than retail markets do.
- **Low credit risk, by design.** The instruments are meant to be near-money, which is why a single doubt about a large issuer can stop the whole market rather than reprice it.
- **Collateral.** Much of the market is secured (repo), which makes it safe in normal times and makes collateral quality the variable that matters in a crisis.

## The functions

| **Function** | **Who relies on it** |
| --- | --- |
| **Liquidity management** | Banks and corporates park cash for days or weeks without leaving the financial system |
| **Funding** | Banks fund their balance sheets; firms fund working capital |
| **Policy transmission** | The central bank's rate reaches the economy through this market first: policy rate → interbank and repo rates → lending and deposit rates |
| **Benchmarking** | Short-term rates price everything from floating-rate loans to derivatives |
| **Cash-collateral transformation** | Repo turns securities into money and back, which is how dealers finance inventories |

## The pathologies

- **The run that was not a run.** In 2007–08 the money market froze: holders of commercial paper and repo refused to roll, not because the issuers were insolvent but because the collateral's value could not be established. A market built on the assumption that its instruments are as good as cash discovered that the assumption was the collateral.
- **Benchmark manipulation.** LIBOR was compiled from *submitted* estimates rather than transactions, which made it both gameable and unverifiable. The scandal's lesson is structural: a benchmark that is not derived from trades is an honour system with a number attached. The replacement benchmarks — SOFR, €STR and the rest — are transaction-based, which removes the discretion and leaves the question of whether the underlying market is deep enough to bear the weight.
- **The fund that breaks the buck.** A money market fund offering a stable value against assets that can fall is a promise the assets do not support; the run happens when the promise is doubted, not when it is broken.
- **The shadow boundary.** Anything that functions as money but sits outside the regulated money market — unsecured dealer funding, off-balance conduits — reappears precisely when the regulated market tightens, which is why the boundary has to be redrawn after every crisis.

## Relation

| **Concept** | **Relation** |
| --- | --- |
| [Financial Market](/view.html?p=notes/social/coordinator/market/instance/finantial/financial-market.md) | The parent instance family: capital markets hold long claims, this one holds short ones |
| [Stock](/view.html?p=notes/social/coordinator/market/instance/finantial/stock.md) | The equity counterpart, priced by continuous auction rather than by a rate |
| [Market](/view.html?p=notes/social/coordinator/market/market.md) | The arena; this is the short-term debt instance |
| [Interest Rate](/view.html?p=notes/social/coordinator/money/interest-rate.md) | The price by which everything here is quoted |
| [Monetary System](/view.html?p=notes/social/coordinator/money/monetary-system.md) | The system whose policy rate this market transmits |
| [Money](/view.html?p=notes/social/coordinator/money/money.md) | What the instruments are near-substitutes for, and why the market exists |

## References

- Gorton, G. B. (2010). *Slapped by the invisible hand: The panic of 2007*. Oxford University Press. — the repo market as the place where the crisis actually happened
- Mehrling, P. (2011). *The new Lombard Street: How the Fed became the dealer of last resort*. Princeton University Press. — the money market as the system's liquidity plumbing
- Gorton, G., & Metrick, A. (2012). Securitized banking and the run on repo. *Journal of Financial Economics*, 104(3), 425–451. — the run, measured
- Cecchetti, S. G., & Schoenholtz, K. L. (2020). *Money, banking, and financial markets* (6th ed.). McGraw-Hill. — the instruments and participants, described as a system
- [Money market](https://en.wikipedia.org/wiki/Money_market)
- [Financial Market](/view.html?p=notes/social/coordinator/market/instance/finantial/financial-market.md) — the parent family
- [Interest Rate](/view.html?p=notes/social/coordinator/money/interest-rate.md) — the rate that prices every instrument here
