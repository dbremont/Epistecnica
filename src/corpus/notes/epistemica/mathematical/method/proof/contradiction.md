---
tags: [note, mathematics, method, technique]
---

# Proof by Contradiction

> **Proof by contradiction** establishes a statement by assuming its negation and deriving an impossibility: since the negation cannot hold, the statement must.

## Formulation

> **What it is.** The routine of *reductio ad absurdum*. Assume $\lnot P$, derive a formula and its negation (or a falsehood), conclude $P$. Its close relative, proof by contrapositive, proves $P \Rightarrow Q$ by proving $\lnot Q \Rightarrow \lnot P$; the two are often conflated and are not the same move.
>
> **Type.** An `Epistemic Method`; in the [ZFC](/view.html?p=notes/epistemica/epistemic/theory/foundation/zfc.md) setting it is licensed by classical logic, and its validity is exactly the law of excluded middle.
>
> **Boundary.** In constructive mathematics a proof by contradiction proves only $\lnot\lnot P$, never $P$ — this is the line between classical and intuitionistic logic, and the reason some existence proofs are non-constructive.

## Key results

- **Euclid.** Infinitely many primes: assume finitely many, multiply and add one, obtain a prime outside the list.
- **Irrationality.** $\sqrt{2} \notin \mathbb{Q}$: assume $p/q$ in lowest terms, derive that both are even.
- **Cantor and Gödel.** Both are contradictions built on [diagonalization](diagonalization.md) — the technique supplies the construction, contradiction supplies the conclusion.
- **The classical/constructive distinction.** $\lnot\lnot P \Rightarrow P$ is not provable in intuitionistic logic; a constructive proof must exhibit a witness.
- **Non-constructive existence.** "Assume no such object exists" plus compactness or Zorn often yields existence with no example — the price of the method.

## References

- https://en.wikipedia.org/wiki/Proof_by_contradiction
- [Diagonalization](diagonalization.md) · [Descent](descent.md) · [ZFC](/view.html?p=notes/epistemica/epistemic/theory/foundation/zfc.md) · [Extremal Principle](extremal-principle.md)
