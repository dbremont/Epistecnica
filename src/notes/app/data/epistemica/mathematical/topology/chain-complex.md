---
tags: [note, mathematics, topology, algebraic]
---

# Chain Complex

> A **chain complex** is a sequence of abelian groups and homomorphisms $\cdots \to C_{n+1} \xrightarrow{\partial_{n+1}} C_n \xrightarrow{\partial_n} C_{n-1} \to \cdots$ with $\partial_n \circ \partial_{n+1} = 0$.

## Formulation

> **What it is.** The algebraic skeleton of homology: the condition $\partial^2 = 0$ says boundaries have no boundary, so the image of one map sits inside the kernel of the next, and the quotient measures the failure of exactness. That quotient is the homology.
>
> **Type.** A `Concept` — a diagram of groups with a defining equation; the object a [functor](../structure/category.md) assigns to a space.
>
> **Boundary.** A chain complex is not a space: it is the algebraic shadow of one. Different complexes compute the same homology, which is what makes the theory flexible (simplicial, singular, cellular).

## Key results

- **Homology.** $H_n = \ker \partial_n / \operatorname{im} \partial_{n+1}$ — cycles modulo boundaries, the standard invariant of a space.
- **Boundaries squared.** $\partial^2 = 0$ is the only axiom, and everything follows from it: this is the "one equation that generates a subject".
- **Chain maps and homotopies.** Maps of complexes induce maps on homology, and chain homotopic maps induce the same map — the algebra mirrors the topology.
- **Long exact sequence.** A short exact sequence of complexes yields a long exact sequence in homology — the workhorse computed by the [snake lemma](exact-sequence.md).
- **Universal coefficients.** Homology and cohomology of a complex are related by $\mathrm{Ext}$ and $\mathrm{Tor}$, the derived functors of Hom and tensor.

## References

- https://en.wikipedia.org/wiki/Chain_complex
- [Exact Sequence](exact-sequence.md) · [Homology](homology.md) · [Cohomology](cohomology.md) · [Category](../structure/category.md)
