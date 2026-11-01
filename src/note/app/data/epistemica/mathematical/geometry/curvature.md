---
tags: [geometry, differentialgeometrical]
---

# Curvature

> **Curvature** measures the failure of parallel transport to be path-independent: transport a vector around a closed loop and the defect is the curvature of the connection integrated over the enclosed surface.

## Formulation

> **What it is.** The second derivative of the geometry. Given a [connection](connection.md), the Riemann tensor $R(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$ records how much the covariant derivatives fail to commute.
>
> **Type.** A `Concept` — a tensor field derived from a connection; it is a construction about the manifold, not a property of the point.
>
> **Boundary.** There is no curvature without a connection, and no scalar "the curvature" without a choice of contraction. Riemann, Ricci and scalar curvature are contractions of one object, which is why they answer different questions.

## Key results

- **Riemann tensor.** The full curvature, with the symmetries $R_{abcd} = -R_{bacd} = -R_{abdc} = R_{cdab}$.
- **Ricci and scalar.** $\mathrm{Ric}_{ab} = R^c{}_{acb}$ and $R = g^{ab}\mathrm{Ric}_{ab}$ — the two contractions that appear in general relativity and in the [Ricci flow](../ricci-flow.md).
- **Theorema egregium.** Gaussian curvature of a surface is intrinsic: it can be measured by an inhabitant, without reference to the ambient space.
- **Holonomy.** Curvature is the infinitesimal holonomy of a connection; flat connections are exactly those with trivial holonomy around every contractible loop.
- **Einstein's equation.** $R_{ab} - \tfrac{1}{2}R g_{ab} = 8\pi T_{ab}$ — the physical reading of the Ricci contraction.

## References

- https://en.wikipedia.org/wiki/Curvature_of_Riemannian_manifolds
- [Connection](connection.md) · [Geodesic](geodesic.md) · [Ricci Tensor](../ricci-tensor.md) · [Ricci Flow](../ricci-flow.md)
