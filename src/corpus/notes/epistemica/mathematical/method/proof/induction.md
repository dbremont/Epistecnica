---
tags: [note, mathematics, method, technique, foundation]
---

# Induction

> **Induction** proves a statement for every natural number by proving it for the base case and showing that its truth at $n$ forces its truth at $n+1$: a property closed under successors and holding at zero holds everywhere.

## Formulation

> **What it is.** The routine that turns an infinite family of claims into two finite ones. It is the fifth [Peano axiom](note.html?p=notes/epistemica/epistemic/theory/foundation/peano-axioms.md) read as a proof method, and the reason arithmetic can be developed at all.
>
> **Type.** An `Epistemic Method` — a reproducible order of acts (base case, induction hypothesis, step). It is not the axiom it rests on, and not the [ordinal](note.html?p=notes/epistemica/epistemic/theory/foundation/ordinal.md) recursion that generalizes it.
>
> **Boundary.** Induction proves statements about *discrete, well-founded* structures. It does not prove real-valued statements, and "induction" in the epistemic sense — [universal induction](../../universal-induction.md), Solomonoff's prior — is a different thing entirely.

## The forms

| Form | Hypothesis proved | When it is needed |
| --- | --- | --- |
| **Weak induction** | $P(n) \Rightarrow P(n+1)$ | The step depends on the previous case only |
| **Strong induction** | $P(k)$ for all $k < n$ $\Rightarrow P(n)$ | The step needs arbitrary smaller cases — factorization, termination |
| **Structural induction** | Every constructor preserves $P$ | Trees, terms, lists: the natural generalization past numbers |
| **Transfinite induction** | $P(\alpha)$ for all $\alpha < \beta$ $\Rightarrow P(\beta)$ | Ordinals; the general form once well-ordering is available |

## Key results

- **Well-ordering equivalence.** Induction, strong induction and the well-ordering of $\mathbb{N}$ are equivalent — one theorem in three costumes.
- **Canonical examples.** $\sum_{k=1}^n k = n(n+1)/2$; every $n > 1$ has a prime factorization; the number of leaves of a full binary tree exceeds its internal nodes.
- **The classic failure.** Proofs that "all horses are the same colour" fail in the base-to-step bridge, not in the algebra: the lesson is that the induction hypothesis must cover exactly the case the step uses.
- **Generalization.** Well-founded induction works on any relation with no infinite descending chains — the form used for termination proofs in rewriting and computation.

## References

- https://en.wikipedia.org/wiki/Mathematical_induction
- [Peano Axioms](note.html?p=notes/epistemica/epistemic/theory/foundation/peano-axioms.md) · [Ordinal](note.html?p=notes/epistemica/epistemic/theory/foundation/ordinal.md) · [Descent](descent.md) · [Extremal Principle](extremal-principle.md)
