---
tags: [note, nature, substance-matter, geoscience, matter, geological-material]
qa:
 - When does a sediment become a rock?
 - Is sediment defined by what it is made of, or by how it got there?
 - Why does grain size survive transport better than composition?
---

# Sediment

> **Sediment** is unconsolidated particulate material — mineral grains, rock fragments, shell debris, precipitates or organic remains — that has been transported and deposited by water, wind, ice or gravity. It is the loose precursor of sedimentary rock: lithification is the only difference.

> A sediment is read per [How to decompose any natural instance?](/view.html?p=notes/meta/philosophia-naturalis-et-operis.md).

## Formulation

### What natural element type does this sediment instance belong to?

**Sediment belongs to `Ontic Element (→ Kind) Substance` — a material body, not a process and not a system.** It is an aggregate of grains held by contact rather than by chemical bonding, but it is a substance in the guide's sense: it occupies space, has composition and structure, and persists as the same body through transport.

Readable secondarily as a `Phenomenon` when the emphasis falls on *deposition* rather than on the material deposited — a sediment body is also the record of the flow that laid it down. Readable again as a `Process` in the compound *sedimentation*. Those readings are prose here and are not separate roots.

The choice matters because the neighbouring rows are easy to confuse. A sediment is not a `Rock`: the two differ only by lithification, so typing sediment as rock would erase the stage distinction the table is built on. It is not a `Mineral` either, since a sediment is defined by its grain population, not by a single lattice.

### What is this natural instance?

> A sediment is characterised by four things, and the first is not its composition. **Grain size** decides what the material is called — gravel, sand, silt, clay — and it is the most durable property a grain has: a feldspar grain can weather to clay but a sand grain stays sand-sized through most transport. **Sorting** records how uniform the grain sizes are, and therefore how selective the transporting agent was. **Roundness** records how far the grain travelled and how hard it was abraded. **Provenance** records where it came from, and survives in the heavy-mineral fraction long after the softer minerals have been destroyed.
>
> Those four are what make sediment readable as history. The composition tells you the source rock; the texture tells you the journey; the structure of the deposit — cross-bedding, grading, imbrication — tells you the direction and energy of the flow that delivered it. A deposit is a physical record of a flow that no longer exists.
>
> The boundary case is lithification. Compaction squeezes water out, cementation precipitates a mineral between the grains, and the loose aggregate becomes a coherent rock. Nothing about the grains themselves has to change: the same sand becomes sandstone. This is why sediment and rock sit side by side in the geological table rather than in separate branches — the row names a stage, and the stage is the whole difference.

### What is the recursive instance decomposition of this sediment instance?

> Boundary: the sediment body as a population of grains plus the pore space and fluid between them. The transporting flow, the depositional basin and the later diagenesis are associated processes, not parts of the instance.
>
> Stopping rule: a row is terminal when it names a measurable attribute, a grain-size class, a transport agent or a constituent whose own decomposition lives elsewhere.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: an individual grain and its surface texture are **micro**; a sediment body and its bedding are **meso**; a sedimentary basin fill is **macro**. Limitation checklist for the segment: **Scale** (the same deposit is micro to one observer and macro to another), **Non-Repeatability** (a deposit records one flow that cannot recur identically), **Partial Observability** (the transporting flow is gone; only its deposit remains), **Uncertainty** (provenance is an inference from a surviving mineral fraction).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment | Bound root instance: unconsolidated particulate material at the stage before lithification. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Part)` Grain Population | Grouping: the solid particles the sediment is made of. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Part)` Grain Population `(→ Instance)` Clast Set | Fragments of pre-existing rock, the dominant constituent of clastic sediment. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Part)` Grain Population `(→ Instance)` Bioclast Set | Skeletal and shell debris produced by organisms. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Part)` Grain Population `(→ Instance)` Precipitate Set | Grains formed by chemical precipitation rather than by fragmentation — ooids, evaporite crystals. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Part)` Matrix | The finer-grained material filling the space between the larger grains. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Part)` Pore Space and Fluid | The void between grains and the water, air or hydrocarbon it holds. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Attribute)` Grain Size Class | Grouping: the size band that names the sediment. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Attribute)` Grain Size Class `(→ Kind)` Gravel | Clasts above 2 mm; the coarsest class that is still transported as grains. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Attribute)` Grain Size Class `(→ Kind)` Sand | Clasts from 0.0625 mm to 2 mm; the class that survives transport best. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Attribute)` Grain Size Class `(→ Kind)` Silt | Clasts from 0.004 mm to 0.0625 mm; cohesive once deposited, easily carried in suspension. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Attribute)` Grain Size Class `(→ Kind)` Clay | Clasts below 0.004 mm; chemically active, and the class whose minerals weather fastest. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Attribute)` Sorting | How narrow the grain-size distribution is, and therefore how selective the transport was. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Attribute)` Roundness | The degree of abrasion of grain edges, recording distance and energy of transport. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Attribute)` Provenance | The source rock the grains were derived from, inferred from the surviving mineral assemblage. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Kind)` Transport Agent | Grouping: what carried the grains, which fixes the deposit's texture and geometry. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Kind)` Transport Agent `(→ Instance)` Fluvial Sediment | Deposited by flowing water in channels and on floodplains; alluvium. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Kind)` Transport Agent `(→ Instance)` Colluvial Sediment | Deposited by gravity on slopes; angular and poorly sorted. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Kind)` Transport Agent `(→ Instance)` Aeolian Sediment | Deposited by wind; well sorted and well rounded, as in loess and dune sand. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Kind)` Transport Agent `(→ Instance)` Glacial Sediment | Deposited by ice; unsorted, unrounded, and made of rock flour as well as clasts. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Kind)` Transport Agent `(→ Instance)` Marine Sediment | Settled through water in a sea or lake, by suspension or by gravity flows. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Instance)` Sediment `(→ Bound)` Lithification | The transition that ends the instance: compaction and cementation turn the sediment into sedimentary rock. |

## References

- [Sediment](https://en.wikipedia.org/wiki/Sediment)
- [Sedimentary rock](https://en.wikipedia.org/wiki/Sedimentary_rock)
- [Sorting (sedimentology)](https://en.wikipedia.org/wiki/Sorting_(sedimentology))
- [Roundness (geology)](https://en.wikipedia.org/wiki/Roundness_(geology))
- [Provenance (geology)](https://en.wikipedia.org/wiki/Provenance_(geology))
- [How to decompose any natural instance?](/view.html?p=notes/meta/philosophia-naturalis-et-operis.md) (Tabular and Recursive views, Limitation checklist, level gate)
- [Philosophia Naturalis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-naturalis-et-operis.md) (schema and table contract)
