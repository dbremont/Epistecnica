---
tags: [note, nature, substance-matter, geoscience, matter, geological-material]
qa:
 - Is ore a natural kind or an economic category?
 - What happens to an ore body when the metal price falls?
 - Is a low-grade deposit that cannot be mined still an ore?
 - Does the boundary between ore and waste lie in the rock or in the market?
---

# Ore

> **Ore** is rock or sediment that contains a mineral — or a metal within a mineral — at a concentration high enough to be recovered at a profit. It is the one material category individuated by **price** rather than by nature: the substance is unchanged when the market moves, only its classification changes.

> An ore is read per [How to decompose any natural instance?](/view.html?p=notes/meta/philosophia-naturalis-et-operis.md).

## Formulation

### What natural element type does this ore instance belong to?

**Ore belongs to `Ontic Element (→ Kind) Substance` — a material body, and specifically one individuated by its recoverable content rather than by its own composition.** It is a host rock or sediment plus a concentration, and the concentration is defined relative to a process and a price.

Readable secondarily as an `Aspect` of the host rock — the rock considered under the dimension *what can be taken from it*. That reading is worth naming because it explains the strangest thing about ore: nothing in the rock changes when it stops being ore, so the category cannot be a property of the rock alone. Readable again as `readable as technique` — ore is a term of the extraction practice, and the same material is ore or overburden according to the technology brought to it. Neither reading is a second root.

The choice matters. Ore is not a `Mineral`: a mineral is a lattice, whereas an ore is a rock or sediment that *contains* minerals of which only some are valuable. It is not a `Rock`: a rock is individuated by genesis and remains that rock regardless of grade. Ore cuts across both.

### What is this natural instance?

> Three quantities decide whether a body of rock is ore, and only the first is geological. **Grade** is the concentration of the valuable element in the host — grams per tonne for gold, percent for copper, parts per million for rare earths. **Recovery** is the fraction of that content the available process can actually extract, which depends on the mineral hosting the metal: gold in free grains is recovered almost entirely, gold locked in refractory sulfides may lose most of itself to the tailings. **Cost** is what the extraction consumes in energy, reagents, water, labour and capital.
>
> The **cut-off grade** is the concentration at which recovery value equals cost. Everything follows from it. Raise the metal price and the cut-off falls, so rock that was waste becomes ore and a deposit grows without a single gram being added. Improve the process and the same thing happens; exhaust the easy part of the deposit and the cut-off rises, and ore becomes waste. This is why reserves are reported as a function of price and technology rather than as a fixed quantity — a reserve statement dated and priced is a statement about a market as much as about a rock.
>
> That relational character is the whole reason the note exists. The geological table lists ore beside mineral, rock and sediment, but ore is the only row whose boundary moves without the material moving. Calling it a geological matter type is a convenience of filing. What the rock has is a **grade**; what the category adds is a **calculation**.

### What is the recursive instance decomposition of this ore instance?

> Boundary: the ore body as host material plus the mineral assemblage it carries, with grade, recovery and cut-off as its decisive attributes. The mining operation, the processing plant and the market are associated systems, not parts of the instance — though the cut-off is defined by them.
>
> Stopping rule: a row is terminal when it names a constituent mineral, a deposit class, a measured attribute or a named economic condition whose own decomposition lives elsewhere.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the ore mineral and its locking texture are **micro**; the ore body and its grade distribution are **meso**; the metallogenic province is **macro**. Limitation checklist for the segment: **Uncertainty** (grade is estimated from sparse assay samples), **Partial Observability** (the deposit is known only where it has been drilled), **Non-Repeatability** (a deposit is mined once), **Scale** (grade is defined over a volume whose size changes the number), **Measurement Disturbance** (sampling and assaying perturb and select the material they measure).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore | Bound root instance: host material carrying a recoverable concentration. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Host Material | Grouping: the geological body that carries the ore minerals. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Host Material `(→ Instance)` Host Rock | A rock body, individuated by its genesis as any rock is — igneous, sedimentary or metamorphic. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Host Material `(→ Instance)` Host Sediment | An unconsolidated body — a placer, a heavy-mineral sand — where the valuable grains are already free. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Ore Mineral Set | Grouping: the minerals that carry the value. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Ore Mineral Set `(→ Instance)` Oxide Ore Mineral | Oxides and hydroxides — hematite, magnetite, rutile, cassiterite, uraninite. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Ore Mineral Set `(→ Instance)` Sulfide Ore Mineral | Sulfides — chalcopyrite, galena, sphalerite, pentlandite; the refractory hosts that most often defeat recovery. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Ore Mineral Set `(→ Instance)` Native Metal | The metal uncombined — gold, silver, copper, platinum-group metals; the easiest to recover and the rarest. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Ore Mineral Set `(→ Instance)` Carbonate and Silicate Ore Mineral | Malachite, cerussite, garnierite, spodumene — gangue-like hosts that carry the metal in their structure. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Part)` Gangue | The valueless minerals accompanying the ore minerals, which the process must separate and discard. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Attribute)` Grade | The concentration of the valuable element in the host, in g/t, percent or ppm. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Attribute)` Recovery | The fraction of the contained metal the available process can extract, fixed by the locking and mineralogy. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Attribute)` Cut-off Grade | The concentration below which recovery value no longer covers cost; the boundary that makes ore ore. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Attribute)` Reserves and Resources | The tonnage and grade reported under a stated price and process — a dated, priced statement, not a fixed quantity. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Kind)` Deposit Class | Grouping: the geological process that concentrated the metal. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Kind)` Deposit Class `(→ Instance)` Magmatic Deposit | Concentration by crystal settling or immiscible sulfide liquid separating from magma. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Kind)` Deposit Class `(→ Instance)` Hydrothermal Deposit | Concentration by hot fluids dissolving, transporting and precipitating metals in fractures. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Kind)` Deposit Class `(→ Instance)` Placer Deposit | Concentration by water or wind sorting dense, resistant grains out of a weathering rock. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Kind)` Deposit Class `(→ Instance)` Residual Deposit | Concentration by weathering removing everything soluble and leaving the metal behind. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Kind)` Deposit Class `(→ Instance)` Sedimentary Deposit | Concentration by chemical or biological precipitation — banded iron formation, phosphorite, evaporite. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Ore `(→ Bound)` Economic Condition | The market and technological state that fixes the cut-off; the bound of the instance rather than a part of it. |

## References

- [Ore](https://en.wikipedia.org/wiki/Ore)
- [Ore genesis](https://en.wikipedia.org/wiki/Ore_genesis)
- [Gangue](https://en.wikipedia.org/wiki/Gangue)
- [Cut-off grade](https://en.wikipedia.org/wiki/Cut-off_grade)
- [Mineral resource classification](https://en.wikipedia.org/wiki/Mineral_resource_classification)
- [How to decompose any natural instance?](/view.html?p=notes/meta/philosophia-naturalis-et-operis.md) (Tabular and Recursive views, Limitation checklist, level gate)
- [Philosophia Naturalis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-naturalis-et-operis.md) (schema and table contract)
