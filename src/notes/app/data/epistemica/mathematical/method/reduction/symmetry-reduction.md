---
tags: [note, mathematics, method, technique, geometry]
---

# Symmetry Reduction

> **Symmetry reduction** exploits the invariance of a problem under a group: the solution is constant along the group's orbits, so the problem descends to a lower-dimensional quotient — or to an ordinary differential equation.

## Formulation

> **What it is.** The routine of finding the symmetry group of an equation and using it to cut variables. An $n$-variable problem with a one-parameter symmetry becomes an $(n-1)$-variable problem; enough symmetry and it becomes an ODE.
>
> **Type.** An `Epistemic Method`. Its theory is Lie group analysis — the [transformation groups](../../structure/algebra/lie-group.md) that leave the equation's solution set fixed.
>
> **Boundary.** Symmetry reduces, it does not solve: the reduced equation can still be hard. And a symmetry found in one coordinate system need not be visible in another — the choice of variables is part of the method.

## Key results

- **Similarity solutions.** A scaling-invariant PDE has solutions depending only on a similarity variable $x/t^{1/2}$ — the diffusion kernel is the canonical instance.
- **Noether.** Every continuous symmetry of an action yields a conserved quantity — the bridge from reduction to [conservation laws](note.html?n=epistemica/epistemic/guidance/principle/conservation-law.md).
- **Group-invariant solutions.** The solutions invariant under a subgroup are the orbits of the symmetry group; classifying them classifies the reductions.
- **Bifurcation and normal forms.** Symmetry fixes the allowed terms in a normal form, which is why [bifurcation theory](../../change/bifurcation-theory.md) is organized by the symmetry of the problem.
- **Computational use.** In optimization and control, symmetry reduction shrinks the search space — the same routine, different setting.

## References

- https://en.wikipedia.org/wiki/Symmetry_reduction
- [Lie Group](../../structure/algebra/lie-group.md) · [Lie Algebra](../../structure/algebra/lie-algebra.md) · [Conservation Law](note.html?n=epistemica/epistemic/guidance/principle/conservation-law.md) · [Bifurcation Theory](../../change/bifurcation-theory.md)
