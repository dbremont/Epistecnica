---
tags: [note, nature, physical-object, electromagnetism, ontology]
---

# Magnet

> A **magnet** is a body whose elementary magnetic moments are aligned, so that it produces a magnetic field of its own — the alignment is carried by the material, and no current is needed to sustain it.

> The alignment is not absolute. It is held in domains, tolerated only while the coercivity outweighs the field opposing it, and lost above the Curie temperature. A magnet is therefore a body with a *retained* state, not a body with a fixed one: the same piece of alloy, demagnetized, is the same body without the property.

## Formulation

### What natural element type does this natural instance belong to?

`Natural Object` at meso level of organization (Ontic; Existential), specialized through `Substantive` — a fully specified material particular whose magnetization is a property it carries rather than a process it undergoes.

It is **readable as** a `Constitutive Technical Object` in the technica grammar — the component inside a motor rotor, a loudspeaker driver or a sensor — and that reading is recorded as prose, not as a second root. It is **not** a `Property`: magnetization, remanence and coercivity are the properties, and the magnet is their bearer. It is **not** a `Substance / Matter`: NdFeB, ferrite and magnetite are the stuff it is made of. It is **not** a `Natural System`: the [electromagnet](/view.html?p=notes/nature/electromagnet.md) is one — coil, core and driving current taken together — while the magnet is the body that keeps its field after the current is gone.

### What is this natural instance?

> A bar magnet, a horseshoe, a sintered NdFeB block in a rotor, a ferrite ring on the back of a loudspeaker cone, a lodestone. Every one of them is a piece of hard ferromagnetic material whose domains have been swept into a common direction and then pinned there; what distinguishes them is the material's coercivity, which decides how much opposing field the alignment survives.

The distinction that matters is between the body and its field. The [field](/view.html?p=notes/nature/electromagnetic-field-em.md) is what the magnet produces and the [magnetism](/view.html?p=notes/nature/magnetism.md) note studies; the magnet is the bounded particular that produces it, and it can be moved, held, heated and demagnetized while the field it produces changes with it.

### What is the recursive instance decomposition of this natural instance?

> Boundary: one magnetic body, decomposed to the units that carry the magnetization, the stuff they are made of, the properties the body carries and the bounds it must respect — not the field it produces (that is the field note's) and not the current-driven case (that is the electromagnet's).
>
> Identity: paths begin at `Ontic Element`, one labelled link per row; grouping types are `` `code` `` and instances are Title Case; no type terminates a branch; each instance row declares its level of organization.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Kind)` Magnet | Body whose aligned moments produce a magnetic field of its own. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` | Grouping: the units that carry and bound the magnetization. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Kind)` Magnetic Domain | A region in which the moments point one way; the body is a mosaic of them. Micro. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Kind)` Domain Wall | The transition region across which the moment direction turns from one domain to the next. Micro. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Kind)` Magnetic Pole | Grouping: the regions where the field leaves and enters the body. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Kind)` Magnetic Pole `(→ Kind)` North Pole | The region the field leaves; a magnet has one per closed flux path. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Kind)` Magnetic Pole `(→ Kind)` South Pole | The region the field enters; not a separate substance, only the other end of the same alignment. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` | Grouping: the stuff the body is made of. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` NdFeB Alloy | Sintered rare-earth magnet, the highest energy product in commercial use; coercivity falls with heat. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Samarium–Cobalt Alloy | Rare-earth magnet that holds its coercivity at high temperature; weaker than NdFeB at room temperature. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Alnico | Cast or sintered iron–nickel–aluminium–cobalt: modest coercivity, high remanence, stable when hot. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Ceramic Ferrite | Barium or strontium ferrite: cheap, electrically insulating, low energy product. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Magnetite | The naturally occurring iron oxide that magnetizes in the ground; lodestone is the aligned variety. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Attribute)` `Property` | Grouping: what the body carries as a whole. |
| `Natural Object` `(→ Kind)` Magnet `(→ Attribute)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Magnetic Moment | The body's dipole moment, the quantity its field falls off from at distance. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Attribute)` `Property` `(→ Kind)` Magnetization | Moment per unit volume; the state the domains jointly realize. Micro. |
| `Natural Object` `(→ Kind)` Magnet `(→ Attribute)` `Property` `(→ Kind)` Remanence | The field the body retains once the magnetizing field is removed. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Attribute)` `Property` `(→ Kind)` Coercivity | The opposing field the alignment survives — the property that makes a magnet permanent rather than soft. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Attribute)` `Property` `(→ Kind)` Energy Product | The largest $B\cdot H$ the material sustains in the second quadrant; the figure of merit for a magnet. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` | Grouping: the bounds the retained state must respect. |
| `Natural Object` `(→ Kind)` Magnet `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Curie Temperature | Above it the thermal energy overcomes the exchange coupling and the alignment vanishes. Micro. |
| `Natural Object` `(→ Kind)` Magnet `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Demagnetizing Field | The body's own field, opposing its magnetization; the shape sets how strongly. Meso. |
| `Natural Object` `(→ Kind)` Magnet `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Coercive Stability | The operating point must stay inside the second quadrant of the $B$–$H$ loop or the state is lost irreversibly. Meso. |

**Limitations.** *Scale* — the domains are micro and the body is meso, so the same magnet read at the scale of a motor becomes a component of a larger object. *Many-Body coupling* — domains interact through their walls, and neighbouring magnets interact through their fields, so the body's state is not a sum of independent moments. *Partial Observability* — only the external field is measurable; the internal domain pattern is inferred from the loop, not seen.

## Kinds of magnet

What separates the kinds is where the field comes from, not what the body looks like.

| Kind | How it holds its field | Instances |
| --- | --- | --- |
| **Permanent (hard)** | Remanence pinned by coercivity; no supply needed | NdFeB, SmCo, Alnico, ceramic ferrite, lodestone |
| **Soft-core** | No useful remanence; magnetized only while driven | Iron core of a transformer, relay or inductor |
| **Current-driven** | The field comes from a current in a coil, concentrated by a core | Solenoid, lifting magnet, [electromagnet](/view.html?p=notes/nature/electromagnet.md) |
| **Superconducting** | A persistent current in a lossless coil | MRI and accelerator magnets; [levitation](/view.html?p=notes/nature/superconductivity.md) from the same persistent current |

Only the first kind is a magnet in the strict sense — a body that keeps its field once every source is removed. The others are magnets in use, and each is a different composition of body and source.

## Why the alignment holds

Inside the body, $B = \mu_0 (H + M)$: the field measured outside is the applied field plus the material's own magnetization. A permanent magnet is a body with $M \neq 0$ at $H = 0$, which requires the domains to stay aligned against their own demagnetizing field $H_d = -N M$ — the factor $N$ set by the shape, large for a thin plate, small for a long bar. Coercivity is what makes that stability possible, and the energy product $(BH)_{\max}$ is what a designer buys: it fixes how much flux a given volume of material can drive through a gap.

Nothing about it is a source of energy. The field stores energy, and a magnet returns it when the flux path changes — which is why a magnet can hold a load without doing work on it, and why the same magnet in a motor converts electrical to mechanical energy only while the current drives the coils.

## Where they appear

- **Machines** — motors, generators and actuators, where the permanent magnet replaces the field winding and the [electromagnet](/view.html?p=notes/nature/electromagnet.md) becomes unnecessary.
- **Sensing and storage** — Hall and magnetoresistive sensors, [GMR](/view.html?p=notes/nature/giant-magnetoresistance-gmr.md) read heads, and [MRAM](/view.html?p=notes/nature/magnetic-random-access-memory-mram.md), which stores a bit as a magnetization direction.
- **Medicine and research** — [superconducting](/view.html?p=notes/nature/superconductivity.md) magnets for MRI and particle accelerators, where the field is the instrument.
- **Navigation** — lodestone and the compass, the first instrument built on a body that keeps its alignment.

## References

- https://en.wikipedia.org/wiki/Magnet
- [Magnetism](/view.html?p=notes/nature/magnetism.md) — the phenomenon this body produces · [Electromagnet](/view.html?p=notes/nature/electromagnet.md) — the current-driven case · [Electromagnetic Field](/view.html?p=notes/nature/electromagnetic-field-em.md) — the field the body carries
- [Spin](/view.html?p=notes/nature/property/spin.md) — the microscopic moment the alignment is built from · [Electron](/view.html?p=notes/nature/matter/elementary/electron.md) — the particle whose spin and motion produce it
- [Solid State Phenomena](/view.html?p=notes/nature/solid-state-phenomena.md) — the magnetic materials and effects · [Superconductivity](/view.html?p=notes/nature/superconductivity.md) · [Giant Magnetoresistance (GMR)](/view.html?p=notes/nature/giant-magnetoresistance-gmr.md) · [Magnetic Random Access Memory (MRAM)](/view.html?p=notes/nature/magnetic-random-access-memory-mram.md)
- [Physical Object](/view.html?p=notes/nature/body/physical-object.md) — the body family the magnet is a member of · [How to decompose any natural instance?](/view.html?p=notes/philosophia-naturalis-et-operis.md)
