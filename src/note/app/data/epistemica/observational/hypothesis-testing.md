---
tags: [model-evaluation, statistic]
---

# Hypothesis Testing

 : E-values (E-values%208179324899fa49448dff9f4b2d8e3138.md), p-value (p-value%20073a994bc0c54d2f861d8a7dbe15a62a.md), Model Validation (Model%20Validation%2024fc0f5171ec8060b23af2f0f74afdc4.md)

> WE can’t povee that things works this way; but we can prove that things does not work in a way. - This is the most fundamental idea in science test.
> 

## Strategy

| **Test Name** | **Description** | **Used For** | **Assumptions** |
| --- | --- | --- | --- |
| **Z-Test** | Tests the mean of a population against a known value when the population variance is known. | Comparing population means with a known variance | Normal distribution, known variance, large sample size |
| **T-Test (Student's T-Test)** | Compares the means of two groups (independent or paired samples) or compares the mean to a known value. | Comparing means between two groups or against a known value | Normal distribution, unknown variance, small sample size |
| **ANOVA (Analysis of Variance)** | Tests for differences among three or more group means to determine if at least one group mean is different. | Comparing means across multiple groups | Normal distribution, equal variances (homoscedasticity) |
| **Chi-Square Test** | Tests the association between categorical variables or the goodness-of-fit of observed data to expected data. | Testing independence, goodness-of-fit, or homogeneity | Large sample size, expected frequencies ≥ 5 |
| **F-Test** | Compares the variances of two populations to determine if they are significantly different. | Comparing variances between two groups | Normally distributed populations, equal sample sizes |
| **Mann-Whitney U Test** | A non-parametric test comparing differences between two independent groups on an ordinal or continuous outcome. | Comparing medians between two independent groups | No assumption of normality, ordinal data |
| **Wilcoxon Signed-Rank Test** | A non-parametric test for comparing two related samples or repeated measurements on a single sample. | Comparing paired samples | No assumption of normality, ordinal data |
| **Kruskal-Wallis Test** | A non-parametric version of ANOVA for comparing more than two groups on an ordinal or continuous outcome. | Comparing medians across multiple groups | No assumption of normality, ordinal data |
| **Fisher's Exact Test** | Tests for an association between two categorical variables, particularly useful with small sample sizes. | Testing independence in small sample sizes | Suitable for small sample sizes |
| **Log-Rank Test** | Compares survival distributions of two or more groups in survival analysis. | Comparing survival times between groups | Independent observations, consistent survival rates |
| **Cochran's Q Test** | A non-parametric test used for testing differences between three or more matched groups on a binary outcome. | Comparing binary outcomes across multiple matched groups | Binary outcomes, repeated measures |
| **Shapiro-Wilk Test** | Tests the null hypothesis that a sample comes from a normally distributed population. | Testing normality of a distribution | Small to moderate sample sizes |
| **Kolmogorov-Smirnov Test** | Compares a sample with a reference probability distribution, or compares two samples to test for differences. | Testing the goodness-of-fit or comparing two distributions | No assumption of normality |
| **Levene's Test** | Tests for equality of variances across groups. | Testing homogeneity of variances | Continuous data, can handle non-normal distributions |
| **Pearson's Chi-Square Test** | Tests the independence of two categorical variables in a contingency table. | Testing the association between categorical variables | Expected frequencies ≥ 5 |
| **Spearman's Rank Correlation** | Assesses the strength and direction of association between two ranked variables. | Measuring the correlation between two ordinal variables | No assumption of normality, ordinal data |
| **Bootstrap Resampling** | A non-parametric method for estimating the sampling distribution of a statistic by resampling with replacement. | Estimating the sampling distribution of a statistic from small samples | No assumption of normality, robust to small sample sizes |
| **Permutation Test** | A non-parametric method that tests the null hypothesis by calculating all possible values of a test statistic. | Testing hypotheses without making assumptions about the data distribution | No assumption of normality, computationally intensive |

## Hypothesis Testing

> **Hypothesis Testing:** Procedures for making decisions or inferences about population parameters based on sample data. Involves formulating null and alternative hypotheses and using statistical tests.
> 

> ANOVA (Analysis of Variance):  Models and compares means across multiple groups to assess significant differences.
> 

> Should I Reject   $H_0$?  Yes the p-value **is small** (≤ α);   no other wise.  If H₀ and H make the explanatory universe; rejecting H₀ proves H.
> 

> **Note.**  p-values does not really prove anything is juts for **rejection; but using the logic we can make a little abuse of the method.**
> 

**State the Hypotheses**

> Basic Setting:  ✅ The world works like this  “H” vs   ❌ It does not   $H_o$ (Not H).
> 
- **Null Hypothesis (H₀)**: This is the default assumption, typically stating that there is no effect or no difference. For example, H₀ might claim that a new drug has no effect.
- **Alternative Hypothesis (H₁ or Ha)**: This is the hypothesis that you aim to support, which posits that there is an effect or a difference. For example, Ha might claim that a new drug has an effect.

### 📋 Evaluation of Hypothesis Testing

> **Reject  $H_0$ or**  p-value **is small** (≤ α) **?**
> 

> **Null Hypothesis is True . →  No Reject (Does Not Means Accept - It’s Science; New Data Can Come)  ☑️**
> 

> **Null Hypothesis is False. → Reject  ❌**
> 

| **Ground Truth** | **Decision** | **Interpretation** |
| --- | --- | --- |
| ☑️ | ☑️ | **True Positive**: Correctly detected a real effect |
| ☑️ | ❌ | **Type II Error (False Negative)**: Missed detecting a real effect |
| ❌  | ☑️ | **Type I Error (False Positive)**: False alarm; no effect when there is none |
| ❌ | ❌ | **True Negative**: Correctly accepted the null hypothesis |

### p-hacking

> https://www.youtube.com/watch?v=HDCOUXE3HMM
> 

> https://www.youtube.com/watch?v=ncqcFNHmMoc
> 

> https://www.youtube.com/watch?v=i60wwZDA1CI&t=85s
> 

## References

- https://en.wikipedia.org/wiki/Statistical_hypothesis_test
- https://www.youtube.com/watch?v=DAkJhY2zQ3c
