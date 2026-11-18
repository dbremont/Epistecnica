---
tags: [note, nature, phenomenon, oscillation, wave]
---

# Oscillation

> **An oscillation** is the repeated return of a system's state toward a configuration and away from it about a stable point — a back-and-forth in one or more quantities that repeats in time.

> It is not a substance, and it is not a wave. A wave is an oscillation that travels; an oscillation stays where it is put. A pendulum, a plucked string, a current in an LC circuit, a vibrating molecule and a neuron's membrane potential all oscillate, and none of them is made of "oscillation" — each is a system whose states repeat.

> What makes the repetition possible is a **restoring tendency**: a displacement creates a tendency to return, the return overshoots because of inertia, and energy traded between two forms — kinetic and potential, magnetic and electric — carries the motion through. Add **dissipation** and the overshoot shrinks; add **drive** and the shrinking is replenished or the rhythm is captured; add **coupling** and the rhythm is shared.

## Formulation

### What natural element type does this natural instance belong to?

**An oscillation, read as a natural instance, belongs to `Ontic Element (→ Kind) Phenomenon` — a regularity predicated over the trajectory of a system that repeatedly returns toward an equilibrium state.**

Readable secondarily as a `Property`: the oscillatory character of a system, considered as a feature the system bears. Readable again as a `Process` when one particular oscillation is bound to one system and one interval — "this swing" — whereas this note is the general pattern. Those readings are prose here, not second roots.

The choice matters, and the other readings fail for reasons worth stating. An oscillation is not a `Substance`: nothing in the world is made of it. It is not one `Process`: a process is a bounded causal sequence in one system, while the same pattern holds for every system that repeats. It is not a `State`: a state is a configuration at a moment, and an oscillation is what a *sequence* of configurations does. What it is, is the **pattern those sequences share** — a stable point, a restoring tendency, a repeated crossing, a period — and that is a phenomenon in the guide's sense.

### What is this natural instance?

> Every oscillation is read through the same slots: the **oscillating system**, its **equilibrium state**, the **restoring tendency** that drives displacement back, the **inertia** (or the accumulating quantity) that carries it past equilibrium, the **energy** the two forms trade, the **amplitude** it reaches, and the **period or frequency** at which it returns.

> Three terms are worth separating, because they are used loosely and they name different things. **Oscillation** is the temporal pattern — repetition about an equilibrium. **Vibration** is the mechanical case, where the repeating quantity is the displacement of matter. **Wave** is the propagating case, where the pattern moves through space and the medium does not travel with it. **Periodicity** is weaker than all three: a rotating body is periodic without oscillating, because it never reverses direction.

> Damping and driving are not decorations — they decide which regime the phenomenon is in. The **undamped** case conserves its energy and repeats indefinitely. The **damped** case loses amplitude each cycle and either settles toward equilibrium while still crossing it, or crosses into a non-oscillatory decay. The **driven** case can be made to repeat at the driver's frequency, and at **resonance** a small drive builds a large amplitude. The **self-sustained** case — a clock escapement, a heartbeat, a limit cycle — repeats from its own internal source of energy, with an amplitude set by the system rather than by the initial condition, which is why it is robust to perturbation in a way a free oscillation is not.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the pattern itself — the states it is predicated over, the cycle it generates, the quantities that characterise it, and the conditions that bound it. The particular systems that oscillate, their histories, and the instruments that observe them are associated, not parts. The wave reading is a different instance — the propagation of a disturbance through space — and is linked from Related, never nested here.

> Stopping rule: a row is terminal when it names a modelling slot, a characteristic quantity, or a governing condition whose own decomposition lives elsewhere.

> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: a single cycle of one oscillator is **micro**; the pattern shared by a population of coupled oscillators is **meso** — synchronization is a property of the ensemble, not of any one member. Limitation checklist for the segment: **Nonlinearity** (past small amplitudes the restoring tendency stops being proportional to the displacement), **Chaos** (a driven nonlinear oscillator can be sensitive to its initial condition), **Partial Observability** (the cycle is read from samples at a finite rate, so the phase is inferred rather than seen), **Measurement Disturbance** (measuring a small oscillator loads it), **Many-Body coupling** (coupled oscillators cannot be read one at a time).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation | Bound root instance: the regularity that a system's state repeatedly returns toward and away from an equilibrium. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Predication)` `State` | Grouping: the states the regularity is predicated over. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Predication)` `State` `(→ Instance)` Equilibrium State | The configuration the pattern is organised around — the state the restoring tendency points to. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Predication)` `State` `(→ Instance)` Extreme Displacement State | A turning point: maximum displacement, where the velocity vanishes and the direction reverses. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Predication)` `State` `(→ Instance)` Crossing State | Passage through equilibrium, where the restoring tendency vanishes and the speed is greatest. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Predication)` `Trajectory` | Grouping: the ordered sequence of states the pattern generates. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Predication)` `Trajectory` `(→ Instance)` Oscillation Cycle | One complete sequence from a state back to the same state at the same phase. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Predication)` `Trajectory` `(→ Instance)` Oscillation Cycle `(→ Part)` `State` | Grouping: the states constituting one cycle. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Predication)` `Trajectory` `(→ Instance)` Oscillation Cycle `(→ Part)` `State` `(→ Instance)` Successive State Set | The ordered states of one period, each one step further in phase than the last. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` | Grouping: the quantities that characterise an oscillation. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` `(→ Instance)` Amplitude | The greatest displacement from equilibrium reached in a cycle. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` `(→ Instance)` Period | The duration of one complete cycle. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` `(→ Instance)` Frequency | Cycles per unit time — the reciprocal of the period, in hertz. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` `(→ Instance)` Phase | The position within the cycle, as an angle or a fraction of a period — what makes two oscillations comparable point by point. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` `(→ Instance)` Damping Ratio | How strongly the amplitude is dissipated per cycle; it decides whether the decay crosses equilibrium or not. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` `(→ Instance)` Quality Factor | Stored energy over energy lost per cycle — how many cycles the oscillator rings before it is spent. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` `(→ Instance)` Resonance Frequency | The drive frequency at which a driven oscillator responds with the largest amplitude. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Property` `(→ Instance)` Oscillation Energy | The energy traded between the two forms — conserved when undamped, dissipated when damped. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Variable Aspect` | Grouping: the aspects whose value varies across the cycle. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Variable Aspect` `(→ Instance)` Displacement | The departure from the equilibrium configuration — the quantity that is reversed twice per cycle. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Attribute)` `Variable Aspect` `(→ Instance)` Momentum | The quantity that carries the system past equilibrium — the reason the return overshoots. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Situation)` `Environment` | Grouping: the external conditions that act on the oscillator. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Situation)` `Environment` `(→ Instance)` Dissipative Environment | The surroundings that remove energy each cycle, through friction, viscosity, resistance or radiation. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Situation)` `Environment` `(→ Instance)` Driving Environment | The external source that supplies energy at a stated frequency, and so can set the rhythm. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Bound)` `Constraint` | Grouping: what decides which regime the oscillation is in. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Bound)` `Constraint` `(→ Instance)` Restoring Law | The relation between displacement and the tendency to return; its linearity is what makes the oscillation harmonic. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Bound)` `Constraint` `(→ Instance)` Energy Dissipation | What removes energy per cycle, and so bounds how long the oscillation lasts. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Bound)` `Constraint` `(→ Instance)` Resonance Condition | The match between drive frequency and natural frequency at which the response is greatest. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Instance)` Oscillation `(→ Bound)` `Constraint` `(→ Instance)` Synchronization Condition | The coupling strength and frequency detuning at which coupled oscillators adopt one shared rhythm. |

## Which are the kinds of oscillation?

> Ordered by **what keeps the oscillation going** — the energy source and the mechanism that sustains the repetition, not the field that studies it. Each row is one kind; a real oscillator can move between them as a parameter changes (a clock's escapement is self-sustained; the same pendulum, undriven, is damped).

| Kind | Mechanism Set | Description | Case Study |
| --- | --- | --- | --- |
| **Harmonic** | A linear restoring tendency and inertia, with no dissipation and no drive | The displacement is sinusoidal; period independent of amplitude | A small-angle pendulum; an ideal LC circuit |
| **Damped** | A linear restoring tendency with energy lost each cycle | Amplitude decays exponentially; the period lengthens slightly; past critical damping there is no crossing at all | A pendulum in air; an RLC circuit with resistance |
| **Driven** | A periodic external supply at a stated frequency | The response settles at the driver's frequency; amplitude peaks when the frequencies match | A swing pushed in time; a loudspeaker cone |
| **Parametric** | A parameter of the system modulated periodically, rather than a direct drive | Energy enters by varying stiffness or length, not by pushing; instability bands replace a single resonance | A pumped swing; a child on a swing standing and crouching |
| **Relaxation** | A slow accumulation and a fast discharge, repeated | The waveform is far from sinusoidal — slow build, abrupt reset — and the period is set by the time constants | A dripping tap; a neon-lamp oscillator |
| **Self-Sustained** | An internal energy source plus a nonlinearity that regulates amplitude | A limit cycle: the amplitude is set by the system, so perturbations decay back onto it | A clock escapement; a heartbeat; a violin string under the bow |
| **Coupled** | Two or more oscillators exchanging energy through a link | Frequencies pull toward a common value; sufficiently strong coupling locks them in phase | Huygens' synchronized clocks; fireflies; Josephson arrays |
| **Stochastic** | A restoring tendency plus random forcing | The rhythm is present only in the spectrum; phase diffuses rather than advancing cleanly | A Brownian particle in a trap; a noisy electronic oscillator |

## QA

### Is an oscillation a wave?

> No, and the corpus keeps them apart. An oscillation repeats in **time** at a place; a wave repeats in **time and space** and carries the pattern away from its source. A sound wave is both at once — the medium oscillates and the disturbance propagates — which is why the natural notes split the reading: [Wave](/view.html?p=notes/nature/wave/wave.md) owns the propagation, this note owns the temporal pattern, and [Sound](/view.html?p=notes/nature/sound.md) is the case where both are present.

### Is an oscillation a change of matter?

> Not in the sense the change shelf means. [Matter Change](/view.html?p=notes/nature/matter/change.md) decomposes transformations that alter the state of a substance — melting, reaction, fission — and its mark is that the system ends somewhere it was not. An oscillation returns: after one cycle the system is the same system in the same state, and the repetition is the point. It is a **configuration** that changes, not a substance.

### Why is a rotation not an oscillation?

> Because nothing reverses. A rotating body is periodic — it returns to the same orientation after a fixed interval — but its angular displacement keeps increasing in one direction, so it exhibits the property of periodicity without the back-and-forth that defines an oscillation. This is why `periodic` is the weaker term and why the two notes are linked rather than merged.

### Is the pendulum an oscillation, or the system that oscillates?

> The pendulum is the `Natural Object`; its swinging is the oscillation. The distinction matters for decomposition: the pendulum decomposes as a body with a suspension, a bob and a restoring torque, while the oscillation decomposes as the pattern above. A worked dissipative case of the pair is [A case study of a dissipative system: damped pendulum](/view.html?p=notes/unclassified/a-case-study-of-a-dissipative-system-damped-pendul.md).

### Why does the self-sustained case matter more than the harmonic one?

> Because it is the case the world is actually made of. A perfect harmonic oscillator is a limit: it needs a strictly linear restoring law and no dissipation, and every real oscillator departs from it. The self-sustained oscillator is the opposite extreme and the more robust object — its amplitude is regulated by its own nonlinearity, so it recovers from perturbation and keeps time — which is why clocks, hearts, lasers and circadian rhythms are all limit cycles rather than ideal pendulums.

## References

- [Philosophia Naturalis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-naturalis-et-operis.md) (schema owner)
- [Wave](/view.html?p=notes/nature/wave/wave.md) — the propagating case of the same pattern
- [Sound](/view.html?p=notes/nature/sound.md) — the case where the pattern and its propagation are both present
- [Frequency (Periodicity)](/view.html?p=notes/nature/frequency-periodicity.md) · [Periodic](/view.html?p=notes/nature/periodic.md) · [Amplitude](/view.html?p=notes/nature/amplitude-a.md) — the quantities and the weaker property
- [Oscillation](/view.html?p=notes/nature/wave/oscillation.md) — the pattern this quantity counts
- [Alternating Current](/view.html?p=notes/nature/alternating-current-ac.md) — the electrical instance of the pattern
- [Harmonic Analysis](/view.html?p=notes/epistemica/epistemic/discipline/harmonic-analysis.md) — the discipline that decomposes an oscillation into its harmonics
- [Stability Theory](/view.html?p=notes/epistemica/mathematical/change/stability-theory.md) — the dynamical reading: equilibrium, linearization, limit cycle
- [Coupled Oscillator Network](/view.html?p=notes/epistemica/mathematical/change/rsp/coupled-oscillator-network.html) — the playground that simulates the coupled case
- [MEMS Oscillator](/view.html?p=notes/production/technique/fisicatecnica/electromagnetic/mems-oscillator.md) — the engineered instance
- Andronov, A. A., Vitt, A. A., & Khaikin, S. E. (1966). *Theory of oscillators*. Pergamon Press.
- Den Hartog, J. P. (1985). *Mechanical vibrations*. Dover.
- Galileo, G. (1638). *Discorsi e dimostrazioni matematiche intorno a due nuove scienze*. Lodewijk Elzevir. — the isochronism of the pendulum, the first oscillation measured against time.
- Hooke, R. (1678). *De potentia restitutiva*. — the linear restoring force, *ut tensio, sic vis*.
- Huygens, C. (1673). *Horologium oscillatorium*. — the pendulum clock, and the first treatment of coupled clocks.
- Kuramoto, Y. (1984). *Chemical oscillations, waves, and turbulence*. Springer.
- Pikovsky, A., Rosenblum, M., & Kurths, J. (2001). *Synchronization: A universal concept in nonlinear sciences*. Cambridge University Press.
- Strutt, J. W., Baron Rayleigh. (1877–1878). *The theory of sound* (2 vols.). Macmillan.
- Strogatz, S. H. (2015). *Nonlinear dynamics and chaos* (2nd ed.). Westview Press.
- Thomson, W., & Tait, P. G. (1867). *Treatise on natural philosophy*. Clarendon Press.
- Van der Pol, B. (1927). On relaxation-oscillations. *Philosophical Magazine*, 2(11), 978–992.
- Winfree, A. T. (1980). *The geometry of biological time*. Springer.
- [Oscillation](https://en.wikipedia.org/wiki/Oscillation)
