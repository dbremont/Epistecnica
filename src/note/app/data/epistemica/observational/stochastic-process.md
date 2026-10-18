---
tags: [probability, stochastic-process]
---

# Stochastic Process

 : Lévy Proces (L%C3%A9vy%20Proces%2015fc0f5171ec808895a7d1e75b525ff5.md), Martingale (Martingale%207b5a50c6c4c042b99e85cc9a1c5d643c.md), Filtration (Filtration%2015fc0f5171ec8000a310e17a381d06de.md), Hawkes Process (Hawkes%20Process%20336c0f5171ec802b9302e1fbd7e6066e.md), Marked Point Process (Marked%20Point%20Process%20336c0f5171ec80ca9e39f6f3bbee3493.md)

> A **stochastic process** is formally defined as a **family of random variables** ${X_t}_{t \in T}$ indexed by a parameter (t) (often representing time), which models the evolution of a system under uncertainty - defined  by a given **probability space**.
> 

> **Note:** The term *random variable*—often defined as a mapping from the sample space to the real line—is used loosely in practice; sometimes it is taken to mean just the associated probability law. The terminology in probability theory is notoriously inconsistent and confusing.
> 

> Note: The term ‘family’ fixes the issue  of the common denotation of the term ‘collection of random variables’ .
> 

> **Clarification:** Although texts often speak of a “collection of random variables,” in rigorous probability theory this does not imply completely distinct random variables. Rather, it’s a single underlying random mechanism (X), whose observed value depends on the index (t). The index (t) specifies which “slice” or **manifestation** of the process we are observing.  See [What does the term random variables denotes? What do we mean in practice when we write  X1, X2, …, Xn?](random-variable.md).
> 

> **Note:** A **stochastic process** provides a very general **epistemic mechanism** to model portions of reality—such as processes or phenomena—or, in the most abstract sense, **event streams**  grounded by that reality The variations in the process may either be **intrinsic to the underlying reality** (ontic) or reflect **epistemic uncertainty** due to incomplete knowledge.
> 

> **Note:** There is clever use of stochastic processes—where the sequence of observations encodes a function—so the “process” here actually serves as an inference tool.   One can used them to inference functions building distribution over them.
> 

> Modelling Node:  The abstract formulation of a stochastic process - is not useful in building models - of the ‘event stream ‘
> 

Guiding questions:

- What is the fundamental nature of a stochastic process?
- What are the types of stochastic processes, and how can their type space be rigorously characterized?
- What is the representational capacity of stochastic processes?
- What  is the  affirmation type space about  a stochastic process?
- How can a stochastic process representation be validated against real `event streams`?
- What additional key questions should be considered when analyzing stochastic processes?

## Formulation

> What is a stochastic process?
> 

> What is the fundamental nature of a stochastic process?
> 

> **Note:** In some **random processes**, the **realizations of random variables** can be structured objects (i.e., elements with internal structure). These may be mapped to real values when required, but the underlying structured objects themselves are what carry the relevant information. In the case of Gaussian Processes, observations take the form ($x, f(x) + \text{noise}$), and it is these structured input–output pairs that are used to learn the latent function.
> 

## Process Space

> What are the types of stochastic processes, and how can their type space be rigorously characterized?
> 

### Space

> **The stochastic process space** is a formal representation of all stochastic processes under consideration, organized by categories, types, and their assumed generative structures, providing a structured framework to describe and compare the probabilistic behavior of event streams.
> 

> **Category:** Broad grouping of stochastic processes (e.g., discrete-time, continuous-time, counting processes).
> 

> **Type:** Specific stochastic process within the category (e.g., Bernoulli process, Poisson process).
> 

> **Generator Assumption:** The assumed statistical or structural properties of the underlying generator (ontic substrate responsable for the event stream). These assumptions define how the event stream is represented, without claiming a complete ontic description of the system.
> 

> **Random Walk is not a process,  Martingale is a property.**
> 

| **Category** | **Type** | **Description** | **Generator Assumption(s)** |
| --- | --- | --- | --- |
| **Discrete-Time, Discrete-State** | Bernoulli Process | Sequence of i.i.d. binary variables | Independent trials, fixed probability; **memoryless** |
|  | Binomial Process | Sum of Bernoulli trials over time | Independent, identically distributed; **memoryless** |
|  | Markov Chain | Memoryless property (future depends only on present) | Transition probability matrix; **Markovian (1-step memory)** |
|  | Hidden Markov Model (HMM) | Latent Markov states with observable outputs | Latent Markov states + emission probabilities; **Markovian in latent states** |
|  | Semi-Markov Process | Like Markov chain, but general holding times | Transition kernel + holding time distribution; **duration-dependent memory** |
|  | Pólya’s Urn | Reinforced discrete outcomes | Reinforcement: probability of next draw depends on past outcomes; **long-range memory** |
|  | Ehrenfest Urn | Particle transfer between two urns | Markovian transitions with fixed probabilities; **1-step memory** |
| **Discrete-Time, Continuous-State** | Autoregressive (AR) Process | Linear dependence on past values | Linear combination of finite lags + i.i.d. noise; **finite memory (order p)** |
|  | Moving Average (MA) Process | Dependence on past noise terms | Linear combination of past innovations; **finite memory (order q)** |
|  | ARMA / ARIMA | Combination of AR and MA (integrated for ARIMA) | Stationary increments + differencing; **finite memory + integration** |
|  | GARCH / ARCH Process | Conditional variance depends on past squared innovations | Past squared innovations + i.i.d. noise; **finite memory in volatility** |
| **Continuous-Time, Discrete-State** | Poisson Process | Count process with independent, exponentially distributed interarrival times | Independent increments, stationary; **memoryless** |
|  | Renewal Process | Arbitrary interarrival distributions | i.i.d. interarrival times; **memoryless if exponential, otherwise memory via distribution** |
|  | Compound Poisson Process | Poisson arrivals with random jump sizes | Poisson arrivals + independent jump magnitudes; **memoryless in counts, independent jumps** |
|  | Birth–Death Process | Markovian population dynamics | Transition rates for births/deaths; **1-step memory** |
|  | Queueing Process (M/M/1, etc.) | Markovian queue dynamics | Arrival + service rates, exponential; **1-step memory (Markovian)** |
| **Continuous-Time, Continuous-State** | Brownian Motion (Wiener Process) | Continuous path, normally distributed increments | Independent, stationary Gaussian increments; **memoryless in increments** |
|  | Geometric Brownian Motion | Exponential of Brownian motion | Multiplicative drift + Gaussian diffusion; **memoryless in log-space increments** |
|  | Ornstein–Uhlenbeck Process | Mean-reverting Gaussian process | Linear drift toward mean + Gaussian increments; **Markovian** |
|  | Fractional Brownian Motion | Long-memory generalization of Brownian motion | Self-similar, correlated Gaussian increments; **long-range memory** |
|  | Lévy Process | Stationary, independent increments, may include jumps | Independent, stationary increments; **memoryless in increments** |
|  | Jump-Diffusion Process | Brownian motion + Poisson jumps | Gaussian increments + stochastic jumps; **memoryless in increments, jumps independent** |
|  | CIR (Cox–Ingersoll–Ross) Process | Square-root mean-reverting diffusion | Non-negative, mean-reverting diffusion; **Markovian** |
|  | Vasicek Process | Gaussian mean-reverting process | OU-type with constant volatility; **Markovian** |
|  | Schramm–Loewner Evolution (SLE) | Random conformally invariant curves | Brownian motion driving function, complex analytic structure; **Markovian in driving function** |
| **Point / Counting Processes** | Poisson Point Process | Random points in space/time | Independent, homogeneous/inhomogeneous intensity; **memoryless in time** |
|  | Cox Process (Doubly Stochastic Poisson) | Poisson process with stochastic intensity | Random intensity function; **memory via intensity process** |
|  | Hawkes Process | Self-exciting process | Intensity depends on past events; **explicit memory / self-excitation** |
|  | Marked Point Process | Points with associated marks | Conditional independence of marks; **memory depends on marks** |
|  | Spatial-Temporal Poisson Process | Poisson events over space-time | Independent increments across space/time; **memoryless in space-time** |
| **Function-Valued / Infinite-Dimensional** | Gaussian Process | Every finite collection is multivariate Gaussian | Mean function + covariance kernel; **memory via kernel / correlation structure** |
|  | Dirichlet Process | Distribution over distributions | Infinite-dimensional, exchangeable; **full exchangeability, no explicit temporal memory** |
|  | Gaussian Random Field | Spatial generalization of GP | Covariance over spatial domain; **memory via spatial correlation** |
|  | Student-t Process | Heavy-tailed generalization of Gaussian Process | Multivariate Student-t finite marginals; **memory via covariance structure** |
|  | Markov Random Field | Random field with local dependencies | Local Markov property; **finite-range memory** |
|  | Gibbs Process | Spatial process with energy-based structure | Probability density defined via energy function; **memory via interactions** |
| **Rare / Modern / Specialized** | Lévy Flight | Random walk with heavy-tailed step sizes | Independent heavy-tailed increments; **memoryless in increments** |
|  | Fractional Poisson Process | Non-Markovian Poisson process | Interarrival times with long-range dependence; **long memory** |
|  | Subordinated Process | One stochastic process as time-change of another | Stochastic operational time drives another process; **memory via operational time** |
|  | α-Stable Process | Stable distribution increments | Independent, stationary, heavy-tailed increments; **memoryless in increments** |
|  | Multi-type Branching Process | Branching with multiple types | Generational dependence structure; **finite memory per generation** |
|  | Cox–Ingersoll–Ross Jump | CIR + Poisson jumps | Mean-reverting + stochastic jumps; **Markovian + independent jumps** |

### Affirmation Space

> What  is the  affirmation type space about  a stochastic process?
> 

> The **affirmation space** of a stochastic process is the formal set of all meaningful statements, properties, or predicates that can be asserted about the process. These affirmations can concern distributional properties, temporal dependencies, pathwise properties, asymptotics, extremal behavior, and more.
> 

| **Category** | **Affirmation Type** | **Description** | **Instance** |
| --- | --- | --- | --- |
| **Distributional** | Marginal Distribution | Statement about the distribution of the process at a single time point | $(X_t \sim \text{Normal}(0,1))$ |
|  | Joint Distribution | Statement about the joint distribution at multiple time points | $(X_{t_1}, X_{t_2})$ are bivariate Gaussian with covariance Σ |
|  | Stationarity | Marginals or joint distributions are invariant under time shift | Process has weak stationarity: mean constant, covariance depends only on lag |
|  | Ergodicity | Time averages converge to ensemble averages | Sample mean converges to expected value as $(t \to \infty)$ |
| **Temporal / Dependence** | Memory / Dependence Structure | Assertion about correlations or conditional dependence | Process is Markovian (1-step memory) |
|  | Autocorrelation | Correlation between values at different times | AR(1) process has $(\text{Corr}(X_t, X_{t-k}) = \phi^k)$ |
|  | Long-Range Dependence | Correlation decays slowly | Fractional Brownian motion with Hurst parameter (H > 0.5) |
| **Pathwise / Trajectory** | Continuity | Assertions about sample path continuity | Paths are continuous almost surely (Brownian motion) |
|  | Differentiability | Assertions about smoothness of paths | Ornstein–Uhlenbeck paths are almost nowhere differentiable |
|  | Monotonicity / Boundedness | Constraints on path values | Poisson process is non-decreasing |
| **Extremal / Rare Events** | Maximum / Minimum | Distribution of extrema | Maximum of Brownian motion over [0,T] follows reflected Brownian distribution |
|  | First-Passage / Hitting Time | Probability distribution of time to reach threshold | $(\tau = \inf{t : X_t \ge a})$ |
|  | Tail / Heavy-Tailed Behavior | Assertions about probability of extreme values | α-stable process has infinite variance |
| **Structural / Generative** | Markov Property | Conditional independence structure | Given ($X_t$), the future is independent of the past |
|  | Self-Similarity / Scaling | Scale invariance or fractal property | Fractional Brownian motion: $(X_{ct} \overset{d}{=} c^H X_t)$ |
|  | Exchangeability | Invariance under permutation of indices | Dirichlet process: order of draws does not matter |
| **Stochastic Calculus / Functional** | Martingale Property | Expected future equals current value |  |
|  | Quadratic Variation | Pathwise second-order increment | $[X]_t = t$ for Brownian motion |
|  | Covariation / Cross-Correlation | Relation between two processes | $[X,Y]_t = \int_0^t \rho_s ds$ |
| **Asymptotic / Limit** | Law of Large Numbers | Time or ensemble averages converge | $(\frac{1}{T} \int_0^T X_t dt \to E[X])$ |
|  | Central Limit Theorem | Convergence of normalized sum to Gaussian | $(\sqrt{n}(\bar X_n - \mu) \to N(0, \sigma^2))$ |
|  | Large Deviations | Probability of rare events decays exponentially | $(P(S_n/n > x) \sim e^{-nI(x)})$ |
| **Statistical / Estimation** | Parameter Estimation | Properties of estimators | MLE of λ in Poisson process is consistent |
|  | Hypothesis Testing | Assertions about validity of model | Test H0: process is homogeneous Poisson |
|  | Predictive Distribution | Conditional prediction of future values | Given past data, ($X_{t+1}$) has predictive Gaussian distribution |

## Process Selection

> How does one select the appropriate stochastic process for a given event stream?
> 

> How sensitive are inferences to assumptions about the generator (e.g., Markov, stationarity, memory)?
> 

> How can one compare competing process models in terms of predictive accuracy, interpretability, and computational tractability?
> 

## Model Validation

> How can a stochastic process representation be validated against real `event streams`?
> 

> How sensitive are inferences to assumptions about the generator (e.g., Markov, stationarity, memory)?
> 

## **Stochastic Simulation**

> 

## Long Memory Process

> 

## QA

### Do stochastic process–based models represent the event stream—the observations—or the underlying ontic mechanisms of reality? In other words, are they models of the observations rather than the generating processes?

> **Stochastic process** models are primarily models of the **observations/event streams**, but they can **sometimes** incorporate **assumptions about underlying generative mechanisms**. They rarely provide a complete **ontic description**—they are a formal tool bridging reality and our knowledge of it.
> 

> Even models that incorporate assumptions about generative mechanisms (e.g., memory patterns, dependencies) do not provide an ontic account of these mechanisms—the assumptions capture higher level properties - not ontic structure of the generator.
> 

### When we have a stochastic process representation of the event stream, what types of inferences can one make?

Which others affirmation can be made about the event stream?

- We can **forecast future events** and assign probabilistic measures to their potential occurrence (“materialization potential”).
- We can **construct derived or approximated process representations** of the event stream. For example, we can compute the probability of observing a specific outcome—like one “H” in 10 trials—under the assumed stochastic model.
- Detect deviations from expected stochastic behavior or model assumptions.
- Generate synthetic realizations of the event stream for testing, planning, or “what-if” analyses.
- Infer latent states in partially observed systems (e.g., Hidden Markov Models, Kalman filters).
- Infer parameters of the underlying generative model (e.g., mean, variance, transition rates) from observed data.
- …

## References

- [Stochastic simulation](https://en.wikipedia.org/wiki/Stochastic_simulation)
- [Dynamical System](../mathematical/dynamical-system.md)
- https://en.wikipedia.org/wiki/Stochastic_process
- https://en.wikipedia.org/wiki/Stationary_process
- https://en.wikipedia.org/wiki/Cyclostationary_process
- https://en.wikipedia.org/wiki/List_of_stochastic_processes_topics
- [‣](https://app.notion.com/p/140598edb7908081baf3f5000be015eb?pvs=21)
- https://mathworld.wolfram.com/topics/Time-SeriesAnalysis.html
- [Affirmation Space](https://app.notion.com/p/Affirmation-Space-336c0f5171ec80928f75ddbde09d7121?pvs=21)
