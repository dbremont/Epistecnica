---
tags: [linear-algebra]
---

# Dimension

> The **dimension** of a vector space is the cardinality of any [basis](basis.md) of it — a number the space forces, not a choice anyone makes.

## Formulation

> **What it is.** The invariant that says how many independent directions a space has. Finite dimension is the regime of matrices; infinite dimension is the regime of function spaces, where the algebra of [linear operators](linear-operator.md) becomes analysis.
>
> **Type.** A `Concept` — a cardinal invariant of a structure.
>
> **Boundary.** The word is overloaded across mathematics: the dimension of a manifold, of a fractal (Hausdorff), of a variety (Krull) and of a vector space agree only in the nicest cases. This note is the linear-algebra sense.

## Key results

- **Basis invariance.** Every basis of a space has the same cardinality — the theorem that makes dimension well defined, proved by the Steinitz exchange lemma.
- **Subspace bounds.** For $U \le V$, $\dim U \le \dim V$, with equality only if $U = V$ in the finite case.
- **Rank–nullity.** $\dim \ker A + \operatorname{rank} A = \dim V$ — dimension is conserved across a linear map.
- **Infinite dimension.** A space is infinite-dimensional iff it contains an infinite linearly independent set; [Hilbert](../../space/hilbert-space.md) and [Banach](../../space/banach-space.md) spaces are the analytic instances.

## References

- https://en.wikipedia.org/wiki/Dimension_(vector_space)
- [Basis](basis.md) · [Rank](rank.md) · [Hilbert Space](../../space/hilbert-space.md)
