---
tags: [note, mathematics, topology, algebraic]
---

# Fundamental Group

> The **fundamental group** $\pi_1(X, x_0)$ is the set of loops based at $x_0$ up to homotopy, with concatenation as the operation — the first algebraic invariant of a space.

## Formulation

> **What it is.** The group that records the *holes* of a space in a way homology cannot: it sees the difference between the circle and the sphere, and between spaces that are homotopy equivalent but not homeomorphic.
>
> **Type.** A `Concept` — a functor from pointed spaces to groups (see [category](../structure/category.md)); each continuous map induces a homomorphism, and that is what makes it computable.
>
> **Boundary.** It depends on the basepoint only up to conjugation, so for path-connected spaces one writes $\pi_1(X)$ up to isomorphism. It is non-abelian in general, unlike homology, which is why it carries strictly more information.

## Key results

- **Functoriality.** A continuous $f: X \to Y$ gives $\pi_1(f): \pi_1(X) \to \pi_1(Y)$, and homotopic maps give conjugate homomorphisms — the invariant is a functor, not a function.
- **Van Kampen.** The fundamental group of a union is the amalgamated free product of the pieces over their intersection — the computation theorem.
- **Circle and spheres.** $\pi_1(S^1) \cong \mathbb{Z}$ and $\pi_1(S^n) = 0$ for $n \ge 2$; the first fact is the winding number, the second is why higher spheres are simply connected.
- **Covering spaces.** Loops lift to paths, and the subgroups of $\pi_1$ correspond to [covering spaces](covering-space.md) — the Galois correspondence of topology.
- **Brouwer.** No retraction of the disk onto its boundary, hence the fixed-point theorem — proved by $\pi_1$.

## References

- https://en.wikipedia.org/wiki/Fundamental_group
- [Homotopy](homotopy.md) · [Covering Space](covering-space.md) · [Homology](homology.md) · [Category](../structure/category.md)
