---
tags: [method, technique, foundation, mathematics]
---

# Diagonalization

> **Diagonalization** constructs an object that differs from every member of a listed family at its own index: $d_i \neq a_{ii}$. The diagonal escape proves that some families cannot be listed at all.

## Formulation

> **What it is.** A proof routine in three moves — assume an enumeration, read down the diagonal, alter each entry — whose conclusion is that the enumeration cannot be complete. Cantor used it for the reals, Gödel encoded it for arithmetic, Turing ran it on machines.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** It proves *non*-existence (of a surjection, a complete list, a decision procedure). It gives no constructive counterexample to a specific claim, which is why it is a proof of impossibility rather than a construction.

## Key results

- **Cantor (1891).** The reals are uncountable: given any list of sequences, flip the diagonal and obtain a sequence not on the list. The origin of [cardinality](../../number/cardinality.md) as a comparison of sizes.
- **Russell's paradox.** The set of all sets not containing themselves leads to contradiction by the same diagonal move — the reason naive comprehension was abandoned (see [ZFC](note.html?n=epistemica/epistemic/theory/foundation/zfc.md)).
- **Gödel.** Arithmetization turns "this sentence is unprovable" into a diagonal construction inside a formal system — the engine of the [incompleteness theorem](note.html?n=epistemica/epistemic/theory/foundation/incompleteness-theorem.md).
- **Turing.** The halting problem is undecidable: assume a decider, build the machine that does the opposite of what it predicts, contradict.
- **The pattern.** A diagonal argument always needs: an enumeration hypothesis, an encoding of the list into its own members, and a negation step.

## References

- https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
- [Cardinality](../../number/cardinality.md) · [Incompleteness Theorem](note.html?n=epistemica/epistemic/theory/foundation/incompleteness-theorem.md) · [Contradiction](contradiction.md) · [Induction](induction.md)
