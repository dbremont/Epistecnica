---
tags: [learning-system]
---

# Markov Model


> A Markov model is a stochastic process in which the probability of each future state depends only on the present state and not on the sequence of events that preceded it.
> 

> A discrete-time stochastic process satisfying the Markov property is known as a [Markov chain](https://en.wikipedia.org/wiki/Markov_chain).
> 

> The result is a class of probability distributions on the possible trajectories.
> 

> In the early 1900s Markov himself already observed this "bug" and proposed an n-gram model to rectify it. That style of model designs transitions of pairs (or triplets, or 4-tuples, etc) of words. So your first example is modelled as the state transition (what, the) -> (the, fuck) in a 2-gram Markov Chain.
> 

> **Transition Probabilities:** Probabilities associated with moving from one state to another.
> 

> **Markov Property:** Whether the future state depends only on the present state and not on the sequence of events that preceded it.
> 

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

## References

- https://en.wikipedia.org/wiki/Markov_model
- [‣](https://app.notion.com/p/489031f368a14dc2a5b4f65709bb8f80?pvs=21)
- [Markov chain](https://en.wikipedia.org/wiki/Markov_chain)
- https://en.wikipedia.org/wiki/Markov_property
- https://www.youtube.com/playlist?list=PLu0UjEkXuQyo_tqRSqht_vNyB8zeejSx-
- https://www.youtube.com/watch?v=CIe869Rce2k
- An introduction to the theory of Markov processes [https://fys.kuleuven.be/english/staff/christ/files/pdf/pub/markovlectures2015.pdf](https://fys.kuleuven.be/english/staff/christ/files/pdf/pub/markovlectures2015.pdf)
- [‣](https://app.notion.com/p/489031f368a14dc2a5b4f65709bb8f80?pvs=21)
- [Using a Markov chain to generate readable nonsense with 20 lines of Python](https://news.ycombinator.com/item?id=38829772) ([benhoyt.com](http://benhoyt.com/))
- [Examples of Markov chains](https://en.wikipedia.org/wiki/Examples_of_Markov_chains)
