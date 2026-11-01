---
tags: [method, technique, analytical]
---

# Contraction Mapping

> A **contraction mapping** is a map $T$ on a metric space with $d(Tx, Ty) \le q\,d(x,y)$ for some $q < 1$. On a complete space it has exactly one fixed point, and iteration from any starting point converges to it.

## Formulation

> **What it is.** The existence-and-uniqueness routine. It does two jobs at once: it proves a solution exists, and it gives the algorithm that finds it — iterate. That combination is why it is the most used fixed-point theorem in analysis.
>
> **Type.** An `Epistemic Method`; its warrant is the [Banach fixed-point theorem](../../construction/banach-fixed-point-theorem.md) on a [complete space](../../space/complete-space.md).
>
> **Boundary.** The contraction constant must be strictly below one, uniformly. A merely non-expansive map ($q = 1$) can fail to have a fixed point (a translation), and a contraction on an incomplete space can push its fixed point out of the space.

## Key results

- **Picard–Lindelöf.** An ODE with a Lipschitz right-hand side has a unique local solution — proved by contracting the integral operator.
- **Error bound.** $d(x_n, x^*) \le \frac{q^n}{1-q}d(x_1, x_0)$ — the convergence rate is geometric and known in advance.
- **Implicit function theorem.** The inverse and implicit function theorems are contraction arguments on a suitable complete space of functions.
- **Iterative solvers.** Fixed-point iteration, Jacobi and Gauss–Seidel are contraction methods; their convergence is exactly the contraction condition.
- **Reinforcement learning.** Discounted value iteration is a contraction in the sup-norm with $q = \gamma$ — the same theorem, another field.

## References

- https://en.wikipedia.org/wiki/Contraction_mapping
- [Banach Fixed-Point Theorem](../../construction/banach-fixed-point-theorem.md) · [Complete Space](../../space/complete-space.md) · [Iterative Method](../approximation/iterative-method.md) · [Fixed Point](../../change/fixed-point.md)
