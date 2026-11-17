---
tags: [note, nature, phenomenon, oscillation, vibration]
qa:
 - Is resonance a large response or a small damping — and why is the amplitude at resonance set by dissipation rather than by the drive?
 - A system driven at its natural frequency stores energy instead of reflecting it; what happens to that energy when the damping is zero?
 - Every structure has resonances; is the engineering question avoiding them, or designing what happens when they occur?
---

# Resonance

> **Resonance** is the pattern in which a system driven near its own natural frequency responds with an amplitude far larger than the drive would suggest. The drive does not grow; the **stored energy** does, because each cycle adds a little at the phase where the system can accept it.

> Its consequence is that amplitude at resonance is set by **dissipation**, not by the force. A lightly damped system driven at its natural frequency has an enormous response and takes many cycles to reach it; a heavily damped one has a modest response and follows the drive immediately. Resonance is therefore the phenomenon that makes damping a design variable rather than a nuisance.

## Formulation

### What natural element type does this natural instance belong to?

`Resonance Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to the driven response of a system with a natural frequency.

It is **not** the natural frequency itself, which is a property of the system; resonance is what happens when a drive meets it. It is **not** a `Bound`, though `vibration.md` lists it as one for structures — the bound is the engineering statement, the phenomenon is the mechanism. It is **not** **interference** in the wave sense, though the two are relatives: both are phase-coherent additions, one in time and one in space.

### What is this natural instance?

> A glass breaking at one note; a bridge oscillating under marching feet; a car body shaking at a particular engine speed; a tuning fork setting another ringing; the radio tuned to a station; a swing pushed in step; a building swaying with an earthquake whose period matches its own; a microwave oven exciting a water mode.

The mechanism is a phase condition plus an energy balance. A driven oscillator obeys

$$\ddot{x}+2\zeta\omega_0\dot{x}+\omega_0^{2}x=\frac{F_0}{m}\cos\omega t,$$

whose steady amplitude peaks near $\omega\approx\omega_0$ at a value that scales as $1/(2\zeta)$: halve the damping and double the peak. Three consequences follow, and together they are the whole phenomenon:

- **The peak is inversely proportional to damping.** With no dissipation the response grows without limit — the mathematical statement that a system driven exactly at resonance with no loss has no steady state, only ramping amplitude.
- **The phase carries the information.** Below resonance the response lags the drive; at resonance it lags by a quarter cycle, which is why the drive does work on the system at every cycle; above resonance it lags by half a cycle and the system starts pushing back.
- **The bandwidth trades against the height.** A sharp peak means a narrow band: high-Q systems are selective, which is what makes a tuning circuit a filter and a bridge a hazard.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon across domains — its kinds by mechanism, the quantities that characterise the peak and the bounds it meets — not the oscillating body (decomposed on its own shelf) and not the control that exploits it.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Resonance Phenomenon `(→ Instance)` Resonance | Meso. Large response of a system driven near its natural frequency. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Resonance Phenomenon `(→ Instance)` Resonance `(→ Kind)` Mechanical Resonance | Meso. Structures, machines and suspensions: the case that fails. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Resonance Phenomenon `(→ Instance)` Resonance `(→ Kind)` Acoustic Resonance | Meso. Air columns and cavities: the pipe, the instrument body, the room mode. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Resonance Phenomenon `(→ Instance)` Resonance `(→ Kind)` Electrical Resonance | Meso. LC circuits: the case that is useful, and the basis of tuning and filtering. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Resonance Phenomenon `(→ Instance)` Resonance `(→ Attribute)` `Property` `(→ Instance)` Quality Factor | Meso. The sharpness of the peak: stored energy over energy lost per cycle. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Resonance Phenomenon `(→ Instance)` Resonance `(→ Attribute)` `Property` `(→ Instance)` Bandwidth | Meso. The frequency range over which the response is large — the reciprocal of the quality factor. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Resonance Phenomenon `(→ Instance)` Resonance `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Dissipation | Micro. Amplitude at resonance is limited by damping; zero damping gives no steady amplitude at all. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Resonance Phenomenon `(→ Instance)` Resonance `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Structural Capacity | Micro. The engineering bound: the amplitude must stay below what the body can carry, which is what design does about the phenomenon. |

**Limitations.** *Nonlinearity* — real systems shift their resonant frequency with amplitude, so a large response detunes itself. *Uncertainty* — damping is the least predictable parameter in the model, often known to a factor of two, and the peak height is inversely proportional to it. *Many-Body coupling* — a structure has many resonances and they interact; avoiding one moves the problem to the next.

## References

- Strutt, J. W. (1877). *The theory of sound* (Vol. 1). Macmillan. — the driven oscillator and the origin of the quality factor
- Den Hartog, J. P. (1956). *Mechanical vibrations* (4th ed.). McGraw-Hill. — resonance and isolation as design problems
- Feynman, R. P., Leighton, R. B., & Sands, M. (1963). *The Feynman lectures on physics* (Vol. I, ch. 23). Addison-Wesley. — the phase argument, which is the honest explanation
- [Resonance](https://en.wikipedia.org/wiki/Resonance)
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) · [Vibration](/view.html?p=notes/nature/wave/vibration.md) · [Oscillation](/view.html?p=notes/nature/wave/oscillation.md)
- [Frequency (Periodicity)](/view.html?p=notes/nature/frequency-periodicity.md) · [Natural Frequency](/view.html?p=notes/nature/natural-frequencys.md)
