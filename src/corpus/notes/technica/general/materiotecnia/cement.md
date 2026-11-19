---
tags: [note, production, materials-science, cement, binder]
---

# Cement

> **Cement** is a finely ground inorganic powder that, mixed with water, sets and hardens into a solid mass by chemical reaction — and does so under water as well as in air. That last clause is the whole difference: a non-hydraulic binder needs air to carbonate, a hydraulic one needs only water, which is why the hydraulic binder is the material a harbour wall, a tunnel lining and a foundation can be poured from.

> The concept is a technical one, not a natural one. No deposit yields cement: limestone and clay are quarried, proportioned, burned to clinker at about 1,450 °C, cooled and ground with a set regulator, and the powder that results is a designed intermediate — not a rock. Cement is therefore filed as a material the plant produces, beside the kilns and the techniques that make it.

## Formulation

### What technical element type does this technical instance belong to?

**Cement belongs to the `Constitutive Technical Object` technical element type — a stuff-kind that constitutes larger objects and systems.**

It is a constitutive object because it does not act: it is the material a paste, a mortar, a grout or a concrete is made of, and its setting behaviour is a constraint the builder works inside. Read beside [Ceramic](/view.html?p=notes/technica/general/materiotecnia/ceramic.md), the adjacent inorganic class: ceramics are consolidated by firing a formed body, cements are consolidated by hydrating a ground powder at ambient temperature.

### What is this technical instance?

> A hydraulic binder in powdered form: ordinary Portland cement (clinker plus a few per cent of gypsum); the blended cements that dilute clinker with granulated slag, fly ash, natural pozzolana, limestone or calcined clay; the calcium aluminate cements that harden fast and serve in refractories; the oil-well cements retarded for well completion; and the alkali-activated geopolymer binders that contain no Portland clinker at all.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one material concept, decomposed at shallow depth — the cement kinds, the clinker they are made from and the phases that do the setting. The mix design that turns cement into concrete belongs to the concrete note; the kiln belongs to nonmetallic production.
>
> Stopping rule: a row is terminal when it names a concrete cement family or a named clinker phase.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: the kiln *burns* the raw meal; water *hydrates* the clinker phases; the paste *sets* and then *hardens*.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technical Object` → Cement | A ground inorganic powder that sets and hardens by reaction with water. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` | Grouping: the cement kinds. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Portland Cement | Clinker ground with gypsum: the reference family, CEM I. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Blended Cement | Clinker diluted with slag, fly ash, pozzolana, limestone or calcined clay, CEM II–V. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Calcium Aluminate Cement | Aluminous clinker for rapid hardening and refractory service. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Geopolymer Cement | Alkali-activated aluminosilicate binder, made without Portland clinker. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Oil-Well Cement | Retarded, sulfate-resisting cement for well completion. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Clinker | The burned intermediate the kiln delivers, before grinding. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Gypsum | The set regulator ground in at a few per cent. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Clinker → `Constitutive Technical Object` | Grouping: the clinker phases. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Clinker → `Constitutive Technical Object` → Alite | Tricalcium silicate, the phase that gives early strength. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Clinker → `Constitutive Technical Object` → Belite | Dicalcium silicate, the phase that gives late strength. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Clinker → `Constitutive Technical Object` → Tricalcium Aluminate | The flux phase that sets fast, and the reason gypsum is added. |
| `Constitutive Technical Object` → Cement → `Constitutive Technical Object` → Clinker → `Constitutive Technical Object` → Tetracalcium Aluminoferrite | The iron-bearing phase, which darkens the clinker. |

### What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Cement**, defined above as *a finely ground inorganic powder that sets and hardens by chemical reaction with water, under water as well as in air*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: cement is separated from lime and gypsum plaster (which need air or a different chemistry), from ceramic (consolidated by firing, not hydration), from the polymer (organic) and from the concrete it binds. Definitional Clarity — **pass**: powder, water, hydraulic set and ambient temperature are operational, and the standard compositions fix the permissible families. Conceptual Determinacy — **qualified**: the boundary against a general *binder* is conventional, and the geopolymer sits at the edge of the class — a clinker-free binder that is called a cement by part of the field and an alkali-activated material by the rest; the note states the edge rather than hiding it. Internal Consistency — **pass**: every family is a kind of cement, and clinker is the intermediate they are made from, not a rival root. Representational Adequacy — **qualified**: complete for the kinds, the clinker phases and the production chain; mix design, conformity testing and the economics of carbon are linked rather than grown. Purpose Adequacy — **pass**: the decomposition serves material selection and process understanding, and every leaf is a kind, a phase or a regulator the builder or the kiln operator acts on.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from lime, plaster, ceramic, polymer and concrete; typed as a constitutive object, not a producer. |
| Definitional Clarity | pass | Powder, water, hydraulic set and ambient temperature are operational; EN 197-1 fixes the family compositions. |
| Conceptual Determinacy | pass (qualified) | The binder line and the geopolymer edge are conventions on a continuous field; the note states where the edge is drawn. |
| Internal Consistency | pass | All families are kinds of cement; clinker is the shared intermediate, not a second root. |
| Representational Adequacy | qualified | Complete for kinds, phases and process; mix design, standards and carbon economics are links. |
| Purpose Adequacy | pass | Every leaf serves material selection, kiln operation or the setting behaviour the builder must predict. |

## Cement as a hydraulic binder

> A **binder** is what holds other materials together. Cement is one kind of binder, and the kind matters: the class is defined by *how* it sets, not by what it is made of.

| Binder | How it sets | Consequence |
| --- | --- | --- |
| **Non-hydraulic lime** | Calcium hydroxide carbonates in air, taking CO₂ from the atmosphere | Cannot set under water, cures slowly, breathes with masonry; the classical mortar. |
| **Hydraulic lime** | Lime burned from argillaceous limestone forms hydraulic silicates and aluminates that react with water | Sets under water; the bridge from Roman practice to Portland cement. |
| **Natural pozzolana + lime** | Amorphous silica from volcanic ash reacts with lime to form calcium silicates | The Roman hydraulic mortar — *opus caementicium* — and the reason Roman harbour works survive. |
| **Portland cement** | Clinker silicates and aluminates hydrate to calcium silicate hydrate and portlandite | Fast, strong, reproducible, standardised; the industrial binder. |
| **Calcium aluminate cement** | Aluminous phases hydrate to calcium aluminate hydrates | Rapid hardening and refractory service; strength regression in hot, humid service is its named bound. |
| **Geopolymer** | Alkali activation dissolves and polycondenses aluminosilicate precursors | No calcination of limestone; standards and long-term performance are still being established. |

The distinction between cement, mortar and concrete is a distinction of *what the binder is mixed with*, not of the binder:

- **Paste** — cement and water only. The hardened paste is the binding matrix.
- **Mortar** — paste plus fine aggregate (sand). Joins masonry units and renders surfaces.
- **Grout** — a fluid mortar, placed by pumping into voids, joints or post-tensioning ducts.
- **Concrete** — paste plus fine and coarse aggregate. The composite that carries load; its strength is the paste's strength constrained by the aggregate and by the water-to-cement ratio.

## The production chain

| Stage | What happens | What it costs |
| --- | --- | --- |
| **Quarrying and crushing** | Limestone (the calcium source) and clay or shale (the silica, alumina and iron source) are extracted and crushed. | Land, dust, transport; the chemistry of the deposit sets the raw-meal correction. |
| **Raw meal preparation** | The components are proportioned to a target composition, ground fine and homogenised. | Grinding energy; the closer the raw meal to the clinker target, the less kiln correction. |
| **Clinker burning** | The raw meal is preheated, calcined (CaCO₃ → CaO + CO₂) and sintered at about 1,450 °C in a rotary kiln to clinker. | The largest energy and emissions item: fuel for the flame and the CO₂ released by calcination. |
| **Cooling** | The clinker is cooled fast enough to retain the reactive alite and belite rather than let them transform. | Cooling air; the rate sets the phase assemblage. |
| **Grinding and blending** | Clinker is ground with a few per cent of gypsum and any supplementary material (slag, fly ash, limestone, calcined clay). | Grinding energy; fineness sets early strength and setting time. |
| **Storage and dispatch** | The powder is stored, sampled, tested for setting time, soundness and strength, and shipped. | Standards conformity; the product is a certified commodity. |

## Chemistry: clinker phases and hydration

Clinker is not a compound but an assemblage of four principal phases, each with a job:

| Phase | Formula | Share of clinker | Role |
| --- | --- | --- | --- |
| **Alite** | tricalcium silicate, Ca₃SiO₅ (C₃S) | 50–70 % | Early and main strength; the phase that makes Portland cement fast. |
| **Belite** | dicalcium silicate, Ca₂SiO₄ (C₂S) | 15–30 % | Slow, late strength; the phase that keeps gaining after alite has finished. |
| **Tricalcium aluminate** | Ca₃Al₂O₆ (C₃A) | 5–10 % | Flux in the kiln; reacts fast with water and would flash-set the paste, which is why gypsum is added. |
| **Tetracalcium aluminoferrite** | Ca₄Al₂Fe₂O₁₀ (C₄AF) | 5–15 % | Iron-bearing flux; gives the clinker its dark colour and contributes little strength. |

Hydration is the reaction that turns powder into solid. Alite and belite dissolve and reprecipitate as **calcium silicate hydrate** (C-S-H), the amorphous binding phase that makes up roughly half to two thirds of the hardened paste, together with **portlandite** (Ca(OH)₂). The aluminate reacts with the dissolved gypsum to form **ettringite**, a sulfate-rich phase that coats the aluminate grains and holds back the flash set; when the gypsum is consumed the reaction resumes and the paste begins to stiffen.

Two words that are constantly confused:

- **Setting** is the loss of workability — the paste stops being placeable. Initial set is typically within an hour; final set within a working day.
- **Hardening** is the gain of strength, which continues for weeks, months and, in a thick section, years, because the hydration front advances inward through the grains.

Three variables dominate the outcome: the **water-to-cement ratio** (more water gives more porosity and less strength — Abrams' law, 1918), the **fineness** (finer grinds hydrate faster, at the cost of grinding energy and heat), and the **curing** (hydration needs water; a paste that dries out stops gaining strength).

## The families

The European standard EN 197-1 sorts common cements by how much clinker they contain:

| Family | Clinker content | What is added | Why it exists |
| --- | --- | --- | --- |
| **CEM I — Portland** | 95–100 % | Gypsum only | The reference product; predictable and widely specified. |
| **CEM II — Portland-composite** | 65–94 % | Slag, fly ash, pozzolana, limestone, silica fume or calcined clay | Lower clinker factor with familiar performance; the main substitution route. |
| **CEM III — Blastfurnace** | 5–64 % | Granulated blast-furnace slag | Low heat of hydration and sulfate resistance; the steel-industry by-product route. |
| **CEM IV — Pozzolanic** | 45–89 % | Natural or artificial pozzolana | Uses volcanic or combustion residues; slower early strength. |
| **CEM V — Composite** | 20–64 % | Slag plus pozzolana | Combines the two substitution routes. |

Beyond that standard: **calcium aluminate cement** (aluminous, rapid-hardening, refractory), **oil-well cement** (retarded and sulfate-resisting for well completion), **white cement** (low iron, for architectural concrete), **sulfate-resisting cement** (low C₃A), and the **geopolymer and alkali-activated** binders that fall outside EN 197-1.

## Concrete, mortar, grout

Cement exists to be mixed, and the mix is where its properties become the structure's:

- **Water-to-cement ratio** — the single strongest lever. Roughly 0.40–0.50 for structural concrete; above 0.60 the capillary porosity and permeability rise sharply.
- **Aggregate** — typically 60–80 % of the concrete volume; its grading, shape and strength bound what the paste can deliver.
- **Admixtures** — plasticisers and superplasticisers for workability at low water, retarders for hot weather, accelerators for cold, air entrainment for freeze–thaw.
- **Supplementary cementitious materials** — slag, fly ash, silica fume and calcined clay, added at the mixer or already blended into the cement.

See [Concrete Strength](/view.html?p=notes/miscellanea/unclassified/concrete-strength.md) for the strength side, and the `Cement Kiln` row of [Nonmetallic Production](/view.html?p=notes/technica/production/industry/nonmetallic-production.md) for the kiln as a production object.

## Energy, CO₂ and the decarbonisation problem

Cement is the largest single industrial source of CO₂, at roughly 7 % of global emissions, for two reasons that cannot be separated:

1. **Process CO₂.** Calcining limestone releases the carbon that was locked in the carbonate: about 0.51–0.54 tonnes of CO₂ per tonne of clinker is chemistry, not fuel. No amount of clean energy removes it; only a different calcium source or capture does.
2. **Fuel CO₂.** The kiln flame holds the material at about 1,450 °C, and the fuel that does it adds roughly a third of a tonne of CO₂ per tonne of clinker.

The global average now sits near 0.6 tonnes of CO₂ per tonne of cement, because the clinker factor has been falling — the same cement is made with less clinker and more slag, fly ash, limestone or calcined clay. The levers, in the order the industry applies them:

- **Clinker substitution** — the cheapest and largest near-term lever. Its own limit is a supply limit: blast-furnace slag and coal fly ash are by-products of industries that are themselves being decarbonised, so their availability falls as steel and coal change.
- **Calcined clay** — abundant and clinker-free at the reactive end; limestone calcined clay cement (LC3) is the main scalable answer where slag and ash are scarce.
- **Energy efficiency and alternative fuels** — dry-process kilns with preheaters and precalciners, and fuels from waste and biomass.
- **Carbon capture** — the only route that addresses the process CO₂ directly; expensive, and it must be fitted to a kiln that is otherwise efficient.
- **Novel clinkers** — belite-rich and calcium sulfoaluminate clinkers that need less limestone and burn cooler.

The obstacle to all of them is not only cost. [Path dependence](/glossarium/?t=path-dependence) is written into the standard: EN 197-1 defines the common cements by their clinker-based composition, so a binder that departs from the recipe must be certified as something else. The clinker route is [locked in](/glossarium/?t=lock-in) by the kilns, the quarries, the grinding circuits, the specification culture and the trained workforce built around it — which is why substitution proceeds by diluting the incumbent recipe rather than by replacing it.

## References

- https://en.wikipedia.org/wiki/Cement
- https://en.wikipedia.org/wiki/Portland_cement
- https://en.wikipedia.org/wiki/Calcium_silicate_hydrate
- https://en.wikipedia.org/wiki/Clinker_(cement)
- Taylor, H. F. W. (1997). *Cement Chemistry* (2nd ed.). Thomas Telford.
- Hewlett, P. C. (ed.) (1998). *Lea's Chemistry of Cement and Concrete* (4th ed.). Arnold.
- Mindess, S., Young, J. F., & Darwin, D. (2003). *Concrete* (2nd ed.). Prentice Hall.
- Juenger, M. C. G., Winnefeld, F., Provis, J. L., & Ideker, J. H. (2011). Advances in alternative cementitious binders. *Cement and Concrete Research*, 41(12), 1232–1243.
- Scrivener, K. L., John, V. M., & Gartner, E. M. (2018). Eco-efficient cements: Potential economically viable solutions for a low-CO₂ cement-based materials industry. *Cement and Concrete Research*, 114, 2–26.
- Andrew, R. M. (2018). Global CO₂ emissions from cement production. *Earth System Science Data*, 10, 195–217.
- EN 197-1:2011. *Cement — Part 1: Composition, specifications and conformity criteria for common cements*. CEN.
- [Ceramic](/view.html?p=notes/technica/general/materiotecnia/ceramic.md) — the adjacent inorganic class, consolidated by firing
- [Materiotecnia](/view.html?p=notes/technica/general/materiotecnia/readme.md) — the materials shelf this note belongs to
- [Concrete Strength](/view.html?p=notes/miscellanea/unclassified/concrete-strength.md) — what the paste does inside the composite
- [Nonmetallic Production](/view.html?p=notes/technica/production/industry/nonmetallic-production.md) — the cement kiln as a production object
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
