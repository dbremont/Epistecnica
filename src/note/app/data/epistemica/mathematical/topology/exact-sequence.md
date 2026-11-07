---
tags: [mathematics, topology, algebraic]
---

# Exact Sequence

> A sequence of groups and homomorphisms $\cdots \to A \xrightarrow{f} B \xrightarrow{g} C \to \cdots$ is **exact** at $B$ when $\operatorname{im} f = \ker g$: what arrives is exactly what is annihilated.

## Formulation

> **What it is.** The bookkeeping device for structure: a short exact sequence $0 \to A \to B \to C \to 0$ says $B$ is built from $A$ and $C$, without saying whether $B$ splits. Exactness is the local statement that a [chain complex](chain-complex.md)'s failure to be exact is the interesting part.
>
> **Type.** A `Concept` — a diagram with a vanishing condition; the language in which homological algebra is written.
>
> **Boundary.** Exactness at one place is local; a *short* exact sequence is the packaged form of a quotient, and the extension problem is exactly the failure of it to split.

## Key results

- **Splitting.** A short exact sequence splits iff there is a section (equivalently a retraction), and over vector spaces it always does — which is why linear algebra has no extension theory and module theory does.
- **Snake lemma.** A map between two short exact sequences produces a connecting homomorphism $\delta: \ker \to \operatorname{coker}$, with a six-term exact sequence around it.
- **Long exact sequence.** From a short exact sequence of [chain complexes](chain-complex.md), the connecting maps assemble into $\cdots \to H_n(A) \to H_n(B) \to H_n(C) \xrightarrow{\delta} H_{n-1}(A) \to \cdots$.
- **Five lemma.** If four maps in a commutative ladder are isomorphisms, so is the fifth — the standard diagram chase.

## References

- https://en.wikipedia.org/wiki/Exact_sequence
- [Chain Complex](chain-complex.md) · [Homology](homology.md) · [Category](../structure/category.md) · [Duality](../structure/duality.md)
