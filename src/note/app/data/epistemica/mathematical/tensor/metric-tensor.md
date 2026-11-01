---
tags: [analytical, geometry, type]
---

# Metric Tensor

> The **metric tensor** $g_{\mu\nu}$ is the symmetric tensor field that assigns an inner product to each tangent space: it defines lengths, angles and volumes, and it is the object that turns a manifold into a Riemannian one.

## Formulation

> **What it is.** The generalization of the dot product to curved space. Distance along a curve is $\int\sqrt{g_{\mu\nu}\dot x^\mu \dot x^\nu}\,dt$; the metric is the field that makes that integral meaningful at every point.
>
> **Type.** A `Concept` — a distinguished tensor field, and the extra structure that elevates a manifold to a Riemannian manifold.
>
> **Boundary.** A manifold has no metric by itself: many metrics fit the same topology, and the choice is physical or geometric content, not part of the manifold. Signature matters too — the Lorentzian case organizes relativity, the positive-definite case ordinary geometry.

## Key results

- **Index algebra.** $g_{\mu\nu}$ raises and lowers indices: $v^\mu = g^{\mu\nu}v_\nu$, with $g^{\mu\nu}$ the inverse matrix. This is what makes "the same tensor in covariant and contravariant form" a statement about one object.
- **Volume element.** $\sqrt{|\det g|}\,dx^1\cdots dx^n$ is the invariant volume form — the reason integrals on manifolds need the metric or a form.
- **Levi-Civita connection.** The metric determines a unique torsion-free, metric-compatible [connection](../geometry/connection.md); its Christoffels are built from derivatives of $g$.
- **Geodesics.** The paths extremizing the metric length are the [geodesics](../geometry/geodesic.md) — straight lines, in the only sense available.
- **Curvature from the metric.** All curvature tensors are computed from $g$ and its first two derivatives; this is why "the metric is the gravitational field" in general relativity.

## References

- https://en.wikipedia.org/wiki/Metric_tensor
- [Tensor Field](tensor-field.md) · [Connection](../geometry/connection.md) · [Geodesic](../geometry/geodesic.md) · [Riemann Tensor](riemann-tensor.md)
