---
tags: [model-evaluation]
---

# p-value

> Notice: the trick here is tno set the null hypotheis as negatingsomethgn that you wnat to provee,  if you find the null hy0pothee false - than the thing that you want to provee is validaetd.

> It’s a hypothesis testing method that answers the question: Should we **reject the null** hypothesis?
> 

> If the null hypothesis is true (high - p value)?  What is the probability of obtaining a **statistic as extreme** as to **observe results**?
> 

- High P-Value → The data that I observe  is in favor of the null (Low Surprise)
- Small P-Value → The data that I observe  is against the null (High Surprise)

QA:

- Why a metric on rejecting a hypothesis and not a metric on accepting a **hypothesis**?
- Do we have more clear and better definitions than “The **p-value** is the probability of obtaining test results at **least (>)** as extreme as the observed results, assuming that the **null hypothesis $H_0$** is true”?

The (asymptotic) p-value of a test ψ_α is the smallest (asymptotic)
level α at which ψα rejects H0. It is random, it depends on the
sample.

Golden rule p-value ≤ α ⇔ H_0 is rejected by ψα, at the (asymptotic) level α.
The smaller the p-value, the more confidently one can reject H_0.

## Formulation

> The **p-value** is the probability of obtaining test results at **least (>)** as extreme as the observed results, assuming that the **null hypothesis $H_0$** is true.
> 
- A small p-value (typically ≤ 0.05) suggests strong evidence against $H_0$, leading to its rejection.
- A large p-value (> 0.05) suggests weak evidence against $H_0$, meaning we fail to reject it.

### **Mathematical Formulation**

> For a test statistic $T$ with observed value $t$:
> 
- **One-tailed test (right-tailed):**  $p\text{-value} = P(T \geq t \mid H_0)$
- **One-tailed test (left-tailed):**  $p\text{-value} = P(T \leq t \mid H_0)$
- **Two-tailed test:**  $p\text{-value} = 2 \cdot \min \left( P(T \geq t \mid H_0), P(T \leq t \mid H_0) \right)$

### **Steps in the p-value Procedure**

1. **State Hypotheses:**
    - Null hypothesis $H_0$
    - Alternative hypothesis $H_1$ or $H_a$
2. **Choose Significance Level $\alpha$:** Common values: 0.01, 0.05, or 0.10.
3. **Compute Test Statistic:** Depends on the test (e.g., z-test, t-test, chi-square test).
4. **Calculate p-value:** Use the appropriate statistical distribution (Normal, t, F, χ², etc.).
5. **Make Decision:**
    - If $p\text{-value} \leq \alpha$, **reject $H_0$**.
    - If$p\text{-value} > \alpha$, **fail to reject $H_0$**.

### **Assumptions**

- The data must meet the assumptions of the statistical test used (e.g., normality, independence, random sampling).
- The p-value is **not** the probability that $H_0$ is true or false; it only measures compatibility with $H_0$.

### **Interpretation Caveats**

- **Not a measure of effect size:** A small p-value does not imply a large effect.
- **Sensitive to sample size:** Large samples may yield small p-values even for trivial effects.
- **Misuse risks:** P-hacking (fishing for significance) can lead to false positives.

### **Alternatives & Complements**

- **Confidence Intervals (CI):** Provide a range of plausible values for the parameter.
- **Bayesian Methods:** Use prior distributions to compute posterior probabilities.
- **Effect Size Measures:** Cohen’s d, odds ratio, R², etc.

### **Common Tests & p-value Calculations**

| **Test** | **Test Statistic** | **p-value Calculation** |
| --- | --- | --- |
| **Z-test** |  $Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}$ | From standard normal distribution |
| **T-test** | $t = \frac{\bar{X} - \mu}{s/\sqrt{n}}$ | From t-distribution (df = n-1) |
| **Chi-square test** | $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$ | From chi-square distribution |
| **F-test (ANOVA)** | $F = \frac{MS_{\text{between}}}{MS_{\text{within}}}$ | From F-distribution |

## References

- https://en.wikipedia.org/wiki/P-value
- https://en.wikipedia.org/wiki/Misuse_of_p-values
- https://www.youtube.com/watch?v=ncqcFNHmMoc
- Goodman, Steven. "A dirty dozen: twelve p-value misconceptions." Seminars in hematology. Vol. 45. No. 3. WB Saunders, 2008.
- https://news.ycombinator.com/item?id=9330076
- https://news.ycombinator.com/item?id=7225739
- https://news.ycombinator.com/item?id=16916145
- https://news.ycombinator.com/item?id=5679707
- https://news.ycombinator.com/item?id=9463806
- **Cohen, J. (1994).** *The Earth is Round (p < .05)*. *American Psychologist*.
- Ioannidis, J. P. A. (2005). Why Most Published Research Findings Are False. PLoS Medicine.
- Wasserstein, R. L., et al. (2019). Moving to a World Beyond “p < 0.05”. The American Statistician.
- Thiese, Matthew S., Brenden Ronna, and Ulrike Ott. "P value interpretations and considerations." Journal of thoracic disease 8.9 (2016): E928.
- Thisted, Ronald A. "What is a P-value." Departments of Statistics and Health Studies (1998).
- https://www.youtube.com/watch?v=9jW9G8MO4PQ
- [https://en.wikipedia.org/wiki/Neyman–Pearson_lemma](https://en.wikipedia.org/wiki/Neyman%E2%80%93Pearson_lemma)
- Hypothesis Testing (Hypothesis%20Testing%201d8c0f5171ec8059ab37d8dcb755dbae.md)

