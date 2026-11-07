---
tags: [note, mathematics, method, technique, analytical]
---

# Perturbation Method

> A **perturbation method** solves a problem that has no closed form by expanding its solution in a small parameter, order by order: the unperturbed problem is solved exactly, and each correction solves a linear problem built from the previous orders.

## Formulation

> **What it is.** The routine of the small parameter. Write the solution as $x = x_0 + \varepsilon x_1 + \varepsilon^2 x_2 + \cdots$, substitute, and equate powers of $\varepsilon$; each order is a problem one step easier than the last.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** The expansion is asymptotic, not convergent: it approximates for small $\varepsilon$ and may diverge for any fixed $\varepsilon$. A *singular* perturbation — where the small parameter multiplies the highest derivative — breaks the naive expansion and needs boundary layers.

## Key results

- **Regular perturbation.** The expansion is uniformly valid; the error is $O(\varepsilon^{N+1})$ after $N$ orders.
- **Singular perturbation.** The limit $\varepsilon \to 0$ changes the order of the equation, so the solution develops a boundary layer; matched asymptotic expansions patch an inner and an outer solution.
- **Secular terms.** Naive expansion of an oscillator produces terms growing without bound; multiple-scale analysis removes them by letting the amplitude depend on a slow time.
- **WKB.** For $\varepsilon y'' + q(x)y = 0$ the expansion is exponential, not polynomial — the method's most important variant.
- **Adjoint solvability.** At each order, solvability requires the correction to be orthogonal to the null space of the adjoint — the Fredholm alternative appearing inside the routine.

## References

- https://en.wikipedia.org/wiki/Perturbation_theory
- [Asymptotic Analysis](asymptotic-analysis.md) · [Linearization](../reduction/linearization.md) · [Stationary Phase](stationary-phase.md) · [Differential Equation](../../change/differential-equation.md)
