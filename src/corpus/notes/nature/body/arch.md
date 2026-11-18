---
tags: [note, nature, physical-object, structural-engineering, ontology]
qa:
 - Is an arch a shape or a path — could the same profile be a beam, and what would make it stop being an arch?
 - Masonry cannot take tension, so the arch survives by never needing to; what happens to the argument when the material can take tension, as in steel or reinforced concrete?
---

# Arch

> An **arch** is a [structure](/view.html?p=notes/nature/body/structure.md) that spans an opening by carrying load **in compression along a curved path** to its supports. The curve is not chosen for its profile but for the path: the arch stands when a line of thrust can be found inside its own material for every load it must carry, and it falls when no such line exists.

## Formulation

### What natural element type does this natural instance belong to?

`Structure` at **meso** level of organization (Ontic; Existential) — a discrete body whose parts are held by a load path, specialized to the spanning-by-compression form.

It is **not** a [beam](/view.html?p=notes/nature/body/beam.md), although the two span the same opening: a beam carries its load in bending, with tension on one face and compression on the other, while an arch carries it in compression throughout. That difference is a difference of *material requirement*: a beam needs a material that can pull, an arch needs only one that can push, which is why masonry and unreinforced concrete build arches and not beams. It is **not** a `Property` (thrust is carried by it, not identical with it), not a `Natural System` (it is one particular with a path, not a set of interacting components), and not the practice that designs it, which is [structural mechanics](/view.html?p=notes/miscellanea/discipline/structural-mechanics.md).

### What is this natural instance?

> A Roman semicircular bridge arch, a Gothic pointed vault rib, a segmental arch over a window, a horseshoe arch, a flat arch over a lintel position, a brick arch in a wall, the stone voussoirs of an aqueduct.

Its behaviour is a single inequality: for the arch to stand, a **line of thrust** — the funicular of the applied loads — must be found that lies entirely within the material. For a masonry arch that is the whole of the theory, because masonry has (almost) no tensile strength: if the thrust line leaves the stone, the joint opens, a hinge forms, and if enough hinges form the arch becomes a mechanism and collapses. The **four-hinge condition** is the standard statement of collapse for a semicircular masonry arch.

Three quantities characterise the form, and each is a design decision with a structural consequence:

- **Span** — the opening it crosses; the wider the span, the larger the thrust for a given rise.
- **Rise** — the height of the crown above the springing. A shallow arch carries its load with a large horizontal **thrust** at the supports and therefore needs strong abutments; a steep one pushes less horizontally and more vertically. This is the trade the buttress, the flying buttress and the tie rod all exist to resolve.
- **Thickness** — the depth of material available for the thrust line to move within as the load varies. A thin arch works only for one load pattern; a thick one tolerates the live load moving across it.

The historical importance is that the arch is the first structural form whose *stability* was reasoned about before its *strength* — first graphically (the funicular polygon), then as a statics problem (Coulomb's thrust), then as the plastic/limit analysis that Heyman formalised. It is the corpus's cleanest case of a body whose capacity is decided by geometry rather than by material.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the arch as a body — its forms, the quantities that characterise it and the bounds it must satisfy — not the practice that designs it, not the abutments' ground, and not the building that contains it.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch | Meso. The spanning body that carries load by compression along a curve. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Kind)` Semicircular Arch | Meso. A half-circle: the Roman form, with the thrust line's geometry fixed by the profile. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Kind)` Segmental Arch | Meso. A circular arc shallower than a half-circle: less rise, more horizontal thrust. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Kind)` Pointed Arch | Meso. Two arcs meeting at a point: the Gothic form, which raises the crown and steepens the thrust near the springing. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Kind)` Flat Arch | Meso. Near-zero rise: an arch that works only within a thick wall, where the thrust line can remain inside the masonry. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Instance)` Voussoir | Meso. The wedge-shaped block: the member of a masonry arch, transmitting compression joint to joint. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Part)` `Building Block` `(→ Kind)` Support `(→ Instance)` Abutment | Meso. The support that receives the thrust — the arch's other half, and its usual point of failure. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Attribute)` `Property` `(→ Instance)` Thrust | Meso. The horizontal force at the springing: the quantity the abutment must take and the reason for buttresses and tie rods. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Attribute)` `Property` `(→ Instance)` Line of Thrust | Meso. The funicular of the applied loads: the curve whose containment inside the material is the condition of standing. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` No Tension | Micro. The material cannot pull, so the thrust line must stay inside the section — the bound that makes the arch a shape problem. |
| `Natural Object` `(→ Kind)` Structure `(→ Instance)` Arch `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Four-Hinge Mechanism | Meso. Four hinges turn the arch into a mechanism: the collapse criterion of the masonry form. |

**Limitations.** *Scale* — an arch read at the scale of its voussoirs is an assembly of blocks and joints, and the same name denotes a different node. *Many-Body coupling* — the arch's stability depends on the abutments, so a sound arch on a moving support is not a sound structure. *Uncertainty* — the thrust line is determined by load history and support movement, so the same arch can be safe under one sequence and not another.

## References

- Coulomb, C. A. (1773). Essai sur une application des règles de maximis et minimis à quelques problèmes de statique relatifs à l'architecture. *Mémoires de mathématique et de physique présentés à l'Académie royale des sciences*, 7, 343–382. — the thrust of an arch treated as a problem of statics
- Heyman, J. (1966). The stone skeleton. *International Journal of Solids and Structures*, 2(2), 249–279. — the three assumptions that make masonry arches analysable: no tension, no sliding, unlimited compressive strength
- Heyman, J. (1995). *The stone skeleton: Structural engineering of masonry architecture*. Cambridge University Press. — the book-length statement, with the four-hinge criterion
- Mainstone, R. J. (1975). *Developments in structural form*. Allen Lane. — the arch among the structural forms, read historically
- Benvenuto, E. (1991). *An introduction to the history of structural mechanics*. Springer. — how the arch's stability was reasoned about before its strength
- [Structure](/view.html?p=notes/nature/body/structure.md) · [Member](/view.html?p=notes/nature/body/member.md) · [Cable](/view.html?p=notes/nature/body/cable.md) — the same equilibrium in tension
- [Load Path](/view.html?p=notes/nature/property/load-path.md) — the funicular the arch is
- [Structural Mechanics](/view.html?p=notes/miscellanea/discipline/structural-mechanics.md) · [Stability Analysis](/view.html?p=notes/miscellanea/discipline/stability-analysis.md)
