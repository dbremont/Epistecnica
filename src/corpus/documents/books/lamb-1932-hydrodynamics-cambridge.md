---
tags: [document, book, hydrodynamics, fluid-mechanics, classical-mechanics]
---

# Lamb, H. (1932). Hydrodynamics (6th ed.). Cambridge University Press.

```python
@book{lamb1932hydrodynamics,
  title = {Hydrodynamics},
  author = {Lamb, Horace},
  edition = {6},
  publisher = {Cambridge University Press},
  address = {Cambridge},
  year = {1932},
  note = {Reprinted by Dover Publications, New York, 1945},
}
```

## Notes

Lamb's *Hydrodynamics* is the classical treatise on the motion of fluids: the kinematics of a fluid, the equations of motion, irrotational motion and the velocity potential, the theory of waves, vortex motion, and the viscous fluid. It is the book that made the subject teachable at a level between the original memoirs and the modern computational treatment — every result is derived, and the derivation is the argument.

**The scope.** The book is organised by the mathematical object rather than by the engineering application: the first chapters establish the kinematics (streamlines, vorticity, the stream function, the velocity potential); the middle chapters treat irrotational flow, sources and sinks, spheres and cylinders in a stream, the motion of solids through a fluid, and the vortex theorems of Helmholtz and Kelvin; the later chapters carry waves on water, the tides, and viscous motion. Each topic is developed with the classical methods — conformal mapping in two dimensions, spherical harmonics in three — and the physical interpretation follows the calculation.

**Its place.** Lamb (1849–1934) was the Cambridge mathematician who, with Horace Lamb's own *Hydrodynamics* (1878, six editions to 1932) and Rayleigh's *Theory of Sound*, set the standard vocabulary of classical fluid dynamics. The sixth edition is the settled version: the subject had been built, the results were in the book, and the next change was not another edition but a different method — the numerical solution of the [Navier–Stokes equations](/view.html?p=notes/epistemica/singular/navierstokes-equations.md) on computers.

**What it still gives.** The exact solutions — the potential flow past a sphere, the Rankine vortex, the Stokes flow past a sphere, the deep-water wave dispersion relation, the Kutta–Joukowski lift — are the reference cases every numerical code is checked against, and the derivations are the derivations those cases are cited for. It is a reference book in the strict sense: one goes to it for the solution that has a closed form, before asking the computer for the one that does not.

**The limits.** The book predates boundary-layer theory's absorption into the mainstream (Prandtl's 1904 paper is in the literature, not yet in the teaching), turbulence is treated as a phenomenon rather than a closure problem, and nothing here anticipates computational fluid dynamics. It is classical hydrodynamics, deliberately — and the deliberate boundary is what makes it still usable.

## Editions

> *Hydrodynamics* was first published in **1878**, when Lamb was in his twenties and the subject was still being assembled from the memoirs of Euler, Lagrange, Cauchy, Stokes, Helmholtz and Kelvin. It then grew through **six editions**, reaching the sixth in **1932** — the last in Lamb's lifetime; he died in 1934. The editions track the growth of the field: each one absorbed the results that had become classical since the previous, and the sixth is the settled compendium rather than a new argument.

| Edition | Date | Note |
| --- | --- | --- |
| First | 1878 | The young Cambridge mathematician's synthesis of the classical memoirs |
| … | — | The intermediate editions expand with the subject (waves, vortices, viscous motion) |
| **Sixth** | **1932** | The settled text; the edition every later citation refers to |
| Dover reprint | 1945 | The sixth edition kept in print; the copy usually found second-hand |

> The publishing history matters for citation. A reference to "Lamb, *Hydrodynamics*" almost always means the sixth edition; the page numbers of the earlier editions do not agree with it, and the archive.org scan (`hydrodynamics00lamb`) is the Dover reprint of the sixth.

## References

- [Hydrodynamics](https://archive.org/details/hydrodynamics00lamb) — the Internet Archive scan (Dover reprint, 1945)
- [Navier–Stokes Equations](/view.html?p=notes/epistemica/singular/navierstokes-equations.md) — the equation the treatise sets up and solves in special cases
- [Continuum Mechanics Framework](/view.html?p=notes/epistemica/singular/continuum-mechanic-framework.md) — the general framework the book specialises
- [Fluid](/view.html?p=notes/nature/body/fluid.md) — the natural element whose motion is modelled
- [Transport Phenomena](/view.html?p=notes/nature/transport-phenomena.md) — momentum, heat and mass transport in the same language
- [Bernoulli, D. (1738). *Hydrodynamica*.](/view.html?p=documents/books/bernoulli-1738-hydrodynamica.md) — the founding treatise of the subject
- [Lamb, H.](https://en.wikipedia.org/wiki/Horace_Lamb) — the author
