---
tags: [note, nature, physical-object, structural-engineering, geotechnical, ontology]
qa:
 - Is a foundation a part of the structure or a part of the ground — and if it is the interface, which of the two does it belong to?
 - Settlement is a serviceability bound, not a strength bound; why does a foundation fail more often by moving than by breaking?
---

# Foundation

> A **foundation** is the [support](/view.html?p=notes/nature/body/structure.md) through which a structure delivers its load to the ground: the body that spreads the concentrated actions of the members over an area of soil, rock or pile shaft large enough for the ground to carry them. It is a `Building Block` of the structure and, uniquely among them, the one whose other half is a **substance** — the soil it sits in.

## Formulation

### What natural element type does this natural instance belong to?

`Support` at **meso** level of organization (Ontic; Constitutive), within `Structure (→ Part) Building Block (→ Kind) Support`, specialized here to `Foundation`.

It is **not** the [structure](/view.html?p=notes/nature/body/structure.md) it carries: the structure is the assembly above, and the foundation is one of its parts. It is **not** the [soil](/view.html?p=notes/nature/matter/geological/soil.md): the soil is the substance that receives the load, and the foundation is the body that distributes it. It is **not** a `Property` — bearing capacity belongs to the ground-foundation system, not to either alone, which is why the note's quantities are joint quantities.

### What is this natural instance?

> A strip footing under a wall, a pad under a column, a raft under a whole building, a pile driven to a firmer layer, a caisson sunk to rock. Each is a body whose purpose is geometric: to enlarge the area over which a load meets the ground, or to reach ground that can take it.

Two families follow from that purpose. A **shallow** foundation spreads the load over an area near the surface — the footing, the pad, the raft — and its capacity is governed by the soil's **bearing capacity** and by the **settlement** it tolerates. A **deep** foundation carries the load down through weak material to a stratum that can take it — the pile by skin friction and end bearing, the caisson by bearing alone — and its capacity is governed by the shaft and the base rather than by the surface.

The note's most important statement is about which failure governs. A foundation rarely fails by *breaking*: it fails by **moving** — differential settlement tilting a structure that is still intact, or a bearing-capacity failure in which the soil shears and the foundation punches into it. That is why the design bounds are two, and why the settlement bound, which is about use rather than survival, is usually the one that decides the size.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the support body — its families, the quantities of the joint ground-foundation system and the bounds that govern it — not the structure above, not the soil's own classification, and not the design practice, which is [geotechnical engineering](/view.html?p=notes/miscellanea/discipline/geotechnical-engineering.md).
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Kind)` Foundation | Meso. The body that delivers the structure's load to the ground. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Kind)` Foundation `(→ Kind)` Shallow Foundation | Meso. Spreads the load over an area near the surface: strip, pad, raft. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Kind)` Foundation `(→ Kind)` Deep Foundation | Meso. Carries the load to a deeper stratum: pile, caisson, pier. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Kind)` Foundation `(→ Attribute)` `Property` `(→ Instance)` Bearing Pressure | Meso. The load per unit area delivered to the ground — the quantity the area is chosen to keep within limits. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Kind)` Foundation `(→ Attribute)` `Property` `(→ Instance)` Settlement | Meso. The vertical movement of the ground under load, and its differential across the structure. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Kind)` Foundation `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Bearing Capacity | Micro. The shear strength of the ground bounds the pressure before it fails. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Kind)` Foundation `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Tolerable Movement | Meso. The settlement the supported structure can accept — usually the binding bound. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Kind)` Foundation `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Sliding and Overturning | Meso. The support must not translate or rotate as a body under horizontal action. |

**Limitations.** *Uncertainty* — the ground is sampled at points and inferred between them, so its properties are the least known quantities in the structure. *Partial Observability* — the failure surface is underground and invisible until it moves. *Many-Body coupling* — capacity is a property of the foundation *and* the soil, not of either. *Non-Repeatability* — loading the ground changes it, and the second load path is not the first.

## References

- Terzaghi, K. (1943). *Theoretical soil mechanics*. Wiley. — bearing capacity and settlement as the two governing problems
- Terzaghi, K., & Peck, R. B. (1948). *Soil mechanics in engineering practice*. Wiley. — the joint ground-foundation system treated as an engineering object
- [Soil](/view.html?p=notes/nature/matter/geological/soil.md) — the substance that receives the load
- [Geotechnical Engineering](/view.html?p=notes/miscellanea/discipline/geotechnical-engineering.md) — the practice that designs this support
- [Structure](/view.html?p=notes/nature/body/structure.md) · [Load Path](/view.html?p=notes/nature/property/load-path.md) · [Member](/view.html?p=notes/nature/body/member.md) · [Connection](/view.html?p=notes/nature/body/connection.md)
