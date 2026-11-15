---
tags: [note, como]
---

# What is the role of documentation in program comprehension? Can the meaning of a program be derived solely from its code? Similarly, can the meaning of a mathematical model be fully understood only from its symbolic representation?


> What is the role of documentation in program comprehension? Can the meaning of a program be derived solely from its code? Similarly, can the meaning of a mathematical model be fully understood only from its symbolic representation?
> 

> The role of documentation in **program comprehension** is analogous to the role of **explanatory text, definitions, and contextual framing** in understanding a **mathematical model**. While both code and symbolic expressions may be *formally complete*, their *pragmatic meaning*—how they relate to human intentions, domain concepts, or real-world phenomena—is often opaque without documentation.
> 

## Index

## Theoretical Anchors

> How to think deeply about the questions in this note?
> 
- **Peirce’s Semiotic Triad** *(1930s)* — A foundational model of meaning based on the triadic relation between **sign**, **object**, and **interpretant**, emphasizing the mediated and interpretive nature of symbols.
- **Wittgenstein’s Language Games** *(1953)* — Language derives its meaning from use within specific **social and practical contexts**; understanding is tied to participation in a rule-governed activity.
- **The Symbol Grounding Problem** *(Harnad, 1990)* — Challenges how **symbols acquire intrinsic meaning**, arguing that syntactic manipulation alone is insufficient without some grounding in perception or action.
- **Underdetermination of Theory by Data** *(Quine, 1960)* — A single dataset can support **multiple, equally valid models or theories**. "A thousand models can fit the same data": empirical adequacy does not uniquely determine theoretical truth.
- **Models of Program Comprehension** *(e.g., Top-Down / Bottom-Up, von Mayrhauser & Vans, 1995)* — Describes how programmers mentally construct meaning from code, either through **strategic goal-driven inference** or **local structural exploration**.

## Mathematical Model vs a Program

| Aspect | Program Code | Mathematical Model |
| --- | --- | --- |
| Core Representation | Source Code | Symbolic Expression (e.g., equations) |
| Formal Semantics | Language semantics + execution model | Mathematical rules & logic |
| Fully self-descriptive? | No (not for humans) | No (not for humans) |
| Requires context? | Yes (domain, intent, architecture) | Yes (variables, assumptions, mapping) |
| Documentation needed for… | Intent, behavior, edge cases, usage | Physical interpretation, assumptions |
| Pure formal analysis yields | Behavior (trace, output) | Internal consistency, structure |

## 1. **Can the meaning of a program be derived solely from its code?**

> **In principle:** Yes, from a *formal/computational standpoint*, the code fully specifies the behavior of a program. Given complete code and its execution environment, one can simulate or analyze the program's behavior.
> 

**In practice:** Rarely. Deriving meaning *solely from code* assumes: Perfect knowledge of the programming language semantics.

- Complete knowledge of external dependencies, APIs, and protocols.
- No ambiguity in variable naming, data structures, or logic flow.
- No need to understand the *why* (design decisions, goals, constraints).

Documentation bridges this gap:

- Explains the **intent** behind the code.
- Describes **architectural decisions**.
- Provides **examples**, **constraints**, **invariants**, and **use cases**.
- Reduces cognitive load and interpretive ambiguity.

## 2. **Can the meaning of a mathematical model be fully understood from its symbolic representation alone?**

**Formally:** The symbolic representation (e.g. equations) defines the mathematical structure and its internal relationships.

**But practically and semantically:** No. Mathematical symbols are **declarative**, but:

- Symbols are **arbitrary** (e.g., `x` could be position, time, voltage, etc.).
- Models often require **assumptions** and **interpretations** (e.g., boundary conditions, domain-specific meaning).
- Context gives **meaning**—e.g., what system is being modeled? Why this form?

Without documentation (text, diagrams, assumptions, verbal reasoning), even experts may misinterpret a symbolic model.

## Model vs Understanding (Model Itself and The Object Being Represented)

> A model is a representation of a system, but not the system itself. Can we, by inspecting the model alone, determine what it represents? In programming, source code models both the problem domain and the chosen implementation strategies. These implementation details often obscure the essence of what is being modeled.
> 

> Understanding a model requires more than just reading it—it involves running it, observing its behavior, and constructing layered mental representations that allow one to navigate different levels of abstraction. These layers help answer different types of questions, from what it does to why it does it.
> 

> A **program** may still serve as a model of a system even when its internal components and structure do not correspond directly to those of the target system—for instance, when identifiers are obfuscated or renamed.
> 

## Summary

- Code and symbolic models are **formally complete** but **semantically underdetermined**.
- Documentation plays a **semantic scaffolding role**, grounding formal representations in human meaning.
- Understanding involves more than parsing syntax—it requires interpretation, context, and purpose.

## References

- Suppes, Patrick. "Models of data." *Studies in logic and the foundations of mathematics*. Vol. 44. Elsevier, 1966. 252-261.
- Morgan, Mary S., and Margaret Morrison, eds. Models as mediators: Perspectives on natural and social science. No. 52. Cambridge University Press, 1999.
- [‣](https://app.notion.com/p/10e598edb790818fafefc1104e6abf28?pvs=21)
- Storey, Margaret-Anne. "Theories, tools and research methods in program comprehension: past, present and future." Software Quality Journal 14 (2006): 187-208.
-
