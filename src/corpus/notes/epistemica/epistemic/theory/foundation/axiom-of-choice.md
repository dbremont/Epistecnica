---
tags: [note, foundation, logic]
---

# Axiom of Choice

> The **axiom of choice** states that for every family of non-empty sets there is a function choosing one element from each — even when the family is infinite and no rule for choosing is given.

## Formulation

> **What it is.** The axiom that turns "there exists one for each" into "there is a choice function". It is independent of the other axioms of set theory, and it is the reason mathematics has a non-constructive half.
>
> **Type.** A `Constitutive Element` — a `Foundation` of the [ZFC](zfc.md) representational system, not a theorem.
>
> **Boundary.** Over finite families it is a theorem of logic; over infinite ones it is an assumption. The controversy is not about truth but about what a proof is allowed to assert: a choice function exists without being definable.

## The equivalent forms

| Form | Statement | Where it is used |
| --- | --- | --- |
| **Zorn's lemma** | A non-empty poset in which every chain has an upper bound has a maximal element | Existence of bases, maximal ideals, Hahn–Banach |
| **Well-ordering theorem** | Every set can be well-ordered | Transfinite construction, [ordinals](ordinal.md) |
| **Tychonoff** | An arbitrary product of compact spaces is compact | Topology, functional analysis |
| **Hahn–Banach** | A bounded functional on a subspace extends with the same norm | The dual space is rich enough to separate points |
| **Trichotomy of cardinals** | Any two sets are comparable in size | Cardinal arithmetic |

## Key results

- **Independence.** Cohen's forcing shows choice is consistent and independent: neither it nor its negation follows from ZF.
- **Non-measurable sets.** With choice, $\mathbb{R}$ has non-measurable subsets — the [Vitali set](/note.html?p=notes/epistemica/mathematical/vitali-set.md) is the standard witness. Without choice, all sets can be measurable.
- **Banach–Tarski.** A ball splits into finitely many pieces reassembling into two balls — the most quoted pathology, and a proof that choice is doing real work.
- **Constructive alternatives.** Dependent choice suffices for most analysis; countable choice for most measure theory; the full axiom is needed mostly for algebra and topology.

## References

- https://en.wikipedia.org/wiki/Axiom_of_choice
- [ZFC](zfc.md) · [Ordinal](ordinal.md) · [Vitali Set](/note.html?p=notes/epistemica/mathematical/vitali-set.md) · [Basis](/note.html?p=notes/epistemica/mathematical/structure/linear/basis.md)
