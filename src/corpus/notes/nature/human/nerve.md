---
tags: [note, nature, natural-object, biology, neuroscience, anatomy]
qa:
 - Is a nerve the same thing as a neuron?
 - Why is a bundle of axons in the brain called a tract and not a nerve?
 - Why can a cut nerve regrow and a cut spinal cord not?
 - How did a nerve turn out to be a two-way street?
 - Why do the fastest fibres conduct a hundred times faster than the slowest?
 - What is a nerve's own blood supply, and what happens when it fails?
---

# Nerve

> A **nerve** is an enclosed bundle of axons running outside the central nervous system, together with the Schwann cells that sheath them, the connective tissue that binds them, and the small vessels that feed them. It is the peripheral nervous system's cable: not a cell — the cells are the neurons whose processes it carries — but a **structure** assembled from many fibres, and the unit a surgeon cuts, a graft replaces, or an electrode records from.

## Formulation

### What natural element type does this nerve instance belong to?

**A nerve, read as an anatomical structure, belongs to `Ontic Element (→ Kind) Substantive (→ Kind) Natural Object` — a fully specified material particular at the meso level.**

Readable secondarily as a `Building Block` of the nervous system: the guide licenses the system's parts as natural objects, and a nerve is one of them. Readable again as an `Entity` when a single nerve is counted or tracked — the specimen on a bench, the graft in a repair, the structure under an electrode. Those readings are prose here, not second roots.

### What is this natural instance?

> Three things have to be kept apart, because ordinary language merges them. A **neuron** is a cell. A **nerve fibre** is a single axon with its sheath. A **nerve** is a bundle of fibres, wrapped in three connective layers and supplied by its own vessels. The note [Neuron](/view.html?p=notes/nature/human/neuron.md) takes the cell; this note takes the bundle.
>
> The distinction that follows from it is anatomical rather than verbal. The same structure inside the central nervous system is called a **tract**, and the difference is not nomenclature. Peripheral myelin is made by **Schwann cells**, one cell per internode, and peripheral axons regrow after injury at roughly a millimetre a day. Central myelin is made by **oligodendrocytes**, one cell sheathing many axons, and central axons do not regenerate — the environment inhibits them. A nerve can be cut and repaired; a tract generally cannot.

> **What the bundle contains.** Each fibre runs in a collagen-and-fibroblast sleeve, the **endoneurium**; fibres are gathered into **fascicles** bound by the **perineurium**, whose concentric cell layers form the blood–nerve barrier; the fascicles are bound together into the nerve by the **epineurium**. Its own arterial supply, the **vasa nervorum**, runs in the epineurium and penetrates the fascicles — which is why a nerve can be damaged by ischaemia as well as by section, and why long nerves are more vulnerable than short ones.

> **How it conducts.** In a myelinated fibre the action potential is regenerated only at the **nodes of Ranvier**, so the impulse jumps between nodes rather than crawling along the membrane — saltatory conduction. The gain is large: an Aα fibre of 12–20 µm carries impulses at 70–120 m/s, while an unmyelinated C fibre of under a micrometre manages 0.5–2 m/s. The Erlanger–Gasser classification (Aα, Aβ, Aγ, Aδ, B, C) is essentially a table of calibre against velocity against function, and it is the reason a nerve's fibre composition predicts what it can do.

> **A two-way street.** Bell's 1811 experiments and Magendie's of 1822 established that the dorsal root carries sensory fibres and the ventral root motor fibres — the **Bell–Magendie law**. Most named nerves are therefore *mixed*: the vagus carries both the parasympathetic supply to the viscera and sensory information back from them, and a single spinal nerve carries somatic sensation, motor axons, and sympathetic fibres on their way to the periphery.

> **The named nerves.** Twelve pairs of **cranial nerves** leave the skull, and thirty-one pairs of **spinal nerves** leave the vertebral column — eight cervical, twelve thoracic, five lumbar, five sacral, one coccygeal. Beyond the column they interweave into plexuses and re-sort, so that a nerve's name describes a route rather than an origin. The largest, the **sciatic**, carries fibres for the whole lower limb and reaches about two centimetres across at the hip.

> **After injury.** Cutting an axon separates a distal stump that no longer has a cell body. The stump degenerates within days — **Wallerian degeneration** — while the Schwann cells dedifferentiate, proliferate, and line up in **bands of Büngner** to guide the returning growth cone. Regeneration proceeds at about a millimetre a day, and the outcome depends on the gap, the sheath, and the accuracy of reconnection: a sensory fibre that reinnervates the wrong target produces a mislocalised sensation rather than a restored one. In the central nervous system the same injury produces a persistent deficit, and the inhibitors of the central myelin — Nogo, MAG, OMgp — are the reason a tract is not a repairable nerve.

### What is the recursive instance decomposition of this natural instance?

> Boundary: one nerve — its fibres and sheaths, the mechanisms that conduct and transport along them, the processes it serves, and the measurable attributes by which it is identified. The neurons whose axons it carries, the muscles and organs it reaches, and the nervous system it belongs to are related elements with their own notes, not parts of the nerve.
>
> Stopping rule: a row is terminal when it names a structural constituent, a conduction or transport mechanism, a process the nerve participates in, or a measurable attribute whose own decomposition lives elsewhere.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the nerve is **meso**; the fibres and sheaths composing it are **micro**, and the system it belongs to is **macro**. Limitation checklist for the segment: **Complexity** (three connective layers, two glial arrangements, mixed modalities in one bundle), **Partial Observability** (conduction velocity is inferred from compound action potentials, never measured per fibre), **Scale** (fibre diameters sit at the resolution limit of light microscopy), **Non-Repeatability** (a regeneration trajectory is a one-off, and its success cannot be re-run).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve | Bound root instance: the peripheral bundle of axons with its sheaths and vessels. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` | Grouping: the structural constituents of the bundle. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Nerve Fibre Bundle | The axons the nerve carries — the reason it exists as a structure at all. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Fascicle | A bundle of fibres bound by perineurium; the unit from which a nerve is assembled. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Myelinated Fibre | A large-calibre axon wrapped by Schwann cells, conducting saltatorily. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Unmyelinated Fibre | A small unmyelinated axon, bundled in Remak fibres, conducting continuously and slowly. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Schwann Cell Sheath | The peripheral myelin: one Schwann cell per internode, unlike the central oligodendrocyte. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Endoneurium | The collagen sleeve and capillary bed around each individual fibre. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Perineurium | The concentric cell layers around a fascicle, constituting the blood–nerve barrier. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Epineurium | The outer collagen sheath that binds the fascicles into one nerve. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Part)` `Natural Object` `(→ Instance)` Vasa Nervorum | The intrinsic arterial supply running in the epineurium and penetrating the fascicles. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Component)` `Mechanism` | Grouping: the mechanisms operating in and through the nerve. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Component)` `Mechanism` `(→ Instance)` Saltatory Conduction | Regeneration of the action potential at each node of Ranvier, so the impulse jumps between nodes. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Component)` `Mechanism` `(→ Instance)` Axonal Transport | Fast and slow transport along microtubules, supplying a process far from its soma. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Component)` `Mechanism` `(→ Instance)` Axon Reflex | Antidromic conduction to the terminal and release of transmitters there, independent of the soma. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Component)` `Mechanism` `(→ Instance)` Wallerian Degeneration | Breakdown of the distal stump after section, and the glial dedifferentiation that follows it. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Occurrence)` `Natural Process` | Grouping: the processes the nerve participates in. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Occurrence)` `Natural Process` `(→ Instance)` Sensory Transmission | Afferent signalling from receptors to the central nervous system. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Occurrence)` `Natural Process` `(→ Instance)` Motor Innervation | Efferent drive to skeletal muscle, delivered at the neuromuscular junction. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Occurrence)` `Natural Process` `(→ Instance)` Autonomic Innervation | Sympathetic and parasympathetic fibres reaching the viscera, often travelling inside mixed nerves. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Occurrence)` `Natural Process` `(→ Instance)` Peripheral Regeneration | Regrowth along the bands of Büngner at about a millimetre a day. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Attribute)` `Property` | Grouping: measurable attributes of the structure. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Attribute)` `Property` `(→ Instance)` Fibre Calibre | Diameters from about 0.4 µm in C fibres to 20 µm in Aα fibres. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Attribute)` `Property` `(→ Instance)` Conduction Velocity | 70–120 m/s in Aα fibres, 0.5–2 m/s in C fibres — the calibre–velocity relation in numbers. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Attribute)` `Property` `(→ Instance)` Myelination | Present in A and B fibres, absent in C fibres; the variable that separates the two conduction regimes. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Attribute)` `Property` `(→ Instance)` Modality | Whether the nerve is sensory, motor, or mixed — a fact about its fibre population, not its name. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Attribute)` `Property` `(→ Instance)` Segmental Identity | Twelve cranial pairs and thirty-one spinal pairs: eight cervical, twelve thoracic, five lumbar, five sacral, one coccygeal. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Attribute)` `Property` `(→ Instance)` Nerve Diameter | From a fraction of a millimetre to roughly two centimetres across in the sciatic nerve. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural Object` `(→ Instance)` Nerve `(→ Attribute)` `Property` `(→ Instance)` Injury Response | Regeneration in the periphery, failure in the central tract — the same injury, two outcomes. |

## References

- [Nerve](https://en.wikipedia.org/wiki/Nerve) (the connective sheaths, fibre classes, cranial and spinal nerves)
- [Nerve tract](https://en.wikipedia.org/wiki/Nerve_tract) (the central counterpart, and why the name differs)
- Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *The Journal of Physiology, 117*(4), 500–544. https://doi.org/10.1113/jphysiol.1952.sp004764
- Erlanger, J., & Gasser, H. S. (1937). *Electrical signs of nervous activity*. University of Pennsylvania Press.
- Bell, C. (1811). *Idea of a new anatomy of the brain*. (The dorsal-root experiments behind the Bell–Magendie law.)
- Magendie, F. (1822). Expériences sur les fonctions des racines des nerfs rachidiens. *Journal de physiologie expérimentale et de pathologie, 2*, 276–279.
- Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of neural science* (6th ed.). McGraw Hill.

## Related

- [Neuron](/view.html?p=notes/nature/human/neuron.md) — the cell whose axon the nerve carries.
- [Nervous System](/view.html?p=notes/nature/human/nervous-system.md) — the system the nerve is a part of.
- [Human Nervous System](/view.html?p=notes/nature/human/human-nervous-system.md) — the human instance, with its CNS/PNS division.
- [Synapse in Nervous System](/view.html?p=notes/nature/human/synapse-in-nervous-system.md) — where the fibres end.
- [Myelination](/view.html?p=notes/nature/myelination.md) — the sheathing process whose peripheral agent is the Schwann cell.
- [Muscle](/view.html?p=notes/nature/human/muscle.md) — the effector of motor fibres.
