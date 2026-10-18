---
tags: [probability]
---

# Distribution

 : (Statistic) Estimator ((Statistic)%20Estimator%2010fc0f5171ec8015accadab377f913a5.md), Random Object (Random%20Object%2024ec0f5171ec800b8c30edbce9c37968.md), Data (Data%20264c0f5171ec80bb9fb2fa8e2e3a82a9.md)

> In this note, we will explore the fundamental concept of a **probability distribution**—the mathematical mechanism we use to **assign weights or probabilities to different outcomes of a random process**, allowing us to describe, analyze, and predict the behavior of stochastic systems.
> 

> **Note:** The concept of a distribution essentially captures a probabilistic model, both in a descriptive sense $P(X)$ and in a model sense $P(X, Y)$.
> 

## Meta

> Evaluation Framework.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21).
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | ⭐⭐⭐: Moderately useful. Covers essential ideas but may lack depth, cohesion, or polish. |
| **Completeness** | ⭐⭐½: Covers the core concepts (definition, types, parameters, derivation, applications), but could be expanded with more examples, derivations, visualizations, and connections to real-world data scenarios. |
| **Coherence & Structure** | ⭐⭐⭐: The note is mostly well-structured, with clear sections and logical flow, but some sections could be better connected (e.g., distribution derivation and joint/marginal distributions). |
| **Epistemic Self-Assessment** | ⭐⭐⭐ (Competent). Adequate understanding; functional in typical contexts; recognizes patterns but may not generalize broadly. |
| **Should I Reorganize This -in My Content Forest?** | ⚖️ Yes, consider linking related sections (parameters ↔ distribution types ↔ derivation) to improve navigability and reinforcing mental models. |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | A probability distribution is the fundamental mathematical mechanism that **assigns weights to potential outcomes under uncertainty**, capturing the structure of randomness and quantifying the likelihood of each event. At its essence, it represents **uncertainty in a structured, formalized way**. |
| **Telos (Intent) 🎯** | A probability distribution is intended to **model uncertainty, support reasoning, and enable prediction**. It allows computation of expectations, variances, and probabilities of events, facilitating decision-making and risk assessment. It provides a **tool for simulation, inference, and optimization under uncertainty**. |
| **Gnosis (Understanding) 🧠** | To mentally represent a distribution, one should understand its **declarative aspects** (mean, variance, shape, parameters) and **procedural aspects** (how to sample from it, how to compute probabilities). Developing a mental model involves recognizing patterns across distributions (continuous vs. discrete, unimodal vs. multimodal), understanding parameter effects, and connecting distributions to real-world phenomena. Prior knowledge of basic probability, algebra, and statistics is necessary. |
| **Epignosis (Application) 🛠️** | Probability distributions are applied in **statistics, machine learning, physics, finance, engineering, and decision science**. Mastery enables tasks like modeling uncertainty, hypothesis testing, Bayesian inference, stochastic simulations, and risk modeling. Advanced insights include understanding distribution families, transformations, and approximations. |
| **Relatio (Connections) 🔗** | Closely related to **random variables, stochastic processes, statistical inference, and information theory**. Interdisciplinary connections exist in physics (quantum probabilities), economics (risk modeling), biology (population modeling), and computer science (probabilistic algorithms, AI). |
| **Idoneitas (Suitability) 📐** | Effectiveness is measured by **fit to observed data, predictive accuracy, and tractability**. Metrics include likelihood, information criteria (AIC/BIC), and mean squared error for predictions. |
| **Limites (Limits) ⛔** | Distributions are **idealizations**; they assume a fixed structure and independence conditions that may not hold in complex systems. Parameters may be estimated inaccurately, and models may fail to capture extreme events or dependencies. |
| **Contextus (Context) 🌍** | Emerged historically from **gambling, actuarial science, and astronomy**, evolving into a cornerstone of modern probability theory and statistics. Applications are shaped by the availability of data, computational methods, and domain-specific needs. |
| **Dynamis (Evolution) 🌱** | Probability distributions evolve with **computational advances, high-dimensional modeling, and machine learning frameworks**. Emerging trends include non-parametric and generative approaches, deep probabilistic models, and data-driven distribution discovery. |
| **Critica (Critique) 🔍** | Criticisms include over-reliance on idealized assumptions, poor fit for real-world heavy-tailed or dependent data, and misinterpretation of probabilities. Debates focus on **frequentist vs. Bayesian interpretations** and the robustness of parametric models. |
| **Verbum Usus (Language Use) 🗣️** | Used in discourse as “X follows a Normal distribution,” “the probability distribution of Y,” or “modeled as Poisson.” Contexts influence connotation: in statistics it is formal, in general speech it may simply mean “pattern of likelihood.” Trends show expanding usage in AI, ML, and data science. |

## Terminology

> A **probability measure** is like a **rule that assigns “weights” to events**, always between $0$ and $1$, consistently.
> 

> A **probability distribution** is the measure-theoretic mapping that fully describes how probability is allocated over the possible values of a **random object**.
> 

> A **probability measure** is a mathematical function that assigns a **numerical probability** to events in a probability space, providing a formal way to quantify uncertainty.
> 

> **Copulas:**  Models dependencies between variables while preserving their marginal distributions.
> 

> **Support:** The **set of outcomes where a probability distribution is non-zero**. For a discrete random variable, it’s the set of points with positive probability; for a continuous variable, it’s the region where the probability density is positive.
> 

## Quick Guide

> The majority of these distributions model derived or more complex random variables. When studying such a distribution, always ask: which underlying random variables drive the behavior that this distribution is capturing? **Which aspect of reality does this distribution is capturing?**
> 
- **Bernoulli**: one trial.
- **Binomial**: number of successes in $n$ trials.
- **Geometric**: trials until first success.
- **Negative Binomial**: trials until $\text{r-th}$ success.
- **Uniform Distribution**: equal probability over an interval or finite set.
- **Gaussian Distribution**: bell-shaped, defined by mean and variance.
- **Poisson Distribution**: counts of events in fixed time/space, with rate $\lambda$.
- **Gamma Distribution**: waiting time until the $\text{r-th}$ **event** in a Poisson process, generalizes the exponential.
- **Exponential Distribution:**  waiting time until the **first event** in a Poisson process (special case of Gamma with $r=1$).

## Distribution

### Parameter

> A **parameter** is a **numerical value that characterizes a specific aspect of a probability distribution**. It defines the behavior of the distribution, such as its location, spread, shape, or rate, and allows us to describe the distribution **compactly and systematically**.
> 

### Type

> A list of the **fundamental functional forms** and **probability measures**.
> 

> These are **conceptual categories of probability measures/distributions** that define **how the probability of an event is considered in isolation, in combination, or given other information**.
> 

| Type | Description | Discrete Functional Form | Continuous Functional Form |
| --- | --- | --- | --- |
| **Unconditional (Absolute)** | Probability of an event without conditions | $P(X = x)$ | $f_X(x)$ |
| **Marginal** | Probability/density of one variable by summing/integrating out others | $P(X = x) = \sum_y P(X=x, Y=y)$ | $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dy$ |
| **Conditional** | Probability/density given another variable | $P(X=x \mid Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)}$ | $f_{X \mid Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$ |
| **Joint** | Probability/density of multiple variables together | $P(X=x, Y=y)$ | $f_{X,Y}(x,y)$ |

### Property

| **Property** | **Description** | **Tag(s)** |
| --- | --- | --- |
| **Support** | The subset of the sample space on which the probability measure assigns non-zero mass; equivalently, the smallest closed (or measurable) set outside of which the distribution is almost surely zero. | [Definitional], [Structural], [Primitive], [Measure-Theoretic], [Topological], [Univariate], [Multivariate] |
| **Type** | The categorical classification of the distribution according to the nature of its measure (e.g., discrete, absolutely continuous, singular, or mixed), which determines admissible representations and analytical tools. | [Definitional], [Structural], [Primitive], [Measure-Theoretic] |
| **PMF / PDF** | A function that represents the probability measure relative to a reference measure (counting or Lebesgue), enabling pointwise or density-based evaluation, likelihood computation, and simulation. | [Definitional], [Representational], [Primitive], [Measure-Theoretic], [Analytic], [Computable], [Simulation-Relevant] |
| **CDF** | A cumulative mapping from the sample space to ([0,1]) that fully characterizes the distribution via monotonicity and right-continuity, supporting probability queries and inversion-based methods. | [Representational], [Derived], [Analytic], [Measure-Theoretic], [Identifying], [Computable] |
| **Moments (raw / central)** | Expectation-based functionals capturing aggregate properties of the distribution such as location, dispersion, and shape, provided the corresponding integrals exist. | [Functional], [Primitive], [Moment], [Analytic], [Algebraic], [Estimable], [Inferential] |
| **Mean** | The first raw moment, representing the distribution’s center of mass and serving as the optimal point estimator under squared-error loss when finite. | [Functional], [Derived], [Moment], [Descriptive], [Estimable], [Non-Robust], [Inferential] |
| **Variance** | The second central moment, measuring average squared deviation from the mean and quantifying dispersion relevant to uncertainty propagation and optimization. | [Functional], [Derived], [Moment], [Descriptive], [Estimable], [Optimization-Relevant], [Non-Robust] |
| **Standard Deviation** | The square root of variance, restoring scale compatibility with the original variable and providing a linearized measure of dispersion. | [Functional], [Derived], [Moment], [Descriptive], [Algebraic], [Estimable] |
| **Skewness** | A normalized third central moment quantifying directional **asymmetry** of the distribution around its mean. | [Functional], [Derived], [Moment], **[Shape]**, [Geometric], [Non-Robust], [Descriptive] |
| **Kurtosis** | A normalized fourth central moment measuring tail heaviness and peak sharpness relative to a reference distribution, with strong sensitivity to extreme values. | [Functional], [Derived], [Moment], **[Shape]**, [Geometric], [Tail], [Asymptotic], [Non-Robust] |
| **Quantiles / Median** | Order-based functionals defined via the inverse CDF that summarize distributional location and spread while remaining robust to outliers. | [Functional], [Derived], [Order-Theoretic], [Robust], [Inferential] |
| **Mode** | The point(s) at which the probability mass or density is maximized, corresponding to the most probable or most likely outcome(s). | [Functional], [Derived], **[Shape]**, [Geometric], [Optimization-Relevant], [Non-Robust] |
| **Entropy** | An information-theoretic functional measuring average uncertainty or unpredictability inherent in the distribution. | [Information-Theoretic], [Functional], [Derived], [Uncertainty], [Compression-Relevant], [Optimization-Relevant] |
| **MGF** | A transform encoding all finite moments of the distribution in a neighborhood of zero, when it exists, enabling analytic derivations and limit theorems. | [Transformational], [Derived], [Moment], [Analytic], [Algebraic], [Inferential] |
| **Characteristic Function** | The Fourier transform of the probability measure, always well-defined, uniquely identifying the distribution and supporting convergence and spectral analysis. | [Transformational], [Primitive], [Spectral], [Analytic], [Identifying], [Multivariate] |
| **Tail Behavior** | The asymptotic decay properties of the distribution at extreme values, governing rare-event probabilities, risk, and stability. | [Structural], [Derived], **[Shape]**, [Asymptotic], [Tail], [Risk-Relevant] |
| **Symmetry** | Structural invariance of the distribution under specific transformations (e.g., reflection), constraining moments and simplifying inference. | [Structural], [Derived], **[Shape]**, [Geometric], [Identifying] |
| **Continuity / Smoothness** | Regularity properties of the distribution or its density, such as continuity or differentiability, which determine admissible analytical and numerical methods. | [Structural], [Derived], [Analytic], [Topological] |
| **Parameterization** | The specification of the distribution in terms of parameters that control its shape, scale, and location, forming the basis for estimation and inference. | [Definitional], [Structural], [Primitive], [Parametric], [Inferential] |
| **Support Boundedness** | Whether the support is finite, semi-infinite, or unbounded, influencing moment existence, tail risk, and asymptotic behavior. | [Structural], [Derived], [Topological], [Asymptotic] |
| **Dependence Structure** | The specification of statistical relationships among components in multivariate distributions, including correlation, copulas, and conditional independencies. | [Definitional], [Relational], [Primitive], [Multivariate], [High-Dimensional] |

### List of Distributions

List of Probability Distribution

## Property

> What properties can be defined for a probability distribution?
> 

Property; Description; Value(s)

## Marginal Distribution

> The marginal distribution of a random variable is the probability distribution of that variable alone, obtained from a joint distribution by summing (discrete) or integrating (continuous) over the other variables. For example,  $P(X=x) = \sum_y P(X=x, Y=y)$ or $f_X(x) = \int f_{X,Y}(x,y)\,dy$.
> 

## Joint Distribution

> The joint distribution of two or more random variables specifies the probability (in the discrete case) or probability density (in the continuous case) that those variables simultaneously take particular values. Formally, for random variables $X$ and $Y$, the joint distribution is described by $P(X=x, Y=y)$ or $f_{X,Y}(x,y)$.
> 

## Conditional Distribution

> The conditional distribution of one random variable given the value of another specifies the probability distribution of the first under the condition that the second has taken a certain value. For example,  $P(Y=y)P(X=x \mid Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)}$ (when $P(Y=y)>0$), or in the continuous case $f_{X|Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$.
> 

## Distribution Derivation

> Let’s say that we have a random variable X that follows certain distribution D, and we apply operator to that random variable - including ones that deal with other random variable; how to derive the new distribution form $X_d$ where d means derived?
> 

> **Note:** This is a **key concept** because many problems are simply **compositions or derivations** based on a set of fundamental building blocks.
> 

> See more in [Random Variable](random-variable.md);  [Binomial Distribution](binomial-distribution.md);  [**Geometric Distribution**](geometric-distribution.md), …
> 

## Asymptotic Distribution

> **This concept captures the limiting probability distribution** of a sequence of random variables $X_n$ as $n \to \infty$, formally expressed as  $X_n \xrightarrow{d} X$ meaning that $X_n$ **converges in distribution** to a random variable $X$ with that limiting distribution.
> 

> This is another application of the **fundamental notion of convergence**, widely used in probability theory.
> 

## ❓ QA

### When people used the word of ‘data distribution’ in ml; are they referring to the same thing as in ‘probability distribution’?

> **Probability distribution** is a **mathematical object** that specifies all possible values a random variable can take, along with their probabilities (discrete case) or density (continuous case).
> 

> **Data distribution** usually refers to the **empirical distribution** of the data we have in hand—a finite sample.
> 

> **Relation:** In ML, we often assume our observed data are **drawn from an underlying probability distribution** (sometimes called the “true distribution”). The **data distribution** is the observable approximation of that underlying distribution.
> 

### What do the parameters of a distribution tell us about it?

> **Parameters** represent properties that characterize the distribution.
> 

> Parameters are **numerical quantities** that define or characterize the distribution’s shape, location, scale, or other properties.
> 

### Why do we use parameters to describe a distribution?

> **Parameters** provide a compact way to summarize and define a probability distribution.
> 

They allow us to:

1. **Characterize key properties**: Parameters encode important aspects of the distribution, such as its central tendency (mean), spread (variance), shape (skewness/kurtosis), or rate of occurrence.
2. **Generate or simulate data**: Knowing the parameters allows us to produce random samples that follow the distribution, useful in modeling, simulations, and forecasting.
3. **Compare distributions**: Parameters let us describe, classify, and compare different distributions systematically.
4. **Perform statistical inference**: Parameters provide a bridge between observed data (samples) and the underlying stochastic process, enabling estimation, hypothesis testing, and prediction.

### What types of parameters are usually used?

- **Location parameters:** describe the “center”
- **Scale parameters:** describe “spread” or dispersion
- **Shape parameters:** describe the shape of the distribution
- **Rate or probability parameters:** for discrete events

### What **makes a** parameter an effective characterization of a distribution?

> It should capture **essential and interpretable features** of the distribution.
> 

> Allow **easy computation** of key quantities (moments, probabilities, etc.).
> 

> Are **mathematically sufficient**: fully describe the distribution.
> 

### Does the parameters of the distribution are always related with it’s population statistics?

> Parameters often describe the distribution, but they do not always equal the population statistics—they sometimes encode shape, rate, or latent structure instead.
> 

### How do we estimate the parameters of a underlying distribution using Sample Statistics?

> We **never know the true parameters exactly**; we approximate them using the sample.
> 

> We compute a set of **sample statistics** (e.g., sample mean, sample variance) and relate them to the corresponding **distribution parameters**, then solve for the parameter estimates.
> 

### How do we get the PDF/PMF of a Distribution?

> A distribution is a mathematical tool designed to describe common characteristics of a set of stochastic scenarios.
> 

> To define a distribution, we select a **mathematical form** that fits the empirical data, characterize it with parameters., test this against the data.
> 

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [](https://app.notion.com/p/245c0f5171ec80749daec722e73b8a81?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- https://www.youtube.com/watch?v=mBCiKUzwdMs
- https://www.math.wm.edu/~leemis/chart/UDR/UDR.html
- https://en.wikipedia.org/wiki/List_of_probability_distributions
- https://en.wikipedia.org/wiki/Relationships_among_probability_distributions
- https://en.wikipedia.org/wiki/ProbOnto
- https://rpubs.com/nayefahmad/additive-and-multiplicative-effects
- https://www.jstor.org/stable/2096242
- [Normalization](../mathematical/normalization.md)
- https://en.wikipedia.org/wiki/Probability_measure
- https://en.wikipedia.org/wiki/Conditional_probability
- https://stats.stackexchange.com/questions/563949/difference-in-probability-measure-vs-probability-distribution
- https://math.stackexchange.com/questions/384923/what-exactly-is-a-probability-measure-in-simple-words
- https://en.wikipedia.org/wiki/Marginal_distribution
- https://github.com/dbremont/algorithms/tree/main/om/prob/distribution
- [Statistical Function](statistical-function.md)
- https://en.wikipedia.org/wiki/Joint_probability_distribution
- https://en.wikipedia.org/wiki/Marginal_distribution
- https://en.wikipedia.org/wiki/Asymptotic_distribution
- https://en.wikipedia.org/wiki/Skewness
