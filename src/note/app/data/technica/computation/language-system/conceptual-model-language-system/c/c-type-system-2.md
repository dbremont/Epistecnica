# C++: 🏷️ Type System

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
| Time of Checking (Enforcement) | **Primarily static (compile-time)**, with limited dynamic checking via RTTI (`dynamic_cast`, `typeid`) and library/runtime assertions |
| Type Annotation | **Explicit + partial inference** |
| Type Inference (Type Deduction) Scope | **Local and expression-scoped** (`auto`, `decltype`, template argument deduction, CTAD); not whole-program inference |
| Strength of Conversion Checking | **Moderate / permissive** |
| Conversion Direction | **Implicit and explicit**, both widening and narrowing (narrowing more restricted under brace initialization) |
| Conversion Automaticity | **Partially automatic** — many standard conversions happen implicitly; user-defined conversions can also participate |
| Type Compatibility | **Nominal**, with some structural behavior in templates / duck-typed instantiation |
| Type Soundness | **Not sound** |
| Type Safety | **Partially type-safe** |
| Null Safety | **Unsafe by default** (`nullptr` typed, but dereference not checked) |
| Linear Type | **No** |
| Affine Type | **Partial / idiomatic only** (`std::unique_ptr` approximates affine ownership) |
| Ownership Type | **Library-level / idiomatic**, not built into the type system core |
| Uniqueness Type | **Partial**, via move semantics and `std::unique_ptr` |
| Session Type | **No** |
| Mutability | **Mutable by default**; `const` provides immutability constraints |
| Type Variance | **Mostly invariant** |
| Effect System | **No built-in effect system** |
| Type Reflection | **Limited runtime reflection** (`RTTI`); no full static reflection standardized yet |
| Refinement Type | **No** |
| Context Sensitivity | **High** — overload resolution, template specialization, value category (`lvalue`/`rvalue`), cv-qualification, lookup context |

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
| **Class Type** | `class` | Declares a new nominal user-defined type with encapsulation, methods, constructors, inheritance, etc. |
| **Structure Type** | `struct` | Declares a new nominal record type; semantically similar to `class`, differing mainly in default visibility. |
| **Union Type** | `union` | Declares a new type whose members overlap in storage. |
| **Enumeration Type** | `enum` | Declares a new enumeration type with named constants. |
| **Scoped Enumeration Type** | `enum class` | Declares a strongly scoped enumeration type distinct from integers. |
| **Template-Instantiated Type** | class template specialization | Each specialization (`std::vector<int>`, `std::vector<double>`) forms a distinct type. |
| **Closure Type** | lambda expression | Every lambda introduces a unique unnamed compiler-generated type. |
| **Array Type** | `T[N]` | Creates fixed-size array types from another type. |
| **Pointer Type** | `T*` | Constructs pointer types over another type. |
| **Reference Type** | `T&`, `T&&` | Constructs lvalue and rvalue reference types. |
| **Function Type** | `R(Args...)` | Defines callable/function signature types. |
| **Qualified Type** | `const`, `volatile` | Produces cv-qualified variants of a type. |
| **Dependent Type Constructor** | template instantiation | Produces specialized types like `std::vector<int>`. |

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
- …