---
tags: [analytical, geometry, type, mathematics]
---

# Tensor Field

> A **tensor field** assigns a tensor to every point of a manifold: it is a smooth section of a tensor bundle, and it is the object through which geometry and physics are written.

## Formulation

> **What it is.** The pointwise generalization of a [tensor](tensor.md). At each point of a manifold the tangent space carries its own tensor algebra; a field chooses one element of it at every point, varying smoothly. Scalar fields, vector fields, differential forms, metrics and curvature are all tensor fields of different ranks.
>
> **Type.** A `Concept` — a construction about a manifold, not a property of a single point.
>
> **Boundary.** A tensor field is not a function into numbers, and not a matrix of numbers at one point: it is an assignment that must be transported consistently across coordinate charts. Its smoothness is what makes the [connection](../geometry/connection.md) and derivatives of it meaningful.

## Key results

- **Sections of a bundle.** A tensor field of type $(r,s)$ is a section of $T^r{}_s M$; the bundle language is what makes "varies smoothly" precise (see [bundle](../geometry/bundle.md)).
- **Coordinate expression.** In a chart it is a family of components $T^{\mu_1\cdots\mu_r}{}_{\nu_1\cdots\nu_s}(x)$ that transform multilinearly under a change of coordinates — the transformation law, not the components, defines the object.
- **Tensor calculus.** Sums, products, contractions and index raising are pointwise operations on fields; the metric supplies the raising and lowering.
- **Covariant derivative.** Differentiating a field requires a connection; the derivative of a tensor field is again a tensor field, unlike the naive partial derivative.
- **The physics catalogue.** Metric, curvature, stress-energy, electromagnetic and stress tensors are the standard fields; each has its own note in this scope.

## References

- https://en.wikipedia.org/wiki/Tensor_field
- [Tensor](tensor.md) · [Metric Tensor](metric-tensor.md) · [Riemann Tensor](riemann-tensor.md) · [Bundle](../geometry/bundle.md)
