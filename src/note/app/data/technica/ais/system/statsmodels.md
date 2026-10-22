---
tags: [tool]
---

# Statsmodels


> 

## Core Abstractions

Here’s a table summarizing the core abstractions in `statsmodels`, a Python library for statistical modeling:

| **Abstraction** | **Description** | **Example Usage** | **Key Features** |
| --- | --- | --- | --- |
| **`OLS`** | Ordinary Least Squares regression model for linear relationships between variables. | `sm.OLS(y, X).fit()` | Provides estimates, diagnostics, and predictions for linear regression models |
| **`Logit`** | Logistic regression model for binary outcome variables. | `sm.Logit(y, X).fit()` | Used for modeling binary outcome data and provides odds ratios |
| **`Probit`** | Probit regression model for binary outcome variables, using a cumulative normal distribution. | `sm.Probit(y, X).fit()` | Similar to Logit but based on a different link function |
| **`GLM`** | Generalized Linear Model framework that allows for specifying different distributions and link functions. | `sm.GLM(y, X, family=sm.families.Gaussian()).fit()` | Flexible framework for various types of regression models |
| **`MixedLM`** | Linear Mixed Effects Model for data with hierarchical or grouped structures. | `sm.MixedLM(y, X, groups=group_var).fit()` | Handles data with both fixed and random effects |
| **`TimeSeries`** | Tools for analyzing time series data, including models for autoregressive and moving average processes. | `sm.tsa.ARIMA(y, order=(p,d,q)).fit()` | Includes models for forecasting and seasonal adjustments |
| **`DescriptiveStats`** | Functions for summarizing and describing data, such as mean, variance, and percentiles. | `sm.descr.describe(data)` | Provides descriptive statistics for exploratory data analysis |
| **`Anova`** | Analysis of Variance (ANOVA) models for comparing means across groups. | `sm.stats.anova_lm(model, typ=2)` | Tests differences between group means and provides statistical significance |
| **`Robust`** | Methods for estimating models with robust standard errors to handle heteroscedasticity and outliers. | `sm.RLM(y, X).fit()` | Provides robust regression estimates with standard error adjustments |

## References

- https://www.statsmodels.org/stable/index.html
- https://github.com/statsmodels/statsmodels/
- [Statistics](https://app.notion.com/p/Statistics-c9d6a53f36a8494eae934a1a14f969da?pvs=21)
