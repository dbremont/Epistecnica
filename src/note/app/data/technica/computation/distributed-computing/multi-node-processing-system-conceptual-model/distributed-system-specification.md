# Distributed System Specification


## Modelling

> A system model captures our assumptions about how nodes and the network behave. It is an abstract description of their properties, which can be implemented by various technologies in practice.
> 

We need a set of tools to reason about distributed systems: A theory of distributed system / aka a model will consist: - A mathematical structure that abstract out all relevant properties of a large distributed system.

- In this class we will choose models from the family of automaton-based models.
- We model each process in the system as an automaton that has soem sort of local state, an dmodel local comptuation as transition rule that tell us how to update this tate in resopnse to various events.
- transition : state, event -> state
- This as some modelling assumptions about distributed system, in practice they are much more complex.
- Local state,
- Global State,
- Events,
- Transitions
- Proceses
- Links
- Timing Models
- Cryptography