---
tags: [geometry, differentialgeometrical]
---

# Connection

> A **connection** is the rule that lets a vector be transported from one tangent space of a manifold to another, and therefore the rule that says what "the derivative of a vector field" means.

## Formulation

> **What it is.** On a manifold each tangent space is separate, so there is no canonical way to compare vectors at different points. A connection supplies one — a covariant derivative $\nabla_X Y$ — and with it the notions of parallel transport, geodesics and curvature.
>
> **Type.** A `Concept` — extra structure on a manifold, not part of the manifold itself.
>
> **Boundary.** A connection is not unique: every manifold has many, and choosing one is choosing what "straight" means. A Riemannian metric singles out the *Levi-Civita* connection, the unique one that is torsion-free and metric-compatible.

## Key results

- **Covariant derivative.** $\nabla_X Y$ is linear in $X$, additive in $Y$, and satisfies the Leibniz rule with respect to functions.
- **Parallel transport.** Vectors move along curves by solving $\nabla_{\dot\gamma} V = 0$; the result depends on the path exactly when curvature is nonzero.
- **Levi-Civita.** Given a metric there is exactly one torsion-free, metric-compatible connection — the Christoffel symbols are its coordinates.
- **Gauge reading.** A connection on a [bundle](bundle.md) is the geometric form of a gauge field; the electromagnetic potential is the archetype.

## References

- https://en.wikipedia.org/wiki/Connection_(mathematics)
- [Curvature](curvature.md) · [Geodesic](geodesic.md) · [Bundle](bundle.md) · [Manifold](../topology/manifold.md)
