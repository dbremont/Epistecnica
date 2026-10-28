---
tags: [validation, statistics]
qa:
  - What are the conventions for interpreting a p-value and determining the range of a p-value calculation procedure?
  - Why a metric on rejecting a hypothesis and not a metric on accepting a hypothesis?
  - Do we have clearer or better definitions than "the probability of obtaining test results at least as extreme as the observed results, assuming H0 is true"?
  - Which common tests produce p-values, and from which null distributions?
  - What are the alternatives and complements to the p-value?
  - What is a significance-level (p-value) framework?
  - What are the properties of a p-value?
  - What the p-value is not?
  - **What are the problems with the following wording?** 'The p-value is the tail probability of a test statistic under the null model'.
  - Why is hypothesis testing is a form of model validation?
  - Why is this useful 'The p-value is the probability under the null hypothesis of obtaining a real-valued test statistic at least as extreme as the one obtained '?
  
  - I find it difficult to interpret what it means to have \(p > 0.05\). Does this mean that we cannot reject the null hypothesis? What exactly do the tails tell us? Why is having a larger proportion of observations in the tail a reason not to reject the null hypothesis? Is this about how surprising the observed result is? If so, why?
---

# P-Value

> aka. Significance Level.

> In this note, we introduce the **p-value** as a mechanism for evaluating a model of the population by using sample data to assess its consistency with the model.

> **Note:** Studying statistics is basically an exercise in fixing historically crappy terminology. Statistics is the field with the worst terminology: a huge pile of materialized, never-refactored definitions, terms, and conceptualizations. So, a huge amount of time is wasted trying to fit things into terrible conceptual frameworks instead of getting to the substance.

## Formulation

### What Is This Epistemic Instance?

> The intuitive, pre-formal idea behind p-values is the following.

> Suppose we need to validate a `fitted statistical  model` (parameters, properties of the parameters) for a population. Let us call this model \(M_p\).

> A sensible way to approach  to this -- is to draw multiple samples (subsets of the population) and recompute the parameters of interest for each sample. The resulting values form an **empirical** sampling **distribution** of the inference parameter (statistic), let's called  \(T\). In statistical terminology, each computed value is called a **test statistic**.

> This is the fundamental building block of any p-value calculation procedure. Computing a p-value involves **deriving a probability from the distribution of \(T\)**, typically by integrating over the **tails** - **extremes** (define relative to some **reference value**) (**our observation**). In other words, it measures how unusual the tails are relative to the rest of theelements in the distribution. After this, we use a **decision threshold**, usually denoted by \(\alpha\), to determine whether the observed sample results are in accordance with the model or not.

> Note: This makes seems like a paradox (at least to me) but thin tails, will have a small p-value, meanin less probably, that is less consistent with what the model overall entails.

> Note: In statistics, we never definitively prove or disprove a hypothesis; we simply evaluate and summarize the available evidence. This is because statistical models are not substantive descriptions of reality; they are surface-level representations of the aspects of reality captured by the observed data.

> Note: In  practice - the distribution is assume - and the value is just computed. So it's assumption after assumption.

### Which is the usual technical formulation of the p-value computation?

> Note: For practical purposes, what we are interested in is the \(p\)-value of \(t_{\mathrm{obs}}\) derived from \(M_p\).

> Note: The specific formula for computing the `p-value` depends on the type of distribution, but it's always a measure of extremeness.How much do the elements differ from the common?

> Note: The extreme - blah, blah cames from the >, <.

> See [P-Value Atlas](data/epistemica/validation/atlas/pvalue.html) — the null distributions, their tail formulas, and a simulation lab.

> The p-value is the **largest** probability, over all parameter values consistent with the null hypothesis, of observing a test statistic **at least as extreme** as the one actually observed — where "at least as extreme" is defined by a pre-specified ordering \(\succeq\).

> Let:
> 
> - \(X = (X_1, \dots, X_n)\) be a random sample from a distribution \(P_\theta\), where \(\theta \in \Theta\).
> - \(\Theta_0 \subseteq \Theta\) be the **null parameter space** (the set of parameter values consistent with \(H_0\)).
> - \(T: \mathcal{X} \to \mathbb{R}\) be a **test statistic** (a measurable function of the sample).
> - \(\succeq\) be a **total preorder** on the range of \(T\) (the "at least as extreme as" ordering).
> - \(x\) be the **observed** sample, and \(t_{\text{obs}} = T(x)\) the observed value of the statistic.
>
> The **p-value** is defined as:
>
> \[
\boxed{
p(x) \;=\; \sup_{\theta \in \Theta_0} \; P_\theta\big(T(X) \succeq t_{\text{obs}}\big)
}
\]

### Which are the parts of the technical formulation?


1. **Sample and sample space**  
   - **Technical:** \(X=(X_1,\dots,X_n)\), sample space \(\mathcal{X}\), observed sample \(x\in\mathcal{X}\).  
   - **Intuition:** This is the data you actually got, and all the data you could have gotten.

2. **Statistical model**  
   - **Technical:** A family \(\{P_\theta:\theta\in\Theta\}\) plus assumptions such as independence, normality, identical distribution, etc.  
   - **Intuition:** This is the assumed data-generating machine. It says what kinds of data are plausible under different parameter values.

3. **Null hypothesis / null parameter space**  
   - **Technical:** \(H_0:\theta\in\Theta_0\), where \(\Theta_0\subseteq\Theta\). Simple null: \(\Theta_0=\{\theta_0\}\). Composite null: \(\Theta_0\) has more than one value.  
   - **Intuition:** This is the claim you are testing — the “boring” or “no effect” model you want to check against the data.

4. **Test statistic**  
   - **Technical:** A measurable function \(T:\mathcal{X}\to\mathbb{R}\), with observed value \(t_{\text{obs}}=T(x)\).  
   - **Intuition:** This is the single number that summarizes how far the data are from what the null model expects.

5. **Extremeness ordering**  
   - **Technical:** A total preorder \(\succeq\) on the range of \(T\), defining “at least as extreme as.” It is induced by the alternative hypothesis, the likelihood ratio, or a convention such as equal-tailed or shortest-interval.  
   - **Intuition:** This says which outcomes count as “more surprising” or “more against \(H_0\)” than the observed one. Without it, “at least as extreme” is undefined.

6. **Null distribution / probability computation**  
   - **Technical:** Compute  
     \[
     p(x)=\sup_{\theta\in\Theta_0} P_\theta\big(T(X)\succeq T(x)\big).
     \]
     For a simple null, this is just \(P_{\theta_0}(T(X)\succeq t_{\text{obs}})\).  
   - **Intuition:** This is the actual tail probability: how often the test statistic would be at least as extreme as what you observed, if the null model were true. The supremum makes the p-value valid for composite nulls.


### How to find p-values for different distributions?

![p-value](../assets/note/epistemica/validation/p-value.png)

### How to Interpret p-values?

> To interpret \(p_{\mathrm{obs}}\), we introduce the significance threshold, or significance level, \(\alpha\). Comparing \(p_{\mathrm{obs}}\) with \(\alpha\) provides a decision criterion for evaluating the compatibility of \(t_{\mathrm{obs}}\) with the null hypothesis ($P_m$).

> In research practice \(\alpha\) is set to 0.05.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Representation`** — the p-value is a `Representation Element` in a **Quantitative Representation** system, read as a **Statistical Quantity**. 

> Secondary type: **`Epistemic Operation`** — the p-value calculation is a **Statistical Operation** under **Statistical Inference** → **Hypothesis Testing**. The decomposition table roots both under the shared `Epistemic Element` genus, as the two hierarchies do.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in four ways that the decomposition keeps apart.

> **First, aspect.** The p-value is a quantity, the p-value calculation is an operation, the rule $p \le \alpha$ is a decision rule, and "evidence" is a role the quantity can play under a severity reading. Collapsing them into one type makes "p-value" equivocal.

> **Second, framework.** Fisher's p-value is a continuous measure of evidence against $H_0$ without a specified alternative; the Neyman–Pearson framework uses a pre-specified $\alpha$, a power $\beta$, and a decision between $H_0$ and $H_1$; null-hypothesis significance testing (NHST) conflates the two; the Bayesian framework computes a posterior-predictive p-value and a Bayes factor against a posterior reference model. The note keeps the quantity and the decision rule separate, and files the four frameworks as formulations of the statistical significance validation — `Organization` → Statistical Significance Validation → Formulation.

> **Third, time.** $p(X)$ is a random variable with a null distribution; $p(x)$ is a realized value. A p-value is not a property of $H_0$ that exists before the sample.

> **Fourth, model and ordering.** "At least as extreme" is not determined by $H_0$ alone; it requires an ordering induced by the alternative or the likelihood ratio. Composite nulls use the supremum, discrete statistics produce conservative p-values, and two-sided tests need a convention that can fail for asymmetric null distributions. The same data can yield different p-values under different tests; that is the definition, not a defect.

> The ambiguity is resolved by declaring the two branches and keeping $\alpha$, the test statistic, the null model, the ordering, and the decision rule as separate elements. A p-value is determinate relative to a declared test, not absolutely.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: the table decomposes the p-value element under two kind branches — the representation (the quantity) and the operation (the statistical significance validation that computes it). Stopping rule: a row is terminal when it names a concrete quantity, model component, procedure, act, principle, test, or formulation; the branches are not decomposed further here. Identity: every path is unique; instance rows are Title Case; type groupings are backticked; no type terminates a branch. Typing: the root is `Epistemic Element`; the p-value branch is `Epistemic Representation`, the calculation branch is `Epistemic Operation`, organized as the statistical significance validation; both are read as elements of inquiry.

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
| `Epistemic Element` → `Epistemic Operation` → `Organization` | Grouping: the organized operation that validates a model by statistical significance. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation | The practice that validates a model by asking how surprising the observed data are under it. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → Formulation | The formulation the practice adopts: reference model, quantity, role of $\alpha$, licensed output, evidence claim, and error guarantee. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → Formulation → Fisherian Formulation | Null-reference tail probability read as graded evidence; $\alpha$ is a reporting grade; no alternative, no accept/reject. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → Formulation → Neyman–Pearson Formulation | Null-and-alternative reference with pre-set $\alpha$ and power $\beta$; the p-value serves a rejection rule whose currency is error rates. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → Formulation → NHST Formulation | Fisher's tail probability run through Neyman–Pearson's threshold: a decision without an alternative or power, an evidence claim without severity. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → Formulation → Bayesian Formulation | Posterior-predictive reference: the Bayesian p-value and the Bayes factor replace the null tail and $\alpha$; a peer formulation whose reference model is the posterior, not $H_0$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` | Grouping: generalized ways of performing the validation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation | The organized class of operations that infer from sample to population under a statistical model. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference | Inference from sample to population under a model. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing | The method that evaluates $H_0$ against $H_1$ by a test statistic and a rejection rule. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` | Grouping: ordered routines within hypothesis testing. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation | The procedure that computes the p-value from the observed statistic and its null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` | Grouping: the steps of the p-value calculation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` → Test Statistic Computation | Compute $T(x)$ on the sample. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` → Tail Probability Computation | Integrate or sum the null distribution over the critical region. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` → Decision Comparison | Compare $p$ with the pre-specified $\alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → P-Value Calculation → `Procedure` → P-Value Report | Report the value with the test, model, sample size, and multiplicity correction. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` | Grouping: the tests that realize hypothesis testing. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → Z-Test | Test a mean or other parameter with a standard normal null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → T-Test | Test a mean with a $t$ null distribution and an estimated variance. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → Chi-Square Test | Test categorical frequencies or model fit with a chi-square null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → F-Test | Test variance ratios or model terms with an $F$ null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → Permutation Test | Build the null distribution by permuting observations or assignments. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Action` | Grouping: the primitive acts of the calculation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Action` → Specify Hypothesis Act | Fix $H_0$, $H_1$, the model, and the test statistic. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Action` → Choose Significance Level Act | Fix $\alpha$ before looking at the data. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Action` → Compute Test Statistic Act | Evaluate $T(x)$ on the sample. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Action` → Compute Tail Probability Act | Evaluate the probability of a statistic at least as extreme. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Action` → Compare To Threshold Act | Apply the golden rule $p \le \alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Action` → Report P-Value Act | Report the value with its test, model, and multiplicity context. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Principle` | Grouping: rules guiding the calculation and its use. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Principle` → Significance Principle | Reject $H_0$ at level $\alpha$ iff $p \le \alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Principle` → Severity Principle | Read the p-value as evidence only relative to a test with a good chance of detecting a false $H_0$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Principle` → Multiplicity Principle | Adjust $\alpha$ or the p-values for multiple comparisons. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → Statistical Significance Validation → `Principle` → Model-Checking Principle | Check the model assumptions before reading the p-value. |

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

> **Range.** A p-value lies in the interval \([0,1]\). It is calculated from the observed test statistic and its reference distribution under the null hypothesis. For a continuous test statistic and a valid p-value, the p-value follows a uniform distribution on \([0,1]\) under \(H_0\). For discrete test statistics, the p-value generally has a discrete distribution and is conservative: \(P(p \leq \alpha \mid H_0) \leq \alpha\).

> **Interpretation.** The p-value measures how extreme the observed test statistic is relative to its reference distribution under \(H_0\). A small p-value indicates that the observed statistic falls in a region that would be relatively unusual if the null hypothesis were true. It does not measure the probability that \(H_0\) is true, nor does it measure the probability that the observed data arose by chance.

> **Decision threshold.** The significance level \(\alpha\) is a threshold chosen before examining the results. Common choices are \(0.05\), \(0.01\), and \(0.001\), but these are conventions rather than universal rules. At a pre-specified significance level:
>
> - \(p \leq \alpha\): reject \(H_0\).
> - \(p > \alpha\): fail to reject \(H_0\).
>
> The threshold determines the decision rule; it does not change the observed p-value. Failing to reject \(H_0\) does not establish that it is true.

> **Statistical properties of the procedure.** The significance level controls the probability of rejecting \(H_0\) when it is true. For a composite null hypothesis with parameter space \(\Theta_0\), a test has level \(\alpha\) if
>
> \[
> \sup_{\theta \in \Theta_0}
> P_\theta(\text{reject } H_0) \leq \alpha.
> \]
>
> The power of the test at a particular alternative parameter value \(\theta_1\) is
>
> \[
> P_{\theta_1}(\text{reject } H_0).
> \]
>
> These properties describe the behavior of the testing procedure across repeated samples, rather than the interpretation of an individual p-value.

> **Reporting and communication.** Report the p-value alongside the test specification and, where relevant, an effect-size estimate and confidence interval. Statistical significance does not establish practical importance, and a p-value alone does not establish the truth of a hypothesis.

**Key distinction:** The p-value is a measure of extremeness relative to a null distribution; \(\alpha\) is the decision threshold; and the significance level and power describe the testing procedure's long-run behavior.

### What are the properties of a p-value?

| Property | Description |
| --- | --- |
| **Range** | \(p(x) \in [0,1]\): it is a probability computed under \(H_0\). |
| **Uniformity under a simple null** | For a continuous test statistic and a simple null, \(p(X) \sim U(0,1)\) under \(H_0\); hence \(P(p \le \alpha \mid H_0) = \alpha\) exactly. |
| **Level validity** | For a composite null, the supremum construction gives \(P(p \le \alpha \mid \theta) \le \alpha\) for every \(\theta \in \Theta_0\); with discrete statistics the test is conservative. |
| **Stochasticity** | Before the sample is drawn \(p(X)\) is a random variable with a null distribution; after, \(p(x)\) is a realized value. |
| **Monotonicity in extremeness** | For a fixed test, \(p\) decreases as the observed statistic becomes more extreme under the declared ordering. |
| **Sample-size dependence** | The null distribution of \(T\), and hence \(p\), changes with \(n\); at large \(n\) a trivial effect can produce a small p-value. |
| **Model dependence** | \(p\) depends on the model, the statistic, and the extremeness ordering, not on \(H_0\) alone; the same data can yield different p-values under different tests. |
| **Ordering dependence** | The one-sided / two-sided / likelihood-ratio convention fixes "at least as extreme" and therefore changes the number. |
| **Sensitivity to the sampling plan** | \(p\) is not valid under optional stopping or data-dependent sampling; the stopping rule is part of the test (unlike e-values). |
| **Not a property of \(H_0\)** | \(p\) is a property of the data relative to a test specification, not of the hypothesis. |

> The decomposition files the structural ones as `Constitutive Substrate` → `Property`; the table adds level validity, monotonicity, ordering dependence, and sensitivity to the sampling plan.

### What the P-Value Is Not?

> The p-value is **not**:

| Misinterpretation | Correct Statement |
| --- | --- |
| The probability that \(H_0\) is true | \(p(x) \neq P(H_0 \mid X)\). This would require a prior and Bayes' theorem. |
| The probability that the data arose by chance | \(p(x)\) is computed **under** \(H_0\); it is not the probability of \(H_0\). |
| The probability of rejecting \(H_0\) when it is true | That is \(\alpha\), not \(p\). \(\alpha\) is pre-specified; \(p\) is computed from the data. |
| A measure of effect size | A small p-value does not imply a large effect; with large \(n\), trivial effects can yield small p-values. |
| The probability of replication | \(p(x)\) is not \(P(\text{replication})\). Replication probabilities depend on power and the true effect size. |
| A measure of the truth of \(H_0\) | The p-value is a measure of **compatibility** with \(H_0\), not a measure of truth. |
| A property of \(H_0\) | The p-value is a property of the **data** (relative to a test specification), not of \(H_0\). |

> The p-value is a measure of compatibility with \(H_0\) under a declared test, nothing more.

### What does surprise even means here?

> ...

### Are p-values about subsets (samples) of populations, or observations?

> ...

### Should the statistics computed from these samples have low variance?

> ...

### What is the underlying `logic` aroud p-values?

> We have a model, a population, and samples drawn from that population. We compute a statistic for each sample and assume a theoretical sampling distribution that these statistics should follow under the model. We then compare the observed statistic with this theoretical distribution to assess how unusual it is.

> Note: We usually do not construct the empirical distribution either. Instead, we use the parameters of the theoretical distribution to calculate the tail probabilities.

> Unusualness means that the observed statistic falls in a region with a small probability under the theoretical distribution, resulting in a small p-value.

> This seems crazy: we are assuming a theoretical distribution, its parameters, and so on. The method seems quite ungrounded. Following the procedure is relatively easy, but justifying its assumptions is much harder. It almost feels like an oracle.

### Is the p-value computed from the distribution of \(T\) or from \(M_p\), which determines the distribution of \(T\)?

> **Note:** By \(M_p\), I mean the fitted model, not an estimator of its parameters.

> The p-value depends on the distribution of \(T\). However, this distribution is determined by the statistical procedures used to estimate the parameters of \(M_p\), not by the specific parameter values contained in \(M_p\).

### Which common tests produce p-values, and from which null distributions?

| Test | Test statistic | Null distribution | p-value |
| --- | --- | --- | --- |
| **Z-test** | $Z = (\bar{X} - \mu_0)/(\sigma/\sqrt{n})$ | standard normal | tail probability of $Z$ |
| **T-test** | $t = (\bar{X} - \mu_0)/(s/\sqrt{n})$ | $t$ with $n-1$ degrees of freedom | tail probability of $t$ |
| **Chi-square test** | $\chi^2 = \sum (O_i - E_i)^2 / E_i$ | chi-square with the appropriate degrees of freedom | upper-tail probability |
| **F-test (ANOVA)** | $F = MS_{\text{between}}/MS_{\text{within}}$ | $F$ with the appropriate degrees of freedom | upper-tail probability |
| **Permutation test** | any test statistic | permutation distribution under exchangeability | proportion of permuted statistics at least as extreme |

> The full procedure space — parametric, rank-based, exact, resampling, survival — and the assumptions each type carries are in [Statistical Hypothesis Testing](note.html?n=epistemica/validation/statistical-hypothesis-testing.md).

### Why Is Hypothesis Testing a Form of Model Validation?

> A model is a representation of a population. It has parameters, and we can define properties of those parameters.

> A hypothesis is a statement about the model's parameters, a property of those parameters, or the parameters themselves. Hence, when we test a hypothesis, we are validating a claim about the model.

> The problem lies in how the term *model* is used in statistics. It often refers to, or is conflated with, a class of procedures or methods rather than a concrete epistemic artifact: a representation of some aspect of reality that can be evaluated and validated.

### What are the alternatives and complements to the p-value?

> - **Confidence intervals** — a range of plausible parameter values; the interval is the estimate, the p-value is a compatibility summary.
> - **Effect sizes** — Cohen's $d$, odds ratios, risk differences, $R^2$; a small p-value does not imply a large effect.
> - **Bayes factors and posterior probabilities** — evidence and belief updating with an explicit prior and loss.
> - **E-values** — a test martingale that remains valid under optional stopping and multiplicity.
> - **Severity** — the probability that a test would have detected a false $H_0$; a p-value is evidence only relative to a severe test.
> - **Replication and pre-registration** — the design features that make a significance claim credible.
> - **Power analysis** — the probability of detecting an effect of a given size before the data are collected.

### What is a significance-level (p-value) framework?

> A framework is the **technical formulation** that fixes how a p-value is read. It is not a theory of inference — it claims no mechanism — and it is not the calculation either: the same tail probability can be produced under any of them. What a framework fixes is the bundle of conventions around the quantity:

> 1. the **reference model** against which extremeness is judged — null distribution, null-and-alternative pair, or posterior predictive;
> 2. the **quantity** computed and reported — tail probability, rejection indicator, Bayesian p-value, Bayes factor;
> 3. the **role of $\alpha$** — reporting grade, pre-set error rate, decision threshold, or nothing;
> 4. the **licensed output** — graded evidence, accept/reject, "significant", belief update;
> 5. the **evidence claim** the number is allowed to support;
> 6. the **error guarantee** it carries.

> The quantity is framework-neutral; the reading is not. The four formulations are peers, not stages: each is a complete way of organizing the validation, with its own reference model and its own licensed output.

| Formulation | Reference model | Quantity | Role of $\alpha$ | Licensed output | Error guarantee |
| --- | --- | --- | --- | --- | --- |
| **Fisherian** | null distribution only | tail probability $p$ | reporting grade ($0.05$, $0.01$) | graded evidence against $H_0$ | none — no alternative, no power |
| **Neyman–Pearson** | null and alternative | critical region, $p$ instrumental | pre-set Type I rate, with power $\beta$ | accept or reject $H_0$ | Type I and Type II rates, power |
| **NHST** | null only, with a threshold applied | Fisher's $p$ | decision threshold | "significant / not significant" | nominal $\alpha$ only, often not attained in practice |
| **Bayesian** | posterior predictive | Bayesian p-value, Bayes factor | replaced by a posterior or loss threshold | posterior belief and evidence ratio | calibration to the declared prior |

> The same number reads differently under each. Take $p = 0.03$: moderate evidence against $H_0$ (Fisherian); a rejection at $\alpha = 0.05$ with a known Type I rate (Neyman–Pearson); a publishable "significant" result (NHST); and, for the Bayesian, a posterior-predictive check that may or may not flag the model — the quantity of interest there is $P(H_0 \mid x)$ or the Bayes factor, not the tail probability.

> The note keeps the quantity and the calculation framework-neutral: the decomposition files the four formulations under `Organization` → Statistical Significance Validation → Formulation, and where a reading is required it uses severity — a p-value is evidence only relative to a test with a good chance of detecting a false $H_0$ — while treating $\alpha$ as a decision convention, not a property of the data.



## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [Statistical Hypothesis Testing](note.html?n=epistemica/validation/statistical-hypothesis-testing.md)
- [Validation](note.html?n=epistemica/validation/validation.md)
- [Calibration](note.html?n=epistemica/validation/calibration.md)
- [E-value](note.html?n=epistemica/validation/e-value.md)
- [EES atlas](data/epistemica/ees.html)
- [P-Value Atlas](data/epistemica/validation/atlas/pvalue.html) — the null distributions, their tail formulas, and a simulation lab
- Goodman, S. (2008). A dirty dozen: Twelve p-value misconceptions. *Seminars in Hematology*, 45(3), 135–140.
- Cohen, J. (1994). The earth is round (p < .05). *American Psychologist*, 49(12), 997–1003.
- Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine*, 2(8), e124.
- Wasserstein, R. L., & Lazar, N. A. (2016). The ASA statement on p-values: Context, process, and purpose. *The American Statistician*, 70(2), 129–133.
- Wasserstein, R. L., Schirm, A. L., & Lazar, N. A. (2019). Moving to a world beyond "p < 0.05". *The American Statistician*, 73(sup1), 1–19.
- Greenland, S., Senn, S. J., Rothman, K. J., Carlin, J. B., Poole, C., Goodman, S. N., & Altman, D. G. (2016). Statistical tests, P values, confidence intervals, and power: A guide to misinterpretations. *European Journal of Epidemiology*, 31(4), 337–350.
- Mayo, D. G. (2018). *Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars*. Cambridge University Press.
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver and Boyd.
- Neyman, J., & Pearson, E. S. (1933). On the problem of the most efficient tests of statistical hypotheses. *Philosophical Transactions of the Royal Society of London. Series A*, 231(694–706), 289–337.
- Jeffreys, H. (1939). *Theory of Probability*. Oxford University Press.
- Meng, X.-L. (1994). Posterior predictive p-values. *The Annals of Statistics*, 22(3), 1142–1160.
- Kass, R. E., & Raftery, A. E. (1995). Bayes factors. *Journal of the American Statistical Association*, 90(430), 773–795.
- Gelman, A. (2013). P values and statistical practice. *Epidemiology*, 24(1), 69–72.
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
- [P-values and significance tests](https://www.khanacademy.org/math/ap-statistics/xfb5d8e68:inference-categorical-proportions/idea-significance-tests/v/p-values-and-significance-tests)
- [Power](https://en.wikipedia.org/wiki/Power_(statistics))
- [Lies, Damn Lies, and Statistics... P-Hacking](https://www.youtube.com/watch?v=Et9pORQHR2A)
- [Fisher's exact test](https://en.wikipedia.org/wiki/Fisher%27s_exact_test)


