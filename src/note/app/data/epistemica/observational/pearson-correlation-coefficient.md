# Pearson Correlation Coefficient

 : Correlation (Correlation%2020cc0f5171ec8067ae1cf62c8673990e.md), Covariance (Covariance%201cfc0f5171ec80aead47fc52bbd5c430.md)

Let $X$ and $Y$be two random variables defined on the same probability space $(\Omega, \mathcal{F}, \mathbb{P})$, with finite second moments: $\mathbb{E}[X^2] < \infty, \quad \mathbb{E}[Y^2] < \infty$

The **Pearson correlation coefficient** $\rho_{X,Y}$ is defined as:

$\rho_{X,Y} = \frac{\mathrm{Cov}(X, Y)}{\sqrt{\mathrm{Var}(X) \cdot \mathrm{Var}(Y)}}
= \frac{\mathbb{E}[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \sigma_Y}$

where:

- $\mu_X = \mathbb{E}[X], μY=E[Y]\mu_Y = \mathbb{E}[Y]$
- $\sigma_X^2 = \mathrm{Var}(X) = \mathbb{E}[(X - \mu_X)^2]$
- $\sigma_Y^2 = \mathrm{Var}(Y) = \mathbb{E}[(Y - \mu_Y)^2]$
- $\mathrm{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)]$

## **Properties**

- $\rho_{X,Y} \in [-1, 1]$
- $\rho_{X,Y} = 1$: Perfect positive linear relationship.
- $\rho_{X,Y}$ $= -1$: Perfect negative linear relationship.
- $\rho_{X,Y} = 0$: No linear correlation (but not necessarily statistical independence).

## **Technical Distinctions**

- **Correlation vs. Covariance**: Covariance is scale-dependent; correlation is the normalized (unitless) version.
- **Correlation vs. Independence**: Zero correlation ($\rho = 0$) implies no *linear* association but does *not* imply independence unless $X$ and $Y$ are jointly Gaussian.

## Case Study

To **manually compute the Pearson correlation coefficient** between two variables $X$ and $Y$, you follow this formula:

$r = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2 \cdot \sum (Y_i - \bar{Y})^2}}$

Given two lists:

- $X = [2, 4, 6, 8]$
- $Y = [1, 3, 5, 7]$

### Step 1: Compute the means

$\bar{X} = \frac{2 + 4 + 6 + 8}{4} = 5 \quad \text{and} \quad \bar{Y} = \frac{1 + 3 + 5 + 7}{4} = 4$

### Step 2: Compute the numerator

$\sum (X_i - \bar{X})(Y_i - \bar{Y}) = (2 - 5)(1 - 4) + (4 - 5)(3 - 4) + (6 - 5)(5 - 4) + (8 - 5)(7 - 4)$

= $(-3)(-3) + (-1)(-1) + (1)(1) + (3)(3) = 9 + 1 + 1 + 9 = 20$

### Step 3: Compute the denominator

$\sqrt{\sum (X_i - \bar{X})^2 \cdot \sum (Y_i - \bar{Y})^2}$

- $\sum (X_i - \bar{X})^2 = (-3)^2 + (-1)^2 + 1^2 + 3^2 = 9 + 1 + 1 + 9 = 20$
- $\sum (Y_i - \bar{Y})^2 = (-3)^2 + (-1)^2 + 1^2 + 3^2 = 9 + 1 + 1 + 9 = 20$

### Step 4: Final Pearson correlation

$r = \frac{20}{20} = 1.0$

## References

- https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
