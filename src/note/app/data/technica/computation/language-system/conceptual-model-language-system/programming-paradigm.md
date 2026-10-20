---
tags: [programming-paradigm]
---

# Programming Paradigm

- [Map/Reduce (MapReduce) Paradigm](note.html?n=technica/computation/language-system/conceptual-model-language-system/map-reduce-mapreduce-paradigm.md)

> **Programming Paradigm:** A programming paradigm is a fundamental style or approach to programming that shapes how problems are conceptualized and how solutions are expressed. It defines the structure, patterns, and techniques used in writing and organizing code.
> 

> **Programming Paradigm =   Style and Mechanisms to Write Programs in a Given Model of Computation.**
> 

> **Model of Computation vs. Programming Paradigm:** A *model of computation* provides a formal mathematical abstraction of how computation is performed (e.g., Turing Machine, Lambda Calculus, π-calculus). A *programming paradigm* , on the other hand, is a practical methodology for writing and structuring programs within or on top of such computational models. Paradigms often reflect different ways of reasoning about computation—stateful vs. stateless, declarative vs. imperative, etc.
> 

## Taxonomy

| **Family** | **Paradigm** | **Description** | **Underlying Model(s) of Computation** |
| --- | --- | --- | --- |
| **🧱 Imperative Family** |  | Programs express sequences of state-changing commands. | Turing Machine, Von Neumann Architecture |
|  | Structured Programming | Emphasizes clear, linear control flow (sequences, conditionals, loops); avoids `GOTO`. | Turing Machine |
|  | Procedural Programming | Organizes code into reusable procedures/subroutines; supports top-down design. | Turing Machine |
|  | Object-Oriented (OOP) | Encapsulates data/behavior in "objects"; uses inheritance/polymorphism. | Turing Machine, Class/Object Model |
|  | Modular Programming | Divides programs into modules with defined interfaces. | Turing Machine |
| **🧮 Declarative Family** |  | Focuses on *what* should be done, not *how*; avoids explicit control flow. | Lambda Calculus, Logic, Algebraic Models |
|  | Functional Programming | Uses pure functions (no side effects), recursion, and immutability. | Lambda Calculus |
|  | Logic Programming | Programs as logical rules; computation via theorem proving. | Predicate Logic, Resolution-Based Inference |
|  | Constraint Programming | Solves problems by stating constraints/relationships. | Constraint Satisfaction Problems (CSP) |
|  | Relational (e.g., SQL) | Describes relations/queries over data (databases). | Relational Algebra, Tuple Relational Calculus |
| **⛓️ Concurrent & Parallel** |  | Manages simultaneous processes/threads (message/memory communication). | CSP, Actor Model, π-calculus, Petri Nets |
|  | Concurrent Programming | Multiple independent/interacting operation sequences. | CSP, π-calculus, Actor Model |
|  | Parallel Programming | Explicit simultaneous computations for performance. | PRAM, Fork-Join Model, SIMD/MIMD |
|  | Distributed Programming | Concurrency across machines; handles network state/faults. | Message Passing, Distributed CSP |
|  | Reactive Programming | Reacts continuously to data streams/events. | Functional Reactive Programming, Event Streams |
| **🔁 Control Flow-Oriented** |  | Controls execution order and side effects. | State Machines, Continuation Passing Style |
|  | Event-Driven Programming | Execution triggered by external events (e.g., user input). | Event Loop, Finite State Machines |
|  | Coroutine/Generator-Based | Suspends/resumes functions for asynchronous flows. | Continuation-Passing Style |
|  | Automata-Based Programming | Behavior expressed as state machines/transition systems. | FSMs, Pushdown Automata |
| **🧬 Metaprogramming** |  | Programs generate/analyze/transform other programs. | Reflective Models, Macros, Syntax Trees |
|  | Compile-Time Metaprogramming | Code generation/optimization at compile time (e.g., C++ templates). | Syntax Tree Rewriting, Type Systems |
|  | Runtime Reflection | Programs inspect/modify their own structure at runtime. | Introspection Models |
|  | Generative Programming | Automatically constructs software from specifications. | DSLs, Code Synthesis |
| **🧠 Symbolic & AI-Oriented** |  | Symbolic representations/manipulations (non-numeric). | Term Rewriting, Knowledge Bases |
|  | Symbolic Programming | Manipulates symbols/expressions as data (e.g., LISP). | Symbolic Algebra, Term Rewriting |
|  | Rule-Based Programming | Uses if-then rules and inference engines (e.g., expert systems). | Production Rule Systems |
| **🔧 Domain-Specific** |  | Tailored to specific domains/problems. | Varies (algebraic, visual, etc.) |
|  | Dataflow Programming | Computation as data flow through operation networks. | Dataflow Networks, Synchronous Dataflow |
|  | Visual Programming | Graphical program composition (e.g., node-link diagrams). | Flowcharts, Visual DSLs |
|  | Hardware Description (HDL) | Models circuits/digital systems (e.g., Verilog). | FSMs, Boolean Algebra |
| **🧪 Experimental/Hybrid** |  | Combines paradigms or explores alternatives. | Multi-model (Turing + Lambda + Actor, etc.) |
|  | Multi-Paradigm | Languages supporting multiple paradigms (e.g., Scala, Rust). | Composite Models |
|  | Aspect-Oriented | Separates cross-cutting concerns (e.g., logging) into "aspects". | Weaving Models, Join Point Models |
|  | Intentional Programming | Programs at the level of intentions/domain concepts. | Conceptual Graphs, DSL Frameworks |

## References

- https://en.wikipedia.org/wiki/Programming_paradigm