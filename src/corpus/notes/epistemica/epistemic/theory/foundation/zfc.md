---
tags: [note, foundation, logic]
---

# ZFC

> **ZFC** — Zermelo–Fraenkel set theory with Choice — is the standard axiomatic foundation of mathematics: nine axioms describing which sets exist, from which every ordinary mathematical object is built.

## Formulation

> **What it is.** The formal system in which "set" is the only primitive notion and everything else — numbers, functions, spaces — is encoded. A proof is a finite derivation from the axioms; a theorem is what such a derivation establishes.
>
> **Type.** A `Constitutive Element` — a `Foundation` of the mathematical representational system. Its axioms are the rules of well-formed existence.
>
> **Boundary.** ZFC is one foundation among several: type theory, category-theoretic foundations and constructive set theories are alternatives. It is the default because it is expressive, well-understood and (so far) consistent in practice.

## The axioms

| Group | Axioms |
| --- | --- |
| **Existence and extent** | Empty set, Extensionality, Pairing, Union, Power set, Infinity |
| **Comprehension** | Separation (subsets defined by a property), Replacement (images of definable functions) |
| **Regularity** | Foundation (no infinite descending membership chain) |
| **Choice** | The [axiom of choice](axiom-of-choice.md) |

## Key results

- **Encoding.** Ordered pairs, functions, relations, natural numbers (as finite ordinals) and the reals (as Dedekind cuts or Cauchy sequences) are all sets — the reason one theory suffices.
- **Independence.** Choice and the continuum hypothesis are independent of the other axioms (Gödel, Cohen).
- **Limits.** [Gödel's incompleteness](incompleteness-theorem.md) applies: if ZFC is consistent, it cannot prove its own consistency.
- **Separation versus naive comprehension.** Russell's paradox is blocked by restricting comprehension to subsets of an existing set.

## References

- https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory
- [Axiom of Choice](axiom-of-choice.md) · [Ordinal](ordinal.md) · [Peano Axioms](peano-axioms.md) · [Incompleteness Theorem](incompleteness-theorem.md)
