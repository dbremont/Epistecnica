---
tags: [geometry, topology]
---

# Bundle

> A **bundle** is a map $p: E \to B$ whose fibres look locally like a fixed model fibre $F$: every point of the base has a neighbourhood $U$ with $p^{-1}(U) \cong U \times F$.

## Formulation

> **What it is.** The standard way to attach data to every point of a space: a tangent bundle attaches vector spaces, a principal bundle attaches symmetry groups, a [covering space](../topology/covering-space.md) attaches discrete sets. The bundle is the *varying* object; the base is the parameter space.
>
> **Type.** A `Concept` — a structured map; the setting in which connections and curvature live.
>
> **Boundary.** Local triviality is the hypothesis; global twisting is the subject. The Möbius band is the canonical example of a bundle that is not a product.

## Key results

- **Sections.** A section $s: B \to E$ with $p \circ s = \mathrm{id}$ is a choice of one element per fibre — a vector field for the tangent bundle, a scalar field for a line bundle.
- **Vector bundles.** Fibres are vector spaces and the transition maps are linear; the tangent and cotangent bundles are the archetypes.
- **Principal bundles.** Fibres are a group $G$ acting freely; every vector bundle with structure group $G$ comes from one.
- **Characteristic classes.** Cohomology classes measuring the twisting; they obstruct the existence of nowhere-zero sections and of global frames.
- **Gauge theory.** A [connection](connection.md) on a principal bundle is a gauge field, and curvature is its field strength.

## References

- https://en.wikipedia.org/wiki/Fiber_bundle
- [Connection](connection.md) · [Curvature](curvature.md) · [Covering Space](../topology/covering-space.md) · [Cohomology](../topology/cohomology.md)
