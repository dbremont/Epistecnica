---
tags: [program]
---

# Program

- [Program Element](note.html?n=technica/computation/language-system/conceptual-model-language-system/program-element.md), [Computation Description Artifact](note.html?n=technica/computation/language-system/conceptual-model-language-system/computation-description-artifact.md)

> A program is a set of interconnected **computational elements** that **animate a computational process**.
> 

> A program describes a family (or space) of possible computations.
> 

> A computation is a set (or sequence) of state transitions governed by the rules of the program.
> 

> A computation is a set of successive configurations (states and control points) representing one possible **execution path** of a program.
> 

Guiding Questions:

- …

## Goal

> 

## Ontology

> A **program** *is a text* or *formal structure* that encodes rules of transformation.
> 

> *The program is a potential rule books that guides the  unfolding physical process.*
> 

## Formulation

### Formal Structure

> The **formal structure** of a program defines its syntactic and operational grammar — the symbolic system through which computational processes are described.
> 

> **Token of computation:** the atomic symbol or instruction that, when interpreted, effects a transformation in state.
> 

> **State:** the complete configuration of all relevant variables and control information at a given instant.
> 

> See more in [‣](https://app.notion.com/p/15f598edb7908187a28bea3fc54ad64e?pvs=21).
> 

### Meaning Structure

> The **meaning structure** maps formal symbols to semantic effects.
> 

> It defines how the syntactic elements of a program correspond to actions, transformations, or conditions in an abstract computational universe.
> 

> It is the **bridge between representation and operation**, or between the “grammar of computation” and its “world of meaning.”
> 

### Causal Structure

> The **causal structure** specifies the dependency relations among states, instructions, and effects.
> 

> It determines the flow of control (computation) — what happens before and after — and thus defines the *temporal topology* of computation.
> 

> **Flow of Execution:** The **Flow of Execution** is the **order in which the instructions of a program or steps of a computation are carried out**. It defines how a computation proceeds from start to finish. Understanding it is crucial for analyzing both the behavior and structure of programs.
> 

> **Computation Path:** A computation path is an ordered sequence of program states representing one possible execution of the program. Or the set of **instructions executed**.
> 

> **Computation Path:** A computation path is one element of the set of all possible computations described by a program; it represents a particular realization of its semantics under a given set of conditions or inputs.
> 

> A **program’s control structure** (sequence, branching, loops, function calls, concurrency) determines **all the possible paths a computation can take**.
> 

> Each path corresponds to **one possible execution**, i.e., one sequence of states over time. That is a **Computation**. Along each path, the flow of execution defines a **temporal order**: what happens **before** and **after**.
> 

What happens, we  program  to embed multiple’s flow of execution?

- **Correct Temporal Order:** The **correct temporal order** is the **sequence of events or state transitions that respects the logical and causal dependencies of a computation**. In other words, it ensures that each computation step happens **after all its prerequisites have been completed**.
- Space of Temporal Ordering: The **space of temporal ordering** is the abstract structure that represents **all possible sequences of events or states that a computation can follow**, taking into account **causal dependencies, branching, and concurrency**.

How to conceptualize a computation when we have multiple execution flows at the same time?

> Things get complicated because we need both;  the computation or computation that unfolds  for both execution flow -  but also we need to capture the time (in order to understand the interaction with the state).
> 
- Time T;   Execution 1:  Instruction A,  Execution 2:  Instruction B,
- Time T;   Execution 1:  Instruction A,  Execution 2:  Instruction B,
- So we need to record; the instruction set (computation)  that drives the state changes, but add a tag of time;
- Formalism
    - Timed Traces
    - Event Logs with Timestamps
    - Petri Nets
    - Message Sequence Charts
    - State Machines with Time Labels

### Computational (Refined) Form

> **Computational Space:** The set of all computation paths definable by the program.
> 

> The computation unfolds in the light of the **physical substrate** and is fundamentally molded by the **execution environment** — including memory, processor architecture, I/O constraints, and external interactions — which together determine the **realizable paths** within the program’s computational space.
> 

### Systemic Structure

> The **systemic structure** situates the program within a broader environment of interaction — between input, output, memory, and external systems.
> 

> It provides the **context of enactment** for computation.
> 

### Design Structure

> The **design structure** reflects the intentional organization of the program — its modularity, abstraction layers, and architecture.
> 

> It expresses the **human conceptual schema** behind the program: how functions, data, and processes are decomposed, named, and composed to achieve a goal.
> 

> The design structure reveals the *cognitive form* of the program: the way human reasoning is crystallized into formal mechanisms.
> 

## Property

> What types of properties can programs themselves have?
> 

## References

- [Algorithm](note.html?n=technica/computation/algorithm.md)
- [‣](https://app.notion.com/p/15f598edb7908187a28bea3fc54ad64e?pvs=21)
- [Property](https://app.notion.com/p/Property-271c0f5171ec80498865e3db652beafb?pvs=21)
- https://en.wikipedia.org/wiki/Computer_program