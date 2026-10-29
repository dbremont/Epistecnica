---
tags: [framework]
---

# Probability

 : Statistics (Statistics%20c9d6a53f36a8494eae934a1a14f969da.md), Shannon Information Theory (Shannon%20Information%20Theory%20a22d92f3a8b845698e10e8039544dad3.md), Algorithmic Information Theory (AIT) (Algorithmic%20Information%20Theory%20(AIT)%2002ef38459a5743eeb0726c479584010a.md), High Dimensional Probability (High%20Dimensional%20Probability%20265c0f5171ec80289fb2e3a647f67d14.md), Theory of Probability (Theory%20of%20Probability%20272c0f5171ec80c1bcafcd23a25b4f50.md), Probability Representation Regime (Probability%20Representation%20Regime%20347c0f5171ec8041b866c4a0f4d333aa.md), Variability (Variability%203cdc0f5171ec80939305fbc2587075e7.md)

> Probability is a **formal framework** that enables the representation of systems—whether influenced by the **observer (subject)** or  **inherent stochasticity**—through (model building tools - or description building tools)  , to support, in the most **abstract sense**,  **forecasting** (What is the next state of the system likely to be?) - **prediction** (now-casting) (asociation) (relation) part (predict unknown part from known parts in the current state), **retrodiction or backcasting** (How did we get here? Why are we here?), and **simulation** (How can we generate possible new states or sequences of states?).
> 

> **A probability** is an extremely abstract concept and a fundamental building block of probabilistic modeling. It represents the **weight** or **degree of plausibility** of a specific outcome occurring in a single **instance**, **trial**, or **observation of a system under a fixed background ontic substrate.  (Scientific View).**

In more general settings, where the context may be heterogeneous or non-stationary, this definition no longer suffices and an alternative formulation of probability is required.
> 

> **A probability distribution**  seeks to represent, describe, or **characterize (weight) (ponder)  -  every potential outcome in an situation** in the face of uncertainty—where the **only certainty is the structure of the uncertainty itself**.
> 

> In general, probability provides a universal framework for modeling both stochastic and deterministic systems, including causal structures and related phenomena. For deterministic systems, this use is primarily for the sake of unification, rather than necessity.
> 

> **(**⚠️⚠️⚠️⚠️⚠️**) Note:** In modeling, we often assume that the conditions—the context—of an experiment are stable, such that the probability distribution does not change; see more in - [Context  (**Well-behaved Trial**)](probability.md). Aka, without a **stable ontic background**, the notion of a probability for the experiment vanishes.
> 

> The **practice of probability** is **profound recognition** that the **context–state relation** is non-deterministic, such that a fixed context does not uniquely determine a state but instead induces a structured distribution over possible realizations.
> 

> Note: In some application scenarios, the context is not fixed but continuously evolving. This raises a fundamental challenge: how can models be validated under non-stationary conditions? In such settings, validation shifts from static fit metrics to criteria like predictive coherence, robustness to context drift, and stability of conditional structure.  To me this does not offers **scientific**  understanding  - it’s mere observational fitting.
> 

> This note is a major undertaking—recording my understanding of probability—so some degree of incoherence should be expected.
> 

![image.png](../assets/note/epistemica/observational/probability/image.png)

> **Note:** This perspective focuses on a type of *fixed weighting of possibilities*. Under this view, there may exist more complex constructions, such as sequences of such mechanisms (e.g., Markov chains), where states evolve over time, but the underlying outcome space is still assumed to be fixed.
> 
> 
> However, there are also other mechanisms that go beyond this assumption—frameworks that *generate* or *instantiate* new possible outcomes or variations rather than merely assign weights over a pre-defined set.
> 
> Examples include point processes and other generative or event-based models, where the structure of outcomes is not strictly fixed in advance but can emerge dynamically through the process itself.
> 
> See more in [Probability Representation Regime](probability-representation-regime.md).
> 

## TODO

I need to improve the concept of probably and adjust the intro accordintly:

| Term | Meaning | Appropriate for Probability? |
| --- | --- | --- |
| **Uncertainty** | Lack of certainty about states, events, or outcomes | ★★★★★ |
| **Variability** | Observable differences or fluctuations | ★★★★☆ |
| **Randomness** | Inherent unpredictability | ★★★☆☆ |
| **Stochasticity** | Mathematical randomness in a process | ★★★★★ |
| **Indeterminacy** | Outcome is not uniquely determined | ★★★★☆ |
| **Ignorance** | Missing knowledge | ★★★☆☆ |
| **Incomplete Information** | Partial observation of the system | ★★★★☆ |
| **Partial Knowledge** | Unknown aspects of the system | ★★★★☆ |
| **Ambiguity** | Multiple plausible interpretations or models | ★★★☆☆ |
| **Unpredictability** | Difficulty predicting future states | ★★★☆☆ |
| **Potentiality** | Set of possible future realizations | ★★★★☆ |
| **Possibility** | What may occur (not necessarily probabilistic) | ★★★★☆ |
| **Contingency** | Dependence on uncertain events | ★★★☆☆ |
| **Dispersion** | Statistical spread of values | ★★☆☆☆ |
| **Volatility** | Time-varying variability (finance) | ★★☆☆☆ |

## Meta

> See more in [**✅** Evaluation](https://app.notion.com/p/Evaluation-24ac0f5171ec801f862dd06f6e8fb364?pvs=21).
> 

> Evaluation Framework.
> 

> **Note:** “What’s my study Strategy? Should I Change It?” Only applies from tree’s the forest of knowledge.
> 

> **Note:** Like any other toolset or technique, it needs to be evaluated. When applied, ask yourself: what does it mean to solve this problem?
> 

### **✅** Evaluation

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | ⭐⭐⭐⭐: Strong note. Well-structured, relevant, and insightful, though with minor room for improvement. |
| **Completeness** | ⭐⭐⭐⭐: Covers core probability concepts thoroughly, but lacks depth in advanced topics (e.g., quantum probability, free probability) and practical implementation guidance. |
| **Coherence & Structure** | ⭐⭐⭐⭐⭐: Exceptionally organized with clear hierarchies, logical flow from foundations to applications, and consistent terminology. The separation of Representation vs. Modelling is pedagogically sound. |
| **Epistemic Self-Assessment** | ⭐⭐	Basic |
| **Internalization Self-Assessment** | **⭐⭐⭐ Moderate** – The concept is **understood and occasionally applied**, with **some influence on behavior or reasoning**, but full internalization has not yet occurred. |
| **Should I Reorganize This -in My Content Forest?** | Does having a piece for **Representation** and another for **Modelling** is a **Good Architecture**? In General Design a Better Architecture for This Note.  Remove relation with other notes;  by adding proper entry points from this note to them. |
| **What’s my study Strategy? Should I Change It?** |  |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

> **Probability: Toolbox** `×` **{Problem,  Representation} →  {Representation,  Inference}.**
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | Probability is the calculus that allows us to characterize stochastic systems or processes — that is, to formally **characterizing** the **uncertainty (contingency) (posibility) of their outcomes - $P(x)$, P(X, Y)** or **P(Y | X).** |
| **Evidentia (Evidence) 📊** | Empirical frequency data, repeatable experiments, simulation outcomes, and logical derivations from axioms. In Bayesian contexts, evidence also includes updating beliefs based on observed data via Bayes’ theorem. Verification comes from comparing predictions to real-world event frequencies and coherence in reasoning. |
| **Telos (Intent) 🎯** | To model and reason about uncertainty, enabling prediction, backcasting,  simulation,  decision-making under incomplete information, and risk assessment. Probability provides the language and tools (random variables, distributions, conditional probability) for formalizing and solving uncertainty-related problems. |
| **Gnosis (Understanding) 🧠** | Build a mental representation through layered learning: from intuitive frequency notions → formal axioms → combinatorics → probability distributions → advanced inference frameworks. Foundational prerequisites include set theory, logic, and basic algebra. A strong representation links abstract theory (e.g., sigma-algebras) with procedural skill (e.g., computing conditional probabilities, designing experiments). |
| **Epignosis (Application) 🛠️** | Applied across statistics, AI/ML, finance, engineering reliability, epidemiology, quantum physics, gambling theory, and risk modeling, probability mastery enables not only the formulation of **stochastic models**, hypothesis testing, uncertainty quantification, and optimal decision-making but also a profound understanding that in many **deterministic systems**, probability serves as a language for expressing epistemic uncertainty arising from irreducible complexity and incomplete observability—transforming how we approach prediction and knowledge in complex, non-random processes. |
| **Relatio (Connections) 🔗** | Strong links to statistics, measure theory, combinatorics, information theory, decision theory, stochastic processes, and thermodynamics. Interdisciplinary connections include neuroscience (probabilistic brain models), linguistics (Bayesian language models), and economics (expected utility theory). |
| **Idoneitas (Suitability) 📐** | Effectiveness is measured by predictive accuracy, calibration of probabilities, coherence with axioms, and robustness under model uncertainty. In applied contexts, suitability also depends on computational tractability and interpretability. |
| **Limites (Limits) ⛔** | Assumes well-defined sample spaces and measurable events. Struggles with modeling deep uncertainty, rare events with limited data, and subjective aspects of prior selection in Bayesian methods. Cannot eliminate uncertainty—only describe it. |
| **Contextus (Context) 🌍** | Historically emerged from gambling problems (Pascal, Fermat) → formalized by Laplace → axiomatized by Kolmogorov (1933). In modern science, it underpins statistical inference, ML algorithms, and risk analysis in engineering and policy. |
| **Dynamis (Evolution) 🌱** | Evolving toward richer models: non-classical probability (quantum probability, imprecise probability), probabilistic programming, causal inference, and integration with machine learning for real-time adaptive models. |
| **Critica (Critique) 🔍** | Frequentist vs Bayesian debates on interpretation; limitations in modeling real-world complexity; over-reliance on independence assumptions; misuse in public discourse (e.g., confusing probability with certainty). Some argue it fails to capture true randomness in chaotic or deterministic systems. |
| **Verbum Usus (Language Use) 🗣️** | In everyday speech, often conflated with "possibility" or "chance," sometimes used vaguely (“probably,” “likely”). In technical discourse, tied to precise mathematical meaning. Bayesian communities use “belief” and “credence,” while frequentists speak of “long-run frequencies.” Evolving usage reflects the growth of probabilistic thinking in AI and data science. |

### 🕰️ History

> History of Probability Thinking.
> 

| **Period** | **Place** | **Development** |
| --- | --- | --- |
| Ancient Times | Egypt, Greece | Early ideas of chance and risk in gambling and divination; no formal theory. |
| 16th Century | Italy, France | Renaissance gamblers and mathematicians begin informal studies of odds (e.g., Cardano). |
| 1654 | France | Pascal and Fermat correspond on gambling problems, laying foundations of probability theory. |
| 17th Century | Europe | Huygens publishes first book on probability; concept of expectation introduced. |
| 18th Century | Europe | Bernoulli’s *Ars Conjectandi* formalizes probability; Law of Large Numbers stated. |
| Early 18th Century | France, England | Bayes develops Bayesian inference; de Moivre approximates normal distribution. |
| 19th Century | Europe | Frequentist interpretations develop; Chebyshev inequalities; central limit theorem formalized. |
| Early 20th Century | Global | Kolmogorov axiomatizes probability theory (1933); measure theory foundation. |
| Mid to Late 20th Century | Global | Development of modern statistical inference, stochastic processes, information theory. |
| 21st Century | Global | Computational probability, machine learning, Bayesian methods flourish with big data and AI. |

### 🔬 Field

| Area | Description |
| --- | --- |
| **Foundations of Probability** | Mathematical basis of probability (measure theory, Kolmogorov axioms, σ-algebras). |
| **Random Variables & Distributions** | Study of discrete and continuous random variables, probability distributions, and their properties. |
| **Limit Theorems** | Results about asymptotic behavior, such as the Law of Large Numbers and the Central Limit Theorem. |
| **Stochastic Processes** | Families of random variables indexed by time/space (Markov chains, Poisson processes, Brownian motion). |
| **Martingale Theory** | Special class of stochastic processes with applications in finance, gambling theory, and statistics. |
| **High-Dimensional Probability** | Probability in large dimensions, concentration inequalities, random matrices, geometric aspects. |
| **Extreme Value Theory** | Analysis of the distribution of maxima, minima, and rare events. |
| **Random Matrix Theory** | Behavior of eigenvalues/eigenvectors of large random matrices, with applications in physics and data science. |
| **Geometric Probability** | Probabilistic methods applied to geometric problems, including convex bodies and random polytopes. |
| **Applied Probability** | Modeling real-world random systems (queueing, networks, reliability, epidemiology, finance). |
| **Bayesian Probability** | Probability as degree of belief; Bayesian inference and updating. |
| **Statistical Mechanics & Physics** | Use of probability to model particle systems, phase transitions, and thermodynamic limits. |
| Large Deviations Theory | Large deviations is a branch of probability theory that studies the probabilities of rare events, i.e., events that deviate significantly from the expected behavior. Unlike classical laws of large numbers or the central limit theorem, which describe typical fluctuations, large deviations quantify exponentially small probabilities of atypical events. |

### **💡** Terminology

> Note. A Density is not a probability is a derivative of it; the probability is $d(x)dx$.
> 

> **Meta:** Definitions of probability are almost always circular. It seems that, to define probability meaningfully, we need to introduce examples to ground the concept, because the purely formal definition does not capture the essence of probability.
> 

| Term | Description |
| --- | --- |
| **Chance** | The objective tendency or propensity for a specific outcome to occur in a given context, often thought of as the inherent randomness in a process. |
| **Uncertainty** | A state of incomplete knowledge where the true outcome, value, or state of a system is unknown or only partially known. It can be due to randomness, lack of data, or imperfect models. |
| **Indeterminism** | The idea that not all events are determined by prior causes; some events occur without deterministic necessity, allowing for multiple possible future outcomes. |
| **Likelihood** | In statistics, a function that measures how probable a set of observed data is under different possible parameter values of a model. In common usage, it refers to the subjective or objective plausibility of an event. |
| **Contingency** | The property of events or states that could have been otherwise — they occur in some circumstances but not inevitably, depending on specific conditions or chance. |
| **Randomness** | The lack of pattern, predictability, or deterministic cause in a sequence of events or outcomes, either as an inherent property of a process (ontological randomness) or as a result of limited knowledge (epistemic randomness). |
| **Inference** | Computing things, model parameters, new state probabilites, why (pass states), simulation, etc. |
| **Data Distribution** | A data distribution is the way in which the values of a dataset or random variable are spread or arranged, showing the frequency or probability of each possible outcome. |
| Density | A function that characterizes the relative likelihood of different outcomes for a continuous random variable. The probability of the variable falling within an interval is given by the area under the density curve over that interval. |

### Guide

This note structures the study of the **Probability Toolbox** by focusing on practical modeling, decomposed into three core aspects:

1. **Representation** – How probabilistic knowledge and dependencies are formally expressed.
2. **Inference** – How conclusions, predictions, or decisions are derived from the model.
3. **Computation** – The algorithms and procedures used to perform inference efficiently.

## **Formulation**

> aka.  **Kolmogorov Probabilty Framework.**
> 

> **Kolmogorov probability** is the axiomatic formulation of probability as a measure on a σ-algebra of events over a sample space, grounding uncertainty in rigorous measure theory so that probabilistic reasoning reduces to analysis of measurable sets and integrable random variables.
> 

We consider a **probability setting formalized using Kolmogorov’s axioms**.

Specifically, we define a **probability space** $(\Omega, \mathcal{F}, P)$, where:

1. $\Omega$ is the **sample space**, representing all possible outcomes of an experiment.
2. $\mathcal{F}$ is a **σ-algebra** of events, i.e., a collection of subsets of $\Omega$ closed under complementation and countable unions.
3. $P: \mathcal{F} \to [0,1]$ is a **probability measure** satisfying:
    - **Non-negativity:** $P(A) \ge 0$ for all $A \in \mathcal{F}$,
    - **Normalization:** $P(\Omega) = 1$,
    - **Countable additivity:** For any countable sequence of disjoint events $A_1, A_2, \dots \in \mathcal{F}$, 
    $P\Big(\bigcup_{i=1}^\infty A_i\Big) = \sum_{i=1}^\infty P(A_i).$

Within this framework:

- **Experiment:** A procedure or action that generates an outcome from a well-defined set of possible outcomes. Mathematically, it corresponds to generating an outcome $\omega \in \Omega$.
- **Outcome:**  A single element of the sample space.
- **Event:** A subset of the sample space, $A \subseteq \Omega$, representing a condition we can ask about regarding the experiment.

### Notation

| **Category** | **Symbol** | **Meaning** |
| --- | --- | --- |
| **Basic Probability** | $P(A)$ | Probability of event $A$ |
|  | $A^c, \neg A$ | Complement of event $A$ |
|  | $A \cap B$ | Intersection: both $A$ and $B$ occur |
|  | $A \cup B$ | Union: either $A$ or $B$ occurs |
|  | $\emptyset$ | Empty event, probability 0 |
|  | $\Omega$ | Sample space: all outcomes of an experiment |
|  | $\mathcal{F}$ | σ-algebra: set of measurable events |
|  | $I_A(\omega)$ | Indicator function of $A$ |
| **Random Variable** | $X$ | Random variable |
|  | $x$ | Specific value of a random variable |
|  | $X \sim D$ | $X$ is distributed as $D$ |
|  | $p_X(x)$ | Probability mass function (discrete) |
|  | $f_X(x)$ | Probability density function (continuous) |
|  | $F_X(x)$ | Cumulative distribution function |
|  | $\mathbb{E}[X]$ or $E[X]$ | Expected value / mean |
|  | $\mathrm{Var}(X)$ | Variance |
|  | $\mathrm{Std}(X)$ | Standard deviation |
|  | $\mathrm{Cov}(X,Y)$ | Covariance between $X$ and $Y$ |
|  | $\mathrm{Corr}(X,Y)$ | Correlation coefficient |
| **Conditional Probability** | $P(A \mid B)$ | Probability of $A$ given $B$ |
|  | $P(B \mid A)$ | Probability of $B$ given $A$ |
|  | $P(A,B)$ | Joint probability of $A$ and $B$ |
|  | $P(A) = \sum_B P(A \mid B) P(B)$ | Law of total probability |
|  | $\pi(\theta)$ | Prior distribution in Bayesian statistics |
|  | $p(x \mid \theta)$ | Likelihood of data given parameter |
|  | $p(\theta \mid x)$ | Posterior distribution |
| **Multiple Random Variables** | $X, Y$ | Random variables (joint modeling) |
|  | $p_{X,Y}(x,y)$ | Joint PMF/PDF |
|  | $f_{X \mid Y}(x \mid y)$ | Conditional PDF |
|  | $p_X(x) = \sum_y p_{X,Y}(x,y)$ | Marginal PMF |
|  | $f_X(x) = \int f_{X,Y}(x,y) dy$ | Marginal PDF |
|  | $X \perp Y$ | $X$ independent of $Y$ |
| **Expectation & Operators** | $\mathbb{E}[g(X)]$ | Expected value of a function of $X$ |
|  | $\mathrm{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$ | Variance formula |
|  | $\mathbb{E}[X \mid Y]$ | Conditional expectation |
|  | $\mathrm{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$ | Covariance formula |
| **Stochastic Processes** | $X(t)$ | Random process at time $t$ |
|  | $\{X_t\}_{t \in T}$ | Collection of random variables indexed by $T$ |
|  | $\mathbb{E}[X_t]$ | Mean function at time $t$ |
|  | $\mathrm{Cov}(X_s, X_t)$ | Covariance function |
|  | $X_t \sim \text{i.i.d.}$ | Independent and identically distributed |
|  | $X_t \sim \text{Markov}$ | Markov property: future depends only on present |
|  | $f_{X_{t+1} \mid X_t}(x_{t+1} \mid x_t)$ | Transition probability density |
| **Special Functions & Distributions** | $\phi(x)$ | Standard normal PDF |
|  | $\Phi(x)$ | Standard normal CDF |
|  | $\Gamma(\cdot)$ | Gamma function |
|  | $\text{Binomial}(n,p)$ | Binomial distribution |
|  | $\text{Poisson}(\lambda)$ | Poisson distribution |
|  | $\text{Exp}(\lambda)$ | Exponential distribution |
|  | $\text{Normal}(\mu,\sigma^2)$ | Gaussian / Normal distribution |

### Corollary

> Can I See the **beauty** of these derivations?
> 

| **Corollary** | **Statement** |
| --- | --- |
| $P(\emptyset) = 0$ | Probability of the empty set is zero. |
| $P(A^c) = 1 - P(A)$ | Probability of the complement of $A$. |
| $P(A) = P(A \cap B) + P(A \cap B^c)$ | Intersection Partition Rule |
| $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Inclusion-Exclusion Principle |
| $P(A∪B∪C)=P(A)+P(B)+P(C)−P(A∩B)−P(A∩C)−P(B∩C)+P(A∩B∩C)$ | Inclusion-Exclusion Principle |
| $P(A \cap B) \leq P(A)$ and $P(A \cap B) \leq P(B)$ | Probability of intersection cannot exceed probability of each event. |
| If $A$ and $B$ are disjoint, $P(A \cap B) = 0$ | Disjoint events have zero intersection probability. |
| $P(A) \leq 1$ | Probability of any event is at most 1. |
| If $A \subseteq B$, then $P(A) \leq P(B)$ | Monotonicity of probability. |
| If $A$ and $B$ are disjoint, $P(A \cup B) = P(A) + P(B)$ | Additivity for disjoint events. |
| $P\left(\bigcup_{i=1}^\infty A_i\right) \leq \sum_{i=1}^\infty P(A_i)$ | Subadditivity (for any countable union). |
| $P(A^c \cap A = \emptyset)  = 0$ | … |

### Property

> See [Property](https://app.notion.com/p/Property-271c0f5171ec80498865e3db652beafb?pvs=21) and [Independence](independence.md).
> 

> Which are the **`properties`** associated with the **elements** of **probability theory**?
> 

| **Element** | **Properties** |
| --- | --- |
| **Sample Space ($\Omega$)** | - Exhaustive: contains all possible outcomes
- Elementary events are mutually exclusive |
| **Event ($A, B, …$)** | - Subset of sample space: $A \subseteq \Omega$
- Complement exists: $A^c$
- Closed under union/intersection: $A \cup B, A \cap B$ |
| **Probability Function ($P$)** | - Non-negativity: $P(A) \ge 0$
- Normalization: $P(\Omega) = 1$
- Additivity: $P(\cup_i A_i) = \sum_i P(A_i)$ for mutually exclusive $A_i$
- Complement: $P(A^c) = 1 - P(A)$
- Inclusion-exclusion: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **Random Variable ($X, Y, …$)** | - Mapping: $X: \Omega \to \mathbb{R}$
- Measurability ensures well-defined probabilitie
- Defined by PMF/PDF |
| **Independence** | - Multiplicativity: $P(A \cap B) = P(A) P(B)$
- Extends to multiple events for mutual independence |
| **Independent and identically distributed random variables (i.i.d)** | A set of random variables that are all independent of each other and follow the same probability distribution. |

### Principle

> A **probability principle** is a fundamental concept or rule that underpins the mathematical study and analysis of random events and their likelihoods.
> 

| **Principle** | **Description** |
| --- | --- |
| **Statistical Inference** | Use data to estimate parameters and update beliefs about the system. |
| **Capturing Variability and Noise** | Reflect inherent variation and measurement noise in observations. |
| **Probabilistic Prediction and Reasoning** | Provide likelihoods, confidence levels, and risk assessments rather than single predictions. |
| **Assumptions About Data** | Depend on assumptions such as independence, stationarity, or known distribution forms. |
| **Laplace Rule (Rule of Succession)** | Provides a method for calculating probabilities when no prior information is available. |
| **Principle of Indifference** | Without relevant evidence, all outcomes should be considered equally likely. |
| **Chebyshev's Inequality** | Bounds the probability that a random variable deviates from its mean by more than a given number of standard deviations. |
| **Markov's Inequality** | Gives an upper bound on the probability that a non-negative random variable exceeds a specific value. |
| **Law of Total Expectation** | The expected value of a random variable can be computed by conditioning on different events and summing the results. |
| **Independence Principle** | Two events are independent if the occurrence of one does not affect the probability of the other. |
| **Total Probability Rule** | The probability of an event can be found by considering all possible ways it can occur. |
| **Complementarity Principle** | The probability of an event is one minus the probability of its complement. |
| **Additivity Principle** | For mutually exclusive events, the probability of either occurring is the sum of their probabilities. |
| **Central Limit Theorem** | The sum (or average) of many independent, identically distributed variables tends toward a normal distribution. |
| **Law of Large Numbers** | As the number of trials increases, the relative frequency of an event converges to its probability. |
| **Principle of Maximum Entropy** | The **principle of maximum entropy**, in the context of **statistical mechanics** and **information theory**, states that, when estimating a **probability distribution** with incomplete information, the distribution should be chosen to be as uniform as possible (**maximizing entropy**) while still satisfying the given constraints, reflecting the principle of maximum ignorance about the unknown information. |
| **Simulation-Guided Model Understanding** | Building analytical probabilistic models and understanding them is hard. One effective way to grasp these models is to simulate them, decomposing the model into a simpler stochastic core plus non-stochastic components. |

### Context  (**Well-behaved Trial**)

> Aka, without a **stable ontic background**, the notion of a probability for the experiment vanishes.
> 

> A **well-behaved trial** is a repeatable experiment conducted under fixed and controlled conditions such that the probability of each outcome is stable and well-defined.
> 

> **Note:** A key element in the practice of probability is the notion of *context*, which is implicit in all modeling. Formally, probabilities should be understood as conditioned on a contextual structure:  $P(\text{State} \mid \text{Context}, \text{Situation})$.
> 

> In practice, when we write $P(\text{State})$, we are implicitly referring to $P(\text{State} \mid \text{Context})$. The context is assumed fixed for tractability and therefore omitted from the notation, but it is always conceptually present.
> 

> By *context*, we mean the ontic substrate or generative conditions that stabilize the probability distribution. Under a fixed context, the distribution over outcomes is invariant; changes in context induce changes in the distribution.
> 

> See  more in [Context-State Relation](https://app.notion.com/p/Context-State-Relation-33fc0f5171ec8057ac4ff9342e814a98?pvs=21).
> 

### Random Object

> How can we encode sample spaces (especially non-numeric ones) using numbers to facilitate operations?
> 

> A fundamental concept that maps the sample space, outcomes, and events to a numerical domain, either simple or complex,  facilitating the certain numerical computations, like expectation etc.
> 

> See more [Distribution](distribution/distribution-2.md),  [Random Object](random-object.md) and [Statistical Function](statistical-function.md).
> 

### Join Probability

> **Joint probability** quantifies the likelihood that two (or more) events occur simultaneously. For events (A) and (B), the joint probability is denoted as $P(A \cap B)$  and represents the probability that both (A) and (B) happen together.
> 

> When (A) and (B) are independent, $P(A \cap B) = P(A) \cdot P(B)$; otherwise, their joint probability captures any dependence or interaction between the events.
> 

> **Extension:** For multiple events $(A_1, A_2, \dots, A_n)$, the joint probability $P(A_1 \cap A_2 \cap \dots \cap A_n)$ describes the likelihood that all events occur simultaneously, forming the foundation for multivariate probability modeling.
> 

> **Note:** The distributions governing each event do not need to be the same; joint probability only requires a well-defined joint distribution that describes how the events relate to each other.
> 

> In practice, real-world systems are almost always **high-dimensional**, involving several interacting random variables. To formally encode both the uncertainty in each variable and the dependencies among them, one models the system using a **joint probability distribution**. This joint distribution serves as the foundational representation from which marginals, conditional probabilities, simulations, and inferences can all be derived.
> 

### Conditional Probability

> aka. **Influence Measure.**
> 

> Let’s explore another fundamental notion in probability: conditioning, which captures the probability of an event $A$ given that another event $B$ has occurred. That is if B has occur;   which are the numbers of time that we also see A.
> 

> **Conditional probability** is the probability of an event $A$ occurring given that another event $B$ has already occurred, defined as $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$, where $P(B) > 0$.
> 

> **History:**  Emerging from 17th-century analyses of games of chance by Pascal and Fermat, the concept of conditional probability evolved through Bernoulli’s combinatorial reasoning and Bayes–Laplace’s formulation of inference under partial information, ultimately attaining its rigorous measure-theoretic definition within Kolmogorov’s 20th-century axiomatization of probability.
> 

### Bayesian Theorem

> See more in [**Bayes’ Theorem**](bayes-theorem.md).
> 

### Law of Total Probability

> The **law of total probability** states that the probability of an event $A$ can be found by summing its conditional probabilities over a complete partition of the sample space, weighted by the probabilities of the partition events.
> 

Suppose we have a sample space $\Omega$, and let $B_1, B_2, \ldots, B_n$ be a **partition** of $\Omega$. That means:

1. $B_i \cap B_j = \varnothing$ if $i \neq j$ (they don’t overlap).
2. $\bigcup_{i=1}^n B_i = \Omega$ (they cover the whole space).
3. Each $B_i$ has nonzero probability: $\Pr(B_i) > 0$.

Then, for any event $A$:

- $A = \bigcup_{i=1}^n (A \cap B_i)$.
- $\Pr(A) = \sum_{i=1}^n \Pr(A \cap B_i)$,
- $\Pr(A) = \sum_{i=1}^n \Pr(A \mid B_i) \Pr(B_i)$.

## Representation Theory

> How to build probability models? It’s an art.
> 

> Probability is a **formal framework** that enables the representation - description of  **stochastic pieces of reality** (systems and `events`) —or observer-induced stochasticity—through simulation or formal modeling, to support, in the most **abstract sense**,  **forecasting** (What is the next state of the system likely to be?) - **prediction** (now-casting) (asociation) (relation) part (predict unknown part from known parts in the current state), **retrodiction or backcasting** (How did we get here? Why are we here?), and **simulation** (How can we generate possible new states or sequences of states?).
> 

![image.png](../assets/note/epistemica/observational/probability/image-1.png)

> Note: **Almost `Any System`** can be model with **probability**, even if there is no inherent stochasticity in it,  just **observer stochastic**. In applying probability to non-stochastic systems, we do not model inherent randomness, but rather quantify the profound epistemic uncertainty arising from the irreducible complexity and incomplete observability of deterministic processes, transforming probability from a measure of chance into a language for the boundaries of human knowledge.  See more here [Suppose we have a function f(x). How should we interpret a probabilistic model of P(f(x)∣x)?](probability.md)
> 

### Representation Target

> What is the general structure of the **`system be represented (representation target)` of** probability theory?
> 

> The **representation target** defines the **general structure** through which a system is modeled or described. It specifies **what aspects of the system are captured** and **how they are encoded**, providing a framework for analysis and prediction.
> 

> Note (Case):  In a car repair station, the **state space** can be viewed as the set of all cars currently in the station, each with its own condition or configuration (e.g., specific faults, repair status). The **dynamic law** governs how this **set of cars changes over time**—for example, cars arriving at the station, cars being repaired and leaving, or cars moving between different repair stages. It captures the evolution of the entire system’s state rather than just changes within an individual car. Probability can then model uncertainties such as the arrival rate of cars, the distribution of repair times, or the order in which cars are serviced.
> 

**Concepts for Structuring the Formulation of the Representation Target**

- **Process:** Represents the overarching evolution of the system over time.
- **Phenomena:** Observable patterns, events, or outcomes that emerge from the process.
- **State:** Encodes the current condition or configuration of the system at a given moment.
- **Dynamics:** Formal rules or laws governing how the state evolves over time.
- **Control Variables:** External inputs or interventions that can influence the system’s behavior or trajectory.

### Representation Signature Syntax

> Note: This is only the model signature; not the structure itself.
> 

> Which are the mathematical syntactical forms in which a probability model can be express?
> 

| **Form** | **Syntactic Expression** | **Description** | **Uses** |
| --- | --- | --- | --- |
| **Uncoditional probability** | $P(X)$ | Probability distribution of a variable $X$. | Describe the overall uncertainty of a variable without conditions. |
| **Conditional probability** | $P(Y \mid X)$ | Probability of $Y$ given $X$. | Modeling dependencies, causal inference, Bayesian updating. |
| **Joint probability** | $P(X, Y)$ or $P(X \land Y)$ | Distribution over multiple variables simultaneously. | Captures co-occurrence patterns, basis for factorization. |
| **Disjunctive probability** | $P(X \lor Y)$ | Probability of the union of events. | Risk aggregation, reliability analysis. |
| **Complementary probability** | $P(\neg X)$ | Probability that an event does not occur. | Modeling failure rates, binary classification. |
| **Bayesian inversion** | $P(X \mid Y) \propto P(Y \mid X) P(X)$ | Bayes’ rule form. | Statistical inference, evidence updating. |
| **Density form** | $p(x)$ | Probability density function (continuous case). | Modeling continuous variables, likelihood functions. |
| **Cumulative form** | $F(x) = P(X \leq x)$ | Cumulative distribution function. | Quantiles, medians, threshold probabilities. |
| **Factorized form** | $\prod_i P(X_i \mid \text{parents}(X_i))$ | Factorization in graphical models. | Efficient modeling of high-dimensional systems. |
| **Measure-theoretic form** | $P(A) = \int_A d\mu$ | Abstract measure-theoretic definition. | Foundations of probability, advanced theory, rigorous proofs. |

### Inference

> What inferences can we make from a probability representation or from raw pieces of reality? What are the tools used to make these inferences?
> 

> What kinds of **‘questions’** can the **probabilistic model** $L_m$ answer? How does it **answer** it them?  In a stochastic system, we infer probabilities, **expected behaviors**, **variability**, **hidden states**, and **governing mechanisms and parameters**—but never exact future outcomes. The focus is on distributions, likelihoods, and uncertainty management, not deterministic prediction.
> 

> What is the representation capacity of a **probabilistic**  **model** $L_m$?   A **probabilistic model** is a **representation** of a **stochastic system** — i.e., a system whose behavior involves inherent randomness — using **probability distributions** over possible outcomes, states, or events.
> 

> See: [(Statistic) Estimator](statistic-estimator.md) and  [Operator](operator.md).
> 

> See [Probability is a **formal framework** that enables the representation of systems—whether influenced by the **observer (subject)** or  **inherent stochasticity**—through (model building tools - or description building tools)  , to support, in the most **abstract sense**,  **forecasting** (What is the next state of the system likely to be?) - **prediction** (now-casting) (asociation) (relation) part (predict unknown part from known parts in the current state), **retrodiction or backcasting** (How did we get here? Why are we here?), and **simulation** (How can we generate possible new states or sequences of states?). ](probability.md)
> 

| **Type of Method** | **Key Question** | **Tools** |
| --- | --- | --- |
| **📊 Descriptive Inference** | What is the average behavior over time or many realizations? | Expected values (means), moments analysis |
|  | How much variability does the system exhibit? | Variance, higher-order moments (skewness, kurtosis) |
|  | What are the higher moments (e.g., skewness, kurtosis)? | Moment analysis, statistical distribution fitting |
|  | What is the long-run or stationary distribution over states (if it exists)? | Stationary distribution estimation |
| **🎲 Simulation (What could happen?)** | What are possible behaviors or outcomes of the system? | Simulation methods (Monte Carlo, scenario analysis) |
| **🔮 Prediction (What is likely to happen?)** | What is the probability of future or unobserved outcomes? | Probabilistic forecasting, Bayesian prediction |
|  | What is the probability of a future state given current observations? | Markov transition probabilities |
| **🧩 Structural Inference** | What are the unknown parameters governing the system (e.g., transition probabilities, noise parameters)? | Parameter estimation, maximum likelihood, Bayesian inference |
|  | Which stochastic process model best describes the system (e.g., Markov chain, Poisson process)? | Model selection, information criteria (AIC, BIC) |
|  | What is the most probable sequence of hidden states when the system is only partially observed? | State-space inference, hidden Markov models (HMM) |
|  | What are the transition probabilities between states in Markov models? | Transition matrix estimation, empirical probability estimation |
|  | What are the dependencies or causal relations among variables? | Correlation analysis, graphical models (Bayesian networks) |
|  | Given observations, what are the most likely hidden states, causes, or parameters? | Expectation-maximization (EM), particle filtering |
| **🔗 Causal Inference** | What is the effect of intervening or perturbing the system inputs? | Randomized experiments, propensity score matching |
|  | How do such interventions change the distribution of outputs? | Counterfactual analysis, structural equation modeling |
|  | What assumptions are necessary to identify causal effects (e.g., conditional independence)? | Causal graphs, do-calculus, sensitivity analysis |
| **❓ Uncertainty Quantification** | What are confidence or credible intervals for predictions or parameters? | Bootstrap methods, Bayesian credible intervals |
|  | How does uncertainty propagate through the system over time? | Monte Carlo error propagation, ensemble forecasting |
| **⏪ Backcasting** | What past conditions or events led to the current state? | Inverse modeling, historical data reconstruction |
|  | How could the system have evolved to reach its present state? | Path analysis, reverse-time simulations |

### **Representation Toolbox**

> How can we represent stochastic systems or phenomena?
> 

> In this section, we explore a set of model classes — canonical representations of different aspects of stochastic reality. These forms provide a structured way to capture uncertainty, dependencies, and variability in complex systems.
> 

> **Formal representations of stochastic systems** are mathematical or probabilistic models used to describe and analyze the behavior of systems that exhibit randomness or uncertainty.
> 

> **Mathematical Representation:**  Mathematical representations describe stochastic systems using formal equations and structures. Examples include probability distributions (discrete or continuous), stochastic differential equations (SDEs), Markov chains, and Poisson processes. These representations allow precise reasoning about system behavior, derivation of analytical properties, and formulation of expectations, variances, and higher-order moments. They provide a foundation for theoretical analysis, control, and optimization of stochastic systems.
> 

> **Algorithmic Representation:** Algorithmic representations focus on computational procedures for simulating or approximating the behavior of stochastic systems. Examples include Monte Carlo simulations, random number generation, stochastic optimization algorithms, and agent-based models. These representations enable experimentation, prediction, and scenario analysis when closed-form mathematical solutions are intractable. Algorithmic models are particularly useful for complex systems where the stochastic dynamics emerge from interactions of multiple components.
> 

> **Structural Representation:** Structural representations of stochastic systems capture the underlying mechanisms and relationships that generate the observed randomness. These include state-space models that define system states and their transitions, often represented through transition matrices in Markov processes or stochastic differential equations in continuous systems. Graphical models like Bayesian networks or Markov random fields visually encode conditional dependencies between random variables. Hierarchical models organize variables at different levels of abstraction, showing how macro-level randomness emerges from micro-level stochastic components. These representations aim to uncover the generative process behind the observed data, enabling deeper understanding and prediction of system behavior.
> 

> **Superficial Representation:** Superficial representations focus on the observable manifestations of stochastic systems without necessarily revealing their underlying structure. These include sample paths or realizations that show specific sequences of system states over time, statistical summaries like means, variances, and autocorrelation functions that capture key properties of the system's behavior, and empirical distributions derived from observed data. Visual representations such as time series plots, histograms, and scatter plots provide intuitive ways to understand the system's behavior. While these representations are valuable for analysis and communication, they typically do not explicitly show the mechanisms generating the randomness, making them more descriptive than explanatory.
> 

Building Blocks:

> **Note:** To build complex representations, we derive them through compositions of simpler representations.
> 

> [Random Object](random-object.md): – An entity whose value is **not deterministic** but governed by a probability distribution; can be a variable, vector, or more complex structure.
> 

> [Statistical Function](statistical-function.md):  A function or transformation that **acts on random objects or distributions**, producing new objects or modifying their properties (e.g., sum, scaling, convolution).
> 

> [Distribution](distribution/distribution-2.md):  A formal description of the **probabilistic behavior of a random object**, specifying the likelihood of different outcomes.
> 

**Model Taxonomy**

> **Model Type:** abstract, general, reusable system definition.
> 

> **Model Instance:** concrete, dataset-specific, fully parameterized model ready for prediction or generation.
> 

| **Model Type** | **Description** | **Representation  (Mathematical Formulation) Ontology** | **Evaluation** | **Optimization** | **Enable** |
| --- | --- | --- | --- | --- | --- |
| **Naive Bayes** | Conditional independence graph (simple DAG) |  | Maximize $p(Y \mid X)$ or full $p(X, Y)$ | Maximum Likelihood Estimation (MLE) | Prediction, Generation |
| **Bayesian Network** | Directed Acyclic Graph (DAG) over variables |  | Maximize likelihood or posterior over parameters/structure | EM, MCMC, Variational Inference | Prediction, Forecasting, Backcasting, Generation |
| **Markov Random Field** | Undirected graph (Markov blanket dependencies) |  | Maximize log-likelihood of $p(X)$ | Contrastive Divergence, Gibbs Sampling | Prediction, Generation |
| **Hidden Markov Model (HMM)** | Chain-structured latent variables with emissions |  | Maximize joint likelihood $p(X, Z)$ | Expectation-Maximization (Baum-Welch) | Prediction, Forecasting, Backcasting, Generation |
| **Gaussian Mixture Model (GMM)** | Mixture of Gaussians with latent assignments |  | Maximize marginal likelihood $p(X)$ | EM, Variational Bayes | Generation |
| **Logistic Regression** | Linear decision boundary; conditional $p(Y \mid X)$ |  | Maximize conditional log-likelihood | Gradient Descent, Newton-Raphson | Prediction |
| **Conditional Random Field (CRF)** | Undirected graphical model over sequences |  | Maximize conditional log-likelihood | Gradient-based (L-BFGS), SGD | Prediction, Forecasting |
| **Bayesian Linear Regression** | Linear model with prior over weights |  | Maximize posterior $p(w \mid D)$ | Closed-form or MCMC | Prediction, Forecasting, Generation |
| **Variational Autoencoder (VAE)** | Neural encoder-decoder with latent space |  | Maximize ELBO (variational lower bound) | Stochastic Gradient Descent + Reparameterization | Generation |
| **Normalizing Flow** | Invertible transformation of a simple distribution |  | Maximize likelihood via change-of-variables | Gradient Descent | Generation |
| **Dirichlet Process Mixture** | Infinite mixture model (nonparametric) |  | Maximize posterior | Gibbs Sampling, Stick-Breaking, Variational Inference | Generation |
| **Kalman Filter** | Linear-Gaussian dynamical system |  | Minimize expected squared error (MAP) | Recursive updates | Prediction, Forecasting, Backcasting, Generation |
| **Gaussian Process (GP)** | Covariance function (kernel) over functions |  | Maximize marginal likelihood | Matrix inversion, gradient descent | Prediction, Forecasting, Backcasting, Generation |
| **Latent Dirichlet Allocation (LDA)** | Hierarchical mixture of multinomials for topic modeling |  | Maximize marginal likelihood or posterior | Variational Inference, Gibbs Sampling | Discovery, Prediction |
| **Hierarchical Bayesian Models** | Multi-level probabilistic models with nested priors |  | Maximize posterior $p(\theta \mid D)$ | MCMC, Variational Inference | Prediction, Forecasting, Generation |
| **Particle Filter** | Sequential Monte Carlo for nonlinear/non-Gaussian state estimation |  | Minimize expected error, approximate posterior $p(x_t \mid y_{1:t})$ | Resampling + Importance Sampling | Prediction, Forecasting, Backcasting |
| **Switching Linear Dynamical System** | Mixture of linear dynamical systems with discrete switching states |  | Maximize joint likelihood $p(X, Z)$ | EM, Particle Filtering | Prediction, Forecasting |
| **Indian Buffet Process (IBP)** | Nonparametric latent feature allocation model |  | Maximize posterior | Gibbs Sampling, Variational Inference | Feature discovery, Generation |

### Modelling Pitfalls

| **Pitfall** | **Description** |
| --- | --- |
| Overfitting | Model fits noise or peculiarities in limited data, reducing generalization. |
| Ignoring or violating assumptions | Leads to misleading conclusions or invalid inferences. |
| Confusing correlation with causation | Interpreting probabilistic associations as causal relationships. |
| Underestimating uncertainty | Using overly simple models that fail to capture true variability and risk. |
| Arbitrary decision thresholds | Using fixed probability cutoffs without domain-specific justification, causing suboptimal decisions. |
| Assuming a stationary data distribution  | Ignoring the evolving dynamics of the data distribution that govern the system’s behavior. |
| Validation on non-representative data | Testing model performance on data not representative of real-world conditions leads to overoptimistic results. |
| Model misspecification | Choosing an incorrect model family or structure that poorly represents the underlying system. |
| Insufficient data quantity or quality | Small or biased samples reduce the reliability of estimation and increase variance. |
| Failure to test model robustness | Not evaluating model sensitivity to assumptions, parameters, or data perturbations. |
| Failure to account for fat-tailed distributions | Neglecting heavy tails leads to underestimating the probability and impact of extreme events, resulting in poor risk assessment and model failure. |
| Ignoring Hidden Context  - Dependencies | Failing to model joint or conditional distributions when variables are interdependent, leading to incomplete or misleading probabilistic representations. |

## Representation

> See more in  ([Representation Target](probability.md)) for an introduction.
> 

### **Outcome Modelling**

> How do we validate that our probability estimate $P(\text{something})$ is reliable? What’s the deep meaning of $P(\text{something})$?  How to specify and verify a context that  will determine a **well behaved trial**?
> 

> **Note 🚨:** This is a general overview, but each probability school differs slightly in its approach.
> 

> Single-event probabilities are the foundation of probability theory, joint probabilities describe how events occur together, and conditional probabilities allow us to **update probabilities** based on new information: the **probability of a single event** is the likelihood that a specific outcome occurs; **joint probability** measures the chance of two or more events occurring simultaneously; and **conditional probability** gives the likelihood of an event **given that another event has already occurred**.
> 

> Assigning a probability to an outcome is subtle and challenging. A common, often implicit, assumption is that we are dealing with a  trial under fixed conditions, $P(\text{Outcome})$, but in reality trials vary in ways that affect outcomes. When contextual factors matter, probabilities must be modeled conditionally, as $P(\text{Outcome} \mid \text{Context})$ - to satisfy the well behave assumption.
> 

> **Note:** Get the context right, or the entire modeling framework will collapse—like a sandcastle. 😎
> 

### Model Specification

> See models here [**Representation Toolbox**](probability.md).
> 

> ⚠️ Any specification implies assumptions—see [Model Assumption](probability.md).
> 

### Model Assumption

> Every **probabilistic model** relies on a set of assumptions that define the structure and behavior of the system under study. These assumptions guide the choice of model, estimation methods, and interpretation of results. Understanding and explicitly stating these assumptions is critical for model validity and applicability.
> 

> See more in [Independent and identically distributed random variables (***i.i.d***)](https://app.notion.com/p/Independent-and-identically-distributed-random-variables-i-i-d-250c0f5171ec80509fdaea01a358ed42?pvs=21) && …
> 

| **Assumption** | **Description** | **Importance** |
| --- | --- | --- |
| **Independence** | Observations or events are assumed to be statistically independent, meaning the occurrence of one does not influence another. | Violation can lead to biased estimates and incorrect inferences. Critical for many statistical methods including hypothesis testing and regression models. |
| **Identically Distributed** | Data points are assumed to come from the same probability distribution. This homogeneity simplifies analysis. | May not hold in evolving or heterogeneous systems. Violation can invalidate standard statistical procedures that assume consistent data generation processes. |
| **Stationarity** | The statistical properties of the process (mean, variance, autocorrelation) do not change over time or space. | Crucial for many time series and spatial models. Non-stationary data requires specialized techniques like differencing or detrending. |
| **Linearity** | Relationships between variables are assumed linear for simplicity and tractability. | Nonlinear dynamics may require more complex models. Assumption underlies many fundamental statistical techniques like linear regression. |
| **Distributional Form** | The underlying data or noise is assumed to follow a specific probability distribution (e.g., normal, Poisson). | Incorrect distributional assumptions can degrade model performance. Affects parameter estimation, confidence intervals, and hypothesis testing. |
| **Parametric Form** | Models assume a known functional form with a finite set of parameters. | Nonparametric models relax this but require more data. Parametric assumptions enable efficient estimation but risk model misspecification. |
| **Causal Structure** | When interpreting models causally, assumptions about the direction and nature of causal effects must be made and justified. | Essential for causal inference but often untestable without experimental design. Incorrect assumptions lead to erroneous causal claims. |

### Model Estimation

> **Probability model** estimation involves constructing a mathematical representation of a system’s uncertain behavior by identifying the probability distributions governing its states or outputs based on observed data.
> 

> **Note:** Estimation is as much an art as a science; it always involves some degree of error. If the underlying system exhibits fat-tailed distributions, estimation becomes particularly challenging due to the increased likelihood of extreme events and greater variability.
> 

> See more in [(Statistic) Estimator](statistic-estimator.md).
> 

The process typically follows these steps:

1. **Model Specification:** Define a probabilistic model structure that represents the system, including the choice of distribution families (e.g., Gaussian, Bernoulli, Poisson) and parameters.
2. **Data Collection:** Gather observed data that reflect realizations or measurements of the system’s states or outputs.
3. **Parameter Estimation:**
    
    Use statistical methods to infer the parameters of the model. Common approaches include:
    
    - **Maximum Likelihood Estimation (MLE):** Finds parameters maximizing the probability of observed data.
    - **Bayesian Estimation:** Incorporates prior knowledge with observed data to produce a posterior distribution over parameters.
    - **Method of Moments:** Matches theoretical moments of the model with empirical moments from data.
    - **Laplace Rule of Succession**:  …
4. **Model Validation:** Evaluate the estimated model’s goodness-of-fit using techniques such as likelihood tests, cross-validation, or information criteria (AIC, BIC).
5. **Inference and Prediction:** Once estimated, the model enables probabilistic inference about unobserved variables and prediction of future outcomes.

### Model Validation

> See more in  & [Model Validation](note.html?n=epistemica/validation/validation.md) and [Probability Model Validation](probability-model-validation.md).
> 

> See more in [Why do almost all types of real probability specifications need to be joint or conditional?](probability.md)
> 

> How  do we validate our probabilistic model? How to test, if a sequence if really random?
> 

| **Category** | **Method** | **Description** | **Use Case** |
| --- | --- | --- | --- |
| Bayesian Model Checking | **Posterior Predictive Checks** | Compare data simulated from the model’s posterior predictive distribution to observed data. | Assess model fit and detect lack of fit in Bayesian models. |
| Model Validation | **Cross-Validation (e.g., K-Fold)** | Partition data to train and test sets to evaluate predictive accuracy. | General model validation in both Bayesian and frequentist contexts. |
| Model Comparison | **Likelihood-Based Tests (e.g., Likelihood Ratio)** | Compare likelihoods of nested models to assess improvement. | Model comparison and selection. |
| Model Comparison | **Information Criteria (AIC, BIC, DIC, WAIC)** | Penalized measures combining goodness-of-fit and model complexity. | Model comparison and selection. |
| Calibration & Forecast Eval | **Calibration Tests** | Evaluate whether predicted probabilities correspond to observed frequencies. | Validating probabilistic forecasts. |
| Diagnostic Analysis | **Residual Analysis** | Analyze residuals (differences between observed and predicted) for patterns. | Detect model misspecification. |

### Model Limitation

> What are the practical limitations or constraints of Probabilistic Model $L_m$ in real-world applications?
> 

> **LIMITS:** ⚠️ Assumes well-defined sample spaces and measurable events. 😰 Struggles with modeling deep uncertainty, rare events with limited data, and subjective aspects of prior selection in Bayesian methods. ❌ Cannot eliminate uncertainty—only describe it.
> 

| **Limitation** | **Description** |
| --- | --- |
| Dependence on model assumptions | Incorrect assumptions (e.g., independence) can lead to biased or invalid results. |
| Data requirements | Requires sufficient, high-quality data for reliable estimation and prediction. |
| Computational complexity | Complex models with many variables can be computationally expensive and slow to run. |
| Sensitivity to **outliers** and mis-specification | Outliers or wrong model choices can skew results significantly. |
| Interpretation challenges | Probabilistic outputs can be hard to interpret or communicate to non-experts. |
| **Dynamic environments** | Models trained on static data may fail in non-stationary settings (e.g., shifting user behavior). |

## Sampling

> In probability and statistics, **sampling** refers to the process of selecting a subset of elements from a larger **population** or **universe** in order to make inferences about the whole population. The main idea is that it is usually impractical or impossible to observe every member of a population, so we observe a sample and use it to estimate population properties.
> 

> This is a key procedure in **estimation** and **data selection**. We usually cannot operate on the entire dataset, because the data is generated according to an underlying probabilistic process (at least we assume this), which may itself change over time in **non-stationary** settings.
> 

> See more in [Sampling](sampling.md).
> 

## Simulation

> In the context of **probability theory**, a **simulation** is a method of **approximating the behavior of a random system or stochastic process** by using **computational or experimental procedures to generate samples from the underlying probability distributions**.
> 

Formally, it involves:

1. **Modeling** a probabilistic system mathematically (e.g., defining random variables, distributions, and dependencies).
2. **Generating random samples** according to the specified distributions (often using pseudo-random number generators).
3. **Estimating probabilities, expectations, or other quantities of interest** from the simulated data.

## Problem Solving

> Which are the set of techniques for solving **probability-based problems**?
> 

| **Technique** | **Description** | **Use** |
| --- | --- | --- |
| **Mapping Between Probability Space** | Transforming a complex probability problem into another probability space where calculations are simpler. | Useful when direct computation is difficult but an equivalent scenario is easier to analyze. |
| **Indicator Random Variable** | Define 0–1 random variables to represent events, allowing sums of indicators to count occurrences. | Useful for counting problems, expected value calculations, and simplifying complex events. |
| **Generating Function** | Encode sequences or probabilities into a function; use algebraic operations to extract probabilities or moments. | Useful for combinatorial problems, branching processes, and recurrence relations. |
| **Recursion** | Express probabilities in terms of smaller or previous instances of the problem. | Useful for sequential processes, Markov chains, or problems with a natural iterative structure. |
| **Monte Carlo Method** | Simulate random trials and use the outcomes to estimate probabilities. | Useful when analytical solutions are difficult or in high-dimensional problems. |
| **Expectation & Variance Method** | Use linearity of expectation and properties of variance to calculate probabilities indirectly. | Useful for problems where direct probability computation is hard but moments are tractable. |
| **Rejection Sampling** | Generate samples from a target distribution by sampling from a proposal distribution and rejecting some samples. | Useful for sampling from complex distributions when direct sampling is not feasible. |
| **Sequential / Multi-step Mapping** | Break down events into sequences of dependent stages and compute probabilities step by step. | Useful for multi-stage experiments or Markov processes. |
| **Probabilistic Weighting / Rescaling** | Adjust probabilities of events to simplify calculations or to account for conditioning. | Useful when dealing with weighted events or conditional probabilities. |

## Foundation

> Probability does not exist as a physical property. Probability is a measure of a person’s degree of belief about uncertain events, constrained only by the logical consistency of their beliefs.  - **de Finetti.**
> 

### Tool

> aka. Meta - Theory Tools.
> 

> Core mathematical instruments used to **develop the fundamental tools that provide support for the  probability theory.**
> 

> What is the limiting distribution of a sequence of random variables? How fast does convergence occur (rate of convergence)? How likely are large deviations from expected behavior in the limit?
> 

> See more in [Theory of Probability](theory-of-probability.md).
> 

### Interpretation

> What are the sources of probability?
> 

> Probability theory is a branch of mathematics that deals with quantifying uncertainty and randomness. There are various alternative models and interpretations within probability theory.
> 

> The **framework of probability** addresses chance, uncertainty, probably, indeterminism, likelihood, and contingency, as well as our lack of knowledge about them and possible ways to remedy it.
> 

| **Interpretation** | **Definition** | **Verification Model** | **Limitations** |
| --- | --- | --- | --- |
| **Frequentist Probability** | Probability is the long-run relative frequency of an event after many trials. | Compare observed frequencies over repeated experiments to predicted probabilities. | Doesn’t handle single events well; prior beliefs not incorporated |
| **Bayesian Probability (Epistemic)** | Probability is a degree of belief, updated by evidence via Bayes’ theorem. | **Calibration:** check predictive accuracy over multiple instances; consistency with Bayes’ updates. | Depends on choice of prior; can be subjective |
| **Subjective Probability** | Probability expresses personal belief about uncertainty, not necessarily empirical. | **Coherence checks:** e.g., Dutch book arguments to ensure internal consistency of beliefs. | Can lack reproducibility; may vary widely between individuals |
| **Logical Probability (Optional)** | Probability is a measure of plausibility based on available information. | Verify consistency with axioms of probability and logical reasoning. | Difficult to quantify; can be abstract and context-dependent |

### Formalization

> In probability, a **σ-algebra** represents the collection of events to which probabilities can be assigned.
> 

> See [Free Probability Theory](free-probability-theory.md), [Imprecise Probability](imprecise-probability.md), [**Formulation**](probability.md).
> 

| **Formalization** | **Core Idea** | **Mathematical Framework** |
| --- | --- | --- |
| **Kolmogorov Probability** | Probability is a measure over a sigma-algebra of events. | Measure theory; $(\Omega, \mathcal{F}, P)$ |
| **Quantum Probability** | Probabilities arise from state vectors and operators in Hilbert spaces. | Hilbert space; non-commutative algebra |
| **Fuzzy Probability** | Probability is modeled with degrees of truth/membership. | Fuzzy set theory; possibility distributions |
| **Imprecise Probability** | Probability is represented as an interval or set of distributions. | Upper/lower probability functions; credal sets |
| **Dempster-Shafer Theory** | Belief functions allow explicit modeling of ignorance and partial knowledge. | Evidence theory; belief and plausibility functions |
| Algorithmic Probability | Probability is the a priori likelihood of a sequence based on all possible generative programs, weighted by program length. | Algorithmic information theory; Solomonoff induction |
| Free Probability | Probability theory for **non-commuting random variables** arising in large random matrix limits. | Non-commutative probability spaces; free independence |

### Open Theoretical  Problem

| **Problem** | **Description** |
| --- | --- |
| **Interpretations of Probability** | What does probability mean? Is it subjective, objective, or a property of events? |
| **The Problem of Induction** | How can probabilistic reasoning justify inductive inferences (e.g., predicting the future based on past data)? |
| **The Reference Class Problem** | How to assign probabilities when an event belongs to multiple reference classes (e.g., "What is the probability this patient will survive?"). |
| **Probability in Science** | How should probability be used in scientific explanations (e.g., quantum mechanics, statistical mechanics)? |
| **Objective vs. Subjective Probability** | Is probability a feature of the world (e.g., quantum chances) or a measure of belief (e.g., Bayesian degrees of confidence)? |
| **The Principle of Indifference** | How to assign equal probabilities in the absence of information (e.g., in classical probability)? |
| **Probability and Causation** | Can probabilistic relationships (e.g., correlation) imply causation? How are they linked? |
| **Decision Theory** | How should agents act under uncertainty? What role does probability play in rational choice? |
| **Probability in Mathematics** | How are mathematical probabilities (e.g., measure theory) connected to real-world applications? |
| **Chance and Determinism** | Can genuine chance exist in a deterministic universe (or vice versa)? |

## Application

> See more in [What types of questions does probability help answer?](probability.md).
> 

| **Application** | **Description** |
| --- | --- |
| **Language Models** | Probability is central to modeling the structure and generation of language, enabling tasks like text generation, speech recognition, and machine translation. |
| **Weather Forecasting** | Probabilistic models predict weather conditions and provide probabilistic forecasts of temperature, precipitation, and other meteorological variables. |
| **Financial Markets** | Probability is used to model stock price movements and assess risk and price options in finance. |
| **Epidemiology** | Probability models help track disease outbreaks, estimate disease spread, and assess the effectiveness of interventions in epidemiological studies. |
| **Queueing Systems** | Probability models waiting times and service processes in call centers and traffic management systems. |
| **Game Theory** | Probability is crucial in modeling strategic interactions and decision-making in economics and political science. |
| **Genetics** | Probability is used to model genetic inheritance, mutation, and the likelihood of genetic disorders in population genetics. |
| **Risk Assessment** | Probabilistic models assess and manage risks in various fields, including insurance, engineering, and public safety. |
| **Quality Control** | Probability is used to model defects and control quality in manufacturing processes. |
| **Machine Learning** | Probabilistic models like Bayesian networks are used in various machine learning tasks, including classification, regression, and recommendation systems. |
| **Robotics** | Probability models help robots understand and navigate their environment by estimating the uncertainty in sensor measurements and control actions. |
| **Environmental Modeling** | Probability models and predicts environmental phenomena like climate change and ecological dynamics. |
| **Communication Systems** | Probability is employed in modeling data transmission and error correction in wireless networks and the Internet. |
| **Psychology and Behavioral Sciences** | Probability models are used to understand human behavior and cognitive processes in psychology and social sciences. |
| **Supply Chain Management** | Probability models help optimize inventory management, demand forecasting, and supply chain logistics. |
| **Healthcare** | Probability models disease progression, patient outcomes, and medical decision-making in healthcare analytics. |
| **Cryptography** | Probability plays a role in securing cryptographic protocols and encryption algorithms. |
| **Natural Language Processing** | Besides language models, probability is used for tasks like sentiment analysis, document classification, and information retrieval. |
| **Energy Systems** | Probability models are applied in energy demand forecasting, grid management, and renewable energy resource modeling. |
| **Transportation Systems** | Probability helps model traffic flow, public transportation scheduling, and logistics in transportation systems. |

## Case Study

> Note: That the probability toolbox; can be apply even to non-stochastic systems.
> 

> See more in https://github.com/dbremont/algorithms & https://github.com/csiglab/responsum.
> 

| **Case Study** | **Problem** | **Description** | **Type of Stochasticity Modeled** |
| --- | --- | --- | --- |
| **Manufacturing – Defective Products** | A factory produces 10,000 bolts a day. 2% are defective. If a random sample of 5 bolts is tested, what’s the probability all pass inspection? | Helps estimate the likelihood of releasing a fully good batch and guides quality control sampling size. | Aleatory uncertainty (inherent randomness in defects) |
| **Retail – Stockout Risk** | A store sells an average of 50 units/day of a product, with demand following a Poisson distribution (λ = 50). What’s the probability of demand exceeding 60 units in a day? | Used to set safety stock levels and reduce lost sales due to stockouts. | Aleatory uncertainty (random demand fluctuations) |
| **Telecom – Network Failure** | A network consists of 5 routers in series, each with a 99% uptime probability. What’s the probability the network stays operational? | Guides redundancy planning to ensure service level agreements (SLAs). | Aleatory uncertainty (random failures) |
| **Finance – Credit Default** | A bank estimates a 3% default probability on loans. For a portfolio of 100 loans, what’s the probability of 5 or more defaults? | Helps assess credit risk and determine capital reserves under Basel III. | Epistemic uncertainty (modeling default risk based on limited info) & Aleatory uncertainty (inherent credit risk) |
| **Aviation – Component Failure** | An aircraft engine component fails with probability 0.001 per flight. For a fleet making 1,000 flights, what’s the probability of at least one failure? | Supports maintenance scheduling and component replacement planning. | Aleatory uncertainty (inherent failure probability) |
| **Car Repair – Probabilistic Description** | Given the probability of certain car problems occurring, describe how likely each is and estimate expected repair frequency. | Assists in diagnostics, preventive maintenance scheduling, and customer cost estimation. | Epistemic uncertainty (incomplete observability & knowledge about failures) |
| **Coin Flip** | A fair coin is flipped 10 times. What’s the probability of getting exactly 6 heads? | Classic example of discrete probability, used for teaching binomial models and basic combinatorics. | Aleatory uncertainty (inherent randomness in outcomes) |
| **Arrival Time Between Two Customers** | Customers arrive at a store following a Poisson process with rate 10/hour. What’s the probability the time between two arrivals exceeds 15 minutes? | Used in queuing theory to optimize staffing and reduce wait times. | Aleatory uncertainty (random arrival process) |
| **Linear Regression** | Given past housing data, estimate the relationship between size, location, and price, and predict the price of a new house. | Treats observed prices as random variables with a mean given by a linear function of predictors plus noise, allowing both estimation and uncertainty quantification. | Epistemic uncertainty (unknown parameters) & Aleatory uncertainty (residual noise) |

## QA

> Why is **probability** is counterintuitive?
> 

### How can we infer the probability model of a new stochastic system from an existing one?

> For example, suppose we have a system involving a single die, and we have a probability model for it. How can we infer the probability model for a new system where we have two dice instead?
> 

> This form of problems appears a lot; it’s basically about deriving a new probability model for the new situation.
> 

### What are the sources of randomness? Can random **systems emerge** from non-random systems?

> Is **Randomness** even real? Which **statistical tests** can be used to determine if a **sequence is random**?
> 

> Can random **systems emerge** from non-random systems? It seems yes.
> 

| **Source of Randomness** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Intrinsic (Aleatory) Randomness** | Inherent variability or unpredictability in a process or system. | Radioactive decay, dice roll, coin toss |
| **Epistemic (Knowledge-based) Uncertainty** | Uncertainty due to incomplete knowledge or information about the system or environment. | Weather forecasting, customer behavior modeling |
| **Measurement Noise** | Random errors or noise introduced by sensors or instruments during data collection. | Sensor inaccuracies, signal interference |
| **Environmental Variability** | Random fluctuations in external conditions affecting a system. | Temperature changes, market fluctuations |
| **Chaotic Dynamics** | Deterministic systems exhibiting sensitive dependence on initial conditions that appear random. | Weather systems, turbulent fluid flow |
| **Emergent Complexity** | Unpredictable behavior arising from interactions of many components in a complex system. | Traffic patterns, crowd behavior |
| **Quantum Indeterminacy** | Fundamental randomness at the quantum level according to quantum mechanics. | Photon polarization, electron spin measurement |

### Why do we have very similar concepts such as probability distributions, laws, and random variables? What value does the idea of a random variable offers?

![image.png](../assets/note/epistemica/observational/probability/image-2.png)

> This is simpler than I imagined: the probability distribution is **basically the characterization of the stochastic system (row state  → probability)**, assigning a probability to each event  and the  **random variable (**and more generally random objects), is just a **numerical representation** of the same space.
> 

> So the **random object** is an **effective abstraction of the sample space**. In a very abstract sense, we can treat it as a 'potential probabilistic value'—we can apply functions to it, compute expectations, and reason systematically about uncertainty. In essence, random variables bridge the gap between raw probability spaces and the quantities we actually care about in modeling, analysis, and inference.
> 

> **Random variable:** an abstract object representing the probabilistic outcome modeled by a probability distribution.
> 

> Why this? A numerical representation allows mathematical operations to be performed on it, such as computing summaries, aggregations, or other transformations.
> 

### What types of questions does probability help answer?

| **Category** | **General Question** | **Description** |
| --- | --- | --- |
| **Event likelihood** | What is the chance of one success/failure? / What is the probability that event *A* happens? | Binary outcomes; basic probability assignment — quantifies the chance of a specific outcome. |
| **Joint behavior** | What is the probability that events *A* and *B* happen together? | Captures co-occurrence, interactions, or dependencies between events. |
| **Conditional behavior** | Given that *B* happened, what is the probability of *A*? | Allows reasoning about **causal-like constraints** or inference in uncertain environments. |
| **Repeated trials** | How many successes in *n* trials? | Multiple independent Bernoulli trials (Binomial models). |
| **Waiting time until first success** | How many trials until the first success? | Models trial count for first event (Geometric distribution). |
| **Number of events in fixed time/space** | How many events occur in an interval? | Random arrivals/events (Poisson distribution). |
| **Time between events** | How long until the next event? | Continuous-time waiting (Exponential distribution). |
| **Distributional form** | What is the probability distribution of variable *X*? | Complete description of how uncertainty spreads across possible values. |
| **Expectation / average case** | What is the expected value of *X*? | Quantifies the “long-run average” outcome across repetitions. |
| **Dispersion / uncertainty spread** | How variable is *X*? | Variance/standard deviation measure stability vs volatility of the system. |
| **Spread across categories** | What is the distribution of outcomes across multiple categories? | Multinomial / categorical settings (more than 2 outcomes). |
| **Extreme values / tail risks** | What’s the probability of unusually large/small values? | Heavy-tail distributions, rare but impactful events (risk, reliability). |
| **Comparisons** | Is system *A* more likely to produce outcome *x* than system *B*? | Supports decision-making under uncertainty, distribution comparisons. |
| **Updates & learning** | How should probabilities change after observing new evidence? | Bayesian updating, posterior inference, adaptive learning. |
| **Processes over time** | How does the probability of events evolve over time? | Time-series probability, stochastic processes (Markov chains, Poisson processes). |
| **Decision-oriented** | What action maximizes expected utility under uncertainty? | Links probability to rational choice and optimization. |

### Suppose we have a function f(x). How should we interpret a probabilistic model of P(f(x)∣x)?

> It can be interpreted as a measure over all possible outcomes of $f(x)$ given $x$, treating $f(x)$ as a random variable rather than a deterministic mapping. In other words, the model assigns **weights (probabilities)** to each potential output, reflecting uncertainty in the function’s outcome or in our knowledge of it.
> 

> How to we convert back P(f(x) |x) to x → f(x)? For every x output the f(x) with higher probability, assign. Basically **Maximum A Posteriori (MAP) Estimate.**
> 

> **Note:** Different probability frameworks—Bayesian and frequentist—support different kinds of problems, or the same question in slightly different ways.
> 

### How can we model a deterministic function $(x, f(x))$  using probability? H*ow can we represent a system that is fully determined as if it were stochastic?*

> See more here [Representation Toolbox](statistics.md).
> 

| **Technique** | **Probabilistic Form** | **Description** |
| --- | --- | --- |
| **Dirac Delta** | $P(y \mid x) = \delta(y - f(x)$ | Represents the deterministic function exactly as a "spike" in probability: all mass is concentrated at $y = f(x)$. |
| **Noise-Augmented** | $y = f(x) + \epsilon$, where $\epsilon \sim p(\epsilon)$ | Introduces small stochasticity (e.g., Gaussian noise) to model uncertainty around $f(x)$, useful in probabilistic modeling. |
| **Categorical** | $P(y \mid x) = \text{Categorical}(y; \mathbf{p})$ where $\mathbf{p}$ is a one-hot vector at $f(x)$. | For discrete outputs, this treats $f(x)$ as a deterministic category while fitting it in a probabilistic framework. |
| **Softmax/Boltzmann** | $P(y \mid x) = \frac{\exp(f(x)/\tau)}{\sum_{y'}\exp(f(x')/\tau)}$ | Converts deterministic scores into a smoothed probability distribution over possible outputs; $\tau \to 0$recovers determinism. |
| **Gaussian Process** | $f \sim \mathcal{GP}(m(x), k(x, x'))$ conditioned on data ${(x_i, f(x_i))
}$. | Treats $f(x)$ as a realization of a stochastic process; even if underlying function is deterministic, GPs allow uncertainty quantification. |
| **Probabilistic Programming** | `y = delta(f(x))` or `y ~ Normal(f(x), small_sigma)` | Enables modeling deterministic computations in probabilistic languages by using exact or near-exact distributions. |
| **Monte Carlo** | $P(y \mid x) \approx \frac{1}{N} \sum_{i=1}^N \delta(y - f(x))$ | Uses repeated sampling (e.g., bootstrapping) to approximate the deterministic outcome as a probability measure. |
| **Ensemble Approximation** | $P(y \mid x) \approx \frac{1}{M} \sum_{m=1}^M \delta(y - f_{\theta_m}(x))$ | Represents a deterministic function through an ensemble of models to capture epistemic uncertainty or model variability. |
| Energy Based Model | $P(y \mid x) \propto \exp(-E(y, x))$ | Represents a deterministic function $f(x)$ as the **minimum of an energy function** $E(y, x)$. By designing $E(y, x)$ so that its minimum corresponds to $f(x)$, EBMs convert deterministic outputs into a probabilistic framework, allowing uncertainty modeling, sampling, and integration with probabilistic inference methods. |

### Why do so many probabilistic modeling methods in statistics and machine learning focus on learning the joint probability distribution of a system rather than just individual variables or conditional probabilities?

> See more in [Distribution](distribution/distribution-2.md).
> 
- **Encodes all marginal and conditional distributions:** The joint distribution is like a master map of all the variables. From it, you can figure out the behavior of any single variable (marginals) or how one variable behaves given others (conditionals). Learning the joint gives you access to everything.
- **Captures dependencies between variables:** Variables in a system often influence each other. By modeling the joint distribution, you naturally capture these relationships, correlations, and interactions, which you would miss if you only looked at variables individually.
- **Supports flexible inference:** Once you know the joint, you can answer many different questions: predict one variable from others, compute probabilities, or calculate expected outcomes. Focusing only on marginals or conditionals limits what you can infer.
- **Foundation for generative modeling:** If you want to generate new data that looks realistic, you need to know how all variables combine. The joint distribution tells you how to generate coherent samples, while individual marginals wouldn’t produce consistent data.
- **Mathematical and computational advantages:** While the joint can be huge, it can often be broken down into simpler parts using clever factorizations (like in Bayesian networks). This makes it both practical and powerful: you can model complex systems without losing the ability to answer any probabilistic question.

### What is the role of a Probability Model Type in the probability toolbox?

> A **Probability Model Type** is the **formal template** that defines how uncertainty is represented, inferred, and used. It sits at the core of the probabilistic toolbox because it dictates **representation, inference, optimization, and operational capabilities**, enabling modularity, composability, and systematic reasoning under uncertainty.
> 

### Why do almost all types of real probability specifications need to be joint or conditional?

> See more in  [**Outcome Modelling**](probability.md).
> 

> Assigning a probability to an outcome is subtle and challenging. A common, often implicit, assumption is that we are dealing with a  trial under fixed conditions, $P(\text{Outcome})$, but in reality trials vary in ways that affect outcomes. When contextual factors matter, probabilities must be modeled conditionally, as $P(\text{Outcome} \mid \text{Context})$ - to satisfy the well behave assumption.
> 

> This leads to several important questions: How do we validate a probability representation? What happens when we ignore context? How can a representation fail? How can we detect such failures?
> 

### What is the insight relating probability and how people miss explain the world?

> What is the name of this cognitive pathology? **Overfitting of explanations, illusion of causality,  Universality  of Explanation Error, Explanatory Drive.**
> 

> Let’s say we have an observation — for example, we saw a cat hiding under the car three times today. People tend to explain observations by trying to causally connect every event. However, in reality, not every observation requires a causal explanation. Most observations have a non-zero probability of occurring, so events can appear **without any underlying causal mechanism**.
> 

> Other similar tendencies include **over-rationalization** — trying to explain human behavior solely in rational terms.
> 

> See more in [Explanation](https://app.notion.com/p/Explanation-11dc0f5171ec80b8b8bcf08793bc64a8?pvs=21).
> 

## References

- [σ-algebra](../mathematical/algebra-2.md)
- http://bactra.org/notebooks/probability.html
- [‣](https://app.notion.com/p/10e598edb790816293a7c8ae6bd662ff?pvs=21)
- [‣](https://app.notion.com/p/10e598edb790813e9bc3e6df60b3011e?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081a7b49bd1cdf69ee63d?pvs=21)
- https://en.wikipedia.org/wiki/History_of_randomness
- https://plato.stanford.edu/entries/probability-interpret/?ref=jcreinhold.com
- https://en.m.wikipedia.org/wiki/Principle_of_maximum_entropy
- https://stats.stackexchange.com/questions/243746/what-is-probabilistic-inference
- [On Chomsky and the Two Cultures of Statistical Learning](https://norvig.com/chomsky.html)
    - https://news.ycombinator.com/item?id=2591154
    - https://news.ycombinator.com/item?id=11951444
- [Kullback–Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
- [Probability and Measure](https://www.colorado.edu/amath/sites/default/files/attached-files/billingsley.pdf)
- [The Probabilistic Method](http://math.bme.hu/~gabor/oktatas/SztoM/AlonSpencer.ProbMethod3ed.pdf)
- [Chain rule (probability)](https://www.wikiwand.com/en/Chain_rule_(probability))
- [The Unreasonable Effectiveness of Conditional Probabilities](https://two-wrongs.com/unreasonable-effectiveness-of-conditional-probabilities.html)
- [A Brief Introduction to Graphical Models and Bayesian Networks](https://www.cs.ubc.ca/~murphyk/Bayes/bayes.html)
- [Probabilistic Algorithms: Approximate Counting, *LogLog and Bloom Filters](https://github.com/lucasschmidtc/Probabilistic-Algorithms/blob/master/Probabilistic%20Algorithms.ipynb)
- Mitzenmacher, M. (2003). A brief history of generative models for power law and lognormal distributions. Internet Mathematics, 1 (2), 226–251
- Farmer, J. D., & Geanakoplos, J. (2008). Power laws in economics and elsewhere. Working Paper, Santa Fe Institute. Available online: http://tuvalu.santafe.edu/ jdf/papers/powerlaw3.pdf.
- Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). Power-Law Distributions in Empirical Data. SIAM Review, 51 (4), 661–703.
- https://en.wikipedia.org/wiki/Sunrise_problem
- https://en.wikipedia.org/wiki/Rule_of_succession
- https://en.wikipedia.org/wiki/Characterization_(mathematics)
- [‣](https://app.notion.com/p/193598edb7908092a59dcee5509d4764?pvs=21)
- [‣](https://app.notion.com/p/a41164f993de416e805fe3e991c8f056?pvs=21)
- https://www.nature.com/articles/d41586-024-04096-5#ref-CR1
- https://en.wikipedia.org/wiki/Random_variable
- https://en.wikipedia.org/wiki/Chebyshev's_inequality
- [The Problem of Induction](https://app.notion.com/p/The-Problem-of-Induction-1fdc0f5171ec8031a27ef5c52d2c549e?pvs=21)
- https://plato.stanford.edu/entries/logic-probability
- https://plato.stanford.edu/entries/causation-probabilistic/#Prob
- https://plato.stanford.edu/entries/chance-randomness/
- https://plato.stanford.edu/entries/probability-medieval-renaissance/
- https://en.wikipedia.org/wiki/Applications_of_randomness
- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [](https://app.notion.com/p/245c0f5171ec80749daec722e73b8a81?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- [Distribution](distribution/distribution-2.md)
- [Enumeration (Counting)](../mathematical/enumeration-counting.md)
- Davidson-Pilon, Cameron. *Bayesian methods for hackers: probabilistic programming and Bayesian inference*. Addison-Wesley Professional, 2015.
- Bayes, Thomas. "An essay towards solving a problem in the doctrine of chances." *Biometrika* 45.3-4 (1958): 296-315.
- Talbott, William J. "Two principles of Bayesian epistemology." *Philosophical Studies: An International Journal for Philosophy in the Analytic Tradition* 62.2 (1991): 135-150.
- https://en.wikipedia.org/wiki/Bayesian_epistemology
- https://en.wikipedia.org/wiki/Bayes'_theorem
- https://plato.stanford.edu/entries/epistemology-bayesian/
- https://www.richardcarrier.info/archives/16374
- https://en.wikipedia.org/wiki/Bayesian_statistics
- https://en.wikipedia.org/wiki/Likelihood_function
- [**Statistical Mechanics**](note.html?n=epistemica/construction/statistical-mechanics.md)
- https://en.wikipedia.org/wiki/Likelihood_function
- [‣](https://app.notion.com/p/25e598edb7908013ba65d2eec601e725?pvs=21)
- [‣](https://app.notion.com/p/25e598edb790809691e4d60f88bcbd3b?pvs=21)
- https://en.wikipedia.org/wiki/Large_deviations_theory
- https://mathworld.wolfram.com/topics/Probability.html
- [Set](../mathematical/set.md)
- [Combinatorics](../mathematical/combinatorics.md)
- [Enumeration (Counting)](../mathematical/enumeration-counting.md)
- [Inclusion-Exclusion Principle](../mathematical/inclusion-exclusion-principle.md)
- [‣](https://app.notion.com/p/10e598edb790813e9bc3e6df60b3011e?pvs=21)
- https://brilliant.org/wiki/probability-rule-of-product/
- https://brilliant.org/wiki/rule-of-sum/
- https://en.wikipedia.org/wiki/Chain_rule_(probability)
- [A General Guide to Representation & Estimation](https://app.notion.com/p/A-General-Guide-to-Representation-Estimation-22dc0f5171ec8099a450f1d8f419a67f?pvs=21)
- [Measure](../mathematical/measure.md)
- [Enumeration (Counting)](../mathematical/enumeration-counting.md)
- https://en.wikipedia.org/wiki/Tree_diagram_(probability_theory)
- https://en.wikipedia.org/wiki/Venn_diagram
- https://www.youtube.com/playlist?list=PLY11JnnnTUCZSUk2xnombjwfg6z3-okP5
- https://www.youtube.com/playlist?list=PLoROMvodv4rOpr_A7B9SriE_iZmkanvUg
- https://www.youtube.com/playlist?list=PLMrJAkhIeNNR3sNYvfgiKgcStwuPSts9V
- https://www.youtube.com/@AProbabilitySpace
- https://www.youtube.com/watch?v=GEFxFVESQXc`
