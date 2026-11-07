---
tags: [note, foundation, logic, number]
---

# Peano Axioms

> The **Peano axioms** characterize the natural numbers: zero is a number, every number has exactly one successor, zero is no successor, distinct numbers have distinct successors, and induction holds.

## Formulation

> **What it is.** The minimal theory of counting. Everything true of $\mathbb{N}$ that needs no more than the successor structure follows from these five statements — including addition, multiplication and order, which are *defined* rather than assumed.
>
> **Type.** A `Constitutive Element` — a `Foundation` of arithmetic, the axiom set that the [numeral system](/note.html?p=notes/epistemica/mathematical/number/numeric-system.md) is built on.
>
> **Boundary.** The axioms describe the *structure* of the naturals, not their notation. Which symbols denote them is a representational choice; which relations hold is fixed here.

## The axioms

| # | Axiom |
| --- | --- |
| 1 | $0$ is a natural number |
| 2 | Every $n$ has a unique successor $S(n)$ |
| 3 | $0$ is not the successor of any $n$ |
| 4 | $S(m) = S(n) \Rightarrow m = n$ |
| 5 | If a set contains $0$ and is closed under $S$, it contains every natural number (induction) |

## Key results

- **Recursion.** Functions on $\mathbb{N}$ may be defined by giving a value at $0$ and a rule for $S(n)$ — the definition scheme behind every inductive definition.
- **Induction as an axiom, not a theorem.** In first-order logic the fifth axiom is a schema, one instance per formula, and non-standard models exist; in second-order logic it pins the naturals uniquely up to isomorphism.
- **Arithmetic from successor.** $m + 0 = m$ and $m + S(n) = S(m+n)$ define addition; multiplication follows the same pattern — this is the "rule" side of the [transformation rules](/note.html?p=notes/epistemica/mathematical/transformation.md) the numeral system carries.
- **Consistency.** The naturals are a model of the axioms; by [Gödel](incompleteness-theorem.md) the theory cannot prove that of itself.

## References

- https://en.wikipedia.org/wiki/Peano_axioms
- [ZFC](zfc.md) · [Incompleteness Theorem](incompleteness-theorem.md) · [Numeric System](/note.html?p=notes/epistemica/mathematical/number/numeric-system.md) · [Number](/note.html?p=notes/epistemica/mathematical/number/number.md)
