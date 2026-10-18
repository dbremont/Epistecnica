---
tags: [statistic]
---

# Correlation

 : Pearson Correlation Coefficient (Pearson%20Correlation%20Coefficient%2020dc0f5171ec8057a1e1d8368df4fffe.md), Regression (Regression%20175c0f5171ec80ba9eb2d67dd7339800.md)

> **Correlation** refers to the *statistical dependency* or *degree of linear association* between two random variables.
> 

> **Correlation**: A measure of the strength and direction of the relationship between two variables, often represented by Pearson's correlation coefficient (r).
> 

> **Autocorrelation:** The degree of correlation between the values of the process at different times.
> 

> Note: Take two variables;  the correlation will not be cero.
> 

## Formulation

| **Type** | **Formula** | **Description** |
| --- | --- | --- |
| **Pearson correlation coefficient** | $\rho_{X,Y} = \frac{\mathrm{Cov}(X, Y)}{\sigma_X \sigma_Y}$ | Measures linear correlation; assumes finite second moments (population version). |
| **Sample Pearson correlation** | $r_{XY} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2} \sqrt{\sum (y_i - \bar{y})^2}}$ | Used in applied statistics and data analysis (sample version). |
| **Cosine similarity (Covariance-normalized)** | $r_{XY} = \cos(\theta) = \frac{\langle \vec{x}, \vec{y} \rangle}{\|\vec{x}\| \|\vec{y}\|}$ | Geometric interpretation in vector space; common in ML and NLP. |
| **Spearman's rank correlation** | $\rho_s = \rho(\mathrm{rank}(X), \mathrm{rank}(Y))$ | Nonparametric measure for monotonic relationships using ranks. |
| **Kendall’s tau** | $\tau = \frac{n_c - n_d}{\binom{n}{2}}$ | Nonparametric; based on concordant/discordant pairs. |
| **Point-Biserial correlation** | — | Pearson applied between a binary and a continuous variable. |
| **Phi coefficient (φ)** | — | Special case of Pearson correlation for two binary variables. |
| **Tetrachoric correlation** | — | Estimates correlation between latent continuous variables behind binary observations. |
| **Polychoric correlation** | — | Assumes latent continuous variables behind ordinal variables. |
| **Partial correlation** | $\rho_{XY \cdot Z} = \mathrm{Corr}(X - \hat{X}_Z, Y - \hat{Y}_Z)$ | Measures association between XX and YY controlling for ZZ. |
| **Canonical correlation** | $\rho = \max_{a,b} \mathrm{Corr}(a^\top X, b^\top Y)$ | Measures linear relation between two variable sets. |
| **Correlation matrix** | $\boldsymbol{R} = \boldsymbol{D}^{-1} \boldsymbol{\Sigma} \boldsymbol{D}^{-1}$ | Matrix of pairwise Pearson correlations; used in multivariate stats, PCA. |
| **Autocorrelation** | $\rho_k = \frac{\mathbb{E}[(X_t - \mu)(X_{t+k} - \mu)]}{\sigma^2}$ | Correlation of time series with lagged self. |
| **Cross-correlation (time series)** | $R_{XY}(k) = \mathbb{E}[X_t Y_{t+k}]$ | Time-lagged dependence between two series. |
| **Distance correlation (dCor)** | $\mathrm{dCor}(X,Y) > 0 \iff X \not\perp Y$ | Captures both linear and nonlinear dependence. |
| **Mutual information** | $I(X; Y) = \iint p_{XY}(x,y) \log \frac{p_{XY}(x,y)}{p_X(x)p_Y(y)} dxdy$ | Information-theoretic dependency measure. |
| **HSIC (Hilbert-Schmidt Independence Criterion)** | — | Kernel-based dependence measure in RKHS. |

## **Anti-Transitivity**

> A relationship is *anti-transitive* if, whenever it holds between **A → B** and **B → C**, it *necessarily does not hold* for **A → C**.
> 

> Anti-transitivity of correlation refers to the phenomenon where variables $X$ and $Y$ may both be positively correlated with a third variable $Z$, yet exhibit zero or even negative correlation with each other, due to the non-transitive nature of linear dependence in multivariate distributions.
> 

**Example**: "Beats" in Rock-Paper-Scissors:

- Rock → Scissors (beats)
- Scissors → Paper (beats)
- But Rock *does not beat* Paper (anti-transitive).

## Case  Studies

### “Fast walkers have higher IQ & larger brains than slow walkers.”

> [https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2752818](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2752818)`
> 

> Note: This study abuses the idea of transivity;  the non-tarnsitive correlation is also very small; it’s just  avery bad study.
> 

## Pitfalls

Correlation is a powerful statistical tool, but it comes with several **pitfalls** that can lead to **misinterpretation or misuse** if not properly understood. Here's a breakdown of the key issues:

### ⚠️ **Correlation ≠ Causation**

- **Pitfall:** People often assume that a correlation implies one variable causes the other.
- **Example:** Ice cream sales and drowning deaths are positively correlated—but both are driven by hot weather, not one another.

### 🔄 **Reverse Causality**

- **Pitfall:** The direction of cause is unclear.
- **Example:** A correlation between stress and poor sleep doesn’t tell you whether stress causes poor sleep or vice versa.

### 🌪️ **Confounding Variables**

- **Pitfall:** A third variable might influence both correlated variables.
- **Example:** Shoe size and reading ability may correlate in children, but age is the real driver.

### 🧾 **Spurious Correlation**

- **Pitfall:** Some correlations are coincidental or meaningless, especially when working with large datasets.
- **Example:** Correlation between cheese consumption and deaths by bedsheet entanglement—completely unrelated variables.

### 📏 **Linearity Assumption**

- **Pitfall:** Pearson correlation only detects **linear relationships**.
- **Consequence:** Nonlinear associations might be strong but have a low correlation coefficient.
- **Solution:** Use rank-based methods like **Spearman’s rho** or **visualize** the data.

### 💔 **Outliers Distorting Results**

- **Pitfall:** Outliers can heavily influence the correlation coefficient.
- **Example:** A single outlier in an otherwise weak relationship can create a misleadingly high correlation.

### 🔢 **Aggregation Bias / Simpson’s Paradox**

- **Pitfall:** Aggregating data can hide or reverse true relationships.
- **Example:** Two groups may show positive correlation individually, but combined data may show no correlation or a negative one.

### 🧠 **Misinterpretation of Strength**

- **Pitfall:** A "high" correlation (e.g., 0.8) is not always strong, depending on context, sample size, and measurement error.
- **Rule of Thumb:** Always interpret correlation in context.

### 📊 **Correlation Doesn’t Account for Time**

- **Pitfall:** Correlation is typically **synchronous**; it ignores time-lagged relationships.
- **Solution:** Use time series techniques if lagged effects are expected.

### 🔄 **Correlation in Non-Independent Observations**

- **Pitfall:** Correlation assumes data points are independent. Violations occur in clustered or repeated measures data.
- **Solution:** Use models that account for dependency (e.g., mixed models, hierarchical models).

## References

- https://en.wikipedia.org/wiki/Correlation
- [ ]  https://www.academia.edu/39797871/Fooled_by_Correlation_Common_Misinterpretations_in_Social_Science_
- [ ]  https://gwern.net/everything
- Correlation
Lee Rodgers, Joseph, and W. Alan Nicewander. "Thirteen ways to look at the correlation coefficient." The American Statistician 42.1 (1988): 59-66.
- [Correlation](https://en.wikipedia.org/wiki/Correlation)
- Yule, G. Udny. "On the theory of correlation." Journal of the Royal Statistical Society 60.4 (1897): 812-854.
- Pearson, Karl. "Notes on the history of correlation." Biometrika 13.1 (1920): 25-45.
- Spearman, Charles. "The proof and measurement of association between two things." The American journal of psychology 100.3/4 (1987): 441-471.
- A New Coefficient of Correlation ([arxiv.org](http://arxiv.org/))
[https://news.ycombinator.com/item?id=29687613](https://news.ycombinator.com/item?id=29687613)
- How to Think about Correlation? ([columbia.edu](http://columbia.edu/))
[https://news.ycombinator.com/item?id=25341601](https://news.ycombinator.com/item?id=25341601)
- Cosines and correlation (2010) ([johndcook.com](http://johndcook.com/))
[https://news.ycombinator.com/item?id=10498549](https://news.ycombinator.com/item?id=10498549)
- Thinking Clearly About Correlations and Causation (2018)
[https://news.ycombinator.com/item?id=24506243](https://news.ycombinator.com/item?id=24506243)
- When correlation is better than causation ([narrator.ai](http://narrator.ai/))
[https://news.ycombinator.com/item?id=28327198](https://news.ycombinator.com/item?id=28327198)
- Does Causation Imply Correlation? ([stats.stackexchange.com](http://stats.stackexchange.com/))
[https://news.ycombinator.com/item?id=7317254](https://news.ycombinator.com/item?id=7317254)
- Correlation is usually not causation. But why not? ([gwern.net](http://gwern.net/))
[https://news.ycombinator.com/item?id=8282373](https://news.ycombinator.com/item?id=8282373)
- If correlation doesn’t imply causation, then what does? (2012) ([michaelnielsen.org](http://michaelnielsen.org/))
[https://news.ycombinator.com/item?id=6030627](https://news.ycombinator.com/item?id=6030627)
- Spurious Correlations
[http://www.tylervigen.com/spurious-correlations](http://www.tylervigen.com/spurious-correlations)
- [A New Coefficient of Correlation](https://news.ycombinator.com/item?id=29687613) ([arxiv.org](http://arxiv.org/))
- [Guess the Correlation](http://guessthecorrelation.com/)
- [Correlation](https://en.wikipedia.org/wiki/Correlation)
- [What is the difference between an estimator and a statistic?](https://stats.stackexchange.com/questions/47728/what-is-the-difference-between-an-estimator-and-a-statistic)
- [Variance](variance.md)
- [Covariance](covariance.md)
- [Covariance Matrix](../mathematical/covariance-matrix.md)
- [Independence](independence.md)
