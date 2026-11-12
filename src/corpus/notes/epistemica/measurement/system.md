---
tags: [note, measurement, system]
---

# Measurement System

> A **measurement system** is the constellation of units, standards and rules that a body of work uses to attach numbers to quantities: a set of **base quantities**, a **base unit** chosen for each, and the **rules** that derive every other unit from those and tie each to a physical realization. It is what turns the mapping of [Measurement Theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md) — empirical relational system → numerical relational system — into numbers anyone can reproduce.

## Definition

A measurement system is a triple

$$S = (Q,\ U,\ R)$$

where

- **$Q$** is a chosen set of **base quantities** — length, mass, time and whatever else the system decides not to derive (electric current, temperature, amount of substance, luminous intensity);
- **$U$** is a **base unit** for each quantity in $Q$ — metre, kilogram, second, …;
- **$R$** is the rule set: the derivation rules that build every other unit as a product of powers of the base units, and the **realization** that fixes what each base unit means — an artefact, a physical effect, or a fixed value of a constant of nature.

Every other unit in the system is a **derived unit**, a monomial $\prod u_i^{e_i}$ over the base units, so the choice $(Q, U, R)$ is the whole of the system: change any one of the three and you have a different system.

## Unit, Quantity and Dimension

The three terms are routinely conflated and the system depends on keeping them apart.

| Term | What it is | Example |
| --- | --- | --- |
| **Quantity** | a measurable attribute of a thing | the length of a rod, a duration, an electric current |
| **Dimension** | the *kind* of a quantity, independent of any unit — the exponent pattern over the base quantities | length has dimension $\mathsf{L}$; a velocity $\mathsf{L}\,\mathsf{T}^{-1}$ |
| **Unit** | the scale chosen to express one quantity | metre, second, ampere |

A dimension is what stays fixed when the system changes; a unit is what the system supplies. **Dimensional analysis** is the invariance this buys: an equation between physical quantities must be dimensionally homogeneous whatever units are used, so a system's job is to make that homogeneity checkable.

## The Space of Measurement Systems

Measurement systems are not alternatives to be listed but **points in a space**, and the space has a few decisive coordinates. Each system is a choice along every one of them.

| Coordinate | The choice | Extreme positions |
| --- | --- | --- |
| **Base quantities** | which quantities are taken as primitive | length–mass–time only (CGS, MKS) vs a system adding electric current as its own base (MKSA, SI) |
| **Coherence** | whether derived units are products of powers of base units with no numerical factor | coherent (newton $= \mathrm{kg\,m\,s^{-2}}$) vs non-coherent (kilogram-force, where $1\,\mathrm{kgf} = 9.80665\,\mathrm{N}$) |
| **Rationalisation** | whether the $4\pi$ of the solid-angle factor is absorbed into the unit | rationalised (MKSA, SI) vs unrationalised (CGS-electrostatic) |
| **Realization basis** | what fixes the size of each base unit | artefact (the international prototype kilogram, 1889–2019) vs fixed constant of nature ($h$, $c$, $e$, $k$, $N_A$ since 2019) |
| **Prefixes** | whether multiples are expressed by decimal prefixes on one unit or by separate names | SI prefixes ($\mathrm{km}$, $\mu\mathrm{s}$) vs customary systems (inch, foot, mile) |
| **Admission of non-SI units** | which units outside the system are tolerated and for how long | SI's accepted non-SI units (minute, hour, litre, ångström, electronvolt) |

**The historic points in this space**, each a different coordinate choice:

| System | Base quantities | Realization | Why it lost or won |
| --- | --- | --- | --- |
| CGS | length, mass, time | artefacts and mercury columns | convenient at laboratory scale; two competing electrical branches (electrostatic and electromagnetic) |
| MKS | length, mass, time | artefacts | a size fix, not a structure fix |
| MKSA / Giorgi | length, mass, time, **current** | artefacts | the electrical units stop being an extra family: one coherent set covers mechanics and electromagnetism |
| SI | the seven base quantities | artefacts, then fixed constants (2019) | the current system: coherent, rationalised, decimal, traceable to constants |

The trajectory is a walk through that space, not a succession of unrelated conventions: each step changes one coordinate — MKS changes the size, Giorgi adds a base quantity, SI rationalises and completes the set, the 2019 revision changes the realization basis from artefacts to constants.

## Structure of a System

- **Base units** — one per base quantity; the only units the system *declares* rather than derives.
- **Derived units** — every unit that follows from the base ones by the derivation rules; some carry special names for convenience (newton, joule, watt, pascal).
- **Prefixes** — decimal multiples and submultiples attached to a unit name and symbol; they scale the *unit*, never the quantity.
- **Accepted non-SI units** — units a system admits without deriving them, because they are too entrenched to displace: the minute and hour, the litre, the ångström ($10^{-10}\,\mathrm{m}$) in crystallography, the electronvolt in particle physics.
- **Realization and traceability** — for each unit, the physical procedure that produces it and the chain of calibrations that links a working instrument back to it. This is the coordinate that makes a system *usable* rather than merely named.

The system in current scientific use is the [International System of Units](/view.html?p=notes/epistemica/measurement/isu.md), which sits at one point of this space.

## References

- [System of units of measurement](https://en.wikipedia.org/wiki/System_of_units_of_measurement)
- [Non-SI units](https://www.sciencelearn.org.nz/resources/1872-non-si-units)
- [Ångström](https://en.wikipedia.org/wiki/Angstrom)
- [Dimensional analysis](https://en.wikipedia.org/wiki/Dimensional_analysis)
- [International System of Units](/view.html?p=notes/epistemica/measurement/isu.md) — the system in current use
- [Measurement Theory](/view.html?p=notes/epistemica/measurement/measurement-theory.md) — the representation the system realizes
- [Symbol Atlas](/corpus/notes/epistemica/symbols.html) — the notation units are written in
