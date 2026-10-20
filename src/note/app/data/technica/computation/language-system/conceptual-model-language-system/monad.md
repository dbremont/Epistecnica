---
tags: [effect-system]
---

# Monad


> A monad is a technique for representing (wrapping) an **underlying value (`return`)** and providing a means to **apply transformations (`bind`)** to it, enabling the **composition of computations** in a coherent and sequential manner.
> 

> Note: `OperationResult<T>`k  was really a ‘tag container’;   this does not ‘encapsulate’ ‘abstract’ an ‘effect’; just a return result.
> 

## Definition

A monad is a data type that consists of three components:

- A **type constructor** that represents the type of values that the monad will operate on.
- A **“unit”** function that takes a value of the underlying type and wraps it in a monadic context.
- A **“bind”** function that takes a monadic value and a function that maps a value of the underlying type to another monadic value, and produces a new monadic value.

## Use

> **Monads are used to encode effects  by threading it through the computation.**
> 

> Monads provide a structured way to handle **side effects, sequencing of computations, and context propagation** in functional programming, enabling abstraction over **state management, asynchronous execution, error handling, and I/O operations** while preserving composability.
> 

> Delayed Computation: …
> 

> Potential Value: Maybe, Either, Option, MightBeTrue, Result, …
> 

## Cons

| **Con** | **Explanation** |
| --- | --- |
| Steep Learning Curve | Monads are abstract and can be difficult for beginners to grasp. |
| Boilerplate Code | Requires extra syntax and chaining that can feel verbose or cumbersome. |
| Composability Challenges | Combining multiple monads needs complex techniques like monad transformers, increasing complexity. |
| Less Intuitive Control Flow | The flow of data and effects is implicit, making code harder to read compared to imperative style. |
| Debugging Difficulty | Wrapped effects and implicit sequencing make debugging monadic code more challenging. |
| Performance Overhead | Additional abstraction layers can lead to runtime inefficiencies. |
| Harder Modularity | Encapsulated effects require understanding the whole monadic context, limiting independent reasoning. |

## Etymology

> The name “monad” comes from the Greek word “monas,” which means “unity” or “single unit.” In philosophy, the term “monad” was used by the philosopher Gottfried Wilhelm Leibniz to refer to an indivisible and unchangeable unit of reality.
> 

> The use of the term “monad” in computer science was first introduced by the mathematician and computer scientist Eugenio Moggi in his 1989 paper “Computational lambda-calculus and monads.” In this paper, Moggi introduced the idea of using monads as a way to model side effects in functional programming languages.
> 

## Effect

> An **effect** is anything a computation **does beyond returning a value** — reading, writing, failing, waiting, branching, etc.
> 

> Note: This definition is a definition by extension; it's hard to define an effect by a simple characteristic adjective.
> 

> **Note:** Don’t be a slave to definitions—this is an engineering concept. Always ask yourself: *Is this really an effect? Can it be mapped to something that is not an effectful computation?*
> 

An **effect** is any interaction of a computation with **context beyond its immediate input/output**, such that it may:

- Depend on external state
- Modify shared state
- Fail, pause, interact, or produce multiple outcomes

## Types of Monads

> 

| **Category** | **Monad** | **Description** | **Use** |
| --- | --- | --- | --- |
| **Side Effects Handling** | `IO` | Encapsulates side effects in computations, allowing pure functions to handle I/O operations. | Managing user input/output, file I/O, interacting with external systems while keeping functions pure. |
|  | `Cont` | Represents computations that can be interrupted and resumed, encapsulating side effects. | Delayed computations, managing continuations, controlling the flow of control in functional programs. |
| **State Management** | `State` | Encapsulates mutable state in a pure functional context, allowing stateful computations. | Managing game state, session information, or mutable state without breaking purity. |
|  | `ST` | Represents computations with mutable state that can be executed in a sequence. | Sequential stateful computations (e.g., imperative-style loops in functional programming). |
| **Error Handling** | `Maybe` | Represents computations that may fail without causing runtime errors, often used for optional values. | Handling optional values, avoiding `null` or `undefined` in a safe and predictable manner. |
|  | `Option` | Represents an optional value that can either be present or absent, used for safe computation. | Handling optional data, where a value may or may not be available. |
| **Error Handling (with messages)** | `Either` | Represents computations that may fail, providing an error message or a successful result. | Handling operations that can return success or failure with detailed error messages. |
|  | `Result` | Encapsulates success or failure with an error message, often used in scenarios where computation can fail. | Used for computations that may return either a successful value or an error message (e.g., parsing). |
| **Asynchronous Programming** | `Future` | Represents a value that may not be computed yet, allowing chaining of asynchronous operations. | Managing asynchronous tasks like HTTP requests, I/O operations, or database queries. |
|  | `Promise` | Represents a computation that will complete in the future, allowing the chaining of async operations. | Handling asynchronous tasks in JavaScript, chaining computations that depend on the results of async calls. |
| **Concurrency** | `ReaderT` | Threads read-only state (e.g., configuration) through computations without mutable state. | Passing shared configurations or global state through multiple computations without side effects. |
|  | `Task` | Encapsulates an asynchronous computation that may be executed concurrently. | Managing asynchronous computations, often used in systems programming or concurrency-heavy applications. |
| **Parsing** | `Parser` | Allows building complex parsers by composing smaller parsers in a clean and modular way. | Building compilers, interpreters, or complex parsing libraries (e.g., parsing JSON or regular expressions). |
|  | `Attoparsec` | A parser combinator library that allows building parsers with high performance and composability. | Fast, combinatory parsing, often used in high-performance parsing applications (e.g., JSON parsers). |
| **Probabilistic Computations** | `List` | Represents non-deterministic computations where multiple results may arise from a single computation. | Non-deterministic algorithms, like search algorithms or AI decision-making with multiple possible outcomes. |
|  | `Free` | Encapsulates free monads that can model computations with non-determinism and probabilistic outcomes. | Modeling complex control flows, building interpreters or non-deterministic simulations. |
| **Logging & Debugging** | `Writer` | Collects logs or additional information alongside computations without affecting their result. | Collecting logs during program execution, tracking additional metadata, or tracing execution flow. |
|  | `Logging` | Accumulates log data or other metadata as a result of computations, often used for debugging purposes. | Generating logs or tracking debugging information without side effects. |
| **Dependency Injection** | `Reader` | Passes implicit dependencies (like configurations) through computations to avoid mutation. | Managing global configurations, settings, or dependencies in a functional programming paradigm. |
|  | `Env` | Provides a consistent environment for computations to access external dependencies or configurations. | Structuring applications where a global environment (e.g., configuration) is needed throughout the program. |
| **Blockchain/Smart Contracts** | `SmartContract` | Ensures that computations in blockchain systems are deterministic and pure, avoiding side effects. | Writing smart contracts in functional programming languages, ensuring determinism in blockchain computations. |
|  | `Plutus` | A platform for writing smart contracts on the Cardano blockchain, using pure functional programming. | Writing secure, deterministic smart contracts for blockchain environments, ensuring integrity in decentralized applications. |

## OperationResut<T>

```csharp
public class OperationResult<T>
{
    private  bool IsSuccess { get; set; }
    private T Value { get; set; }

    // Return function - wrap a value into the monadic context
    public static OperationResult<T> Return(T value)
    {
        return new OperationResult<T> { IsSuccess = true, Value = value };
    }

    // Bind function - chain operations
    public OperationResult<U> Bind<U>(Func<T, OperationResult<U>> func)
    {
        if (!IsSuccess) return new OperationResult<U> { IsSuccess = false };
        return func(Value);
    }
}
```

## QA

### Why branching is considered an effect?

> Branching is considered an effect because it dynamically alters control flow based on conditions, introducing context-dependent computation paths that can influence or depend on side effects like failure, state, or nondeterminism.
> 

> It **shaped** the computation.
> 

## References

- [Functor](https://app.notion.com/p/Functor-19dc0f5171ec80b0b10bf84a18c37fe8?pvs=21)
- [What the hell are Monads?](https://www-users.mat.umk.pl//~adwid/materialy/haskell-doc/Monads.html)
- [Monads as a Design Pattern](https://blog.theincredibleholk.org/blog/2014/05/24/monads-as-a-design-pattern/)
- [Notions of computation and monads](https://www.cs.cmu.edu/~crary/819-f09/Moggi91.pdf)
- [The Marriage of Effects and Monads](https://www.cs.tufts.edu/~nr/cs257/archive/phil-wadler/effectstocl.pdf)
- [Monads in Computer Science](https://www.uibk.ac.at/mathematik/algebra/staff/fritz-tobias/ct2021_course_projects/category_theory.pdf)
- [Monads and Effects](https://bartoszmilewski.com/2016/11/30/monads-and-effects/)
- [What the Heck is a Monad, Anyway?](https://gist.github.com/kvverti/2ea422007a0f18b7877326cf3f8def86)
- [From Monads to Effects and Back](https://goto.ucsd.edu/~nvazou/koka/padl16.pdf)
- [The essence of functional programming](https://jgbm.github.io/eecs762f19/papers/wadler-monads.pdf)
- [If monads are the solution, what is the problem?](https://news.ycombinator.com/item?id=17645277)
- [Tracing monadic computations and representing effects](https://www.cs.ox.ac.uk/jeremy.gibbons/publications/trmon.pdf)
- Wadler, P. (1998). Marriage of Effects and Monads. 63–74.
- Moggi, E. (1991). Notions of Computation and Monads. 93(1), 55–92.
- Benton, N., Hughes, J., Moggi, E. (2000). Monads and Effects. 2395 LNCS, 42–122.
- Kim, T., Spivak, D. I. (2013). In Search of a Monad For System Call Abstractions.