# PHP: 🏷️ Type System

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
| **Time of Checking (Enforcement)** | **Runtime (dynamic)** with optional **compile-time hints** checked at runtime. Errors become `TypeError` or `Fatal error`. |
| **Type Annotation** | Optional — function parameters, return types, class properties. Supports scalar types, union types (`int |
| **Type Inference (Type Deduction) Scope** | Minimal — no global inference. Only local `$x = expr;` type tracking possible by static analyzers (Psalm, PHPStan). Interpreter itself does not infer. |
| **Strength of Conversion Checking** | Weak — implicit conversions common (string ↔ int, bool ↔ int). Type strictness depends on `declare(strict_types=1)`. |
| **Conversion Direction** | Bidirectional but asymmetric: numbers <-> strings, bool <-> numbers/strings, arrays <-> objects (`(object)$arr`). Some unsafe conversions allowed. |
| **Conversion Automaticity** | Automatic (implicit coercions) by default. Can be disabled partially with `strict_types=1`. |
| **Type Compatibility** | Structural & nominal mix. Classes/interfaces use nominal typing, scalars are compatible via coercion rules. |
| **Type Soundness** | Unsound — type declarations enforced only at runtime, and coercions can bypass declared types (esp. without strict mode). |
| **Type Safety** | Partial — runtime enforcement can catch mismatches, but implicit coercions and dynamic features (e.g., `__call`) break safety. |
| **Null Safety** | Not enforced — any variable may hold `null` unless explicitly declared non-null (`Type` vs `?Type`). Still runtime-checked only. |
| **Linear Type** | Not supported. |
| **Affine Type** | Not supported. |
| **Ownership Type** | Not supported. Objects are reference-like but without ownership guarantees. |
| **Uniqueness Type** | Not supported. Multiple aliases to objects allowed. |
| **Session Type** | Not supported. |
| **Mutability** | Full mutability by default. No language-level immutability (workarounds with `readonly` properties in PHP 8.1+). |
| **Type Variance** | Declared: covariance for return types, contravariance for parameters. Introduced in PHP 7.4+. |
| **Effect System** | None. Side effects are unchecked. |
| **Type Reflection** | Supported. Reflection API can inspect types, properties, methods, attributes. |
| **Refinement Type** | Not natively. Enforced only via assertions or external analyzers. |
| **Context Sensitivity** | High — type interpretation depends on `strict_types` directive, runtime environment, and operator overloading (`__toString`, `__call`, etc.). |

## Type Guarantee

- Type Safety
- Null Safety
- Soundness
- Completeness
- **Correctness**

## Type Declaration

> Which are the mechanisms to define new types?
> 

| Kind | **Type** | **Description** |
| --- | --- | --- |
| **Class** | `class ClassName { ... }` | Defines a user-defined type representing objects with properties and methods. |
| **Interface** | `interface InterfaceName { ... }` | Defines a contract for classes; specifies methods without implementation. |
| **Trait** | `trait TraitName { ... }` | Defines a reusable set of methods/properties that can be included in classes. |
| **Enum** | `enum EnumName { ... }` | Defines a finite set of named values (PHP 8.1+). Can be backed by scalar types. |
| **Type Alias / `class` alias** | `class_alias('Original', 'Alias')` | Creates an alternative name for an existing class type. |
| **Function Type** | `callable` | Any valid callback; can be constrained in parameters or properties. |
| **Union Type** | `Type1 | Type2` |
| **Intersection Type** | `TypeA&TypeB` | Variable must satisfy all listed types simultaneously (PHP 8.1+). |
| **Nullable Type** | `?Type` | Type or `null`; allows optional null assignment. |

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

## Type References

> **Rferences:** PHP supports references for variables and objects. Unlike Java, PHP only has **strong references** by default and **weak references** (PHP 7.4+) for objects.
> 

| **Reference Type** | **Description** | **Garbage Collection Behavior** | **Creation** |
| --- | --- | --- | --- |
| **Strong Reference** | Default type of reference. Variables or objects holding a strong reference prevent the value from being garbage collected. | Object/variable is not freed until all strong references are gone. | `php $obj = new stdClass();` |
| **Weak Reference** | Allows referencing an object **without preventing its garbage collection**. Useful for caches or cyclic structures. | Cleared automatically when no strong references remain. | `php $obj = new stdClass(); $weak = WeakReference::create($obj);` |

## References

- [Type system](https://doc.rust-lang.org/reference/type-system.html#type-system)
- [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md)
- …