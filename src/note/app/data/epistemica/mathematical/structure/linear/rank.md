---
tags: [linear-algebra]
---

# Rank

> The **rank** of a linear map is the dimension of its image: the number of independent directions the map actually reaches.

## Formulation

> **What it is.** The single integer that measures how much of the codomain a map can produce. $\operatorname{rank} A = \dim \operatorname{im} A$, equal to the number of nonzero rows in a row-echelon form and to the largest order of a non-vanishing minor.
>
> **Type.** A `Concept` — a numerical invariant of a linear map.
>
> **Boundary.** Rank is not a property of the matrix entries but of the map; row operations change the entries and preserve the rank, which is why elimination is the standard computation.

## Key results

- **Rank–nullity.** $\dim \ker A + \operatorname{rank} A = n$ — the conservation law of linear maps, and the reason a square matrix is invertible exactly when its rank is full.
- **Solvability.** $Ax = b$ has a solution iff $\operatorname{rank} A = \operatorname{rank}[A \mid b]$ (Rouché–Capelli).
- **Low-rank approximation.** The [SVD](singular-value-decomposition-svd.md) truncates to rank $k$ and gives the best approximation in the Frobenius norm — the theorem behind PCA and dimensionality reduction.
- **Rank and determinant.** $\operatorname{rank} A = n$ iff $\det A \neq 0$ for a square $A$.

## References

- https://en.wikipedia.org/wiki/Rank_(linear_algebra)
- [Basis](basis.md) · [Dimension](dimension.md) · [Singular Value Decomposition](singular-value-decomposition-svd.md) · [Determinant](determinant.md)
