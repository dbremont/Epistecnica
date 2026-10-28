---
tags: [validation, model-evaluation, statistics]
qa:
  - Why is "the model fits" not a conclusion that a goodness-of-fit test can deliver?
  - What exactly does $p > \alpha$ establish when the test has low power?
  - Why does estimating $m$ parameters from the same data cost $m$ degrees of freedom — and when does that correction fail?
  - When is the Kolmogorov–Smirnov test with fitted parameters conservative, and what replaces it (Lilliefors, parametric bootstrap)?
  - Why does the Pearson $\chi^2$ statistic need expected counts of at least five, and what do you do when they are smaller?
  - How does the choice of binning change the $\chi^2$ p-value for the same data?
  - How do goodness of fit, calibration, and predictive validation differ, and which question does each answer?
  - Why is comparing AIC/BIC across candidate models not a goodness-of-fit test?
  - How does power grow with $n$, and why does that make a significant $\chi^2$ uninformative about the size of the misspecification?
---

# Goodness of Fit

> **Goodness of fit** is the assessment of how closely a fitted or specified model reproduces the observed data — measured as a discrepancy $D(F_n, F_\theta)$ between the empirical distribution $F_n$ of the sample and the distribution $F_\theta$ the model implies, judged against the sampling distribution $D$ would have if the model were true.

> A goodness-of-fit judgement is a statement about a *model relative to a sample*, not about reality. Rejecting the model says the data are improbable under it; failing to reject says only that this test, at this sample size, did not detect the misspecification it is powered to detect.

> Goodness of fit is one activity inside [Validation](note.html?n=epistemica/validation/validation.md) — the model-checking step — and must be kept apart from **calibration** (fixing parameters against a reference), from **model selection** (ranking candidates by a penalized criterion), and from **predictive validation** (judging forecasts on held-out data).

> See the [Goodness-of-Fit Atlas](data/epistemica/validation/atlas/gof.html) — the discrepancy measures, their null distributions, and a simulation lab that draws the fit, the null cloud, the power curve, and the p-value calibration.

## Formulation

### What is this epistemic instance?

> The instance is the organized practice of **checking a distributional model against data**: given observations $x_1, \dots, x_n$ and a model $F_\theta$, compute a discrepancy statistic, obtain its distribution under the model, and read how extreme the observed discrepancy is.

> The formal core is a triple — a discrepancy, a reference model, and a null distribution:

$$D_{\mathrm{obs}} = D\big(F_n,\; F_{\hat\theta}\big), \qquad p = \Pr_{\theta \in H_0}\big(D \ge D_{\mathrm{obs}}\big).$$

> The empirical distribution function $F_n(t) = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}\{x_i \le t\}$ carries everything the sample says about the shape; the model contributes $F_\theta$; the discrepancy compresses the difference between the two into one number.

> Three families of discrepancy dominate practice:

| Family | Statistic | What it weights |
| --- | --- | --- |
| **Quadratic / binned** | Pearson $\chi^2 = \sum_k \frac{(O_k - E_k)^2}{E_k}$, likelihood-ratio $G = 2\sum_k O_k \ln\frac{O_k}{E_k}$ | Departures in cell frequencies; a few large deviations dominate. |
| **Supremum / CDF** | Kolmogorov–Smirnov $D_n = \sup_t \lvert F_n(t) - F_\theta(t)\rvert$ | The single worst vertical gap; sensitive to location and shape shifts near the bulk. |
| **Weighted $L^2$ / CDF** | Cramér–von Mises $\omega^2 = n\int (F_n - F_\theta)^2 \, dF_\theta$; Anderson–Darling $A^2 = n\int \frac{(F_n - F_\theta)^2}{F_\theta(1-F_\theta)}\, dF_\theta$ | The whole CDF curve; Anderson–Darling up-weights the tails. |

> The reference model is where the difficulty lives. If $\theta$ is **fully specified** before seeing the data, the null distributions are the classical ones ($\chi^2$ with $k-1$ degrees of freedom, the Kolmogorov law, the Cramér–von Mises and Anderson–Darling laws). If $\theta$ is **estimated from the same sample** — the ordinary case — the statistic is stochastically smaller, the classical null is wrong, and the correction is either a degrees-of-freedom penalty ($k - 1 - m$ for $m$ estimated parameters) or a resampling null (parametric bootstrap, Lilliefors tables).

> The output is not a verdict on the model but a **compatibility reading** with an explicit direction of error: the test controls the probability of rejecting a true model at $\alpha$, and its power against the misspecifications it is meant to catch is a separate, usually unreported, quantity.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Operation`** — goodness of fit is an organized **Model Validation** method, an `Organization` → `Method` under `Statistical Inference`, realized by concrete procedures (Pearson, Kolmogorov–Smirnov, Cramér–von Mises, Anderson–Darling) and acts (estimate, bin, compute, simulate, compare, report).

> Secondary type: **`Epistemic Representation`** — the discrepancy itself is a `Representation Element` in a **Quantitative Representation** system: a statistical quantity with a null distribution.

> Tertiary type: **`Epistemic Evaluation`** — the judgement it issues is an assessment under `Epistemic Standard` ($\alpha$, pre-specification) and `Epistemic Criterion` (discrepancy, power), with its characteristic `Error` (a true model rejected, a false model retained) and its `Feedback` (revise the model).

> The decomposition roots all three under the shared `Epistemic Element` genus, read as **elements of inquiry**: the branches are inquiry branches — the operation that checks, the quantity it computes, the evaluation it issues — not segments of parsed reality.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in four ways the decomposition keeps apart.

> **First, aspect.** Goodness of fit names a *practice*, a *statistic*, a *test*, and a *verdict* — "the fit is good", "the $\chi^2$ goodness-of-fit test", "$D_n = 0.08$", "the model fits". Collapsing them makes the term equivocal. The note keeps the operation, the representation, and the evaluation as separate branches.

> **Second, reference model.** The same statistic means different things with $\theta$ fixed a priori, with $\theta$ estimated from the data, and with $\theta$ estimated from *other* data. The first two have different null distributions; the third is a genuine out-of-sample check. "Goodness of fit" without a declared estimation regime is underdetermined.

> **Third, target of the judgement.** A distributional fit check ("does the data look like this law?") is not a regression fit check ("do the residuals behave?") and not a predictive check ("do the forecasts hold up?"). They use different statistics, different nulls, and different failure modes.

> **Fourth, verdict polarity.** Rejection is informative, non-rejection is not. The test is a *falsification device with bounded power*: $p > \alpha$ is compatible with a model that is badly wrong in a direction the statistic does not see, at a sample size too small to see it.

> The ambiguity is resolved by declaring the statistic, the estimation regime, the null distribution, the sample size, and $\alpha$ — and by refusing to read non-rejection as evidence of fit.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: the table decomposes the goodness-of-fit instance under three kind branches — the operation (the practice and its procedures), the representation (the discrepancy and its substrate), and the evaluation (the standards and errors it issues). Stopping rule: a row is terminal when it names a concrete statistic, model component, procedure, act, principle, standard, criterion, or error. Identity: every path is unique; instance rows are Title Case; type groupings are backticked; no type terminates a branch. Typing: the root is `Epistemic Element`; the branches are `Epistemic Operation`, `Epistemic Representation`, and `Epistemic Evaluation`, read as elements of inquiry.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` → `Epistemic Operation` | Grouping: goodness of fit read as an organized operation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` | Grouping: the organization of the model-checking operation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` | Grouping: generalized ways of performing the check. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation | The class of operations that infer from sample to model under a statistical framework. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference | Inference from sample to model under an assumed distributional family. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation | The method that judges whether a model is adequate for its stated purpose. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice | The distributional model-checking step of validation: discrepancy, null distribution, compatibility reading. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Method` | Grouping: the discrepancy measures that realize the check. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Method` → Pearson Chi-Square Test | Binned quadratic discrepancy against expected cell counts. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Method` → Likelihood-Ratio G Test | Binned deviance $G = 2\sum O \ln(O/E)$, asymptotically equivalent to Pearson. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Method` → Kolmogorov–Smirnov Test | Supremum distance between empirical and model CDFs. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Method` → Cramér–von Mises Test | Weighted $L^2$ distance between empirical and model CDFs. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Method` → Anderson–Darling Test | Tail-weighted $L^2$ distance between empirical and model CDFs. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Method` → Chi-Square Independence Test | The binned statistic applied to contingency tables rather than to a fitted law. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Method` → Residual Diagnostic | The regression counterpart: assess residual structure rather than a marginal law. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Procedure` | Grouping: ordered routines of the check. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Procedure` → Distributional Fit Check | Fit a law to a sample, compute a discrepancy, read its null distribution. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Procedure` → Binned Fit Check | Bin the support, compare observed and expected counts, compute Pearson or $G$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Procedure` → Regression Fit Check | Compare residual behaviour with the assumptions of the linear model. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Model Validation → Goodness of Fit Practice → `Procedure` → Parametric Bootstrap Check | Re-estimate the model on simulated samples to build the null of the discrepancy. |
| `Epistemic Element` → `Epistemic Operation` → `Action` | Grouping: the primitive acts of the check. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Specify Reference Model Act | Fix the family, the estimation regime, and the parameter space before the check. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Estimate Parameters Act | Obtain $\hat\theta$ by maximum likelihood or matching, recording $m$. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Bin Support Act | Choose cell edges or counts, merging sparse tails. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Compute Discrepancy Act | Evaluate $D_{\mathrm{obs}}$ on the sample. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Obtain Null Distribution Act | Use the classical law, a corrected table, or a resampled null. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Compare To Threshold Act | Compare $p$ with the pre-specified $\alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Report Fit Act | Report the statistic, null, $n$, $m$, binning rule, and power context. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` | Grouping: rules governing the check. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Degrees-of-Freedom Principle | Estimating $m$ parameters costs $m$ degrees of freedom: $k-1-m$ for binned statistics. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Expected-Count Principle | Binned asymptotics require expected counts of roughly five or more; merge sparse cells. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Estimation-Aware Null Principle | With estimated parameters the classical null is invalid; use Lilliefors tables or a parametric bootstrap. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Pre-Specification Principle | The statistic, bins, and $\alpha$ are fixed before the data are seen. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Power Principle | Non-rejection is read only against the misspecifications the test can detect at this $n$. |
| `Epistemic Element` → `Epistemic Representation` | Grouping: the discrepancy read as a representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` | Grouping: the quantitative sign system in which the discrepancy is expressed. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation | The system of quantities, scales, and numerical comparison. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` | Grouping: the combinable constituents of the representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Goodness-of-Fit Statistic | The scalar discrepancy $D(F_n, F_\theta)$ that orders samples by misfit. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Goodness-of-Fit Statistic → `Representation Element` | Grouping: the realized discrepancies. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Goodness-of-Fit Statistic → `Representation Element` → Pearson Chi-Square Statistic | $\sum_k (O_k - E_k)^2 / E_k$ over cells. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Goodness-of-Fit Statistic → `Representation Element` → Likelihood-Ratio Statistic | $G = 2\sum_k O_k \ln(O_k/E_k)$, the binned deviance. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Goodness-of-Fit Statistic → `Representation Element` → Kolmogorov Distance | $\sup_t \lvert F_n(t) - F_\theta(t)\rvert$. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Goodness-of-Fit Statistic → `Representation Element` → Cramér–von Mises Statistic | Weighted integral of the squared CDF gap. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Goodness-of-Fit Statistic → `Representation Element` → Anderson–Darling Statistic | Tail-weighted integral of the squared CDF gap. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Fit P-Value | The tail probability of the discrepancy under the reference model. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` | Grouping: the rules and structures constituting the representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Empirical Distribution Function | $F_n$, the sample's own CDF; the data side of the comparison. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Fitted Model Distribution | $F_{\hat\theta}$, the model side of the comparison. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Null Distribution | The law of $D$ when the reference model holds. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Degrees of Freedom | The parameter $k-1-m$ fixing the asymptotic $\chi^2$ reference. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Binning Rule | The cell edges and merge rule that turn a continuous sample into counts. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` | Grouping: properties of the discrepancy representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Non-Negativity | Every discrepancy is non-negative and zero only at exact agreement. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Null Distribution Dependence | The reference law depends on the statistic, the estimation regime, and the binning. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Estimation Shrinkage | Estimated parameters shrink $D$, making the classical null conservative. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Sample-Size Dependence | $D$ grows with $n$ under a fixed alternative; power rises with $n$. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Discreteness Conservativeness | Discrete statistics produce p-values that over-cover. |
| `Epistemic Element` → `Epistemic Evaluation` | Grouping: the judgement the check issues. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: standards under which the fit is judged. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Standard` → Significance Standard | Reject the model at level $\alpha$ when $p \le \alpha$. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Standard` → Reference Model Standard | The family, estimation regime, and binning must be declared for the reading to be determinate. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Criterion` | Grouping: the evaluated properties. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Criterion` → Discrepancy Criterion | The size of $D_{\mathrm{obs}}$ relative to its null distribution. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Criterion` → Power Criterion | The probability of detecting the misspecifications the test targets. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Criterion` → Effect Size Criterion | The magnitude of the misfit, which the p-value does not report. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Constraint` | Grouping: limits on the judgement. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Constraint` → Sample-Size Limit | Small samples cannot detect real misspecification; large samples detect trivial misspecification. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Constraint` → Bin-Count Limit | Sparse cells invalidate the $\chi^2$ asymptotics. |
| `Epistemic Element` → `Epistemic Evaluation` → `Epistemic Constraint` → Alternative Specificity Limit | A test has power against some alternatives and none against others. |
| `Epistemic Element` → `Epistemic Evaluation` → `Error` | Grouping: the errors the judgement can make. |
| `Epistemic Element` → `Epistemic Evaluation` → `Error` → True Model Rejection | Type I error: a correct model rejected at rate $\alpha$. |
| `Epistemic Element` → `Epistemic Evaluation` → `Error` → Misspecification Acceptance | Type II error: a wrong model retained because the test lacked power. |
| `Epistemic Element` → `Epistemic Evaluation` → `Error` → Binning Artefact | A rejection produced by the cell choice rather than by the model. |
| `Epistemic Element` → `Epistemic Evaluation` → `Feedback` | Grouping: the judgement returned into modelling. |
| `Epistemic Element` → `Epistemic Evaluation` → `Feedback` → Model Revision | Respecify the family or the covariates after a rejection. |
| `Epistemic Element` → `Epistemic Evaluation` → `Feedback` → Power Reassessment | Recompute the detectable effect after a non-rejection. |
| `Epistemic Element` → `Epistemic Evaluation` → `Feedback` → Out-of-Sample Check | Escalate from fit to predictive validation on held-out data. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The note distinguishes goodness of fit from calibration, model selection, and predictive validation, and separates the practice, the statistic, and the verdict. |
| **Definitional Clarity** | Partial | The formal core $D(F_n, F_\theta)$ is clear, but the term is used for binned tests, CDF distances, residual diagnostics, and informal visual checks; the definition is only determinate once the statistic and the estimation regime are named. |
| **Conceptual Determinacy** | Partial | Which instances qualify depends on the reference model (fixed vs estimated), on the binning rule, and on the statistic's sensitivity profile; borderline cases (a non-significant $\chi^2$ with $n = 12$) have no stable classification. |
| **Internal Consistency** | Pass | The practice, the representation, and the evaluation branches agree: the null distribution belongs to the declared reference model, the degrees-of-freedom penalty matches the estimation act, and the error branch matches the decision rule. |
| **Representational Adequacy** | Partial | It represents compatibility of a sample with a model, not the truth of the model, the size of the misfit, or the model's predictive performance; $\chi^2$ and KS weight different features, and neither represents calibration. |
| **Purpose Adequacy** | Partial | Adequate as a falsification device with declared power; inadequate as evidence *for* a model, as a selection criterion, or as a substitute for out-of-sample prediction. The complements are effect sizes, power analysis, calibration curves, and held-out validation. |

## QA

### Why is "the model fits" not a conclusion that a goodness-of-fit test can deliver?

> A goodness-of-fit test has a point null — the data are drawn from $F_\theta$ — and a test can only reject a point null or fail to reject it. Failure to reject is compatible with every alternative against which the test has low power, and with every alternative the statistic is blind to (a KS test is nearly blind to a shift in the far tail; $\chi^2$ is blind to reorderings that preserve cell counts).

> The correct reading of $p > \alpha$ is: *this test, with this $n$, did not detect a discrepancy of the kind it is sensitive to*. It is not a certificate of fit. Models are never confirmed by a non-significant test; they survive it.

### What exactly does $p > \alpha$ establish when the test has low power?

> It establishes one thing only: the observed discrepancy falls inside the non-rejection region the test fixes at $1 - \alpha$. That region is a statement about the statistic, not about the model — every alternative whose typical discrepancy at this $n$ stays below the critical value is inside it too.

> Power is the quantity that makes the reading legible. For a fixed alternative, the rejection probability is $\pi(\theta) = \Pr_\theta(D \ge c_\alpha)$, and at small $n$ it can sit near $\alpha$ even for a grossly wrong model: with $n = 20$ and a Kolmogorov test against a normal fitted from the data, a sample contaminated by a fifth is detected only about a quarter of the time. The non-significant $p$ then carries almost no information — it is the expected outcome under both hypotheses.

> What the report owes the reader is therefore the pair: the discrepancy with its null, and the detectable-effect size at this $n$ (equivalently, the power curve against the alternatives of interest). A non-rejection without a power statement is a test that could not have failed.

### Why does estimating $m$ parameters from the same data cost $m$ degrees of freedom — and when does that correction fail?

> Estimating parameters lets the model move toward the data, so the fitted distribution is closer to $F_n$ than a fixed distribution would be. Under the null the Pearson statistic then behaves like a $\chi^2$ with fewer degrees of freedom: for $k$ bins and $m$ estimated parameters the reference is $\chi^2_{k-1-m}$.

> The correction is a local, asymptotic linearization: it assumes the estimator is efficient and the model is regular (smooth in $\theta$, parameters not on the boundary, no parameters identified only by the binning). It fails for non-regular models (support depending on a parameter, mixture components, boundary parameters), where the null is a mixture of $\chi^2$ laws or must be simulated. When in doubt, the parametric bootstrap replaces the correction entirely.

### When is the Kolmogorov–Smirnov test with fitted parameters conservative, and what replaces it?

> With $\theta$ estimated from the sample, $D_n$ is stochastically smaller than under the fully specified null, so the classical Kolmogorov critical values over-reject far less often than $\alpha$ — the test becomes conservative and loses power. Lilliefors (1967) computed corrected critical values for the normal and exponential families; for other families the standard remedy is a parametric bootstrap: simulate from $F_{\hat\theta}$, re-estimate on each simulated sample, recompute $D$, and read the observed value against that cloud.

> The Anderson–Darling statistic has the same problem, with published correction tables for a few families (normal, exponential, Weibull, gamma, logistic) and bootstrap elsewhere.

### Why does the Pearson $\chi^2$ statistic need expected counts of at least five, and what happens otherwise?

> The $\chi^2_{k-1-m}$ reference comes from a multivariate normal approximation to the multinomial cell counts, which requires each expected count to be large enough for the normal approximation to hold. The conventional rule of thumb is $E_k \ge 5$ (some texts say 1 is tolerable if few cells violate it). With smaller counts the statistic's distribution is stochastically larger than $\chi^2$, so p-values are wrong in the anti-conservative direction.

> Remedies: merge adjacent cells until the rule holds (costing degrees of freedom), use an exact multinomial test, or use a Monte Carlo null. For $2\times2$ tables, Yates' continuity correction is the classical patch.

### How does the choice of binning change the $\chi^2$ p-value for the same data?

> Binning is a modelling decision: cell edges determine both $D_{\mathrm{obs}}$ and the degrees of freedom. Coarse bins discard the shape within a cell and lose power against local deviations; fine bins create sparse cells that break the asymptotics. Shifting edges moves observations between cells and changes the statistic for identical data.

> This is why a $\chi^2$ p-value is only reproducible when the binning rule is reported, and why CDF-based statistics (KS, Cramér–von Mises, Anderson–Darling) are preferred when the alternative is a smooth shape difference rather than a specific cell pattern.

### How do goodness of fit, calibration, and predictive validation differ?

| Question | Practice | Typical instrument |
| --- | --- | --- |
| Does the sample look like this law? | **Goodness of fit** | $\chi^2$, KS, Cramér–von Mises, Anderson–Darling |
| Do the stated probabilities match observed frequencies? | **Calibration** | Reliability diagrams, proper scoring rules, coverage checks |
| Do the predictions hold on data the model has not seen? | **Predictive validation** | Cross-validation, held-out error, posterior predictive checks |

> A model can pass a goodness-of-fit test and be badly calibrated (the law is right, the probabilities are assigned through a distorted map), and it can be well calibrated on the training distribution while failing out of sample. The three are complementary, not interchangeable.

### Why is comparing AIC/BIC across candidate models not a goodness-of-fit test?

> AIC and BIC are *relative* criteria: they rank models within a candidate set by penalized likelihood, and they are defined up to an additive constant that cancels only in comparisons. They say nothing about whether the best candidate fits — the whole set can be wrong.

> A goodness-of-fit test has an absolute null (this model) and can reject it. The two are used together: fit checks screen a model against the data, information criteria choose among survivors. Reporting a "best AIC" as evidence of fit is a category error.

### How does power grow with $n$, and why does that make a significant $\chi^2$ uninformative about the size of the misspecification?

> Under a fixed alternative, the non-centrality of the $\chi^2$ grows linearly in $n$, so for any fixed departure the rejection probability tends to one as $n \to \infty$. Conversely, at small $n$ a large departure can go undetected.

> A significant result at $n = 10^6$ may correspond to a misfit far too small to matter for the intended use, and a non-significant result at $n = 20$ may hide a gross one. This is why the report needs the effect size and the detectable-effect calculation alongside the p-value — the same lesson as in [Statistical Hypothesis Testing](note.html?n=epistemica/validation/statistical-hypothesis-testing.md), applied to model checking.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- Pearson, K. (1900). On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, 50*(302), 157–175. [https://doi.org/10.1080/14786440009463897](https://doi.org/10.1080/14786440009463897)
- Cramér, H. (1928). On the composition of elementary errors. *Scandinavian Actuarial Journal, 1928*(1), 13–74. [https://doi.org/10.1080/03461238.1928.10416862](https://doi.org/10.1080/03461238.1928.10416862)
- von Mises, R. (1931). *Wahrscheinlichkeitsrechnung und ihre Anwendung in der Statistik und theoretischen Physik*. Deuticke.
- Kolmogorov, A. N. (1933). Sulla determinazione empirica di una legge di distribuzione. *Giornale dell'Istituto Italiano degli Attuari, 4*, 83–91.
- Smirnov, N. V. (1948). Table for estimating the goodness of fit of empirical distributions. *The Annals of Mathematical Statistics, 19*(2), 279–281. [https://doi.org/10.1214/aoms/1177730256](https://doi.org/10.1214/aoms/1177730256)
- Anderson, T. W., & Darling, D. A. (1952). Asymptotic theory of certain "goodness of fit" criteria based on stochastic processes. *The Annals of Mathematical Statistics, 23*(2), 193–212. [https://doi.org/10.1214/aoms/1177729437](https://doi.org/10.1214/aoms/1177729437)
- Lilliefors, H. W. (1967). On the Kolmogorov–Smirnov test for normality with mean and variance unknown. *Journal of the American Statistical Association, 62*(318), 399–402. [https://doi.org/10.1080/01621459.1967.10482916](https://doi.org/10.1080/01621459.1967.10482916)
- Stephens, M. A. (1974). EDF statistics for goodness of fit and some comparisons. *Journal of the American Statistical Association, 69*(347), 730–737. [https://doi.org/10.1080/01621459.1974.10480196](https://doi.org/10.1080/01621459.1974.10480196)
- D'Agostino, R. B., & Stephens, M. A. (Eds.). (1986). *Goodness-of-Fit Techniques*. Marcel Dekker.
- Massey, F. J. (1951). The Kolmogorov–Smirnov test for goodness of fit. *Journal of the American Statistical Association, 46*(253), 68–78. [https://doi.org/10.1080/01621459.1951.10500769](https://doi.org/10.1080/01621459.1951.10500769)
- Cochran, W. G. (1952). The $\chi^2$ test of goodness of fit. *The Annals of Mathematical Statistics, 23*(3), 315–345. [https://doi.org/10.1214/aoms/1177729380](https://doi.org/10.1214/aoms/1177729380)
- [Goodness of fit](https://en.wikipedia.org/wiki/Goodness_of_fit)
- [Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)
- [Anderson–Darling test](https://en.wikipedia.org/wiki/Anderson%E2%80%93Darling_test)
- [Cramér–von Mises criterion](https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93von_Mises_criterion)
- [Lilliefors test](https://en.wikipedia.org/wiki/Lilliefors_test)
- [SciPy: `scipy.stats.goodness_of_fit`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.goodness_of_fit.html)
