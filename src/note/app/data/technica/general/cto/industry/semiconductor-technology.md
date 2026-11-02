---
tags: [semiconductors]
---

# Semiconductor Technology

> **Semiconductor Technology** is the device taxonomy for IC-based computation, sensing, and power. Source: Produceologia `docs/Production/Technique/Catalog/Semiconductors.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Semiconductor Technology belongs to the `Technical Element Set` technical element type — the ensemble of semiconductor device families.**

### What is this technical instance?

> Base objects constituting all electronic products: logic (IC, ASIC, SoC, CPU, MCU, GPU, DSP, NPU), programmables (FPGA, CPLD), power (MOSFET, IGBT, SiC, GaN), sensing (MEMS, RF), and memory (DRAM, SRAM, NAND, MRAM).

### What is the recursive instance decomposition of this technical instance?

> Boundary: one domain, decomposed at shallow depth — root plus device families only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Semiconductor Technology Set | IC device domain. |
| `Technical Element Set` → Semiconductor Technology Set → `Constitutive Technical Object` | Grouping: device families of the domain. |
| `Technical Element Set` → Semiconductor Technology Set → `Constitutive Technical Object` → Logic Device Family | IC, ASIC, SoC, CPU, MCU, GPU compute objects. |
| `Technical Element Set` → Semiconductor Technology Set → `Constitutive Technical Object` → Memory Device Family | DRAM, SRAM, NAND, MRAM storage objects. |
| `Technical Element Set` → Semiconductor Technology Set → `Constitutive Technical Object` → Power Device Family | MOSFET, IGBT, SiC, GaN power objects. |
| `Technical Element Set` → Semiconductor Technology Set → `Constitutive Technical Object` → Sensor Device Family | MEMS, RF, mmWave sensing objects. |

## References

- Produceologia `docs/Production/Technique/Catalog/Semiconductors.md`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
