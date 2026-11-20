---
tags: [document, portfolio-management, quantitative-finance, markov-chain, optimization]
---

# Halperin, I. (2026). Are Three Matrices All You Need To Beat the Market? Observable Matrix Dynamics for Portfolio Optimization. arXiv:2607.27461v1 [q-fin.PM]. https://doi.org/10.48550/arXiv.2607.27461

```python
@article{halperin2026three,
  title = {Are Three Matrices All You Need To Beat the Market? Observable Matrix Dynamics for Portfolio Optimization},
  author = {Halperin, Igor},
  journal = {arXiv preprint arXiv:2607.27461},
  year = {2026},
  eprint = {2607.27461},
  archivePrefix = {arXiv},
  primaryClass = {q-fin.PM},
  doi = {10.48550/arXiv.2607.27461},
}
```

## Notes

The paper proposes a dynamic portfolio method whose entire state is **three fixed-size matrices** built from daily prices, trading volumes and market capitalisations:

1. the **distance matrix** of return correlations across the S&P 500 names;
2. the **transition matrix of a Markov chain that ranks names monthly by trailing return**;
3. the **transition matrix of a Markov chain that ranks names monthly by trailing volatility**.

That state replaces the two objects Markowitz mean-variance optimisation is built on — the expected-return vector and the covariance matrix. The claimed consequences are practical: no matrix inversion is required, the method operates on **cross-sectional ranks** rather than raw moments (so outliers and heavy tails are handled by construction), and it is dynamic rather than single-period.

**The empirical core.** The paper is explicit that the two ranks are not equally forecastable. The **volatility rank is forecastable one step ahead**; the **return rank stays close to unforecastable**. That asymmetry is the honest finding, and the strategy is built around it rather than against it: the forecastable volatility rank carries the risk model, and the return rank contributes little beyond a weak momentum signal.

**The portfolio.** A market-neutral momentum long-short sleeve is blended with an opportunistic long-only sleeve. Two refinements are reported:

- **diversifying the long sleeve by residual distance** — names far apart in the residual correlation geometry are preferred — which raises the reported Sharpe and the annualised return on both test sets;
- a **convex information-leader overlay** that insures the market-neutral sleeve: it buys convexity and a shallower drawdown at a small cost in return, with the Sharpe unchanged.

**The reported results.** Two non-overlapping out-of-sample windows: January 2022 – December 2024, and January 2025 – July 2026. Net of a five-basis-point trading cost and marked to market daily, the reported Sharpe is **1.06** against the market's **0.78** in the first window and **1.32** against **1.14** in the second. The method is also reported to outperform the classical **minimum-variance** and **maximum-diversification** portfolios. The residual-distance diversification lifts the Sharpe to **1.08** and **1.44** and the annualised return from **18 % to 20 %** and from **44 % to 56 %** respectively.

**What to keep in mind.** The results are a backtest over two relatively short windows on a single equity universe, reported by a single author, with the trading-cost and market-impact assumptions stated but necessarily simplified. The windows overlap the recent momentum regime, and the long-only sleeve's 44–56 % annualised return in the second window is a high-volatility figure that should be read against its drawdown, not only its Sharpe. The paper's most transferable claim is also its most modest: the volatility rank is predictable, the return rank is not, and a portfolio can be built on the first without pretending the second is known.

## References

- [arXiv:2607.27461v1](https://arxiv.org/abs/2607.27461v1) — abstract, PDF and HTML
- https://doi.org/10.48550/arXiv.2607.27461
- [Finance Industry](/view.html?p=notes/technica/production/industry/finance/readme.md) — the industry the method trades in
- [Finance Toolkit](/view.html?p=notes/technica/business/toolkit/finance/readme.md) — the firm-side practice
- [Quantitative Trading](/view.html?p=notes/technica/business/toolkit/trading/quantitative-trading-qt.md) — the practice the backtest belongs to
- [Share](/view.html?p=notes/technica/production/industry/finance/asset/share.md) — the instrument the portfolio holds
- [Financial](/view.html?p=notes/miscellanea/discipline/financial.md) — the discipline
