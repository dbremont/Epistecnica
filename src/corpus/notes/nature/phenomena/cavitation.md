---
tags: [note, nature, phenomenon, fluid, phase]
qa:
 - A bubble that collapses is louder than the pressure that made it; where does that energy come from, and why does the collapse concentrate it?
 - Cavitation is a phase change caused by motion rather than by heating; does that make it a phenomenon of the liquid or of the flow?
 - Pumps, propellers and blood vessels all meet it; is avoiding cavitation a design constraint or a material one?
---

# Cavitation

> **Cavitation** is the formation of vapour bubbles in a liquid whose local pressure has fallen below its vapour pressure — not by heating, but by *moving*: a fast flow lowers pressure where it accelerates, and the liquid there boils at ambient temperature. The bubbles then collapse when they are carried back into higher pressure, and the collapse is violent because it is nearly isothermal and nearly spherical.

> The damage is the phenomenon's signature. A collapsing bubble focuses the energy of its whole volume into a point, producing a shock wave and, if it collapses against a surface, a microjet that erodes metal. A pump impeller can be destroyed by water that never exceeded forty degrees.

## Formulation

### What natural element type does this natural instance belong to?

`Surface and Phase Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to a phase change driven by a pressure field.

It is **not** boiling: boiling is driven by temperature and produces vapour throughout the volume; cavitation is driven by pressure and nucleates at weak points — dissolved gas, suspended particles, surface imperfections. It is **not** a `Process` — the phenomenon is the pattern, the process is this pump's cavity. It is **not** **capillary action**, though both are surface-tension phenomena and both are governed by the same interface: there the interface is pulled, here it is pulled apart.

### What is this natural instance?

> The rattle and erosion in a pump running too fast; the tip vortices of a ship's propeller; the noise of a kettle just before it boils, which is cavitation of the dissolved air, not boiling; the pistol-shrimp's claw, which fires a cavitation bubble to stun prey; ultrasonic cleaning baths, where the collapse is the cleaning agent; and the damage to heart valves and prosthetic implants.

Three facts organise the phenomenon:

- **The inception condition is a pressure, not a temperature.** Cavitation begins where the local pressure drops below $p_v$, which happens wherever a flow accelerates — around a blade tip, at a valve throat, on the suction side of a foil. The relevant dimensionless number is the cavitation number $\sigma=(p_\infty-p_v)/\tfrac12\rho U^2$: below a threshold value, cavities form.
- **The collapse concentrates energy.** Because the vapour condenses, the bubble has little thermal capacity to resist the collapse; the inertia of the surrounding liquid does the work, and the final stages produce pressures of hundreds of atmospheres and temperatures of thousands of kelvin locally. That is why cavitation erodes even stainless steel and why sonochemistry exists.
- **It is both a damage mechanism and a tool.** Avoided in pumps, propellers and turbines; used deliberately in cleaning, in sonochemistry, in wastewater treatment, and in medicine (histotripsy, lithotripsy).

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon — its kinds, the quantities that decide inception and the bounds it meets — not the machinery it occurs in, and not the chemistry of the collapse products.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Cavitation | Meso. Vapour bubble formation and collapse from a pressure drop in a liquid. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Cavitation `(→ Kind)` Hydrodynamic Cavitation | Meso. In a flowing liquid: blade tips, valve throats, Venturi sections. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Cavitation `(→ Kind)` Acoustic Cavitation | Meso. In a sound field: ultrasonic cleaning, sonochemistry, lithotripsy. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Cavitation `(→ Kind)` Inertial Cavitation | Meso. The violent case: growth and rapid collapse with a shock, which is the one that damages surfaces. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Cavitation `(→ Attribute)` `Property` `(→ Instance)` Cavitation Number | Meso. $(p_\infty-p_v)/\tfrac12\rho U^2$: the dimensionless group that predicts inception. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Cavitation `(→ Attribute)` `Property` `(→ Instance)` Nucleation Sites | Meso. Dissolved gas, particles and wall imperfections: without them a clean liquid withstands tension far below its vapour pressure. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Cavitation `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Vapour Pressure | Micro. Below $p_v$ the liquid phase is not the stable one: the bound that defines the phenomenon. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Cavitation `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Material Damage | Micro. Repeated collapse erodes surfaces, limits impeller speed, and is the engineering bound on any design that must avoid it. |

**Limitations.** *Scale* — inception depends on nuclei measured in micrometres, which are not observable in a real machine. *Uncertainty* — the inception pressure varies with the liquid's history, so the same pump may cavitate today and not tomorrow. *Nonlinearity* — the collapse itself is a strong nonlinearity: shocks, sonoluminescence, and chemistry that the linear acoustics of the drive cannot predict. *Many-Body coupling* — bubbles interact with one another and with the wall, so a cloud behaves differently from a single bubble.

## References

- Rayleigh, L. (1917). On the pressure developed in a liquid during the collapse of a spherical cavity. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 34(200), 94–98. — the collapse calculation, still the model
- Plesset, M. S. (1949). The dynamics of cavitation bubbles. *Journal of Applied Mechanics*, 16, 277–282. — the bubble with surface tension and viscosity included
- Brennen, C. E. (1995). *Cavitation and bubble dynamics*. Oxford University Press. — the standard treatment, from inception to damage
- [Cavitation](https://en.wikipedia.org/wiki/Cavitation)
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) · [Capillary Action](/view.html?p=notes/nature/phenomena/capillary-action.md)
- [Fluid](/view.html?p=notes/nature/body/fluid.md) · [Turbulence](/view.html?p=notes/nature/turbulence.md) · [Vapour Pressure](/view.html?p=notes/nature/phase-change-materials-pcms.md)
