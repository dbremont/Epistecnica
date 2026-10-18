---
tags: [distribution, probability, technique]
---

# Resampling

 : (Statistic) Estimator ((Statistic)%20Estimator%2010fc0f5171ec8015accadab377f913a5.md), Sampling (Sampling%207010404f3cb34b5890130653fc607f65.md)

> **Resampling Techniques:** Bootstrapping and permutation tests estimate sampling distributions and conduct hypothesis testing without strict parametric assumptions.
> 

## Method

| **Method** | **Type** | **Description** | **Use Cases** |
| --- | --- | --- | --- |
| **Bootstrap** | Resampling (Non-Parametric) | Resample with replacement and compute estimator on each resample. | Confidence intervals, bias/variance estimation. |
| **Jackknife** | Resampling (Non-Parametric) | Leave-one-out resampling to estimate variance and bias. | Small sample sizes, bias correction. |
| **Permutation Test** | Resampling (Non-Parametric) | Randomly shuffles data labels to generate the null distribution. | Hypothesis testing, robustness analysis. |
| **Central Limit Theorem (CLT)** | Analytical (Parametric) | Approximates estimator’s distribution as normal for large samples. | Mean estimation, confidence intervals. |
| **Delta Method** | Analytical (Parametric) | Uses Taylor series to approximate variance of a function of an estimator. | Asymptotic variance estimation. |
| **Moment Matching** | Analytical (Parametric) | Matches the first few moments (mean, variance, etc.) to fit a distribution. | Parametric density estimation. |
| **Bayesian Posterior Simulation** | Bayesian | Uses Bayesian inference to estimate a posterior distribution. | Probabilistic inference, small data. |
| **Markov Chain Monte Carlo (MCMC)** | Bayesian | Samples from a Bayesian posterior to approximate an estimator’s distribution. | Bayesian parameter estimation. |
| **Monte Carlo Simulation** | Simulation | Generates random samples from a known model to approximate an estimator’s distribution. | Risk analysis, complex distributions. |
| **Parametric Bootstrap** | Simulation | Simulates data from a parametric model and applies bootstrap resampling. | Model-based inference. |

## References

- https://en.wikipedia.org/wiki/Resampling_(statistics)
