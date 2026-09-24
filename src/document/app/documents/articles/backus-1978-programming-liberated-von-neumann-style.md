---
tags: [physical]
---

# Backus, J. (1978). Can programming be liberated from the von Neumann style? A functional style and its algebra of programs. Communications of the ACM, 21(8), 613–641.


```bash
@article{backus1978can,
  title={Can programming be liberated from the von Neumann style? A functional style and its algebra of programs},
  author={Backus, John},
  journal={Communications of the ACM},
  volume={21},
  number={8},
  pages={613--641},
  year={1978},
  publisher={ACM New York, NY, USA}
	}
```

## Notes

## Summary

> Associated with the **functional style of programming** is **an** **algebra of programs** whose variables range over **programs** and whose operations are **combining forms**.
> 

> Associated with the **functional programming style** is **an  algebra** where **variables** **represent** **programs** and **operations** are **combining form (**combines programs**)**.
> 

> $\text{Let } \mathcal{A} \text{ be an algebra associated with the functional programming style, where } \\
\text{variables } p \in P \text{ represent programs and operations } \oplus, \otimes, \ldots \text{ are combining forms.}$
> 

> A **functional programming language** is one that offers a **programming algebra**, consisting of a set of functional forms and primitive programs.
> 

> **Dense formalism descriptions(higher level / up scale)** refer to compact, highly detailed explanations that utilize specific and often technical language to convey complex information efficiently.
> 

> **Many creative computer scientists** have retreated from **inventing languages** to **inventing tools for describ-ing them**.
> 

> GOALS:  1)  Suggest that basic **defects in the framework of conventional languages(von newman)** make their **expressive weakness** and their **cancerous growth** **inevitable**; 2) to suggest some **alternate avenues** of **exploration** toward the design of new kinds of languages.
> 

| State Transition Semantics | Coupling |
| --- | --- |
| Functional Style | Loose |
| Von Neumann Style | Coupled |

### Models of Computing Systems

…

### Von Neumann Computers

…

### Von Neumann Languages

…

### Comparison of von Neumann and Functional Programs

…

### Language Frameworks versus Changeable Parts

…

### Changeable Parts and Combining Forms

…

### APL versus Word-at-a-Time Programming

…

### Von Neumann Languages Lack Useful Mathematical Properties

…

### What Are the Alternatives to von Neumann Languages?

…

### Functional Programming Systems (FP Systems)

…

### The Algebra of Programs for FP Systems

…

### Formal Systems for Functional Programming (FFP Systems)

…

### Applicative State Transition Systems (AST Systems)

…

### Remarks About Computer Design

…

## QA

### How Monads Solved the Time Problem in Functional Programming?

> The **problem of time** in programming usually refers to how programs handle ***state changes***, *side effects*, and *sequencing of operations* over time — especially in the context of *functional programming*, where immutability and pure functions are emphasized.
> 

> Monads provided an elegant  solution to the problem of modeling time-dependent computations (like  state, I/O, and side effects) in purely functional programming 
languages.
> 

The Core Problem

In purely functional programming:

- Functions must be pure (same input → same output)
- No implicit state or side effects are allowed
- Yet real programs need to handle time-dependent operations (I/O, state changes, etc.)\

How Monads Helped

1. **Sequencing Computations**: Monads allow ordering of operations while maintaining purity by explicitly representing the sequence in the type system.
2. **Separating Evaluation from Execution**: They let you build descriptions of effectful computations that can be executed later.
3. **Maintaining Referential Transparency**: Side effects are wrapped in monadic values, keeping functions pure.

How CoMonad Helped

1. Comonads *can* represent time-dependent processes, especially when you want to model computations that depend on surrounding context or neighborhood in time.

**Modeling Time Explicitly with Values**

- Instead of changing state over time, functional programs represent "state at different times" as **different immutable values**.
- For example, rather than updating a variable, you create a new version of the state representing the next moment in time.
- This approach is sometimes called **persistent data structures**, where you keep old versions intact.

### Summary

…

## References

- Backus, J. (1978). Can programming be liberated from the von Neumann style? *Communications of the ACM*, *21*(8), 613–641. https://doi.org/10.1145/359576.359579
- [Von Neumann Programming Languages](https://en.wikipedia.org/wiki/Von_Neumann_programming_languages)
- [Homoiconicity](https://en.wikipedia.org/wiki/Homoiconicity)
- [Dana Scott](https://en.wikipedia.org/wiki/Dana_Scott)
- https://news.ycombinator.com/item?id=27554355
