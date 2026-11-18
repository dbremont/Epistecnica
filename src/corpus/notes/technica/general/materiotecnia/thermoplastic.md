---
tags: [note, production, materials-science, polymer, plastics, thermoplastic]
---

# Thermoplastic

> A **thermoplastic** is a polymer that softens when heated and re-solidifies when cooled, without a chemical change — the chains are held by entanglement and secondary forces, not by covalent cross-links, so the material can be re-melted and reshaped repeatedly. It is the class that makes extrusion, injection moulding and recycling possible.

> The distinction that matters is not the chemistry but the network: a thermoplastic's chains slide past one another on heating, a thermoset's cannot because they are cross-linked. That single difference decides how the material is processed, whether it can be welded, and whether it can be recycled.

## Formulation

### What technical element type does this technical instance belong to?

**Thermoplastic belongs to the `Constitutive Technical Object` technical element type — a stuff-kind that constitutes larger objects and systems.**

It is a constitutive object because it does not act: it is the material a part is made of, and its properties are the constraints the designer works inside. It is read beside [Polymer](/view.html?p=notes/technica/general/materiotecnia/polymer.md), which owns the general polymer concept; this note owns the meltable class and its boundary against thermosets.

### What is this technical instance?

> Polyethylene, polypropylene, PVC, polystyrene and PET for packaging and consumer goods; polyamide, polycarbonate, POM and ABS for engineering parts; PEEK, PEI, PPS and PTFE where temperature, wear or chemical resistance is the constraint. Each is a chain chemistry with a molecular-weight distribution, a crystallinity, and a processing window — and the window, not the formula, is what the processor buys.

### What is the recursive instance decomposition of this technical instance?

> Boundary: the material class — its families, the structural features that decide its behaviour, the forms it is supplied in, the properties that select it, the processes that shape it and the recycling route. The parts made from it are separate elements.
>
> Stopping rule: a row is terminal when it names a polymer family, a structural attribute, a supplied form, a process or a measured property.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.
>
> Verbs: the material *softens* on heating; the process *shapes* the melt; the recycler *re-melts* it.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technical Object` → Thermoplastic | A polymer that can be repeatedly melted and reshaped. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` | Grouping: the polymer families. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → Polyethylene | PE: the largest-volume commodity polymer, from film to pipe. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → Polypropylene | PP: stiff, fatigue-resistant, the packaging and automotive workhorse. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → PVC | Rigid or plasticised, the pipe and cable material. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → Polystyrene and ABS | Amorphous commodity and rubber-toughened engineering grades. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → PET and Polyester | The bottle, fibre and film polymer. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → Polyamide | Nylon: the engineering thermoplastic of gears, bearings and fibres. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → Polycarbonate | Transparent, tough, dimensionally stable — the optical and housing grade. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → PEEK and PPS | High-temperature, chemically resistant semi-crystalline grades. |
| `Constitutive Technical Object` → Thermoplastic → `Constitutive Technical Object` → PTFE | Fluoropolymer: the lowest friction and the highest chemical inertness. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Parameter` | Grouping: the properties that select the material. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Parameter` → Glass Transition Temperature | Tg: where the amorphous fraction softens, the service ceiling for amorphous grades. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Parameter` → Melting Temperature | Tm: where the crystalline fraction melts, the processing floor for semi-crystalline grades. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Parameter` → Crystallinity | The semi-crystalline fraction, fixing stiffness, opacity, barrier and shrinkage. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Parameter` → Melt Flow Index | The flow at a stated temperature and load — the processor's first specification. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Parameter` → Molecular Weight | Chain length, trading toughness against processability. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Parameter` → Service Temperature | The continuous-use ceiling, set by Tg, Tm and oxidation. |
| `Constitutive Technical Object` → Thermoplastic → `Attribute` | Grouping: the behavioural attributes of the class. |
| `Constitutive Technical Object` → Thermoplastic → `Attribute` → Re-meltability | The defining property: no cross-links, so heat reverses the shaping. |
| `Constitutive Technical Object` → Thermoplastic → `Attribute` → Weldability | The ability to join by melting the interface — hot plate, ultrasonic, laser, friction. |
| `Constitutive Technical Object` → Thermoplastic → `Attribute` → Recyclability | Mechanical re-processing, and the degradation that limits the number of cycles. |
| `Constitutive Technical Object` → Thermoplastic → `Attribute` → Anisotropy | The chain orientation that processing induces, and the shrinkage it causes. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Task` | Grouping: the processes that shape it. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Task` → Extrude | Melt and push through a die — film, sheet, pipe, profile, fibre. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Task` → Inject | Fill a closed mould — the discrete-part process. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Task` → Blow Mould | Inflate a parison against a mould — bottles and hollow parts. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Task` → Thermoform | Heat a sheet and draw it over a mould — packaging and panels. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Task` → Additive Manufacture | Deposit or sinter the melt layer by layer. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Constraint` | Grouping: the bounds the material imposes. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Constraint` → Processing Window | The temperature and shear range between degradation and incomplete melting. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Constraint` → Shrinkage | Crystalline grades shrink on cooling, so the mould is cut oversize. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Constraint` → Creep and Ageing | Sustained load and environmental attack limit the service life. |
| `Constitutive Technical Object` → Thermoplastic → `Technical Constraint` → Recyclate Quality | Each melt cycle shortens the chains and narrows the usable grades. |

## Amorphous and Semi-Crystalline

| Class | Structure | Behaviour on heating | Examples |
| --- | --- | --- | --- |
| **Amorphous** | Disordered chains, no melting point | Softens gradually through Tg; transparent | PS, PVC, PC, PMMA, ABS |
| **Semi-crystalline** | Ordered domains in an amorphous matrix | Sharp Tm; opaque or translucent; shrinks on cooling | PE, PP, PET, PA, PEEK, POM |

> The distinction is the designer's first decision. An amorphous grade gives transparency and dimensional stability; a semi-crystalline one gives chemical resistance, fatigue resistance and a sharp processing window. The same polymer can be either — PET is amorphous in a bottle and semi-crystalline in a fibre — depending on how it is cooled.

## The Families

| Grade class | Service ceiling | Character | Where it is used |
| --- | --- | --- | --- |
| **Commodity** | ~60–100 °C | Cheap, high volume, commodity processing | Packaging, films, pipes, housewares |
| **Engineering** | ~100–150 °C | Stiff, tough, dimensionally stable | Gears, housings, bearings, automotive |
| **High-performance** | 150–260 °C+ | Chemical and thermal resistance, low friction | Aerospace, medical, electrical, oil and gas |

## Processing and Joining

> Every thermoplastic process is the same sequence — dry, melt, shape, cool, eject — and every one is a competition between the melt's viscosity and the cooling that freezes it. Extrusion runs continuously; injection moulding fills and freezes a cavity; blow moulding inflates; thermoforming stretches a sheet. The cycle time is the cooling time, and the cooling time is the section thickness squared.

> Joining is where the thermoplastic's defining property pays off: the interface can be re-melted, so the part can be welded — hot plate, ultrasonic, vibration, laser or friction — instead of glued or fastened. That is what a thermoset cannot do, and it is why the material choice and the assembly method are the same decision.

## Thermoplastic and Thermoset

| Property | Thermoplastic | Thermoset |
| --- | --- | --- |
| **Network** | Entangled chains, secondary forces | Covalent cross-links |
| **On heating** | Softens, re-melts | Degrades, does not melt |
| **Joining** | Weldable | Adhesive or mechanical |
| **Recycling** | Mechanical re-processing, limited cycles | Difficult, usually energy recovery |
| **Dimensional stability at temperature** | Limited by Tg/Tm | High until decomposition |
| **Typical examples** | PE, PP, PET, PA, PC, PEEK | Epoxy, phenolic, polyurethane, unsaturated polyester |

## What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Thermoplastic**, defined above as *a polymer that softens on heating and re-solidifies without chemical change, because its chains are not covalently cross-linked*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: the class is separated from thermosets (cross-linked), elastomers (lightly cross-linked and elastic) and from the individual polymers it contains. Definitional Clarity — **pass**: the defining criterion — reversible melting without chemical change — is operational and testable. Conceptual Determinacy — **pass with qualification**: the boundary against a thermoplastic elastomer is a matter of degree of cross-linking and of service temperature, and the note states that it is a spectrum rather than a binary; the descriptive name is a processing class, not a chemical family. Internal Consistency — **pass**: families, parameters, attributes, processes and constraints are distinct branches; the individual polymer notes are the instances. Representational Adequacy — **qualified**: complete for the class and its selection criteria; the specific grades, the processing equipment and the recycling economics are links. Purpose Adequacy — **pass**: shaped for material selection and process choice — every leaf is a family, a property, a process or a constraint.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from thermosets, elastomers and the individual polymer instances. |
| Definitional Clarity | pass | Reversible melting without chemical change is operational and testable. |
| Conceptual Determinacy | pass (qualified) | The elastomer boundary is a degree of cross-linking; a processing class, not a chemical family. |
| Internal Consistency | pass | Families, parameters, attributes, processes and constraints are separate branches. |
| Representational Adequacy | qualified | Complete for the class and selection; grades, equipment and recycling economics are links. |
| Purpose Adequacy | pass | Every leaf serves material selection or process choice. |

## References

- [Thermoplastic](https://en.wikipedia.org/wiki/Thermoplastic)
- [Polymer](https://en.wikipedia.org/wiki/Polymer) · [Thermosetting polymer](https://en.wikipedia.org/wiki/Thermosetting_polymer)
- [Polyethylene](https://en.wikipedia.org/wiki/Polyethylene) · [Polypropylene](https://en.wikipedia.org/wiki/Polypropylene) · [Polyethylene terephthalate](https://en.wikipedia.org/wiki/Polyethylene_terephthalate)
- [Polyamide](https://en.wikipedia.org/wiki/Polyamide) · [Polycarbonate](https://en.wikipedia.org/wiki/Polycarbonate) · [PEEK](https://en.wikipedia.org/wiki/Polyether_ether_ketone)
- [Polymer](/view.html?p=notes/technica/general/materiotecnia/polymer.md) — the polymer concept this class specializes
- [Plastics Production](/view.html?p=notes/technica/production/industry/plastics-production.md) — the production system that shapes it
- [Physical Material Technology](/view.html?p=notes/technica/general/physical-material-technology.md) — the materials system, with the polymer and processing rows
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
