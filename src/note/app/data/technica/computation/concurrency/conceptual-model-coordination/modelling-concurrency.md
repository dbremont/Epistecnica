---
tags: [formal-model]
---

# Modelling Concurrency


> A collection of mathematical, graphical, and algebraic frameworks—such as interleaving models, transition systems, Petri nets, process calculi (CSP, CCS, π-calculus), actor models, temporal logic, vector clocks, and event structures—used to represent, analyze, and reason about concurrency, synchronization, communication, and causal relationships in distributed and parallel systems.
> 

| **Category** | **Formalism** | **Description** |
| --- | --- | --- |
| **Interleaving-Based Models** | Interleaving Model | Represents concurrent execution as a sequence of atomic steps, interleaving actions from threads. |
|  | Transition Systems | Models systems as states and transitions, where each transition represents an action. |
| **Graphical/Mathematical Models** | Petri Nets | Describes systems using places, transitions, and token flow. |
|  | Event Structures | Represents causal relationships between events in a concurrent system. |
| **Process Algebras/Calculi** | Process Calculi | Algebraic frameworks for modeling concurrent systems. |
|  | CSP (Communicating Sequential Processes) | Focuses on message passing and synchronization between processes. |
|  | CCS (Calculus of Communicating Systems) | Models systems using actions and composition operators. |
|  | π-Calculus | Extends CCS to handle dynamic process creation and communication. |
| **Actor-Based Models** | Actor Model | Models systems as collections of actors communicating via asynchronous messages. |
| **Temporal/Logical Models** | Temporal Logic | Specifies and verifies temporal properties of concurrent systems. |
|  | Vector Clocks | Tracks causal relationships between events in distributed systems. |
|  | Lamport Timestamps | Provides a partial ordering of events in distributed systems. |
| **Event-Based Models** | Event Structures | Represents events and their dependencies in a concurrent system. |

## References

- https://en.wikipedia.org/wiki/Petri_net