---
tags: [property]
---

# Homoscedasticity


> **Homoscedasticity** is a **property** of a statistical system, particularly of the **error terms** (residuals) in a **regression model**.
> 

> A system is **homoscedastic** if the **variance of the error terms is constant** across all levels of the independent variable(s).
> 

Formally, in a regression model: $Y_i = \beta_0 + \beta_1 X_i + \varepsilon_i$

The **homoscedasticity assumption** means: $\operatorname{Var}(\varepsilon_i) = \sigma^2 \quad \text{for all } i$

## Heteroscedasticity

- **Homoscedasticity**: Constant variance of errors
- **Heteroscedasticity**: Variance of errors **changes** across observations (e.g., increases with XX)=

## Why It Matters

- **Ordinary Least Squares (OLS)** assumes homoscedasticity.
- If violated:
    - OLS estimates are still **unbiased**, but
    - Standard errors are **incorrect**, leading to **invalid confidence intervals and hypothesis tests**.

## Diagnostic Tools

- **Residual plots** (fitted values vs residuals)
- **Breusch–Pagan test**
- **White test**
- **Goldfeld–Quandt test**

## References

- https://en.wikipedia.org/wiki/Homoscedasticity_and_heteroscedasticity
