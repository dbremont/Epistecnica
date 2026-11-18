---
tags: [note, gan, wide-bandgap, semiconductor]
---

# Gallium Nitride

> **Gallium Nitride** is the synthetic wide-bandgap (3.4 eV) compound for efficient high-voltage, high-frequency power, RF, and optoelectronics. Source: Produceologia `docs/Foundation/semiconductor/Gallium-Nitride-GaN.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Gallium Nitride belongs to the `Constitutive Technical Object` technical element type — a compound constituting devices beyond silicon.**

### What is this technical instance?

> GaN FETs and converters for power supplies, RF amplifiers and phased arrays for 5G, radar, and satellites, GaN consumer chargers, and blue and UV LEDs and lasers — switching 10–100x faster than silicon at high efficiency.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one compound, decomposed at shallow depth — root plus device applications only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technical Object` → Gallium Nitride | Wide-bandgap device compound. |
| `Constitutive Technical Object` → Gallium Nitride → `Constitutive Technical Object` | Grouping: device applications. |
| `Constitutive Technical Object` → Gallium Nitride → `Constitutive Technical Object` → GaN Power FET | Fast-switching conversion object. |
| `Constitutive Technical Object` → Gallium Nitride → `Constitutive Technical Object` → RF Amplifier Module | High-frequency transmission object. |
| `Constitutive Technical Object` → Gallium Nitride → `Constitutive Technical Object` → GaN Charger | Compact consumer power object. |
| `Constitutive Technical Object` → Gallium Nitride → `Constitutive Technical Object` → Blue LED Emitter | Solid-state lighting object. |

## Gallium Nitride as a Compound

> Gallium nitride is a **synthetic chemical compound** — a **semiconductor material** used in high-performance electronics. It is not found naturally in large quantities but is **manufactured in labs or factories** for industrial use.

> Gallium Nitride (GaN) is a wide-bandgap semiconductor material that has become a key technology for next-generation power electronics, RF (radio frequency) devices, and optoelectronics.

**Gallium nitride (GaN) is not a chemical element.** It is a **compound** made from two elements:

| Element  | Symbol | Role                 |
| -------- | ------ | -------------------- |
| Gallium  | **Ga** | Metal (Group 13)     |
| Nitrogen | **N**  | Non-metal (Group 15) |

## Basic Properties

| Property                 | Value / Description                         |
| ------------------------ | ------------------------------------------- |
| **Chemical Formula**     | GaN                                         |
| **Crystal Structure**    | Wurtzite (hexagonal) or zinc blende (cubic) |
| **Bandgap**              | ~3.4 eV (wide bandgap)                      |
| **Breakdown Voltage**    | High (can handle high voltages)             |
| **Thermal Conductivity** | Moderate (~130 W/m·K)                       |
| **Electron Mobility**    | High                                        |
| **Saturation Velocity**  | High                                        |

### Why GaN Matters

#### High Efficiency

* Because of its **wide bandgap**, GaN can operate at **higher voltages, frequencies, and temperatures** than silicon (Si).
* It enables smaller, faster, and more efficient **power devices** (like transistors, inverters, and converters).

#### Fast Switching

* GaN switches **10-100x faster** than silicon, reducing energy loss and improving performance in:

  * Power adapters (for phones, laptops, EVs)
  * Data centers and 5G base stations
  * High-efficiency LED lighting
  * Aerospace and defense (radar, satellites)

#### High Frequency

* GaN is ideal for **RF and microwave applications**: it's used in **radars, 5G, satellite communications**, and electronic warfare.

## Key Applications

| Sector                   | GaN Use Case                                       |
| ------------------------ | -------------------------------------------------- |
| **Power Electronics**    | Transistors (GaN FETs), converters, power supplies |
| **Telecom & 5G**         | RF amplifiers, phased array antennas               |
| **Consumer Electronics** | GaN chargers (smaller, faster)                     |
| **Defense & Aerospace**  | Radar, high-power RF                               |
| **LEDs & Lasers**        | Blue/UV LEDs, Blu-ray, solid-state lighting        |

## GaN vs. Silicon (Si) and Silicon Carbide (SiC)

| Feature             | GaN                               | SiC                            | Si                                   |
| ------------------- | --------------------------------- | ------------------------------ | ------------------------------------ |
| **Bandgap**         | 3.4 eV                            | 3.2 eV                         | 1.1 eV                               |
| **Switching Speed** | Very high                         | Moderate                       | Low                                  |
| **Efficiency**      | Very high                         | High                           | Moderate                             |
| **Cost**            | High but dropping                 | High                           | Low                                  |
| **Best for**        | High-frequency, low- to mid-power | High-power, moderate-frequency | Low- to moderate-performance devices |

## Who Buys GaN and In What Form?

Most companies do not buy raw GaN — they purchase:

1. GaN Wafers (for chip fabrication)
    - Example: Apple buys GaN-on-silicon wafers for fast chargers.
2. GaN Power Transistors/ICs (ready-to-use components)
    - Example: Anker uses GaN ICs from Navitas in its chargers.
3. GaN RF Devices (for 5G, radar)
    - Example: Qualcomm buys GaN RF chips for 5G base stations.

Can You Buy GaN Directly?

- No (for consumers) — GaN is sold as part of finished products (e.g., chargers, LEDs).
- Yes (for businesses) — companies like Wolfspeed sell GaN wafers to semiconductor fabs.

## References

- Produceologia `docs/Foundation/semiconductor/Gallium-Nitride-GaN.md`
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md)
