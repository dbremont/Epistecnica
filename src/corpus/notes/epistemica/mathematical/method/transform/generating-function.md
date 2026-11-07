---
tags: [note, mathematics, method, technique, discrete]
---

# Generating Function

> A **generating function** encodes a sequence $(a_n)$ as the coefficients of a formal power series $A(x) = \sum_n a_n x^n$, turning a combinatorial problem into an algebraic one.

## Formulation

> **What it is.** A routine that converts recurrence and counting into algebra: multiplying series becomes convolution of sequences, so the coefficient you want is the coefficient of a product, a quotient, or a composition. The sequence is the data; the series is the computation.
>
> **Type.** An `Epistemic Method` — a generalized routine — not a rule. The algebra it runs on is the [algebraic representational system](../../structure/algebra/algebra.md); the objects it counts live in the [discrete scope](../../discrete/combinatorics.md).
>
> **Boundary.** It is not the probability-side [moment-generating](../../../observational/probability/moment-generating-function-mgf.md) or [probability-generating](../../../observational/probability/probability-generating-function-pgf.md) function: those are analytic objects used for distributions. This is the combinatorial technique, and it works in a formal ring where convergence is irrelevant.

## Key results

- **Ordinary generating functions.** $A(x)B(x)$ has coefficients $\sum_k a_k b_{n-k}$ — convolution becomes multiplication.
- **Fibonacci and friends.** A linear recurrence becomes a rational function, and the closed form is a partial-fraction expansion: $F_n$ from $x/(1-x-x^2)$.
- **Exponential generating functions.** $\sum a_n x^n/n!$ makes labelled structures multiply — the standard tool for permutations and set constructions.
- **Catalan numbers.** $C(x) = 1 + xC(x)^2$ gives $C_n = \frac{1}{n+1}\binom{2n}{n}$ — the prototype of a specification solved algebraically.
- **Analytic combinatorics.** When the series converges, singularity analysis yields asymptotics — the bridge from counting to analysis.

## References

- https://en.wikipedia.org/wiki/Generating_function
- [Combinatorics](../../discrete/combinatorics.md) · [Binomial Coefficient](../../discrete/binomial-coefficient.md) · [Catalan Number](../../discrete/catalan-number.md) · [Recurrence Equation](../../change/recurrence-equation.md)
