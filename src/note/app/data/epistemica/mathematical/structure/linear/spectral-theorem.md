---
tags: [linear-algebra, theorem, operator, mathematics]
---

# Spectral Theorem

> The **spectral theorem** states that a self-adjoint operator on an inner-product space admits an orthonormal basis of eigenvectors with real eigenvalues — so it is diagonal in that basis.

## Formulation

> **What it is.** The structural theorem of linear algebra: it says that the symmetric case is as simple as a diagonal matrix. Every statement of the form "diagonalize by rotating" — principal axes, normal modes, PCA, quantum observables — is an instance of it.
>
> **Type.** A `Construction` of the kind `Theory` — a stated result, not a routine. The [method scope](../../method/method.md) holds the routines that compute it.
>
> **Boundary.** The hypothesis is self-adjointness. For a general matrix the orthogonal diagonalization fails and one gets the Jordan form instead; for a normal matrix ($A A^* = A^* A$) it survives over $\mathbb{C}$.

## Key results

- **Real spectrum.** A self-adjoint operator has real eigenvalues — the reason observables in quantum mechanics are self-adjoint.
- **Orthonormal eigenbasis.** Eigenvectors belonging to distinct eigenvalues are orthogonal, and the whole space decomposes as a direct sum of eigenspaces.
- **Spectral decomposition.** $A = \sum_i \lambda_i P_i$ with $P_i$ orthogonal projections — the finite-dimensional shadow of the projection-valued measure in the infinite case.
- **Unbounded case.** On a Hilbert space the theorem extends to unbounded self-adjoint operators, where it becomes the spectral integral $A = \int \lambda \, dE_\lambda$.

## References

- https://en.wikipedia.org/wiki/Spectral_theorem
- [Eigenvalue](eigenvalue.md) · [Self-Adjoint Operator](self-adjoint-operator.md) · [Spectrum](../../spectrum.md) · [Hilbert Space](../../space/hilbert-space.md)
