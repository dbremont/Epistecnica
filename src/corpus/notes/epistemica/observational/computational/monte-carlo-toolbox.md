---
tags: [note, probability, simulation, technique]
---

# Monte Carlo Toolbox

> Monte Carlo methods are a family of computational methods that share an underlying methodological principle: the use of random sampling to solve problems, estimate quantities, or study systems that may be difficult to analyze analytically.

> **Note:** The way this principle is usually explained can be operationalized through two complementary components: **sampling** (e.g., direct random sampling, importance sampling, rejection sampling, stratified sampling, etc.) and **sample processing** (e.g., sample averaging, weighted averaging, variance estimation, distribution estimation, convergence analysis, etc.).

> **Note:** Monte Carlo is not a concrete method, but a **methodological paradigm** that, at its core, uses **random sampling** to **construct concrete computational procedures** for **approximating quantities of interest**.

## Formulation

> Monte Carlo methods are a family of computational methods that use random sampling and subsequent sample processing to estimate mathematical quantities, solve computational problems, or investigate the behavior of complex systems.

**Parts:**

- **Random Sampling:** Generate samples from a specified probability distribution or stochastic process.
- **Sample Processing:** Apply computational operations to the generated samples to obtain estimates or characterize the system under study.
  - Compute the sample average of function evaluations to estimate an expected value or integral.
  - Compute sample variance and standard deviation to quantify uncertainty.
  - Construct empirical distributions to approximate probability distributions.
  - Calculate weighted averages to account for unequal sampling probabilities.


## Origins

> The method is older than its name. It began as a way of estimating an integral or a transport problem whose analysis was impossible, invented inside a weapons programme, and only decades later became the machinery of inference — the shift that is why this note is filed under observational at all.

| Work | Year | What it introduced |
| --- | --- | --- |
| Buffon's needle — *Essai d'arithmétique morale* | 1777 | The first quantity obtained by sampling: a needle thrown on a ruled plane estimates $\pi$ — the ancestor of the dartboard method in the case study below. |
| Laplace — *Théorie analytique des probabilités* | 1812 | Expectation read as an integral and estimated by ratios of counts; the analytic frame the method would later invert. |
| Fermi — neutron diffusion at Rome and Los Alamos | 1930s–40s | Neutron histories sampled by hand, then with the FERMIAC analogue machine (1947); unpublished, and the reason the method existed before it had a name. |
| Ulam & von Neumann — solitaire and neutron shielding | 1946 | The modern idea: replace a computation that cannot be done by many trials that can. The name comes from Ulam's uncle, who gambled in Monaco. |
| Metropolis & Ulam — *The Monte Carlo Method* | 1949 | The method named and stated publicly, with the ENIAC runs behind it. |
| Metropolis, Rosenbluth, Rosenbluth, Teller & Teller | 1953 | Sampling from a *distribution* rather than estimating an integral: the acceptance rule later called the Metropolis algorithm. |
| Kahn & Marshall | 1953 | Sample-size reduction as a design problem — variance reduction rather than brute force. |
| Hammersley & Morton — *Poor man's Monte Carlo* | 1954 | The same idea on a lattice gas, and the first accounting of what a given accuracy costs in samples. |
| RAND — *A Million Random Digits* | 1955 | The random stream as a published, reproducible object — the infrastructure the method silently assumed. |
| Hastings — *Biometrika* | 1970 | Asymmetric proposals: the transition rule generalised into Metropolis–Hastings. |
| Kirkpatrick, Gelatt & Vecchi; Černý | 1983, 1985 | Simulated annealing: the sampling rule turned into an optimiser. |
| Geman & Geman — image restoration | 1984 | The Gibbs sampler, as stochastic relaxation on a lattice. |
| Gelfand & Smith | 1990 | Gibbs sampling arrives in Bayesian statistics; the MCMC boom begins. |
| Gordon, Salmond & Smith — bootstrap filter | 1993 | Sequential Monte Carlo: the sample population follows the state through time. |
| Green — reversible jump | 1995 | The chain moves between models, not only within one. |
| Halton; Sobol' | 1960, 1967 | Low-discrepancy sequences: the deterministic cousin that trades randomness for equidistribution. |
| Giles — multilevel Monte Carlo | 2008 | The same estimator at several resolutions, combined to cut cost. |
| Andrieu, Doucet & Holenstein — particle MCMC | 2010 | Unbiased estimators inside the chain: the pseudo-marginal family. |
| Neal; Hoffman & Gelman | 2011, 2014 | Hamiltonian Monte Carlo and NUTS: gradients instead of random walks. |

> Two shifts are visible in the column. The first, from 1949 to 1955, is a method for **integrals and transport**: a hard deterministic computation replaced by many cheap random ones, with the error bought down as $1/\sqrt{N}$ and the cost paid in random digits. The second, from 1983 to 1995, is a method for **inference**: once the target is a probability distribution rather than a number, sampling from it becomes the computation, and the same acceptance rule serves a posterior. The second shift is why the note sits beside the models it is used to infer, rather than beside the approximation methods it mathematically resembles.

## Which are the components of a Monte Carlo method?

| Component | Description |
|---|---|
| **Problem Definition** | Defines the problem to be addressed and the quantity, property, or behavior to be investigated. |
| **Mathematical Formulation** | Expresses the problem in mathematical terms, identifying the relevant functions, variables, parameters, and quantities of interest. |
| **Probability Model** | Specifies the probability distributions, random variables, and stochastic processes underlying the problem. |
| **Sampling Strategy** | Defines how samples are generated or obtained from the specified probability model. |
| **Sample Generation** | Produces the actual sample observations or realizations according to the selected sampling strategy. |
| **Sample Processing** | Defines the computational operations applied to the generated samples, such as averaging, aggregation, weighting, statistical estimation, or optimization. |
| **Estimation Procedure** | Uses the processed samples to construct an estimate or approximation of the quantity of interest. |
| **Uncertainty Quantification** | Evaluates the variability and uncertainty associated with the resulting estimates. |
| **Convergence Assessment** | Examines whether and how the estimates stabilize as the number of samples increases. |
| **Validation** | Evaluates the accuracy, reliability, and consistency of the resulting estimates against analytical solutions, known results, or alternative computational procedures. |


## Operationalization

1. **Problem Definition:** Define the problem, the quantity of interest, and the mathematical formulation.
2. **Probability Model Specification:** Define the probability distributions, random variables, and stochastic processes involved.
3. **Sampling Strategy Selection:** Select the sampling technique (e.g., direct sampling, importance sampling, rejection sampling, stratified sampling).
4. **Sample Generation:** Generate the required random samples.
5. **Sample Processing:** Apply the appropriate computational operations to the generated samples.
6. **Estimation:** Obtain the numerical estimate or approximation of the quantity of interest.
7. **Uncertainty Assessment:** Evaluate sampling error, variance, confidence intervals, and convergence.
8. **Validation:** Assess the reliability and accuracy of the results.


## Which are the sampling strategies?

> Sample processing refers to the computational operations performed on generated samples to extract information, estimate quantities, approximate mathematical expressions, or characterize the behavior of a system.

| Processing Type | Description | Usage |
|---|---|---|
| **Arithmetic Averaging** | Calculate the arithmetic mean of sampled observations or function evaluations. | Estimating expected values and integrals. |
| **Weighted Averaging** | Calculate an average in which observations receive different weights. | Importance sampling and weighted estimation. |
| **Summation / Aggregation** | Combine sampled values through summation or other aggregation operations. | Estimating cumulative quantities and mathematical expressions. |
| **Variance Estimation** | Calculate the variance of sampled observations. | Quantifying dispersion and sampling uncertainty. |
| **Distribution Estimation** | Construct an empirical probability distribution from sampled observations. | Approximating probability distributions and characterizing stochastic behavior. |
| **Quantile Estimation** | Estimate quantiles from the empirical sample distribution. | Estimating medians, percentiles, and distribution thresholds. |
| **Frequency Counting** | Count the occurrence of events or outcomes within the sample. | Estimating event probabilities and occurrence frequencies. |
| **Extremum Estimation** | Identify minimum or maximum values among sampled observations. | Optimization and extreme-value analysis. |
| **Correlation Estimation** | Estimate statistical dependence between sampled variables. | Analyzing relationships between random variables. |
| **Regression / Model Fitting** | Fit statistical or mathematical models to sampled observations. | Parameter estimation and system characterization. |
| **Resampling** | Generate new samples from an existing sample, such as through bootstrap procedures. | Estimating estimator uncertainty and sampling distributions. |
| **Convergence Analysis** | Examine how estimates evolve as the number of samples increases. | Assessing numerical stability and approximation accuracy. |

## Concrete Method Space

| Family | Concrete Monte Carlo Method | Description | Structure (Component Set) |
|---|---|---|---|
| **Monte Carlo Estimation** | Crude Monte Carlo Estimator | Estimates an expected value by evaluating a function over independently sampled observations and calculating their arithmetic mean. | Independent random sampling + Function evaluation + Arithmetic averaging |
| **Monte Carlo Integration** | Monte Carlo Integration | Approximates a definite integral by evaluating an integrand at randomly sampled points within its integration domain. | Domain sampling + Integrand evaluation + Sample averaging |
| **Monte Carlo Estimation** | Importance Sampling Estimator | Estimates an expected value by sampling from a proposal distribution and correcting observations through importance weights. | Proposal-distribution sampling + Function evaluation + Importance weighting + Weighted averaging |
| **Monte Carlo Estimation** | Monte Carlo Probability Estimator | Estimates the probability of an event by simulating outcomes and calculating the proportion satisfying the event condition. | Random sampling + Event evaluation + Frequency counting |
| **Monte Carlo Estimation** | Monte Carlo Variance Estimator | Estimates the variance of a random variable using sampled observations and their deviations from the sample mean. | Random sampling + Sample averaging + Squared deviations + Averaging |
| **Monte Carlo Optimization** | Monte Carlo Optimization | Searches for optimal solutions by evaluating an objective function over randomly generated candidate solutions. | Candidate sampling + Objective evaluation + Extremum selection |
| **Monte Carlo Reliability Analysis** | Monte Carlo Reliability Estimator | Estimates system reliability or failure probability by simulating uncertain system conditions and evaluating system performance. | Random sampling of system inputs + System simulation + Failure-event evaluation + Frequency estimation |
| **Monte Carlo Risk Analysis** | Monte Carlo Risk Estimator | Estimates financial or operational risk by simulating uncertain risk factors and calculating the resulting loss distribution or risk measures. | Random sampling of risk factors + Loss simulation + Loss distribution estimation + Risk-measure calculation |
| **Monte Carlo Sensitivity Analysis** | Monte Carlo Sensitivity Analysis | Investigates how variations in model inputs influence model outputs through repeated stochastic evaluations. | Parameter sampling + Model evaluation + Output analysis + Sensitivity estimation |
| **Adaptive Monte Carlo Integration** | VEGAS Algorithm | Estimates multidimensional integrals by adaptively concentrating sampling in regions that contribute most to the integral. | Adaptive importance distribution + Multidimensional sampling + Integrand evaluation + Iterative distribution refinement + Integral estimation |
| **Adaptive Monte Carlo Integration** | MISER Algorithm | Estimates multidimensional integrals by recursively partitioning the integration domain to reduce sampling variance. | Domain partitioning + Variance estimation + Recursive subdivision + Regional sampling + Integral combination |
| **Markov Chain Monte Carlo (MCMC)** | Metropolis Algorithm | Generates samples from a target probability distribution by proposing state transitions and accepting or rejecting them according to a probability ratio. | Initial-state specification + Symmetric proposal generation + Acceptance-probability calculation + State transition + Chain generation |
| **Markov Chain Monte Carlo (MCMC)** | Metropolis–Hastings Algorithm | Generates samples from a target distribution using an asymmetric proposal distribution and a corresponding acceptance probability. | Initial-state specification + Proposal distribution + Candidate-state generation + Acceptance-ratio calculation + State transition |
| **Markov Chain Monte Carlo (MCMC)** | Gibbs Sampling | Generates samples from a joint probability distribution by successively sampling each variable from its conditional distribution given the remaining variables. | Initial-state specification + Conditional-distribution construction + Sequential variable updates + Markov-chain generation |
| **Markov Chain Monte Carlo (MCMC)** | Slice Sampling | Generates samples from a target distribution by introducing an auxiliary variable and sampling within the resulting horizontal slice of the probability density. | Target-density evaluation + Auxiliary-variable generation + Slice construction + Interval expansion or contraction + State selection |
| **Markov Chain Monte Carlo (MCMC)** | Hamiltonian Monte Carlo (HMC) | Generates proposals using Hamiltonian dynamics to explore probability distributions while reducing random-walk behavior. | Momentum generation + Hamiltonian construction + Numerical trajectory integration + Metropolis acceptance correction + State transition |
| **Markov Chain Monte Carlo (MCMC)** | No-U-Turn Sampler (NUTS) | Implements Hamiltonian Monte Carlo with adaptive trajectory construction, automatically determining the trajectory length through a stopping criterion. | Momentum generation + Hamiltonian integration + Binary trajectory expansion + U-turn detection + Candidate selection + Acceptance correction |
| **Sequential Monte Carlo (SMC)** | Bootstrap Particle Filter | Estimates the evolving probability distribution of a hidden state by propagating particles through a state-transition model and weighting them using observations. | Particle initialization + State propagation + Observation weighting + Weight normalization + Resampling |
| **Sequential Monte Carlo (SMC)** | Auxiliary Particle Filter | Improves particle propagation by using preliminary observation information to select promising particles before the next state transition. | Particle initialization + Auxiliary weighting + Ancestor selection + State propagation + Importance correction + Resampling |
| **Sequential Monte Carlo (SMC)** | Regularized Particle Filter | Estimates a sequential distribution by replacing discrete resampling outcomes with continuous kernel-based particle representations. | Particle propagation + Observation weighting + Weight normalization + Particle resampling + Kernel-based regularization |
| **Monte Carlo Optimization** | Simulated Annealing | Searches for approximate global optima by probabilistically accepting candidate solutions, including worse solutions, according to a gradually decreasing temperature. | Initial-solution specification + Neighborhood generation + Objective evaluation + Temperature scheduling + Probabilistic acceptance + Termination |
| **Monte Carlo Optimization** | Monte Carlo Tree Search (MCTS) | Searches decision trees by repeatedly selecting nodes, expanding possible actions, simulating outcomes, and updating accumulated value estimates. | Tree selection + Node expansion + Playout simulation + Value backpropagation + Action selection |
| **Monte Carlo Optimization** | Cross-Entropy Method | Optimizes an objective function by repeatedly generating candidate solutions, selecting elite candidates, and updating a parameterized sampling distribution. | Initial sampling distribution + Candidate generation + Objective evaluation + Elite selection + Distribution parameter updating |
| **Rare-Event Simulation** | Splitting Method | Estimates rare-event probabilities by progressively replicating simulated trajectories that reach intermediate threshold conditions. | Initial trajectory generation + Intermediate threshold definition + Trajectory evaluation + Particle replication + Probability estimation |
| **Rare-Event Simulation** | Subset Simulation | Estimates rare-event probabilities by decomposing an extremely unlikely event into a sequence of more probable conditional events. | Intermediate event construction + Conditional sampling + Markov-chain generation + Threshold updating + Conditional probability estimation |
| **Stochastic Process Simulation** | Gillespie Direct Method | Simulates the time evolution of a stochastic chemical reaction system by selecting the next reaction and its occurrence time according to reaction propensities. | Reaction propensity calculation + Total propensity calculation + Waiting-time generation + Reaction selection + State updating |
| **Stochastic Process Simulation** | Gillespie First-Reaction Method | Simulates stochastic reaction systems by independently generating candidate waiting times for each reaction and executing the reaction with the earliest occurrence time. | Reaction propensity calculation + Reaction-specific waiting-time generation + Minimum-time selection + Reaction execution + State updating |
| **Stochastic Process Simulation** | Kinetic Monte Carlo | Simulates the evolution of a system of discrete states by selecting transitions according to their rates and advancing the system clock. | Transition-rate calculation + Total-rate calculation + Transition selection + Time advancement + State updating |
| **Quantum Monte Carlo** | Variational Monte Carlo (VMC) | Estimates quantum-mechanical properties by sampling particle configurations from the probability density defined by a trial wavefunction. | Trial-wavefunction specification + Probability-density construction + Particle-configuration sampling + Local-observable evaluation + Statistical averaging |
| **Quantum Monte Carlo** | Diffusion Monte Carlo (DMC) | Projects a quantum state toward the ground state through stochastic imaginary-time evolution of particle configurations. | Initial-wavefunction specification + Imaginary-time propagation + Diffusion sampling + Branching or population control + Ground-state estimation |
| **Quantum Monte Carlo** | Path Integral Monte Carlo (PIMC) | Estimates finite-temperature quantum properties by sampling particle paths in an imaginary-time path-integral representation. | Path-integral representation + Imaginary-time discretization + Path sampling + Observable evaluation + Statistical averaging |
| **Quantum Monte Carlo** | Auxiliary-Field Quantum Monte Carlo (AFQMC) | Represents interacting-particle propagation through auxiliary-field transformations and samples the resulting stochastic fields or walker populations. | Many-body Hamiltonian representation + Auxiliary-field transformation + Field sampling + Walker propagation + Observable estimation |
| **Quantum Monte Carlo** | Green's Function Monte Carlo (GFMC) | Calculates quantum ground-state properties by stochastically propagating configurations through an imaginary-time Green's function. | Green's-function construction + Initial-state specification + Stochastic propagation + Population control + Ground-state estimation |


## Method

### How to evaluate the  Convergence Guarantees?

> Characterize the asymptotic and finite-sample behavior.
> 

> This addresses *how reliable the estimate is*.
> 
- **Law of Large Numbers (LLN)** applicability
- **Central Limit Theorem (CLT)** form: $\sqrt{N}(\hat{\theta}_N - \theta) \Rightarrow \mathcal{N}(0, \sigma^2)$
- **Error rate**:
    - $O(N^{-1/2})$ (classical Monte Carlo)
    - Improved rates under variance reduction
- **Confidence intervals / error bounds**
- **Failure modes**: infinite variance, slow mixing, degeneracy

### How can variance reduction and control techniques improve the efficiency and accuracy of Monte Carlo estimation?

> Identify mechanisms that improve efficiency.
> 

> These characterize *how efficiently* the procedure uses samples.
> 
- Control variates
- Antithetic variates
- Importance sampling design
- Rao–Blackwellization
- Stratification

### How to evaluate the computational resources used by the method?

> Describe operational constraints and performance.
> 

> This fixes *how the procedure behaves in practice*.
> 
- **Time complexity**: cost per sample × number of samples
- **Memory footprint**
- **Parallelizability**:
    - Embarrassingly parallel (i.i.d. MC)
    - Sequential dependence (MCMC)
- **Numerical stability**

### Scope

| **Dimension** | **Scope (What Monte Carlo Can Legitimately Establish)** |
| --- | --- |
| **Type of Knowledge** | Produces **conditional probabilistic knowledge** given an explicit stochastic model and parameterization. |
| **Inference Objective** | Estimates expectations, distributions, moments, and risk measures implied by the assumed data-generating process. |
| **Uncertainty Representation** | Quantifies **risk** when uncertainty is formalized as a probability law. |
| **Model Implications** | Makes explicit the logical and quantitative consequences of formal modeling assumptions. |
| **Counterfactual Analysis** | Supports analysis of “what-if” scenarios under controlled, hypothetical assumptions. |
| **Nonlinearity Handling** | Captures nonlinear effects, path dependence, and interaction effects implied by the model. |
| **High-Dimensional Integration** | Enables numerical evaluation of integrals in moderate to high-dimensional spaces where analytic methods fail. |
| **Comparative Evaluation** | Allows relative comparison of strategies, policies, or designs under identical assumptions. |
| **Internal Consistency Checking** | Tests coherence of a model’s implications (e.g., no-arbitrage pricing, constraint satisfaction). |
| **Sensitivity Analysis** | Assesses sensitivity of outcomes to parameters, shocks, and structural features of the model. |
| **Distributional Insight** | Provides full empirical distributions rather than point estimates. |
| **Numerical Convergence** | Guarantees convergence to model-implied quantities as the number of samples increases. |

### Limitation

| **Limitation** | **Description** | **Mitigation** |
| --- | --- | --- |
| **Slow Convergence** | Error scales as $\mathcal{O}(1/\sqrt{N})$, requiring many samples. | Use **variance reduction techniques** (e.g., importance sampling, control variates). |
| **High Computational Cost** | Expensive sample generation and function evaluation. | Optimize code, use **parallel computing**, or employ **approximate models**. |
| **Curse of Dimensionality** | Performance degrades in very high-dimensional spaces. | Use **dimension reduction techniques** or **sparse grids**. |
| **High Variance** | High-variance functions require more samples for accuracy. | Apply **variance reduction methods** like stratified sampling or antithetic variates. |
| **Randomness & Reproducibility** | Results are stochastic and may vary between runs. | Use fixed random seeds or **quasi-random sequences** (e.g., Sobol sequences). |
| **Complex Distributions** | Sampling from complex distributions can be difficult. | Use **Markov Chain Monte Carlo (MCMC)** or **adaptive sampling techniques**. |
| **Bias in Estimates** | Sampling bias or boundary effects can introduce inaccuracies. | Carefully design sampling strategies and validate results. |
| **Limited Applicability** | Less efficient for low-dimensional or deterministic problems. | Combine with **deterministic methods** (e.g., quadrature for low-dimensional integrals). |
| **Rare Events** | Inefficient for estimating probabilities of rare events. | Use **importance sampling** or **subset simulation**. |
| **Dependence on RNGs** | Quality of random number generators affects results. | Use high-quality RNGs and validate their performance. |
| **Parallelization Challenges** | Load balancing and random number generation in parallel environments. | Use **parallel RNGs** and optimize communication between processes. |
| **Interpretability** | Black-box nature makes debugging and understanding results difficult. | Use **visualization tools** and validate intermediate results. |

## Case Study

> Which concrete **Monte Carlo–derived methods** can be used to solve particular classes of problems?
> 

| **Problem** | **Monte Carlo–Derived Method** | **Description (Concrete Procedure)** |
| --- | --- | --- |
| High-dimensional numerical integration | **Crude Monte Carlo Integration** | Draw i.i.d. samples $x_i \sim p(x)$; estimate $\int f(x)p(x)dx$ by sample mean $\frac{1}{N}\sum f(x_i)$. Converges at $O(N^{-1/2})$ independent of dimension. |
| Variance-dominated integrals | **Importance Sampling** | Sample from proposal $q(x)$ instead of $p(x)$; weight samples by $w(x)=p(x)/q(x)$ to reduce estimator variance. |
| Integrals with localized structure | **Stratified Monte Carlo** | Partition domain into strata; sample independently within each stratum; combine weighted estimates to reduce variance. |
| Sampling from intractable distributions | **Rejection Sampling** | Generate samples from an easy proposal; accept or reject based on density ratios to obtain exact samples from target distribution. |
| Bayesian posterior inference | **Metropolis–Hastings (MCMC)** | Construct a Markov chain whose stationary distribution is the posterior; generate correlated samples to approximate expectations. |
| Large Bayesian models | **Gibbs Sampling** | Sequentially sample conditional distributions of each variable; special case of MCMC with guaranteed acceptance. |
| Dynamic state estimation | **Particle Filters (SMC)** | Maintain weighted particle populations evolving over time; resample to approximate filtering distributions. |
| Rare-event probability estimation | **Splitting / Subset Simulation** | Decompose rare event into sequence of more probable intermediate events; estimate probabilities recursively. |
| Stochastic optimization | **Simulated Annealing** | Use randomized exploration with decreasing noise to approximate global optima of non-convex functions. |
| PDEs with probabilistic representation | **Monte Carlo Walk on Spheres** | Simulate Brownian motion paths to approximate solutions to Laplace and Poisson equations. |
| Uncertainty propagation | **Forward Monte Carlo Simulation** | Sample uncertain inputs; propagate through deterministic model; analyze output distribution. |
| Option pricing (finance) | **Monte Carlo Path Simulation** | Simulate stochastic processes (e.g., GBM) for asset paths; compute discounted payoff expectations. |
| Systems with noisy observations | **Bootstrap (Resampling Methods)** | Randomly resample observed data to approximate sampling distributions and confidence intervals. |
| Estimating π | **Dartboard Monte Carlo** | Randomly generate points in a square; count fraction that falls inside an inscribed circle; estimate π as $4 \times (\text{points in circle})/(\text{total points})$. |
| Predicting outcomes of a dice game | **Random Game Simulation** | Simulate many rounds of the game using random dice rolls; compute probabilities of each possible outcome by relative frequency. |
| Estimating probability of a rare event | **Repeated Random Trials** | Randomly simulate the system many times; count the fraction of simulations where the rare event occurs. |
| Estimating average waiting time in a queue | **Stochastic Queue Simulation** | Randomly generate arrivals and service times; simulate queue evolution; compute average waiting times across multiple runs. |
| Pricing a simple financial option | **Option Payoff Simulation** | Randomly simulate possible future asset prices; compute discounted payoff for each scenario; average to estimate option price. |
| Estimating reliability of a lightbulb | **Lifetime Sampling Simulation** | Sample lifetimes from a probability distribution (e.g., exponential); simulate many bulbs; estimate probability of failure before a given time. |
| Forecasting project duration | **Monte Carlo Schedule Simulation** | Randomly sample task durations; simulate entire project timeline repeatedly; aggregate results to estimate completion probability and expected duration. |
| Testing robustness of a simple rule or policy | **Scenario Sampling** | Randomly perturb input parameters according to uncertainty distributions; apply the rule/policy; aggregate outcomes to evaluate stability and risk. |

## QA

- Which are the competing methods?  [Alternative(s)](monte-carlo-toolbox.md)
- Which are the limitations of the method? [Evaluation](monte-carlo-toolbox.md)
- Monte Carlos methods are a toolbox; Do we have some underlying formulation for all the **tools in the toolbox**?
- Why does does all Monte Carlo based algorithms can be model using integration?
- Why does does all Monte Carlo based algorithms can be model using Expected Value?
- Why does does all Monte Carlo based algorithms can be model using Stochastic Process?

### Are Monte Carlo methods a family of techniques, or a set of methods that share an underlying methodological principle?

> Monte Carlo methods are a family of computational methods that share an underlying methodological principle: the use of random sampling to solve problems, estimate quantities, or study systems that may be difficult to analyze analytically.

### Which are the uses of **Monte Carlo Method**?

| **Use** | **Description** |
| --- | --- |
| **Probabilistic Integration** | Numerical estimation of expectations and integrals, especially in high-dimensional spaces where deterministic quadrature is infeasible. |
| **Stochastic Process Simulation** | Generation of sample paths for time-evolving random systems (e.g., diffusion processes, queues, population models). |
| **Financial Pricing** | Valuation of derivatives and structured products by estimating discounted expected payoffs under risk-neutral measures. |
| **Risk Measurement** | Estimation of distributional risk metrics such as Value at Risk (VaR), Expected Shortfall (ES), and tail probabilities. |
| **Uncertainty Propagation** | Propagation of input uncertainty through deterministic or stochastic models to obtain output distributions. |
| **Bayesian Inference** | Approximation of posterior distributions and marginal likelihoods via sampling (e.g., MCMC, particle methods). |
| **Sensitivity Analysis** | Quantification of how model outputs respond to changes in inputs or parameters. |
| **Rare-Event Estimation** | Estimation of low-probability, high-impact events using specialized sampling schemes. |
| **Optimization and Search** | Solution of complex optimization problems using stochastic exploration (e.g., simulated annealing, stochastic optimization). |
| **Statistical Physics** | Approximation of equilibrium properties and thermodynamic quantities of complex systems. |
| **Reliability Engineering** | Estimation of system failure probabilities and lifetime distributions under uncertain conditions. |
| **Computer Graphics** | Physically based rendering and light transport simulation via random sampling. |
| **Algorithm Analysis** | Performance evaluation of randomized algorithms and probabilistic systems. |
| **Decision Analysis** | Evaluation of expected outcomes and risk profiles of competing decisions under uncertainty. |
| **Simulation** | Generation of synthetic realizations of a system by sampling from an explicitly specified probabilistic model, in order to study its behavior, distributions, and derived quantities when analytical solutions are unavailable. |

## Which are the other methods that can subtiute the monte carlo ones?

| **Category** | **Method** | **Description** | **Use Case** | **Evaluation** (Which are the cons and pros?) |
| --- | --- | --- | --- | --- |
| **Deterministic Methods** | **Quadrature** | Approximates integrals by evaluating functions at specific points. | Low-dimensional integrals |  |
|  | **Finite Element Method (FEM)** | Solves PDEs by discretizing the domain into smaller elements. | Engineering simulations |  |
|  | **Finite Difference Method (FDM)** | Approximates derivatives using a grid. | Solving PDEs in physics/engineering |  |
| **Spectral Methods** | **Spectral Methods** | Represents solutions as a sum of basis functions (e.g., Fourier series). | Problems with smooth solutions |  |
| **Quasi-Random Methods** | **Quasi-Monte Carlo** | Uses low-discrepancy sequences (e.g., Sobol, Halton) for sampling. | High-dimensional integration |  |
| **Sampling Methods** | **Markov Chain Monte Carlo (MCMC)** | Samples from complex distributions using a Markov chain. | Bayesian inference, statistical physics |  |
| **Sparse Methods** | **Sparse Grids** | Reduces the number of points needed for high-dimensional problems. | High-dimensional integration |  |
| **Uncertainty Quantification** | **Polynomial Chaos Expansion (PCE)** | Represents random variables as expansions in orthogonal polynomials. | Uncertainty quantification |  |
| **Machine Learning** | **Surrogate Models** | Uses machine learning (e.g., neural networks) to approximate complex functions. | High-dimensional optimization |  |
| **Analytical Methods** | **Analytical Solutions** | Solves problems using exact mathematical formulas. | Problems with known solutions |  |
| **Particle Methods** | **Particle Methods** | Represents systems as collections of particles and evolves their states. | Fluid dynamics, molecular dynamics |  |
| **Reduced-Order Models** | **Reduced-Order Models (ROMs)** | Approximates high-dimensional systems using lower-dimensional models. | Systems with repetitive behavior |  |
| **Adaptive Methods** | **Adaptive Methods** | Dynamically adjusts sampling or discretization based on problem features. | Problems with localized complexity |  |

## References

**Primary sources**

- Metropolis, N. & Ulam, S. (1949). The Monte Carlo method. *Journal of the American Statistical Association* 44(247), 335–341. https://doi.org/10.1080/01621459.1949.10483310
- Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H. & Teller, E. (1953). Equation of state calculations by fast computing machines. *Journal of Chemical Physics* 21(6), 1087–1092. https://doi.org/10.1063/1.1699114
- Kahn, H. & Marshall, A. W. (1953). Methods of reducing sample size in Monte Carlo computations. *Operations Research* 1(5), 263–278. https://doi.org/10.1287/opre.1.5.263
- Hammersley, J. M. & Morton, K. W. (1954). Poor man's Monte Carlo. *Journal of the Royal Statistical Society B* 16(1), 23–38. https://doi.org/10.1111/j.2517-6161.1954.tb00143.x
- Halton, J. H. (1960). On the efficiency of certain quasi-random sequences of points in evaluating multi-dimensional integrals. *Numerische Mathematik* 2, 84–90. https://doi.org/10.1007/BF01386213
- Sobol', I. M. (1967). On the distribution of points in a cube and the approximate evaluation of integrals. *USSR Computational Mathematics and Mathematical Physics* 7(4), 86–112. https://doi.org/10.1016/0041-5553(67)90144-9
- Hastings, W. K. (1970). Monte Carlo sampling methods using Markov chains and their applications. *Biometrika* 57(1), 97–109. https://doi.org/10.1093/biomet/57.1.97
- Kirkpatrick, S., Gelatt, C. D. & Vecchi, M. P. (1983). Optimization by simulated annealing. *Science* 220(4598), 671–680. https://doi.org/10.1126/science.220.4598.671
- Geman, S. & Geman, D. (1984). Stochastic relaxation, Gibbs distributions, and the Bayesian restoration of images. *IEEE Transactions on Pattern Analysis and Machine Intelligence* PAMI-6(6), 721–741. https://doi.org/10.1109/TPAMI.1984.4767596
- Gelfand, A. E. & Smith, A. F. M. (1990). Sampling-based approaches to calculating marginal densities. *Journal of the American Statistical Association* 85(410), 398–409. https://doi.org/10.1080/01621459.1990.10476213
- Gordon, N. J., Salmond, D. J. & Smith, A. F. M. (1993). Novel approach to nonlinear/non-Gaussian Bayesian state estimation. *IEE Proceedings F* 140(2), 107–113. https://doi.org/10.1049/ip-f-2.1993.0015
- Green, P. J. (1995). Reversible jump Markov chain Monte Carlo computation and Bayesian model determination. *Biometrika* 82(4), 711–732. https://doi.org/10.1093/biomet/82.4.711
- Giles, M. B. (2008). Multilevel Monte Carlo path simulation. *Operations Research* 56(3), 607–617. https://doi.org/10.1287/opre.1070.0496
- Andrieu, C., Doucet, A. & Holenstein, R. (2010). Particle Markov chain Monte Carlo methods. *Journal of the Royal Statistical Society B* 72(3), 269–342. https://doi.org/10.1111/j.1467-9868.2009.00736.x

**Books and surveys**

- Hammersley, J. M. & Handscomb, D. C. (1964). *Monte Carlo Methods*. Methuen.
- Kalos, M. H. & Whitlock, P. A. (2008). *Monte Carlo Methods* (2nd ed.). Wiley.
- Liu, J. S. (2001). *Monte Carlo Strategies in Scientific Computing*. Springer.
- Robert, C. P. & Casella, G. (2004). *Monte Carlo Statistical Methods* (2nd ed.). Springer.
- MacKay, D. J. C. (1998). Introduction to Monte Carlo methods. In *Learning in Graphical Models*, 175–204. Springer. https://doi.org/10.1007/978-94-011-5014-9_7
- Andrieu, C., de Freitas, N., Doucet, A. & Jordan, M. I. (2003). An introduction to MCMC for machine learning. *Machine Learning* 50, 5–43. https://doi.org/10.1023/A:1020281327116
- Neal, R. M. (2011). MCMC using Hamiltonian dynamics. In *Handbook of Markov Chain Monte Carlo*, 113–162. CRC Press. https://arxiv.org/abs/1206.1901
- Hoffman, M. D. & Gelman, A. (2014). The No-U-Turn Sampler. *Journal of Machine Learning Research* 15, 1593–1623. https://arxiv.org/abs/1111.4246

**Sources, links and the note's own trail**

- [FERMIAC](https://www.wikiwand.com/en/FERMIAC) — the analogue machine Fermi and Richtmyer built to mechanise neutron-history sampling
- [Metropolis & Ulam (1949), scan](https://web.williams.edu/Mathematics/sjmiller/public_html/341Fa09/handouts/MetropolisUlam_TheMonteCarloMethod.pdf)
- Bauer, W. F. (1958). The Monte Carlo method. *Journal of the Society for Industrial and Applied Mathematics* 6(4), 438–451. https://doi.org/10.1137/0106028
- [Monte Carlo method — Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method) · [Introduction to Monte Carlo methods](https://austingwalters.com/introduction-to-monte-carlo-methods/) · [video course](https://www.youtube.com/playlist?list=PLLyj1Zd4UWrNwo2LFGDzKmfqvJCocCFTQ)
- https://arxiv.org/abs/2405.16359
- [Sampling](sampling.md) — the sampling side of the toolbox · [Observational](../observational.md) — the scope this shelf serves
