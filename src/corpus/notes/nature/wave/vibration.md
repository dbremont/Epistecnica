---
tags: [note, nature, phenomenon, oscillation, mechanics, vibration]
qa:
 - Is vibration a kind of oscillation or the mechanical case of it — and does the answer change when the vibrating thing is a field rather than a body?
 - Resonance is an amplitude bound, fatigue a lifetime bound: why does the same phenomenon fail a structure slowly at one amplitude and suddenly at another?
---

# Vibration

> **Vibration** is the mechanical case of [oscillation](/view.html?p=notes/nature/wave/oscillation.md): the repeating displacement of matter about an equilibrium configuration, driven by a restoring tendency and carried past that equilibrium by inertia. Where an oscillation can be a current, a voltage or a population, a vibration is always a **body moving** — which is why it is the case with the most engineering consequences and the sharpest bounds.

## Formulation

### What natural element type does this natural instance belong to?

`Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Ontic Element (→ Kind) Phenomenon`, specialized through `Oscillation (→ Kind) Vibration`, read as parsed reality.

It is **not** a `Process` bound to one system: the same pattern holds for any body with a restoring force and inertia, and this note is the pattern, not "this swing". It is **not** a `Property` of the body, though the *natural frequency* is one: the vibration is what the body does over a trajectory. It is **not** a [wave](/view.html?p=notes/nature/wave/wave.md): a wave is an oscillation that travels, and a vibration stays where it is put — the distinction the oscillation note draws and this note inherits.

### What is this natural instance?

> A plucked string, a tuning fork, a bridge deck under traffic, a machine on its mounts, a building in an earthquake, a molecule in a crystal lattice, a vocal fold, a car suspension over a washboard road.

Every case is read through the same four quantities, and each has a bound attached:

- **Natural frequency** — the frequency at which the body oscillates freely, set by stiffness and mass together: $f_n \propto \sqrt{k/m}$. Heavier is slower, stiffer is faster, and this is the one number an engineer moves first.
- **Mode shape** — a body does not have one frequency but a spectrum of them, each with a shape: a string's harmonics, a beam's bending modes, a building's sway modes. A vibration is generally a combination, and which modes are excited depends on where the load is applied.
- **Damping ratio** — the rate at which amplitude decays. It separates the three regimes: **under-damped**, which oscillates and decays; **critically damped**, which returns without crossing; **over-damped**, which returns slowly without crossing. Structural damping is small, which is why structures ring.
- **Amplitude** — how far it moves, and the quantity that decides which bound it meets: a small amplitude for a long time is **fatigue**, a large amplitude once is **resonance** or **yielding**.

Three regimes of driving follow, and they are the note's practical content. **Free** vibration is the body left to itself after a displacement. **Forced** vibration is the body driven at a frequency, and when the driver approaches the natural frequency the response grows without the force growing — **resonance**, the phenomenon that brought down the Tacoma Narrows bridge and that every machine mount exists to avoid. **Self-excited** vibration is the case where the motion itself admits energy from a steady source — a violin string under a bow, a flag in the wind, a wheel shimmy — so the amplitude settles at a level set by the system rather than by the initial condition, which is why such vibrations do not decay and cannot be damped away by removing a driver.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the mechanical oscillation as a pattern — its regimes, the quantities that characterise it and the bounds it meets — not the body that vibrates, which is decomposed on its own shelf, and not the wave it may launch.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case, no type terminates a branch.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration | Meso. The mechanical oscillation: matter displacing about equilibrium. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration `(→ Kind)` Free Vibration | Meso. The body left to itself: frequency set by stiffness and mass, amplitude by the initial displacement. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration `(→ Kind)` Forced Vibration | Meso. The body driven at a frequency: response set by the ratio of driver to natural frequency. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration `(→ Kind)` Self-Excited Vibration | Meso. The motion feeds itself from a steady source, so the amplitude is set by the system and does not decay. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration `(→ Attribute)` `Property` `(→ Instance)` Natural Frequency | Meso. The frequency of free motion: the square root of stiffness over mass. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration `(→ Attribute)` `Property` `(→ Instance)` Mode Shape | Meso. The spatial pattern of one natural frequency; the body has a spectrum of them. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration `(→ Attribute)` `Property` `(→ Instance)` Damping Ratio | Meso. The rate of decay, which separates under-damped, critical and over-damped regimes. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Resonance | Meso. Driver and natural frequency coincide: the amplitude grows without the force growing. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Oscillation `(→ Kind)` Vibration `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Fatigue | Meso. Many small cycles accumulate damage: the bound that governs machines, bridges and aircraft rather than the one-off overload. |

**Limitations.** *Nonlinearity* — amplitude-dependent stiffness and damping make the linear resonance picture wrong at large amplitudes. *Uncertainty* — damping is the least predictable quantity in the model, often known only to a factor of two. *Many-Body coupling* — every real structure is a coupled system, so modes are not independent once two of them share a frequency. *Scale* — the same phenomenon at the scale of a molecule and of a bridge, with no shared mechanism.

## References

- Strutt, J. W. (1877). *The theory of sound* (Vol. 1). Macmillan. — the general theory of vibrating systems, before "vibration engineering" existed
- Timoshenko, S. (1928). *Vibration problems in engineering*. Van Nostrand. — the subject as a branch of structural design
- Den Hartog, J. P. (1956). *Mechanical vibrations* (4th ed.). McGraw-Hill. — forced vibration, resonance and isolation stated for designers
- [Oscillation](/view.html?p=notes/nature/wave/oscillation.md) — the temporal pattern this is the mechanical case of
- [Wave](/view.html?p=notes/nature/wave/wave.md) — the oscillation that travels, and the boundary of this note
- [Natural Frequency](/view.html?p=notes/nature/natural-frequencys.md) · [Frequency and Periodicity](/view.html?p=notes/nature/frequency-periodicity.md) · [Amplitude](/view.html?p=notes/nature/amplitude-a.md)
- [Beam](/view.html?p=notes/nature/body/beam.md) · [Column](/view.html?p=notes/nature/body/column.md) · [Structure](/view.html?p=notes/nature/body/structure.md) — the bodies that vibrate, and the ones whose fatigue bound this sets
