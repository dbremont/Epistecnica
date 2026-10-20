# Rust: 🏷️ Type System

> A **"Type System"** in programming defines the rules and structures for classifying and managing data types, ensuring that operations on data are performed in a consistent and safe manner.
> 

Guiding Questions:

- Is the type system static (checked at compile-time) or dynamic (checked at runtime)?
- Does it support type inference (e.g., let x = 10 instead of let x: int = 10)?
- Is the type system static (checked at compile-time) or dynamic (checked at runtime)?
- Is it strongly typed (strict rules, no implicit conversions) or weakly typed (flexible, allows implicit conversions)?
- Is subtyping nominal (Java), structural (TypeScript), or a mix (Rust traits)?
- Type Annotations & Declarations
    - How are types explicitly declared? (e.g., variable: Type in Python/TypeScript)
    - Does the language allow type aliases or typedefs? (e.g., type Age = number in TypeScript)
    - Are there generic types (parameterized types)? (e.g., List<T> in Java, Rust)
- Type Checking & Safety
    - Does the language perform type coercion (automatic type conversion)? (e.g., JavaScript's "5" + 2 = "52")
    - How does it handle type errors? (Compile-time errors? Runtime exceptions?)
    - Does it support gradual typing (mixing static and dynamic types)? (e.g., Python with mypy)
- Advanced Typing Features
    - Does the language support union types (A | B) or intersection types (A & B)?
    - Are there sum types (enums with data) or product types (tuples/structs)? (e.g., Rust’s enum, Haskell’s data)
    - Does it have dependent types (types depend on runtime values)? (e.g., Idris)
    - Are higher-kinded types supported? (e.g., Functor in Haskell)
- Polymorphism
    - Does the language support parametric polymorphism (generics)? (e.g., List<T>)
    - Does it have ad-hoc polymorphism (function overloading, traits)? (e.g., Rust traits, Haskell typeclasses)
    - Is subtype polymorphism (inheritance) supported? (e.g., Java classes, Kotlin sealed classes)
- Type System Soundness & Expressiveness
    - Is the type system sound (no false negatives in type checking)?
    - Can types represent complex invariants? (e.g., "non-empty list", "positive integer")
    - Does it allow type casting (explicit or implicit)? (e.g., as in Rust, static_cast in C++)
- Runtime Behavior & Erasure
    - Are types erased at runtime (e.g., Java generics) or reified (kept at runtime, e.g., C#)?
    - Does the language support reflection (inspecting types at runtime)? (e.g., Python’s type(), Java’s Class<?>)
- Quirks
    - Are there surprising behaviors? (e.g., TypeScript’s any, Go’s empty interface interface{})
- Type Representation:
    - How types are represented in runtime?

## Characterization

| Dimension | Value |
| --- | --- |
| Time of Checking (Enforcement) |  |
| Type Annotation |  |
| Type Inference (Type Deduction) Scope |  |
| Strength of Conversion Checking |  |
| Conversion Direction |  |
| Conversion Automaticity |  |
| Type Compatibility  |  |
| Type Soundness |  |
| Type Safety |  |
| Null Safety |  |
| Linear Type |  |
| Affine Type |  |
| Ownership Type |  |
| Uniqueness Type |  |
| Session Type |  |
| Mutability |  |
| Type Variance |  |
| Effect System |  |
| Type Reflection |  |
| Refinement Type |  |
| Context Sensitivity |  |

## Type Guarantee

- Type Safety
- Null Safety
- Soundness
- Completeness
- **Correctness**

## Type Declaration

> 

| Kind | **Type** | **Description** |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

## Type Conversion

> **Type coercions** are implicit operations that change the type of a value. They happen automatically at specific locations and are highly restricted in what types actually coerce.
> 

## Type Inference

> 

## Type Compatibility

> 

## Type Equivalence

> 

## Polymorphism

> 

## Sub Typing

> 

## Type Variance

> 

## Error Handling

> 

## Pattern Matching

> 

## Type Soundness

> 

## **Ownership System**

> The **Rust** ownership model is a **cross-cutting semantic feature** of the language that extends beyond the type system into memory management, resource lifetime, aliasing discipline, and execution semantics.
> 

> Rust’s ownership system is a **statically enforced resource ownership, borrowing, and aliasing discipline** that governs value lifetime, destruction, and access permissions. It is realized through move semantics, references, borrowing, lifetimes, and destructor semantics; implemented via compiler analyses such as move tracking, borrow checking, region inference, and MIR dataflow; and provides compile-time guarantees of memory safety and race freedom while remaining conservative and selectively escapable through runtime-checked abstractions and `unsafe` code.
> 
- How should the Rust ownership system be classified as a language feature?
- Which linguistic constructs realize the ownership system, and how are they used?
- How is the ownership system implemented? What mechanisms and techniques does the compiler use to enforce it?
- What is the scope of the ownership system? What guarantees does it provide, and what are its limitations?
- Which are the similar ideas in other languages?

## Macro System

> 

## References

- [Type system](https://doc.rust-lang.org/reference/type-system.html#type-system)
- [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md)
- [Type system](https://doc.rust-lang.org/reference/type-system.html#type-system)
- [Special types and traits](https://doc.rust-lang.org/reference/special-types-and-traits.html)
- [Rust's Type System Is Turing-Complete: Type-Level Programming in Rust](https://news.ycombinator.com/item?id=13843288) ([sdleffler.github.io](http://sdleffler.github.io/))
- [Untapped potential in Rust's type system](https://news.ycombinator.com/item?id=27490596) ([jakobmeier.ch](http://jakobmeier.ch/))
- [Bjarne Stroustrup Weighs in on Distributed Systems, Type Safety and Rust](https://news.ycombinator.com/item?id=24036827) ([thenewstack.io](http://thenewstack.io/))
- [Fighting Rust's Expressive Type System](https://news.ycombinator.com/item?id=24867610) ([thefuntastic.com](http://thefuntastic.com/))
- [The usability of advanced type systems: Rust as a case study](https://news.ycombinator.com/item?id=34890787) ([arxiv.org](http://arxiv.org/))
- Will Crichton. 2020. The Usability of Ownership. arXiv preprint arXiv:2011.06171 (2020).
- Will Crichton, Marco Patrignani, Maneesh Agrawala, and Pat Hanrahan. 2021. Modular Information Flow Through Ownership. CoRR abs/2111.13662 (2021). arXiv:2111.13662 [https://arxiv.org/abs/2111.13662](https://arxiv.org/abs/2111.13662)
- [Special types and traits](https://doc.rust-lang.org/reference/special-types-and-traits.html)
- [Common Collections](https://doc.rust-lang.org/book/ch08-00-common-collections.html)
- [Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- - [Appendix C: [Derivable Traits]](https://doc.rust-lang.org/book/appendix-03-derivable-traits.html)
- [Resource Lifetime](note.html?n=technica/computation/language-system/conceptual-model-language-system/resource-lifetime.md)
- [Resource Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/resource-management.md)