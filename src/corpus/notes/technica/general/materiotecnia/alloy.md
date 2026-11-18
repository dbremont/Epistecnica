---
tags: [note, production, materials-science, metallurgy]
---

# Alloy

> An **alloy** is a homogeneous mixture of two or more elements, at least one of which is a metal, whose composition is chosen to give properties the pure metal does not have. The second element is there for a reason: to raise strength, to hold hardness at temperature, to resist corrosion, to lower melting point, or to make the material castable, weldable or machinable.

> The concept is a technical one, not a natural one. No ore yields an alloy; a metallurgist fixes a composition and a treatment to obtain a property, and the phase diagram says which compositions and temperatures can deliver it. That is why alloys are filed with the materials the plant produces, beside the techniques that make them — never among the natural elements.

## Formulation

### What technical element type does this technical instance belong to?

**Alloy belongs to the `Constitutive Technical Object` technical element type — a stuff-kind that constitutes larger objects and systems.**

It is a constitutive object because it does not act: it is the material a component is made of, and its properties are the constraints the designer works inside. It is read beside [Steel](/view.html?p=notes/technica/production/industry/steel.md), which is the dominant alloy family and carries the composition, microstructure and grade tables; this note owns the concept that Steel is one case of.

### What is this technical instance?

> Substitutional solid solutions such as brass and bronze; interstitial solutions such as carbon steel; precipitation-hardened systems such as the nickel superalloys and the aluminium 2xxx and 7xxx series; ordered intermetallics such as the titanium aluminides; and the special classes — shape-memory alloys, high-entropy alloys, metallic glasses and solder — each fixed by a composition, a phase diagram and a heat treatment.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one alloy concept, decomposed at shallow depth — the families and the exemplar systems that show what an alloy is for. The full grade tables of steel belong to the steel note.
>
> Stopping rule: a row is terminal when it names a concrete alloy family or a named commercial system.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a phase diagram *bounds* the composition; a heat treatment *fixes* the microstructure; the alloy *constitutes* the component.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technical Object` → Alloy | A metal-based material whose composition and treatment are chosen for a property. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` | Grouping: the alloy families. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` → Steel | The iron–carbon family: the largest alloy family, decomposed in its own note. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` → Brass and Bronze | Copper alloyed with zinc or tin: the classical substitutional alloys. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` → Solder | Low-melting tin, lead, silver or copper alloys joining metals by wetting. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` → Nickel Superalloy | Nickel with chromium, cobalt, aluminium and titanium, holding strength at turbine temperatures. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` → Titanium Alloy | Titanium with aluminium and vanadium, trading density for strength and corrosion resistance. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` → Aluminium Alloy | Aluminium with copper, magnesium, zinc or silicon, hardened by precipitation or by work. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` → Shape-Memory Alloy | Nickel–titanium and copper-based alloys that recover a trained shape on a phase change. |
| `Constitutive Technical Object` → Alloy → `Constitutive Technical Object` → High-Entropy Alloy | Several principal elements in near-equal proportion, stabilising a simple solid solution. |

### What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Alloy**, defined above as *a metal-based material whose composition and treatment are chosen to give properties the pure metal does not have*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: the alloy is separated from the pure element, from the compound (a definite stoichiometry, not a composition range) and from the composite (a mixture of phases at a larger scale). Definitional Clarity — **pass**: metal base, alloying element, homogeneous mixture and property purpose are all operational, and the phase diagram supplies the boundary. Conceptual Determinacy — **pass with qualification**: the line against an intermetallic compound and against a heavily doped or micro-alloyed metal is set by convention and by the phase diagram, not by a sharp natural discontinuity; the note states the rule rather than pretending the boundary is given. Internal Consistency — **pass**: the families are kinds of alloy, and steel is one family rather than a competing root. Representational Adequacy — **qualified**: complete for the material families and the property trade; processing routes, standards and the economics of alloying are linked rather than grown. Purpose Adequacy — **pass**: shaped for material selection — every leaf is a family, a mechanism or a property the designer trades.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from the pure element, the intermetallic compound and the composite; typed as a constitutive object, not a producer. |
| Definitional Clarity | pass | Metal base, alloying element, homogeneity and property purpose are operational; the phase diagram fixes the admissible compositions. |
| Conceptual Determinacy | pass (qualified) | The compound and micro-alloy boundaries are conventions on a continuous composition range; stated, not assumed. |
| Internal Consistency | pass | All families are kinds of alloy; steel is a family with its own note, not a second root. |
| Representational Adequacy | qualified | Complete for families and properties; processing, standards and cost are links. |
| Purpose Adequacy | pass | Every leaf serves material selection or the property trade the selection makes. |

## Alloy Families

| Family | Mechanism | What the second element buys | Examples |
| --- | --- | --- | --- |
| **Substitutional solid solution** | Solute atoms replace solvent atoms in the lattice | Strength by lattice distortion, and colour or corrosion behaviour | Brass (Cu–Zn), bronze (Cu–Sn), sterling silver |
| **Interstitial solid solution** | Small atoms sit in the lattice gaps | Strength and hardness at the cost of ductility | Carbon in iron; nitrogen in steel |
| **Precipitation-hardened** | A second phase precipitates from a supersaturated solid solution on ageing | High strength retained to temperature | Al–Cu (2xxx), Al–Zn (7xxx), nickel superalloys |
| **Ordered intermetallic** | Solute and solvent form an ordered lattice | Strength and creep resistance at high temperature, with low ductility | TiAl, NiAl, iron aluminides |
| **Shape-memory** | A martensitic transformation is reversible with temperature or stress | Large recoverable strain, actuation and superelasticity | Nitinol (Ni–Ti), Cu–Zn–Al |
| **High-entropy** | Several principal elements share one lattice | A simple phase with slow diffusion and good irradiation resistance | CoCrFeMnNi (Cantor), refractory HEA families |
| **Metallic glass** | The melt is cooled too fast to crystallise | Very high strength and elastic limit, no grain boundaries | Zr-based and Fe-based bulk metallic glasses |

## What the Alloying Buys

| Property | Mechanism | Design consequence |
| --- | --- | --- |
| **Strength** | Solid-solution distortion, precipitates, grain boundaries and work hardening block dislocation motion | The section can be thinner, the component lighter, the service stress higher. |
| **Hardness and wear** | Carbides, nitrides or intermetallics resist abrasion | Cutting tools, dies and wear plates take the load without reforming. |
| **Corrosion resistance** | A passive chromium, aluminium or silicon oxide layer, or a noble composition | Service in water, salt, acid or high temperature without a coating. |
| **Creep resistance** | Precipitates and grain-boundary control slow diffusion at temperature | Turbine blades and furnace parts hold shape under load for years. |
| **Melting-point control** | Eutectic compositions lower the melting point | Solders, fusible links and casting alloys. |
| **Castability and weldability** | Composition and freezing range fix fluidity and cracking | Complex shapes can be cast or joined without defects. |
| **Magnetic response** | Composition and phase fix permeability, coercivity and saturation | Soft magnetic cores, permanent magnets, shielding. |

## Why an Alloy and Not the Pure Metal

> Pure metals are soft, oxidise readily and lose strength at modest temperature, because there is nothing in the lattice to obstruct dislocation motion and no second phase to carry load. The alloy exists because a small addition changes the lattice, the phase or the surface — and because the same addition can be withdrawn or balanced when it costs ductility, conductivity or corrosion resistance. Every alloy is therefore a trade stated in the phase diagram: the composition that maximises one property is usually the composition that sacrifices another, and the design is the selection of where on that trade the component must live.

## References

- https://en.wikipedia.org/wiki/Alloy
- https://en.wikipedia.org/wiki/Solid_solution
- https://en.wikipedia.org/wiki/Precipitation_hardening
- https://en.wikipedia.org/wiki/Shape-memory_alloy
- https://en.wikipedia.org/wiki/High-entropy_alloy
- [Steel](/view.html?p=notes/technica/production/industry/steel.md) — the dominant alloy family, with the grade tables
- [Heat Treatment](/view.html?p=notes/technica/general/materiotecnia/heat-treatment.md) — the cycles that turn a composition into a property
- [Welding](/view.html?p=notes/technica/general/welding.md) — joining the families, and the weldability that limits it
- [Materiotecnia](/view.html?p=notes/technica/general/materiotecnia/readme.md) — the materials shelf this note belongs to
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
- https://alloy.phys.cmu.edu/
