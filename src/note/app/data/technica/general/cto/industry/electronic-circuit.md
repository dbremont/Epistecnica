---
tags: [circuit, eda]
---

# Electronic Circuit

> The **Electronic Circuit** workflow runs end-to-end from specification to fabrication with a full abstraction stack. Source: Produceologia `docs/Production/Technique/Fisicatecnica/Electromagnetic/Circuit/Electronic Circuit.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Electronic Circuit belongs to the `Constitutive Technique` technical element type — an internal dynamic logic establishing how the circuit operates and fulfills its role.**

### What is this technical instance?

> Spec, system, schematic, SPICE, PCB and IC layout, DRC/LVS, prototyping, tape-out and Gerber stages across system, behavioral, RTL, gate, transistor, and physical GDSII levels, tooled by KiCad, Altium, Virtuoso, Verilator, LTspice, Calibre, TSMC, and JLCPCB flows.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one technique, decomposed at shallow depth — root plus stage constituents only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technique` → Electronic Circuit | Spec-to-fabrication circuit technique. |
| `Constitutive Technique` → Electronic Circuit → `Operative Technique` | Grouping: stages of the technique. |
| `Constitutive Technique` → Electronic Circuit → `Operative Technique` → Schematic Capture | Graphical design entry stage. |
| `Constitutive Technique` → Electronic Circuit → `Operative Technique` → SPICE Simulation | Behavioral verification stage. |
| `Constitutive Technique` → Electronic Circuit → `Operative Technique` → PCB Layout | Physical placement and routing stage. |
| `Constitutive Technique` → Electronic Circuit → `Operative Technique` → Tape-Out Release | Fabrication handoff stage. |

## References

- Produceologia `docs/Production/Technique/Fisicatecnica/Electromagnetic/Circuit/Electronic Circuit.md`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
