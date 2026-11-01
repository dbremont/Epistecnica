---
tags: [foundation, relation]
---

# Ordinal

> An **ordinal** is the order type of a well-ordered set: the canonical representative of "how long" a well-ordering is, extending the natural numbers past infinity.

## Formulation

> **What it is.** Where a [cardinal](../../mathematical/number/cardinality.md) answers "how many", an ordinal answers "in what order". $\omega$ is the order type of the naturals, $\omega+1$ of the naturals followed by one more element, and the ordinals continue transfinitely.
>
> **Type.** A `Concept` — a construction in set theory, defined as a transitive set well-ordered by $\in$ (von Neumann ordinals).
>
> **Boundary.** Ordinals and cardinals coincide for finite sets and diverge at infinity: $\omega$, $\omega+1$, $\omega+2$, … are all countably infinite but distinct ordinals.

## Key results

- **Well-ordering.** Every ordinal is well-ordered by $\in$, and every well-ordered set is isomorphic to exactly one ordinal.
- **Transfinite induction.** A property holding for $0$, inherited by successors, and holding at limits for all ordinals holds for all ordinals.
- **Transfinite recursion.** Functions may be defined along the ordinals, which is how [Zorn's-lemma](../../mathematical/structure/algebra/algebra.md)-free constructions are run.
- **Arithmetic.** $\omega + 1 \neq 1 + \omega$: ordinal addition is not commutative, because order matters.
- **Cantor normal form.** Every ordinal is a finite sum $\omega^{\alpha_1}c_1 + \cdots$ — the base-$\omega$ expansion.

## References

- https://en.wikipedia.org/wiki/Ordinal_number
- [Axiom of Choice](axiom-of-choice.md) · [Well-ordering](axiom-of-choice.md) · [Cardinality](../../mathematical/number/cardinality.md) · [Order](../../mathematical/order.md)
