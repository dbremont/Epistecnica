---
tags: [note, guia]
---

# A Set of Mental Models about ML


> Mental Models for Understanding ML - Deep Representation Learning.
> 

> Note:  ML System capacity - it’s all about  state evolution - it the dynamics.
> 

> The Key to Intelligence is how the brain builds  models (and represent and simulate) -
> 

**ML System (Deep Parametric Ones)**:

Computation (Inference)

→ Input Representation

→Internal Representation → … Internal Representation

→ Output:

→ Output Representation

→ Tag

## On Representation

> Note that a useful conception of representation will allow to makes sense of the dynamics that- the next internal representation - in the majority of ML system we will need to define representation as the (State + System Internal Configuration - Context - etc).
> 

> Meaning is **distributed across state + dynamics**, not localized in coordinates.
> 

> A task induces constraints on what constitutes a *useful state representation*, determining which aspects of the input must be preserved, abstracted, or discarded in order to support effective downstream computation.
> 

> **Will they be a universal representation?** It is unlikely that any single representation would be useful across all kinds of tasks. Even the human brain does not operate this way; instead, it exhibits strong functional specialization, with different tasks relying on differently structured internal representations.
> 

> What is the role of the structure of the state - representation? The structure of a state–representation determines which transformations are easy to learn, which distinctions are preserved, and which tasks the system can perform efficiently.
> 

## On Task

> Can they be one task to rule them all?
> 

> Next Token Prediction?
> 

> Task and Representation.
> 

## On Generation

> Is simulation generation? **All simulation is generation, but only generation grounded in internal state dynamics qualifies as simulation.**
> 

> There are two classes of trainable machine learning systems: one that learns both an internal ontology and the dynamics of the domain, enabling **generative or simulation capabilities**, and another that learns a **direct input–output mapping**, approximating the function from observations without constructing an explicit model of the underlying system.
> 

> Note: A system that learns input–output mappings may capture superficial or interfacial dynamics relevant to the task, but it does not acquire the deep ontological structure and intrinsic dynamical couplings required for faithful generative simulation of the domain.
> 

## World Model

> A **world model** is an internal generative model that a system constructs to represent the underlying structure and dynamics of its environment. Unlike simple input–output mappings, a world model encodes both **ontology** (what entities exist and their attributes) and **dynamics** (how these entities evolve over time under various conditions).
> 

“”

There is no question that world models should perform prediction in latent space.
The debate is whether the training criterion for world models should be based on predicting the observation (i.e. using a generative decoder) or through a collapse prevention criterion in representation space (as implemented by JEPA, DINO, and other joint embedding architectures).
My money is on the decoder-free, joint embedding approach.

“” ???

Structure

1. **State Representation:** Encodes the current situation, including objects, context, and internal variables relevant to the system.
2. **Dynamics Model:** Describes how states evolve over time, including probabilistic transitions and causal interactions.
3. **Observation Model:** Maps latent states to observable outputs, enabling comparison between predicted and actual observations for learning and correction.
4. **Control / Policy Module (Optional):** In systems capable of planning or acting, the world model interfaces with a policy to select actions that optimize objectives within the simulated environment.

## References

- https://www.youtube.com/watch?v=QWidx8cYVRs&t=49s
- https://www.youtube.com/watch?v=rie-9AEhYdY
- https://en.wikipedia.org/wiki/Discriminative_model
- https://en.wikipedia.org/wiki/Generative_model
- [The Brain as a Model Builder](https://app.notion.com/p/The-Brain-as-a-Model-Builder-243c0f5171ec80d9868efe03a537dc65?pvs=21)
    - https://www.pnas.org/doi/10.1073/pnas.1912340117
- https://arxiv.org/abs/1803.10122
- https://arxiv.org/abs/2511.09057v2
