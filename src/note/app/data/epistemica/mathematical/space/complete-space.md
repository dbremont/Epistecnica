---
tags: [space, analytical]
---

# Complete Space

> A metric space is **complete** when every Cauchy sequence converges in it: the space has no holes, because every sequence that should converge does.

## Formulation

> **What it is.** The property that separates the real numbers from the rationals, and a [Banach space](banach-space.md) from a mere normed space. It is what makes the contraction-mapping and fixed-point theorems work: iterations converge because their limit is guaranteed to exist inside the space.
>
> **Type.** A `Concept` — a property of a metric structure, checked sequence by sequence.
>
> **Boundary.** Completeness is metric, not topological: $\mathbb{R}$ and $(0,1)$ are homeomorphic but only the first is complete. The topological shadow is complete metrizability, and the invariant form is Baire category.

## Key results

- **Completion.** Every metric space embeds isometrically and densely into a unique complete one — the construction that builds $\mathbb{R}$ from $\mathbb{Q}$ and $L^p$ from simple functions.
- **Banach fixed point.** A contraction on a complete metric space has a unique fixed point — see the [fixed-point construction](../construction/banach-fixed-point-theorem.md).
- **Baire category.** A complete metric space is not a countable union of nowhere-dense sets; this is the source of most existence theorems without construction.
- **Nested sets.** A decreasing sequence of closed sets with diameters going to zero has a non-empty intersection exactly in the complete case.

## References

- https://en.wikipedia.org/wiki/Complete_metric_space
- [Metric Space](metric-space.md) · [Banach Space](banach-space.md) · [Banach Fixed-Point Theorem](../construction/banach-fixed-point-theorem.md) · [Cauchy Sequence](../change/cauchy-sequence.md)
