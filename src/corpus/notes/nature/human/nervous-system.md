---
tags: [note, nature, natural-system, biology, neuroscience]
qa:
 - Why is "nervous system" not one thing but a grade of organisation?
 - What does a nerve net do that a ganglionated cord does better?
 - How does fast electrical signalling differ from hormonal signalling?
 - Why does the brain cost so much energy for so little mass?
 - What makes a network property more than the sum of its neurons?
 - Why is the peripheral nervous system repairable and the central one not?
---

# Nervous system

> A **nervous system** is a system of excitable cells connected so that a disturbance at one place produces a fast, addressed change somewhere else: a sensor's depolarisation reaching a muscle, a retinal pattern reaching a cortex, a remembered signal returning to the viscera. It is the body's fast-signalling system — the endocrine system broadcasts slowly and to everyone, a nervous system addresses quickly and to one target — and it is the only system whose parts are wired to each other rather than bathed in a common medium.

## Formulation

### What natural element type does this nervous-system instance belong to?

**The nervous system, read as an organised whole, belongs to `Ontic Element (→ Kind) Substantive (→ Kind) Natural System` — a natural system at the meso level.**

Readable secondarily as a `Complex System` where the emphasis falls on emergence rather than on parts: the network's behaviour is not carried by any neuron. Readable again as a `Natural Object` at the coarse grain at which one speaks of *the* nervous system of an animal — the thing a dissection exposes whole. Those readings are prose here, not second roots.

### What is this natural instance?

> **Three grades, not one thing.** A nervous system is a solution to a problem — getting a signal from one place to another quickly — and it has been solved three times, at three grades of organisation, which is why the term covers structures that share almost nothing else.
>
> A **nerve net**, as in cnidarians, is a diffuse mesh of neurons with no centre: a touch anywhere propagates in all directions, and the same net can both sense and drive the body wall. A **ganglionated system**, as in annelids and arthropods, gathers neurons into segmental ganglia joined by connectives, so that signals are routed along defined pathways and the animal can do different things with different segments. A **centralised system**, as in cephalopods and vertebrates, concentrates the circuits at one end into a brain, and separates a central nervous system from a peripheral one that merely carries traffic between centre and body.
>
> The grades replace one another in evolution without abolishing the earlier one: a vertebrate still has the reflex arcs a ganglionated cord already had, and its enteric plexus is a nerve-net-like system embedded in the gut wall, running largely without the brain.

> **What it is made of.** Two cell families. **Neurons** are excitable cells with processes — dendrites collecting input, an axon carrying output — that connect at **synapses**. **Glial cells** do not conduct but make conduction possible: astrocytes buffer ions and metabolites, oligodendrocytes and Schwann cells wrap axons in myelin, microglia police injury and infection, ependyma line the fluid spaces. The classical ratio of about ten glia per neuron is a myth of counting methods; in the human brain the two populations are roughly equal in number, near 86 billion each.

> **How a signal travels.** An axon's membrane holds a resting potential of about −70 mV; a depolarisation past threshold opens voltage-gated sodium channels, and the resulting **action potential** is all-or-none and self-regenerating. In a myelinated fibre it is regenerated only at the nodes of Ranvier, so it jumps — **saltatory conduction** — and speed rises with calibre: from 0.5 m/s in a fine unmyelinated C fibre to 120 m/s in a large myelinated Aα fibre. At the far end, the terminal releases transmitter into the synaptic cleft, and the next cell integrates what arrives.

> **What it does.** The standard division of labour is **sensation** (transduction and afferent transmission), **integration** (convergence, comparison, and the weighting of inputs in circuits), and **motor output** (efferent command to muscle or gland). Autonomic regulation runs the viscera in parallel and largely below awareness. Development builds the wiring — the neural tube and neural crest, axonal pathfinding, activity-dependent pruning, myelination continuing into the third decade — and degeneration tests how much of it can be rebuilt. In the periphery a cut axon regrows; in the central nervous system it generally does not.

> **What it costs.** The human brain is about 2% of body mass and takes roughly 20% of the body's oxygen and glucose at rest. Most of that budget is not the spikes themselves but the pumps that restore the ion gradients the spikes spend — signalling fast is expensive because it is always paying back the disturbance it caused.

> The human instance — its central, peripheral, and autonomic divisions — has its own note, [Human Nervous System](/view.html?p=notes/nature/human/human-nervous-system.md); this note is the type.

### What is the recursive instance decomposition of this natural instance?

> Boundary: one nervous system — the cell types that compose it, the mechanisms that carry and modulate its signals, the processes it performs, and the measurable attributes that identify its grade and capacity. The organism it belongs to, the muscles and organs it acts on, and the endocrine system it works alongside are associated elements with their own notes, not parts of the system.
>
> Stopping rule: a row is terminal when it names a cell type, a signalling mechanism, a process the system performs, or a measurable attribute whose own decomposition lives elsewhere. The neurons it contains are parts, but a single neuron's internal structure belongs to the neuron's note.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the system is **meso**; its cells and synapses are **micro**, and the behaving organism is **macro**. Limitation checklist for the segment: **Complexity** (10¹¹ cells, 10¹⁴ synapses, many cell types), **Emergence** (network properties are in no constituent neuron), **Nonlinearity** (thresholds, oscillations, saturation), **Scale** (molecular events to behaviour, twelve orders of magnitude), **Partial Observability** (the system is never observed whole; recordings are always local and samples), **Many-Body coupling** (every measurement perturbs the circuit it measures).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System | Bound root instance: the wired system of excitable cells of an animal, at whatever grade of organisation. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Part)` `Natural Object` | Grouping: the structural constituents of the system. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Part)` `Natural Object` `(→ Instance)` Neuron | The excitable cell: dendrites collect input, an axon carries output, synapses connect them. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Part)` `Natural Object` `(→ Instance)` Glial Cell | The non-conducting support population: astrocytes, oligodendrocytes and Schwann cells, microglia, ependyma. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Part)` `Natural Object` `(→ Instance)` Nerve | The peripheral bundle of axons with its sheaths and vessels. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Part)` `Natural Object` `(→ Instance)` Ganglion | A cluster of neuron somata outside the central nervous system — the routing node of the ganglionated grades. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Part)` `Natural Object` `(→ Instance)` Nerve Tract | The central counterpart of the nerve: a bundle of axons inside the central nervous system, with oligodendroglial myelin. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Part)` `Natural Object` `(→ Instance)` Neural Circuit | A connected set of neurons whose joint activity performs one function — the unit of organisation above the cell. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Component)` `Mechanism` | Grouping: the mechanisms by which the system carries and changes signals. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Component)` `Mechanism` `(→ Instance)` Action Potential | The all-or-none, self-regenerating spike of the axonal membrane. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Component)` `Mechanism` `(→ Instance)` Synaptic Transmission | Transfer across the junction, chemical at most synapses and electrical at gap junctions. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Component)` `Mechanism` `(→ Instance)` Saltatory Conduction | Regeneration of the spike only at the nodes of Ranvier, so the impulse jumps between them. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Component)` `Mechanism` `(→ Instance)` Reflex Arc | The shortest complete circuit — sensor to interneuron to effector — operating without the brain. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Component)` `Mechanism` `(→ Instance)` Neuromodulation | Volume transmission by amines and peptides that changes how circuits respond rather than what they carry. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Component)` `Mechanism` `(→ Instance)` Long-Term Potentiation | The activity-dependent strengthening of a synapse — the mechanism by which use changes the wiring. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Occurrence)` `Natural Process` | Grouping: the processes the system performs. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Occurrence)` `Natural Process` `(→ Instance)` Sensation | Transduction at receptors and afferent transmission of the result. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Occurrence)` `Natural Process` `(→ Instance)` Integration | Convergence, comparison, and weighting of inputs within circuits — what a centre does that a nerve net does not. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Occurrence)` `Natural Process` `(→ Instance)` Motor Output | Efferent command reaching muscle or gland, and the correction that follows from its consequences. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Occurrence)` `Natural Process` `(→ Instance)` Autonomic Regulation | Involuntary control of the viscera, running largely below awareness and partly without the brain. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Occurrence)` `Natural Process` `(→ Instance)` Development And Myelination | Neural tube and crest, axonal pathfinding, activity-dependent pruning, sheathing into the third decade. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Occurrence)` `Natural Process` `(→ Instance)` Degeneration And Repair | Injury, degeneration, and the asymmetry between peripheral regeneration and central failure. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Attribute)` `Property` | Grouping: measurable attributes of the system. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Attribute)` `Property` `(→ Instance)` Organisation Grade | Diffuse nerve net, ganglionated cords, or centralised system — the attribute that distinguishes the kinds. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Attribute)` `Property` `(→ Instance)` Cephalisation | Concentration of circuits at the anterior end, from the first ganglia to a brain. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Attribute)` `Property` `(→ Instance)` Conduction Velocity | 0.5–2 m/s in unmyelinated C fibres, 70–120 m/s in large myelinated fibres. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Attribute)` `Property` `(→ Instance)` Neuron Number | About 86 billion in the human case: 16 billion cortical, 69 billion cerebellar, the rest in cord and periphery. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Attribute)` `Property` `(→ Instance)` Metabolic Cost | About 2% of body mass and 20% of resting oxygen and glucose in the human case, most of it ion pumping. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Attribute)` `Property` `(→ Instance)` Plasticity | The capacity of the wiring to change with use, over minutes and over a lifetime. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Nervous System `(→ Attribute)` `State` `(→ Instance)` Arousal State | Wake, sleep, and the neuromodulatory setting that gates what the system can do at all. |

## References

- [Nervous system](https://en.wikipedia.org/wiki/Nervous_system) (the grade taxonomy: nerve net, ganglionated, centralised)
- [Neuron](https://en.wikipedia.org/wiki/Neuron) and [Glia](https://en.wikipedia.org/wiki/Glia) (the two cell families)
- Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *The Journal of Physiology, 117*(4), 500–544. https://doi.org/10.1113/jphysiol.1952.sp004764
- Herculano-Houzel, S. (2009). The human brain in numbers: a linearly scaled-up primate brain. *Frontiers in Human Neuroscience, 3*, 31. https://doi.org/10.3389/neuro.09.031.2009
- Sherrington, C. S. (1906). *The integrative action of the nervous system*. Yale University Press.
- Ramón y Cajal, S. (1909–1911). *Histologie du système nerveux de l'homme et des vertébrés*. Maloine.
- Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of neural science* (6th ed.). McGraw Hill.

## Related

- [Human Nervous System](/view.html?p=notes/nature/human/human-nervous-system.md) — the human instance: central, peripheral, and autonomic divisions.
- [Neuron](/view.html?p=notes/nature/human/neuron.md) — the cell the system is built from.
- [Nerve](/view.html?p=notes/nature/human/nerve.md) — the peripheral bundle, and what a tract is not.
- [Synapse in Nervous System](/view.html?p=notes/nature/human/synapse-in-nervous-system.md) — the junction where transmission happens.
- [Myelination](/view.html?p=notes/nature/myelination.md) — the sheathing that buys conduction velocity.
- [Synaptic Plasticity](/view.html?p=notes/nature/synaptic-plasticity.md) — the change of wiring with use.
- [Brain](/view.html?p=notes/nature/human/brain.md) — the centralised grade's organ.
- [Motor System](/view.html?p=notes/nature/human/motor-system.md) — the output side.
- [Endocrine System](/view.html?p=notes/nature/human/endocrine-system.md) — the slow chemical system it works alongside.
- [Early Nervous Systems](/view.html?p=notes/nature/human/early-nervous-systems.md) · [Complex Nervous Systems](/view.html?p=notes/nature/human/complex-nervous-systems.md) · [Modern Nervous Systems](/view.html?p=notes/nature/human/modern-nervous-systems.md) — the comparative and historical members.
