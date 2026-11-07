---
tags: [mathematics, structure, algebraic]
---

# Duality

> **Duality** is the pattern in which every object of a kind has a partner — its dual — such that statements about the object become statements about the partner, with the arrows reversed, and applying the operation twice returns the original.

## Formulation

> **What it is.** A translation principle, not a single construction. Vector spaces have [dual spaces](../space/dual-vector-space.md); linear programs have dual programs; categories have opposite categories; projective geometry has points and lines exchanged. In each case a theorem proved once yields its dual for free.
>
> **Type.** A `Concept` — a structural pattern that recurs across branches.
>
> **Boundary.** Duality is not analogy: a genuine duality comes with a *contravariant* map that is involutive up to natural isomorphism, and a theorem that the two readings agree. Without that, "duality" is a metaphor.

## The dualities worth knowing

| Domain | Object | Dual | What the duality buys |
| --- | --- | --- | --- |
| Linear algebra | vector space $V$ | $V^* = \mathrm{Hom}(V, k)$ | Coordinates as functionals; the [dual basis](../structure/linear/basis.md) |
| Analysis | function space | its dual of measures/distributions | [Weak convergence](../space/weak-convergence.md), [distributions](../mapping/generalized-function.md) |
| Optimization | primal problem | [dual problem](../method/certify/convex-duality.md) | Certificates of optimality; strong duality for convex problems |
| Category theory | category $C$ | $C^{op}$ | Every statement has a free dual — see [category](category.md) |
| Projective geometry | points | hyperplanes | Theorems about incidence come in pairs |
| Logic | formula | its negation | De Morgan, quantifier duality |
| Fourier analysis | space | frequency space | Convolution becomes multiplication |

## Key results

- **Double dual.** For finite-dimensional spaces $V \cong V^{**}$ canonically; for infinite-dimensional ones this fails, and the gap is exactly what reflexivity names.
- **Fenchel–Moreau.** A convex function equals its biconjugate iff it is closed — the analytic form of the double-dual identity.
- **Pontryagin duality.** Locally compact abelian groups are self-dual under the character group, and the Fourier transform is the map that realizes it.

## References

- https://en.wikipedia.org/wiki/Duality_(mathematics)
- [Dual Vector Space](../space/dual-vector-space.md) · [Category](category.md) · [Convex Duality](../method/certify/convex-duality.md) · [Weak Convergence](../space/weak-convergence.md)
