---
tags: [note, nature, property, structural-engineering, ontology]
qa:
 - Is a load path a property of the structure, of the load, or of the pair — and if the pair, why is it filed as a property rather than as a relation?
 - Two arrangements of the same steel are two structures because the load takes two paths; is the path then the identity of the structure, or a consequence of it?
---

# Load Path

> The **load path** is the route by which every imposed force reaches a support. It is not a drawing convention and not a metaphor: a structure *is* the set of paths it offers, two arrangements of the same members are two structures because the paths differ, and a structure with no continuous path for a given load has no way to carry it — whatever its members are capable of.

## Formulation

### What natural element type does this natural instance belong to?

`Interaction-Derived Quantity` at **meso** level of organization (Ontic; Qualitative), specialized from `Property` — a joint-state quantity, since a path exists only between an applied load and a support-`[structure](/view.html?p=notes/nature/body/structure.md)` pair.

It is **not** a `State`: a state is the configuration of an element at a moment, and the load path is what the configuration *does* to forces at every moment of the load. It is **not** the `Constraint` of equilibrium, which says that the forces must balance and not which route they take. It is **not** a member: members are the bodies the path runs through, and the same member can be on a primary path, a secondary path, or no path at all depending on what is loaded.

### What is this natural instance?

> A floor's load entering a joist, the joist delivering it to a beam, the beam to a column, the column to a footing, the footing to the ground. Also: an arch's thrust running in compression along the voussoirs to the abutments; a hanger's tension running up to a cable; a diaphragm's shear running sideways to a core.

The quantity has three attributes that decide almost everything about a structure, and each has a failure mode attached:

- **Continuity.** The path must be unbroken from load to support, in a medium that can carry the action it is given — a cable cannot continue a compressive path, and a joint that cannot transmit moment ends a bending path. Most structural failures are a broken path, not an overloaded member.
- **Directness.** The straighter the path, the less material and the fewer members it takes. The search for the shortest set of paths is a real problem with a real answer: Michell's optimal trusses are the limiting form, and every arch, dome and cable net is a device for making a curved path short.
- **Redundancy.** The number of independent paths between a load and its support. One path is a chain — failure is loss of the structure; several paths let the load redistribute, which is what "not failing progressively" means in practice.

The note's reason to exist is the first attribute. A path is invisible in the finished structure and decisive in it, which is why the corpus files it as a property the structure carries rather than as a drawing: it must be *traced* to be known, and it can be wrong while every member is adequate.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the path as a property — its kinds, the attributes that characterise it and the bounds that govern it — not the members it runs through, which are decomposed in `member.md`, and not the analysis technique, which is technica.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path | Meso. The route from an imposed load to a support. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path `(→ Kind)` Primary Path | Meso. The route the design intends: from load to support through the main members. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path `(→ Kind)` Secondary Path | Meso. The route that appears when the primary is overloaded or lost — the one that decides whether failure propagates. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path `(→ Kind)` Funicular Path | Meso. The equilibrium shape of a compression or tension path: the arch's line of thrust, the cable's catenary. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path `(→ Attribute)` `Property` `(→ Instance)` Continuity | Meso. The path is unbroken and its every medium can carry the action it is given. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path `(→ Attribute)` `Property` `(→ Instance)` Directness | Meso. How short the route is: the quantity optimal structures minimise. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path `(→ Attribute)` `Property` `(→ Instance)` Redundancy | Meso. The number of independent routes — the property that makes failure graceful. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Equilibrium | Micro. Every path must deliver its forces and moments to the supports: the bound no path escapes. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Load Path `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Compatibility | Micro. Paths that share members must deform consistently where they meet. |

**Limitations.** *Partial Observability* — the path is inferred from the analysis model and confirmed only by strain measurements at a few points. *Complexity* — in a redundant structure the forces distribute according to relative stiffness, so no path is purely a design intention. *Scale* — the path at the scale of a building is a single line; at the scale of a joint it is a field of local paths, and both are the same property at two levels.

## References

- Maxwell, J. C. (1864). On reciprocal figures, frames, and diagrams of forces. *Transactions of the Royal Society of Edinburgh*, 26, 1–40. — the graphical method in which a path becomes a diagram
- Michell, A. G. M. (1904). The limits of economy of material in frame-structures. *Philosophical Magazine*, 8(47), 589–597. — the optimal path set, and the quantity directness minimises
- Gordon, J. E. (1978). *Structures: Or why things don't fall down*. Penguin. — the path explained by tracing a load through a building
- Heyman, J. (1995). *The stone skeleton*. Cambridge University Press. — the funicular path in masonry, where the route must stay inside the stone
- [Structure](/view.html?p=notes/nature/body/structure.md) — the body whose identity is its paths
- [Member](/view.html?p=notes/nature/body/member.md) · [Connection](/view.html?p=notes/nature/body/connection.md) · [Foundation](/view.html?p=notes/nature/body/foundation.md) · [Arch](/view.html?p=notes/nature/body/arch.md) · [Cable](/view.html?p=notes/nature/body/cable.md)
- [Stability Analysis](/view.html?p=notes/technica/discipline/stability-analysis.md) · [Structural Mechanics](/view.html?p=notes/technica/discipline/structural-mechanics.md)
