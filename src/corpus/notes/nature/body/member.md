---
tags: [note, nature, physical-object, structural-engineering, ontology]
qa:
 - Is a member a body in its own right, or only a part — and does the answer change when the same member is read at the scale of the joint that holds it?
 - A member is designed for the action it carries; when the load path changes, has the member changed its type or only its state?
---

# Structural Member

> A **structural member** is a body that carries an action along its own span: a bar in tension or compression, a beam in bending, a column in compression, a cable in tension only, a slab or shell in surface action. It is a *building block* of a [structure](/view.html?p=notes/nature/body/structure.md) and, at the same time, a body in its own right — which is why it can be typed twice, as a part of an assembly and as a particular with a shape and a material.

## Formulation

### What natural element type does this natural instance belong to?

`Building Block` at **meso** level of organization (Ontic; Constitutive), licensed on `Natural Object` through `Structure (→ Part) Building Block`, and specialized here to `Structural Member`.

It is **not** the [Structure](/view.html?p=notes/nature/body/structure.md): the structure is the assembly whose load path the members constitute, and a member alone has no path to deliver. It is **not** a `Substance / Matter` — steel and timber are what a member is made of, not what it is. It is **not** a `Property`: the member *carries* strength and stiffness; they are not identical with it.

### What is this natural instance?

> A joist under a floor, a rafter in a roof, a column in a shed, a cable in a suspension bridge, a slab in a car park, a bone in a leg. Each is a body whose geometry is chosen so that the forces it receives at its ends travel along it.

The member's identity is its **action**, not its material or its name. The same steel section is a beam where it bends, a column where it is compressed, and a tie where it hangs: the section is identical and the member is three different things, because the load it carries takes three different forms. This is why the member kinds below are classified by the *state of stress* they are designed for rather than by shape.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the member as a body — its kinds, the attributes that decide its behaviour and the bounds it must respect — not the assembly it sits in, which is decomposed at `structure.md`, and not the theory that predicts its response, which is technica (`structural-mechanics.md`, `euler-bernoulli-beam-theory.md`).
>
> Identity: every Instance Tree Path begins at `Ontic Element`, one labelled link per row; grouping types are `` `code` ``, instances Title Case, no type terminates a branch.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member | Meso. A body carrying an action along its span. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Bar | Meso. Axial action only: a truss member, a tie rod, a strut. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Beam | Meso. Bending action: the [beam](/view.html?p=notes/nature/body/beam.md) carries transverse load by curvature. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Column | Meso. Compression with the risk of [buckling](/view.html?p=notes/nature/body/column.md). |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Cable | Meso. Tension only: the [cable](/view.html?p=notes/nature/body/cable.md) cannot push. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Kind)` Surface Member | Meso. Slab or shell: carrying load in two directions through a surface. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Attribute)` `Property` | Grouping: what the member carries. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Attribute)` `Property` `(→ Instance)` Cross-Section | Meso. The shape that distributes the stress — area for axial action, second moment for bending. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Attribute)` `Property` `(→ Instance)` Span | Meso. The distance between the points that deliver the action to it. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Strength | Micro. The material must not be overstressed at any point of the section. |
| `Natural Object` `(→ Part)` `Building Block` `(→ Kind)` Structural Member `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Stability | Micro. A compressed member must not lose its configuration — the bound that separates a column from a bar. |

**Limitations.** *Scale* — a member read at the scale of its joints is an assembly of plates and bolts, and the same name then denotes a different node. *Many-Body coupling* — a member's ends are restrained by the structure, so its effective behaviour depends on the assembly it is part of. *Partial Observability* — the internal action is inferred from strain at a few instrumented points, rarely measured along the whole span.

## References

- Galilei, G. (1638). *Discorsi e dimostrazioni matematiche intorno a due nuove scienze*. Elzevir. — the first analysis of a member's strength, and the first scaling error in it
- Timoshenko, S. P. (1953). *History of strength of materials*. McGraw-Hill. — the two centuries in which the member became a calculable body
- Gordon, J. E. (1978). *Structures: Or why things don't fall down*. Penguin. — tension, compression and bending read as three ways of carrying a load
- [Structure](/view.html?p=notes/nature/body/structure.md) — the assembly a member constitutes
- [Beam](/view.html?p=notes/nature/body/beam.md) · [Column](/view.html?p=notes/nature/body/column.md) · [Cable](/view.html?p=notes/nature/body/cable.md) · [Connection](/view.html?p=notes/nature/body/connection.md) · [Foundation](/view.html?p=notes/nature/body/foundation.md)
- [Load Path](/view.html?p=notes/nature/property/load-path.md) · [Structural Mechanics](/view.html?p=notes/miscellanea/discipline/structural-mechanics.md)
