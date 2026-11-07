---
tags: [mathematics, method, technique, analytical]
---

# Compactness Argument

> A **compactness argument** proves existence by extracting a convergent subsequence: from a bounded family one selects a subsequence that converges, and the limit is shown to be the object sought.

## Formulation

> **What it is.** The routine behind most existence theorems in analysis: bound the approximating sequence, extract a convergent subsequence by compactness, pass to the limit. The theorem being invoked is Bolzano–Weierstrass, Arzelà–Ascoli, Banach–Alaoglu or Tychonoff, depending on the setting.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** The extraction is weak: it gives a [weakly convergent](../../space/weak-convergence.md) subsequence, not a norm-convergent one, so the limit must be shown to satisfy the equation — that is where lower semicontinuity and the direct method of the calculus of variations come in.

## Key results

- **Bolzano–Weierstrass.** A bounded sequence in $\mathbb{R}^n$ has a convergent subsequence — the finite-dimensional model case.
- **Arzelà–Ascoli.** A uniformly bounded, equicontinuous family of functions has a uniformly convergent subsequence — the compactness theorem of function spaces.
- **Banach–Alaoglu.** The unit ball of a dual space is weak-* compact — the infinite-dimensional replacement, and the existence engine of variational problems.
- **The direct method.** Minimize a coercive, lower semicontinuous functional: bounded minimizing sequence, weak limit, semicontinuity gives the minimizer.
- **Finite subcover.** The topological form: from an open cover take a finite subcover, and the local property becomes global.

## References

- https://en.wikipedia.org/wiki/Compact_space
- https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem
- [Compact Space](../../topology/topology.md) · [Weak Convergence](../../space/weak-convergence.md) · [Complete Space](../../space/complete-space.md) · [Extremal Principle](../proof/extremal-principle.md)
