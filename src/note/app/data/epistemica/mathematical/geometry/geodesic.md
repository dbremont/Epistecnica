---
tags: [mathematics, geometry, differentialgeometrical]
---

# Geodesic

> A **geodesic** is a curve whose tangent vector is parallel along itself: the generalization to a curved space of a straight line, and the path along which a free particle travels.

## Formulation

> **What it is.** The solution of $\nabla_{\dot\gamma}\dot\gamma = 0$. On a Riemannian manifold it is also the stationary curve of length (and of energy), which is the variational definition; the equivalence of the two is the content of the notion.
>
> **Type.** A `Concept` — a distinguished family of curves determined by a [connection](connection.md).
>
> **Boundary.** Geodesics are locally, not globally, length-minimizing: on a sphere, a great circle beyond the antipode is geodesic but not shortest. The cut locus is where that failure begins.

## Key results

- **Local existence and uniqueness.** Through each point and each tangent direction there is exactly one geodesic, by the Picard–Lindelöf theorem applied to the geodesic equation.
- **Exponential map.** $\exp_p(v)$ is the point reached by travelling unit time along the geodesic with initial velocity $v$; normal coordinates are the coordinates it defines.
- **Variational characterization.** Geodesics extremize $\int \sqrt{g(\dot\gamma,\dot\gamma)}\,dt$, so the Euler–Lagrange equation *is* the geodesic equation.
- **Jacobi fields.** Deviation of nearby geodesics is governed by curvature: positive curvature focuses them, negative curvature spreads them.

## References

- https://en.wikipedia.org/wiki/Geodesic
- [Connection](connection.md) · [Curvature](curvature.md) · [Manifold](../topology/manifold.md) · [Variational Method](../method/reduction/variational-method.md)
