---
tags: [ess, storage]
---

# Stationary Energy Storage

> **Stationary Energy Storage** covers large-scale stationary systems versus portable power banks, with metrics, vendors, and loads. Source: Produceologia `docs/Production/Technique/Fisicatecnica/Miscellanea/ESS.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Stationary Energy Storage belongs to the `Production Technical System` technical element type — an organized set of objects realizing buffering capability.**

### What is this technical instance?

> Battery banks (Li-ion, LiFePO4, lead-acid) with BMS, inverter-chargers, and transfer switching, measured in kWh, kW, C-rate, 85–95% efficiency, 2–10k cycles, DoD, millisecond response, and $150–400 per kWh, complementing automobile BMS and EV charging.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one storage system, decomposed at shallow depth — root plus bank, management, conversion, and switching constituents only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Stationary Energy Storage | Stationary buffering system. |
| `Production Technical System` → Stationary Energy Storage → `Constitutive Technical Object` | Grouping: constituents of the system. |
| `Production Technical System` → Stationary Energy Storage → `Constitutive Technical Object` → Battery Bank | Li-ion storage mass object. |
| `Production Technical System` → Stationary Energy Storage → `Constitutive Technical Object` → Battery Management System | Charge-health supervision object. |
| `Production Technical System` → Stationary Energy Storage → `Constitutive Technical Object` → Inverter-Charger | Conversion object between DC and AC. |
| `Production Technical System` → Stationary Energy Storage → `Constitutive Technical Object` → Transfer Switch | Source-selection object. |

## References

- Produceologia `docs/Production/Technique/Fisicatecnica/Miscellanea/ESS.md`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
