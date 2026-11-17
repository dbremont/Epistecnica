---
tags: [note, nature, phenomenon, wave, optics]
qa:
 - If light travels in straight lines, why does it arrive where geometry says it cannot — and why is the answer a bound on every instrument rather than a curiosity?
 - Diffraction sets resolution; what exactly is being traded when an instrument is made larger, and is the trade about light or about aperture?
 - Is a shadow's edge a fact about the obstacle or about the wave — where does the phenomenon actually occur?
---

# Diffraction

> **Diffraction** is the spreading of a wave into the region that a straight-line description would leave dark. It is not a defect of edges or a failure of lenses: it is what a wave does whenever it passes an aperture or an obstacle comparable in size to its wavelength, and it therefore sets a floor under the resolution of every instrument that uses waves.

> Its importance is not that it is surprising but that it is **unavoidable**. A microscope cannot resolve below roughly half a wavelength by any refinement of its lenses, because the information that would distinguish two closer points has already spread out before the light reaches the first element.

## Formulation

### What natural element type does this natural instance belong to?

`Propagation Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to a wave's encounter with an aperture or an obstacle.

It is **not** a `Bound` or a `Constraint`, although it produces one: the resolution limit is a consequence of the phenomenon, and the guide would file *that* as a constraint on instruments. It is **not** **interference**, though a diffraction pattern *is* an interference pattern — diffraction is the spreading caused by the aperture, interference is what the spread parts then do to one another. It is **not** a `Process`: nothing is carried through the shadow; the amplitude distribution simply evolves.

### What is this natural instance?

> The soft edge of a shadow, with fringes inside it; a laser spot that is never a point; sound audible around a corner; radio reception behind a hill; the rings around a star in a telescope image; the inability of a microscope to separate two bacteria closer than a few hundred nanometres; X-ray diffraction from a crystal, which is the same phenomenon used as a ruler.

Two regimes, and the small-angle one is the instrument's:

- **Fraunhofer, far field.** A plane wave through an aperture produces a pattern whose angular width is $\theta\approx\lambda/D$ for aperture $D$: wider aperture, narrower spread. That inverse relation is the resolution law — the Rayleigh criterion writes it as $\theta_{\min}=1.22\,\lambda/D$ for a circular aperture.
- **Fresnel, near field.** Close to the aperture, the pattern is a set of fringes whose spacing changes with distance; a shadow edge is not sharp but is crossed by bands.

The phenomenon is also an instrument. Because the pattern depends on the structure that scatters the wave, irradiating a specimen and reading the pattern is a measurement of the specimen at scales far below the wavelength of visible light: X-ray crystallography, electron diffraction, and the diffraction grating as the dispersing element in a spectrometer.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon — its regimes, the quantities that set the pattern and the bounds it imposes — not the waves themselves and not the instruments, which are technica.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Diffraction | Meso. Spreading of a wave into the geometrically excluded region. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Diffraction `(→ Kind)` Fraunhofer Diffraction | Meso. Far-field regime: angular width inversely proportional to aperture size. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Diffraction `(→ Kind)` Fresnel Diffraction | Meso. Near-field regime: fringe structure that changes with distance from the aperture. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Diffraction `(→ Kind)` Diffraction Grating | Meso. Periodic structure used deliberately, so that the pattern becomes a wavelength scale. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Diffraction `(→ Attribute)` `Property` `(→ Instance)` Angular Spread | Meso. $\lambda/D$: the width of the central maximum, and the quantity resolution is written in. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Diffraction `(→ Attribute)` `Property` `(→ Instance)` Fringe Structure | Meso. The secondary maxima and minima: the Fourier transform of the aperture, which is why the pattern is a measurement. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Diffraction `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Resolution Limit | Micro. Two sources closer than about $\lambda/2D$ cannot be separated by any image formed from that wave — the bound every optical instrument meets. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Diffraction `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Wavelength Comparability | Micro. The effect is negligible when the aperture is many wavelengths wide, and dominant when it is comparable: the condition that decides whether a ray description is usable. |

**Limitations.** *Scale* — the phenomenon is defined relative to the wavelength, so the same obstacle diffracts radio and blocks light. *Partial Observability* — the phase of the diffracted field is lost in an intensity measurement unless interferometry is used. *Many-Body coupling* — in a crystal the pattern is the superposition of scattering from many centres, which is what makes it informative and what makes it hard to invert.

## References

- Young, T. (1804). Experiments and calculations relative to physical optics. *Philosophical Transactions of the Royal Society of London*, 94, 1–16. — the observations from which diffraction and interference were read together
- Fresnel, A. (1818). Mémoire sur la diffraction de la lumière. *Annales de Chimie et de Physique*, 1, 239–281. — the near-field treatment, and the argument that carried the wave theory
- Born, M., & Wolf, E. (1999). *Principles of optics* (7th ed.). Cambridge University Press. — Fraunhofer and Fresnel regimes, and the resolution criteria
- Feynman, R. P., Leighton, R. B., & Sands, M. (1963). *The Feynman lectures on physics* (Vol. I, ch. 30). Addison-Wesley.
- [Diffraction](https://en.wikipedia.org/wiki/Diffraction)
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) · [Interference](/view.html?p=notes/nature/phenomena/interference.md)
- [Wave](/view.html?p=notes/nature/wave/wave.md) · [Light](/view.html?p=notes/nature/light.md) · [Microscopy](/view.html?p=notes/nature/microscopy.md)
