---
tags: [eda, toolchain]
---

# Electronic Design Automation

> **Electronic Design Automation** is the toolchain taxonomy for schematic, PCB, IC, verification, and physical signoff. Source: Produceologia `docs/Production/Technique/Fisicatecnica/Electromagnetic/Design/` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Electronic Design Automation belongs to the `Technical Element Set` technical element type — the ensemble of design and verification tools.**

### What is this technical instance?

> OrCAD and KiCad capture, Altium, Eagle, and PCBnew layout, Virtuoso custom design, Verilator, Vivado, Quartus, ModelSim, and QuestaSim simulation, Design Compiler, Genus, IC Compiler II, Innovus, PrimeTime, Spectre, HSPICE, HFSS, and COMSOL signoff — supporting circuits, PCBs, SoCs, FPGAs, and MEMS-photonics.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one toolchain, decomposed at shallow depth — root plus tool families only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Electronic Design Automation Set | Circuit design toolchain ensemble. |
| `Technical Element Set` → Electronic Design Automation Set → `Production Virtual Technical Object` | Grouping: tool families of the chain. |
| `Technical Element Set` → Electronic Design Automation Set → `Production Virtual Technical Object` → Schematic Editor | Design-entry tool family. |
| `Technical Element Set` → Electronic Design Automation Set → `Production Virtual Technical Object` → PCB Layout Tool | Placement and routing tool family. |
| `Technical Element Set` → Electronic Design Automation Set → `Production Virtual Technical Object` → Logic Simulator | Verification tool family. |
| `Technical Element Set` → Electronic Design Automation Set → `Production Virtual Technical Object` → Signoff Suite | Timing and physics closure tool family. |

## References

- Produceologia `docs/Production/Technique/Fisicatecnica/Electromagnetic/Design/`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
