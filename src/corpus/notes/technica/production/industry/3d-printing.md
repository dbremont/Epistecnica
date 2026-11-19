---
tags: [note, production, manufacturing, additive-manufacturing]
---

# 3D Printing

> **3D printing**, or **additive manufacturing**, builds a part layer by layer from a digital model instead of removing material from a block. The technique's importance is not that it makes the same parts a different way, but that it makes **different parts economic**: geometry that no mould or cutter can produce, one-offs that need no tooling, and assemblies consolidated into single pieces.

## The process family

| Process | How it builds | Materials | Typical tolerance |
| --- | --- | --- | --- |
| **Material extrusion** (FDM/FFF) | A thermoplastic filament is laid down through a heated nozzle | PLA, ABS, PETG, PEEK, filled polymers | Rough; layer lines visible |
| **Vat photopolymerisation** (SLA/DLP) | A resin is cured layer by layer by light | Photopolymers, some ceramics after sintering | Fine surface, brittle parts |
| **Powder bed fusion** (SLS polymer, SLM/DMLS metal) | A laser or electron beam fuses powder layer by layer | Nylon, titanium, aluminium, steel, superalloys | Good; supports not needed but powder handling is |
| **Binder jetting** | A binder is printed into powder, then sintered | Sand (casting moulds), metals, ceramics | Medium; shrinkage in sintering |
| **Directed energy deposition** | Metal powder or wire is deposited and melted as the head moves | Metals, repair of existing parts | Coarse but large and repairable |

## What the technique buys

> **No tooling.** The first part costs nearly as much as the thousandth, which inverts the economics of conventional manufacturing: 3D printing is competitive exactly where volumes are low, designs iterate, or the part is bespoke (implants, dental, tooling, prototypes). **Geometry that could not exist otherwise**: internal lattices, conformal cooling channels in injection moulds, hollow topologies, and parts consolidating what used to be an assembly of twenty.

## What it costs

> Three limits decide where it is used. **Surface finish and anisotropy** — an extruded or powder-fused part is weaker across the layers, so the build orientation is part of the design. **Per-part cost that does not fall** with volume, which is why additive has not replaced casting or stamping for mass production. **Qualification** — in aerospace and medical work, the material and process must be certified, and a process with thousands of parameters is expensive to qualify. The result is the honest summary: additive manufacturing is a **prototyping and low-volume production technique that has moved into serial production only where geometry, weight or consolidation justify it** — brackets, fuel nozzles, implants, and spare parts for long-lived equipment.

## Process chain

> Model → orientation and support strategy → slicing → build → post-processing (support removal, curing, sintering, heat treatment, machining of critical surfaces) → inspection. The **post-processing** is where most of the cost and variability sit, which is the part the marketing photograph omits.

## References

- [3D printing — Wikipedia](https://en.wikipedia.org/wiki/3D_printing)
- [CNC Machining](/view.html?p=notes/technica/production/industry/cnc-machining.md) — the subtractive counterpart
- [Additive Manufacturing — Wikipedia](https://en.wikipedia.org/wiki/Additive_manufacturing)
- [Metrology](/view.html?p=notes/technica/general/metrology.md) — how the printed part is checked
