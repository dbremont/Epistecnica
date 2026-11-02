---
tags: [chemicals]
---

# Basic Chemicals Production

> **Basic Chemicals Production** is the basic-chemicals taxonomy in production with R&D-intensity differentiation. Source: Produceologia `docs/Production/Industry/Chemical/README.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Basic Chemicals Production belongs to the `Production Technical System` technical element type — an organized set of objects realizing chemical-feedstock capability.**

### What is this technical instance?

> Crackers, reactor trains, and distillation columns converting feedstocks into basic chemicals at varying R&D intensities.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one chemicals system, decomposed at shallow depth — root plus cracker, reactor, and column constituents only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Basic Chemicals Production | Feedstock-to-chemicals system. |
| `Production Technical System` → Basic Chemicals Production → `Production Technical Object` | Grouping: unit objects of the system. |
| `Production Technical System` → Basic Chemicals Production → `Production Technical Object` → Cracker Unit | Hydrocarbon-breaking object. |
| `Production Technical System` → Basic Chemicals Production → `Production Technical Object` → Reactor Train | Synthesis object. |
| `Production Technical System` → Basic Chemicals Production → `Production Technical Object` → Distillation Column | Separation object. |

## References

- Produceologia `docs/Production/Industry/Chemical/README.md`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
