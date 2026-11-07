---
tags: [linear-algebra, spectrum, mathematics]
---

# Eigenvalue

> An **eigenvalue** of a linear map $A$ is a scalar $\lambda$ for which there is a nonzero vector $v$ with $Av = \lambda v$: a direction the map leaves fixed up to scale.

## Formulation

> **What it is.** The scalar half of a stationary pair; the [eigenvector](eigenvector.md) is the direction, the eigenvalue the stretch. Together they say where a linear map acts as a scaling and nowhere else.
>
> **Type.** A `Concept` — a constructed discriminator of a linear map's behaviour.
>
> **Boundary.** Eigenvalues exist only when solutions of $\det(A - \lambda I) = 0$ exist in the field; over $\mathbb{R}$ a rotation has none, over $\mathbb{C}$ it always has $n$ counted with multiplicity. This is the algebraic-closure distinction, not a modelling choice.

## Key results

- **Characteristic polynomial.** The eigenvalues are the roots of $\det(A - \lambda I)$; there are exactly $n$ over $\mathbb{C}$, counted with algebraic multiplicity.
- **Trace and determinant.** $\operatorname{tr} A = \sum \lambda_i$ and $\det A = \prod \lambda_i$ — the shortest bridge between the matrix and its spectrum.
- **Diagonalization.** $A$ is diagonalizable iff it has $n$ independent eigenvectors; symmetric real matrices always are — see the [spectral theorem](spectral-theorem.md).
- **Stability.** In a [dynamical system](../../change/dynamical-system.md), the eigenvalues of the linearization decide whether a fixed point attracts or repels: $\operatorname{Re}\lambda < 0$ is stable.
- **Spectrum.** For operators on infinite-dimensional spaces the eigenvalue notion generalizes to the [spectrum](../../spectrum.md), where $\lambda I - A$ may fail to be invertible without ever vanishing on a vector.

## References

- https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
- [Eigenvector](eigenvector.md) · [Characteristic Polynomial](characteristic-polynomial.md) · [Spectral Theorem](spectral-theorem.md) · [Spectrum](../../spectrum.md)
