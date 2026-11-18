---
tags: [note]
---

# An Essay on Representation in Computationally Synthesized Systems


> 
> 
> 
> In this note, we reason deeply about the concept of representation in computationally synthesized systems, particularly neural networks, addressing the question: What does it mean to say that a **neural network** represents $x$?
> 

> A **Trained  Neural network representation capacity** is fundamentally **state changes induced by the system’s underlying dynamics (including re-current dynamics)**. Other perspectives—such as the **geometric, feature, circuit, and algorithmic views**—can be understood as **different levels of description of this same dynamical system**. The structure of characterization of **such dynamics constitute the representation.** That is **r**epresentation through operationalization (dynamics).
> 

> Note: Some mental representations emerge during their operationalization. In working memory, they consist of multiple parts bound together by a scaffold. During the operationalization process, these parts are brought into working memory as needed.
> 

> **Note:** One possible criticism of this note is that it is merely linguistic and therefore unimportant. However, the distinction actually matters for understanding neural networks. In many papers and books, the notions of *representation* and *dynamics* are not made explicit and are often used interchangeably. For conceptual clarity, we need to specify whether a **representation refers to the network state** (e.g., an activation vector) or whether it refers to the **dynamics that generate those states**, that is, the transformations that induce trajectories in activation space.
> 

Guiding Questions:

- How **should representation** be conceptualized in computational systems, particularly neural networks?
- Is **representation instantiated** in the internal dynamics of the system (computation, connectivity, and state transitions), or in the resulting neural outputs produced by those dynamics?
- Is **representation** the mechanism or the result?
- Which **are the conceptions of representations**? Can all of them be derived from the notion of representation as dynamics?

## View Space

> Which are the **views on representation**?
> 

| **View** | **Description** | **Critique** | **How it can be derived from dynamics?** |
| --- | --- | --- | --- |
| **Activation View** | Representation is the **vector of neural activations** at some layer. A representation is simply the internal state $h_l(x)$ produced by the network. | Too shallow conceptually. Activations are only **snapshots**, not explanations of how representation arises. | Activations are **instantaneous states** of the dynamical system as it evolves through layers or time. |
| **Geometric View** | Representations are **geometric structures** (clusters, manifolds, directions, subspaces) in activation space. | Pure geometry ignores **mechanisms** that generate those structures. | Geometry emerges from the **global organization of trajectories** induced by the network's dynamics. |
| **Feature View** | Representations consist of **latent features** (e.g., directions in activation space) that encode properties like sentiment, syntax, objects, etc. | Features may not correspond to single neurons and can exist in **superposition**, making interpretation difficult. | Features correspond to **dynamical modes or stable directions** repeatedly amplified by the network transformations. |
| **Information View** | Representation is defined by **information preserved about variables** in the data (e.g., via mutual information $I(R;Y)$. | Information measures are often **difficult to estimate** and may ignore structural organization. | Information corresponds to **input properties that remain invariant under the network's transformations**. |
| **Manifold View** | Data is mapped onto **low-dimensional manifolds** in high-dimensional activation space. These manifolds encode latent factors like pose or identity. | Manifold assumptions sometimes fail when data representations are highly entangled. | Manifolds arise when dynamics map inputs into **structured attractor regions** in state space. |
| **Circuit View** | Representation arises from **computational circuits** composed of interacting neurons or attention heads implementing specific functions. | Circuits can be difficult to isolate in large networks and may be distributed. | Circuits correspond to **localized subsystems of the global dynamical process**. |
| **Algorithmic View** | The network represents and executes **algorithms** (e.g., copying, induction, arithmetic). | Hard to prove algorithmic equivalence; often inferred heuristically. | Algorithms correspond to **structured trajectories through state space produced by the network dynamics**. |
| **Compression View** | Representations are **compressed latent encodings** capturing task-relevant structure while discarding irrelevant details. | Compression alone does not explain *what structure emerges*. | Compression emerges when dynamics must **map diverse inputs into a shared low-dimensional latent structure**. |
| **Linear Decodability View** | A variable is represented if it can be **linearly decoded** from activations. Widely used in neuroscience and probing studies. | Linear decodability does not imply the network **uses** the information computationally. | Dynamics often reshape state space so that task variables become **linearly separable directions**. |
| **Probabilistic View** | Representations encode **probabilistic beliefs or latent variables** of a generative model. | Requires assumptions about latent-variable structure that may not exist in purely discriminative models. | Dynamics implement **approximate inference processes**, mapping inputs to latent states representing distributions. |
| **Dynamics View** | Representation is the organization of trajectories, attractors, and transformations in the network’s state space induced by its parameterized dynamics. The network defines a dynamical system where inputs generate flows through high-dimensional state space. | Can be abstract and difficult to measure directly. Requires tools from dynamical systems, geometry, and nonlinear analysis to study. | This is the primitive view. Other views arise as partial descriptions of the dynamical system: activations are instantaneous states, geometry is the structure of trajectories, features are dynamical modes, circuits are localized subsystems, algorithms are structured trajectories, and information corresponds to invariants preserved by the dynamics. |

## QA

### Why saying ‘a neuron detecting cat ears’ is misleading?

> A neuron that appears to “detect cat ears” does so **because the underlying network dynamics produce that response**. The neuron itself is not intrinsically a “cat-ear detector.” Its behavior is **induced by the learned transformation implemented by the network weights and nonlinearities**.
> 

## References

- https://arxiv.org/abs/2510.09782
- https://physics.allen-zhu.com/home
- [Representation](https://app.notion.com/p/Representation-1bac0f5171ec80f9a083ffbf6651ee3a?pvs=21)
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- https://en.wikipedia.org/wiki/Engram_(neuropsychology)
