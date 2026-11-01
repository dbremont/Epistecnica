---
tags: [topology]
---

# Covering Space

> A **covering space** of $X$ is a space $\tilde X$ with a map $p: \tilde X \to X$ that is locally a homeomorphism onto $X$: every point of $X$ has a neighbourhood evenly covered by sheets of $\tilde X$.

## Formulation

> **What it is.** The geometric form of "unwrapping": the real line covers the circle, the plane covers the torus, the sphere covers the projective plane. Paths and homotopies lift, so a question on $X$ becomes a question on the simpler $\tilde X$.
>
> **Type.** A `Concept` — a morphism of spaces with a local triviality condition; it is the topological case of a [bundle](../geometry/bundle.md).
>
> **Boundary.** Coverings are discrete-fibre bundles: the fibre is a set, not a vector space. The universal cover is the simply connected one, and it exists whenever $X$ is connected, locally path-connected and semilocally simply connected.

## Key results

- **Lifting.** A path in $X$ lifts uniquely once a starting point is chosen; a homotopy lifts once one end is fixed. This is the engine of every argument in the subject.
- **Galois correspondence.** Connected coverings of $X$ correspond to subgroups of $\pi_1(X)$: the universal cover to the trivial subgroup, the cover itself to the image of $\pi_1(\tilde X)$.
- **Deck transformations.** The group of automorphisms of a cover is $\pi_1(X)/\pi_1(\tilde X)$, and for the universal cover it is $\pi_1(X)$ itself.
- **Universal cover.** $\mathbb{R} \to S^1$ is the model case: the winding number of a loop is its endpoint in the cover.

## References

- https://en.wikipedia.org/wiki/Covering_space
- [Fundamental Group](fundamental-group.md) · [Homotopy](homotopy.md) · [Bundle](../geometry/bundle.md) · [Manifold](manifold.md)
