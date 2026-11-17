---
tags: [note, nature, phenomenon, wave, optics]
qa:
 - If speed depends on frequency, what is the speed of a pulse — and why does the answer need two different velocities?
 - A prism separates white light; is that dispersion, or only its visible symptom?
 - Dispersion limits fibre bandwidth and enables spectroscopy; is it a defect of media or a resource of instruments?
---

# Dispersion

> **Dispersion** is the dependence of a wave's speed on its frequency: in a dispersive medium the phase velocity is a function $v(\omega)$, and a composite wave — a pulse, a white beam, a broadband signal — therefore does not remain a copy of itself as it travels.

> Two velocities become necessary and they are not interchangeable. The **phase velocity** is the speed of a crest of one frequency; the **group velocity** is the speed of the envelope that the frequencies together make. When they differ, a pulse's shape changes while it moves, and the difference is the measure of the dispersion.

## Formulation

### What natural element type does this natural instance belong to?

`Propagation Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to a wave whose medium responds differently to different frequencies.

It is **not** a `Property` of the medium in the guide's narrow sense, though it is described by one (the refractive index as a function of frequency): the phenomenon is what a *wave* does because of that function. It is **not** **diffraction**, which separates waves spatially by propagation, while dispersion separates them by the medium's response. It is **not** a `Process`: nothing is produced — the components simply travel at different speeds.

### What is this natural instance?

> White light through a prism; the rainbow, which is the same thing with raindrops; a fibre-optic pulse smeared after kilometres; a chirped laser pulse compressed by a grating pair; the broadening of a radar pulse in the ionosphere; sound separating in the air over distance.

The mechanism is a frequency-dependent response, and its most useful statement is the definition that follows from it:

$$v_{\text{phase}}=\frac{\omega}{k},\qquad v_{\text{group}}=\frac{d\omega}{dk}.$$

Three consequences carry the phenomenon:

- **A pulse is a superposition, and its parts arrive at different times.** Group-velocity dispersion broadens a pulse in proportion to its spectral width and the distance travelled, which is the fundamental bandwidth limit of an optical link.
- **Material and geometric dispersion are different causes with the same effect.** In a medium it comes from the atomic response (a resonance far above the band, which raises the index); in a waveguide it comes from the geometry constraining which wavelengths fit. Fibres are engineered so the two cancel at one wavelength — the zero-dispersion point.
- **Angular dispersion is the instrument.** Because the deviation angle depends on frequency, a prism or a grating separates wavelengths spatially; every spectrometer is a dispersion measurement, and the resolving power is the angular spread divided by the angular width.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon — its kinds, the quantities that describe it and the bounds it imposes — not the waves and not the instruments built from it.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Dispersion | Meso. Speed dependence on frequency, and the separation that follows. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Dispersion `(→ Kind)` Material Dispersion | Meso. The medium's atomic response: normal dispersion raises the index with frequency, anomalous dispersion lowers it. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Dispersion `(→ Kind)` Waveguide Dispersion | Meso. Geometry: the structure admits different wavelengths at different effective speeds. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Dispersion `(→ Kind)` Modal Dispersion | Meso. Different paths through a multimode guide arrive at different times — the reason single-mode fibre exists. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Dispersion `(→ Attribute)` `Property` `(→ Instance)` Refractive Index Spectrum | Meso. $n(\omega)$: the measurable function the phenomenon is stated in. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Dispersion `(→ Attribute)` `Property` `(→ Instance)` Group-Velocity Dispersion | Meso. How fast a pulse broadens per unit length and unit bandwidth. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Dispersion `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Pulse Broadening | Micro. The fundamental bandwidth limit of a link: spectral width × dispersion × distance. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Dispersion `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Causality | Micro. Anomalous dispersion cannot exceed what the medium's response time permits — the reason a refractive index cannot be made to do everything. |

**Limitations.** *Nonlinearity* — at high intensity the index depends on the intensity too, so dispersion and nonlinearity mix (solitons, supercontinuum). *Partial Observability* — a single frequency measurement gives $n$ at one point, and the dispersion is the derivative, which is noisier. *Many-Body coupling* — in a fibre the material and waveguide contributions add with opposite signs, so the behaviour cannot be attributed to either alone.

## References

- Newton, I. (1704). *Opticks*. Sam. Smith & Benj. Walford. — the prism experiments, and the rejection of a single refractive index
- Fizeau, H. (1850s). — the measurement of light's speed in moving media, from which the dragging of the phase follows
- Born, M., & Wolf, E. (1999). *Principles of optics* (7th ed.). Cambridge University Press. — phase and group velocity, and the dispersion relations in full
- Agrawal, G. P. (2019). *Nonlinear fiber optics* (6th ed.). Academic Press. — group-velocity dispersion as the bandwidth limit, and the zero-dispersion design
- [Dispersion (optics)](https://en.wikipedia.org/wiki/Dispersion_(optics))
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) · [Diffraction](/view.html?p=notes/nature/phenomena/diffraction.md) · [Interference](/view.html?p=notes/nature/phenomena/interference.md)
- [Wave](/view.html?p=notes/nature/wave/wave.md) · [Light](/view.html?p=notes/nature/light.md) · [Speed of Light](/view.html?p=notes/nature/speed-of-light.md)
