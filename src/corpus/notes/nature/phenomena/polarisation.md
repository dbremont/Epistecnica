---
tags: [note, nature, phenomenon, wave, optics]
qa:
 - Polarisation is invisible to the naked eye unaided; what makes a transverse wave's orientation observable at all?
 - Is unpolarised light a mixture or a superposition — and does the answer change what a polarising filter does to the intensity?
 - If a wave can be polarised only when it is transverse, is polarisation a phenomenon of light or the evidence that light is transverse?
---

# Polarisation

> **Polarisation** is the orientation of a transverse wave's oscillation in the plane perpendicular to its direction of travel. It is not an extra property added to light: it is the fact that light *has* an orientation, and its observability is the classical evidence that light is transverse rather than longitudinal.

> The phenomenon is the reason a reflected glare can be filtered out, a liquid-crystal display can switch, and a stressed plastic model can be read as a stress map. It is also the classical case where a wave has more degrees of freedom than a scalar description admits: two independent transverse directions, and anything in between.

## Formulation

### What natural element type does this natural instance belong to?

`Propagation Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to the transverse orientation of a wave.

It is **not** a `Property` of the wave in the simple sense, though each wave carries a polarisation state: the phenomenon includes what *changes* it — reflection, transmission through a medium, scattering — and those changes are the measurable content. It is **not** **interference** in general, although two beams of different polarisation interfere differently, and the 90-degree case does not interfere at all: that is the observation that makes polarisation a separate degree of freedom. It is **not** a `Process`.

### What is this natural instance?

> The glare off a wet road, cut by polarising sunglasses; the blue of the sky, which is polarised at ninety degrees from the sun by scattering; a liquid-crystal pixel switching between transmitting and blocking; a stressed transparent model showing coloured bands between crossed polarisers; the rotation of the plane of polarisation by a sugar solution.

The mechanism is a transverse vector field, and the essential facts are few:

- **Two independent states.** Any transverse wave decomposes into two orthogonal linear polarisations, or into left- and right-circular ones. A polariser passes one component, so it reduces the intensity of unpolarised light by half — and of already-polarised light by $\cos^2\theta$.
- **The medium can rotate or select.** Birefringent materials have two refractive indices, so the two components travel at different speeds and the state changes along the path; dichroic materials absorb one component and are therefore polarisers; optically active solutions rotate the plane, which is how a polarimeter measures sugar concentration.
- **Reflection polarises.** Light reflected near the Brewster angle is completely polarised in one direction, which is why the glare from a horizontal surface is horizontally polarised and why the filter that removes it is vertical.
- **Scattering polarises.** A dipole re-radiating light does so with a pattern that is fully polarised at ninety degrees to the incident beam — the sky's polarisation, and a natural compass used by some insects.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon — its kinds, the quantities that describe a state and the bounds it meets — not the electromagnetic field theory that underlies it, and not the displays and instruments that use it.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Polarisation | Meso. Orientation of a transverse wave's oscillation, and what changes it. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Polarisation `(→ Kind)` Linear Polarisation | Meso. The field oscillates along one line; the state a filter selects. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Polarisation `(→ Kind)` Circular Polarisation | Meso. The field rotates as it propagates: the state of a photon's helicity, and of a quarter-wave plate output. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Polarisation `(→ Kind)` Birefringence | Meso. Two refractive indices, so the two components separate or accumulate a phase difference. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Polarisation `(→ Attribute)` `Property` `(→ Instance)` Polarisation State | Meso. The description of the ellipse the field traces: two angles, or a Stokes vector. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Polarisation `(→ Attribute)` `Property` `(→ Instance)` Degree of Polarisation | Meso. How much of the intensity is in a definite state — one for a laser, zero for a lamp, a fraction for the sky. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Polarisation `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Transversality | Micro. Only transverse waves polarise; a longitudinal wave has no orientation to select — which is what makes the phenomenon a test of the wave's nature. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Propagation Phenomenon `(→ Instance)` Polarisation `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Malus's Law | Micro. A polariser transmits $\cos^2$ of the incident intensity from the aligned state: the bound that makes the phenomenon quantitative. |

**Limitations.** *Scale* — the state is defined for a beam, and at the single-photon level it becomes a statement about probability. *Partial Observability* — the phase between the two components is not measured by an intensity detector; a quarter-wave plate or an interferometer is needed. *Many-Body coupling* — in a scattering medium the state degrades along the path, so what arrives is a mixture whose degree of polarisation is a property of the whole path.

## References

- Malus, É.-L. (1809). Sur une propriété de la lumière réfléchie par les corps diaphanes. *Mémoire de la Société d'Arcueil*, 2, 143–158. — the reflection law, and the first quantitative statement of the phenomenon
- Brewster, D. (1815). On the laws which regulate the polarisation of light by reflexion from the surfaces of transparent bodies. *Philosophical Transactions of the Royal Society of London*, 105, 125–159. — the angle at which the reflected beam is completely polarised
- Born, M., & Wolf, E. (1999). *Principles of optics* (7th ed.). Cambridge University Press. — Stokes vectors, Jones calculus and the full phenomenology
- Hecht, E. (2017). *Optics* (5th ed.). Pearson. — the working account, with the instruments
- [Polarization (waves)](https://en.wikipedia.org/wiki/Polarization_(waves))
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) · [Interference](/view.html?p=notes/nature/phenomena/interference.md) · [Dispersion](/view.html?p=notes/nature/phenomena/dispersion.md)
- [Wave](/view.html?p=notes/nature/wave/wave.md) · [Light](/view.html?p=notes/nature/light.md) · [Polarity](/view.html?p=notes/nature/polarity.md)
