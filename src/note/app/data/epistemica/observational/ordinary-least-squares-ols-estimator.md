---
tags: [estimator, probability]
---

# Ordinary Least Squares (OLS) Estimator


> The standard method for estimating $\beta$ is the **Ordinary Least Squares (OLS)** estimator, obtained by minimizing the residual sum of squares (RSS): $\hat{\beta}_{\text{OLS}} = \arg \min_{\beta \in \mathbb{R}^p} \| Y - X\beta \|_2^2$.
> 

> Assuming $X \in \mathbb{R}^{n \times p}$ has full column rank, the closed-form solution is: $\hat{\beta}_{\text{OLS}} = (X^T X)^{-1} X^T Y$
> 

## Breviary

> 

| **Attribute** | **Details** |
| --- | --- |
| **Estimator Name** | Ordinary Least Squares (OLS) |
| **Goal** | Minimize the **Mean Squared Error (MSE)** between predicted and observed values |
| **Model Assumed** | Linear regression model:  $y = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\varepsilon}$ |
| **Estimator Formula** | $\boldsymbol{\hat{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}$ |
| **Loss Function Minimized** | Mean Squared Error (MSE):  $\mathcal{L}(\boldsymbol{\beta}) = \frac{1}{n} | \mathbf{y} - \mathbf{X}\boldsymbol{\beta} |^2$ |
| **Update Rule Type** | Closed-form (non-iterative) solution |
| **Interpretability** | High — coefficients directly quantify the marginal effect of predictors |
| **Computational Complexity** | $O(n d^2 + d^3)$ for $n$ samples and $d$ features (due to matrix inversion) |
| **Main Advantages** | Simple, efficient for small to moderate datasets, interpretable coefficients |
| **Main Limitations** | Not suitable with multicollinearity, nonlinearity, or heteroscedasticity |
| **Statistical Assumptions** | See Below. |
| **When Inference is Valid** | When all assumptions are satisfied, especially normality of residuals |

## Property

- **Linearity in parameters**: Model is linear in $\beta$, not necessarily in $X$.
- **BLUE Property**: Under Gauss–Markov assumptions (linearity, full rank, exogeneity, homoskedasticity, no autocorrelation), OLS is the **Best Linear Unbiased Estimator**.
- **Projection Interpretation**: OLS projects $Y$ orthogonally onto the column space of $X$.
- **Statistical Inference**: Under normality of $\varepsilon$, hypothesis testing and confidence intervals for $\beta$ are tractable via t-distribution and F-statistics.

## Assumption

> What are the assumptions imposed by the estimator on the data? In other words, what conditions must the data meet for the estimator to be validly applied?
> 

- Linearity: Relationship between predictors and outcome is linear.
- Independence: Observations are independent.
- Homoscedasticity: Constant variance of errors.
- No multicollinearity: Predictors are not linearly dependent.
- Exogeneity: Predictors are uncorrelated with the error term.
- Normality of errors (for inference): Errors are normally distributed.
- Fixed design matrix: In classical regression, XX is fixed, not random.
- No measurement error in predictors: Predictors are measured without noise.

## Proof

Objective Function (**Residual Sum of Squares**)

$S(\boldsymbol{\beta}) = (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^T (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})$

$= \mathbf{y}^T\mathbf{y} - 2\boldsymbol{\beta}^T \mathbf{X}^T\mathbf{y} + \boldsymbol{\beta}^T\mathbf{X}^T\mathbf{X} \boldsymbol{\beta}$

Take Gradient w.r.t. $\boldsymbol{\beta}$

$\nabla_{\boldsymbol{\beta}} S(\boldsymbol{\beta}) = -2 \mathbf{X}^T \mathbf{y} + 2 \mathbf{X}^T \mathbf{X} \boldsymbol{\beta}$

Set the gradient to zero: $\mathbf{X}^T \mathbf{X} \boldsymbol{\beta} = \mathbf{X}^T \mathbf{y}$

Solve for $\boldsymbol{\beta}$

$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ This is the **OLS estimator**.

### Gauss–Markov Theorem

> The Gauss–Markov Theorem states that, under a specific set of assumptions, the OLS estimator is the **Best Linear Unbiased Estimator (BLUE)** — that is, it has the minimum variance among all linear and unbiased estimators.
> 

## References

- https://en.wikipedia.org/wiki/Proofs_involving_ordinary_least_squares
- https://en.wikipedia.org/wiki/Least_squares
- [(Statistic) Estimator](statistic-estimator.md)
- [Theory of Statistics](theory-of-statistics.md)
- [Theory of Probability](theory-of-probability.md)
- https://en.wikipedia.org/wiki/Least_squares
- https://en.wikipedia.org/wiki/Polynomial_regression
- https://en.wikipedia.org/wiki/Ordinary_least_squares
- https://en.wikipedia.org/wiki/Gauss–Markov_theorem
