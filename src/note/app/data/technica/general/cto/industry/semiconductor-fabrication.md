---
tags: [semiconductor, fab, cpu]
---

# Semiconductor Fabrication

> **Semiconductor Fabrication** is the fabless–foundry–IDM production chain from EDA design through front-end fab to back-end assembly and test, including the CPU concept-to-silicon workflow. Source: Produceologia `docs/Production/Industry/Electronics/Semiconductor/` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Semiconductor Fabrication belongs to the `Production Technical System` technical element type — an organized set of objects realizing integrated-circuit production.**

### What is this technical instance?

> Design in EDA, front-end lithography, etch, and doping, back-end ATP; bottlenecks in EUV, specialty gases, and ultra-pure wafers; value split across design, fab, and ATP with foundry concentration; dynamics in Moore's Law, chiplets, 3D packaging, GaN and SiC, high R&D intensity, and export controls. The CPU workflow runs inside: ISA and microarchitecture, RTL, dominant verification (UVM, formal, emulation), physical design to GDSII, ~80–100-mask fab runs, binning, and burn-in.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one fabrication system, decomposed at shallow depth — root plus chain stages only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Semiconductor Fabrication | IC production chain system. |
| `Production Technical System` → Semiconductor Fabrication → `Technical Practice` | Grouping: chain stages of the system. |
| `Production Technical System` → Semiconductor Fabrication → `Technical Practice` → EDA Design Flow | Schematic-to-tapeout design practice. |
| `Production Technical System` → Semiconductor Fabrication → `Technical Practice` → CPU Design Workflow | ISA-to-package processor practice with dominant verification. |
| `Production Technical System` → Semiconductor Fabrication → `Production Technical Object` | Grouping: plant objects of the system. |
| `Production Technical System` → Semiconductor Fabrication → `Production Technical Object` → Lithography Cell | Pattern-transfer plant object and bottleneck. |
| `Production Technical System` → Semiconductor Fabrication → `Production Technical Object` → ATP Line | Assembly and test plant object. |

## References

- Produceologia `docs/Production/Industry/Electronics/Semiconductor/`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
