---
tags: [concept]
---

# Currying


> **Currying** is a systematic transformation that takes a function of multiple arguments and converts it into a chain of single-argument functions.
> 

> Formally, for any function $f : X \times Y \times \cdots \times Z \to W,$  currying produces a function  $f_c : X \to (Y \to (\cdots \to (Z \to W)))$.
> 

> This means that instead of providing all arguments at once, you provide the first argument to get back a function waiting for the next argument, and so on, until all arguments are supplied, and the final result is produced.
> 

## References

- https://en.wikipedia.org/wiki/Currying