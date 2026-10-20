# Erlang: 🏷️ Type System

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

> Which are the mechanisms to **create new types?**
> 

| **Kind** | **Mechanism** | **Description** |
| --- | --- | --- |
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

## References

- [Type system](https://doc.rust-lang.org/reference/type-system.html#type-system)
- [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md)
- [Resource Lifetime](note.html?n=technica/computation/language-system/conceptual-model-language-system/resource-lifetime.md)
- [Resource Management](note.html?n=technica/computation/language-system/conceptual-model-language-system/resource-management.md)