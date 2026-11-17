---
tags: [note, nature, phenomenon, wave, optics]
qa:
 - Interference belongs to neither wave alone; does that make it a relation rather than a phenomenon, and what does the answer change about how it is measured?
 - Coherence is the condition that makes interference visible; is coherence a property of a source, a state of a field, or a claim about what two detectors could correlate?
 - Every precision measurement at the wavelength scale is an interferometer. What does that say about interference — a phenomenon, or the limiting instrument of physics?
---

# Interference

> **Interference** is the pattern produced when two or more waves occupy the same region: their amplitudes add, and the sum is larger where the phases agree and smaller where they oppose. It is the visible content of superposition, and the reason the wave description of light was accepted before any wave could be seen.

> Its decisive feature is that it belongs to **neither wave alone**. Either wave, arriving by itself, produces a smooth intensity; only together do they produce structure. That is what makes interference a phenomenon in the guide's sense rather than a property — it is a pattern predicated over the pair, and it disappears when they are separated.

## Formulation

### What natural element type does this natural instance belong to?

`Propagation Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to the superposition of waves.

It is **not** a `Property` of the wave, for the reason above. It is **not** a `Process` — no energy is created or moved by interference; the energy is redistributed, and the total is the sum of the two. It is **not** **diffraction**, though the two always occur together in practice: diffraction is a wave bending into a region it would not classically enter, interference is what the bent parts then do to each other.

### What is this natural instance?

> Two ripples crossing on a pond and forming a grid of crests and hollows; the coloured bands of a soap film; a thin oil slick on wet asphalt; the fringes of a Michelson interferometer; the anti-reflective coating on a lens; the noise-cancelling headphone; the moiré of two grids; the diffraction pattern of a double slit.

The mechanism is an addition and a path difference. Two waves reaching a point with a path difference $\Delta$ arrive with a phase difference $2\pi\Delta/\lambda$, and the observed intensity is

$$I=I_1+I_2+2\sqrt{I_1I_2}\cos\left(\frac{2\pi\Delta}{\lambda}\right),$$

which says three things: the fringes are periodic in the *wavelength*, so they are a ruler; the contrast depends on the two amplitudes, so equal beams give the deepest fringes; and everything depends on the two waves being able to hold a stable phase relation at all. That last condition is **coherence**, and it is what separates interference from a mere crossing of waves — two independent lamps sum to a uniform brightness, while two parts of the same beam produce fringes.

Two limits of the phenomenon are worth keeping:

- **Constructive and destructive** are the extremes, at path differences of whole and half wavelengths. The half-wavelength case is the working principle of anti-reflective coatings, and the whole-wavelength case is how an interferometer measures displacement to a fraction of a wavelength.
- **The pattern is in the intensity, not the field.** No detector can follow the field at optical frequencies; what is measured is the time-averaged intensity, which is why an interference experiment is always, in practice, an experiment about coherence time.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon — its kinds, the quantities that characterise the pattern and the bounds that govern its visibility — not the waves that interfere, and not the instruments that exploit it.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Interference | Meso. The superposition pattern of two or more waves. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Interference `(→ Kind)` Constructive Interference | Meso. Path difference near a whole wavelength: amplitudes add, intensity rises. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Interference `(→ Kind)` Destructive Interference | Meso. Path difference near a half wavelength: amplitudes cancel, intensity falls — the anti-reflection case. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Interference `(→ Kind)` Thin-Film Interference | Meso. Fringes formed by reflections at the two faces of a layer, which is why the colour depends on thickness. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Interference `(→ Attribute)` `Property` `(→ Instance)` Fringe Spacing | Meso. The period of the pattern: inversely proportional to the separation of the sources, so the pattern is a measurement scale. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Interference `(→ Attribute)` `Property` `(→ Instance)` Visibility | Meso. Contrast of the fringes — the measurable trace of coherence, degrading with path difference. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Interference `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Coherence | Micro. The two waves must hold a stable phase relation over the integration time; independent sources fail this and show no pattern. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Interference `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Conservation of Energy | Micro. Interference redistributes energy; it never creates or destroys it, and the dark fringes are fed by the bright ones. |

**Limitations.** *Scale* — the fringe spacing sets a length scale, and structures much smaller than the wavelength cannot be resolved by the pattern. *Partial Observability* — a single-shot intensity measurement cannot separate coherence loss from amplitude loss. *Nonlinearity* — at high intensity the superposition principle itself fails. *Many-Body coupling* — in a medium, dispersion and absorption compete with interference and the visibility falls with thickness.

## References

- Young, T. (1804). Experiments and calculations relative to physical optics. *Philosophical Transactions of the Royal Society of London*, 94, 1–16. — the two-slit experiment, and the argument that removed the corpuscular reading
- Feynman, R. P., Leighton, R. B., & Sands, M. (1963). *The Feynman lectures on physics* (Vol. I, ch. 29–30). Addison-Wesley. — interference derived from adding amplitudes, which is the whole of the mechanism
- Born, M., & Wolf, E. (1999). *Principles of optics* (7th ed.). Cambridge University Press. — coherence stated properly, and the fringe visibility formalism
- [Interference (wave propagation)](https://en.wikipedia.org/wiki/Wave_interference)
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) · [Diffraction](/view.html?p=notes/nature/phenomena/diffraction.md) — the two phenomena that never occur apart in practice
- [Wave](/view.html?p=notes/nature/wave/wave.md) · [Light](/view.html?p=notes/nature/light.md) · [Frequency (Periodicity)](/view.html?p=notes/nature/frequency-periodicity.md)
