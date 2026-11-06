---
tags: [foundation, logic, theorem]
---

# Incompleteness Theorem

> **Gödel's first incompleteness theorem**: any consistent, recursively axiomatized formal system strong enough to express arithmetic contains a true statement it cannot prove. The second adds: such a system cannot prove its own consistency.

## Formulation

> **What it is.** The limit theorem of formalization. It does not say mathematics is unreliable or that proofs are wrong; it says that no single effective axiom system captures all arithmetical truth — there is always a statement the system can neither prove nor refute.
>
> **Type.** A `Construction` of the kind `Theory` — a stated result about formal systems, not about numbers.
>
> **Boundary.** The hypotheses matter: consistency, effective axiomatization, and enough arithmetic. Weaker systems (Presburger arithmetic) are complete; stronger but non-effective ones escape the theorem.

## Key results

- **The Gödel sentence.** A sentence $G$ asserting its own unprovability: if the system proves $G$ it is inconsistent; if it is consistent, $G$ is true but unprovable.
- **Undecidability.** The set of arithmetical truths is not recursively enumerable — no algorithm lists them all.
- **Second theorem.** Consistency cannot be proved within the system. Hilbert's programme of a finitary consistency proof is thereby closed, though Gentzen's transfinite induction proof shows what is needed.
- **Relativity of the limit.** Incompleteness is a property of *one* system: a stronger system proves the weaker one's Gödel sentence, and the tower continues. The [ZFC](zfc.md) system is at the bottom of the usual tower.

## References

- https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
- [ZFC](zfc.md) · [Peano Axioms](peano-axioms.md) · [Gödel Machine](../../mathematical/godel-machine.md) · [Model versus proof](zfc.md)
