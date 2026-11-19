---
tags: [note, nature, energy, bioenergy, biomass, matter]
qa:
 - Is bioenergy a kind of energy, a kind of fuel, or a relation between the two?
 - Photosynthesis stores a small fraction of the sunlight it receives. What happens to the rest, and what does that say about the scale of bioenergy?
 - Why is a fuel molecule better described as an energy carrier than as an energy?
---

# Bioenergy

> **Bioenergy** is the chemical energy stored in biological molecules: the energy fixed by photosynthesis and held in biomass, in the bonds of carbohydrates, lipids and other organic matter, released when a suitable mechanism — combustion, digestion, fermentation, gasification, pyrolysis or biological respiration — breaks those bonds and converts the stored potential into work, heat or another energy form.

> The distinction that organises the note is between the **quantity** and the **carrier**. Energy is the quantity; a **fuel molecule is an energy carrier** — it contains chemical potential in a form that a reaction mechanism can release. The same quantity can be carried by wood, by methane, by ethanol or by a sugar, and the carrier decides how the release happens, at what temperature, with what losses and with what useful output.

## Formulation

### What natural element type does this bioenergy instance belong to?

**Bioenergy belongs to `Ontic Element (→ Kind) Property (→ Kind) Interaction-Derived Quantity` — it is a quantity of a system, not a substance and not a mechanism.**

It is interaction-derived because it is not a thing the biomass contains like a part; it is the potential of a configuration of atoms and bonds, defined relative to the reactions that can release it. The same kilogram of wood has one chemical energy, a different useful energy when burned in a stove and a different one again when digested, because the quantity is a property of the material *and* of the conversion path.

Readable secondarily as an `Aspect` — biomass considered under the dimension *what energy can it yield* — and as a `Natural Process` when the release is read as the process rather than the quantity. Those readings are prose here, not second roots.

The boundary against **fossil fuel** is geological age: both are photosynthetic energy stored in organic matter, and the difference is whether the carbon was fixed recently or millions of years ago. The boundary against **food** is the use: the same molecule is food when eaten and fuel when burned.

### What is this natural instance?

> The organic matter of the biosphere read as an energy store: wood and crop residues, energy crops, animal and municipal organic waste, the sugars and starches that ferment to ethanol, the lipids that become biodiesel, and the methane produced when organic matter decays without oxygen. Its quantity is fixed by the feedstock's composition — the calorific value, the moisture, the ash, the carbon-to-oxygen ratio — and its usefulness by the conversion route available.

### What is the recursive instance decomposition of this bioenergy instance?

> Boundary: the quantity and the material forms that carry it, with the attributes that determine how much is released and the mechanisms that release it. The ecosystems that produce the biomass and the industries that convert it are associated systems, not parts of the instance.
>
> Stopping rule: a row is terminal when it names a carrier form, a measured attribute, a conversion mechanism or a named bound.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the bond and the molecule are **micro**; the feedstock and the biomass stock are **meso**; the biosphere's net primary production and the bioenergy industry are **macro**. Limitation checklist for the segment: **Uncertainty** (calorific value varies with moisture, composition and species), **Scale** (the energy is defined per unit mass, per hectare or per year, and the numbers change with the unit), **Measurement Disturbance** (drying and sampling change the value being measured), **Complexity** (the feedstock, the conversion path and the end use are three different systems).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy | Bound root instance: the chemical energy stored in biological molecules. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Kind)` Carrier Form | Grouping: the material forms that carry the quantity. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Kind)` Carrier Form `(→ Instance)` Woody and Agricultural Biomass | Wood, straw, husks and crop residues — the solid feedstock burned or gasified. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Kind)` Carrier Form `(→ Instance)` Energy Crops | Plants grown for their energy content — grasses, short-rotation coppice, sugar and oil crops. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Kind)` Carrier Form `(→ Instance)` Biogas | Methane and carbon dioxide from anaerobic digestion or landfill — a gaseous carrier. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Kind)` Carrier Form `(→ Instance)` Liquid Biofuel | Ethanol from fermentation, biodiesel from transesterification — the transport carriers. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Kind)` Carrier Form `(→ Instance)` Organic Waste and Residue | Manure, food waste, sewage sludge — the carrier with a disposal problem attached. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Attribute)` Energy Content | Calorific value per unit mass — higher and lower heating value, dry basis or as received. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Attribute)` Moisture Content | Water in the feedstock: it lowers the useful energy and must be evaporated first. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Attribute)` Carbon-to-Oxygen Ratio | The oxidation state of the carbon — the reason wood burns and methane ignites. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Attribute)` Ash and Contaminant Content | The mineral residue and the elements that limit combustion or digestion. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Component)` `Mechanism` | Grouping: the mechanisms that release the stored energy. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Component)` `Mechanism` `(→ Instance)` Combustion | The carbon is oxidised to CO₂ and the bond energy leaves as heat. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Component)` `Mechanism` `(→ Instance)` Anaerobic Digestion | Microbes convert organic matter to methane and CO₂ without oxygen. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Component)` `Mechanism` `(→ Instance)` Fermentation | Microbes convert sugars to ethanol, releasing the rest as heat and CO₂. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Component)` `Mechanism` `(→ Instance)` Gasification and Pyrolysis | Heat converts the feedstock to a combustible gas, oil or char without full oxidation. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Component)` `Mechanism` `(→ Instance)` Cellular Respiration | The biological release: the same oxidation, at body temperature, through enzymes. |
| `Ontic Element` `(→ Kind)` `Property` `(→ Kind)` `Interaction-Derived Quantity` `(→ Instance)` Bioenergy `(→ Bound)` `Environment` | The feedstock supply, the conversion technology and the competing land and water use that bound what the quantity can deliver. |

## Forms

| Carrier | What it is | Typical conversion | Character |
| --- | --- | --- | --- |
| **Wood and residues** | Solid lignocellulosic matter | Combustion, gasification, pyrolysis | The oldest fuel; low moisture and high density are the quality |
| **Energy crops** | Plants grown for energy | Combustion, fermentation, transesterification | Competes with food and nature for land |
| **Biogas** | Methane-rich gas from digestion | Combustion in an engine or boiler, upgrading to biomethane | Wet feedstocks; the digester is the conversion plant |
| **Ethanol** | Fermented sugar or starch | Blend with petrol | The sugar and starch fraction only; lignin is left behind |
| **Biodiesel** | Transesterified vegetable oil or fat | Blend with diesel | Oil crops and waste fats; glycerol is the by-product |
| **Organic waste** | Manure, food waste, sludge | Digestion, combustion | The carrier that is also a waste-management problem |

## Release Mechanisms

| Mechanism | Oxygen | Temperature | What leaves | What is captured |
| --- | --- | --- | --- | --- |
| **Combustion** | Excess | High | Heat, CO₂, water, ash | Heat for power or process |
| **Gasification** | Limited | High | Combustible gas (CO, H₂, CH₄) | A gas that can be burned or synthesised |
| **Pyrolysis** | None | Moderate–high | Gas, bio-oil, char | A liquid or solid carrier |
| **Anaerobic digestion** | None | Ambient–mesophilic | Methane, CO₂, digestate | A gas and a fertiliser |
| **Fermentation** | None | Ambient | Ethanol, CO₂ | A liquid fuel |
| **Respiration** | Yes | Ambient, enzymatic | CO₂, water, ATP | The cell's usable energy |

## The Conversion Chain

> Photosynthesis fixes a small fraction of the incident sunlight — the theoretical maximum is around 4.6 % for C3 plants and somewhat higher for C4, and the realised field efficiency is lower still. Everything downstream is a conversion of that already-small store, and each step loses more:

$$\text{sunlight} \;\to\; \text{biomass} \;\to\; \text{carrier} \;\to\; \text{useful energy}.$$

> The chain explains the two facts that dominate the subject. **The area is large**: because the photosynthetic efficiency is low, a meaningful amount of bioenergy needs a meaningful amount of land — which is why the food-versus-fuel and land-use debates are not political decoration but arithmetic. **The carrier matters**: wood burned in a stove delivers a different fraction of its chemical energy than the same wood gasified, and wet waste that cannot be burned economically can still be digested. The quantity is natural; the delivered energy is a property of the conversion path.

> The carbon accounting is a second chain. The carbon released when bioenergy is used was fixed recently, so the net emission depends on the regrowth, the land-use change, the fertiliser and the transport — which is why "carbon neutral" is a claim about a whole cycle, not about the fuel.

## References

- [Bioenergy](https://en.wikipedia.org/wiki/Bioenergy)
- [Biomass (energy)](https://en.wikipedia.org/wiki/Biomass_(energy)) · [Biofuel](https://en.wikipedia.org/wiki/Biofuel) · [Biogas](https://en.wikipedia.org/wiki/Biogas)
- [Energy carrier](/view.html?p=notes/nature/energy-carrier.md) — the concept the carrier forms instantiate
- [Type of Energy](/view.html?p=notes/nature/property/energy.md) — the family of energy quantities
- [Energy Transformation](/view.html?p=notes/nature/energy-transformation.md) — the general conversion logic
- [Chemical Processes](/view.html?p=notes/nature/chemical-processes.md) — the reactions the mechanisms run
- [Energy](/view.html?p=notes/technica/general/energy.md) — the technical conversion systems, with the biomass and bioenergy row
- [Biogas](/view.html?p=notes/technica/general/materiotecnia/biogas.md) — the material note on the gaseous carrier
- [How to decompose any natural instance?](/view.html?p=notes/philosophia-naturalis-et-operis.md) — the tabular and recursive views, the level gate and the Limitation checklist
- [Philosophia Naturalis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-naturalis-et-operis.md) — the schema and the table contract
