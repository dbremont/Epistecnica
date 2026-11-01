---
tags: [linear-algebra, function]
---

# Determinant

> The **determinant** is the alternating multilinear function $\det: \mathbb{R}^{n\times n} \to \mathbb{R}$ that assigns to a square matrix the signed factor by which its linear map scales oriented volume.

## Formulation

> **What it is.** A single number summarizing three things at once: whether the map is invertible, how it scales volume, and how it orients space. $\det A = 0$ exactly when $A$ is singular.
>
> **Type.** A `Concept` — an `Epistemic Construction` about linear maps, computed by a `Transformation Rule` (row reduction, Laplace expansion).
>
> **Boundary.** It is defined for *square* matrices only; the rectangular generalization is the collection of minors, which is what [rank](rank.md) reads.

## Key results

- **Multiplicativity.** $\det(AB) = \det A \cdot \det B$ — the reason determinants turn a group homomorphism into a scalar one, and the reason $\mathrm{SL}(n)$ exists as the kernel `det = 1`.
- **Invertibility.** $A$ is invertible iff $\det A \neq 0$; $\det(A^{-1}) = 1/\det A$.
- **Change of variables.** The Jacobian determinant is the volume factor in the multivariate integral; this is where the determinant earns its keep in analysis.
- **Characteristic polynomial.** $\det(A - \lambda I)$ is the polynomial whose roots are the [eigenvalues](eigenvalue.md).
- **Volume.** $|\det A|$ is the volume of the parallelepiped spanned by the columns — the geometric reading that survives in any dimension.

## References

- https://en.wikipedia.org/wiki/Determinant
- [Matrix](matrix.md) · [Rank](rank.md) · [Eigenvalue](eigenvalue.md) · [Trace](trace.md)
