---
tags: [computation]
---

# Computation  (Computational Process)

- [Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md), [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md), [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md)

> A note that dives deep into the very abstract notion of computation.
> 

> For a more formal treatment see [Computation](https://app.notion.com/p/Computation-1c8c0f5171ec8074a6fbe931c2102aec?pvs=21).
> 

QA:

- How can the notion of computation — a process directed via a program — be conceived? What is the **underlying conception of change**?
- …
- Which can be the generator - of the dynamics - that  it’s what underlies the computation - what is the atom of change?
    - Transition Semantics
    - …

## Formulation

### **What is a computation?**

> A computation is an evolution of formal states under a rule-governed transition relation, independent of any particular physical substrate. At its core, it is a process that maps inputs to outputs through a series of intermediate configurations, each determined by syntactic operations defined by some model of computation (e.g., λ-calculus reductions, Turing machine transitions, register-machine instructions). What distinguishes computation from mere physical evolution is that its dynamics are **denotationally interpretable**: the transitions can be understood as implementing a mathematical function or procedure. Computation is thus best seen as a layered construct—an abstract causal structure realized in some medium but not reducible to it—where the notion of “doing work” is the principled traversal of a well-defined state space.
> 

### How can the notion of computation — a process directed via a program — be conceived? What is the **underlying conception of change**?

> Note: The idea of `Change Formalism` is the fundamental notion needed to have a reasonable conception of a model of computation.
> 

> Note: The only conception of change that we are interested in Computer Science are the one that can be `capture - induced - represented`  via a `program`.
> 

> See more [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md).
> 

### **What constitutes the *state* of a computation?**

> The state of a computation is the complete, minimal, and sufficient description of the information necessary to determine the computation’s *next* step under its transition rules. This includes the explicit data (e.g., symbols on a tape, values in registers), the control position (e.g., program counter, continuation structure), and any latent structure determining future behavior (e.g., call stack, environments, closures, memory stores). Crucially, state is not merely data—it is the **entire computational configuration**, the snapshot of the machine’s operational semantics at a given instant. By choosing different abstractions (e.g., small-step vs large-step semantics), one can compress or expand what counts as “state,” but the invariant is that it must encode all causal determinants of the computation’s next move.
> 

### **How to think about the notion of a set of related computation? Is this useful for the praxis?**

> Imagine Sorting - Different Data, Maybe Different Paths, etc. A set of related computations is best conceptualized as a **computational ensemble**: multiple executions of the same program (or algorithmic schema) across varying inputs, nondeterministic choices, or environmental conditions. The **ensemble reveals the program’s *behavioral topology*:** the branching structure of possible execution paths, the conditions under which paths diverge or converge, and the invariants preserved across all runs. In praxis, this notion is indispensable because engineering robust systems requires reasoning not about a single trajectory but about the entire **family of trajectories** a system can generate—e.g., all possible sorting operations on all inputs, or all scheduling outcomes in a distributed system under arbitrary message delays. Related computations thus form a space in which one can analyze stability, worst-case complexity, robustness, and emergent patterns.
> 

## Description

> **What is the relation of a computation and a program?** A program is a *description* of a computation, not the computation itself. Formally, a program is a syntactic artifact—an element in some programming language—whose operational semantics induces one or more computations when interpreted or executed. The computation is the dynamic unfolding of that description in time. This distinction is crucial: programs are static structures in a symbolic system, while computations are temporally extended processes in an abstract state space. The mapping from program to computation is mediated by a model of execution, which may itself vary (e.g., different evaluation strategies, machines, or abstract interpreters), showing that the same program can denote many possible computations depending on the execution environment.
> 

> How to describe a **set of related computations**? What is gained when a program can shape its own execution path, thereby generating not a single computation but a family of possible computations? A set of related computations can be described through **conditional, parameterized, or nondeterministic operational semantics**, capturing all branches that may arise from input variation or internal control flow. When a program dynamically shapes its own execution path—through conditionals, recursion, continuations, or reflective mechanisms—it ceases to define a single linear computation and instead defines a **computation-generating process**: a mechanism that produces a *family* of potential executions. This increases expressive power because it lets the program encode *decision structure* rather than fixed procedure, enabling adaptability, context-sensitivity, optimization, and generalization. It also enables the analysis of global behavior—proofs of correctness, complexity bounds, or safety properties—over entire execution families rather than isolated traces.
> 

### Semantics

**Semantics: What is the mapping from a program to the computational process it induces?**

The semantics is the *contract* that a language system establishes between a program’s static form and the dynamic process it must generate during execution. It specifies, in a mathematically precise way, how each syntactic construct contributes to the construction, evolution, and termination of the computation. Through this contract, the semantics guarantees that programs have *determinable meaning*: the same program, interpreted under the same semantic rules, will always give rise to the same abstract computational trajectory, independent of the underlying machine or implementation strategy. Semantics thus mediates between syntax and behavior, ensuring that the structure of a program reliably induces the computational process it is intended to denote.

### Self-Referential

> **What is the nature of computations that manipulate their own descriptions, thereby altering or influencing their own behavior?** Self-referential computations operate within a meta-level in which the boundary between program and data dissolves: the computation has access to, and can transform, the very structures that determine its behavior. Examples include meta-circular interpreters, self-modifying code, reflective languages, and partial evaluators that specialize programs using fragments of themselves. Such systems exhibit **computational reflexivity**: they can represent their own transition rules internally and alter them, effectively changing the mapping from description to execution. This creates a powerful but delicate dynamical regime where the computation’s semantics become **endogenous**—shaped internally rather than externally imposed—leading to expressive capabilities such as adaptation, learning, optimization, or bootstrapping, but also exposing risks of instability or undecidability.
> 

### Execution Model

> **How does the execution model constrain or expand the expressivity of a model of computation?** The execution model determines *how* a program’s semantics are realized—whether evaluation is strict or lazy, deterministic or nondeterministic, sequential or concurrent, and so on. Although many models remain Turing-complete in expressive power, the execution model shapes what can be expressed **naturally, efficiently, or compositionally**. For example, concurrency primitives dramatically expand expressive clarity for parallel processes, while laziness enables expressions of infinite data structures without explicit control scaffolding. Conversely, restrictive models (like finite automata or purely functional languages without side effects) limit the shape of state transitions, yielding simpler but less expressive behaviors. Thus, the execution model determines not the *absolute* theoretical limits but the *practical expressive geometry* of the computations one can formulate.
> 

> **Note:** It is a *contract* between the language system and the programmer—the computation’s **conjurer, inducer, and describer**. The programmer provides a syntactic artifact, trusting that the language’s semantic rules will faithfully transform that description into the intended computational process. Conversely, the language system promises that every construct, expression, and control form has a precisely defined behavioral interpretation, so that the programmer can reason about, predict, and ultimately *shape* the family of computations the program may induce.
> 

## Multicomputaiton

> **How to think about multicomputaiton or many threads of computation over the same environment?**
> 

> Multicomputation can be conceived as the **concurrent evolution of multiple computational trajectories**—potentially heterogeneous in structure, causality, and resource profile—unfolding over a **shared configurational substrate** whose **state is itself an aggregate function of all active threads**. At a technical level, each individual computation induces its own transition relation, but these relations are no longer independent: they interleave, contend, or cooperate through a common environment that acts as a higher-order state space whose updates must respect some global consistency condition (e.g., a memory model, a transactional semantics, a conflict-resolution policy, or a scheduler). Thus multicomputation is not merely “parallelism” but a second-order dynamical system in which computations become interacting processes whose mutual interference or reinforcement shapes the overall evolution. One can formalize this as a coproduct of labeled transition systems coupled through shared state variables, or as a fibered dynamical system in which each thread’s local transition is a section subject to global invariants. The analytic challenge is that the semantics of any single thread is no longer closed: the meaning of its next state depends on the concurrent histories of others, making the semantics relational, non-deterministic, and often path-dependent. Consequently, multicomputation is best understood as computation over a non-separable phase space, where both expressive power and complexity arise from the compositional structure of interacting computational flows rather than from the isolated capabilities of a single machine.
> 

## Transition Semantic(s)

> See  Transition Semantic(s)
> 

## Implementation

> **What is the relationship between physical implementation and abstract computation?** Why can the same computation (e.g., calculating "2+2") be realized in silicon, water, neurons, or tinker toys? What is the "substance" of the computation that remains invariant across these wildly different physical substrates? Physical implementation provides the causal substrate that instantiates the abstract transition structure of computation. What remains invariant across substrates—silicon, neurons, water pipes, tinker toys—is the **causal topology**: the pattern of state transitions and their dependencies. Abstract computation is substrate-independent because it concerns only this topology, not the material through which it is realized. A physical system implements a computation when its causal dynamics can be homomorphically mapped onto the formal transition system described by the model of computation. Hence, “2+2” is not a physical act but a pattern of transitions that can be encoded in many physical systems so long as they preserve the relevant causal relations.
> 

## Meaning

> **How does semantic meaning (the "aboutness" of a thought or symbol)
 arise from purely syntactic, rule-based computation?** How do the 1s and 
0s inside a computer, which are utterly meaningless in themselves, come 
to *represent* a cat video, a financial transaction, or a mathematical proof for a conscious observer? Semantic meaning emerges through **interpretation**, the mapping from syntactic structures to the world, mediated by a cognitive agent or an embedding environment that assigns significance to patterns of tokens. Computation itself operates purely on form—symbol manipulation under syntactic rules—but when a system is situated within an environment in which certain configurations reliably covary with external states (e.g., binary encodings of images, prices, proofs), the computation can come to *represent* something beyond itself. Meaning thus arises not from the symbols but from the **triadic relation** between symbol, system, and world: syntactic state → referential mapping → semantic content. For humans and high-level systems, this mapping is stabilized by conventions, inference, and memory; for machines, by encoding schemes and interfaces. In both cases, semantics is not inside the 1s and 0s but in the interpretive architecture that links them to a domain of discourse.
> 

## References

- https://plato.stanford.edu/entries/computer-science/
- https://plato.stanford.edu/entries/computation-physicalsystems/