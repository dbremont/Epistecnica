---
tags: [automobile, vehicle]
---

# Automobile System

> The **Automobile System** is the MCU-centric decomposition of vehicle functions from ECU fuel control to ADAS sensor fusion. Source: Produceologia `docs/Production/Technique/Fisicatecnica/Mechanical/Automolbile-System.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Automobile System belongs to the `Production Technical System` technical element type — an organized set of objects realizing transport capability.**

### What is this technical instance?

> ECU fuel and ignition, transmission, ABS and ESC brake-by-wire, airbag, TPMS, BMS and EV charging, infotainment, lighting, power steering, HVAC, and ADAS LiDAR-radar-camera fusion.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one vehicle system, decomposed at shallow depth — root plus function domains only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Automobile System | MCU-centric vehicle function system. |
| `Production Technical System` → Automobile System → `Constitutive Technical Object` | Grouping: function domains of the vehicle. |
| `Production Technical System` → Automobile System → `Constitutive Technical Object` → Engine Control Unit | Fuel and ignition management object. |
| `Production Technical System` → Automobile System → `Constitutive Technical Object` → Braking Control Set | ABS, ESC, and brake-by-wire objects. |
| `Production Technical System` → Automobile System → `Constitutive Technical Object` → Battery Management System | EV charge and health object. |
| `Production Technical System` → Automobile System → `Constitutive Technical Object` → ADAS Fusion Stack | LiDAR, radar, and camera fusion object. |

## References

- Produceologia `docs/Production/Technique/Fisicatecnica/Mechanical/Automolbile-System.md`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
