---
tags: [computational-entity, linguistic-abstraction]
---

# Function

- [Language Execution System](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-execution-system.md)

> The **function mechanism** enables the construction of a new **computational entity**, a ***function***, which packages a fragment of program description into a reusable abstraction. This entity defines a contract over inputs and outputs, hides internal state transitions, and generates a well-specified computational evolution each time it is applied.
> 

## Formulation

> **Note:** Computational entities can be analyzed from two complementary perspectives: (1) the *descriptions* that specify them, and  (2) the *computations* they *generate* when executed.
> 

A **function can be understood** simultaneously as:

- **Section of Computation**: A delimited region of a larger computational space, which when invoked establishes an initial substate, performs a transition sequence, and returns control with a final substate.
- **Module of a Description**: A compositional unit within the program’s syntactic/semantic structure, providing a named, parameterized, and reusable specification of behavior.
- **Abstract Unit of Computation**: A computation-producing operator: when supplied with arguments, it instantiates a new computational process according to its semantics and evaluation strategy.

## **Description**

> How to analyze the function from the program perspective?
> 

From the description standpoint, a function is a **syntactic and semantic abstraction** that includes:

- **A signature:** specifying parameter types, names, arity, and constraints.
- **A body:** a finite description that denotes the computation to be produced.
- **A contract:** preconditions, postconditions, invariants, and side-effect boundaries.
- **A compositional role:** how it interacts with the host language’s scoping, type system, and module system.

## **Computation**

> How to think about the function from the computation perspective?
> 

From the computational standpoint, a function denotes:

- **A computation schema:** a rule-governed transition pattern parameterized by input values.
- **An instantiation mechanism:** each invocation creates a new activation record, environment, or continuation—depending on the execution model.
- **A dynamic control structure:** functions induce control flow (calls, returns, recursion, mutual recursion) and shape the global computational trajectory.

## Interface

> How to interact with a function?
> 

### Parameter Passing Mechanism

Different models specify how arguments are bound to parameters and how evaluation interacts with state:

- **Call-by-value / call-by-sharing**: arguments evaluated before binding.
- **Call-by-reference**: parameters alias caller state locations.
- **Call-by-name / call-by-need**: arguments re-evaluated or memoized on demand.
- **Copy-in/copy-out**: used in some imperative and distributed languages.

### Local Environment

> See more in [Language Specification](note.html?n=technica/computation/language-system/conceptual-model-language-system/language-specification.md).
> 

The local environment determines the internal state configuration of a function:

- **Lexical vs dynamic scope**
- **Closure formation**
- **Frame layout** (stack frames, heap frames, register windows)
- **Lifetime rules** (automatic vs heap-allocated activations)

### Return Model

> How a function returns to its caller?
> 

The return model specifies:

- **Control transfer** (stack unwind, continuation invocation, coroutine yield)
- **Result passing** (registers, stack slots, value objects)
- **Tail-call semantics** (frame reuse vs frame creation)
- **Finalization guarantees** (RAII, `defer`, structured unwinding)

### Exceptional Control Flow

Exceptional control flow generalizes ordinary returns:

- **Synchronous exceptions** (runtime errors, assertion failures)
- **Asynchronous exceptions** (interrupts, cancellation)
- **Effect handlers** (algebraic effects, resumable exceptions)
- **Pattern-based unwinding** (matchable error values)

## QA

### What is a Lambda Expression?

> A **lambda expression** is an anonymous function expression used to define computational behavior inline, without explicitly declaring a named function.
> 

It typically captures:

- a set of parameters,
- a computation or expression body,
- and optionally a surrounding lexical environment (closure).

A lambda expression is commonly treated as a **first-class value**, meaning it can be:

- assigned to variables,
- passed as arguments,
- returned from functions,
- or stored in data structures.

Cases:

| Language | Example |
| --- | --- |
| Python | `lambda x: x + 1` |
| Java | `(x) -> x + 1` |
| JavaScript | `(x) => x + 1` |
| C# | `x => x + 1` |
| Haskell | `\x -> x + 1` |
| Scheme | `(lambda (x) (+ x 1))` |

## References

- https://en.wikipedia.org/wiki/Function_(computer_programming)
- [Recursion](note.html?n=technica/computation/algorithm/conceptual-model-algorithm/recursion.md)
- https://en.wikipedia.org/wiki/Tail_call