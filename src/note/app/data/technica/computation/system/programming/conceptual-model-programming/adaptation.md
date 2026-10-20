---
tags: [technique]
---

# Adaptation

- [System Change](note.html?n=technica/computation/system/programming/conceptual-model-programming/system-change.md)

> aka Late Bound Structure
> 

> A **meta-pattern** where a **general computational or data structure** is defined with **intentionally incomplete (partial)  (**un-reifined**) parts**, allowing users to **extend or adapt (reified)**  it by providing concrete implementations. This generates a **finalized, executable (reified) structure** tailored to specific needs.
> 

> Partial Definition: The core structure is **partially abstract**, with "gaps" (hooks, placeholders, or abstract methods) that must be filled.
> 

> Reification: The adapted structure becomes fully computable after refinement.
> 

> Note: This is an extremely powerful general concept, alongside:;  along side with Compositionality, Reflection**,**  Lazy Evaluation (On-Demand Computation),  Constraint Propagation (Declarative Systems),  Interpretation,  Decomposition , Abstraction, Polymorphism,  Concurrency, Reactivity,   etc.
> 

> See more in
> 

Types:

- Basic Adaptation : Parameters / Declarative
- Behavior, …

Uses:

- Template Method,
- Strategy,
- Factory Method,
- Abstract Factory,
- Partial Evaluation,
- Decorator**,**
- Dependency Injection / Late Binding
- Hooking

| Term | Meaning |
| --- | --- |
| **Placeholder** | A location awaiting a concrete value or implementation. |
| **Hole** | A missing expression, statement, type, or function body. Common in program synthesis and language theory. |
| **Stub** | A temporary implementation to be completed later. |
| **Template Parameter** | A designated variable part of a template. |
| **Extension Point** | A location designed for future customization. |
| **Abstract Method** | A required implementation left unspecified. |
| **Partial Program** | A program containing unresolved components. |
| **Program Sketch** | A program with holes that must be synthesized or completed. |

Uses:

- Adapter Pattern.

## Hooking

> Hooking: Dynamic Adaptation of Control Flow. In computer programming, “hooking” refers to the process of intercepting and modifying the behavior of an application or system component.
> 
> 
> Specifically, it involves inserting a piece of code (called a “hook”) into the application’s execution path to monitor or modify its behavior in some way. This can be useful for a variety of purposes, such as debugging, performance analysis, or security testing.
> 
> Hooking can be done at different levels of the software stack, from low-level system functions to high-level application APIs. Some common types of hooking include function hooking, message hooking, and API hooking.
> 
> A system may be designed with a hooking mechanism or extension points.
> 
> However, it is important to note that hooking can be used for malicious purposes as well, such as intercepting sensitive data or performing unauthorized actions. Therefore, it is a technique that must be used carefully and responsibly.
> 

## Callback

> A “callback” is a mechanism that allows a piece of code to specify a function to be called by another piece of code. It is a way to pass behavior as a parameter, which can be useful for implementing event-driven programming, asynchronous programming, and other programming patterns.
> 

> While a callback can be used to hook into the behavior of another piece of code, it is not necessarily the same thing as a “hooking mechanism”. Hooking is a technique used in computer programming to intercept and modify the behavior of software components at runtime. Hooking involves inserting additional code into an application’s runtime environment to intercept and modify the normal flow of execution.
> 

> Callbacks can be used as part of a hooking mechanism to intercept and modify the behavior of a software component, but they are not the same thing. Callbacks are a general mechanism for passing behavior as a parameter, while hooking is a specific technique for intercepting and modifying the behavior of software components at runtime.
>