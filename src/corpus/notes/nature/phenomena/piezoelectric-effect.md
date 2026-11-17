---
tags: [note, nature, phenomenon, coupling, materials]
qa:
 - A crystal produces a voltage when squeezed and changes shape when charged; is that one effect with two directions or two effects that share a material?
 - The effect requires a crystal with no centre of symmetry — what does that single structural condition exclude, and why is it decisive rather than incidental?
 - Quartz clocks, ultrasound probes and gas lighters all rely on it; what does that say about the phenomenon — a curiosity of minerals, or the standard converter between mechanical and electrical?
---

# Piezoelectric Effect

> The **piezoelectric effect** is the coupling of mechanical strain and electric charge in a crystal that lacks a centre of symmetry: squeeze it and a voltage appears across it (**direct** effect); apply a voltage and it changes shape (**converse** effect). The two are not two phenomena but one coupling read in two directions, and the existence of either requires the same structural condition.

> That condition is the whole story. In a crystal with a centre of symmetry, a compression that reverses the crystal also reverses every polarisation it could produce, so the two contributions cancel and no voltage appears. Remove the centre of symmetry and the cancellation fails by construction — which is why the effect is found in quartz, in tourmaline, in barium titanate ceramics and in aluminium nitride, and not in table salt.

## Formulation

### What natural element type does this natural instance belong to?

`Coupling Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to a conversion between a mechanical and an electrical state.

It is **not** a `Property` of the crystal, although it depends on one (the absence of a symmetry centre): the phenomenon is the *conversion*, and the property is the structure that permits it. It is **not** **thermoelectricity**, its close relative: there the coupled quantities are heat and charge, and the structural condition is a carrier population rather than a crystal class. It is **not** a `Process` — quartz does not change; it responds.

### What is this natural instance?

> The spark of a gas lighter, struck from a piezoelectric button; a quartz watch, whose resonator is a tuning fork cut from the crystal; the transducer in an ultrasound probe, running in both directions — transmit by driving it, receive by listening; a sonar array; an inkjet nozzle that deforms to eject a drop; a knock sensor on an engine; a scanning tunnelling microscope's sub-nanometre positioner.

Three facts organise the phenomenon:

- **It is reversible and fast.** The coupling works in both directions in the same material, and its response time is acoustic — microseconds or less — which is what makes it the standard converter for anything that must alternate between mechanical and electrical at speed.
- **It is resonant by nature.** A piezoelectric element is a piece of crystal with a natural frequency, so when driven it also is a **resonator**: the quartz in a watch is not primarily a voltage source but a very stable oscillator, and its stability is why it replaced clockwork.
- **The ceramics are poled.** Barium titanate and lead zirconate titanate are not piezoelectric as fired: they are ferroelectric ceramics whose domains are aligned by a strong field, which is what makes a cheap material behave like a crystal.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon — its two directions, the quantities that describe the coupling and the bounds it meets — not the crystallography of the specific materials and not the devices, which belong to technica.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Coupling Phenomenon `(→ Instance)` Piezoelectric Effect | Meso. Reversible conversion between strain and charge in a non-centrosymmetric crystal. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Coupling Phenomenon `(→ Instance)` Piezoelectric Effect `(→ Kind)` Direct Effect | Meso. Strain produces charge: the sensor and the energy harvester. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Coupling Phenomenon `(→ Instance)` Piezoelectric Effect `(→ Kind)` Converse Effect | Meso. Charge produces strain: the actuator and the transducer's transmit direction. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Coupling Phenomenon `(→ Instance)` Piezoelectric Effect `(→ Attribute)` `Property` `(→ Instance)` Piezoelectric Coefficients | Meso. The tensor relating strain to field — the numbers a manufacturer publishes. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Coupling Phenomenon `(→ Instance)` Piezoelectric Effect `(→ Attribute)` `Property` `(→ Instance)` Resonance | Meso. The element's own natural frequency, which is what a quartz clock exploits and an ultrasonic probe must tune. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Coupling Phenomenon `(→ Instance)` Piezoelectric Effect `(→ Attribute)` `Property` `(→ Instance)` Poling | Meso. The field alignment of domains in a ferroelectric ceramic — the process that gives the effect to a material that lacks it as fired. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Coupling Phenomenon `(→ Instance)` Piezoelectric Effect `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Absence of a Symmetry Centre | Micro. The structural condition: the crystal class must be non-centrosymmetric, which is the reason the effect exists in quartz and not in table salt. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Coupling Phenomenon `(→ Instance)` Piezoelectric Effect `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Curie Temperature | Micro. Above it a ferroelectric ceramic loses its poled state and the effect with it — the operating limit of every PZT device. |

**Limitations.** *Scale* — the effect is defined for a bulk crystal; at very small dimensions surface and flexoelectric contributions compete. *Partial Observability* — the charge produced by a small strain is tiny and needs high-impedance electronics, so the measurement chain is part of the experiment. *Many-Body coupling* — the element's response is inseparable from the structure it is bonded to, which is why transducer design is a system problem. *Nonlinearity* — at large drive the response departs from linear and the material heats.

## References

- Curie, J., & Curie, P. (1880). Développement, par pression, de l'électricité polaire dans les cristaux hémièdres à faces inclinées. *Comptes rendus de l'Académie des sciences*, 91, 294–295. — the discovery, with the symmetry condition already implicit in "hémièdre"
- Voigt, W. (1910). *Lehrbuch der Kristallphysik*. Teubner. — the tensor formulation, which made the effect a property of a crystal class
- Cady, W. G. (1946). *Piezoelectricity*. McGraw-Hill. — the resonator theory behind the quartz clock
- Mason, W. P. (1950). *Piezoelectric crystals and their application to ultrasonics*. Van Nostrand. — the transducer as an engineering object
- [Piezoelectricity](https://en.wikipedia.org/wiki/Piezoelectricity)
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) · [Resonance](/view.html?p=notes/nature/phenomena/resonance.md)
- [Crystalline Structure](/view.html?p=notes/nature/crystalline-structure.md) · [Crystal Symmetry](/view.html?p=notes/epistemica/mathematical/symmetry.md) · [Vibration](/view.html?p=notes/nature/wave/vibration.md)
