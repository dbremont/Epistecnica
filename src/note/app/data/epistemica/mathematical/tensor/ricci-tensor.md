---
tags: [analytical, geometry, type]
---

# Ricci Tensor

> The **Ricci tensor** $\mathrm{Ric}_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$ is the trace of the Riemann tensor: the average of sectional curvatures over the directions orthogonal to a given one.

## Formulation

> **What it is.** The first contraction of [Riemann](riemann-tensor.md), and the piece that survives when Weyl is removed. It measures how volumes distort — a ball of freely falling particles shrinks or grows at a rate governed by Ricci — where Weyl measures how shapes shear.
>
> **Type.** A `Concept`; a derived [tensor field](tensor-field.md).
>
> **Boundary.** Ricci is not the full curvature: in four dimensions it has 10 independent components against Riemann's 20, and the missing 10 are exactly Weyl. Two spacetimes with the same Ricci can have entirely different tidal structure.

## Key results

- **Definition.** $\mathrm{Ric}_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, symmetric by the symmetries of Riemann.
- **Scalar curvature.** $R = g^{\mu\nu}\mathrm{Ric}_{\mu\nu}$ — the second, complete contraction.
- **Einstein's equation.** $\mathrm{Ric}_{\mu\nu} - \tfrac12 R g_{\mu\nu} = 8\pi G\,T_{\mu\nu}$; equivalently $\mathrm{Ric}_{\mu\nu}$ equals the stress-energy up to its trace (see [Einstein tensor](einstein-tensor.md)).
- **Volume distortion.** $\ddot{V}/V = -\mathrm{Ric}_{\mu\nu}u^\mu u^\nu$ along a geodesic congruence — the Raychaudhuri equation, and the reason positive Ricci focuses.
- **Ricci flow.** $\partial_t g_{\mu\nu} = -2\mathrm{Ric}_{\mu\nu}$ deforms the metric by its own Ricci curvature; Perelman's use of it proved the geometrization conjecture. See [Ricci flow](../ricci-flow.md).

## References

- https://en.wikipedia.org/wiki/Ricci_curvature
- [Riemann Tensor](riemann-tensor.md) · [Einstein Tensor](einstein-tensor.md) · [Weyl Tensor](weyl-tensor.md) · [Ricci Flow](../ricci-flow.md) · [Curvature](../geometry/curvature.md)
