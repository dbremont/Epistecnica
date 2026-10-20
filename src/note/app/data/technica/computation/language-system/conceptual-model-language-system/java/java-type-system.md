# Java: 🏷️ Type System

> A **"Type System"** in programming defines the rules and structures for classifying and managing data types, ensuring that operations on data are performed in a consistent and safe manner.
> 

> The **Java type system** is a strong, statically-typed system that enforces strict type checking at compile time to ensure type safety and prevent type-related errors by categorizing data into primitive types, reference types, and various class hierarchies.
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
- Miscellanea
    - (Java) What is a reifiable type?
    - (Java) What is the size of char in bytes?
    - (Java) What is the size of short in bytes?
    - (Java) What is the size of int in bytes?
    - (Java) What is the size of float in bytes?
    - (Java) What is the size of double in bytes?
    - (Java) How big is an Object?
    - (Java) Why is there no sizeof?
    - (Java) What are anonymous inner classes?
    - (Java) What is the package?
    - (Java) What is an Interface?

## Characterization

| **Dimension** | **Value (Java)** |
| --- | --- |
| **Time of Checking (Enforcement)** | Compile-time (Static Typing) with some runtime checks (e.g., casts, reflection). |
| **Type Annotation** | Required in most cases; introduced optional annotations with Java 8+ (`@NonNull`, `@Nullable`, etc.). |
| **Type Inference (Type Deduction) Scope** | Limited local inference (`var` in Java 10+); no global type inference or function return inference. |
| **Strength of Conversion Checking** | Strong — disallows unsafe conversions without explicit casting. |
| **Conversion Direction** | Widening (safe) is automatic; narrowing (unsafe) requires explicit cast. |
| **Conversion Automaticity** | Automatic for widening (e.g., `int → long`); explicit for narrowing (e.g., `long → int`). |
| **Type Compatibility** | Nominal typing — compatibility based on declared type names. |
| **Type Soundness** | Mostly sound but **not fully** due to type erasure in generics and some corner cases (e.g., `raw types`, arrays). |
| **Type Safety** | Strong but weakened by unsafe casts, reflection, raw types, and array covariance. |
| **Null Safety** | Unsafe by default; nulls allowed everywhere unless using tools or annotations (`@NonNull`) + external enforcement (e.g., Checker Framework). |
| **Linear Type** | Not supported. |
| **Affine Type** | Not supported. |
| **Ownership Type** | Not natively supported; can be approximated via discipline or frameworks (e.g., Capabilities/Checker Frameworks). |
| **Uniqueness Type** | Not supported. |
| **Session Type** | Not supported in the type system; only via protocol libraries or external DSLs. |
| **Mutability** | Mutable by default; no native immutability enforcement, but `final` and custom practices are common. |
| **Type Variance** | Partial — supports variance annotations in generics (`? extends`, `? super`), but less expressive than Scala/Kotlin. |
| **Effect System** | Not supported in base language; some annotation-based tools exist (e.g., Checker Framework). |
| **Type Reflection** | Supported via runtime reflection (`Class<T>`, `java.lang.reflect`). |
| **Refinement Type** | Not natively supported; partially emulable via annotations + external tools (e.g., Liquid Java, Checker Framework). |
| **Context Sensitivity** | Very limited — context-insensitive; no dependent types or higher-rank types. |
| Type Erasure | Java performs type erasure for generics, removing generic type information at runtime, and replacing it with raw types. |
| Type Casting | Java allows explicit casting between compatible types, and performs implicit casting (widening) for primitive types. |

## Type Guarantee

- Type Safety
- Null Safety
- Soundness
- Completeness
- **Correctness**

## Type Declaration

> Java supports several kinds of type declarations to model structured, reusable, and encapsulated data and behavior. These include classes, interfaces, enums, records, arrays, type parameters, and primitive types. Below is a classification of these types.
> 

| **Kind** | **Type** | **Description** |
| --- | --- | --- |
| **Reference** | `class` | Defines a blueprint for objects with fields and methods. Can be extended (single inheritance) and can implement interfaces. |
|  | `interface` | A contract with method signatures and default/static methods. Supports multiple inheritance via interfaces. |
|  | `enum` | A special kind of class that defines a fixed set of constants. Can include fields, methods, and constructors. |
|  | `record` | A concise, immutable data class introduced in Java 14+. Automatically generates constructor, accessors, `equals`, `hashCode`, and `toString`. |
|  | `array` | A fixed-size, indexed collection of elements of the same type. Syntax: `int[]`, `String[]`, etc. |
|  | `var` (local type inference) | Used for local variables where the type can be inferred by the compiler (Java 10+). Cannot be used for fields or parameters. |
| **Generic** | `T`, `E`, `K`, `V`, etc. | Type parameters used in generics. Provide type safety for parameterized classes and methods. |
| **Primitive** | `int`, `long`, `float`, `double`, `char`, `boolean`, `byte`, `short` | Built-in value types not derived from `Object`. Each has a corresponding wrapper class (`Integer`, `Double`, etc.). |
| **Special** | `void` | Used to declare that a method does not return a value. Not a type for variables. |
|  | `varargs` (`T...`) | A syntactic sugar for arrays in method parameters, allowing variable-length arguments. |

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

> **References:** Java has four types of references, determining how the garbage collector treats objects no longer referenced by any live threads in the application.
> 

| **Reference Type** | **Description** | **Garbage Collection Behavior** | **Creation** |
| --- | --- | --- | --- |
| **Strong Reference** | The default type of reference. Objects with at least one firm reference are considered live, not garbage collected. | Not cleared by the garbage collector as long as the firm reference exists. | `Object obj = new Object();` |
| **Soft Reference** | Used to hold onto objects that are not strictly necessary but might be helpful to if memory is available. | Cleared if JVM determines insufficient memory; useful for caches. | `new SoftReference<>(object);` (java.lang.ref.SoftReference) |
| **Weak Reference** | Useful for data structures that should automatically remove objects no longer in use. | Cleared as soon as no strong references remain. | `new WeakReference<>(object);` (java.lang.ref.WeakReference) |
| **Phantom Reference** | Used to track the finalization of objects, allowing cleanup of resources when the object is no longer reachable. | Enqueued on a reference queue after the object is finalized. | `new PhantomReference<>(object, queue);` (java.lang.ref.PhantomReference) |

## QA

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
- What is the value of `new BigDecimal(0.1)`?

## References

- [Type system](https://doc.rust-lang.org/reference/type-system.html#type-system)
- [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md)
- [Taming Wildcards in Java’s Type System](https://www.cs.cornell.edu/~ross/publications/tamewild/tamewild-tate-pldi11.pdf)
- [The Java type system is broken](https://wouter.coekaerts.be/2018/java-type-system-broken)
- [Generics in Java](https://en.wikipedia.org/wiki/Generics_in_Java)
- [How to set constraints on generic types in Java?](https://stackoverflow.com/questions/2081663/how-to-set-constraints-on-generic-types-in-java)
- [Java Generics are Turing Complete](https://arxiv.org/pdf/1605.05274.pdf)
- [Java Type System Interview Questions](https://www.baeldung.com/java-type-system-interview-questions)
- [An Abstract State Machine Model for the Generic Java Type System](http://pages.di.unipi.it/boerger/Papers/Java-JVM/JavaBraunschweigTR-2010-02.pdf)
- [Java is not type-safe](https://www.cis.upenn.edu/~bcpierce/courses/629/papers/Saraswat-javabug.html)
- [A Formal Type System for Java](https://www.jot.fm/issues/issue_2007_09/article3.pdf)
- [Java Generics are Turing Complete](https://arxiv.org/pdf/1605.05274.pdf)
- [Initial Values of Variables](https://docs.oracle.com/javase/specs/jls/se7/html/jls-4.html)
- [Java is Unsound: The Industry Perspective](https://dev.to/rosstate/java-is-unsound-the-industry-perspective)
- [Java Generics are Turing Complete](https://arxiv.org/pdf/1605.05274.pdf)
- [Java and scala’s type systems are unsound: the existential crisis of null pointers](https://dl.acm.org/doi/10.1145/2983990.2984004)
- [When to use parallel streams](https://gee.cs.oswego.edu/dl/html/StreamParallelGuidance.html)
- [What is the concept of erasure in Java generics?](https://stackoverflow.com/questions/313584/what-is-the-concept-of-erasure-in-generics-in-java)
- Syntactical Structure - Literal Values