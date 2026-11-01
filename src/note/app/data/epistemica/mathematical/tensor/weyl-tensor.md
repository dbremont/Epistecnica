---
tags: [analytical, geometry, type]
---

# Weyl Tensor

> The **Weyl tensor** $C_{abcd}$ is the totally traceless part of the Riemann tensor: the piece of curvature that survives when every contraction vanishes, and the piece that travels.

## Formulation

> **What it is.** Riemann decomposes into a scalar part (the scalar curvature), a trace part (Ricci) and a traceless part (Weyl). Only Weyl is conformally invariant, and only Weyl is nonzero in vacuum — so it is the tensor that describes gravity where there is no matter.
>
> **Type.** A `Concept`; a derived [tensor field](tensor-field.md).
>
> **Boundary.** In fewer than four dimensions Weyl vanishes identically: three-dimensional gravity has no local degrees of freedom, which is why the subject changes character at $n = 4$.

## Key results

- **Decomposition.** $R_{abcd} = C_{abcd} + \frac{1}{n-2}(g_{a[c}R_{d]b} - g_{b[c}R_{d]a}) - \frac{R}{(n-1)(n-2)}g_{a[c}g_{d]b}$ — the algebraic split of curvature into its irreducible parts.
- **Conformal invariance.** $C$ is unchanged by conformal rescaling of the metric, so it measures shape distortion rather than size change.
- **Tidal forces.** The geodesic deviation equation is driven by Riemann, and in vacuum by Weyl alone: the tensor that stretches and squeezes freely falling bodies.
- **Gravitational waves.** Far from a source the field is pure Weyl, and the two propagating polarizations are its Newman–Penrose components $\Psi_4$ and $\Psi_0$.
- **Algebraic classification.** Petrov types classify spacetimes by the algebraic type of Weyl — the analogue of classifying a matrix by its Jordan form.

## References

- https://en.wikipedia.org/wiki/Weyl_tensor
- [Riemann Tensor](riemann-tensor.md) · [Ricci Tensor](ricci-tensor.md) · [Curvature](../geometry/curvature.md) · [Geodesic](../geometry/geodesic.md)
