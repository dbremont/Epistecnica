---
tags: [probability]
---

# Random Variable

 : Random Object (Random%20Object%2024ec0f5171ec800b8c30edbce9c37968.md), Central Limit Theorem (CLT) (Central%20Limit%20Theorem%20(CLT)%20c878cc8c663448af9e416ba34cf5598d.md)

> A random variable at its core is a **virtual object that represents** some {state,  tag, …} in a piece of a stochastic system or reality. This virtual object is always numeric, enabling computations on these representations.
> 

> A random variable is implemented by a function  maps between a **sample space** to the **real line: $X:Ω→R$.**
> 

> **Note:** A random variable is neither *random* in the everyday sense nor a traditional *variable*. Instead, it is a deterministic function that assigns a numerical value to each outcome in a probability space, capturing uncertainty through the underlying probability measure.
> 

## Meta

> Evaluation Framework.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | ⭐⭐⭐ (Moderate). Covers essential ideas but may lack depth, cohesion, or polish. |
| **Completeness** | **Completeness:** ⭐⭐⭐⭐. Covers almost everything for a first-principles, advanced probability perspective. |
| **Coherence & Structure** | **Coherence & Structure:** ⭐⭐⭐. The content is logically organized, but some sections could be consolidated to reduce repetition and improve readability. |
| **Epistemic Self-Assessment** | ⭐⭐⭐ (Competent). Adequate understanding; functional in typical contexts; recognizes patterns but may not generalize broadly. |
| **Internalization Self-Assessment** | **⭐⭐⭐ Moderate** – The concept is **understood and occasionally applied**, with **some influence on behavior or reasoning**, but full internalization has not yet occurred. |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** |  |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | A random variable (RV) is a **mapping from outcomes of a probabilistic experiment to a numerical domain**. It encapsulates uncertainty by assigning numbers to outcomes in a way that allows systematic analysis of probabilistic events. At its core, it’s the **bridge between abstract probability spaces and quantifiable analysis**. |
| **Telos (Intent) 🎯** | Random variables provide a **formal tool to quantify uncertainty**. They enable calculation of **probabilities, expectations, moments**, and form the foundation for **statistical inference, stochastic modeling, and probabilistic reasoning**. Outcomes aimed: predictions, risk assessment, simulations, decision-making under uncertainty. |
| **Gnosis (Understanding) 🧠** | Build a mental representation: imagine a **space of possible outcomes**, a **function mapping to numbers**, and its **distribution shape**. Procedural understanding includes computing probabilities, expectations, transformations, sums of RVs. Prerequisites: set theory, functions, basic probability concepts. Organize by **type** (discrete vs continuous), **domain**, and **moments**. Visual tools: probability mass/density functions, cumulative distribution functions. |
| **Epignosis (Application) 🛠️** | Random variables are applied in: **risk modeling, finance (stock returns), engineering (noise modeling), AI/ML (features as RVs), simulation (Monte Carlo methods), statistical inference (estimators as RVs)**. Mastery allows: deriving **distributions of functions of RVs**, **central limit theorem applications**, modeling **dependent or independent RVs**, **joint distributions**, stochastic processes. |
| **Relatio (Connections) 🔗** | RVs connect probability theory with **statistics, measure theory, stochastic processes, information theory, ML, econometrics**, and **physics (statistical mechanics)**. They are foundational for **expectation operators, covariance, correlation, and entropy**. |
| **Idoneitas (Suitability) 📐** | Metrics: **how well it models uncertainty**, predictive performance in simulations, closeness of empirical distribution to theoretical distribution (goodness-of-fit). Suitability is measured via **variance, bias, and relevance of chosen RV representation** for the problem at hand. |
| **Limites (Limits) ⛔** | RVs are limited to **quantifiable aspects of randomness**. They require a **well-defined sample space** and **measurable mapping**. They cannot directly represent non-quantifiable or purely semantic uncertainties. Complex dependencies may require **vectors of RVs** or **stochastic processes**. |
| **Contextus (Context) 🌍** | Originates in **probability theory (17th–18th century: Bernoulli, Laplace)** and matured through **measure theory (Kolmogorov, 1930s)**. Used historically in **gambling, actuarial science**, and now central to **statistics, data science, and physics**. |
| **Dynamis (Evolution) 🌱** | RVs evolve through: **generalization to multivariate and functional RVs**, **non-commutative (free) probability**, **stochastic processes**, and **probabilistic programming frameworks**. Emerging influences: AI/ML, high-dimensional data, quantum probability. |
| **Critica (Critique) 🔍** | Challenges: oversimplification of real-world uncertainty, misinterpretation of RV as “random numbers” rather than mappings, difficulty in **estimating distributions from limited data**, and assumptions of independence that often fail. Debates exist in **frequentist vs Bayesian interpretations**. |
| **Verbum Usus (Language Use) 🗣️** | In discourse, “random variable” signals **quantitative abstraction of uncertainty**. Context-dependent: in math, it’s formal; in statistics/ML, it’s often data-oriented; in casual speech, may be confused with “random number”. Trends: increasing use in **data science, stochastic modeling, AI**, reflecting its central role in applied uncertainty quantification. |

## Formulation

> A **random variable** is a measurable function $X: (\Omega, \mathcal{F}, P) \to (\mathbb{R}, \mathcal{B})$ that assigns a real number to each possible outcome $\omega$ of an experiment, where $\mathcal{B}$ is the Borel σ-algebra on $\mathbb{R}$.
> 

A **probability space** is the mathematical foundation for probability.

It is a triple:  $(\Omega, \mathcal{F}, P)$

- **Sample Space** $\Omega$: the set of all possible outcomes of an experiment.
- **σ-algebra** $\mathcal{F}$: the collection of events (subsets of $\Omega$) we can measure.
- **Probability measure** $P$: assigns a probability $P(A) \in [0,1]$ to every event $A \in \mathcal{F}$.

## Characterization

| **Category** | **Mechanism** | **Description** |
| --- | --- | --- |
| **Distribution** | Probability Mass Function (PMF) / Probability Density Function (PDF) | Specifies the probability of each outcome (discrete) or the density over outcomes (continuous). Fully describes the RV. |
| **Cumulative Distribution** | Cumulative Distribution Function (CDF) | Gives $P(X \le x)$ for all xx. Encodes all probabilistic information of the RV. |
| **Moments** | Expectation, Variance, Skewness, Kurtosis | Summarizes key properties: central tendency (mean), spread (variance), asymmetry (skew), tail heaviness (kurtosis). Useful for compact characterization. |
| **Generating Functions** | Moment Generating Function (MGF), Characteristic Function (CF) | Functional transforms that uniquely encode the distribution. Useful for sums of RVs and theoretical analysis. |
| **Transformations** | Functions of other RVs | Defines a RV as a function of other RVs, e.g., $Y = aX + b$, or $Z = X_1 + X_2$. Allows construction of new RVs from known ones. |

## Property

> Which properties does a random variable possess?
> 

> Note the i.i.d is hard to me in high dimensions, but remember [What does the term random variables denotes? What do we mean in practice when we write  X1, X2, …, Xn?](random-variable.md)
> 
- Independent : **Independent** – a property of a set of r.v.’s: the joint distribution factorises into the product of the marginals.
- Identically Distributed: **Identically Distributed** – a property of a set of r.v.’s: every member has the same marginal distribution.

## Representing

> How can we use random variables to represent the world? How do we model the state of the world using random variables? How to map a ‘piece of reality’ to a **random variable**? What constitutes a good representation of reality?
> 

### Taxonomy

> Note: At this stage of my cognitive representation of random variables ($R_v$), I understand two main types: (1) a basic type that captures a state, and (2) a derived type that captures a property of the world, such as the number of trials until success.
> 

### Case

| **World State** | **Random Variable Representation** |
| --- | --- |
| **Single die roll** | $X \in \{1,2,3,4,5,6\}$ |
| **Three die rolls** | $X_1, X_2, X_3$ |
|  | $Y = (X_1,X_2,X_3)$ |
|  | $Z = X_1+X_2+X_3$ |
| **Daily rainfall** | $R_t \in \mathbb{R}_{\geq 0}$ |
|  | $\mathbf{R} = (R_1,\dots,R_{30})$ |
| **Temperature across city** | $T(x,y)$ |
| **Light bulb lifetime** | $L \sim \text{Exponential}(\lambda)$ |
|  | $S(t)=I\{L>t\}$ |
| **Deck shuffle** | $P \in S_{52}$ |
|  | $Y=(C_1,\dots,C_{52})$ |
|  | $M_{i,j}=I\{i\text{th card = rank }j\}$ |
| **Coin flips over time** | $C_t \in \{0,1\}$ |
|  | $S_n = \sum_{i=1}^n C_i$ |
|  | $\hat{p}_n = \tfrac{1}{n}\sum C_i$ |

### Derivation

> How to think about derived random variables?
> 

> Note: Every operator applies to a $R_v$ yield other $R_v$.
> 

> Suppose $X$ represents the outcome of a single coin toss. A **derived random variable** $Y$ can be defined as the total number of heads observed in $n$ independent tosses. This variable can be modeled by the **binomial distribution**: $Y \sim \text{Binomial}(n, p)$, where $p$ is the probability of getting heads in a single toss.
> 

## Distribution

> Note: A random variable can be seen as a numerical representation of a sample space; here, we will classify random variables according to their ([Distribution](distribution/distribution.md)).
> 

## Discrete Random Variable

> A **discrete random variable** is a random variable that can take on a **finite or countably infinite set of distinct values**. Each value has a well-defined probability, and you can list or enumerate all possible outcomes.
> 

## Continuous Random Variable

> A **continuous random variable** is a random variable that can take on **any value within a continuous interval** of real numbers. The probability of it taking any exact value is 0; probabilities are defined over **intervals** using a probability density function (PDF).
> 

## Probability Mass Function (PMF)

> A **Probability Mass Function (PMF)** defines the probability that a discrete random variable takes a specific value. It assigns a probability $P(X=x)$  to each possible outcome $x$.
> 

## Probability Density Function (PDF)

> A **Probability Density Function (PDF)** describes the relative likelihood of a **continuous random variable** taking on a value in an interval. Probabilities are computed as the **area under the curve** over that interval.
> 

## Cumulative Distribution Function (CDF)

> aka. What’s the probability that the outcomes if less or equal than this reference outcome?
> 

> A **Cumulative Distribution Function (CDF)** gives the probability that a random variable $X$ (discrete or continuous) is **less than or equal to a value** $x$: $F(x) = P(X \le x)$.
> 

## Bound

> Concentration Inequality: …
> 

## Relation

- **Joint:** The **joint relation** describes the probability distribution of two or more random variables considered together, capturing how their outcomes occur simultaneously.
- **Conditional:** The **conditional relation** describes the distribution of one random variable given that another random variable takes a specific value, capturing how one variable behaves when the other is known.

## Algebra

> An **algebra on random variables** is a set of random variables that is **closed under certain operations**, typically addition, multiplication, and scalar multiplication.
> 

## Operator

> **Note:** All of these operators come with their own properties, shortcuts, and special rules. What follows is only a list, not a complete treatment.
> 

> Note: Some functions defined in terms of a random variable — such as the **Moment Generating Function** — are not just arbitrary constructions. They are designed to **aid analysis and computation** by transforming the distribution into a more tractable mathematical object. For instance, the MGF encodes all the moments of a distribution, making it easier to compute expectations, variances, and higher-order moments using differentiation. Similarly, characteristic functions, survival functions, and generating functions provide compact representations that simplify proofs, help derive distributions of sums, and make certain probability problems more manageable.
> 

> See more in [Operator](operator.md) & [Statistical Function](statistical-function.md).
> 

> **Note:** The operation on random variables is defined pointwise: it applies to every possible outcome $(X = x, Y = y)$, producing the value $x \,\text{op}\, y$.
> 

| **Category** | **Operation** | **Definition** | **Signature** | **Description** |
| --- | --- | --- | --- | --- |
| **Algebraic** | Scaling & Shift | $Z = aX + b$ | $(X,a,b)\mapsto Z$ | Linear transformation of scale & location. |
|  | Sum | $Z = X + Y$ | $(X,Y)\mapsto Z$ | Convolution of distributions when independent. |
|  | Difference | $Z = X - Y$ | $(X,Y)\mapsto Z$ | Contrast between two variables. |
|  | Product | $Z = XY$ | $(X,Y)\mapsto Z$ | Interaction (e.g., revenue = price × demand). |
|  | Ratio | $Z = X/Y$ | $(X,Y)\mapsto Z,\;Y\neq 0$ | Relative scaling; often heavy-tailed. |
|  | Minimum | $Z = \min(X,Y)$ | $(X,Y)\mapsto Z$ | Earliest/lowest outcome. |
|  | Maximum | $Z = \max(X,Y)$ | $(X,Y)\mapsto Z$ | Latest/highest outcome. |
|  | General Transform | $Z = g(X)$ | $(X,g)\mapsto Z$ | Deterministic mapping (log, square, etc.). |
|  | Linear Combination | $Z = aX + bY$ | $(X,Y,a,b)\mapsto Z$ | Weighted mixture; core of regression & Gaussian models. |
| **Statistical** | Expectation ([**Expected Value**](expected-value.md)) | ${E}[X]=\sum x\,p(x)$ or $\int x\,f(x)\,dx$ | $X\mapsto\mu\in\mathbb{R}$ | Center of mass of the distribution. |
|  | Variance ([Variance](variance.md)) | $\mathrm{Var}(X)=\mathbb{E}[(X-\mu)^{2}]$ | $X\mapsto\sigma^{2}\in\mathbb{R}_{\ge 0}$ | Spread / uncertainty. |
|  | Standard Deviation ([Standard Deviation](standard-deviation.md)) | $\sigma_X = \sqrt{\mathrm{Var}(X)}$ | $X\mapsto\sigma\in\mathbb{R}_{\ge 0}$ | Spread in original units. |
|  | Covariance ([Covariance](covariance.md)) | $\operatorname{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])]$ | $(X,Y)\mapsto c\in\mathbb{R}$ | Joint variability. |
|  | Correlation ([Correlation](correlation.md)) | $\rho(X,Y)=\dfrac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}$ | $(X,Y)\mapsto\rho\in[-1,1]$ | Normalized dependence measure. |
|  | k-th Moment | $\mu'_k=\mathbb{E}[X^{k}]$ | $X\mapsto\mu'_k\in\mathbb{R}$ | Higher-order shape measure. |
|  | Central Moment | $\mu_k=\mathbb{E}[(X-\mu)^{k}]$ | $X\mapsto\mu_k\in\mathbb{R}$ | Variance ($k=2$), skewness ($k=3$), kurtosis ($k=4$). |
|  | Mean | $\mu=\mathbb{E}[X]$ | $X\mapsto \mu$ | Average value of the random variable. |
|  | Coefficient of Variation (CV) | $\mathrm{CV} = \sigma/\mu$ | $X\mapsto \mathrm{CV}$ | Relative variability (unitless). |
| **Joint & Marginal** | Joint Distribution | $(X,Y)\mapsto f_{X,Y}$ | Discrete: $P(X=x,Y=y)$. Continuous: $f_{X,Y}(x,y)$. | Full law of variables together; basis for dependence. |
|  | Marginal Distribution | $f_{X,Y}\mapsto f_X,f_Y$ | Discrete: $P(X=x)=\sum_y P(X=x,Y=y)$. Continuous: $f_X(x)=\int f_{X,Y}(x,y)\,dy$. | Distribution of a subset, ignoring the rest. |
|  | Conditional Distribution | $(X\mid Y)\mapsto f_{X\mid Y}$ | $f_{X\mid Y}(x\mid y)=\dfrac{f_{X,Y}(x,y)}{f_Y(y)},\;f_Y(y)>0$. | Distribution of $X$ once $Y$ is known. |
|  | Independence | $(X,Y)\mapsto\text{bool}$ | $f_{X,Y}(x,y)=f_X(x)f_Y(y)\;\forall x,y$. | Factorization; no dependence between $X$ and $Y$. |
|  | Conditional Independence | $(X,Y\mid Z)\mapsto\text{bool}$ | $f_{X,Y\mid Z}(x,y\mid z)=f_{X\mid Z}(x\mid z)\,f_{Y\mid Z}(y\mid z)$. | Given $Z$, $X$ and $Y$ become independent. |
|  | Joint CDF | $(X,Y)\mapsto F_{X,Y}$ | $F_{X,Y}(x,y)=P(X\le x,Y\le y)$. | Probability both variables fall below thresholds. |
|  | Marginal CDF | $F_{X,Y}\mapsto F_X,F_Y$ | $F_X(x)=\lim_{y\to\infty}F_{X,Y}(x,y)$. | CDF of one variable, ignoring the other. |
|  | Conditional Expectation (restated) | $(X\mid Y)\mapsto\mathbb{E}[X\mid Y]$ | $\displaystyle\mathbb{E}[X\mid Y]=\int x\,f_{X\mid Y}(x\mid Y)\,dx$. | Best predictor of $X$ given $Y$. |
|  |  |  |  |  |
|  |  |  |  |  |
| **Conditional** | Conditional Expectation | $\mathbb{E}[X\mid Y]$ | $(X,Y)\mapsto\mathbb{E}[X\mid Y]$ | Best predictor of $X$ given $Y$. |
|  | Conditional Variance | $\mathrm{Var}(X\mid Y)$ | $(X,Y)\mapsto\mathrm{Var}(X\mid Y)$ | Spread of $X$ given $Y$. |
|  | Law of Total Expectation | $\mathbb{E}[X]=\mathbb{E}[\,\mathbb{E}[X\mid Y]\,]$ | $(X,Y)\mapsto\mathbb{E}[X]$ | Decomposes mean via conditioning. |
|  | Law of Total Variance | $\mathrm{Var}(X)=\mathbb{E}[\mathrm{Var}(X\mid Y)]+\mathrm{Var}(\mathbb{E}[X\mid Y])$ | $(X,Y)\mapsto\mathrm{Var}(X)$ | Decomposes variance into within- and between-group parts. |
| **Order Statistic** | k-th Order Statistic | $X_{(k)}=$ k-th smallest value | $(X_1,\dots,X_n)\mapsto X_{(k)}$ | Basis for quantiles/percentiles. |
|  | Sample Min | $X_{(1)}=\min(X_i)$ | $(X_1,\dots,X_n)\mapsto X_{(1)}$ | Smallest observation. |
|  | Sample Max | $X_{(n)}=\max(X_i)$ | $(X_1,\dots,X_n)\mapsto X_{(n)}$ | Largest observation. |
|  | Median | $Q_{0.5}$ | $X\mapsto m\in\mathbb{R}$ | Middle value; robust to outliers. |
|  | Quantile (Percentile) | $Q_p=\inf\{x:F(x)\geq p\}$ | $(X,p)\mapsto Q_p$ | Value at probability cutoff $p$. |
| **Transforms** | CDF | $F_X(x)=P(X\le x)$ | $X\mapsto F_X:[0,1]$ | Complete description of the distribution. |
|  | PDF / PMF | Discrete: $P(X=x)$, Continuous: $f(x)$ | $X\mapsto f$ | Fundamental probability law. |
|  | MGF | $M_X(t)=\mathbb{E}[e^{tX}]$ | $X\mapsto M_X(t)$ | Generates all moments. |
|  | Characteristic Function | $\varphi_X(t)=\mathbb{E}[e^{itX}]$ | $X\mapsto\varphi_X(t)\in\mathbb{C}$ | Fourier transform of distribution. |
|  | PGF | $G_X(s)=\mathbb{E}[s^{X}]$ | Discrete $X\mapsto G_X(s)$ | Encodes distribution of integer-valued RVs. |
|  | Laplace Transform | $\mathcal{L}\{f\}(s)=\mathbb{E}[e^{-sX}]$ | $X\mapsto\mathcal{L}_X(s)$ | Used in reliability & survival analysis. |
| **Info-Theoretic** | Entropy | $H(X)=-\sum p(x)\log p(x)$ | $X\mapsto H\in\mathbb{R}_{\ge 0}$ | Uncertainty of the distribution. |
|  | KL Divergence | $D_{\text{KL}}(P|Q)=\mathbb{E}_{P}\!\left[\log\frac{P(X)}{Q(X)}\right]$ | $(P,Q)\mapsto D_{\text{KL}}(P|Q)$ | Distance between two distributions. |
|  | Mutual Information | $I(X;Y)=H(X)-H(X\mid Y)$ | $(X,Y)\mapsto I\in\mathbb{R}_{\ge 0}$ | General measure of dependence. |
| **Limits (Convergence)** | a.s. Convergence | $P(\lim_{n\to\infty}X_n=X)=1$ | $X_n\mapsto X$ | Strongest form of convergence. |
|  | In Distribution | $F_{X_n}(x)\to F_X(x)$ at continuity points | $X_n\mapsto X$ | Convergence of distributions; underlies CLT. |
| Similarity Metric | … | … | … | … |

### Expected Value

> The expected value of a random variable is the long-run average value it takes after many repetitions of the experiment.
> 

> **Expected value** = “center” (average outcome).
> 

> See more in [**Expected Value**](expected-value.md).
> 

Formally, for a random variable $X$:

- If **discrete**: $\mathbb{E}[X] = \sum_{x} x \cdot P(X = x)$
- If **continuous**: $\mathbb{E}[X] = \int_{-\infty}^{\infty} x \cdot f(x)\, dx$ where $f(x)$ is the probability density function.

### Variance

> The variance of a random variable measures **how much its values spread around the expected value (mean)**. It is the expected squared deviation from the mean.
> 

> See more in [Variance](variance.md).
> 

Formally: $\mathrm{Var}(X) = \mathbb{E}\big[(X - \mathbb{E}[X])^2\big] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$

### Covariance

> See more in [Covariance](covariance.md).
> 

### Correlation

> See more here [Correlation](correlation.md).
> 

### Characteristic Function

> A characteristic function is a **representation of a random variable’s probability distribution** in the complex exponential domain that enables analysis, manipulation, and reconstruction of the distribution, particularly for studying sums of independent variables, convergence in distribution, and moment extraction.
> 

> See more here [Characteristic Function](characteristic-function.md)**.**
> 

### Probability-Generating Function (PGF)

> The PGF is a **power series representation of a discrete probability distribution**, particularly useful for non-negative integer-valued random variables like counts or number of events. It simplifies **computing probabilities, moments, and studying sums of independent variables**.
> 

> See more in [Probability-Generating Function (PGF)](probability-generating-function-pgf.md).
> 

### Moment-generating Function (MGF)

> The **moment-generating function** of a random variable (X) is a function $M_X(t)$ that **encodes all the moments of (X)**.
> 

> See more in [Moment-Generating Function (MGF)](moment-generating-function-mgf.md).
> 

## ❓ QA

### Why do we have very similar concepts such as probability distributions, laws, and random variables? What value does the idea of a random variable offers?

> See [Why do we have very similar concepts such as probability distributions, laws, and random variables? What value does the idea of a random variable offers?](../discipline/probability.md)
> 

### What does it mean to do operate (sum, multiply, etc.) two random variables?

> What if the two random variables refer to different parts of the process — that is, they come from different sample spaces? Does it make sense?   If the two random variables are completely unrelated in modeling terms (e.g., one is “temperature in Paris today,” another is “number of customers at a store in Beijing”), adding them may not be meaningful as a quantity, even if you can formally do it. The sum is always definable if you build a product space, but the interpretation may be questionable.
> 

> **Operator on Random Variable** must make sure that the random variable; are different outlook of the same random piece of reality; if not we are we wave a type non-check issue.
> 

> A way to think about this; take a random piece of reality;  what is state; random variables view of that space, then you can operate on those random variables.
> 

What does operations on **random variables** $(+, -, *)$ represents?

- The operations on random variables should be seen as manipulating $(X, Y, Z, \dots)$, which capture aspects of the “state of the world.” We then perform operations on these random variables, combining their possible outcomes and associated probabilities.

### How to Interpret X | Y?

> What’s the probability of X given Y? This is just Conditional Probability.
> 

### How to Interpret X + Y?

> The operation on random variables is defined pointwise: it applies to every possible outcome $(X = x, Y = y)$, producing the value $x + y$.
> 

### What does the term random variables denotes? What do we mean in practice when we write  X1, X2, …, Xn?

> Let’s reason about the following hypothetical example. Suppose we have a **sequence of experiments** represented by $X_1, \dots, X_n$, each corresponding to the outcome of a repeated coin flip. Assume the same  **probability space** $(\Omega, \mathcal{F}, P)$, for each trial.
> 

> **Note:** The notation of probability theory is often convoluted. When filling in the details, there is a lot of creativity in how the symbols are interpreted. In different contexts, the same symbols can carry aggregated or slightly different meanings, all for the sake of notational economy.
> 

Interpretation:

- **A random variable is a function** $X: \Omega \to \mathbb{R}$; it is **not inherently “different” across trials, in fact in our case is the same;  by assumption.**
- The “randomness” resides in the outcomes $\omega \in \Omega$, not in the function itself.
- The whole sequence can be considered a single experiment, but we can also view it as a sequence of independent mini-experiments.  Note that both can be represented as random vectors.
- We may call $X_1$ a **random variable**, which is an instance of the convoluted nature  language of probability. $X_1$ represents a single experiment (a trial) and assigns a value according to a given random variable. In fact, all of $X_1, \dots, X_n$ can be mapped by the **same underlying random variable**; what differs is the particular trial outcome that each one evaluates.
- Writing $X_1, \dots, X_n \sim \text{Normal}(\mu, \sigma^2)$ means that each evaluation of the random variable in its respective trial follows the specified distribution, and means i.i.d unless specify otherwise.
- Insisting that $X_1, \dots, X_n$ must be separate functions misses the abstraction: **what matters is which outcome each one evaluates**.

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- [Indirection](https://app.notion.com/p/Indirection-255c0f5171ec80188596ca316d0a11e4?pvs=21)
- https://en.wikipedia.org/wiki/Random_variable
- https://en.wikipedia.org/wiki/Probability_density_function
- https://en.wikipedia.org/wiki/Probability_mass_function
- https://en.wikipedia.org/wiki/Cumulative_distribution_function
- https://en.wikipedia.org/wiki/Continuous_or_discrete_variable
- https://en.wikipedia.org/wiki/Expected_value
- https://en.wikipedia.org/wiki/Variance
- https://en.wikipedia.org/wiki/Concentration_inequality
- https://math.stackexchange.com/questions/14714/characteristic-functions-and-motivations
- https://en.wikipedia.org/wiki/Algebra_of_random_variables
- [‣](https://app.notion.com/p/27c598edb790804abecbd6749d0a6cff?pvs=21)
- https://en.wikipedia.org/wiki/Delta_method
- [Modelling](https://app.notion.com/p/Modelling-334c0f5171ec803e8cfbe7f0bc02c575?pvs=21)
