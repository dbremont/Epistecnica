---
tags: [note, measurement, system, si]
---

# International System of Units

> The **International System of Units** (French *Système International d'Unités*, abbreviated **SI**) is the measurement system in scientific and legal use: **seven base quantities**, one **base unit** each, and every other unit derived from them as a product of powers with no numerical factor. Since 2019 every one of its base units is fixed by an exact value of a constant of nature, not by a physical object.

## Definition

The system is the point of [Measurement System](/view.html?p=notes/epistemica/quantization/system.md)'s space at which the base quantities are the seven below, the system is coherent and rationalised, multiples are decimal, and the realization basis is a set of fixed constants.

| Base quantity | Base unit | Symbol |
| --- | --- | --- |
| time | second | $\mathrm{s}$ |
| length | metre | $\mathrm{m}$ |
| mass | kilogram | $\mathrm{kg}$ |
| electric current | ampere | $\mathrm{A}$ |
| thermodynamic temperature | kelvin | $\mathrm{K}$ |
| amount of substance | mole | $\mathrm{mol}$ |
| luminous intensity | candela | $\mathrm{cd}$ |

Every other unit is a **coherent derived unit**: a product of powers of the base units with coefficient $1$. **Dimensionless derived units** (the radian, the steradian) carry a dimension of $1$ and are included for clarity.

## Realization: the 2019 Revision

Before 2019 the base units rested on artefacts and on procedures: the kilogram on a platinum–iridium cylinder in Sèvres, the ampere on a thought experiment about parallel wires. Since the 26th General Conference on Weights and Measures (2018, effective 20 May 2019) each base unit is defined by fixing the numerical value of a named constant:

| Constant | Symbol | Fixed value | Fixes |
| --- | --- | --- | --- |
| caesium hyperfine frequency | $\Delta\nu_{\mathrm{Cs}}$ | $9\,192\,631\,770\ \mathrm{Hz}$ | the second |
| speed of light in vacuum | $c$ | $299\,792\,458\ \mathrm{m\,s^{-1}}$ | the metre |
| Planck constant | $h$ | $6.626\,070\,15\times10^{-34}\ \mathrm{J\,s}$ | the kilogram (with $c$ and $\Delta\nu_{\mathrm{Cs}}$) |
| elementary charge | $e$ | $1.602\,176\,634\times10^{-19}\ \mathrm{C}$ | the ampere |
| Boltzmann constant | $k$ | $1.380\,649\times10^{-23}\ \mathrm{J\,K^{-1}}$ | the kelvin |
| Avogadro constant | $N_{\mathrm{A}}$ | $6.022\,140\,76\times10^{23}\ \mathrm{mol^{-1}}$ | the mole |
| luminous efficacy | $K_{\mathrm{cd}}$ | $683\ \mathrm{lm\,W^{-1}}$ | the candela |

The revision changed the *realization basis* coordinate, not the units' sizes: the metre, the second and the ampere kept their magnitude to within measurement uncertainty, and the kilogram, the ampere, the kelvin and the mole moved by amounts below what most instruments can see. The consequence is that the system is now **closed over constants**: a better measurement of a constant refines the realization of a unit, and no unit depends on a particular object surviving in a vault.

## Derived Units

A derived unit is written as a monomial over the base units; some carry a **special name** for brevity, and that name is itself a coherent derived unit.

| Quantity | Unit | Symbol | In base units |
| --- | --- | --- | --- |
| force | newton | $\mathrm{N}$ | $\mathrm{kg\,m\,s^{-2}}$ |
| energy | joule | $\mathrm{J}$ | $\mathrm{kg\,m^{2}\,s^{-2}}$ |
| power | watt | $\mathrm{W}$ | $\mathrm{kg\,m^{2}\,s^{-3}}$ |
| pressure | pascal | $\mathrm{Pa}$ | $\mathrm{kg\,m^{-1}\,s^{-2}}$ |
| frequency | hertz | $\mathrm{Hz}$ | $\mathrm{s^{-1}}$ |
| electric charge | coulomb | $\mathrm{C}$ | $\mathrm{A\,s}$ |
| potential difference | volt | $\mathrm{V}$ | $\mathrm{kg\,m^{2}\,s^{-3}\,A^{-1}}$ |
| capacitance | farad | $\mathrm{F}$ | $\mathrm{kg^{-1}\,m^{-2}\,s^{4}\,A^{2}}$ |
| resistance | ohm | $\Omega$ | $\mathrm{kg\,m^{2}\,s^{-3}\,A^{-2}}$ |

## Prefixes

Decimal multiples and submultiples attach to a unit name and symbol and scale the unit, never the quantity: $\mathrm{km} = 10^{3}\,\mathrm{m}$, $\mu\mathrm{s} = 10^{-6}\,\mathrm{s}$. The prefix belongs to the symbol, so $\mathrm{kg}$ is a base unit despite carrying a prefix — the prefix is part of its name, and no double prefixes are allowed ($10^{-9}\,\mathrm{kg}$, not $\mathrm{\mu kg}$).

## Non-SI Units in Use

The system does not derive everything scientists use. A short accepted list survives because the quantity is culturally or practically entrenched: the minute, hour and day; the degree of arc; the litre; the tonne; the ångström ($10^{-10}\,\mathrm{m}$) in crystallography; the electronvolt in particle physics; the dalton in chemistry. They are **defined in terms of SI units** and used alongside them, which keeps a measurement in them convertible — that convertibility is what makes accepting them tolerable.

## What SI Does Not Cover

- **Customary systems** — the US customary and imperial systems remain the legal systems for trade in some jurisdictions, so a measurement system is a legal object as well as a scientific one.
- **Non-coherent specialised units** — the bar, the atmosphere, the calorie, the kilowatt-hour: convenient, defined in SI terms, not coherent.
- **The measurement theory** — *which* attribute is being measured and *how* its numbers are justified is [Measurement Theory](/view.html?p=notes/epistemica/quantization/measurement-theory.md)'s question; SI only fixes the units the numbers carry.

## References

- https://en.wikipedia.org/wiki/International_System_of_Units
- https://www.bipm.org/en/measurement-units
- [SI Brochure: The International System of Units](https://www.bipm.org/en/publications/si-brochure) — 9th edition, 2019
- [Measurement System](/view.html?p=notes/epistemica/quantization/system.md) — the space of systems this one sits in
- [Measurement Theory](/view.html?p=notes/epistemica/quantization/measurement-theory.md) — the representation the units realize
- [Symbol Atlas](/corpus/notes/epistemica/symbols.html) — the notation of the unit symbols
