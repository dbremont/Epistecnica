---
tags: [metals, metallurgy]
---

# Metals Production

> **Metals Production** pairs upstream smelting, refining, and alloying with downstream cutting, forging, and welding. Source: Produceologia `docs/Production/Industry/Metallurgical/README.md` and `docs/Production/Industry/Metal/README.md` (read-only import; the originals are untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Metals Production belongs to the `Production Technical System` technical element type — an organized set of objects realizing metal capability from ore to part.**

### What is this technical instance?

> Smelters and refineries feeding alloy stocks into cut, forge, and weld operations: the upstream–downstream contrast the source draws between metallurgical production and metalworking.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one metals system, decomposed at shallow depth — root plus smelting and shaping constituents only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Metals Production | Ore-to-part metals system. |
| `Production Technical System` → Metals Production → `Production Technical Object` | Grouping: upstream objects of the system. |
| `Production Technical System` → Metals Production → `Production Technical Object` → Smelter Line | Ore-reduction object. |
| `Production Technical System` → Metals Production → `Production Technical Object` → Refinery Train | Purity-raising object. |
| `Production Technical System` → Metals Production → `Technique` | Grouping: downstream operations of the system. |
| `Production Technical System` → Metals Production → `Technique` → Metalworking Operations | Cut, forge, and weld operation family. |

## References

- Produceologia `docs/Production/Industry/Metallurgical/README.md`
- Produceologia `docs/Production/Industry/Metal/README.md`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
