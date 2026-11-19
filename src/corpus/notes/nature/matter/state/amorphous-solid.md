---
tags: [note, nature, substance-matter, materials-science, matter]
qa:
 - Is an amorphous solid a state of matter or a state of arrest — and does the distinction survive a very slow experiment?
 - If a glass is metastable, at what point does its relaxation time exceed the age of the universe, and what would it mean for the classification if it did?
 - Is the glass transition a phase transition in disguise, or a kinetic crossover that only looks like one?
---

# Amorphous Solid

> An **amorphous solid** is a solid without long-range order: its atoms or molecules are frozen in a disordered arrangement, with short-range order but no periodic lattice. A **glass** is the canonical case — a liquid that was cooled fast enough to miss crystallisation and became rigid instead, with the disorder of the liquid retained. The distinction from a crystal is not that one is ordered and the other is not, but that one has *periodicity* and the other has only local packing.

> The important point is that the amorphous solid is not an equilibrium phase. A crystal is the thermodynamic minimum; a glass is a configuration that the system cannot leave on the timescale of observation. It is a **kinetically arrested** state, and that is why the same material can be crystalline or amorphous depending on how it was made, and why heating it produces first softening and then, above the glass transition, a liquid that will eventually crystallise if it has the time.

## Formulation

### What natural element type does this natural instance belong to?

`Substance / Matter` at **meso** level of organization (Constituent) — a stuff-kind individuated by composition and by the arrangement its constituents were frozen into. It is the disordered counterpart of the crystalline solid: both are `Substance / Matter` readings of the same composition, separated by the presence or absence of long-range periodicity.

It is **not** the [Liquid](/view.html?p=notes/nature/matter/state/liquid.md): a liquid has no long-range order either, but its constituents diffuse, so it has no shear modulus and it flows. It is **not** the [Solid](/view.html?p=notes/nature/matter/state/solid.md) in general — the generic solid note covers the state, crystalline or not. And it is **not** the [Liquid Crystal](/view.html?p=notes/nature/matter/state/liquid-crystal-lc.md), which has orientational order without positional order: the liquid crystal is *between* the two orders, the glass is *frozen below* both.

### What is this natural instance?

> Window glass, metallic glass, polymer glass, amorphous ice, the silica of a fibre-optic cable, the frozen sugar of a candy. Each is a liquid that stopped moving before it could organise: the cooling rate beat the crystallisation kinetics, and the disorder of the melt was locked in place.

Three quantities decide whether a material becomes a glass: the **cooling rate** relative to the crystallisation kinetics, the **glass transition temperature** $T_g$ at which the relaxation time of the melt becomes comparable to the experimental timescale, and the **fragility** of the liquid — how fast its viscosity falls with temperature above $T_g$. A strong liquid such as silica holds its structure over a wide range; a fragile liquid such as an organic melt loses it quickly, and its properties change sharply at the transition.

The structure is described statistically rather than by a lattice: a **radial distribution function** with peaks that decay with distance instead of Bragg peaks in a diffraction pattern. The absence of periodicity is what makes the amorphous solid *isotropic* — the same in every direction — and it is also why it has no Bragg diffraction, no sharp melting point, and a specific heat that changes at $T_g$ rather than a latent heat.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the disordered solid itself — the composition, the arrest that produced it, the properties that follow from the disorder, and the bound below which the description fails. The crystallisation kinetics belong to the phase-transition reading; the engineering of a particular glass belongs to the materials note.
>
> Stopping rule: a row is terminal when it names a class of glass, a measured property, or a named bound.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the atomic arrangement is **micro**; the bulk sample and its shaping are **meso**.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Amorphous Solid | The disordered solid: a frozen liquid configuration, with short-range order and no lattice. |
| `Substance / Matter` `(→ Kind)` Amorphous Solid `(→ Kind)` Silicate Glass | The canonical glass: network-forming silica, strong liquid, wide working range. |
| `Substance / Matter` `(→ Kind)` Amorphous Solid `(→ Kind)` Metallic Glass | A metal alloy quenched too fast to crystallise: metallic bonding without slip planes, hence high strength and low ductility. |
| `Substance / Matter` `(→ Kind)` Amorphous Solid `(→ Kind)` Polymer Glass | Long chains frozen below $T_g$: the glassy state of every thermoplastic, and the reason a plastic bottle is rigid at room temperature. |
| `Substance / Matter` `(→ Kind)` Amorphous Solid `(→ Kind)` Amorphous Ice | Water arrested in a non-crystalline form — a laboratory and astrophysical rarity, stable only at low temperature. |
| `Substance / Matter` `(→ Kind)` Amorphous Solid `(→ Attribute)` `Property` `(→ Instance)` Glass Transition Temperature | Meso. The temperature at which the relaxation time of the melt reaches the observation timescale; not a melting point, because there is no lattice to melt. |
| `Substance / Matter` `(→ Kind)` Amorphous Solid `(→ Attribute)` `Property` `(→ Instance)` Short-Range Order | Micro. The coordination shell survives; periodicity does not. Measured as a radial distribution function. |
| `Substance / Matter` `(→ Kind)` Amorphous Solid `(→ Attribute)` `Property` `(→ Instance)` Isotropy | Meso. No preferred direction, because no lattice axis — the property that makes glass transparent and metallic glass magnetically soft. |
| `Substance / Matter` `(→ Kind)` Amorphous Solid `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Devitrification | Meso. Above $T_g$ the material relaxes and can crystallise; the glass is stable only while the kinetics, not the thermodynamics, hold it. |

**Limitations.** *Scale* — the description is statistical, so a sample must be large enough for the distribution to be meaningful. *Nonlinearity* — the glass transition is not a single sharp transition, and the relaxation spectrum is broad and non-exponential. *Uncertainty* — whether an ideal glass transition exists at all is unresolved; the observed $T_g$ is rate-dependent. *Partial Observability* — the structure is inferred from scattering and simulation, not read off directly.

## References

- Zachariasen, W. H. (1932). The atomic arrangement in glass. *Journal of the American Chemical Society*, 54(10), 3841–3851. — the random-network model: the first structural account of a glass.
- Anderson, P. W. (1958). Absence of diffusion in certain random lattices. *Physical Review*, 109(5), 1492–1505. — localisation, the quantum counterpart of arrest in a disordered medium.
- Debenedetti, P. G., & Stillinger, F. H. (2001). Supercooled liquids and the glass transition. *Nature*, 410(6825), 259–267. — the modern review of the transition and the open questions.
- Berthier, L., & Biroli, G. (2011). Theoretical perspective on the glass transition and amorphous materials. *Reviews of Modern Physics*, 83(2), 587–645. — the theoretical landscape, from mode-coupling to random first-order.
- Callister, W. D., & Rethwisch, D. G. (2007). *Materials science and engineering: An introduction* (7th ed.). Wiley. — the engineering reading: how the glassy state is used and what limits it.
- [Amorphous solid — Wikipedia](https://en.wikipedia.org/wiki/Amorphous_solid)
- [Solid](/view.html?p=notes/nature/matter/state/solid.md) · [Crystalline Solids](/view.html?p=notes/nature/matter/state/crystalline-solids.md) · [Liquid](/view.html?p=notes/nature/matter/state/liquid.md) · [Liquid Crystal](/view.html?p=notes/nature/matter/state/liquid-crystal-lc.md)
- [State — the States of Matter](/view.html?p=notes/nature/matter/state/readme.md) (the shelf this note belongs to)
