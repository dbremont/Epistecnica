---
tags: [note, instrument, electrical-measurement, technique]
---

# Ammeter

> An **ammeter** measures electric current by being placed **in series** with the circuit — the current flows through the instrument, and the instrument turns it into a reading. It is the electrical case of the oldest measurement problem: to measure a quantity you must interact with the system, and the interaction changes what you measure.

## How it works

| Variant | Principle | Range and limit |
| --- | --- | --- |
| **Moving-coil galvanometer** | A coil in a magnetic field deflects against a spring; the deflection is proportional to the current | Microamps to milliamps; the ancestor of every analogue meter |
| **Ammeter with shunt** | A low, known resistance bypasses most of the current; the movement reads the remainder | Amps to kiloamps, by choosing the shunt |
| **Digital ammeter** | The voltage drop across an internal resistor is converted and displayed | Wide range with autoranging; limited by the resistor's thermal drift |
| **Clamp meter** | The magnetic field around a conductor induces a current in a transformer, or is read by a Hall sensor | Amps to kiloamps, **without breaking the circuit** — the instrument for mains and field work |

## What it changes

> The shunt is the whole story. To make the current produce a readable voltage, a resistance must be inserted into the circuit, and that resistance dissipates power and drops voltage: the **burden voltage**. In a low-voltage or high-current circuit the meter becomes a significant load, and the reading is systematically low — a *loading error*, which is the electrical form of the measurement-disturbance problem the corpus carries at the level of [measurement theory](/view.html?p=notes/epistemica/quantification/measurement-theory.md).

> Two practical corollaries follow, and both are taught as rules rather than derived. An ammeter is connected **in series**, never across a source — across a source it is a near short circuit, and if the fuse does not save it the circuit will. And a voltmeter is the mirror image: high impedance, in parallel, because its job is to draw as little current as possible. The two instruments are the same movement with different series resistance, which is why the **multimeter** can be both from one set of terminals with a switch.

> The clamp meter is the escape from the dilemma: measuring the magnetic field measures the current without inserting anything, so the burden disappears — at the price of accuracy and of the requirement that the conductor be separable. It is the same trade every non-invasive measurement makes, and the reason clamp meters are the instrument of record for installation work and not for the laboratory.

## In the catalogue

> The instrument belongs to the **current measurement** technique in the [Organon atlas](/corpus/notes/epistemica/observation/organon.html), in the electrical-measurement family, and its reading is only a measurement once the meter is calibrated against a reference — see [Metrology](/view.html?p=notes/technica/general/metrology.md).

## References

- [Ammeter — Wikipedia](https://en.wikipedia.org/wiki/Ammeter)
- [Organon — the observation domain](/corpus/notes/epistemica/observation/organon.html) — the catalogue this instrument belongs to
- [Electronic Circuit](/view.html?p=notes/technica/general/fisicatecnica/electromagnetic/circuit/electronic-circuit.md) — the circuits it measures
- [Electronics](/view.html?p=notes/technica/general/electronics.md) — the discipline
- [Measurement Theory](/view.html?p=notes/epistemica/quantification/measurement-theory.md) — the disturbance the burden voltage embodies
- [Metrology](/view.html?p=notes/technica/general/metrology.md) — calibration, which makes the reading traceable
