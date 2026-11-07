---
tags: [note, mathematics, geometry, function, space]
---

# Isometry

> An **isometry** is a map between metric spaces that preserves distances: $d(f(x), f(y)) = d(x, y)$ for all $x, y$.

## Formulation

> **What it is.** The structure-preserving map of metric geometry — the analogue at the metric level of what a [linear map](../structure/linear/linear-map.md) is at the vector-space level and a [homeomorphism](../topology/topology.md) at the topological level. A [map](../mapping/map.md) that happens to preserve the whole metric, not just its topology.
>
> **Type.** A `Morphism` of metric spaces, hence a `Concept` in the map taxonomy.
>
> **Boundary.** Isometry is not an equivalence of spaces unless it is onto; an isometric embedding preserves distances without covering the target. Rigid motions are the isometries of Euclidean space, and they compose to a group.

## Key results

- **Injectivity.** Every isometry is injective, so it is an embedding; it is an isomorphism exactly when it is surjective.
- **Mazur–Ulam.** Every surjective isometry of a real normed space is affine — metric rigidity forces linearity.
- **Isometry groups.** The isometries of a space form a group; for $\mathbb{R}^n$ it is the Euclidean group, and its classification is the classical theory of rigid motions.
- **Rigidity.** A metric often determines its space up to isometry (all the geometry is in the distance function), which is the starting point of metric geometry.

## References

- https://en.wikipedia.org/wiki/Isometry
- [Metric Space](metric-space.md) · [Complete Space](complete-space.md) · [Map](../mapping/map.md) · [Linear Map](../structure/linear/linear-map.md)
