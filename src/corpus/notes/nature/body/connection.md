---
tags: [note, nature, physical-object, structural-engineering, ontology]
qa:
 - A connection is where a structure is weakest and where it is most redundant; can both be true of the same joint?
 - The joint transmits force by contact — is a welded joint a material, a body, or a boundary between two bodies?
---

# Connection

> A **connection** is the [building block](/view.html?p=notes/nature/body/structure.md) that transmits action between members: a weld, a bolt, a rivet, a pin, a bearing, an anchorage, a mortise and tenon. It is the joint where the load path is re-routed from one body into another, and it is therefore where the structure's strength is actually decided — the shelf's own definition says strength is "the capacity of the weakest member **or connection**".

## Formulation

### What natural element type does this natural instance belong to?

`Structural Connection` at **meso** level of organization (Ontic; Constitutive), within `Structure (→ Part) Building Block`, specialized to the joint.

It is **not** a [member](/view.html?p=notes/nature/body/member.md): a member is a body with a span, a joint is the interface where two spans meet and is characterised by its transmission mechanism rather than by its length. It is **not** a `Substance / Matter` — weld metal is a substance, the weld is the body and its action. It is **not** a `Property`: ductility and slip resistance are carried by the joint, not identical with it.

### What is this natural instance?

> A welded T-joint, a bolted splice, a riveted girder flange, a pin in a truss node, a bearing under a bridge beam, a column baseplate anchored into concrete, a timber mortise and tenon.

The classification is by **mechanism of transmission**, and each mechanism has its own characteristic failure:

- **Fused** — the weld: continuous, stiff, and failing by cracking at the toe, where the geometry concentrates stress.
- **Friction and bearing** — the bolt and the rivet: slip first, then bearing on the hole, then tear-out of the plate. A friction-grip bolt transmits by clamping; a bearing bolt by contact; the difference is which failure comes first.
- **Contact** — the pin, the roller, the bearing: transmits compression and shear, and cannot transmit a moment at all, which is what makes it the standard way to *model* a hinge rather than to build one.
- **Anchorage** — the baseplate, the tie into concrete: transmits tension into a material that is strong in compression and weak in it, so the failure is often cone-shaped and in the substrate.

Two properties make the connection the governing element it usually is. It is **where the load path changes direction**, so it carries combined actions — a moment, a shear and an axial force at once — where the member carried one. And it is **the most redundant part of the structure**: a connection has many small paths rather than one, which is what allows a ductile joint to redistribute and a brittle one to fail progressively.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the joint — its mechanisms, the quantities that characterise its transmission and the bounds that govern it — not the members it joins, not the design code, and not the welding metallurgy.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection | Meso. The joint that transmits action between members. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection `(→ Kind)` Welded Connection | Meso. Fused: continuous transmission, and stress concentration at the weld toe. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection `(→ Kind)` Bolted Connection | Meso. Clamped or bearing transmission, with slip before bearing. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection `(→ Kind)` Pinned Connection | Meso. Contact only: transmits force and cannot transmit moment — the physical hinge. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection `(→ Kind)` Anchorage | Meso. Transmission into a substrate: baseplate, tie, dowel, and the cone of material that resists it. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection `(→ Attribute)` `Property` `(→ Instance)` Ductility | Meso. The ability to deform before failing, which decides whether the joint redistributes or propagates failure. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection `(→ Attribute)` `Property` `(→ Instance)` Slip Resistance | Meso. The action a friction joint carries before it moves. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Bearing and Tear-Out | Micro. The plate around a fastener is bounded by the area of material resisting the hole. |
| `Natural Object` `(→ Kind)` Structure `(→ Part)` `Building Block` `(→ Kind)` Structural Connection `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Fatigue | Meso. Repeated action cracks the joint from its stress concentration — the bound that governs bridges and machines. |

**Limitations.** *Scale* — a bolted joint read at the scale of the bolt is itself an assembly, and the same name denotes a different node. *Partial Observability* — a welded joint's internal defects are invisible without inspection, so its real capacity is inferred rather than measured. *Many-Body coupling* — the joint's capacity depends on the members' stiffness as much as on the fastener.

## References

- Heyman, J. (1995). *The stone skeleton*. Cambridge University Press. — the dry joint, and why masonry transmits by contact rather than by tension
- Kulak, G. L., Fisher, J. W., & Struik, J. H. A. (2001). *Guide to design criteria for bolted and riveted joints* (2nd ed.). American Institute of Steel Construction. — slip, bearing, tear-out and fatigue as the four bounds of a fastened joint
- [Structure](/view.html?p=notes/nature/body/structure.md) — the assembly the joint holds together, and the sentence that makes it governing
- [Member](/view.html?p=notes/nature/body/member.md) · [Beam](/view.html?p=notes/nature/body/beam.md) · [Column](/view.html?p=notes/nature/body/column.md) · [Foundation](/view.html?p=notes/nature/body/foundation.md)
- [Load Path](/view.html?p=notes/nature/property/load-path.md) — what the joint re-routes
