---
tags: [language-system]
---

# Evaluation Model


> An **evaluation model** in computer science refers to the strategy or method by which expressions and function arguments are computed and resolved within a programming language or computational system.
> 

## Taxonomy

| **Evaluation Model** | **Description** | **Key Characteristics** | **Example Languages** |
| --- | --- | --- | --- |
| **Eager Evaluation** | Expressions are evaluated as soon as they are encountered, with all sub-expressions evaluated before the expression itself. | Immediate evaluation of expressions and sub-expressions. | Python, Ruby, Java |
| **Lazy Evaluation** | Expressions are not evaluated until their results are needed, evaluating sub-expressions only when required. | Deferred evaluation, potentially improving efficiency. | Haskell, Lisp, OCaml |
| **Normal Order Evaluation** | A type of lazy evaluation where the leftmost, outermost redex is evaluated first, evaluating only the minimum required sub-expressions. | Focuses on evaluating expressions as needed, minimizing evaluation. | Lisp, Scheme |
| **Applicative Order Evaluation** | A type of eager evaluation where all arguments to a function are evaluated before the function is called. | All arguments are fully evaluated before function execution. | C, C++, Java |
| **Call by Name** | A type of lazy evaluation where argument expressions are not evaluated before being passed to a function; instead, they are assessed as needed within the function. | Arguments are passed unevaluated and evaluated only when used. | Algol 60, Scala |
| **Call by Value** | A type of eager evaluation where argument expressions are evaluated before being passed to a function. | Arguments are fully evaluated before passing to functions. | C, C++, Java |
| **Call by Reference** | The argument expression is evaluated before being passed, but a reference to the original memory location is passed rather than a copy, allowing modification of the original value. | Functions can modify the original argument through direct reference. | C++ |
| **Partial Evaluation** | An optimization technique in which expressions are partially evaluated at compile time based on known values, leaving the remaining expressions to be evaluated at runtime. | Improves performance by pre-computing parts of expressions. | Various |
| **Remote Evaluation** | An evaluation strategy where expressions are evaluated on a remote server or node is often used in distributed systems. | Offloads computation to remote systems for better resource utilization. | Distributed systems frameworks |
| **Short-Circuit Evaluation** | An optimization in boolean expressions where evaluation stops as soon as the result is determined, preventing unnecessary computation. | Stops evaluation early based on boolean expression results. | C, C++, Java, Python |

## QA

### How to think deeply about **Eager Evaluation vs Lazy Evaluation?**

> The **universe** writes itself into existence one step at a time, like a computation unfolding. Just as a program is an underlying rule that drives the computation, the laws of nature act as the underlying rules that drive the unfolding of the universe.
> 

> A lazily evaluated universe suggests that **what exists is not precomputed**, but **co-emerges** with the processes that demand it.
> 

> Think of a lazy system as **a world of promises**, not actions. Actions emerge when they're *needed*—not before.
> 

> The **lazy-evaluation worldview** reflects **constructivism**, **minimalism**, and **contingent emergence**, while **eager evaluation** aligns with **realism**, **determinism**, and **absolutism**.
> 

| **Eager** | **Lazy** | **Metaphor / Explanation** |
| --- | --- | --- |
| **Being** | **Becoming** | Ontology: Fixed existence vs unfolding process |
| **Actual** | **Potential** | Reality: Materialized vs possible |
| **Value** | **Latent Value** | Entity: Realized output vs hidden potential |
| **Present** | **Future** | Temporal: Already-real vs not-yet-real |
| **Now** | **Later** | Time semantics: Immediate vs deferred execution |
| **Reified** | **Un-reified** | Epistemology: Concrete concept vs potential concept |
| **Compute** | **Delay** | Execution: Immediate vs suspended |
| **Thunk** | **Promise** | Entity: Deferred recipe vs pledged |
| **Determinate** | **On-demand** | Resolution: Predefined vs reactive |
| **Manifest** | **Latent** | Visibility: Apparent vs hidden |
| **Observation** | **Prophecy** | Knowledge: Seen vs foretold |
| **Materialized** | **Virtualized** | Computation: Instantiated vs suspended |
| **Consumption-led** | **Need-led** | Resource strategy: Pre-consumed vs triggered |
| **Time-independent** | **Time-dependent** | Evaluation: Irrespective vs contextual |
| **Static unfolding** | **Dynamic unfolding** | Structure: Predetermined vs adaptive |
| **Front-loaded** | **Deferred-cost** | Cost model: Upfront vs pay-as-you-go |
| **Synchronous** | **Asynchronous** | Timing: Coordinated vs disjointed |
| **Causal upfront** | **Causal downstream** | Causality: Early determined vs triggered late |
| **Static timelines** | **Branching timelines** | Temporality: Linear vs contingent futures |
| **Exposition** | **Invention** | Discourse: Revealed vs generated |
| **Closed-world assumption** | **Open-world assumption** | Epistemic boundaries: Fixed vs expandable |
| **Resolved** | **Unresolved** | Logical state: Final vs pending |
| **Complete** | **Incomplete** | State: Fully formed vs partial |
| **Fixed** | **Emergent** | Nature: Rigid vs evolving |
| **Explicit** | **Implicit** | Expression: Clear vs implied |
| **Certain** | **Contingent** | Knowledge: Definite vs conditional |
| **Immediate** | **Deferred** | Action: Now vs postponed |
| **Substance** | **Process** | Being vs becoming / static vs dynamic |
| **Realized** | **Untapped** | Outcome: Actualized vs latent potential |
| **Folded** | **Unfolded** | State: Condensed vs expanded |
| **Activated** | **Unactivated** | Status: Engaged vs dormant |
| **Action** | **Plan** | Execution: Doing now vs preparing for later |
| **Value** | **Latent Value** | Entity: Realized output vs hidden potential |
| **Value** | **Reference** | Entity: Direct value vs indirect placeholder |

### How do programming languages convert latent or deferred expressions into concrete values, and what are the terms and mechanisms involved in this process?

| Term(s) | Description |
| --- | --- |
| **Evaluation** | The general process of computing the actual value represented by an expression or latent value. |
| **Forcing** | Specifically, in lazy evaluation, forcing means triggering the computation of a deferred expression (thunk) to produce its realized value. |
| **Normalization** | In lambda calculus and some formal systems, this means reducing an expression to its simplest or normal form (a fully evaluated value). |
| **Realization** | Converting a latent or potential representation into a concrete, materialized value. |
| **Dereferencing** | Sometimes used when the latent value is a reference or pointer to an expression that must be computed to get the underlying value. |
| **Materialization** | The act of realizing a latent or deferred computation into an actual value. |

## References

- [Evaluation Strategy](https://en.wikipedia.org/wiki/Evaluation_strategy)
- Partial Application:
    - [Partial Application](https://www.wikiwand.com/en/Partial_application)
    - [Incremental Computation](https://en.wikipedia.org/wiki/Incremental_computing)
- [Abstraction](note.html?n=technica/computation/system/programming/conceptual-model-programming/abstraction.md)
- https://en.wikipedia.org/wiki/Thunk
- [Contingency](https://app.notion.com/p/Contingency-f873fbcc1be345f5829c98d79b5983b9?pvs=21)
- https://en.wikipedia.org/wiki/Lazy_evaluation
- [**Semantics**](https://app.notion.com/p/Semantics-12e375827ade4a74a4349241b07140c3?pvs=21)