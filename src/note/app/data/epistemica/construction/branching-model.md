# Branching Model


> A **branching model** is a mathematical abstraction for representing systems that evolve through successive bifurcations, splits, or decisions. It captures the probabilistic or deterministic evolution of entities or states that give rise to multiple pathways over time.
> 

> What mathematical frameworks can be used to model the bifurcation of a system?
> 

> How can we describe the system's evolution as it progresses through multiple branching paths?
> 

## **Formalization**

> 

## Specific Model

| **Branching Process** | **Type** | **Description** |
| --- | --- | --- |
| **Galton–Watson Process** | Discrete, single-type, stochastic | Classical process; entities reproduce probabilistically in discrete generations. |
| **Bienaymé–Galton–Watson Process** | Discrete, single-type, stochastic | Historical variant of Galton–Watson process; emphasizes early development of branching theory. |
| **Multitype Galton–Watson Process** | Discrete, multitype, stochastic | Entities of different types; offspring distribution depends on type. |
| **Age-dependent / Bellman–Harris** | Discrete/continuous, stochastic | Lifetimes vary; branching occurs after stochastic waiting times. |
| **Markov Branching Process** | Continuous-time, Markovian | Memoryless branching in continuous time; offspring appear according to Poisson process. |
| **Birth–Death Process** | Continuous-time, Markovian | At most one birth or death per small interval; widely used in population and queue modeling. |
| **Branching Random Walk** | Continuous/Discrete, stochastic | Combines branching with spatial movement of entities. |
| **Branching Brownian Motion** | Continuous-space/time, stochastic | Entities move according to Brownian motion and branch probabilistically. |
| **Crump–Mode–Jagers (CMJ) Process** | Generalized, multitype, age-dependent | Allows arbitrary lifetimes, age-dependent reproduction, general offspring distributions. |
| **Continuous-State Branching Process (CSBP)** | Continuous population, stochastic | Models populations with continuous quantities rather than discrete counts. |
| **Markov-modulated Branching Process** | Stochastic, environment-dependent | Branching rates depend on an external Markov process (variable environment). |
| **Phylogenetic / Coalescent Branching** | Application-specific, stochastic | Models evolutionary lineage splits or coalescences over time. |
| **Epidemic Branching Process** | Application-specific, stochastic | Models probabilistic spread of infections through populations. |
| **Network Cascading / Failure Models** | Application-specific, stochastic | Branching processes applied to propagation of failures or events in networks. |

## Related

- **Generating Functions** – Compactly encode distributions of offspring.
- **Transition Matrices** – Especially for Markov or multitype branching processes.
- **Monte Carlo Simulation** – For complex or high-dimensional branching paths.

## Use

> Which **representations or models** can be generalized by this?
> 

| **Model** | **Description** | **Branching Model Representation** |
| --- | --- | --- |
| **Branching Processes** | Stochastic model where entities reproduce or die in discrete generations. | Fundamental probabilistic branching of entities over time. |
| **Decision Trees** | Deterministic or probabilistic tree where nodes represent choices or conditions. | Represents all possible branching paths from a root decision. |
| **Markov Branching Processes** | Branching processes with memoryless (Markov) transitions; future depends only on current state. | Probabilistic branching with Markovian dependencies; generalizes stochastic dynamics. |
| **Multitype Branching Processes** | Entities of different types, each with its own branching rules. | Captures heterogeneous branching behaviors within a single model. |
| **Phylogenetic Tree Models** | Trees representing evolutionary lineage splits over time. | Branching model applied to lineage or history; temporal branching of types. |

## References

- [Binomial Coefficient](../mathematical/binomial-coefficient.md)
- https://en.wikipedia.org/wiki/Branching_process
- https://github.com/csiglab/responsum/blob/main/praxis/src/datamatica/probability.md
- [Galton–Watson Process](../observational/galtonwatson-process.md)
- https://archive.org/details/theoryofbranchin00harr/mode/1up?view=theater&ui=embed&wrapper=false
