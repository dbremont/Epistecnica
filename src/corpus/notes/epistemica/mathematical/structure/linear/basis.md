---
tags: [note, mathematics, linear-algebra]
---

# Basis

> A **basis** of a vector space is a set of vectors that is both linearly independent and spanning: every vector is a unique finite linear combination of its elements.

## Formulation

> **What it is.** The minimal generating set, and equivalently the maximal independent one. A basis is the choice that turns an abstract vector into coordinates — the [coordinate system](../../coordinate-system.md) of linear algebra.
>
> **Type.** A `Concept` — a constructed discriminator of a vector space's structure.
>
> **Boundary.** A basis is never canonical: every non-trivial space has many, and the choice is a convention. The exception is the canonical basis of $\mathbb{R}^n$, which is canonical only because the standard coordinates were chosen first.

## Key results

- **Uniqueness of coordinates.** Every vector has exactly one expansion in a given basis; this is what makes "the coordinates of $v$" well defined.
- **Existence.** Every vector space has a basis; for infinite-dimensional spaces this needs the [axiom of choice](note.html?p=notes/epistemica/epistemic/theory/foundation/axiom-of-choice.md) in the form of Zorn's lemma.
- **Dimension.** All bases of a space have the same cardinality — see [dimension](dimension.md).
- **Change of basis.** The matrix $P$ whose columns are the new basis vectors converts coordinates, and similarity $P^{-1}AP$ is what "the same map in another basis" means.

## References

- https://en.wikipedia.org/wiki/Basis_(linear_algebra)
- [Dimension](dimension.md) · [Span](span.md) · [Linear Map](linear-map.md) · [Coordinate System](../../coordinate-system.md)
