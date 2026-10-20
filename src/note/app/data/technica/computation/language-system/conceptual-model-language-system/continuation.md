---
tags: [effect-system, linguistic-abstraction]
---

# Continuation

- [Closure](note.html?n=technica/computation/language-system/conceptual-model-language-system/closure.md), [Effect System](note.html?n=technica/computation/language-system/conceptual-model-language-system/effect-system.md), [Coroutine](note.html?n=technica/computation/language-system/conceptual-model-language-system/coroutine.md), [Continuation Passing Style (CPS)](note.html?n=technica/computation/language-system/conceptual-model-language-system/continuation-passing-style-cps.md), [Notion of Change](note.html?n=technica/computation/language-system/conceptual-model-language-system/notion-of-change.md)

> In this note we will explore a formalism to encode all of the construct of transition semantics.
> 

> Continuations are an **approach** to **representing and manipulating the flow of control in a program** by making the "rest of the computation" explicit as a first-class entity.
> 

> A **continuation** is an **abstraction of the execution state** of a program that allows resuming computation from a specific point at a later time.
> 

> Captures the **entire execution state** (stack, control flow); or part of that.
> 

> Reader: This is a very abstract idea; explores it’s implications;  implementations (operators); semantics; limitations; real applications, …
> 

QA:

- What is the meaning of “capturing the current **state of a computation**”?
- Is a continuation a fancy word for called stack manipulation?
- How to simulate continuation with  python? Continuation-Passing Style (CPS),  Generators (`yield`),  Coroutines (`async/await`), Exception Handling (for non-local jumps).
- Which features of continuations? Inversion of Control,  Re-invocation,
- What is the power and limitations of **continuations**?

## Formalism

> What it is a **continuation**? A **continuation** is a representation of the **remaining future** computation from a given execution point. A **continuation** is a representation of the remaining future computation from a given execution point.  Note: What I am doing, and what next?
> 

> Which are the mechanism to **implement a continuation**? Continuations can be implemented implicitly through call stacks and return addresses, explicitly through heap-allocated continuation objects or CPS-transformed functions, or via runtime context-capture mechanisms that preserve resumable execution state including instruction pointers, environments, registers, and control contexts.
> 

> What is the status of **continuation from the used to describe computations perspective**?  A continuation is one of the most universal and foundational abstractions for describing computation and control flow, although in most programming systems it remains an implicit background semantic structure exposed indirectly through syntactic control constructs such as function calls, loops, exceptions, generators, coroutines, async/await, and schedulers rather than as an explicit first-class computational object.
> 

> How are continuation **exposed as a programming abstraction**? Continuations are exposed either directly as first-class or delimited control operators (`call/cc`, `shift/reset`, effect handlers) or indirectly through higher-level abstractions such as callbacks, generators, coroutines, async/await systems, schedulers, and cooperative multitasking runtimes that operationally manipulate resumable future computations.
> 

## Encoding

> How are different elements (control flow structures) formulated in terms of continuation?
> 

| Construct | Continuation-Based Formulation |
| --- | --- |
| **Sequential Execution** | A continuation represents “the rest of the computation” after the current step. Execution proceeds by passing the result of one computation into the next continuation. |
| **Conditional Branching (`if`)** | The condition selects between alternative continuations (`then-continuation` vs `else-continuation`). |
| **Loops (`while`, `for`)** | Encoded as recursive continuations where the continuation re-invokes itself until a termination condition redirects to the exit continuation. |
| **Function Call** | A function receives an implicit or explicit continuation representing the caller’s remaining computation. Returning becomes invoking that continuation with a result. |
| **Recursion** | Recursive calls propagate continuations through nested continuation chains, representing deferred future computations. |
| **Return** | Returning from a function is equivalent to invoking the caller continuation with the produced value. |
| **Tail Call** | Tail calls directly reuse the current continuation instead of creating a new continuation frame. |
| **`goto` / Non-Local Jump** | Encoded as direct transfer to a captured continuation representing another execution point. |
| **`break`** | A loop-exit continuation is invoked, bypassing the remaining loop-body continuation. |
| **`continue`** | The loop-iteration continuation is invoked directly, skipping the remaining body computation. |
| **Exceptions (`throw`)** | Exception propagation invokes an exception continuation instead of the normal continuation. |
| **Exception Handlers (`try/catch`)** | Introduce layered continuations: normal continuations and exceptional continuations. |
| **Coroutines** | Coroutines capture continuations representing suspended execution states and later resume them. |
| **Generators (`yield`)** | `yield` captures the current continuation, returns a value outward, and stores the continuation for later resumption. |
| **Async / Await** | Suspended computations are represented as continuations resumed upon future completion events. |
| **Backtracking** | Alternative execution paths are stored as continuations that can later be resumed upon failure. |
| **Nondeterminism** | Multiple continuations coexist simultaneously as possible future execution branches. |
| **Concurrency** | Independent computations possess separate continuations managed by a scheduler continuation system. |
| **Schedulers** | Scheduling policies determine which continuation is resumed next. |
| **Cooperative Multitasking** | Tasks voluntarily yield by transferring control to scheduler continuations. |
| **Preemptive Multitasking** | Execution continuations are externally interrupted, captured, and later resumed by a scheduler. |
| **Event-Driven Execution** | Event handlers are continuations triggered by event-dispatch transitions. |
| **Callbacks** | A callback is explicitly a continuation supplied to be invoked after an operation completes. |
| **Reactive Systems** | Reactive propagation chains can be represented as continuation activations triggered by state changes. |
| **Delimited Continuations** | Only a bounded portion of the continuation chain is captured and manipulated. |
| **Continuation Marks / Contexts** | Metadata is attached to continuations to represent dynamic execution context. |
| **Transactional Control** | Continuations can represent commit paths and rollback paths for transactional execution. |
| **Probabilistic Control** | Continuation selection occurs according to probabilistic transition policies. |
| **Search Trees** | Search branches correspond to stored continuations representing unexplored computational futures. |

## Usage

```python
def loop_cps(start, stop, continuation):
    if start > stop:  # Base case: stop recursion
        return
	  # here the lambda is the continuation
    continuation(start, lambda: loop_cps(start + 1, stop, continuation))

# Define a continuation that prints and calls the next step
def print_cont(value, next_cont):
    print(value)
    next_cont()  # Calls the next step in the loop

# Start the loop
loop_cps(1, 5, print_cont)
```

```racket
	(/ 1 1 (call-with-current-continuation 
	         (lambda (k) 
	           (k 3))))
```

## References

- https://en.wikipedia.org/wiki/Continuation
- [‣](https://app.notion.com/p/10e598edb79081b69b89fee7c47952ef?pvs=21)
- …