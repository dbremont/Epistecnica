---
tags: [mathematics, analytical, geometry, type]
---

# Einstein Tensor

> The **Einstein tensor** $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu}$ combines the Ricci tensor and the scalar curvature into the unique divergence-free symmetric two-tensor built from second derivatives of the metric.

## Formulation

> **What it is.** The left-hand side of Einstein's field equation. Its defining property — $\nabla^\mu G_{\mu\nu} = 0$ — is a geometric identity (contracted Bianchi), and it is exactly what lets it equal a conserved source.
>
> **Type.** A `Concept`; a derived [tensor field](tensor-field.md).
>
> **Boundary.** It is not "the curvature": it is the traceless-free combination that general covariance forces. Adding a cosmological constant $\Lambda g_{\mu\nu}$ preserves the divergence-free property, which is why that extension is admissible.

## Key results

- **Einstein's equation.** $G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}$ — geometry on the left, [stress-energy](stress-energy-tensor.md) on the right.
- **Conservation for free.** $\nabla^\mu G_{\mu\nu} = 0$ identically, so the source must satisfy $\nabla^\mu T_{\mu\nu} = 0$ — energy-momentum conservation is not an extra assumption.
- **Trace.** $G = -R$ in four dimensions, so the equation can be rewritten as $R_{\mu\nu} = 8\pi G (T_{\mu\nu} - \tfrac12 T g_{\mu\nu})$ — the form used in practice.
- **Vacuum.** $T_{\mu\nu} = 0$ gives $R_{\mu\nu} = 0$; the Schwarzschild solution is the spherically symmetric case.
- **Uniqueness.** Lovelock's theorem: in four dimensions this is the only symmetric divergence-free two-tensor built from the metric and its first two derivatives.

## References

- https://en.wikipedia.org/wiki/Einstein_tensor
- https://en.wikipedia.org/wiki/Einstein_field_equations
- [Ricci Tensor](ricci-tensor.md) · [Metric Tensor](metric-tensor.md) · [Stress-Energy Tensor](stress-energy-tensor.md) · [Riemann Tensor](riemann-tensor.md)
