---
tags: [linear-algebra, polynomial, mathematics]
---

# Characteristic Polynomial

> The **characteristic polynomial** of a square matrix $A$ is $p_A(\lambda) = \det(A - \lambda I)$; its roots are the [eigenvalues](eigenvalue.md) and its coefficients are the invariants of the map.

## Formulation

> **What it is.** A single polynomial that packages the spectrum: degree $n$, leading coefficient $(-1)^n$, and coefficients that are the elementary symmetric functions of the eigenvalues.
>
> **Type.** A `Construction` — an artifact computed from a linear map, not a property of one.
>
> **Boundary.** The polynomial depends on the matrix, not on the basis: similar matrices share it, which is what makes it an invariant rather than a coordinate artifact.

## Key results

- **Cayley–Hamilton.** Every matrix satisfies its own characteristic polynomial, $p_A(A) = 0$ — the theorem that turns the polynomial into a tool for computing powers and inverses.
- **Spectral packaging.** $\operatorname{tr} A$ is the coefficient of $\lambda^{n-1}$ and $\det A$ the constant term.
- **Minimal polynomial.** The monic polynomial of least degree annihilating $A$ divides $p_A$ and records the Jordan structure that $p_A$ alone does not.

## References

- https://en.wikipedia.org/wiki/Characteristic_polynomial
- [Cayley–Hamilton Theorem](../../construction/cayley-hamilton-theorem.md) · [Eigenvalue](eigenvalue.md) · [Determinant](determinant.md)
