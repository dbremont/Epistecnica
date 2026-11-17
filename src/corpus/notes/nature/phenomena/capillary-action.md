---
tags: [note, nature, phenomenon, fluid, surface]
qa:
 - A liquid climbs a tube against gravity; what pays for the height it gains, and why does the tube's diameter decide it?
 - Is capillary rise a phenomenon of the liquid, of the solid, or of the interface — and why can none of the three be named as its cause alone?
 - Soil, paper, plant stems and wicks all move water without a pump; is that one phenomenon or several that share a length scale?
---

# Capillary Action

> **Capillary action** is the rise or depression of a liquid in a narrow passage, produced by the competition between **surface tension** pulling the meniscus and **adhesion** holding the liquid to the wall. When adhesion wins, the meniscus is concave and the liquid climbs; when cohesion wins, it is convex and the liquid is pushed down.

> Its scale is the point: the height a liquid reaches is inversely proportional to the passage's radius, so the effect is negligible in a bucket and dominant in a pore. Every porous material — soil, paper, cloth, concrete, lung tissue — is a network of passages where this dominates.

## Formulation

### What natural element type does this natural instance belong to?

`Surface and Phase Phenomenon` at **meso** level of organization (Ontic; Dynamical) — `Phenomenon` specialized to a liquid interface in a confined geometry.

It is **not** a `Property`, though it is described by two (surface tension, contact angle): the phenomenon is the *motion* that the pair produces in a passage of finite width. It is **not** a `Process` — nothing is consumed or transformed; the liquid moves until the pressure balance closes. It is **not** **cavitation**, which is the same interface failing under tension rather than being pulled by it.

### What is this natural instance?

> Water climbing a glass capillary; mercury being depressed in the same tube, because its cohesion beats its adhesion to glass; a paper towel wicking; a candle's wax drawn up the wick; a plant lifting water against gravity in its xylem; damp rising through a wall; a sponge filling; chromatography, where the mobile phase is moved by exactly this mechanism.

The balance is a pressure difference and a weight, and the static result is the one worth remembering:

$$h=\frac{2\gamma\cos\theta}{\rho g r},$$

which says the height grows with surface tension $\gamma$ and the cosine of the contact angle, and falls with density, gravity and — decisively — the **radius** $r$. Four consequences:

- **Smaller means higher**, so a finer pore beats a coarser one; the same relation explains why a compacted soil wicks water differently from a loose one.
- **The contact angle is the switch.** Below ninety degrees the liquid wets the wall and rises; above, it is non-wetting and is depressed. The angle is a property of the *pair*, not of the liquid alone, which is why surface treatment changes the behaviour without changing the fluid.
- **The dynamics are slow and diffusive.** The static height is one thing; the rate of rise goes as the square root of time, because the driving pressure is constant while the viscous resistance grows with the wetted length — Lucas–Washburn.
- **The effect is a pump with no moving parts**, and it is why so much microfluidics works without one: a paper strip is a capillary pump.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the phenomenon at the interface — its kinds, the quantities that set the height and the bounds it meets — not the liquid's bulk properties and not the porous medium's structure, both of which are decomposed on their own shelves.
>
> Identity: paths begin at `Ontic Element`, one labelled link per row, types backticked, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Capillary Action | Meso. Rise or depression of a liquid in a narrow passage. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Capillary Action `(→ Kind)` Capillary Rise | Meso. Wetting case: the meniscus is concave and the liquid climbs. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Capillary Action `(→ Kind)` Capillary Depression | Meso. Non-wetting case: mercury in glass, where cohesion beats adhesion and the level falls. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Capillary Action `(→ Kind)` Wicking | Meso. Rise in a porous network: paper, cloth, soil, where the pore-size distribution sets the front. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Capillary Action `(→ Attribute)` `Property` `(→ Instance)` Contact Angle | Meso. The wetting parameter of the liquid–solid pair, which decides rise against depression. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Capillary Action `(→ Attribute)` `Property` `(→ Instance)` Capillary Length | Meso. The length scale at which gravity and surface tension balance — the size of a meniscus and the depth a wick can climb. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Capillary Action `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Pressure Balance | Micro. Rise stops when the weight of the column equals the capillary pressure: the static bound of the phenomenon. |
| `Ontic Element` `(→ Kind)` `Phenomenon` `(→ Kind)` Surface and Phase Phenomenon `(→ Instance)` Capillary Action `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Pore Size | Micro. The radius sets the height and the rate; below a few nanometres other forces take over and the law stops applying. |

**Limitations.** *Scale* — the law is a continuum result and fails at molecular pore sizes; at the other end, a pore wider than the capillary length shows almost nothing. *Uncertainty* — contact angles show hysteresis between advancing and receding fronts, so one number does not describe a moving meniscus. *Many-Body coupling* — in a real porous medium the pores are distributed in size, so the front is a competition rather than a height. *Partial Observability* — inside an opaque medium the front is measured only at its surface.

## References

- Young, T. (1805). An essay on the cohesion of fluids. *Philosophical Transactions of the Royal Society of London*, 95, 65–87. — the contact angle, and the foundation of the whole account
- Laplace, P.-S. (1805). *Traité de mécanique céleste* (Suppl. 10). — the pressure difference across a curved interface, the other half of the law
- Washburn, E. W. (1921). The dynamics of capillary flow. *Physical Review*, 17(3), 273–283. — the square-root-of-time kinetics of a rising front
- Feynman, R. P., Leighton, R. B., & Sands, M. (1963). *The Feynman lectures on physics* (Vol. II, ch. 40). Addison-Wesley. — surface tension and the capillary length derived from an energy balance
- [Capillary action](https://en.wikipedia.org/wiki/Capillary_action)
- [Phenomena](/view.html?p=notes/nature/phenomena/phenomena.md) · [Cavitation](/view.html?p=notes/nature/phenomena/cavitation.md)
- [Surfaces and Capillarity](/view.html?p=notes/nature/porosity.md) · [Soil](/view.html?p=notes/nature/matter/geological/soil.md) · [Porous Media Transport](/view.html?p=notes/nature/porous-media-transport.md)
