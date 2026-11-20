---
tags: [note, ess, storage]
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

## Battery Energy Storage Systems

> A **BESS** is a battery array with its power conversion and control system, deployed as a grid asset. Lithium-ion dominates the grid market for the same reason it dominates vehicles — a cost curve that fell faster than any alternative — and the deployment is justified by the services it sells rather than by the energy it holds.

| Service | What it does | Why a battery wins |
| --- | --- | --- |
| **Frequency response** | Injects or absorbs power in milliseconds to hold grid frequency | Faster than any thermal plant; paid for availability |
| **Energy arbitrage** | Charges cheap, discharges at peak | Profitable only where the price spread exceeds the round-trip cost |
| **Capacity / firming** | Substitutes for peaking plant; firms renewables | Quick to build and locate |
| **Congestion and constraint management** | Defers a network upgrade | Cheaper than new copper |

> Three engineering realities set the asset's life. **Degradation** — capacity fades with cycling and calendar age, so the system is designed with augmentation in mind (extra racks or spare capacity added later). **Thermal management and fire safety** — a failing cell is a thermal runaway, which is why the safety codes, separation distances and suppression systems around grid batteries were written after the fires. **Round-trip efficiency and duration** — the economics depend on how many hours the battery is asked to run, which is why the market separates short-duration (frequency, arbitrage) from long-duration (which batteries mostly do not yet serve).

## References

- Produceologia `docs/Production/Technique/Fisicatecnica/Miscellanea/ESS.md`
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md)
- [Battery Technology Domain](/view.html?p=notes/technica/general/battery-technical-domain.md)
- [Battery Industry](/view.html?p=notes/technica/production/industry/battery/readme.md)
- [Battery Energy Storage System — Wikipedia](https://en.wikipedia.org/wiki/Battery_energy_storage_system)
