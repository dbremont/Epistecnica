---
tags: [note, mathematics, method, technique]
---

# Invariant Method

> The **invariant method** proves a statement by exhibiting a quantity that every allowed operation preserves — or one that strictly increases — so that no sequence of operations can cross between the two states.

## Formulation

> **What it is.** A proof routine built on a conserved quantity. If an operation preserves colour, parity, sum or area, then any two states differing in that quantity are unreachable from each other; if an operation strictly decreases a positive integer, the process terminates.
>
> **Type.** An `Epistemic Method`. The conserved object itself is an [invariant](../../invariant.md); the method is the routine of finding and using one.
>
> **Boundary.** An invariant proves *impossibility* of a transformation and a monovariant proves *termination*; neither alone proves reachability. The hard direction — showing the invariant is complete — needs a separate construction.

## Key results

- **Parity and colouring.** A chessboard with two corners removed cannot be tiled by dominoes; the colouring invariant settles it in one line.
- **Monovariants.** Euclid's algorithm terminates because the remainder strictly decreases; every termination proof for a rewriting system is a monovariant (see [term rewriting](../../../../technica/computation/)).
- **Invariants in dynamics.** Energy, momentum and angular momentum are conserved by the flow — Noether's theorem explains why, and [dynamical systems](../../change/dynamical-system.md) are classified by them.
- **Conservation as an invariant.** Every [conservation law](/view.html?p=notes/epistemica/epistemic/guidance/principle/conservation-law.md) is an invariant method waiting to be applied: find what the process cannot change.
- **Completeness.** For a group action, the invariant ring separates orbits — the theorem that says when invariants are enough.

## References

- https://en.wikipedia.org/wiki/Invariant_(mathematics)
- [Invariant](../../invariant.md) · [Conservation Law](/view.html?p=notes/epistemica/epistemic/guidance/principle/conservation-law.md) · [Induction](induction.md) · [Extremal Principle](extremal-principle.md)
