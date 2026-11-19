---
tags: [note, nature, phenomenon, wave, measurement]
qa:
 - Is the Doppler effect a change in the wave or a change in the observer — and if the second, why does a moving source give a different formula from a moving observer in sound but not in light?
 - Cosmological redshift is not this effect; how many other "redshifts" are really statements about space rather than about motion?
 - The effect is how relative velocity is measured remotely — radar, ultrasound, spectra. What does that make it: a phenomenon, or an instrument?
---

# Doppler Effect

> The **Doppler effect** is the shift in the frequency observed when source and observer are in relative motion: the number of wavefronts arriving per second changes because the geometry between them changes. It is not a change *in* the wave — the emitted frequency is what it always was — but a change in how the motion samples it.

$$f_{\text{obs}}=f_{\text{src}}\,\frac{v \pm v_{\text{obs}}}{v \mp v_{\text{src}}}$$

> The upper and lower signs are the whole story of the classical case, and they encode an asymmetry that light does not share: a **moving source** changes the wavelength in the medium and therefore the frequency every observer sees, while a **moving observer** changes only how often the wavefronts are met. In a medium those are different experiments; for light, where no medium exists to be moved relative to, they are one, and making them one is where special relativity starts.

## Formulation

### What natural element type does this natural instance belong to?

`Propagation Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to the case of a wave meeting a moving frame.

It is **not** a `Property`: the frequency is the property, and it is unchanged in the source's frame; what shifts is the observed value, so the effect is a relation between two frames and not a feature of either. It is **not** a `Process`: nothing propagates or transforms — the wave travels exactly as before, and a different observer samples it differently. It is **not** the **cosmological redshift**: that is a change in the space the light crosses, and calling it Doppler is the most consequential misnomer in the family.

### What is this natural instance?

> A siren dropping in pitch as it passes; the higher pitch of an approaching train and the sudden fall as it goes by; a police radar reading a speed; a weather radar resolving the rotation inside a storm; an ultrasound probe measuring the velocity of blood in an artery; the blue-shifted and red-shifted limbs of a rotating galaxy; the redshift of a receding quasar — which is not this effect.

Two regimes, and the boundary between them is a speed:

- **Classical, in a medium.** The formula above holds, with the source and observer terms asymmetric because both are referred to the medium. The shift is first order in $v/v_{\text{sound}}$, so at ordinary speeds it is a fraction of a percent — audible as the drop of a passing car, not visible in a laboratory without care.
- **Relativistic, in vacuum.** The formula becomes a single expression in the relative velocity, $f_{\text{obs}} = f_{\text{src}}\sqrt{(1-\beta)/(1+\beta)}$ for recession, and it acquires a **transverse** term: a source moving *across* the line of sight is observed at a lower frequency by the time-dilation factor alone. That term has no classical analogue and was a prediction of special relativity before it was measured.

The transverse case is the note's sharpest teaching point: it is the observable that distinguishes "the motion changes the geometry of sampling" from "the motion changes the clock", and only the second survives when there is no medium.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon itself — its regimes, the quantities that characterise the shift and the bounds on the formula — not the measurement instruments (radar, ultrasound, spectrographs) that exploit it, and not the cosmological expansion, which is a different phenomenon with a similar name.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect | Meso. Frequency shift under relative motion of source and observer. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect `(→ Kind)` Acoustic Doppler Effect | Meso. In a medium: source and observer terms asymmetric, because both are referred to the medium. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect `(→ Kind)` Relativistic Doppler Effect | Meso. In vacuum: one expression in the relative velocity, with no medium to privilege a frame. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect `(→ Kind)` Transverse Doppler Effect | Micro. The second-order shift of a source moving across the line of sight: time dilation, with no classical counterpart. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect `(→ Attribute)` `Property` `(→ Instance)` Fractional Shift | Meso. The relative change in frequency — first order in speed for sound, and what a radar or a spectrograph actually reports. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect `(→ Attribute)` `Property` `(→ Instance)` Sign | Meso. Recession lowers the observed frequency, approach raises it: the red and blue directions of the same quantity. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect `(→ Attribute)` `Property` `(→ Instance)` Line Broadening | Meso. Distinct from the shift: a distribution of velocities broadens a spectral line symmetrically, while bulk motion moves it. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Line-of-Sight Component | Micro. Only the velocity along the line of sight shifts the frequency at first order; the perpendicular component enters only through the transverse term. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Doppler Effect `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Relativistic Limit | Micro. The classical formula is wrong by order $\beta^2$; beyond that the relativistic expression is the one with meaning. |

**Limitations.** *Scale* — the shift is a property of the whole waveform, and at very low signal it is indistinguishable from drift. *Nonlinearity* — at large amplitude a medium generates harmonics, and the observed spectrum is no longer a shifted copy of the emitted one. *Many-Body coupling* — a hot gas has a distribution of velocities, so the observable is a broadened line whose *shape* carries the temperature, not just the bulk motion. *Partial Observability* — the line-of-sight component is measured; the rest of the velocity requires another method.

## The redshift that is not this

Light from distant galaxies is observed at lower frequency than emitted, and the formula that describes it looks like the recession term above. It is not the same phenomenon.

- **Doppler redshift** comes from relative motion *through* space: the source and the observer have a velocity, and the wave is sampled differently because of it.
- **Cosmological redshift** comes from the *expansion of space* between emission and observation: the wavelength is stretched because the space the light crosses grew while the light was in it. There is no velocity of the source relative to the observer in the relevant sense — with a preferred definition of distance, both are close to at rest.

At small redshift the two are numerically indistinguishable, which is why the confusion is durable rather than careless. They separate at high redshift, and the difference is not academic: one is a measurement of motion, the other a measurement of the metric. See [Universe](/view.html?p=notes/nature/universe.md).

## References

- Doppler, C. (1842). *Über das farbige Licht der Doppelsterne und einiger anderer Gestirne des Himmels*. Borrosch & André. — the original claim, made about the colours of double stars, which is the part that did not survive
- Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. *Annalen der Physik*, 17(10), 891–921. — the relativistic expression, and the transverse effect as a consequence of time dilation
- Hubble, E. (1929). A relation between distance and radial velocity among extra-galactic nebulae. *Proceedings of the National Academy of Sciences*, 15(3), 168–173. — cited here precisely to be distinguished: what Hubble measured is not this effect
- Feynman, R. P., Leighton, R. B., & Sands, M. (1963). *The Feynman lectures on physics* (Vol. I, ch. 34). Addison-Wesley. — the effect derived from the geometry of wavefronts, which is the way to understand it
- [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect)
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) — the shelf, and the family this belongs to
- [Frequency (Periodicity)](/view.html?p=notes/nature/frequency-periodicity.md) · [Pitch](/view.html?p=notes/nature/pitch.md) · [Wave](/view.html?p=notes/nature/wave/wave.md) · [Universe](/view.html?p=notes/nature/universe.md)
- [Radar](/view.html?p=notes/technica/general/fisicatecnica/electromagnetic/radar.md) — the echo instrument that turns the effect into a measurement of range and speed
- [Laser Doppler Vibrometer](/view.html?p=notes/technica/production/industry/laser-doppler-vibrometer.md) — the interferometric one, where the effect measures a surface's vibration with the shift doubled by the return path
