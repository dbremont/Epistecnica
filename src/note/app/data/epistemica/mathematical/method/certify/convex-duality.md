---
tags: [method, technique, optimization, mathematics]
---

# Convex Duality

> **Convex duality** pairs a convex minimization problem with a maximization problem over dual variables, such that the two optima coincide under a constraint qualification and the dual gives a certificate of optimality.

## Formulation

> **What it is.** The Lagrangian $L(x,\lambda) = f(x) + \lambda^\top g(x)$ turns a constrained problem into an unconstrained one at a price: the multiplier. Maximizing the Lagrangian's infimum over $\lambda$ yields the dual; the gap between primal and dual measures how badly the constraint bites.
>
> **Type.** An `Epistemic Method` — a routine for producing bounds and certificates — built on the [duality pattern](../../structure/duality.md).
>
> **Boundary.** Without convexity there is a duality gap; with convexity and Slater's condition the gap closes. Lagrange multipliers are the local, equality-constrained case; this is the global, inequality-constrained one.

## Key results

- **Weak duality.** The dual optimum is always a lower bound for the primal — true with no assumptions, and the reason duals are used for certification.
- **Strong duality.** For convex problems satisfying Slater's condition, primal and dual optima coincide.
- **KKT conditions.** Primal feasibility, dual feasibility, complementary slackness and stationarity — necessary and, under convexity, sufficient.
- **Fenchel duality.** $\inf_x f(x) + g(Ax) = -\inf_{y} f^*(-A^\top y) + g^*(y)$ in terms of conjugates — the analytic form of [double duality](../../structure/duality.md).
- **Linear programming.** The LP dual is the special case, and Farkas' lemma is its separation theorem.

## References

- https://en.wikipedia.org/wiki/Duality_(optimization)
- [Optimization](../../../optimization/optimization.md) · [Lagrange Multiplier](../../../optimization/lagrange-multiplier.md) · [Convexity](../../convexity.md) · [Duality](../../structure/duality.md)
