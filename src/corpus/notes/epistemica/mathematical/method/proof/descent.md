---
tags: [note, mathematics, method, technique, discrete]
---

# Infinite Descent

> **Infinite descent** proves that a property holds by showing that any counterexample yields a strictly smaller counterexample — an infinite chain of positive integers that cannot exist.

## Formulation

> **What it is.** Fermat's proof method: assume a smallest counterexample, derive a smaller one, contradict well-ordering. It is the [extremal principle](extremal-principle.md) and [induction](induction.md) wearing a third costume.
>
> **Type.** An `Epistemic Method`.
>
> **Boundary.** The construction must be *strictly* decreasing in a well-founded order, and integer-valued. Over the reals descent proves nothing, which is why the method is native to number theory.

## Key results

- **Fermat.** No right triangle with integer sides has square area — the first documented descent proof, and still the canonical one.
- **Irrationality revisited.** $\sqrt{2}$ irrational by descent: a smaller pair of integers with the same property, forever.
- **No infinite descending chains.** The method *is* the well-ordering of $\mathbb{N}$ read as a proof rule; see [ordinals](/view.html?p=notes/epistemica/epistemic/theory/foundation/ordinal.md) for the transfinite version.
- **Termination.** In computer science descent is the termination argument for recursive programs; the well-founded measure plays the role of the decreasing integer.
- **Equivalence.** Descent, strong induction and well-ordering are the same principle; choosing among them is choosing the presentation, not the logic.

## References

- https://en.wikipedia.org/wiki/Proof_by_infinite_descent
- [Extremal Principle](extremal-principle.md) · [Induction](induction.md) · [Ordinal](/view.html?p=notes/epistemica/epistemic/theory/foundation/ordinal.md) · [Indirect proof](contradiction.md)
