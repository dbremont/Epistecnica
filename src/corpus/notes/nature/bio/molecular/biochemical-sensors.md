---
tags: [note, nature, bio, molecular, property, sensing]
---

# Biochemical Sensors

> **Biochemical sensing** is the natural interaction a biosensor exploits: a biological recognition element — a protein, an enzyme, an antibody, a nucleic-acid sequence, a membrane receptor — binds a target molecule, and that binding changes some measurable physical state of the system: a charge distribution, a refractive index, a mass, a fluorescence yield, a heat flux. The *interaction* is natural; the instrument built around it is not.

## Formulation

### What natural element type does this natural instance belong to?

`Property` at micro level of organization (Ontic; Qualitative) — and more precisely an `Interaction-Derived Quantity`, the guide's kind for a "joint-state quantifier over two or more independent variables". The quantity belongs to the pair (recognition element, analyte), not to either alone: an antibody has an affinity only *for* an antigen.

It is **not** a `Natural System`: nothing self-maintains here, and the recognition element in a sensor is immobilized, isolated from the cell that normally regulates it. It is **not** the instrument: the device that reads this interaction is a technical element, decomposed in [Biosensor](/view.html?p=notes/technica/general/biosensor.md). The earlier reading of this note as a `Natural System` conflated the two and is superseded.

### What is this natural instance?

> The conformational change when an antibody meets its epitope; the electron transfer when an enzyme oxidises its substrate at an electrode; the hybridization of a probe strand with its complement; the shift in a ring resonator's resonance when a protein layer thickens. Each is a state change of the recognition pair, and each is what a transducer registers.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the interaction, its participants and the physical quantity it changes — not the instrument. The instrument's architecture is decomposed in `technica/general/biosensor.md`.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row; grouping types are `` `code` ``, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` | Grouping: quantities that belong to a joint state rather than to one element. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Binding Affinity | The strength of the recognition pair's association, reported as a dissociation constant. Micro. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Catalytic Rate | The turnover an enzyme produces on its substrate once bound. Micro. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Electron Transfer | The charge movement a redox recognition event produces at an electrode. Micro. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Attribute)` Property | Grouping: what the interaction carries into the measurement. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Attribute)` Property `(→ Instance)` Specificity | Whether the recognition element distinguishes the target from structurally similar molecules. Micro. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Attribute)` Property `(→ Instance)` Reversibility | Whether the pair dissociates and can be read again, or binds irreversibly. Micro. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Has)` `Observable` | Grouping: the physical states a transducer can register. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Has)` `Observable` `(→ Instance)` Current | The faradaic or capacitive signal of an electrochemical transducer. Micro. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Has)` `Observable` `(→ Instance)` Refractive Index Shift | The optical signal of a label-free transducer. Micro. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Has)` `Observable` `(→ Instance)` Resonance Frequency | The mass-loading signal of a piezoelectric transducer. Micro. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Has)` `Observable` `(→ Instance)` Fluorescence Yield | The optical signal of a labelled assay. Micro. |

**Limitations.** *Scale* — the interaction is molecular, while what it moves is macroscopic (a current, a resonance). *Partial Observability* — only the transduced part of the interaction is seen; the rest of the binding is inferred. *Uncertainty* — a single binding event is stochastic, so the measurement is a rate over a population.

## References

- [How to decompose any natural instance?](/view.html?p=notes/philosophia-naturalis-et-operis.md)
- [Protein](/view.html?p=notes/nature/bio/molecular/protein.md) — the recognition element's usual material
- [Living System](/view.html?p=notes/nature/bio/organism/living-system.md) — the organization the element is taken from
- [Biosensor](/view.html?p=notes/technica/general/biosensor.md) — the technical element built on this interaction
- https://en.wikipedia.org/wiki/Biosensor
