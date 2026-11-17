---
tags: [note, nature, physical-object, structural-engineering, ontology]
qa:
 - Is a beam a kind of member or a use of one — could the same body be a beam in one structure and a column in another?
 - The beam theory of the corpus assumes small deflections; what is the beam when the deflection is no longer small enough for the assumption to hold?
---

# Beam

> A **beam** is a [structural member](/view.html?p=notes/nature/body/member.md) that carries transverse load by bending: the load acts across its axis, the member answers with curvature, and the internal action is a **bending moment** whose magnitude varies along the span. Its characteristic failure is not crushing but excessive stress at the extreme fibre and deflection at mid-span.

## Formulation

### What natural element type does this natural instance belong to?

`Structural Member` at **meso** level of organization (Ontic; Constitutive) — a `Building Block` of a [structure](/view.html?p=notes/nature/body/structure.md), specialized to the bending case.

It is **not** the [column](/view.html?p=notes/nature/body/column.md): both are members of the same section, and the difference is the action, not the shape — a beam bends under a transverse load, a column is compressed along its axis and fails by buckling. It is **not** a [cable](/view.html?p=notes/nature/body/cable.md): a beam resists bending and therefore carries a moment, which a cable cannot. It is **not** the [structure](/view.html?p=notes/nature/body/structure.md), which is the assembly of which it is one part.

### What is this natural instance?

> A floor joist, a roof rafter, a bridge girder, a lintel over a door, a shelf, a bone in bending. Each receives load across its length and delivers it to the two ends.

Three quantities decide the response, and the theory that relates them is [Euler–Bernoulli beam theory](/view.html?p=notes/technica/discipline/euler-bernoulli-beam-theory.md): the **span** between the supports, the **second moment of area** of the cross-section — the geometric quantity that says how far the material sits from the neutral axis, and therefore how much curvature a moment buys — and the **material's** elastic modulus. Deflection scales with span to the fourth power, which is why a small increase in span is a large increase in depth; strength scales with the section modulus, which is why the same steel can be shallow and strong or deep and stiff.

The beam is also the corpus's cleanest example of a *theory with a stated bound*: the Euler–Bernoulli model assumes small deflections, plane sections remain plane, and shear deformation is negligible. Beyond those assumptions the same body is still a beam, but the note that describes it is a different one.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the member in bending — its support conditions, the section geometry that resists the moment, and the bounds the design must respect — not the assembly, not the theory, and not the material's microstructure.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam | Meso. The member in bending. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam `(→ Kind)` Simply Supported Beam | Meso. Pinned at both ends: the canonical case, maximum moment at mid-span. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam `(→ Kind)` Cantilever | Meso. Fixed at one end: maximum moment at the support, and the largest deflection of any single-span case. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam `(→ Kind)` Continuous Beam | Meso. Over several supports: the moment redistributes, and the support reactions are not statically determinate. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam `(→ Attribute)` `Property` `(→ Instance)` Second Moment of Area | Meso. The section's resistance to curvature: the geometric quantity that converts a moment into a stress. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam `(→ Attribute)` `Property` `(→ Instance)` Deflection | Meso. The displacement of the axis, scaling with the fourth power of the span. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Bending Stress | Micro. The extreme fibre must not be overstressed: the strength bound of the section. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Serviceability | Meso. Deflection must stay within the tolerance of what the beam supports — a bound on use, not on survival. |

**Limitations.** *Scale* — the theory is one-dimensional along the axis and stops resolving the section when the span approaches the depth. *Nonlinearity* — beyond small deflections, geometry and material both become nonlinear. *Many-Body coupling* — the end restraint is supplied by the structure, so the same beam is simply supported or continuous depending on what it is built into.

## References

- Galilei, G. (1638). *Discorsi e dimostrazioni matematiche intorno a due nuove scienze*. Elzevir. — the first strength analysis of a beam, and the scaling error that survived a century
- Euler, L. (1744). *Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes*. Bousquet. — the elastica: the bent beam solved as a variational problem
- Timoshenko, S. P. (1953). *History of strength of materials*. McGraw-Hill. — how the beam became a computable body
- Gordon, J. E. (1978). *Structures: Or why things don't fall down*. Penguin. — bending explained by curvature rather than by formula
- [Euler–Bernoulli Beam Theory](/view.html?p=notes/technica/discipline/euler-bernoulli-beam-theory.md) — the rule this body obeys
- [Member](/view.html?p=notes/nature/body/member.md) · [Column](/view.html?p=notes/nature/body/column.md) · [Cable](/view.html?p=notes/nature/body/cable.md) · [Structure](/view.html?p=notes/nature/body/structure.md)
