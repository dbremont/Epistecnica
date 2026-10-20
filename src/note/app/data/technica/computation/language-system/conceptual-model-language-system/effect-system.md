---
tags: [effect-system]
---

# Effect System

- [Algebraic Effect](note.html?n=technica/computation/language-system/conceptual-model-language-system/algebraic-effect.md), [Continuation](note.html?n=technica/computation/language-system/conceptual-model-language-system/continuation.md), [Type System](note.html?n=technica/computation/language-system/conceptual-model-language-system/type-system.md), [Exception Handling System](note.html?n=technica/computation/language-system/conceptual-model-language-system/exception-handling-system.md), [Unit of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/unit-of-computation.md), [Model of Computation](note.html?n=technica/computation/language-system/conceptual-model-language-system/model-of-computation.md), [Exception](note.html?n=technica/computation/language-system/conceptual-model-language-system/exception.md), [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md)

> An effect is any deviation from a pure, extensional function into a context-sensitive transition system.
> 

> An **Effect System** is a **type system** on steroids, providing a way to track the **flow of values** and **control the flow of effects** in your program. - Oleg Kiselyov
> 

> **Effect systems** are formal systems that analyze and track computational effects in programs. They can statically analyze code to ensure proper handling of effects, such as side effects or exceptions.
> 

> An **effect system** is a type system that provides a way to reason about **computational effects** in programming languages. It is designed to help developers manage and control the effects that a program can have, such as input/output (I/O) operations, exceptions, and mutable state.
> 

> A **computational effect system** is a precise specification of the "abstract state of a computation," tailoring the delivery of specific features to the user within the context of a subset of computations.
> 

> The relationship between an **effect system and a type system** lies in the effect system's extension of the type system, providing a structured means to express and control computational effects within a programming language.
> 

> **Referential transparency (purity)**  means a function always returns the same output for the same input and causes no side effects. This property makes reasoning about programs easier.
> 

QA:

- In which **notion of change (computation)** does a the idea of an effect and effect system makes sense?
- …

## Computational Effect

> A **computational effect** refers to a change in the **“abstract state of a computation”** caused by an action or **operation (effectful computation)**, such as input/output (I/O), exceptions, or mutable state.
> 

> **“Abstract State of a Computation”** is an ill-defined term, but some aspects it captures include control flow (e.g., stack frames, instruction pointer) and program state (e.g., memory, registers, variable bindings, heap allocation, etc.); side effects (sending mails, writing to files, …).
> 

> An **effectful computation** is a computation that has an **observable effect**, such as printing to the console, reading from a file, or modifying a global variable.
> 

## List of Computational Effects

> 

| **Computational Effect** | **Description** |
| --- | --- |
| **State** | Refers to program state changes, such as updating a variable or data structure. |
| **IO** | It involves input/output operations like reading/writing files, network communication, or printing to the console. |
| **Exception** | Refers to the possibility of an exception being thrown or caught, affecting the program's control flow. |
| **Non-determinism** | Refers to the potential for a program to produce different outputs for the same input, such as with random number generators. |
| **Concurrency** | Involves the ability to execute multiple tasks or threads simultaneously, which can introduce race conditions and synchronization issues. |
| **Memory Allocation and Deallocation** | Involves the allocation and deallocation of memory for variables or data structures. |
| **Resource Allocation** | Refers to creating and destroying resources, including memory management. |
| **Time** | Refers to a program's ability to interact with the system clock or other time-related functionality. |
| **Control Transfer** | Changes the control flow of a program, such as through function calls or jumps to different code locations. |
| **Garbage Collection** | The automatic reclamation of unused memory in a program. |
| **Reflection and Introspection** | The ability of a program to inspect or modify its structure and behavior. |
| **Continuation (Stack Manipulation)** | Captures the entire computation state at a certain point, allowing the program to resume or execute later. |
| **Type System Operations** | It involves operations that manipulate or check the compatibility of types, such as casting and type inference. |
| **Side Effects** | Any effect that modifies the program's state or the outside world, such as console output or file modifications. |

## Effect System Primitives

> React's Fiber reconciler breaks work into smaller units and schedules them using a priority-based system.
> 

> Here’s a table summarizing various **computational constructs** related to managing side effects and control flow in programming:
> 

| **Category** | **Primitive** | **Description** | **Example Syntax** | **Used In** |
| --- | --- | --- | --- | --- |
| **State & Environment** | `get` | Retrieves the current state. | `get >>= (\x -> put (x+1))` | Haskell (State Monad), Eff |
|  | `put` | Updates the state. | `put 42` | Haskell, Eff, Algebraic Effects |
|  | `local` | Temporarily modifies an environment. | `local modify (+1)` | Haskell (Reader Monad), OCaml |
|  | `perform` | Triggers an effect (e.g., I/O, system call). | `perform ReadFile "file.txt"` | Eff, Koka, OCaml |
| **Control Flow & Exceptions** | `throw` | Raises an exception. | `throw "Error"` | Java, Python, Haskell |
|  | `catch` | Handles an exception. | `try { ... } catch (e) { ... }` | Java, Python, Haskell |
|  | `call/cc` | Captures and resumes execution state. | `(call/cc (lambda (k) ...))` | Scheme, Racket, Lisp |
|  | `handle` | Defines a handler for an effect. | `handle State { get -> ... }` | Eff, Algebraic Effects |
|  | **setjmp / longjmp** |  |  |  |
| **Continuations & Coroutines** | `resume` | Resumes a suspended computation. | `resume(cont)` | Python, Kotlin |
|  | `suspend` | Pauses a computation. | `suspend fun f() {}` | Kotlin, JavaScript |
|  | `yield` | Suspends execution and returns a value. | `yield x` | Python, JavaScript, C++ |
|  | `co_yield` | Coroutine-based yielding. | `co_yield x` | C++20, JavaScript |
|  | `continuation` | Encapsulates an execution state. | `Continuation<T>` | Java, Kotlin |
|  | `coroutine` | Defines a function that can be paused and resumed. | `CoroutineScope.launch { ... }` | Kotlin, Python, C++ |
| **Async & Parallel Computation** | `async` | Starts an asynchronous computation. | `async function f() {}` | JavaScript, Python, Rust, C# |
|  | `await` | Waits for an async computation to complete. | `await f();` | JavaScript, Python, Rust |
|  | `fork` | Creates a new thread. | `forkIO action` | Haskell, Java, C++ |
|  | `join` | Synchronizes a thread. | `thread.join()` | Java, C++, Rust |
|  | `race` | Runs computations in parallel and returns the first result. | `race(task1, task2)` | JavaScript (Promises), Scala (Cats-Effect) |
|  | `parallel` | Runs multiple computations concurrently. | `parallel(tasks)` | Scala, Rust, Haskell |
| **Effect Composition & Functional Abstractions** | `pure` | Lifts a value into a pure effectful context. | `pure(42)` | Haskell, Scala |
|  | `bind` (`>>=`) | Chains effectful computations. | `m >>= f` | Haskell, Scala, OCaml |
|  | `flatMap` | Functionally composes monadic computations. | `opt.flatMap(f)` | Scala, Java, Kotlin |
|  | `Cont` Monad | Encapsulates continuations. | `runCont (Cont k -> k 42) print` | Haskell, Scala |

## Side Effect

> A **side effect** of a computational expression or procedure **is any externally observable state change or interaction with the environment that occurs during the evaluation of the expression or execution of the procedure, beyond producing a return value.**
> 

> Given a program PP containing an expression or procedure ee, a side effect is any change to a state SS outside the lexical scope of ee, or any interaction II with the external environment, such that executing ee transforms the overall system state or environment from (S,I)(S, I) to (S′,I′)(S', I'), where S′≠SS' \neq S or I′≠II' \neq I, independently of the return value of ee.
> 

Key points:

- **Externally observable** means the change can be detected by other parts of the program or by external systems.
- **State change** includes modification of variables, memory, files, hardware registers, or other resources not local to the expression.
- **Interaction with environment** includes I/O operations such as console output, network communication, or device control.
- The **return value** of the expression is logically separate from these side effects.
- Side effects violate **referential transparency**, as substituting ee by its value alone would change program behavior.

---

### Examples mapped to the definition:

| Side Effect Type | Description |
| --- | --- |
| Global variable mutation | Changing a global variable S→S′S \to S' |
| I/O operation | Writing to a file or console (modifying environment I→I′I \to I') |
| Memory mutation outside scope | Updating a shared data structure or heap memory |
| Network communication | Sending data packets over a network |

---

If you want, I can also provide a formal logic or category-theoretic perspective on side effects!

## References

- [Effect System](https://en.wikipedia.org/wiki/Effect_system)
- [Adding an Effect System to OCaml [video] (janestreet.com)](https://news.ycombinator.com/item?id=18155178)
- Nielson, Flemming, et al. “Type and effect systems.” Principles of Program Analysis (1999): 283-363.
- Marino, Daniel, and Todd Millstein. “A generic type-and-effect system.” Proceedings of the 4th international workshop on Types in language design and implementation. 2009.
- Lucassen, John M., and David K. Gifford. “Polymorphic effect systems.” Proceedings of the 15th ACM SIGPLAN-SIGACT symposium on Principles of programming languages. 1988.
- [Efect System](https://en.wikipedia.org/wiki/Effect_system)
- [Tracing monadic computations and representing effects](https://www.cs.ox.ac.uk/jeremy.gibbons/publications/trmon.pdf)
- Carlsson, M. (2002). Monads for Incremental Ccomputing. 26–35.
- Wadler, P. (1994). Monads and Composable Continuations. 7(1), 39–55.
- Steele, G. L. (1994). Building Interpreters by Composing Monads. 472–492.
- [What is conceptual relationship between monadic effects and algebraic effects?](https://discuss.ocaml.org/t/what-is-conceptual-relationship-between-monadic-effects-and-algebraic-effects/6229)
- https://github.com/acdlite/react-fiber-architecture