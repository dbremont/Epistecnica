---
tags: [model-evaluation, statistics]
qa:
  - What is an e-value, and how does it differ from a p-value?
  - Why does rejecting at E ≥ 1/α control Type I error, and what does an e-process add?
  - How are e-values constructed for simple and composite nulls?
  - How do e-values combine, and how does e-BH control the false discovery rate?
  - What is e-power/GRO, and why maximize E_Q[log E]?
  - What are the common misinterpretations and limits of e-values?
---

# E-Value

> The **e-value** is a statistical quantity: a nonnegative random variable $E(Y)$ whose expectation under every distribution in the null hypothesis is at most one,
>
> $$\mathbb{E}_P[E] \le 1 \quad \text{for all } P \in H_0.$$
>
> Larger realized values are evidence against $H_0$; the value itself is not a probability. An e-value below one has no generally accepted evidence-for-$H_0$ interpretation.

> The note reads the e-value under two hierarchies — as a **representation** (a statistical quantity in a quantitative representation system) and as an **operation** (the calculation that produces it within hypothesis testing). Both are rooted in the shared `Epistemic Element` genus.

## Formulation

### What is this epistemic instance?

> An **e-variable** is a nonnegative random variable $E(Y)$ defined on the sample space of a statistical model, with
>
> $$\mathbb{E}_P[E] \le 1 \quad \text{for every } P \in H_0.$$
>
> An **e-value** is a realized value $e = E(y)$ of an e-variable. The term is often used for both the random variable and its realization; the note distinguishes them when the distinction matters. The e-value is allowed to be infinite in the extended-real formulation; in practice it is a finite nonnegative number.

> **Rejection rule.** For a pre-specified level $\alpha \in (0,1)$, reject $H_0$ when
>
> $$E \ge \frac{1}{\alpha}.$$
>
> Markov's inequality gives
>
> $$\mathbb{P}_{H_0}\left(E \ge \frac{1}{\alpha}\right) \le \alpha\,\mathbb{E}_{H_0}[E] \le \alpha.$$
>
> The rule is a valid level-$\alpha$ test. It is usually conservative: the null probability of crossing $1/\alpha$ can be much smaller than $\alpha$.

> **Relation to p-values.** The reciprocal
>
> $$p' = \min\left(1, \frac{1}{E}\right)$$
>
> is a p-value, the **e-to-p calibration**. The converse is not the identity: $1/p$ is not generally an e-value. A p-to-e calibrator is a decreasing function $f$ with $\int_0^1 f(p)\,\mathrm{d}p \le 1$; the family $f_\kappa(p) = \kappa p^{\kappa-1}$, $\kappa \in (0,1)$, is a standard example. Calibration from p-values to e-values therefore loses information and can be far from growth-optimal.

> **Likelihood ratios.** If $H_0 = \{P_0\}$ is simple and $Q$ is an alternative with density $q$ with respect to $P_0$, then
>
> $$E = \frac{q(Y)}{p_0(Y)}$$
>
> is an e-value. Conversely, for a simple null, every e-variable is a likelihood ratio for some alternative distribution. A Bayes factor is an e-value when the null is simple and the prior on the alternative is a proper probability distribution; a generalized likelihood ratio is not generally an e-value for a composite null.

> **E-processes.** A sequence $(E_n)_{n \ge 0}$, adapted to a filtration $(\mathcal{F}_n)$, is an **e-process** for $H_0$ if for every stopping time $\tau$,
>
> $$\mathbb{E}_P[E_\tau] \le 1 \quad \text{for every } P \in H_0.$$
>
> Equivalently, it is a nonnegative supermartingale with initial expectation at most one under each null distribution. A **test martingale** is the special case of a nonnegative martingale with expectation one. Ville's inequality gives
>
> $$\mathbb{P}_{H_0}\left(\sup_{n \ge 0} E_n \ge \frac{1}{\alpha}\right) \le \alpha,$$
>
> so the e-process controls Type I error uniformly over time, including at data-dependent stopping times. This is the **anytime-valid** property.

> **Evidence, not truth.** An e-value measures evidence against $H_0$ on a multiplicative scale. It is not the probability that $H_0$ is false, not a posterior odds, not a likelihood of the data, not an effect size, and not a Bayes factor in general. The multiplicative reading is literal: independent e-values combine by multiplication, and arbitrary e-values combine by weighted averaging.

### What epistemic element type does this epistemic instance belong to?

> Primary type: **`Epistemic Representation`** — the e-value is a `Representation Element` in a **Quantitative Representation** system, read as a **Statistical Quantity**. Secondary type: **`Epistemic Operation`** — the e-value calculation is a **Statistical Operation** under **Statistical Inference** → **Hypothesis Testing**. The decomposition table roots both under the shared `Epistemic Element` genus, as the two hierarchies do.

> The two kind chains are:
>
> ```text
> Epistemic Element
> └── Epistemic Representation
>     └── Quantitative Representation
>         └── Statistical Quantity
>             └── E-Value
> ```
>
> ```text
> Epistemic Element
> └── Epistemic Operation
>     └── Statistical Operation
>         └── Statistical Inference
>             └── Hypothesis Testing
>                 └── E-Value Calculation
> ```

> The table inserts the guide's licensed type groupings between the instance segments — `Representational System`, `Representation Element`, `Constitutive Substrate`, and `Property` on the representation branch; `Organization`, `Method`, `Procedure`, `Action`, and `Principle` on the operation branch. The instance chain is preserved; the groupings are what let each row be typed.

> Both branches are read as elements of inquiry rather than as elements of reality. The target — population, sample, observable — is ontic and is not part of either branch. The e-value is not a feature of observer-independent reality; it is a representation of a sample relative to a null model and a construction.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in five ways that the decomposition keeps apart.

> **First, aspect.** The e-value is a quantity, the e-value calculation is an operation, the rule $E \ge 1/\alpha$ is a decision rule, and "evidence" is a role the quantity plays relative to a construction. Collapsing them into one type makes "e-value" equivocal.

> **Second, object.** The e-variable is the random variable; the e-value is its realization; the e-process is a sequence of e-variables; the test martingale is a special e-process; the safe test is a testing method built from them. The note keeps the quantity, the process, and the test apart.

> **Third, construction.** The same data can yield different e-values from a likelihood ratio, a mixture, universal inference, or a betting strategy. An e-value is determinate relative to a declared null, alternative or prior, construction, and stopping rule — not absolutely.

> **Fourth, evidence versus decision.** The e-value is a continuous evidence scale; the threshold $1/\alpha$ is a decision convention. A large e-value is evidence against $H_0$ only relative to a construction with a meaningful alternative; a small e-value is not evidence for $H_0$.

> **Fifth, relation to other evidence scales.** A p-value is a tail probability, a Bayes factor is a ratio of marginal likelihoods, a posterior odds includes a prior odds, and an e-value is an expectation-bounded statistic. The conversions $p = \min(1,1/E)$ and $E = f(P)$ are calibrations, not identities.

> The ambiguity is resolved by declaring the two branches and keeping the null, alternative or prior, construction, filtration, stopping rule, and decision threshold as separate elements. An e-value is determinate relative to a declared construction, not absolutely.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: the table decomposes the e-value element under two kind branches — the representation (the quantity) and the operation (its calculation). Stopping rule: a row is terminal when it names a concrete quantity, model component, procedure, act, principle, or test; the branches are not decomposed further here. Identity: every path is unique; instance rows are Title Case; type groupings are backticked; no type terminates a branch. Typing: the root is `Epistemic Element`; the e-value branch is `Epistemic Representation`, the calculation branch is `Epistemic Operation`; both are read as elements of inquiry.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` → `Epistemic Representation` | Grouping: the e-value read as a representation. |
| `Epistemic Element` → `Epistemic Operation` | Grouping: the e-value calculation read as an operation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` | Grouping: the quantitative sign system in which the e-value is expressed. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation | The system of quantities, scales, and numerical comparison. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` | Grouping: the combinable constituents of the quantitative representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Statistical Quantity | A quantity defined by a statistical model and a sampling distribution rather than by direct measurement. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Test Statistic | The statistic whose sampling distribution is used to construct the e-value. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Significance Level | The pre-specified threshold $\alpha$; a convention, not a property of the data. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Rejection Threshold | The rejection threshold $1/\alpha$ on the e-value scale. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Statistical Quantity → `Representation Element` | Grouping: the constituents of the statistical quantity. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Representation Element` → Statistical Quantity → `Representation Element` → E-Value | A nonnegative statistic whose expectation under every null distribution is at most one; larger values are evidence against $H_0$. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` | Grouping: the rules and structures constituting the quantitative representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Null Model | The statistical model with $H_0$ imposed; the distribution under which the e-value has expectation at most one. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Alternative Model | The model or prior on $H_1$ used to construct a growth-optimal e-value. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Likelihood Ratio | The ratio of alternative to null densities; an e-value when the null is simple. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Bayes Factor | The ratio of marginal likelihoods; an e-value when the null is simple and the alternative prior is proper. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Test Martingale | A nonnegative martingale with expectation one; the sequential e-value process. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → E-Process | A nonnegative supermartingale with expectation at most one at every stopping time. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Stopping Time | A data-dependent time at which the e-process is evaluated; optional stopping is licensed. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Filtration | The increasing information set to which the e-process is adapted. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Sampling Distribution | The distribution of the data or statistic under the null model. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Null Hypothesis | The hypothesis $H_0$ whose compatibility the e-value measures. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Alternative Hypothesis | The hypothesis $H_1$ that guides the construction and the e-power. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Independence Assumption | The sampling units are independent under the model. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Distributional Assumption | The assumed family of the data or of the test statistic. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Nuisance Parameter | The parameter not fixed by $H_0$, eliminated by a mixture, projection, or supremum. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Prior Distribution | A probability distribution on $H_1$ used by a mixture or Bayes construction. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → Betting Strategy | The rule that allocates the betting wealth across outcomes. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` | Grouping: properties of the e-value representation. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Nonnegativity | The e-value is nonnegative; negative values are not admissible. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Expectation Bound | Under $H_0$, the expectation of the e-variable is at most one. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Anytime Validity | The e-process controls Type I error uniformly over time, not only at a fixed sample size. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Optional-Stopping Safety | The e-process remains valid when the stopping time is chosen from the data. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Optional Continuation | The product of e-values from independent studies is an e-value even when continuation depends on past results. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Combination by Averaging | A weighted average of e-values is an e-value even under arbitrary dependence. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Unboundedness | The e-value has no finite upper bound; it can be arbitrarily large. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Calibration to P-Value | The e-to-p calibration $\min(1,1/E)$ is a p-value; the converse requires a p-to-e calibrator. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → E-Power | The expected log e-value under the alternative; the analogue of power for e-values. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Growth-Rate Optimality | The construction that maximizes e-power; GRO for a simple alternative, GROW or REGROW for composite alternatives. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Dependence Robustness | The averaging combination and e-BH remain valid under arbitrary dependence. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Stochasticity | The e-value is a random variable before the sample is drawn. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → Model Dependence | The e-value depends on the null, the alternative, and the construction, not on the data alone. |
| `Epistemic Element` → `Epistemic Representation` → `Representational System` → Quantitative Representation → `Constitutive Substrate` → `Property` → No Evidence Below One | Values below one have no generally accepted evidence-for-$H_0$ interpretation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` | Grouping: the organized operation that produces the e-value. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` | Grouping: generalized ways of performing the statistical operation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation | The organized class of operations that infer from sample to population under a statistical model. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference | Inference from sample to population under a model. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing | The method that evaluates $H_0$ against $H_1$ by a test statistic and a rejection rule. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` | Grouping: ordered routines within hypothesis testing. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation | The procedure that constructs an e-value or e-process from the observed data and the null model. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` | Grouping: the steps and constructions of the e-value calculation. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` → Likelihood Ratio Construction | Form the likelihood ratio of an alternative density to a simple null density. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` → Mixture Construction | Average likelihood ratios over a prior or mixing distribution on the alternative. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` → Universal Inference Construction | Divide the alternative likelihood by the supremum of the null likelihood; an automatic e-value. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` → Betting Construction | Construct a nonnegative betting score with conditional expectation at most one under $H_0$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` → E-Process Construction | Multiply conditional e-values into an e-process adapted to the filtration. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` → Expectation Check | Verify the expectation bound or the supermartingale property under $H_0$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` → Threshold Comparison | Compare the e-value with the rejection threshold $1/\alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Procedure` → E-Value Calculation → `Procedure` → E-Value Report | Report the e-value with the null, alternative, construction, and stopping rule. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` | Grouping: the tests that realize hypothesis testing with e-values. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → Safe Test | A test based on an e-value or e-process that preserves Type I error under optional continuation or stopping. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Method` → Statistical Operation → Statistical Inference → Hypothesis Testing → `Method` → E-Process Test | A sequential test that rejects when the e-process crosses $1/\alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Action` | Grouping: the primitive acts of the calculation. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Specify Null Act | Fix $H_0$, the model, and the sample space. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Specify Alternative Act | Fix $H_1$ or a prior on $H_1$ that guides the construction. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Choose E-Value Construction Act | Choose a likelihood-ratio, mixture, universal-inference, or betting construction. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Compute E-Value Act | Evaluate the e-variable on the sample. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Check Expectation Bound Act | Check that the construction is an e-value or e-process under $H_0$. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Compare To Threshold Act | Apply the rule $E \ge 1/\alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Action` → Report E-Value Act | Report the value with its construction and stopping context. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` | Grouping: rules guiding the calculation and its use. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Markov Principle | Markov's inequality bounds the null probability of $E \ge 1/\alpha$ by $\alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Ville Principle | Ville's inequality bounds the null probability that an e-process ever crosses $1/\alpha$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Optional-Stopping Principle | Optional stopping of an e-process preserves Type I error control. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Optional-Continuation Principle | Optional continuation with independent e-values preserves Type I error control. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Averaging Principle | Average e-values when dependence is unknown; multiply when independent. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → E-Power Principle | Choose the construction with the largest expected log e-value under $H_1$. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Calibration Principle | Convert e-values to p-values with $\min(1,1/E)$; calibrate p-values to e-values with a p-to-e calibrator. |
| `Epistemic Element` → `Epistemic Operation` → `Organization` → `Principle` → Multiplicity Principle | Apply e-BH or another e-value multiplicity procedure. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdicts.** The e-value is conceptually well identified once the null, the construction, and the stopping rule are declared: pass. Its definition is formally clear but equivocal between the e-variable, the realized value, and the evidence reading: partial. Its determinacy is relative to a declared construction; the same data can yield different e-values: partial. It is internally consistent once the expectation bound, the Markov rule, and the e-process extension are kept apart: pass. Its representational adequacy is high for evidence against $H_0$, low for truth, effect size, posterior probability, and evidence for $H_0$: partial. Its purpose adequacy is high for safe, anytime-valid inference and combination, low as a universal evidence scale: pass.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The note distinguishes the e-value from the p-value, the Bayes factor, the posterior odds, the test statistic, the decision rule, and the effect size. |
| **Definitional Clarity** | Partial | The formal definition is precise, but the term "e-value" is used for both the random variable and its realization, and "evidence" is not a probability. The value below one has no settled evidence-for-$H_0$ reading. |
| **Conceptual Determinacy** | Partial | The e-value is determinate relative to a declared null, alternative or prior, construction, and stopping rule. Different constructions on the same data can produce different e-values. |
| **Internal Consistency** | Pass | The expectation bound, Markov's inequality, the rejection rule, the e-to-p calibration, and the e-process extension are mutually consistent. |
| **Representational Adequacy** | Partial | It represents evidence against $H_0$ on a multiplicative scale; it does not represent the truth of $H_0$, the size of an effect, the posterior, or evidence for $H_0$. It is conservative relative to an exact p-value. |
| **Purpose Adequacy** | Pass | It serves safe testing, optional stopping, optional continuation, combination, and multiplicity control well. It is not a universal evidence scale and requires a construction with a meaningful alternative. |

## QA

### What is an e-value, and how does it differ from a p-value?

> An e-value is the realized value of a nonnegative e-variable $E$ with $\mathbb{E}_P[E] \le 1$ for every $P \in H_0$. It measures evidence against $H_0$ multiplicatively: larger is stronger evidence, and the rejection rule is $E \ge 1/\alpha$.

| | **E-value** | **P-value** |
| --- | --- | --- |
| Definition | Nonnegative statistic with null expectation at most one | Tail probability of a statistic at least as extreme as the observed one |
| Range | $[0,\infty]$, often unbounded | $[0,1]$ |
| Evidence direction | Larger is stronger evidence against $H_0$ | Smaller is stronger incompatibility with $H_0$ |
| Rejection rule | $E \ge 1/\alpha$ | $p \le \alpha$ |
| Conversion | $p = \min(1,1/E)$ | $E = f(p)$ for a p-to-e calibrator $f$, not $1/p$ in general |
| Optional stopping | An e-process is anytime-valid | A fixed-sample p-value needs alpha-spending or an always-valid construction |
| Combination | Product for independent e-values; weighted average under arbitrary dependence | Requires a p-value combination rule and its dependence assumptions |
| Conservativeness | Usually conservative | Can be exact or asymptotic |
| Evidence for $H_0$ | Values below one have no settled evidence-for-$H_0$ reading | A large p-value is not evidence for $H_0$ without a severity or power argument |

> The two scales are not interchangeable. An e-value is not a "better p-value": it is a different expectation-bounded object with stronger operational guarantees under optional stopping and combination, and weaker finite-sample exactness. The e-to-p calibration is exact in one direction; the p-to-e direction loses information.

> **Worked example.** For a simple null $P_0 = \mathrm{N}(0,1)$ and a simple alternative $Q = \mathrm{N}(\delta,1)$ with a single observation $Y=y$,
>
> $$E(y) = \frac{\varphi(y-\delta)}{\varphi(y)} = \exp\left(\delta y - \frac{\delta^2}{2}\right).$$
>
> Under $P_0$, $\mathbb{E}[E] = 1$, so $E$ is an e-value. The rejection rule $E \ge 1/\alpha$ is equivalent to $y \ge (\log(1/\alpha) + \delta^2/2)/\delta$. The corresponding p-value is $p = \min(1,1/E)$; it is a valid but generally conservative p-value.

### Why does rejecting at $E \ge 1/\alpha$ control Type I error, and what does an e-process add?

> **Markov's inequality.** For a nonnegative random variable $E$ and $c>0$,
>
> $$\mathbb{P}_{H_0}(E \ge c) \le \frac{\mathbb{E}_{H_0}[E]}{c}.$$
>
> With $c=1/\alpha$ and $\mathbb{E}_{H_0}[E] \le 1$, the bound is $\alpha$. No independence, normality, or fixed-sample assumption is used. The test is valid for any e-variable, including a data-dependent construction that was chosen before seeing the data.

> **Ville's inequality.** For a nonnegative supermartingale $(E_n)$ with $E_0 \le 1$,
>
> $$\mathbb{P}_{H_0}\left(\sup_{n \ge 0} E_n \ge \frac{1}{\alpha}\right) \le \alpha.$$
>
> The supremum is over the whole path, so the bound holds at every stopping time simultaneously. This is stronger than applying Markov at a fixed $n$: it licenses stopping when the evidence looks strong, without inflating the Type I error.

> **What an e-process adds.** A single e-value is a one-shot object. An e-process is a sequence adapted to a filtration with the supermartingale property under every null distribution. It can be built by multiplying conditional e-values:
>
> $$E_n = \prod_{i=1}^n E_i, \qquad \mathbb{E}_P[E_i \mid \mathcal{F}_{i-1}] \le 1.$$
>
> Then $(E_n)$ is an e-process. The product is the sequential analogue of combining independent e-values; the conditional expectation is what makes the optional-stopping guarantee work.

> **Optional continuation versus optional stopping.** Optional continuation is the freedom to decide whether to run another independent study after seeing the previous e-values; the product of the per-study e-values remains an e-value, so the final decision is safe. Optional stopping is the freedom to stop within one sequential experiment at a data-dependent time; the e-process and Ville's inequality are what make that safe. A single fixed-sample e-value does not by itself license within-sample optional stopping.

> **A caution.** The bound is a null guarantee, not a measure of evidence for $H_0$. Failing to cross $1/\alpha$ does not establish $H_0$; it may reflect a weak construction, an uninformative alternative, or an underpowered design.

### How are e-values constructed for simple and composite nulls?

| Null | Alternative | Construction | E-value |
| --- | --- | --- | --- |
| Simple $H_0=\{P_0\}$ | Simple $H_1=\{Q\}$ | Likelihood ratio | $E = q(Y)/p_0(Y)$; the GRO e-value |
| Simple $H_0=\{P_0\}$ | Composite $H_1$ | Mixture or Bayes | $E = \int q_\theta(Y)\,\pi(\mathrm{d}\theta)/p_0(Y)$ |
| Simple $H_0=\{P_0\}$ | Composite $H_1$ | Betting | $E = \prod_i (1+\lambda_i(Y_i-\mu_0))$ for a feasible betting strategy |
| Composite $H_0$ | Simple $H_1=\{Q\}$ | Reverse information projection | $E = q(Y)/p_0^*(Y)$ under regularity; GRO |
| Composite $H_0$ | Simple $H_1=\{Q\}$ | Universal inference | $E = q(Y)/\sup_{P \in H_0} p(Y)$; automatic, often conservative |
| Composite $H_0$ | Composite $H_1$ | Mixture plus projection or universal inference | Combine the two constructions; GROW or REGROW under regularity |
| Any p-value $P$ | — | p-to-e calibration | $E = f_\kappa(P) = \kappa P^{\kappa-1}$, $\kappa \in (0,1)$ |

> **Simple null, simple alternative.** The likelihood ratio is the canonical e-value. For a simple null, every e-variable is a likelihood ratio for some alternative, so the likelihood ratio is not merely one construction among many; it is the general form. The Bayes factor is the mixture version when the alternative carries a prior.

> **Simple null, composite alternative.** The method of mixtures averages likelihood ratios over a prior or mixing distribution. The resulting e-value is a Bayes factor against the simple null. A betting construction instead chooses a stake $\lambda$ and scores $1+\lambda(Y-\mu_0)$; for bounded or mean-zero null models, a feasible $\lambda$ keeps the conditional expectation at most one. The product over time is an e-process.

> **Composite null, simple alternative.** The reverse information projection (RIPr) replaces the unknown null density by the element of the null convex hull closest to $Q$ in KL divergence. Under regularity, the ratio $q/p_0^*$ is the GRO e-value. Universal inference avoids the projection and uses $q/\sup_{P \in H_0} p$; it is an e-value because the null likelihood is at most its supremum, but it can be much more conservative.

> **Composite null, composite alternative.** Combine a mixture or prior on the alternative with a projection or universal-inference step on the null. The GROW criterion maximizes the worst-case e-power over the alternative; REGROW maximizes the worst-case regret relative to the best e-value for each alternative. Both are more demanding than the simple-alternative GRO and can be conservative.

> **From p-values.** The identity $E=1/P$ is not a valid calibration in general. The calibrators $f_\kappa(p)=\kappa p^{\kappa-1}$ integrate to one over the uniform p-value distribution and are valid; the integrated calibrator is closer to $1/p$ but still not equal to it. Calibrated e-values are often weak compared with e-values constructed directly from the alternative.

### How do e-values combine, and how does e-BH control the false discovery rate?

> **Averaging.** If $E_1,\dots,E_m$ are e-values for the same null and $w_1,\dots,w_m$ are nonnegative weights summing to one, then
>
> $$\sum_{i=1}^m w_i E_i$$
>
> is an e-value. No independence assumption is needed. This is the default combination when the dependence structure is unknown, and it is the basis for merging analyses on a shared dataset.

> **Multiplication.** If $E_1,\dots,E_m$ are independent e-values, their product is an e-value. More generally, if each $E_i$ is conditional on the past and has conditional expectation at most one under $H_0$, the product is an e-process. Multiplication is the natural combination for independent studies and for sequential evidence; averaging is the robust combination under arbitrary dependence.

> **e-BH.** Let $E_1,\dots,E_m$ be e-values for $m$ hypotheses, and let $E_{(1)} \ge \cdots \ge E_{(m)}$ be their descending order. Define
>
> $$k^* = \max\left\{k \in \{1,\dots,m\} : E_{(k)} \ge \frac{m}{\alpha k}\right\},$$
>
> with $k^*=0$ if the set is empty. Reject every hypothesis with
>
> $$E_i \ge \frac{m}{\alpha k^*}.$$
>
> Equivalently, reject the top $k^*$ e-values. The procedure controls the false discovery rate at $\alpha$ under arbitrary dependence of the e-values. It is the e-value analogue of Benjamini–Hochberg, and it does not require the p-values' PRDS or independence conditions.

> **Why e-BH works.** The threshold is on the e-value scale, not the p-value scale. The proof uses the expectation bound and a counting argument over the rejected set; the arbitrary-dependence guarantee comes from the e-value property rather than from a positive-dependence assumption. Weighted and boosted versions exist. The procedure is optimal among a broad class of e-value multiple-testing rules, but it is not uniformly more powerful than BH when valid, precise p-values and PRDS hold.

> **Reporting.** Report the e-values, the null and alternative or prior, the construction, the stopping rule, the multiplicity procedure, and the threshold. An e-value without its construction is not interpretable as evidence.

### What is e-power/GRO, and why maximize $\mathbb{E}_Q[\log E]$?

> **E-power.** For a simple alternative $Q$, the e-power of an e-variable $E$ is
>
> $$\operatorname{e-power}(E;Q) = \mathbb{E}_Q[\log E].$$
>
> It is the expected logarithmic growth rate of the evidence under the alternative. The name is deliberate: it is the analogue of power in a safe-testing, optional-continuation setting, where the relevant question is how fast evidence accumulates rather than the rejection probability at one fixed sample size.

> **GRO.** The growth-rate optimal e-variable for $Q$ is
>
> $$E_Q^* = \arg\sup_{E \in \mathcal{E}(H_0)} \mathbb{E}_Q[\log E],$$
>
> and its e-power is $\mathrm{GRO}(Q)$. For a simple null, the likelihood ratio is GRO. For a composite null, the GRO e-value is a generalized likelihood ratio against the reverse information projection of $Q$ onto the null convex hull, under regularity. The logarithmic criterion is the Kelly criterion: it maximizes the long-run growth rate of wealth in a betting interpretation and turns multiplication of evidence into addition on the log scale.

> **Composite alternatives.** If the alternative is a family $\mathcal{Q}$, two criteria are common:
>
> - **GROW:** maximize $\inf_{Q \in \mathcal{Q}} \mathbb{E}_Q[\log E]$, the worst-case e-power;
> - **REGROW:** maximize $\inf_{Q \in \mathcal{Q}} \left(\mathbb{E}_Q[\log E] - \mathrm{GRO}(Q)\right)$, the worst-case regret relative to the best e-value for each $Q$.
>
> GROW can be too pessimistic and can push toward a trivial e-value when the null and alternative are close. REGROW is relative and often more useful, but both require a declared alternative family and regularity for existence and uniqueness.

> **Why log?** The log scale turns multiplication of independent e-values into addition of evidence, makes the e-process growth rate additive over time, and connects e-values to Bayes factors and betting wealth. Maximizing $\mathbb{E}_Q[\log E]$ is not the same as maximizing the probability of rejection at a fixed $\alpha$; it optimizes the rate at which evidence accumulates under repeated or optional continuation.

> **Caution.** A GRO e-value can be excellent under the chosen $Q$ and poor under a different alternative. E-power is not a universal measure of test quality; it is relative to the alternative or prior used in the construction.

### What are the common misinterpretations and limits of e-values?

> **"An e-value is the probability that $H_0$ is false."** No. It is a nonnegative statistic with a null expectation bound. It does not assign a probability to a hypothesis.

> **"An e-value of 20 means $H_1$ is 20 times more likely."** No. A likelihood ratio can be read as a Bayes factor only with a prior and a simple null; an arbitrary e-value is not a posterior odds and does not by itself update belief.

> **"An e-value below one is evidence for $H_0$."** There is no generally accepted evidence-for-$H_0$ interpretation of e-values below one. The e-value is constructed to measure evidence against $H_0$; a small value may mean that the construction is weak or that the data are uninformative.

> **"An e-value is just $1/p$."** The e-to-p direction is exact: $p=\min(1,1/E)$ is a p-value. The p-to-e direction is not: $1/p$ is not generally an e-value, and valid p-to-e calibrators are more conservative.

> **"An e-value is a p-value with a different scale."** The two have different definitions, ranges, null guarantees, combination rules, and optional-stopping properties. An e-value is not a rescaled p-value.

> **"Every e-value is a Bayes factor."** Bayes factors are e-values when the null is simple and the alternative prior is proper. The converse fails: e-values can be betting scores, universal-inference ratios, or other expectation-bounded statistics that are not Bayes factors.

> **"A generalized likelihood ratio is an e-value."** Not in general for a composite null. The denominator must be a valid null density or a mixture/projection that preserves the expectation bound; the naive maximum-likelihood ratio can fail.

> **"Optional stopping is always safe."** A fixed-sample e-value is safe for optional continuation when multiplied across independent studies, but within-sample optional stopping requires an e-process or test martingale. A single e-value evaluated at a data-dependent stopping time does not automatically retain the Type I guarantee.

> **"A large e-value proves $H_1$."** It is evidence against $H_0$ relative to a construction. It does not prove $H_1$, establish an effect size, or replace design, replication, and subject-matter judgment.

> **"E-values are always more powerful than p-values."** E-values are usually conservative in fixed-sample tests; their advantage is operational (optional stopping, optional continuation, combination, dependence-robust multiplicity), not universal power. The choice depends on the design and the question.

> **Limits.** E-values require a declared null and a construction; they can be unbounded and highly skewed; their evidence reading below one is unsettled; GRO/GROW/REGROW depend on the alternative or prior; and the e-BH guarantee is an FDR guarantee, not a per-hypothesis posterior probability. They are a powerful complement to p-values, not a replacement for statistical design.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [P-Value](note.html?n=epistemica/validation/p-value.md)
- [Statistical Hypothesis Testing](note.html?n=epistemica/validation/statistical-hypothesis-testing.md)
- [Validation](note.html?n=epistemica/validation/validation.md)
- [Calibration](note.html?n=epistemica/validation/calibration.md)
- [REES atlas](data/epistemica/rees.html)
- https://en.wikipedia.org/wiki/E-values
- Vovk, V., & Wang, R. (2021). E-values: Calibration, combination and applications. *Annals of Statistics*, 49(3), 1736–1754. https://arxiv.org/abs/1912.06116
- Grünwald, P., de Heide, R., & Koolen, W. M. (2024). Safe testing. *Journal of the Royal Statistical Society: Series B*, 86(5), 1091–1128. https://arxiv.org/abs/1906.07801
- Ramdas, A., Grünwald, P., Vovk, V., & Shafer, G. (2023). Game-theoretic statistics and safe anytime-valid inference. *Statistical Science*, 38(4), 576–601. https://arxiv.org/abs/2210.01948
- Wang, R., & Ramdas, A. (2022). False discovery rate control with e-values. *Journal of the Royal Statistical Society: Series B*, 84(3), 822–852. https://arxiv.org/abs/2009.02824
- Koning, N. W. (2024). Post-hoc $\alpha$ hypothesis testing and the post-hoc p-value. https://arxiv.org/abs/2312.08040
- Howard, S. R., Ramdas, A., McAuliffe, J., & Sekhon, J. (2021). Time-uniform, nonparametric, nonasymptotic confidence sequences. *Annals of Statistics*, 49(2), 1055–1080. https://arxiv.org/abs/1810.08240
- Shafer, G. (2021). Testing by betting: A strategy for statistical and scientific communication. *Journal of the Royal Statistical Society: Series A*, 184(2), 407–431. https://arxiv.org/abs/1903.06991
- Waudby-Smith, I., & Ramdas, A. (2024). Estimating means of bounded random variables by betting. *Journal of the Royal Statistical Society: Series B*, 86(1), 1–27. https://arxiv.org/abs/2010.09686
- Robbins, H. (1970). Statistical methods related to the law of the iterated logarithm. *Annals of Mathematical Statistics*, 41(5), 1397–1409.
- Ville, J. (1939). *Étude critique de la notion de collectif*. Gauthier-Villars.
