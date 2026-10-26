---
tags: [model-evaluation, statistic]
qa:
  - What is the origin of the term “null hypothesis”?
  - What does a null hypothesis assert about the world, as opposed to about a statistical model — and can a test decide between the two?
  - Is a p-value a measure of evidence, a decision input, or neither? What would it take for it to be a measure of evidence?
  - What separates Fisher’s significance testing from the Neyman–Pearson decision framework, and which one is invoked by “reject $H_0$”?
  - Under what conditions does failing to reject $H_0$ constitute evidence for $H_0$ — and when is a non-significant result merely an underpowered study?
  - Does a test need a specified alternative to be severe, or can severity be defined without one?
  - How does the choice of test statistic, model, and null constitute the hypothesis rather than merely test it?
  - When is statistical significance epistemically uninformative, and what would make it informative?
  - State the Neyman–Pearson lemma: what does it guarantee, and what does it leave open for composite alternatives?
  - What are the exact distributional assumptions of the $z$-, $t$-, $F$-, and ANOVA tests, and what fails when they do? When do Welch, robust, or bootstrap alternatives apply?
  - When is a permutation test exact? What exchangeability condition must hold, and what happens under unequal variances, dependence, or non-exchangeable designs?
  - How do you compute power and the minimal detectable effect for a two-sample test, and how do $\alpha$, $\beta$, variance, and sample size trade off?
  - What is the duality between confidence intervals and hypothesis tests, and what exactly does a 95% interval exclude?
  - What is the difference between a p-value, a $q$-value, and an adjusted p-value, and which error rate does each control?
  - How do Bonferroni, Holm, Hochberg, and Benjamini–Hochberg differ, and when is the false discovery rate the appropriate target?
  - How do optional stopping and sequential analysis change the null distribution, and what are alpha-spending and always-valid inference?
  - How do you test a composite null with nuisance parameters (profile likelihood, conditional or permutation tests), and when is the test conservative?
  - What are the failure modes of asymptotic tests with sparse or small samples, and when must an exact test be used?
  - What is the difference between a test’s size, power, consistency, and unbiasedness?
  - How do e-values and safe tests avoid the optional-stopping problem that p-values have?
---

# Statistical Hypothesis Testing

Related: [E-values](note.html?n=epistemica/validation/e-values.md), [p-value](note.html?n=epistemica/validation/p-value.md), [Model Validation](note.html?n=epistemica/validation/model-validation.md), [Calibration](note.html?n=epistemica/validation/calibration.md)

> In this note, we will cover statistical model validation — if you strip away the mysticism and historical baggage from hypothesis testing, model validation is what remains.

## Formulation

> Suppose we have a statistical model representing a population. We want to evaluate the model — or part of it — specifically its parameters, or certain properties of them. The value of the property under consideration is called the null hypothesis.

> Our evaluation procedures use sample data to determine whether there is sufficient statistical evidence to reject the null hypothesis (we try to find reasons why it is wrong).

> The guiding principle is to assess whether the observed data provide sufficient evidence against the null hypothesis — basically, to find ways to prove the null hypothesis wrong.

> Note: The terminology surrounding this — and the entire field of statistics — is just horrifying. One could simply say that the model is **non-parameterized**, and that the null hypothesis specifies a proposed value, property, or other characteristic of interest. It's fundamentally the same idea. If the model is non-parameterized, then — this can be seen as — parameter finding and validation at the same time.

> Note: For the most part, terms such as *null hypothesis* are legacy terminology — closely tied to statistical models of interventions. Their use can obscure the more general purpose of statistical hypothesis testing: evaluating and validating a model, or specific aspects of it, using sample data.

## Statistical Evaluation Procedure Space

> Note: The more specific kind is the statistical hypothesis test.

| **Testing Procedure** | **Description** | **Scope** |
|---|---|---|
| **Z-Test** | Tests a hypothesis concerning a population parameter using a Z-statistic. | Population means or other parameters; known variance or an appropriate approximation; normally distributed test statistic. |
| **T-Test (Student's T-Test)** | Tests hypotheses concerning population means using a T-statistic. | One-sample, independent-sample, or paired-sample means; unknown population variance; normally distributed observations or paired differences for exact small-sample inference. |
| **ANOVA (Analysis of Variance)** | Tests whether population means differ across multiple groups. | Comparing three or more means; independent observations, normally distributed errors, and equal variances for classical ANOVA. |
| **Chi-Square Test** | Tests hypotheses concerning categorical data, including independence and goodness-of-fit. | Categorical frequencies; independence, homogeneity, or goodness-of-fit; sufficiently large expected frequencies for standard asymptotic approximations. |
| **F-Test** | Tests hypotheses using an F-statistic, including hypotheses about variance ratios and model comparisons. | Comparing two population variances or evaluating model terms; independent, normally distributed populations for the classical variance-ratio test. |
| **Mann–Whitney U Test** | Tests whether two independent samples are consistent with the same underlying distribution. | Two independent groups; ordinal or continuous outcomes; independent observations. A median-difference interpretation requires additional assumptions about distributional shape. |
| **Wilcoxon Signed-Rank Test** | Tests hypotheses about paired differences using their ranks and signs. | Paired observations or one-sample differences; ordinal or continuous outcomes; symmetric differences for the usual location interpretation. |
| **Kruskal–Wallis Test** | Tests whether independent groups have the same underlying distribution. | Three or more independent groups; ordinal or continuous outcomes; independent observations. A location-difference interpretation requires comparable distributional shapes. |
| **Fisher's Exact Test** | Tests hypotheses concerning associations between categorical variables using exact probabilities. | Contingency tables, especially with small samples or sparse counts; categorical variables; an appropriate fixed-margin sampling framework. |
| **Log-Rank Test** | Tests whether survival distributions differ across groups. | Time-to-event outcomes; two or more groups; independent observations and appropriate handling of censoring. |
| **Cochran's Q Test** | Tests whether the proportions of a binary outcome differ across related conditions. | Three or more matched groups or repeated measurements; binary outcomes; matched observations. |
| **Shapiro–Wilk Test** | Tests the null hypothesis that observations come from a normal distribution. | Testing normality; continuous observations; independent sampling under the conventional formulation. |
| **Kolmogorov–Smirnov Test** | Tests whether an empirical distribution differs from a specified reference distribution or whether two samples come from the same distribution. | One-sample goodness-of-fit or two-sample distribution comparison; continuous distributions; reference distributions and critical values appropriate to the sampling setup. |
| **Levene's Test** | Tests whether population variances are equal across groups. | Comparing variances across two or more groups; continuous outcomes; independent observations; more robust to departures from normality than the classical variance-ratio F-test. |
| **Permutation Test** | Tests a hypothesis using a reference distribution constructed by permuting observations or group assignments. | Hypotheses concerning differences, associations, or other statistics; requires exchangeability under the null hypothesis or another valid permutation scheme. |

## References

- [E-values](note.html?n=epistemica/validation/e-values.md)
- [p-value](note.html?n=epistemica/validation/p-value.md)
- [Model Validation](note.html?n=epistemica/validation/model-validation.md)
- [Calibration](note.html?n=epistemica/validation/calibration.md)
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver and Boyd.
- Neyman, J., & Pearson, E. S. (1933). On the problem of the most efficient tests of statistical hypotheses. *Philosophical Transactions of the Royal Society A*, 231, 289–337.
- Casella, G., & Berger, R. L. (2002). *Statistical Inference* (2nd ed.). Duxbury.
- Lehmann, E. L., & Romano, J. P. (2005). *Testing Statistical Hypotheses* (3rd ed.). Springer.
- Good, P. (2005). *Permutation, Parametric, and Bootstrap Tests of Hypotheses* (3rd ed.). Springer.
- Vovk, V., & Wang, R. (2021). E-values: Calibration, combination and applications. *The Annals of Statistics*, 49(3), 1736–1754.
- Cohen, J. (1994). The earth is round (p < .05). *American Psychologist*, 49(12), 997–1003.
- Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine*, 2(8), e124.
- Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, 22(11), 1359–1366.
- Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B*, 57(1), 289–300.
- Greenland, S., Senn, S. J., Rothman, K. J., Carlin, J. B., Poole, C., Goodman, S. N., & Altman, D. G. (2016). Statistical tests, P values, confidence intervals, and power: A guide to misinterpretations. *European Journal of Epidemiology*, 31(4), 337–350.
- Wasserstein, R. L., & Lazar, N. A. (2016). The ASA statement on p-values: Context, process, and purpose. *The American Statistician*, 70(2), 129–133.
- Wasserstein, R. L., Schirm, A. L., & Lazar, N. A. (2019). Moving to a world beyond “p < 0.05”. *The American Statistician*, 73(sup1), 1–19.
- Mayo, D. G. (2018). *Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars*. Cambridge University Press.
- https://en.wikipedia.org/wiki/Statistical_hypothesis_test
- https://en.wikipedia.org/wiki/Confusion_matrix
- https://www.youtube.com/watch?v=DAkJhY2zQ3c
- https://www.youtube.com/watch?v=HDCOUXE3HMM
- https://www.youtube.com/watch?v=ncqcFNHmMoc
- https://www.youtube.com/watch?v=i60wwZDA1CI&t=85s
