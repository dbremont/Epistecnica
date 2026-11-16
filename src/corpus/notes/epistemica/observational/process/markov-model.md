---
tags: [note, probability, stochastic-process, markov]
---

# Markov Model

Related: [Markov Process](markov-process.md), [Stochastic Process](stochastic-process.md), [CTMC](ctmc-continuous-time-markov-chain.md), [HMM](../computational/hmm-hidden-markov-model.md), [MDP](../../adaptative/markov-decision-processes-mdp.md), [State Estimation](../../singular/state-estimation.md).

> A **Markov model** is a model of a stochastic process that assumes the [Markov property](markov-process.md#sec-the-property): the state carries everything about the past that bears on the future, so the transition law together with the initial law is the whole model.

> It is a *representation*, not the process it represents. The [Markov process](markov-process.md) is the object — a family of random variables on a probability space; the Markov model is the assumption plus the parameters that follow from it, chosen so that a trajectory can be described, predicted from, or controlled.

Its transition law is a [Markov kernel](https://en.wikipedia.org/wiki/Markov_kernel) — a stochastic kernel from a state to a probability law on the next state — and that object, plus the initial law, is what the model consists of.

**Boundary.** The term is used for both sides of that relation, and the two readings should be kept apart. "Markov model" is routinely said of the process itself — a Markov chain, a diffusion — and the corpus keeps a note for each: [Markov process](markov-process.md) for the object, this note for the model. The distinction has consequences. A process satisfies or fails the property; a model *assumes* it, and can therefore be wrong — which is what makes the assumption testable, and what makes a poor choice of state (a state that hides part of the memory) look like a failure of the model rather than of the state definition.

## The axis

The twelve named types below are one family specialised along four parameters. Stating the axis first makes the table readable as a grid rather than a list.

| Axis | Values | What it fixes |
| --- | --- | --- |
| **Time** | discrete / continuous | Whether transitions happen at steps or at any instant, and whether holding times matter |
| **State** | discrete / continuous | Whether the state is counted (a finite or countable set) or measured (a general state space) |
| **Observability** | full / partial | Whether the state is seen directly or inferred from emissions that depend on it |
| **Control** | absent / present | Whether the transition depends on a decision taken at the state |

DTMC is discrete × discrete × full × none; CTMC the same with continuous time; HMM adds partial observability; MDP adds control; POMDP adds both. The quasi-birth–death process is a CTMC with block-structured states; the Markov jump process is the continuous-time, discrete-state case where the generator is a rate matrix.

## Types of Markov Models

| **Type of Markov Model** | **Description** | **Key Applications** |
| --- | --- | --- |
| **Discrete-Time Markov Chain (DTMC)** | A Markov model where transitions between states occur at discrete time steps, with probabilities defined for each possible transition. | Queueing systems, population dynamics, board games, reliability modeling |
| **Continuous-Time Markov Chain (CTMC)** | A Markov model where transitions between states can occur at any continuous point in time, often modeled with exponential waiting times between transitions. | Chemical reactions, queuing theory, failure/repair processes |
| **Hidden Markov Model (HMM)** | A Markov model where the system states are not directly observable (hidden), but can be inferred through observed emissions that depend on the hidden states. | Speech recognition, bioinformatics, time series analysis, machine learning |
| **Markov Decision Process (MDP)** | A Markov model that incorporates decision-making, where transitions between states depend on both the current state and the action chosen by a decision-maker. | Robotics, reinforcement learning, operations research |
| **Partially Observable Markov Decision Process (POMDP)** | An extension of MDP where the system state is not fully observable, and decisions must be made based on partial information. | Autonomous systems, robotics, planning under uncertainty |
| **Absorbing Markov Chain** | A special type of DTMC where certain states, known as absorbing states, cannot be left once entered, and all other states eventually lead to an absorbing state. | Game theory, gambling processes, reliability engineering |
| **Ergodic Markov Chain** | A Markov chain where every state is recurrent and positive, meaning all states are reachable from every other state, leading to a steady-state distribution. | Long-term predictions, steady-state analysis, statistical mechanics |
| **Stationary Markov Process** | A Markov process where the transition probabilities remain constant over time, leading to a stationary distribution that doesn't change as the process evolves. | Equilibrium analysis, stochastic modeling in physics and economics |
| **Reversible Markov Chain** | A Markov chain where the transition process between any two states is the same in both directions, leading to detailed balance in steady-state. | Metropolis-Hastings algorithm, statistical mechanics, network flows |
| **Markov Jump Process** | A type of CTMC where transitions between states occur at random times, often modeled as Poisson processes, with applications in systems with jumps or shocks. | Biology (gene expression), finance (interest rate models), queuing systems |
| **Continuous-Time Hidden Markov Model (CT-HMM)** | An extension of HMM into continuous time, where transitions between hidden states occur continuously rather than at discrete intervals. | Medical prognosis, finance, signal processing |
| **Quasi-Birth-Death Process (QBD)** | A Markov process that extends the birth-death process to multiple types of transitions, often used in queuing systems with complex state transitions. | Telecommunication networks, inventory systems, healthcare operations |

## Uses

| **Field** | **Application** | **Description** |
| --- | --- | --- |
| **Finance** | **Stock Price Modeling** | Used to model the random behavior of stock prices and financial markets, particularly in options pricing and risk management. |
| **Economics** | **Market Dynamics** | Applied to study consumer behavior, economic cycles, and the spread of information in markets. |
| **Queueing Theory** | **Service Systems** | Models the behavior of queues in systems such as customer service centers, network traffic, and manufacturing processes. |
| **Genetics** | **Population Genetics** | Used to model the inheritance of genes and genetic drift over generations in a population. |
| **Epidemiology** | **Disease Spread** | Models the spread of infectious diseases in populations, helping in predicting outbreaks and the effectiveness of interventions. |
| **Operations Research** | **Inventory Management** | Helps in optimizing inventory levels by modeling the restocking process and demand fluctuations. |
| **Computer Science** | **PageRank Algorithm** | Used by Google's search engine to rank web pages based on the likelihood of a user randomly clicking links (a Markov chain model). |
| **Speech Recognition** | **Hidden Markov Models (HMMs)** | Applied in speech recognition systems to model the sequence of spoken words, matching audio signals to likely word sequences. |
| **Robotics** | **Navigation and Localization** | Helps robots navigate and estimate their position in an environment by modeling the transition probabilities between states. |
| **Game Theory** | **Strategy Development** | Models decision-making scenarios where outcomes depend on both current and previous states, often used in stochastic games. |
| **Weather Prediction** | **Modeling Weather Patterns** | Used to predict future weather conditions based on current states, modeling transitions between different weather patterns. |
| **Marketing** | **Customer Behavior Analysis** | Analyzes customer transitions between different states, such as brand loyalty, purchasing habits, or website navigation. |
| **Supply Chain Management** | **Demand Forecasting** | Models the probability of demand levels over time, aiding in supply chain optimization and inventory control. |
| **Insurance** | **Risk Assessment** | Used to predict the likelihood of events like claims or accidents over time, assisting in setting premiums and reserves. |
| **Neuroscience** | **Neuronal Activity Modeling** | Models the firing patterns of neurons as they transition between different states, helping to understand brain activity and information processing. |

## A note on the name

The n-gram case is the one that shows why the state definition matters. A second-order model over words is not first-order Markov in the *word*; it is first-order Markov in the *pair of words*, and the transition is written (what, the) → (the, …). Markov observed the same gap in the early 1900s and constructed his chain on dependent trials precisely to show that dependence does not require independence of the increments — the model class was born as a counterexample, not as an approximation.

## References

- Examples of Markov chains. (n.d.). In *Wikipedia*. https://en.wikipedia.org/wiki/Examples_of_Markov_chains
- Hoyt, B. (2024). *Using a Markov chain to generate readable nonsense with 20 lines of Python* [Blog post]. https://benhoyt.com/writings/markov-chain/ · discussion: https://news.ycombinator.com/item?id=38829772
- *An introduction to the theory of Markov processes* [Lecture notes]. (2015). KU Leuven. https://fys.kuleuven.be/english/staff/christ/files/pdf/pub/markovlectures2015.pdf
- Kemeny, J. G., & Snell, J. L. (1960). *Finite Markov chains*. Van Nostrand.
- Markov, A. A. (1906/1971). Extension of the limit theorems of probability theory to a sum of variables connected in a chain. In R. A. Howard (Ed.), *Dynamic probabilistic systems: Vol. 1. Markov models* (pp. 552–577). Wiley.
- Markov chain. (n.d.). In *Wikipedia*. https://en.wikipedia.org/wiki/Markov_chain
- Markov kernel. (n.d.). In *Wikipedia*. https://en.wikipedia.org/wiki/Markov_kernel
- Markov model. (n.d.). In *Wikipedia*. https://en.wikipedia.org/wiki/Markov_model
- Markov model (working note). (n.d.). *Notion*. https://app.notion.com/p/489031f368a14dc2a5b4f65709bb8f80
- Markov property. (n.d.). In *Wikipedia*. https://en.wikipedia.org/wiki/Markov_property
- Meyn, S. P., & Tweedie, R. L. (2009). *Markov chains and stochastic stability* (2nd ed.). Cambridge University Press.
- Norris, J. R. (1998). *Markov chains*. Cambridge University Press.
- Video on Markov chains [Video]. (n.d.). *YouTube*. https://www.youtube.com/watch?v=CIe869Rce2k
- Video playlist on Markov chains [Video playlist]. (n.d.). *YouTube*. https://www.youtube.com/playlist?list=PLu0UjEkXuQyo_tqRSqht_vNyB8zeejSx-
