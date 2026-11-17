---
tags: [note, nature, physical-object, structural-engineering, ontology]
qa:
 - A cable can only pull; is that a limitation of the material or of the member — could a cable be made to push?
 - The arch and the cable are the same equilibrium argument with opposite sign; does the corpus need both notes, or one note with two signs?
---

# Cable

> A **cable** is a [structural member](/view.html?p=notes/nature/body/member.md) that carries load in **tension only**. It cannot push: any compressive action slackens it and it stops carrying. Its shape is not chosen but found — the cable takes the form of the funicular polygon of the loads it carries, which is why a hanging chain is a calculation and not an ornament.

## Formulation

### What natural element type does this natural instance belong to?

`Structural Member` at **meso** level of organization (Ontic; Constitutive) — a `Building Block` of a [structure](/view.html?p=notes/nature/body/structure.md), specialized to the tension-only case.

It is **not** a `Bar`: a bar is the idealised axial member that may carry tension *or* compression, and a cable is the case where the compression branch simply does not exist. It is **not** the [beam](/view.html?p=notes/nature/body/beam.md), which carries bending and therefore a moment; a cable carries no moment at all, which is exactly why it is efficient — every fibre works in tension instead of only the extreme ones. It is **not** the [arch](/view.html?p=notes/nature/body/arch.md), though it is its dual: the arch is a compressive funicular, the cable a tensile one, and the two are the same statement about equilibrium with the sign of the thrust reversed.

### What is this natural instance?

> A suspension-bridge main cable, a stay, a guy rope, a tie rod, a spider's thread, a clothes line. Every one of them carries load by being pulled, and every one changes shape until the pull is constant along its length.

The mechanics is a single geometric fact with three consequences. A cable with no stiffness in bending takes, under a distributed load, the shape of the **catenary** — or the **parabola** when the load is uniform horizontally, as with a bridge deck — and the tension is the **thrust** of that funicular curve. The consequences:

- **Sag is not decoration.** The horizontal component of tension is constant along the cable and equals the load per unit length divided by the curvature; more sag means less tension for the same load. A taut cable and a slack one carry the same load at very different tensions.
- **Stiffness comes from geometry, not from the material.** A cable resists transverse load only by changing shape, so its transverse stiffness grows with the tension it carries. This is why a pretensioned tie is far stiffer than a slack one, and why a cable structure is only stable once it is loaded.
- **The structure must supply the compression.** A cable pulls its supports toward each other, so a cable-stayed or suspended structure needs something to take that thrust: an anchor, a mast, or a ring in compression.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the tension-only member — its structural roles, the quantities that decide its behaviour and the bounds it must respect — not the assembly that anchors it, and not the theory of funicular curves, which belongs with the arch and the load path.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable | Meso. The tension-only member. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable `(→ Kind)` Main Cable | Meso. Suspension: the cable carries the deck through hangers and delivers the load to the towers. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable `(→ Kind)` Stay | Meso. A straight cable from deck to mast, taking a share of the deck load — the cable-stayed form. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable `(→ Kind)` Tie | Meso. A pretensioned cable that holds two parts together and supplies the stability of a frame. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable `(→ Attribute)` `Property` `(→ Instance)` Sag | Meso. The dip that sets the horizontal tension for a given load. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable `(→ Attribute)` `Property` `(→ Instance)` Pretension | Meso. The tension before any external load — what makes a slack cable into a stiff member. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` No Compression | Micro. In compression the member slackens and stops carrying: the bound that defines the type. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Tensile Capacity | Micro. The strength bound: the cable fails by breaking, and nowhere else. |

**Limitations.** *Nonlinearity* — the response is geometrically nonlinear even with a linear-elastic material, because the shape changes as it loads. *Many-Body coupling* — the cable's tension is set by what it is anchored to, so its behaviour is not a property of the cable alone. *Scale* — at the scale of the strands a cable is itself a structure, and the same name denotes a different node.

## References

- Irvine, H. M. (1981). *Cable structures*. MIT Press. — the static and dynamic theory of cables, where the geometric stiffness is derived
- Heyman, J. (1995). *The stone skeleton*. Cambridge University Press. — the funicular argument, shared with the arch from the other side
- Gordon, J. E. (1978). *Structures: Or why things don't fall down*. Penguin. — tension as the one action every fibre can carry
- [Arch](/view.html?p=notes/nature/body/arch.md) — the same equilibrium, in compression
- [Load Path](/view.html?p=notes/nature/property/load-path.md) — what the cable's shape traces
- [Member](/view.html?p=notes/nature/body/member.md) · [Beam](/view.html?p=notes/nature/body/beam.md) · [Column](/view.html?p=notes/nature/body/column.md) · [Structure](/view.html?p=notes/nature/body/structure.md)
