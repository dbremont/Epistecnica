---
tags: [note, finance, fixed-income, modelling, technical-practice]
qa:
 - Is fixed-income modelling a practice or a set of models — and does the answer change how it is validated?
 - Why can the same bond carry a different value in two models that both fit the market?
 - Where does the technical operation end and the epistemic model begin?
---

# Fixed-Income Modelling

> **Fixed-income modelling** is the practice that turns a debt contract into a priced, measured and stressed position: it lays out the contractual cash flows, discounts them through a yield or a curve, carries the market state the value depends on, measures the sensitivity of the price to that state, and aggregates the position into a portfolio and a risk distribution.

> It is a **mixed** object, and the mix is the point. The *practice* is technical — a repeatable sequence of operations that transforms a contract into a number. The *models* it runs are epistemic: a Nelson–Siegel curve, a Vasicek short rate, a reduced-form default intensity are constructions fitted to data, warranted by calibration and out-of-sample behaviour, not by the transformation they perform. The note keeps the two apart because they fail differently: a practice fails by being wrong about the operation, a model fails by being wrong about the world.

## Formulation

### What technical element type does this technical instance belong to?

**Fixed-income modelling belongs to the `Technical Practice` technical element type — a repeatable, organized pattern of technical work integrating tasks, techniques, models, standards and evaluations.**

It is a practice because it is a standing way of working — schedule, discount, curve, measure, aggregate, stress — not a single model or a single calculation. It is readable as a `Technical Element Set` because the layers it runs are different technical and epistemic element types held together by one purpose: a valued position.

The boundary against the **asset** is the object: [Bond](/view.html?p=notes/technica/production/industry/finance/asset/bond.md) is the contract; this note is the work done on it. The boundary against the **epistemic model** is the warrant: a term-structure model is an inquiry artefact (a fit, a calibration), while the practice is the sequence that chooses it, feeds it and reads it.

### What is this technical instance?

> An analyst, a pricing library and a risk engine working one security from the indenture to the report: reading the cash-flow terms, building the schedule, discounting at a curve, computing the yield and the sensitivities, deciding which model applies to the option or the credit, aggregating the position, and producing the stress and VaR that the desk and the regulator consume.

### What are the layers of this technical instance?

> The modelling stack is a chain of dependencies, not a list of alternatives. Each layer consumes what the layer below produces, and each adds one state variable or one friction.

| Group | Layers | What the group fixes |
| --- | --- | --- |
| **Instrument** | cash flow, pricing, embedded option, prepayment | What the contract pays and when, and what it is worth |
| **Market** | yield, term structure, interest-rate dynamics, spread, liquidity | The coordinates and the state variables the value depends on |
| **Price behaviour** | duration, convexity | How the price responds to those variables |
| **Credit** | credit and spread models | The default and the compensation for it |
| **Portfolio and risk** | portfolio, risk, valuation under uncertainty | The aggregate exposure and its distribution |

### The layers

**Instrument**

| Layer | Kind | What is modelled | Typical models |
| --- | --- | --- | --- |
| **Cash-flow model** | Technical operation | Coupons, principal, maturity, amortisation, day-count and payment dates | Bond cash-flow schedule; amortisation and sinking-fund schedules |
| **Pricing model** | Technical operation | Present value / fair value | Discounted cash flow; clean and dirty price with accrued interest |
| **Yield model** | Technical operation | Yield-to-maturity, spot rates, forward rates | YTM; bootstrapped spot and forward curves |
| **Embedded-option model** | Mixed — practice over an epistemic model | Callable, putable and convertible features | Binomial and trinomial trees, Hull–White trees, Monte Carlo with OAS |
| **Prepayment model** | Mixed — practice over an epistemic model | Early repayment of mortgage-backed and consumer debt | CPR/CDR, PSA, econometric prepayment models |

**Market**

| Layer | Kind | What is modelled | Typical models |
| --- | --- | --- | --- |
| **Term-structure model** | Epistemic model | The evolution of rates across maturities | Nelson–Siegel, Svensson, spline fits, bootstrapping |
| **Interest-rate dynamics** | Epistemic model | How rates change over time | Vasicek, CIR, Hull–White, HJM, LIBOR market model |
| **Credit model** | Epistemic model | Default probability and credit spread | Reduced-form intensity (Jarrow–Turnbull), structural (Merton, Black–Cox) |
| **Spread model** | Epistemic model | Corporate and sovereign spread behaviour | Spread curves, hazard-rate models, z-spread and OAS, CDS basis |
| **Liquidity model** | Mixed | Ability and cost to sell the security | Bid–ask spread, market-impact models, liquidity premium |

**Price behaviour, portfolio and risk**

| Layer | Kind | What is modelled | Typical models |
| --- | --- | --- | --- |
| **Bond-price dynamics** | Technical operation | Price sensitivity to rates | Macaulay and modified duration, convexity, DV01, key-rate durations |
| **Portfolio model** | Technical operation | Aggregate fixed-income exposure | Factor models, duration matching, immunisation, optimisation |
| **Risk model** | Mixed — practice over simulation | VaR, stress, duration and spread risk | Scenario analysis, historical and Monte Carlo VaR, CS01 |
| **Valuation under uncertainty** | Epistemic model, executed as a practice | Future rate and credit scenarios | Monte Carlo simulation, scenario generation, path-dependent pricing |

## The stack

> The chain runs from the contract to the distribution, and the dependency is strict:
>
> $$\text{cash flows} \;\to\; \text{price} \;\to\; \text{yield and curve} \;\to\; \text{dynamics} \;\to\; \text{credit and liquidity} \;\to\; \text{portfolio and risk}.$$
>
> A term-structure model is worthless without a cash-flow schedule; a duration is meaningless without a pricing function; a VaR number is a number about the models underneath it, not about the bond. When a valuation disagrees with the market, the error is located by walking the chain *downward* — first the cash flows, then the curve, then the model — because the upper layers cannot be more reliable than the lower ones.

## The epistemic side

> The models are where the practice meets inquiry, and the corpus files that half under [Epistemic Model](/view.html?p=notes/epistemica/meta/theory/model.md), [Calibration](/view.html?p=notes/epistemica/validation/calibration.md), [Identification](/view.html?p=notes/epistemica/meta/theory/identification.md) and [Validation](/view.html?p=notes/epistemica/validation/validation.md). Three consequences follow, and they are what the mixed note exists to state.
>
> - **A fitted curve is not a fact.** Nelson–Siegel and Svensson are parametric fits; two of them can pass through the same quotes and disagree about the ten-year forward. The choice is an epistemic decision that the practice must record.
> - **A short-rate model is a choice of dynamics.** Vasicek admits negative rates and a constant volatility; CIR keeps rates positive at the cost of a square-root diffusion; Hull–White adds time-dependent parameters to fit the initial curve. The practice selects the dynamics; the model's warrant is the fit and the prices it reproduces.
> - **Credit is the least observable layer.** A default intensity is inferred from spreads, ratings and history, and the spread itself contains liquidity and risk premia. That is why the credit layer is where model risk is largest and where the note marks the boundary most carefully.

## References

- [Finance Sector](/view.html?p=notes/technica/production/industry/finance/readme.md) — the industry shelf this note belongs to
- [Bond](/view.html?p=notes/technica/production/industry/finance/asset/bond.md) — the instrument the practice models
- [Firm Finance](/view.html?p=notes/technica/production/firm/toolkit/finance/readme.md) — the firm-side capital and cost-of-capital reading
- [Halperin (2026) — Three Matrices](/view.html?p=documents/papers/halperin-2026-three-matrices-observable-matrix-dynamics-portfolio-optimization-arxiv.md) — a price-dynamics and portfolio model that deliberately bypasses this stack
- [Epistemic Model](/view.html?p=notes/epistemica/meta/theory/model.md) · [Calibration](/view.html?p=notes/epistemica/validation/calibration.md) · [Validation](/view.html?p=notes/epistemica/validation/validation.md) — the epistemic half
- Fabozzi, F. J. (2013). *Bond markets, analysis, and strategies* (8th ed.). Pearson. — the practice as a stack of layers
- Brigo, D., & Mercurio, F. (2006). *Interest rate models — theory and practice* (2nd ed.). Springer. — the term-structure and short-rate models
- Hull, J. C. (2018). *Options, futures, and other derivatives* (10th ed.). Pearson. — duration, convexity, trees and Monte Carlo
