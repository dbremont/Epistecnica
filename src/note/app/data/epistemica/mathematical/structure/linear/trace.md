---
tags: [linear-algebra]
---

# Trace

> The **trace** of a square matrix is the sum of its diagonal entries, $\operatorname{tr} A = \sum_i a_{ii}$ — an apparently coordinate-dependent number that is in fact a basis-independent invariant.

## Formulation

> **What it is.** The unique (up to scale) linear functional on matrices that is invariant under cyclic permutation: $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
>
> **Type.** A `Concept` — the linear functional that makes the space of operators into an inner-product space.
>
> **Boundary.** It is defined for finite-dimensional endomorphisms; on infinite-dimensional spaces the naive sum diverges, and the replacement is the trace-class condition.

## Key results

- **Cyclicity.** $\operatorname{tr}(ABC) = \operatorname{tr}(BCA)$, hence invariance under similarity: $\operatorname{tr}(P^{-1}AP) = \operatorname{tr} A$.
- **Spectrum.** $\operatorname{tr} A = \sum_i \lambda_i$ — the trace is the first symmetric function of the eigenvalues.
- **Frobenius inner product.** $\langle A, B\rangle = \operatorname{tr}(A^\top B)$ turns matrices into a Hilbert space; this is the inner product behind least squares and the [Gram matrix](gram-matrix.md).
- **Divergence.** The trace of the Jacobian is the divergence of a vector field — the bridge from linear algebra to the [divergence operator](../../change/divergence-operator.md).

## References

- https://en.wikipedia.org/wiki/Trace_(linear_algebra)
- [Determinant](determinant.md) · [Eigenvalue](eigenvalue.md) · [Gram Matrix](gram-matrix.md)
