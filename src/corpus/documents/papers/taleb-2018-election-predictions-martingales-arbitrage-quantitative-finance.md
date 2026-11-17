---
tags: [document, probability, stochastic-process, forecasting]
qa:
 - Is the arbitrage price a better assessor than the forecaster — or does minimising the Brier score only reward the estimator that already behaves like a traded price?
 - If a forecast that never moves is indistinguishable from a martingale, what does that say about scoring rules that see only the final call?
---

# Taleb, N. N. (2018). Election predictions as martingales: An arbitrage approach. Quantitative Finance, 18(1), 1–5. https://doi.org/10.1080/14697688.2017.1395230

```bibtex
@article{taleb2018election,
  title={Election predictions as martingales: an arbitrage approach},
  author={Taleb, Nassim Nicholas},
  journal={Quantitative Finance},
  volume={18},
  number={1},
  pages={1--5},
  year={2018},
  doi={10.1080/14697688.2017.1395230},
  eprint={1703.06351},
  archivePrefix={arXiv},
  primaryClass={q-fin.PR}
}
```

## Notes

> Treat a continuously updated estimate of a binary election outcome as a price, and the no-arbitrage condition turns it into a martingale: the best forecast of the estimator's next value is its present value. From that one requirement the paper derives what a probability assessor is allowed to do.

The instrument is a binary option on the outcome. Pricing it by arbitrage — not by any particular model of the election — yields a valuation that minimises the Brier score, which is the paper's central identity: the proper scoring rule used to judge probability assessors and the no-arbitrage price of a binary are the same object read from two sides. The construction runs on a dual martingale $Y \in [L,H]$, obtained from an arithmetic Brownian motion $X$ on $(-\infty,\infty)$ and read as the number of votes needed for success, with the ratio of the estimator's volatility to that of the underlying variable carried through the valuation.

Two consequences follow, and they are the ones with teeth. When the outcome is very uncertain the arbitrage value migrates toward 50%, and — the operative point — the estimate **should not move much even when polls move a great deal**, since the polls are noise added to a martingale rather than information about it. And the arbitrage relations tie three quantities together: the binary value, the estimate of $Y$, and the volatility of the estimate over the time remaining. A forecaster whose numbers violate these is not merely inaccurate; the numbers are not prices of anything.

The empirical half is the 2016 US presidential cycle, where the forecasting groups are shown to have violated these relations, and where the deeper error is the one the paper names last: scoring only the final assessment. A martingale is judged along its whole path, so every intermediate estimate is part of the record. The final call is the least informative point on it.

## References

- [Taylor & Francis — the article](https://doi.org/10.1080/14697688.2017.1395230)
- [arXiv — 1703.06351](https://arxiv.org/abs/1703.06351)
- [Martingale](/view.html?p=notes/epistemica/observational/process/martingale.md) — the note that cites it
