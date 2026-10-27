---
tags: [validation, statistics]
qa:
  - What are the conventions for interpreting a p-value and determining the range of a p-value calculation procedure?
  - Why a metric on rejecting a hypothesis and not a metric on accepting a hypothesis?
  - Do we have clearer or better definitions than "the probability of obtaining test results at least as extreme as the observed results, assuming H0 is true"?
  - Which common tests produce p-values, and from which null distributions?
  - What are the alternatives and complements to the p-value?
  - **What are the problems with the following wording?** 'The p-value is the tail probability of a test statistic under the null model'.
note: We need to get deeper into the scope, practice, case studies, etc.
---

# P-Value

> In this note, we introduce the **p-value** as a mechanism for evaluating a model of the population by using sample data to assess its consistency with the model.

> **Note:** Studying statistics is basically an exercise in fixing historically crappy terminology. Statistics is the field with the worst terminology: a huge pile of materialized, never-refactored definitions, terms, and conceptualizations. So, a huge amount of time is wasted trying to fit things into terrible conceptual frameworks instead of getting to the substance.

## Formulation

### What Is This Epistemic Instance?

> The intuitive, pre-formal idea behind p-values is the following.

> Suppose we have a statistical model for a population and a set of parameters or properties associated with that model. Let us call this model \(M_p\).

> We want to evaluate a particular property or parameter by repeatedly recomputing its value from sample data. The resulting quantity is called a **test statistic**, denoted by \(T\). Its possible values are characterized by a probability distribution.

> This is the fundamental building block of any p-value calculation procedure. The computation of the p-value in any specific formulation embodies a **a derivation from the distribution of \(T\)**.

### Which is the usual technical formulation of the p-value computation?

> Note: For practical purposes, what we are interested in is the \(p\)-value of \(t_{\mathrm{obs}}\) derived from \(M_p\).

> The usual technical formulation of this calculation is: \(p_{\mathrm{obs}} = \Pr(T < t_{\mathrm{obs}}) + \Pr(T > t_{\mathrm{obs}})\).

> Intrpertion of (p_{\mathrm{obs}} - for thi swe will introduces the significance threshold / alpha level, 

> Note: The extreme - blah, blah cames from the >, <.

![p-value](../assets/note/epistemica/validation/p-value.png)

### How to Interpret p-values?

> To interpret \(p_{\mathrm{obs}}\), we introduce the significance threshold, or significance level, \(\alpha\). Comparing \(p_{\mathrm{obs}}\) with \(\alpha\) provides a decision criterion for evaluating the compatibility of \(t_{\mathrm{obs}}\) with the null hypothesis ($P_m$).

> In research practice \(\alpha\) is set to 0.005.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Representation`** — the p-value is a `Representation Element` in a **Quantitative Representation** system, read as a **Statistical Quantity**. 

> Secondary type: **`Epistemic Operation`** — the p-value calculation is a **Statistical Operation** under **Statistical Inference** → **Hypothesis Testing**. The decomposition table roots both under the shared `Epistemic Element` genus, as the two hierarchies do.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in four ways that the decomposition keeps apart.

> **First, aspect.** The p-value is a quantity, the p-value calculation is an operation, the rule $p \le \alpha$ is a decision rule, and "evidence" is a role the quantity can play under a severity reading. Collapsing them into one type makes "p-value" equivocal.

> **Second, framework.** Fisher's p-value is a continuous measure of evidence against $H_0$ without a specified alternative; the Neyman–Pearson framework uses a pre-specified $\alpha$, a power $\beta$, and a decision between $H_0$ and $H_1$; null-hypothesis significance testing (NHST) conflates the two. The note keeps the quantity and the decision rule separate.

> **Third, time.** $p(X)$ is a random variable with a null distribution; $p(x)$ is a realized value. A p-value is not a property of $H_0$ that exists before the sample.

> **Fourth, model and ordering.** "At least as extreme" is not determined by $H_0$ alone; it requires an ordering induced by the alternative or the likelihood ratio. Composite nulls use the supremum, discrete statistics produce conservative p-values, and two-sided tests need a convention that can fail for asymmetric null distributions. The same data can yield different p-values under different tests; that is the definition, not a defect.

> The ambiguity is resolved by declaring the two branches and keeping $\alpha$, the test statistic, the null model, the ordering, and the decision rule as separate elements. A p-value is determinate relative to a declared test, not absolutely.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: the table decomposes the p-value element under two kind branches — the representation (the quantity) and the operation (its calculation). Stopping rule: a row is terminal when it names a concrete quantity, model component, procedure, act, principle, or test; the branches are not decomposed further here. Identity: every path is unique; instance rows are Title Case; type groupings are backticked; no type terminates a branch. Typing: the root is `Epistemic Element`; the p-value branch is `Epistemic Representation`, the calculation branch is `Epistemic Operation`; both are read as elements of inquiry.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` → `Epistemic Representation` | Grouping: the p-value read as a representation. |
| `Epistemic Element` → `Epistemic Operation` | Grouping: the p-value calculation read as an operation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` | Grouping: the quantitative sign system in which the p-value is expressed. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation | The system of quantities, scales, and numerical comparison. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` | Grouping: the combinable constituents of the quantitative representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Statistical Quantity | A quantity defined by a statistical model and a sampling distribution rather than by direct measurement. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Test Statistic | The statistic $T(X)$ whose sampling distribution orders the sample space. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Significance Level | The pre-specified threshold $\alpha$; a convention, not a property of the data. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Critical Region | The set of samples whose statistic is at least as extreme as the observed one. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Statistical Quantity → `Representation Element` | Grouping: the constituents of the statistical quantity. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Statistical Quantity → `Representation Element` → P-Value | The tail probability of a statistic at least as extreme as the observed one, under $H_0$. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` | Grouping: the rules and structures constituting the quantitative representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Null Model | The statistical model with $H_0$ imposed; the distribution that generates the p-value. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Sampling Distribution | The distribution of $T(X)$ under the null model. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Extremeness Ordering | The rule that defines "at least as extreme" — one-sided, two-sided, or likelihood-ratio. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Null Hypothesis | The hypothesis $H_0$ whose compatibility the p-value represents. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Alternative Hypothesis | The hypothesis $H_1$ that fixes the direction of extremeness. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Independence Assumption | The sampling units are independent under the model. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Distributional Assumption | The assumed family of the data or of the test statistic. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Nuisance Parameter | The parameter not fixed by $H_0$, eliminated by the supremum or by a conditional construction. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` | Grouping: properties of the p-value representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Unit Interval | The p-value lies in $[0,1]$. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Uniform Null Distribution | Under a simple null and a continuous statistic, the p-value is uniform on $(0,1)$. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Stochasticity | The p-value is a random variable before the sample is drawn. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Sample-Size Dependence | The null distribution, and often the p-value, changes with the sample size. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Model Dependence | The p-value depends on the model, the statistic, and the ordering, not on $H_0$ alone. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` | Grouping: the organized operation that produces the p-value. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` | Grouping: generalized ways of performing the statistical operation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation | The organized class of operations that infer from sample to population under a statistical model. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference | Inference from sample to population under a model. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing | The method that evaluates $H_0$ against $H_1$ by a test statistic and a rejection rule. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` | Grouping: ordered routines within hypothesis testing. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation | The procedure that computes the p-value from the observed statistic and its null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` | Grouping: the steps of the p-value calculation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` → Test Statistic Computation | Compute $T(x)$ on the sample. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` → Tail Probability Computation | Integrate or sum the null distribution over the critical region. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` → Decision Comparison | Compare $p$ with the pre-specified $\alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` → P-Value Report | Report the value with the test, model, sample size, and multiplicity correction. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` | Grouping: the tests that realize hypothesis testing. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → Z-Test | Test a mean or other parameter with a standard normal null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → T-Test | Test a mean with a $t$ null distribution and an estimated variance. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → Chi-Square Test | Test categorical frequencies or model fit with a chi-square null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → F-Test | Test variance ratios or model terms with an $F$ null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → Permutation Test | Build the null distribution by permuting observations or assignments. |
| `Epistemic Element` → `Epistemic Operation` → `Action` | Grouping: the primitive acts of the calculation. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Specify Hypothesis Act | Fix $H_0$, $H_1$, the model, and the test statistic. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Choose Significance Level Act | Fix $\alpha$ before looking at the data. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Compute Test Statistic Act | Evaluate $T(x)$ on the sample. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Compute Tail Probability Act | Evaluate the probability of a statistic at least as extreme. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Compare To Threshold Act | Apply the golden rule $p \le \alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Report P-Value Act | Report the value with its test, model, and multiplicity context. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` | Grouping: rules guiding the calculation and its use. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Significance Principle | Reject $H_0$ at level $\alpha$ iff $p \le \alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Severity Principle | Read the p-value as evidence only relative to a test with a good chance of detecting a false $H_0$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Multiplicity Principle | Adjust $\alpha$ or the p-values for multiple comparisons. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Model-Checking Principle | Check the model assumptions before reading the p-value. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The note distinguishes the p-value from $\alpha$, the test statistic, the decision rule, the posterior probability, the Bayes factor, and the effect size. |
| **Definitional Clarity** | Partial | The formal definition is clear only when the model, $H_0$, statistic, and extremeness ordering are declared; the ordinary-language definition ("probability of obtaining results at least as extreme") is ambiguous and easily misread. |
| **Conceptual Determinacy** | Partial | "At least as extreme" is not determined by $H_0$ alone; composite nulls, discrete statistics, and two-sided tests require conventions. The p-value is determinate relative to a declared test, not absolutely. |
| **Internal Consistency** | Pass | The quantity, the operation, and the decision rule are kept distinct; the golden rule is consistent with the definition; uniformity is stated under the conditions that make it true. |
| **Representational Adequacy** | Partial | It represents compatibility with $H_0$ under a model; it does not represent the truth of $H_0$, the size of an effect, the probability of replication, or the posterior. It is adequate for its purpose, not for general evidence quantification. |
| **Purpose Adequacy** | Partial | It serves test-based compatibility and decision rules well; it is inadequate as a standalone measure of evidence or for accepting $H_0$. Confidence intervals, effect sizes, Bayes factors, e-values, and severity are the complements. |

## QA

### What are the conventions for interpreting a p-value and determining the range of a p-value calculation procedure?

> **Range.** The p-value lies in $[0,1]$. Under a simple null with a continuous statistic and a valid test, it is uniform on $(0,1)$ under $H_0$. A discrete statistic produces a countable set of possible p-values and conservative (stochastically larger) values; a composite null uses the supremum over $\Theta_0$; a randomized test can produce a continuous p-value.

> **Thresholds.** $0.05$, $0.01$, and $0.001$ are conventions, not laws of nature. Report the exact p-value, the test, the model, the sample size, and any multiplicity correction. "Statistically significant" is not "practically important".

> **Decision.** At a pre-specified level $\alpha$: $p \le \alpha$ means reject $H_0$; $p > \alpha$ means fail to reject $H_0$. The rule is a decision convention, not a proof. Failing to reject is not accepting: acceptance would require a prior, a loss function, and a power analysis.

> **Evidence.** A smaller p-value means greater incompatibility between the data and $H_0$ under the model. It is not the probability that $H_0$ is true, not the probability that the data arose by chance, not the probability of replication, not an effect size, not a posterior probability, and not a Bayes factor.

> **Communication.** Use compatibility language: "the data are incompatible with the model at the $\alpha$ level", not "the result is significant, therefore the hypothesis is true". Report the p-value alongside an interval estimate and an effect size whenever the question is about magnitude rather than compatibility.

> **Range of the calculation procedure.** The procedure's possible outputs are the p-values generated by the test's rejection regions. Its size is $\sup_{\theta \in \Theta_0} \mathbb{P}_\theta(\text{reject}) \le \alpha$; its power is $\mathbb{P}_{\theta_1}(\text{reject})$ for a chosen alternative. The p-value is the smallest $\alpha$ at which the test rejects, so the procedure's range and its rejection regions are two views of the same test.

> The ASA statement's six principles are the standard communication conventions:
>
> 1. p-values can indicate how incompatible the data are with a specified statistical model;
> 2. p-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone;
> 3. scientific conclusions and decisions should not be based only on whether a p-value passes a specific threshold;
> 4. proper inference requires full reporting and transparency;
> 5. a p-value, or statistical significance, does not measure the size of an effect or the importance of a result;
> 6. by itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis.

### Is the p-value computed from the distribution of \(T\) or from \(M_p\), which determines the distribution of \(T\)?

> **Note:** By \(M_p\), I mean the fitted model, not an estimator of its parameters.

> The p-value depends on the distribution of \(T\). However, this distribution is determined by the statistical procedures used to estimate the parameters of \(M_p\), not by the specific parameter values contained in \(M_p\).

> These procedures must account for the **form of the model**, but not necessarily its specific parameter values. We call such a procedure an *estimator*.

> Note: That the p-value becomes a random variable - sort ot - and one report p for a $t_\text{obs}$, which  can be or p in $M_p$ if we want.

### Which common tests produce p-values, and from which null distributions?

| Test | Test statistic | Null distribution | p-value |
| --- | --- | --- | --- |
| **Z-test** | $Z = (\bar{X} - \mu_0)/(\sigma/\sqrt{n})$ | standard normal | tail probability of $Z$ |
| **T-test** | $t = (\bar{X} - \mu_0)/(s/\sqrt{n})$ | $t$ with $n-1$ degrees of freedom | tail probability of $t$ |
| **Chi-square test** | $\chi^2 = \sum (O_i - E_i)^2 / E_i$ | chi-square with the appropriate degrees of freedom | upper-tail probability |
| **F-test (ANOVA)** | $F = MS_{\text{between}}/MS_{\text{within}}$ | $F$ with the appropriate degrees of freedom | upper-tail probability |
| **Permutation test** | any test statistic | permutation distribution under exchangeability | proportion of permuted statistics at least as extreme |

### What are the alternatives and complements to the p-value?

> - **Confidence intervals** — a range of plausible parameter values; the interval is the estimate, the p-value is a compatibility summary.
> - **Effect sizes** — Cohen's $d$, odds ratios, risk differences, $R^2$; a small p-value does not imply a large effect.
> - **Bayes factors and posterior probabilities** — evidence and belief updating with an explicit prior and loss.
> - **E-values** — a test martingale that remains valid under optional stopping and multiplicity.
> - **Severity** — the probability that a test would have detected a false $H_0$; a p-value is evidence only relative to a severe test.
> - **Replication and pre-registration** — the design features that make a significance claim credible.
> - **Power analysis** — the probability of detecting an effect of a given size before the data are collected.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [Statistical Hypothesis Testing](note.html?n=epistemica/validation/statistical-hypothesis-testing.md)
- [Validation](note.html?n=epistemica/validation/validation.md)
- [Calibration](note.html?n=epistemica/validation/calibration.md)
- [E-value](note.html?n=epistemica/validation/e-value.md)
- [EES atlas](data/epistemica/ees.html)
- Goodman, S. (2008). A dirty dozen: Twelve p-value misconceptions. *Seminars in Hematology*, 45(3), 135–140.
- Cohen, J. (1994). The earth is round (p < .05). *American Psychologist*, 49(12), 997–1003.
- Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine*, 2(8), e124.
- Wasserstein, R. L., & Lazar, N. A. (2016). The ASA statement on p-values: Context, process, and purpose. *The American Statistician*, 70(2), 129–133.
- Wasserstein, R. L., Schirm, A. L., & Lazar, N. A. (2019). Moving to a world beyond "p < 0.05". *The American Statistician*, 73(sup1), 1–19.
- Greenland, S., Senn, S. J., Rothman, K. J., Carlin, J. B., Poole, C., Goodman, S. N., & Altman, D. G. (2016). Statistical tests, P values, confidence intervals, and power: A guide to misinterpretations. *European Journal of Epidemiology*, 31(4), 337–350.
- Mayo, D. G. (2018). *Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars*. Cambridge University Press.
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver and Boyd.
- Neyman, J., & Pearson, E. S. (1933). On the problem of the most efficient tests of statistical hypotheses. *Philosophical Transactions of the Royal Society of London. Series A*, 231(694–706), 289–337.
- Thiese, M. S., Ronna, B., & Ott, U. (2016). P value interpretations and considerations. *Journal of Thoracic Disease*, 8(9), E928.
- Thisted, R. A. (1998). What is a P-value. Departments of Statistics and Health Studies.
- Meehl, P. E. (1967). Theory-testing in psychology and physics: A methodological paradox. Philosophy of Science, 34(2), 103–115. http://www.jstor.org/stable/10.2307/186099
- [p-value](https://en.wikipedia.org/wiki/P-value)
- [Misuse of p-values](https://en.wikipedia.org/wiki/Misuse_of_p-values)
- [p-Values and P-Value Hacking: a simplified lecture](https://www.youtube.com/watch?v=ncqcFNHmMoc)
- [What is a p-value?](https://www.youtube.com/watch?v=9jW9G8MO4PQ)
- [P values are not as reliable as many scientists assume](https://news.ycombinator.com/item?id=7225739&utm_source=chatgpt.com)
- [Why I've lost faith in p values](https://news.ycombinator.com/item?id=16916145&utm_source=chatgpt.com)
- [Don't calculate p-values without understanding them](https://news.ycombinator.com/item?id=5679707&utm_source=chatgpt.com)
- [Statistics: P values are just the tip of the iceberg](https://news.ycombinator.com/item?id=9463806&utm_source=chatgpt.com)
- [P-Values are not Error Probabilities](https://news.ycombinator.com/item?id=9330076)
- [What is the meaning of p values and t values in statistical tests?](https://stats.stackexchange.com/questions/31/what-is-the-meaning-of-p-values-and-t-values-in-statistical-tests)
