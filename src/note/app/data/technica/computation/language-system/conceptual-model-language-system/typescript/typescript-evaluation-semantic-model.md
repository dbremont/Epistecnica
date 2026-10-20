# Typescript: Evaluation(Semantic) Model

> **Rust's Evaluation Model**, particularly how it handles expressions and statements, is central to understanding the language's approach to memory safety, concurrency, and overall performance.
> 

> A **semantics** for a programming language is a model for the computational meaning
of a program written in that language.
> 

## Scoping Model

> Rust’s closures provide a concise and flexible way to define anonymous functions that capture variables from their enclosing scope.
> 

> Rust uses lexical scope.
> 

## Rust Evaluation Model

Rust's evaluation model encompasses the following aspects:

1. Eager Evaluation: Expressions are typically evaluated eagerly, meaning their operands are evaluated before the operation.
2. Strict Evaluation: Rust follows strict evaluation rules, ensuring that expressions are evaluated in a deterministic order and that side effects occur predictably.
3. Call-by-Value: By default, function arguments are passed by value, meaning the function receives a copy of the argument's value.
4. Ownership Semantics: Rust's ownership system dictates how memory resources are managed and ensures memory safety by enforcing rules for ownership, borrowing, and lifetimes.
5. Immutable by Default: Variables are immutable by default in Rust, preventing unintended mutations and encouraging safer programming practices.
6. Move Semantics: Rust employs move semantics to transfer resource ownership, preventing data races and ensuring memory safety.
7. Borrowing: References to data can be borrowed immutably or mutably, allowing safe concurrent access to shared resources.
8. Lifetimes: Rust's lifetime system ensures that references remain valid for the duration they are used, preventing dangling pointers and memory leaks.
9. Pattern Matching: Pattern matching allows for concise and expressive handling of different cases or patterns within data structures, aiding control flow and data manipulation.
10. Lazy Evaluation: Rust supports lazy evaluation through closures and iterators, allowing computations to be deferred until their results are needed.
11. Memory Safety: Rust's evaluation model prioritizes memory safety, preventing common pitfalls such as null pointer dereferencing and buffer overflows through its ownership and borrowing system.

These aspects collectively define Rust's evaluation model, contributing to its safety, performance, and expressiveness as a systems programming language.

## References

- [Constant evaluation](https://doc.rust-lang.org/reference/const_eval.html#constant-evaluation)
- White, Alexa. Towards a Complete Formal Semantics of Rust. Diss. California Polytechnic State University, 2021.
- Kan, Shuanglong, et al. "An Executable Operational Semantics for Rust with the Formalization of Ownership and Borrowing." arXiv preprint arXiv:1804.07608 (2018).
- [Constant Evaluation](https://doc.rust-lang.org/reference/const_eval.html)
- …