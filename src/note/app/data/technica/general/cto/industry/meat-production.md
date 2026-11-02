---
tags: [meat, food]
---

# Meat Production

> **Meat Production** is the meat-type production system with a carcass-to-cut chain and market structure. Source: Produceologia `docs/Production/Industry/Food/Meat.md` (read-only import; the original is untouched).

## Formulation

### What technical element type does this technical instance belong to?

**Meat Production belongs to the `Production Technical System` technical element type — an organized set of objects realizing meat capability.**

### What is this technical instance?

> Slaughter lines through cutting floors into cold stores across beef, pork, and poultry types with noted US market shares.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one meat system, decomposed at shallow depth — root plus line constituents only.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Production Technical System` → Meat Production | Carcass-to-cut meat system. |
| `Production Technical System` → Meat Production → `Production Technical Object` | Grouping: line objects of the system. |
| `Production Technical System` → Meat Production → `Production Technical Object` → Slaughter Line | Primary processing object. |
| `Production Technical System` → Meat Production → `Production Technical Object` → Cutting Floor | Cut fabrication object. |
| `Production Technical System` → Meat Production → `Production Technical Object` → Cold Store | Refrigerated holding object. |

## References

- Produceologia `docs/Production/Industry/Food/Meat.md`
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
