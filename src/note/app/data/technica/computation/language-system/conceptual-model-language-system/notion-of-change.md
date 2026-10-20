---
tags: [effect-system, linguistic-abstraction, notion-of-change]
---

# Notion of Change

- [Continuation](note.html?n=technica/computation/language-system/conceptual-model-language-system/continuation.md), [Exception Handling System](note.html?n=technica/computation/language-system/conceptual-model-language-system/exception-handling-system.md), [Computation  (Computational Process)](note.html?n=technica/computation/language-system/conceptual-model-language-system/computation-computational-process.md), [Effect System](note.html?n=technica/computation/language-system/conceptual-model-language-system/effect-system.md), [Unit of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/unit-of-computation.md)

> In this note - we will introduce the (root) - main note about the idea of **change** - that is the formalism behind a computation.
> 

> This note will be intentionally highly abstract, yet necessary, in **order to concretize** the different forms of computation that emerge from different underlying notions of change.
> 

## Formulation

> Which are the different notions of change that concretize different **notions of computation**?
> 

> This are the main ones - others like reactions - can be formulated in terms of transition semantics., etc.
> 

| **Change Formalism** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Transition Semantics (Explicit Control Flow)  (Control Transfer) (Operational Semantics)** | Computation is conceived as discrete state transitions governed by operational rules. | State machines, structural operational semantics, automata, Function calls, continuations, jumps, schedulers |
| **Reduction (Denotational Semantics)** | Computation is the progressive simplification or normalization of expressions via rewrite rules. | Lambda calculus, term rewriting systems, β-reduction |
| **Causal Propagation** | Computation is the propagation of effects through a dependency or causal network. | Dataflow systems, reactive systems, propagation networks |
| **Constraint Resolution** | Computation is the satisfaction and propagation of constraints over variables or relations. | SAT solvers, logic programming, SMT systems |
| **Inference** | Computation is the derivation of new statements from existing premises according to formal rules. | Prolog, theorem provers, deductive systems |
| **State Evolution** | Computation is the evolution of a system through a state space over time. | Dynamical systems, hybrid systems, physical computation |
| **Trajectory Evolution** | Computation is the traversal of trajectories within a continuous or discrete phase space. | Differential equation systems, control systems |
| **Entropy Transformation** | Computation is the transformation, transfer, or reduction of informational uncertainty. | Information theory, thermodynamic computation |
| **Measurement-Induced Change** | Computation arises through observation-induced state collapse or selection. | Quantum computation, probabilistic systems |

## **Transition Semantics**

> Which are the type of construct that are used to guide transiction sematnics? Which are the general formulations used to encoded every possible constructed?
> 

> Note: Focused on mechanisms for transition semantics (step semantics), rather than higher-level computational formulations such as continuations themselves.
> 

> **A control flow model** is a representation of the sequence and order in which statements or instructions are executed in a program. It describes how the program’s control flows from one statement to the next, based on conditions, loops, and other control structures.
> 

> **Control flow** is like the conductor of an orchestra, directing each instrument at the right time to create a beautiful symphony.
> 

> A **model of control flow** is a representation of the order in which statements are executed in a program. It defines the sequence of execution of statements and how the program flows from one statement to another based on certain conditions or events.
> 

> **Call Stack Manipulation**: Directly controlling the function call stack (e.g., pushing/popping frames, tail calls, stack unwinding).
> 

> See more in ([Concurrency](note.html?n=technica/computation/concurrency.md)) for the idea of computation unit - and multi-computation.
> 

### Construct

| Category | Mechanism | Description | Instance Set |
| --- | --- | --- | --- |
| **Sequential Control** | instruction pointer / straight-line execution | Determines the next executable transition in a sequential process. | straight-line execution |
| **Branching Control** | conditional branching | Selects alternative transition paths based on predicates or state conditions. | `if`, `if-else`, `if-elif-else`, `switch`, `match` |
| **Iterative Control** | loops / recurrence | Repeatedly applies transitions until a termination condition is reached. | `for`, `while`, `foreach` |
| **Jump / Transfer Control** | explicit control transfer | Redirects execution flow to another transition point. | `break`, `continue`, `return`, `goto, **setjmp, longjmp**` |
| **Procedural Control** | function/procedure calls | Transfers execution into reusable subcomputations with return semantics. | function call, procedure call, recursion |
| **Coroutine / Suspension Control** | suspension and resumption semantics | Pauses and later resumes execution contexts. | `yield`, generators, coroutines |
| **Exception Control** | exception propagation and handling | Alters normal transition flow in response to exceptional conditions. | `try-except`, `finally`, `raise`, `throw`, `catch` |
| **State-Based Control** | state-transition relation | Transition legality depends on the current computational state. | finite-state machines, automata |
| **Stack-Based Control** | call stack / execution frames | Maintains nested execution contexts during transitions. | stack frames, activation records |
| **Message-Driven Control** | asynchronous message dispatch | Transitions are triggered by message arrival. | actor systems, mailboxes |
| **Event-Driven Control** | event dispatch | Internal or external events initiate transitions. | GUI events, interrupts, callbacks |
| **Data-Driven Control** | data availability triggering | Executability depends on input/data readiness. | dataflow execution, reactive streams |
| **Scheduler-Governed Control** | scheduling policies | Determines execution ordering and interleaving. | round-robin, priority scheduling, cooperative scheduling |
| **Reactive Control** | stimulus-response execution | Transitions react continuously to environmental changes. | reactive systems, feedback controllers |
| **Temporal Control** | clocks / synchronization | Governs transition timing and synchronization. | timers, barriers, synchronization primitives |
| **Probabilistic Control** | stochastic transition selection | Transition selection follows probabilistic rules. | Markov processes, randomized algorithms |
| **Non-Deterministic Control** | nondeterministic branching | Multiple valid next transitions may coexist. | nondeterministic automata, search branching |
| **Resource-Constrained Control** | resource-sensitive execution | Transition execution depends on resource availability. | semaphore-controlled execution, bounded-resource systems |
| **Spatially Localized Control** | neighborhood interaction rules | Local spatial configurations determine transitions. | cellular automata, lattice systems |
| **Transactional Control** | atomic commit/rollback | Groups transitions under atomicity and consistency constraints. | database transactions, STM |

### **Conditional Control Flow Model**

> **Note:** In programming, an `if` statement is conceptually closer to `condition && action` than to the logical implication `condition → action`. In formal logic, `p → q` is true in almost all cases (false only when `p` is true and `q` is false), which does not capture program control flow. By contrast, an `if` ensures that the action executes *only when* the condition evaluates to true, aligning better with the semantics of conjunction than implication.
> 

### Stack Based Technique Set

- Wee need to re-work this?
- …
- React Fiber (Compute on the Heap → Not the Stack) : https://github.com/acdlite/react-fiber-architecture/blob/master/README.md https://blog.logrocket.com/deep-dive-react-fiber/ (Solve Deep Recursion; Solve Drop Frames Visual)
    - Given a deeply recursive tree structure (e.g., Fiber), how should we operate over it — using the call stack (recursion) or the heap (explicit data structures)?
- …

### Formulation (Encoding)

> Which are the universal formulation (theories of everything) - in which every type of control flow (transition semantics) construct  can be encoded (defined) (formulated) in terms of?
> 

| Formulation | Description |
| --- | --- |
| **Continuation-Based Formulation** | Universal control-flow formulation where computation is represented in terms of explicit continuations — representations of “the rest of the computation.” All control-transfer constructs (`if`, loops, exceptions, coroutines, generators, async/await, backtracking, non-local exits, cooperative multitasking, etc.) can be encoded as continuation manipulation and continuation transitions. Control becomes explicit, reifiable, and composable. |
| **Continuation Monadic Formulation** | Control flow encoded through monadic sequencing where continuations are embedded in the monadic structure (especially the Continuation Monad). Computational effects and control operators are represented algebraically through `bind` composition. Constructs such as exceptions, nondeterminism, early exit, resumable computations, and delimited control can be formulated as monadic continuation transformations. Generalizes sequential control into compositional effectful pipelines. |
| **Algebraic Effects and Effect Handlers** | Universal effect/control formulation where computational effects are represented as abstract operations and interpreted by handlers. Control-flow constructs become effect invocations handled by semantic interpreters. Exceptions, generators, coroutines, async execution, schedulers, backtracking, probabilistic branching, and user-defined control operators can all be encoded uniformly. Separates effect declaration from effect interpretation, making control semantics modular and composable. |

## Reduction Based Change

> Computation = symbolic transformation (`λ`-calculus, rewriting, proof normalization)
> 

## References

- [Abstracting Control](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=eb653db18a55b400ebe77c7b4ed92cfbb3224afb)
- [Continuation-passing style](https://en.wikipedia.org/wiki/Continuation-passing_style)
- [Setjmp and Longjmp Implementation](https://stackoverflow.com/questions/46094444/setjmp-and-longjmp-implementation)
- How setjmp and longjmp work https://offlinemark.com/2016/02/09/lets-understand-setjmp-longjmp/
- Danvy, O., Filinski, A. (1992). Representing Control: a Study of the CPS Transformation. 2(4), 361–391.