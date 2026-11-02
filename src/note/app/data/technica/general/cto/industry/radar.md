---
tags: [radar]
---

# Radar

> **Radar** is the active RF and microwave system inferring position and velocity from echoes. Source: Produceologia `docs/Production/Technique/Fisicatecnica/Electromagnetic/Radar.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Radar belongs to the `Production Technical Object` technical element type — a produced object enabling detection action.**

### What is this technical instance?

> Transmitter, antenna, receiver, signal processor, and display in pulse, CW, Doppler, phased-array, SAR, ISAR, and GPR forms — from automotive 4D imaging to over-the-horizon and bistatic configurations.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one object, decomposed at shallow depth — root plus constitutive constituents only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical Object` → Radar | Active echo-location object. |
| `Production Technical Object` → Radar → `Constitutive Technical Object` | Grouping: constituents of the radar. |
| `Production Technical Object` → Radar → `Constitutive Technical Object` → Transmitter Module | RF energy source of the pulse. |
| `Production Technical Object` → Radar → `Constitutive Technical Object` → Antenna Array | Radiating and receiving aperture. |
| `Production Technical Object` → Radar → `Constitutive Technical Object` → Signal Processor | Echo-to-track computation object. |
| `Production Technical Object` → Radar → `Operative Technique` | Grouping: operating modes of the radar. |
| `Production Technical Object` → Radar → `Operative Technique` → Pulse-Doppler Sweep | Velocity-resolving scan mode. |

## References

- Produceologia `docs/Production/Technique/Fisicatecnica/Electromagnetic/Radar.md`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
