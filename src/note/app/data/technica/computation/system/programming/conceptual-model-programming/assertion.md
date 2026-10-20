# Assertion


> **An Exploration of Assertions in the Context of Programming.**
> 

## Formulation

> What is an **Assertion**? An assertion is an executable predicate over program state, evaluated at runtime (or verified statically), whose falsity signals a violation of an intended invariant or pre/postcondition.
> 

> What is the **technical nature** of an Assertion? Assertions exist at the boundary between static verification and dynamic execution.
> 

## Implementation

> What are the possible **implementations** of an Assertion?
> 

| **Strategy** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Runtime Assertion (Dynamic Check)** | Boolean predicate evaluated at runtime; failure triggers abort, exception, or trap. Often removable in production builds. | `assert()` in C · `assert` in Java · `assert` in Python · `Debug.Assert` in C# |
| **Compile-Time Assertion (Static Assertion)** | Predicate evaluated at compile time; compilation fails if false. Zero runtime overhead. | `_Static_assert` in C · `static_assert` in C++ |
| **Design-by-Contract (DbC)** | Explicit preconditions, postconditions, and invariants attached to program units; may be checked dynamically or statically. | Native contracts in Eiffel · Contract libraries in C# · Annotation-based contracts in Java |
| **Type-System Encoded Assertion** | Invariants encoded in the type system so invalid states are unrepresentable. Moves checks to compile time. | Non-nullable types in C# · `Optional` in Java · Ownership/borrowing guarantees in Rust |
| **Macro-Based / Conditional Assertion** | Assertions included or excluded via preprocessing or build configuration. | `#ifdef DEBUG` patterns in C · Conditional compilation in C++ |
| **Exception-Based Assertion** | Logical guard implemented explicitly with exception throwing; typically always active. | `IllegalStateException` in Java · `InvalidOperationException` in C# |
| **Formal Verification Assertion** | Assertions expressed in a formal specification language and discharged by static proof tools. | Contracts in Ada (SPARK subset) · Specification systems for C |
| **Kernel / Low-Level Assertion** | Critical invariant enforcement at systems level; violation may trigger panic or halt. | `BUG()` / `WARN_ON()` in the Linux kernel |

## Usage

> What is the **criteria model** that should guide the use of Assertions?
> 

### Guiding Questions

- Is this condition logically impossible if the program is correct?
- Is violation indicative of programmer error?
- Is recovery meaningful?
- Can this invariant be moved to compile-time?
- Is the runtime cost acceptable?
- Does this cross a trust boundary?
- What is the cost model of assertions?

### Ideal Assertion Locations

- After state transitions
- After mutation of core data structures
- Before/after critical algorithmic phases
- On boundary of abstraction layers
- Inside “default” or “unreachable” branches

## Against Use

- Using assertions for user validation
- Catching assertion failures
- Logging and continuing after assertion failure
- Using assertions as feature flags
- Placing assertions with side effects

## References

- https://news.ycombinator.com/item?id=7250571
- https://news.ycombinator.com/item?id=23914153
- https://en.wikipedia.org/wiki/Assertion_(software_development)
- https://news.ycombinator.com/item?id=17880722
- https://en.wikipedia.org/wiki/Crash-only_software
- https://news.ycombinator.com/item?id=40212967
- https://www.usenix.org/conference/hotos-ix/crash-only-software
- https://stackoverflow.com/questions/17732/when-should-assertions-stay-in-production-code