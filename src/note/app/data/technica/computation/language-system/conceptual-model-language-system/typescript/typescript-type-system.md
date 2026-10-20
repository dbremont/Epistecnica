# Typescript: Type System

> The Rust programming language type system is **statically typed**, enforcing memory and **type safety** through strict compile-time checks, including ownership, lifetimes, and borrowing rules, which eliminate common bugs like null pointer dereferencing and data races.
> 

> **Rust** has a robust, static type system that helps prevent common programming errors and provides compile-time guarantees about the correctness of programs.
> 

**Rust's Type System**

| Feature | Description | How Rust Implements It |
| --- | --- | --- |
| Static/Dynamic Typing | Types are checked at compile time, ensuring type safety and catching errors before runtime. | Rust's type system is statically typed, meaning type checking is done at compile time. This helps prevent many common bugs and ensures memory safety without runtime overhead. |
| Strong/Weak Typing | Type conversions are restricted, and implicit type conversions are limited, ensuring type integrity and preventing unintended behavior. | Rust has a robust type system that prevents implicit type conversions and promotes explicit conversions instead. This enhances code clarity and reduces the likelihood of runtime errors. |
| Type Inference | The ability of the type system to automatically deduce the type of an expression or variable based on its usage without explicit type annotations. | Rust extensively employs type inference, allowing developers to omit type annotations in many cases while ensuring type safety. This reduces boilerplate and improves code readability. |
| Parametric Polymorphism | The ability to write functions and data structures that can operate on various data types without sacrificing type safety. | Rust supports parametric polymorphism through its generics system, allowing developers to write reusable code that operates on different types while maintaining compile-time type safety. |
| ADTs (Algebraic Data Types) | Composite data types are combinations of more straightforward types, typically sum types (enums) and product types (structs), enabling concise and expressive data modeling. | Rust supports algebraic data types through enums and structs, allowing developers to represent complex data structures in a type-safe manner. This facilitates pattern matching and exhaustive handling. |
| Pattern Matching | A control structure that allows matching values against patterns and executing code based on the match, commonly used with ADTs. | Rust provides powerful pattern-matching capabilities that enable concise and expressive code. This makes it easier to handle different cases and ensures exhaustiveness checking at compile time. |
| Type Safety | The guarantee that operations performed on data will respect the data's type, preventing type errors and ensuring program correctness. | Rust's type system ensures type safety by enforcing strict rules during compilation, preventing common programming errors such as null pointer dereferencing, buffer overflows, and data races. |
| Nominal/Structural | Describes how type compatibility is determined; nominal typing relies on explicit type declarations, while structural typing considers the structure of types. | Rust implements a primarily **nominal type system**, where explicit type declarations primarily determine **compatibility** and **type relationships**. Still, it also incorporates aspects of structural typing through traits, allowing for ad-hoc polymorphism and compatibility based on shared behavior rather than explicit type hierarchy. |
| Borrow Checking | Ensuring memory safety and preventing data races by enforcing strict rules on borrowing and ownership of data, eliminating common pitfalls like use-after-free errors. | Rust's borrow checker analyzes the ownership and borrowing of data at compile time, ensuring that references to data remain valid and preventing multiple mutable references, thus eliminating many common memory safety bugs. |
| Subtyping | Describes relationships between types, where a subtype is a more specific version of a supertype. | Rust implements subtyping through trait bounds, where a type T can be considered a subtype of another type U if T implements all the traits required by U. |
| Generics / Parameterized types | The ability to define traits (interfaces) that types can implement allows generic code to be written regarding traits, promoting code reuse and flexibility. | Rust's trait system allows developers to define traits that types can implement, enabling polymorphism and generic programming. This promotes code reuse and ensures compile-time safety through trait bounds. |
| Mutability Control | Fine-grained control over mutability allows mutable and immutable references to coexist safely, prevents data races, and enables concurrency. | Rust's mutability control is enforced at compile time through the borrow checker. It ensures that mutable references to data are exclusive and prevents data races by statically preventing concurrent mutable access. |
| Lifetime Annotations | Explicit annotations that specify the lifetimes of references, ensuring memory safety and preventing dangling references. | Rust sometimes requires explicit lifetime annotations to ensure the validity of references and prevent dangling pointers. This ensures memory safety by enforcing strict rules on the lifetimes of references. |
| Universal / Unified Type System |  | It uses `any` trade. |
| Type Compatibility |  | Traits and lifetimes determine type compatibility. Types are compatible if they satisfy the trait bounds and lifetime constraints specified in the code, enabling safe and efficient memory management and flexible code reuse. |
|  | … |  |

## Typing Models

- **Primitive types**:  [Boolean](https://doc.rust-lang.org/reference/types/boolean.html) — `bool`;  [Numeric](https://doc.rust-lang.org/reference/types/numeric.html) — integer and float; [Textual](https://doc.rust-lang.org/reference/types/textual.html) — `char` and `str`; [Never](https://doc.rust-lang.org/reference/types/never.html) — `!` — a type with no values.
- **Sequence types**: [Tuple](https://doc.rust-lang.org/reference/types/tuple.html); [Array](https://doc.rust-lang.org/reference/types/array.html); [Slice](https://doc.rust-lang.org/reference/types/slice.html)
- **User-defined types**: [Struct](https://doc.rust-lang.org/reference/types/struct.html); [Enum](https://doc.rust-lang.org/reference/types/enum.html); [Union](https://doc.rust-lang.org/reference/types/union.html)
- F**unction types**: [Functions](https://doc.rust-lang.org/reference/types/function-item.html); [Closures](https://doc.rust-lang.org/reference/types/closure.html)
- **Traits**: Rust’s trait system allows for code reuse through abstract types and methods implemented for any type that satisfies the trait’s constraints.  [Trait objects](https://doc.rust-lang.org/reference/types/trait-object.html); [Impl trait](https://doc.rust-lang.org/reference/types/impl-trait.html).
- **Generics ([Parenthesized types](https://doc.rust-lang.org/reference/types.html#parenthesized-types))**: Rust generics enable the creation of flexible and reusable code by allowing functions, structs, and traits to operate on multiple types while enforcing type safety at compile time.
- **Algebraic Data Types** (Enums and Structs): Rust provides enums and structs for defining custom data types, allowing for expressive and concise representation of data structures.
- **Associated Types and Type Aliases**: Associated types enable types to be associated with traits, allowing for flexible and generic implementations, while type aliases provide convenient names for complex types.
- **Pointer Types**: Rust distinguishes between different kinds of pointers like references (&), mutable references (&mut), raw pointers (*), and smart pointers (e.g., Box<T>, Rc<T>, Arc<T>), providing fine-grained control over memory management and safety.
- **Recursive Types**: Nominal types — [structs](https://doc.rust-lang.org/reference/types/struct.html), [enumerations](https://doc.rust-lang.org/reference/types/enum.html), and [unions](https://doc.rust-lang.org/reference/types/union.html) — may be recursive. Each `enum` variant or `struct` or `union` field may refer, directly or indirectly, to the enclosing `enum` or `struct` type itself.

## Rust Standard Library (std) Types

Here's a simplified table listing some common types found in the Rust Standard Library (std):

| Type | Description |
| --- | --- |
| i8, i16, i32, i64 | Signed integers of various bit widths. |
| u8, u16, u32, u64 | Unsigned integers of various bit widths. |
| isize, usize | Machine-dependent signed and unsigned integers. |
| f32, f64 | Floating-point numbers of single and double precision, respectively. |
| bool | Boolean type representing true or false values. |
| char | A Unicode scalar value, representing a single character. |
| str | A string slice, which is a reference to a UTF-8 encoded string. |
| String | A heap-allocated string type, which is growable and mutable. |
| Vec<T> | A growable, heap-allocated, contiguous array type. |
| Option<T> | Represents an optional value, either Some(T) or None. |
| Result<T, E> | Represents either success with a value of type T or failure with an error of type E. |
| Box<T> | A smart pointer type representing a heap-allocated value of type T with ownership semantics. |
| Rc<T> | A reference-counted smart pointer type for shared ownership of values of type T. |
| Arc<T> | An atomically reference-counted smart pointer type for shared ownership across threads. |
| Cell<T> | A type providing interior mutability for shared references, allowing mutation in immutable contexts. |
| RefCell<T> | A type providing mutable borrowing of its contained value, checked at runtime. |

This table covers some fundamental types available in the Rust Standard Library, including numeric types, strings, collections, smart pointers, and types for managing ownership and mutability.

## Types Representation

Here's a Table Outlining the Data Representation of Types in Rust:

| Type | Data Representation |
| --- | --- |
| **Primitive Types** | Directly represent their values in memory (e.g., integers, floats, characters). |
| **Structs** | Contiguous layout of fields in memory, with padding for alignment and potential optimizations based on field types. |
| **Enums** | Represents one of several possible variants, with each variant having its data representation, often optimized for space efficiency. |
| **Arrays** | Contiguous sequence of elements of the same type, stored in memory consecutively. |
| **Slices** | Reference to a contiguous sequence of elements, represented by a pointer to the start of the sequence and a length. |
| **Tuples** | Ordered collection of elements of potentially different types, with each element having its data representation. |
| **References** | Pointer to a value in memory, with additional information about ownership, borrowing, and lifetime, often represented as a pointer and metadata. |
| **Smart Pointers** | Wrappers around values on the heap, with additional metadata for ownership and reference counting, such as `Box`, `Rc`, and `Arc`. |
| **Option and Result** | Enum types used for error handling and optional values, representing either a value or no value (Option) or a value or an error (Result), with associated data representations for both cases. |

This table provides an overview of the data representation of various types in Rust, highlighting their memory layout and additional metadata when applicable.

## Pointers

> Rust pointers, including safe references (`&T` and `&mut T`), unsafe raw pointers (`*const T` and `*mut T`), and smart pointers like `Box<T>`, `Rc<T>`, and `Arc<T>`, provide diverse mechanisms for memory access and management, ensuring safety and efficiency in system-level programming.
> 

[Rust Pointers](note.html?n=technica/computation/language-system/conceptual-model-language-system/typescript/typescript-type-system/rust-pointers.md)

## Type Coercions

> **Type coercions** are implicit operations that change the type of a value. They happen automatically at specific locations and are highly restricted in what types actually coerce.
> 

> 

## Destructors

When an [initialized](https://doc.rust-lang.org/reference/glossary.html#initialized) [variable](https://doc.rust-lang.org/reference/variables.html) or [temporary](https://doc.rust-lang.org/reference/expressions.html#temporaries) goes out of [scope](https://doc.rust-lang.org/reference/destructors.html#drop-scopes), its *destructor* is run or *dropped*. [Assignment](https://doc.rust-lang.org/reference/expressions/operator-expr.html#assignment-expressions) also runs the destructor of its left-hand operand if it's initialized. If a
variable has been partially initialized, only its initialized fields are dropped.

## Interior Mutability

Sometimes, a type needs to be mutated while having multiple aliases. In Rust, this is achieved using a pattern called *interior mutability*. A type has interior mutability if its internal state can be changed through a [shared reference](https://doc.rust-lang.org/reference/types/pointer.html#shared-references-) to it. This goes against the usual [requirement](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) that the value pointed to by a shared reference is not mutated.

## Lifetime

Rust has rules that allow lifetimes to be omitted in various places where the compiler can infer a sensible default choice.

## Rust Modules System

> Utilizing `mod` and `use` keywords, the Rust module system organizes code into modular namespaces that enhance code reusability, maintainability, and control over privacy and scope within a package.
> 

> 

## Understanding Model

> **Ownership is Rust’s** most unique feature and has deep implications for the rest of the language. It enables Rust to make memory safety guarantees without needing a garbage collector, so it’s important to understand how ownership works. In this chapter, we’ll talk about ownership as well as several related features: borrowing, slices, and how Rust lays data out in memory.
> 
- [Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html#understanding-ownership)

## References

- [Type system](https://doc.rust-lang.org/reference/type-system.html#type-system)
- [Special types and traits](https://doc.rust-lang.org/reference/special-types-and-traits.html)
- [Rust's Type System Is Turing-Complete: Type-Level Programming in Rust](https://news.ycombinator.com/item?id=13843288) ([sdleffler.github.io](http://sdleffler.github.io/))
- [Untapped potential in Rust's type system](https://news.ycombinator.com/item?id=27490596) ([jakobmeier.ch](http://jakobmeier.ch/))
- [Bjarne Stroustrup Weighs in on Distributed Systems, Type Safety and Rust](https://news.ycombinator.com/item?id=24036827) ([thenewstack.io](http://thenewstack.io/))
- [Fighting Rust's Expressive Type System](https://news.ycombinator.com/item?id=24867610) ([thefuntastic.com](http://thefuntastic.com/))
- [The usability of advanced type systems: Rust as a case study](https://news.ycombinator.com/item?id=34890787) ([arxiv.org](http://arxiv.org/))
- Will Crichton. 2020. The Usability of Ownership. arXiv preprint arXiv:2011.06171 (2020).
- Will Crichton, Marco Patrignani, Maneesh Agrawala, and Pat Hanrahan. 2021. Modular Information Flow Through
Ownership. CoRR abs/2111.13662 (2021). arXiv:2111.13662 [https://arxiv.org/abs/2111.13662](https://arxiv.org/abs/2111.13662)
- [Special types and traits](https://doc.rust-lang.org/reference/special-types-and-traits.html)
- [Common Collections](https://doc.rust-lang.org/book/ch08-00-common-collections.html)
- [Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- - [Appendix C: [Derivable Traits]](https://doc.rust-lang.org/book/appendix-03-derivable-traits.html)
- …