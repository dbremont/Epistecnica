---
tags: [analytical, geometry, type, mathematics]
---

# Riemann Curvature Tensor

> The **Riemann curvature tensor** $R^a{}_{bcd}$ is the tensor field measuring the failure of covariant derivatives to commute: the full, uncontracted curvature of a manifold with a connection.

## Formulation

> **What it is.** The object from which every other curvature is obtained by contraction. Its geometric meaning is holonomy — transport a vector around a small loop and the defect is $R$ integrated over the enclosed surface. Its analytic meaning is the commutator $[\nabla_c, \nabla_d]$ acting on vectors.
>
> **Type.** A `Concept`; the [curvature note](../geometry/curvature.md) states the geometric reading, and this note carries the tensor itself and its index algebra.
>
> **Boundary.** It depends on the [connection](../geometry/connection.md): change the connection and the curvature changes. It is not the same object as the metric, although on a Riemannian manifold the Levi-Civita connection ties them.

## Key results

- **Definition.** $R^a{}_{bcd} = \partial_c\Gamma^a_{bd} - \partial_d\Gamma^a_{bc} + \Gamma^a_{ce}\Gamma^e_{bd} - \Gamma^a_{de}\Gamma^e_{bc}$ in components; the nonlinear terms are what make it a tensor while the Christoffels are not.
- **Symmetries.** $R_{abcd} = -R_{bacd} = -R_{abdc} = R_{cdab}$ and the first Bianchi identity $R_{a[bcd]} = 0$ — the algebraic identities that reduce the independent components to $n^2(n^2-1)/12$.
- **Contractions.** Ricci is $R_{ab} = R^c{}_{acb}$; the scalar curvature is $R = g^{ab}R_{ab}$; the traceless part is the [Weyl tensor](weyl-tensor.md).
- **Flatness.** $R = 0$ at every point iff the manifold is locally isometric to Euclidean space — the theorem that makes curvature the complete local invariant.
- **Einstein's equation.** Contracting twice produces the [Einstein tensor](einstein-tensor.md), the divergence-free combination that can equal a stress-energy source.

## References

- https://en.wikipedia.org/wiki/Riemann_curvature_tensor
- [Curvature](../geometry/curvature.md) · [Ricci Tensor](ricci-tensor.md) · [Weyl Tensor](weyl-tensor.md) · [Metric Tensor](metric-tensor.md)
