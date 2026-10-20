# Functional Model of Computation

- [Lambda Calculus](note.html?n=technica/computation/language-system/conceptual-model-language-system/lambda-calculus.md), [Declarative Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/declarative-model-of-computation.md), [SKI Combinator Calculus](note.html?n=technica/computation/language-system/conceptual-model-language-system/ski-combinator-calculus.md)

> Functional programming is a programming paradigm that emphasizes the use of functions as the primary means of computation, treating them as first-class citizens that can be composed and combined to build more complex programs.
> 

## Modelling Time

> See more in [Time](note.html?n=technica/computation/language-system/conceptual-model-language-system/time.md).
> 

> Functional programming is based on the idea of immutable data and pure functions, which means that a function always produces the same output given the same input, and does not have any side effects that modify the state of the program or the environment. While this approach has many advantages, it also means that functional programming is not well-suited for modeling time-dependent behavior or stateful computations.
> 

> Time is a fundamental aspect of many computational problems, such as simulations, games, and real-time systems. These types of problems require a model of computation that can represent and manipulate time-dependent data and state. In contrast, functional programming emphasizes the use of functions that are independent of time and state, and instead operate solely on their inputs to produce their outputs.
> 

> While functional programming languages can include constructs for working with time, such as timers or event streams, they are typically implemented as libraries or extensions to the core language, rather than as fundamental features of the language itself. This means that functional programming is often less well-suited for time-dependent problems than imperative or object-oriented programming, which provide more explicit support for stateful and time-dependent computations.
> 

> Real-world processes involve time and state. While IO in functional languages mimics a von Neumann machine to handle time, this is more of a compromise than a true solution. Pure functional programming introduces a deeper approach: it separates **programming time** (the order in which computations are written or structured) from **execution time** (when computations actually run).
> 

| Representation | Description |
| --- | --- |
| **Lambda Calculus** | A formal system for expressing computation based on function abstraction and application. Functions are represented as lambda expressions, allowing for higher-order functions and recursion. |
| **Functional Data Structures** | Immutable data structures such as lists, trees, maps, and sets that support functional programming paradigms. These structures are persistent and rely on structural sharing for efficiency. |
| **Algebraic Data Types (ADTs)** | Composite data types defined by combining simpler types using product types (e.g., records, tuples) and sum types (e.g., enums, union types). ADTs provide a powerful way to model data. |
| **Pattern Matching** | A language feature that allows for deconstructing data structures and matching patterns within them. Pattern matching is often used with ADTs to handle different cases in a concise manner. |
| **Higher-Order Functions** | Functions that can accept other functions as arguments or return functions as results. Higher-order functions enable composition, abstraction, and expressive programming styles. |
| **Currying** | The technique of transforming a function that takes multiple arguments into a series of functions, each taking a single argument. Currying facilitates partial application and function composition. |
| **Lazy Evaluation** | Delaying the evaluation of expressions until their results are needed. Lazy evaluation enables infinite data structures, improves efficiency by avoiding unnecessary computations, and supports modularity. |
| **Monads** | Computational constructs that provide a framework for sequencing and composing computations while encapsulating side effects. Monads enable imperative-style programming in a pure functional context. |
| **Type Classes** | A mechanism for ad hoc polymorphism, allowing functions to be overloaded based on the types of their arguments. Type classes provide a way to define generic operations and enable modular, extensible code. |
| **Memoization** | Caching the results of function calls to avoid redundant computations. Memoization is often used to optimize recursive or repetitive computations by storing previously computed results. |

## References

- [https://jgbm.github.io/eecs762f19/papers/wadler-monads.pdf](https://jgbm.github.io/eecs762f19/papers/wadler-monads.pdf)
- [Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire](https://maartenfokkinga.github.io/utwente/mmf91m.pdf)
- http://homepages.inf.ed.ac.uk/wadler/papers/essence/
-