---
tags: [paper]
---

# Cardelli, L. (1996). Type Systems.


```bash

```

## Notes

---

> **Type System Goal**:  The fundamental purpose of a **type system** is to prevent the occurrence of **execution errors** during the running of a program.
> 

> What constitutes an **execution error** in **type system theory**? An execution error in type system theory occurs when a program attempts to perform an operation on data of an incompatible type, leading to failures during compilation or runtime exceptions.
> 

> **Type unsound** a program  crash even though it is **judged acceptable** by a **typechecker** .
> 

> A **type system language spec** makes the compiler/interpreter easier / and **not diverge** in the type system implementation.
> 

> …
> 

**Expected properties of type systems**

- **Type systems** should be `decidably` verifiable: an algorithm (called a type-checking algorithm) can ensure that a program is well-behaved.
- **Type systems** should be transparent: a programmer should be able to predict easily whether a program will `typecheck`.
- **Type systems** should be enforceable: type declarations should be statically checked as much as possible and otherwise dynamically checked.

## References

- Cardelli, L. (1996). Type Systems. 28(1), 263–264.
