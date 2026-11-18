---
tags: [note, agro, herbicide, agrochemical, plant-protection, glyphosate]
---

# Glyphosate

> **Glyphosate** — *N*-(phosphonomethyl)glycine, C₃H₈NO₅P — is the broad-spectrum systemic herbicide that blocks the shikimate pathway, and the most widely used pesticide in the world. It is a molecule designed to kill plants through an enzyme that animals do not have, and its history is the history of the herbicide-tolerant crop.

> Its technical importance is not only that it kills weeds. It is that it can be sprayed over a growing crop if the crop carries a resistant enzyme, which turned a burndown chemical into a system: the seed, the spray and the weed-control programme are one product.

## Formulation

### What technical element type does this technical instance belong to?

**Glyphosate belongs to the `Constitutive Technical Object` technical element type — a material that constitutes a larger technical object or system, here the crop-protection programme.**

It is a constitutive object because it does not act by itself: the formulated product, the sprayer and the timing are what operate, and the molecule is the active constituent. Readable as a `Technical Practice` when the weed-control programme is considered, and as a `Technical Constraint` on the cropping system when resistance is the question. Those readings are prose, not second roots.

The boundary against a **fertilizer** is the purpose: a fertilizer supplies a nutrient the plant needs, a herbicide removes a competitor. The boundary against a **contact herbicide** is the translocation: glyphosate moves to the growing points, which is why it kills a perennial's root and not just its leaf.

### What is this technical instance?

> The acid and its isopropylamine, potassium and ammonium salts, formulated with surfactants that let the droplet wet the leaf and carry the molecule through the cuticle. It is applied to foliage, translocated in the phloem to meristems and roots, and it inhibits EPSP synthase, the enzyme that condenses shikimate-3-phosphate with phosphoenolpyruvate in the pathway that makes the aromatic amino acids. The plant stops growing and dies over one to three weeks.

### What is the recursive instance decomposition of this technical instance?

> Boundary: the active substance and its formulation, the mechanism it runs, the tolerant crop it enables, the parameters that decide its fate, and the constraints it meets. The sprayer, the farm programme and the regulatory dossier are separate elements.
>
> Stopping rule: a row is terminal when it names a form, a mechanism, a measured parameter or a named constraint.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.
>
> Verbs: the salt *dissolves*; the surfactant *wets*; the molecule *inhibits* the enzyme; the crop trait *tolerates* it.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technical Object` → Glyphosate | The active substance N-(phosphonomethyl)glycine and the products built from it. |
| `Constitutive Technical Object` → Glyphosate → `Constitutive Technical Object` | Grouping: the forms the substance is supplied in. |
| `Constitutive Technical Object` → Glyphosate → `Constitutive Technical Object` → Glyphosate Acid | The free acid — low solubility, the form whose salts are made for formulation. |
| `Constitutive Technical Object` → Glyphosate → `Constitutive Technical Object` → Isopropylamine Salt | The classic formulated salt, highly water-soluble. |
| `Constitutive Technical Object` → Glyphosate → `Constitutive Technical Object` → Potassium Salt | The high-load salt used in concentrated and drift-reduced formulations. |
| `Constitutive Technical Object` → Glyphosate → `Constitutive Technical Object` → Surfactant System | The wetter and penetrant that carries the molecule through the leaf cuticle. |
| `Constitutive Technical Object` → Glyphosate → `Technical Mechanism` | Grouping: how the molecule kills. |
| `Constitutive Technical Object` → Glyphosate → `Technical Mechanism` → EPSP Synthase Inhibition | Blockade of the enzyme that condenses shikimate-3-phosphate and phosphoenolpyruvate. |
| `Constitutive Technical Object` → Glyphosate → `Technical Mechanism` → Shikimate Pathway Blockade | Aromatic amino acid synthesis stops, and the plant cannot make proteins or lignins. |
| `Constitutive Technical Object` → Glyphosate → `Technical Mechanism` → Systemic Translocation | Phloem movement from the treated leaf to meristems and roots — the reason perennials die. |
| `Constitutive Technical Object` → Glyphosate → `Production Technical Object` | Grouping: the crop system the molecule enables. |
| `Constitutive Technical Object` → Glyphosate → `Production Technical Object` → Glyphosate-Tolerant Crop | A variety carrying a resistant EPSP synthase, so the herbicide can be sprayed over it. |
| `Constitutive Technical Object` → Glyphosate → `Technical Parameter` | Grouping: the variables that decide behaviour. |
| `Constitutive Technical Object` → Glyphosate → `Technical Parameter` → Application Rate | Grams of acid equivalent per hectare, the dose the programme is built around. |
| `Constitutive Technical Object` → Glyphosate → `Technical Parameter` → Soil Adsorption | Strong binding to soil particles, which is why it does not leach to groundwater readily. |
| `Constitutive Technical Object` → Glyphosate → `Technical Parameter` → Degradation Half-Life | Microbial breakdown to AMPA and further, in weeks to months depending on soil and climate. |
| `Constitutive Technical Object` → Glyphosate → `Technical Parameter` → Uptake and Translocation Rate | How much enters the leaf and how fast it reaches the growing points. |
| `Constitutive Technical Object` → Glyphosate → `Technical Constraint` | Grouping: the bounds the use meets. |
| `Constitutive Technical Object` → Glyphosate → `Technical Constraint` → Weed Resistance | Target-site mutation, enzyme over-expression and reduced translocation in repeated-use populations. |
| `Constitutive Technical Object` → Glyphosate → `Technical Constraint` → Drift and Non-Target Damage | Spray movement onto sensitive crops and vegetation. |
| `Constitutive Technical Object` → Glyphosate → `Technical Constraint` → Regulation and Litigation | Residue limits, classification disputes and the liability that follows the product. |

## Mechanism

> The shikimate pathway is how plants, fungi and bacteria make the aromatic amino acids — phenylalanine, tyrosine and tryptophan — and their downstream products: lignins, flavonoids, alkaloids, auxins. Animals do not have the pathway; they obtain those amino acids from their food. That is the selectivity of glyphosate at the biochemical level: it inhibits an enzyme the target has and the consumer does not.

> Glyphosate is a transition-state analogue of phosphoenolpyruvate and binds EPSP synthase tightly. The plant accumulates shikimate-3-phosphate, stops growing, and dies slowly — which is why the visual effect lags the application by one to three weeks, and why a rain event too soon after spraying washes off a molecule that had not yet entered.

## Formulation and Use

| Use | Timing | Why the molecule suits it |
| --- | --- | --- |
| **Burndown** | Before sowing | Kills existing vegetation without soil residue that would injure the next crop |
| **Post-emergent in tolerant crops** | Over the growing crop | The crop's resistant enzyme survives the dose that kills the weeds |
| **Orchard and vineyard strips** | Directed, between rows | Systemic control of perennials without soil disturbance |
| **Non-crop and industrial** | Any | Broad spectrum, low soil activity, no residual carry-over |
| **Aquatic and rights-of-way** | Labelled formulations | Adsorption and degradation limit off-site movement |

> The surfactant is not an inert extra. It decides how much of the droplet enters the leaf, and the formulated product's toxicity and irritancy often follow the surfactant more than the active substance. That is one reason a toxicity argument about "glyphosate" can be an argument about two different objects.

## Tolerant Crops

> The tolerant trait is a bacterial EPSP synthase — the CP4 enzyme from *Agrobacterium* — that glyphosate binds poorly. Inserted into soybean, maize, cotton and canola, it let the herbicide be applied after the crop emerged, and it turned weed control from a sequence of selective products into one molecule plus one seed. The agronomic consequence was a simplification of the programme; the evolutionary consequence was a single selection pressure applied over millions of hectares.

## Resistance

> Resistance has evolved in dozens of weed species. Three mechanisms recur: a **target-site mutation** that changes the enzyme so glyphosate no longer binds; **over-expression** of the enzyme, so the plant out-produces the inhibition; and **reduced translocation**, so the molecule stays in the treated leaf. Multiple resistance to several herbicide groups is now the practical problem, and the answer is the same as in antibiotics — diversity of mechanism, not a stronger dose.

## Fate

> Glyphosate binds strongly to soil, so it is largely immobile and does not usually reach groundwater; it is broken down by soil microbes, with AMPA as the principal metabolite. The environmental questions that remain are about erosion-bound transport, repeated application, and the effects on non-target plants at the field margin — not about persistence in solution.

## Toxicity and Regulation

> Acute toxicity to mammals is low; the formulated surfactant is the more irritant component. The carcinogenicity classification is contested: the International Agency for Research on Cancer classified glyphosate as probably carcinogenic to humans in 2015, while most pesticide regulators — the EPA, EFSA and others — concluded that it is unlikely to be carcinogenic at permitted exposures, and the disagreement is about which studies and which end-points count. The litigation that followed has made the molecule a case study in how a technical object becomes a legal and political one.

## What is a critical conceptual evaluation of this technical element instance?

The concept under evaluation is **Glyphosate**, defined above as *the broad-spectrum systemic herbicide that inhibits EPSP synthase in the shikimate pathway*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: the molecule is separated from the formulated product, from the tolerant crop system and from the herbicide programme. Definitional Clarity — **pass**: the target enzyme, the pathway and the translocation are operational. Conceptual Determinacy — **pass with qualification**: "glyphosate" names the acid, its salts and its formulations, and the toxicity and regulatory questions attach to different objects in that set; the note says so. Internal Consistency — **pass**: forms, mechanism, enabling objects, parameters and constraints are distinct branches. Representational Adequacy — **qualified**: complete for the technical object; the resistance ecology, the regulatory dossiers and the litigation are links. Purpose Adequacy — **pass**: every leaf serves formulation, application, resistance management or regulatory reading.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from the formulation, the tolerant crop and the weed-control programme. |
| Definitional Clarity | pass | Target enzyme, pathway, translocation and dose are operational. |
| Conceptual Determinacy | pass (qualified) | Acid, salts and formulations are different objects for toxicity and regulation; stated. |
| Internal Consistency | pass | Forms, mechanism, enabling objects, parameters and constraints are separate branches. |
| Representational Adequacy | qualified | Complete for the object; resistance ecology, dossiers and litigation are links. |
| Purpose Adequacy | pass | Every leaf serves formulation, application, resistance or regulation. |

## References

- [Glyphosate](https://en.wikipedia.org/wiki/Glyphosate)
- [EPSP synthase](https://en.wikipedia.org/wiki/Enolpyruvylshikimate_3-phosphate_synthase) · [Shikimate pathway](https://en.wikipedia.org/wiki/Shikimate_pathway)
- [Glyphosate-based herbicides](https://en.wikipedia.org/wiki/Glyphosate-based_herbicides) · [Roundup](https://en.wikipedia.org/wiki/Roundup_(herbicide))
- [Herbicide resistance](https://en.wikipedia.org/wiki/Herbicide_resistance)
- [Crop Productivity](/view.html?p=notes/technica/general/agro/crop-productivity.md) — the yield the weed control protects
- [Plant Health Technical Set](/view.html?p=notes/technica/general/plant-health-technical-set.md) — the protection apparatus the molecule belongs to
- [Fertilizer Industry](/view.html?p=notes/technica/production/industry/chemical/fertilizer.md) — the other great input, with the opposite failure mode
- [Agro](/view.html?p=notes/technica/general/agro/agro.md) — the domain entry note
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) — the schema and the permitted link forms
- [Technica Atlas](/corpus/notes/technica/atlas.html) — the forest this decomposition feeds
