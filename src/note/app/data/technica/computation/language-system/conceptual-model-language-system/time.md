---
tags: [model-of-computation]
---

# Time

- [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md), [Declarative Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/declarative-model-of-computation.md)

> The *problem of time* in programming refers to the difficulty of reconciling ***temporal ordering***, ***causal dependency***, and ***observable state change*** with purely ***referentially transparent* computational models**—particularly in functional programming, where time-dependent behavior must be modeled without side effects.
> 

## Key Questions

- What is the Role of Time in Computing?
- Why is the concept of time essential for expressing certain processes? Which types of processes depend on it, and what makes them inherently temporal?

## Summary

| Aspect of Time | Importance in Computation |
| --- | --- |
| Order of operations | Ensures correct dependencies and causality |
| State evolution | Tracks how data changes over time |
| Side effects | Timing affects interaction with the external world |
| Synchronization | Coordination among parallel or distributed tasks |
| Resource usage | Measuring efficiency and performance |
| Real-time constraints | Meeting strict deadlines and predictable behavior |

## The Role of Time in Computing

> The **role of time in computation** is fundamental but multifaceted, because computation inherently unfolds *over time*. Here’s a structured overview of what “time” means and why it matters in computing:
> 

### **Time as Sequence and Ordering**

- Computations happen **step by step**, sequentially or concurrently.
- The **order of operations** matters; some steps depend on the results of previous ones.
- Time enforces causality: outputs depend on inputs computed at earlier times.

### **Time and State Change**

- Many computations involve **changing state** over time.
- State transitions can be thought of as snapshots taken at different moments.
- Managing and reasoning about state changes over time is a core challenge, especially in imperative and reactive systems.

### **Time and Side Effects**

- Effects like reading input, writing output, or modifying memory are **time-sensitive** actions.
- The exact timing and order of side effects influence program behavior and correctness.

### **Time Complexity**

- Time also refers to **resource usage** — how long a program takes to run (time complexity).
- This is a theoretical and practical concern for algorithm design and optimization.

### **Logical and Physical Time**

- **Logical time** refers to ordering of events or steps (e.g., Lamport clocks in distributed systems).
- **Physical time** refers to actual clock time, often important in real-time or embedded systems.

## Approaches to Time in Computation

> How different models of computation deal with time?
> 

> Note: These are not models of computation itself by you can treat them as one.
> 

> **Functional Reactive Programming (FRP):** Treats time as a first-class concept, modeling continuous or discrete data streams evolving over time.
> 

> **Event-driven programming:** Time is implicit in event order and timing.
> 

> **Asynchronous programming:** Time is represented via futures, promises, callbacks, allowing computations to proceed without blocking.
> 

| Model | Role of Time |
| --- | --- |
| **Turing Machine / Classical** | Abstract time as discrete computation steps (state transitions) |
| **Functional Programming** | Time as a sequence of immutable states or explicit effects (monads) |
| **Concurrent / Parallel Systems** | Time for coordinating multiple processes, synchronization, race conditions |
| **Real-Time Systems** | Strict timing constraints, deadlines, and predictability |
| **Distributed Systems** | Time for ordering events (logical clocks), dealing with delays and partial failures |

## Correctness

> How to Reason About the Correctness of Time-Dependent Processes?
> 

A process is time-dependent if:

- **The order of events affects correctness** (non-commutative operations),
- **Past states or inputs influence future outputs** (history-sensitive behavior),
- **Temporal constraints** exist (e.g., deadlines, minimum durations),
- **Interaction with the external world** (I/O, UI, control systems) unfolds in real time.

**Correctness Criteria:**

| Criterion | Description |
| --- | --- |
| **Causality** | Outputs must only depend on past and present inputs (no time-travel). |
| **Temporal Ordering** | Events occur in the intended sequence (`A → B`, not `B → A`). |
| **Safety** | "Nothing bad ever happens" (e.g., no buffer overflows, invariants hold). |
| **Liveness** | "Something good eventually happens" (e.g., response eventually sent). |
| **Deadline Compliance** | Events happen *within* time constraints (real-time systems). |
| **Fairness** | No process is starved indefinitely (in concurrent systems). |

**Methods:**

> See more in [Verification](note.html?n=technica/computation/dependability/verification.md).
> 

| **Category** | **Method** | **Description** |
| --- | --- | --- |
| **Temporal Logic** | **LTL (Linear Temporal Logic)** | Specifies properties over linear sequences of states (e.g., "eventually", "always", "until"). |
|  | **CTL (Computation Tree Logic)** | Captures branching-time properties using path quantifiers (`A`, `E`) and temporal operators. |
|  | **TLA+** | Formal specification language combining logic and set theory, for reasoning about concurrent/time-sensitive systems. |
| **Model Checking** | **Explicit-State Model Checking** | Explores all possible states and transitions to verify whether properties hold. |
|  | **Symbolic Model Checking** | Uses BDDs or SAT/SMT solvers to reason about large or infinite state spaces. |
|  | **UPPAAL / Kronos** | Model checking of real-time systems using *timed automata*. |
| **Automata-Based Models** | **Finite State Machines (FSMs)** | Reason about state transitions and behavior over time, assuming discrete time steps. |
|  | **Timed Automata** | Extends FSMs with clocks to capture timing constraints explicitly. |
|  | **Hybrid Automata** | Combines discrete transitions and continuous time dynamics (for cyber-physical systems). |
| **Denotational Semantics** | **Streams / Signals** | Model time as functions (`Time → Value`) or infinite sequences, enabling compositional reasoning. |
|  | **FRP (Functional Reactive Programming)** | Encodes time-evolving behaviors with pure functions, often using lazy evaluation or arrows. |
| **Operational Semantics** | **Small-Step Semantics** | Defines computation as stepwise transitions; time is implicit in step order. |
|  | **Big-Step Semantics** | Focuses on full evaluations, useful for reasoning about end states rather than execution timing. |
| **Type-Theoretic** | **Dependent Types** | Types can express time-dependent invariants (e.g., a buffer that empties after N steps). |
|  | **Refinement Types** | Attach logical predicates to types (e.g., “event occurs within 5 time units”). |
|  | **Session Types (Timed Variants)** | Specify time-aware communication protocols between processes. |
| **Concurrency Theory** | **Process Calculi (e.g., CSP, π-calculus)** | Model communication and synchronization between time-sensitive processes. |
|  | **Happens-Before Relations** | Captures causal relationships in concurrent and distributed systems (e.g., Lamport clocks). |
| **Runtime Methods** | **Temporal Assertion Checking** | Specify properties (e.g., "event X within 2s of Y") and monitor execution to detect violations. |
|  | **Runtime Verification** | Lightweight formal methods applied during execution to ensure temporal correctness. |
| **Scheduling Theory** | **Rate Monotonic / EDF** | Analyze schedulability and timing guarantees in real-time systems. |
|  | **Worst-Case Execution Time (WCET)** | Determine upper bounds on computation time to ensure deadline compliance. |
| **Simulation / Testing** | **Timed Simulation** | Simulate system execution under various time conditions (e.g., jitter, delay). |
|  | **Property-Based Testing** | Generate and check traces against time-sensitive specifications (e.g., using temporal patterns). |

## QA

### Why is the concept of time essential for expressing certain processes? Which types of processes depend on it, and what makes them inherently temporal?

> Time is a fundamental concept in computing because some processes are inherently **stateful, sequential, or interactive**, making temporal ordering crucial for correctness and behavior.
> 

> Time isn’t just an implementation detail—it’s often **the core abstraction** defining how a system behaves.
> 

**Processes That Depend on Time**

| Type of Process | Why It’s Temporal |
| --- | --- |
| **Reactive Systems** | Must respond to inputs/events over time (e.g. UI, robots). |
| **Control Systems** | Adjust behavior based on evolving conditions. |
| **Simulations** | Model physical/biological/social systems through time. |
| **Streaming Data Processing** | Analyze time-ordered data (e.g. audio, video, telemetry). |
| **Animations & Graphics** | Interpolation and rendering require frame-by-frame updates. |
| **Machine Learning (RNNs, LSTMs)** | Time-series prediction, sequential decision-making. |
| **Concurrency & Scheduling** | Depend on timing for fairness, deadlines, and coordination. |
| **Biological/Cognitive Modeling** | Mental states, attention, memory all evolve with time. |
| **Stateful Computations** |  |
| **I/O & Interactive Systems** |  |
| … |  |

**What Makes These Processes Inherently Temporal?**

- **Order Matters (Non-commutativity) (Order Sensitivity)** : Swapping two operations can change the result (e.g., withdrawing money before depositing). The order of operations matters (`A → B ≠ B → A`).
- **Causality**: Some events must happen before others (e.g., receiving a message before replying).
- **History-dependence**: Current output depends on prior inputs or states.
- **Liveness vs. Safety**: Some systems must **eventually** produce results (liveness) while avoiding bad states (safety).
    - **Duration-sensitive behavior**: How long something takes or lasts affects outcomes.
    - **Temporal constraints**: Some tasks must happen *within* a time window.
    - **Deadlines**: Real-time systems fail if responses are too late.
    

### Can pure lazy functional programming effectively (express) model inherently temporal processes?

> Pure functional programming *can* model temporal processes — but only by reifying time as an explicit structure in the program.
> 

> Pure functional programming, as envisioned by John Backus, can model temporal processes by reifying time as an explicit structure—typically as infinite streams, coinductive data types, or signal functions—rather than relying on implicit side effects or mutable state. Temporal behavior is represented through the transformation of time-indexed values (e.g. `Signal a = Time → a` or `Stream a = [a]`), allowing compositional and declarative reasoning over evolving systems. Techniques such as Functional Reactive Programming (FRP), arrowized signal processing, and lazy evaluation enable the encoding of causality, sequencing, and time-dependence entirely within the pure function-level paradigm. However, real-time interaction with external systems still requires effectful interfaces, usually isolated in monads like `IO`.
> 

## References

- [Time](note.html?n=technica/computation/miscelanea/time.md)
- [‣](https://app.notion.com/p/10e598edb7908183ba99f3b404ea8627?pvs=21)
- https://news.ycombinator.com/item?id=27554355
- https://www.microsoft.com/en-us/research/publication/tackling-awkward-squad-monadic-inputoutput-concurrency-exceptions-foreign-language-calls-haskell/