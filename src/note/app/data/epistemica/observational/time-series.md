---
tags: [learning-system]
---

# Time Series


> “Time series” is a bad name for the interfacial analysis of a dynamical system indexed by time.
> 

## Limits

> What are the limits of the time series modeling approach? What are the limits in capturing the dynamics and changes in the dynamics in general?
> 

> Modeling is fundamentally about capturing dynamics—including, in some sense, meta-dynamics—but it **cannot perceive future dynamic regimes beyond historical precedent**. Its predictive power is bounded by what has been observed and by the assumption that patterns continue to hold.
> 

| Limit Type | Limit | Description | Instance |
| --- | --- | --- | --- |
| Information-Theoretic | Finite information in the past | Forecasting cannot extract information not present in the historical data. | Policy shocks or technological discontinuities absent in the series |
| Information-Theoretic | Entropy / irreducible uncertainty | High randomness or near-random processes make long-term predictions unreliable. | Random walk time series; white noise |
| Dynamical Systems | Chaos / sensitivity to initial conditions | Deterministic systems may still be unpredictable due to exponential error growth. | Financial markets; weather-like economic systems |
| Dynamical Systems | Non-stationarity / regime shifts | Structural breaks and changing parameters limit forecast validity. | Economic crises; policy regime changes |
| Statistical | Bias–variance tradeoff | Complex models may overfit finite data, degrading out-of-sample forecasts. | Over-parameterized ARIMA or neural models on short series |
| Statistical | Small-sample limits | Low effective sample size reduces reliability of parameter estimation. | Short historical series with strong autocorrelation |
| Horizon-Dependent | Short-term vs long-term decay | Forecast skill diminishes as horizon increases; long-term forecasts converge to assumptions. | Medium-term sales forecasting; climate projections |
| Causal | Lack of causality | Pure time series models capture correlation, not causal effects; counterfactuals are unreliable. | Policy evaluation based only on past GDP |
| Computational / Representational | Model class mismatch | Models cannot represent all possible dynamics; assumptions may fail. | Linear models missing nonlinear effects; neural networks extrapolating poorly |
| Computational / Representational | Extrapolation failure | Models assume future resembles past; innovation or crises break assumptions. | Market shocks; sudden technological disruption |
| Reflexivity / Social | Feedback and adaptation | Forecasts can influence the system, creating endogenous non-stationarity. | Central bank forecasts affecting market behavior |

## QA

### How to reason and evaluate the used of Time Series Model for Consumer Demand?

> 

## References

- [Introduction to Dynamic Linear Models for Time Series Analysis](https://arxiv.org/abs/1903.11309#:~:text=Dynamic%20linear%20models%20(DLM)%20offer,coefficients%20can%20vary%20in%20time.)
- [Dynamical System](../mathematical/dynamical-system.md)
