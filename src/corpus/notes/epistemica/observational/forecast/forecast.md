---
order: 0
tags: [note, forecast, prediction, calibration]
---

# Forecast

> A forecast is a claim about a value not yet observed, staked before the value is seen — and the practice is the machinery that makes the claim checkable rather than merely asserted.

A forecast binds four things at once: the **target value** (what is being claimed, in what units), the **time origin and horizon** (from when, to when), the **stated uncertainty** (a point, an interval, or a distribution), and the **scoring rule** (how the claim will be settled once the value is realised). Take one away and the claim stops being a forecast: a prediction with no horizon cannot be scored, a projection without a conditioning scenario is not a claim about the world, a scenario without a score is a story, and a point estimate with no uncertainty is a statement whose failure cannot be attributed to the part that was uncertain.

This directory holds the practices that produce such claims — the members are named below, and each becomes a note of its own as it is written.

## Members

- Point forecast — a single value per horizon, scored by error.
- Interval forecast — a central interval, scored by coverage and width.
- Density forecast — a full predictive distribution.
- Probabilistic and ensemble forecast — a distribution assembled from members or samples.
- Nowcasting — the value that is already happening but not yet reported.
- Judgmental forecast — structured expert elicitation, and its aggregation.
- Scenario forecast — a path conditioned on a stated set of assumptions.

## Evaluation

> A forecast is judged three ways, and the three are not substitutes. **Proper scoring rules** settle the claim — they reward the stated uncertainty rather than punishing it, and a forecaster cannot improve the score by lying about confidence. **Reliability** asks whether the events assigned probability $p$ occur at rate $p$. **Skill** asks whether the forecast beats a naive baseline, which is the only way to know the machinery earned its keep.

The calibration half of that judgement is not restated here: see [Calibration](/view.html?p=notes/epistemica/validation/calibration.md), which separates forecast calibration from parameter calibration and instrument calibration, and states why a calibrated forecast may still be useless.

## References

- [Calibration](/view.html?p=notes/epistemica/validation/calibration.md) · [Time Series](/view.html?p=notes/epistemica/observational/practice/time-series.md) · [Conformal Prediction and Inference](/view.html?p=notes/epistemica/observational/conformal-prediction-inference.md) · [Filter](/view.html?p=notes/epistemica/observational/filter/filter.md)
- Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association*, 102(477), 359–378. https://doi.org/10.1198/016214506000001437
