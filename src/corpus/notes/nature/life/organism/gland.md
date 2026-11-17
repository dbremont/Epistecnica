---
tags: [note, nature, natural-system, biology, system, organ, secretion]
---

# Gland

> **A gland** is a natural system whose organized parts produce and release a secretion: a secretory epithelium, the apparatus that makes the product, and a route — a duct to a surface, or a vascular bed into the blood — by which the product leaves. It is the body's way of moving a substance it has made from where it is made to where it is used.

> What a gland *is* cannot be read off its shape, because the same architecture serves opposite routes. **Exocrine** glands keep a duct and deliver outward — sweat, saliva, milk, digestive enzymes. **Endocrine** glands lose the duct during development and deliver inward, into the blood — thyroid hormone, insulin, cortisol. The dividing question is not what the gland looks like but **where the secretion goes**, and that one answer decides whether the product acts on a surface or on every cell that carries the receptor for it.

> The gland is also the clearest case in the body of a system whose output is regulated rather than merely produced: secretion rate is set by a feedback loop — neural for the salivary and sweat glands, hormonal for the thyroid and adrenal cortex, local for the pancreatic islets — so the organ is read as a controlled flow, not as a fixed structure.

## Formulation

### What natural element type does this natural instance belong to?

**A gland, read as a natural instance, belongs to `Ontic Element (→ Kind) Substantive (→ Kind) Natural System`** — a bounded set of interacting parts with a defined input, a product and a route out, at the meso level of organization.

Readable secondarily as a `Natural Object`: the same gland treated as one discrete anatomical particular, named and counted. That reading is prose here, not a second root. It is not a `Substance / Matter` (a gland is not made of one stuff), not a `Process` (secretion is what happens in it), and not an `Organism` (it does not maintain or reproduce itself).

### What is this natural instance?

> Every gland is read through the same slots: the **secretory unit** that makes the product, the **secretion** itself, the **route** (duct or blood), the **target** the secretion reaches, the **control** that sets the rate, and the **support** — connective capsule, septa, blood supply — that holds the units together and carries what they need.

> Two divisions do most of the work. By **route**: exocrine (duct), endocrine (ductless, vascular), mixed (both at once). By **mode of release**: merocrine (the cell secretes without losing itself), apocrine (the apical cytoplasm goes with the product), holocrine (the whole cell disintegrates into the secretion). The mode is a property of the secretory cell; the route is a property of the gland's architecture. They vary independently, which is why "gland" names a functional class and not a shape.

> A gland is also an **organ** in the corpus's sense, and often a part of a larger system: the thyroid is an organ of the endocrine system, the pancreas belongs to both the digestive and the endocrine systems, and the sweat glands are distributed components of the skin rather than organs in their own right.

### What is the recursive instance decomposition of this natural instance?

> Boundary: one gland as a natural system — its parts, the mechanism that produces the secretion, the process that releases it, the quantities that characterise it, and the conditions that bound it. The particular gland instances are decomposed in their own notes (`thyroid`, `pancreas`, `pituitary`, …) and linked from Related; the hormones a gland releases are molecules, filed in the human corpus. The systems a gland belongs to are associated, not parts.

> Stopping rule: a row is terminal when it names a structural part, a mechanism, a quantity, or a governing condition whose own decomposition lives elsewhere.

> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the secretory cell is **micro**; one gland is **meso**. Limitation checklist for the segment: **Scale** (the same gland appears as an organ in one system and as a component of another), **Partial Observability** (secretion rate is measured from samples, not watched continuously), **Nonlinearity** (feedback makes the rate a function of the response, not of the stimulus alone), **Many-Body coupling** (a gland's output is read against the other glands of its axis).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland | Bound root instance: a bounded secretory system — units that make a product, a route out, and a control that sets the rate. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Part)` `Natural Object` | Grouping: the material particulars constituting the gland. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Part)` `Natural Object` `(→ Instance)` Secretory Unit | The acinus or tubule of epithelial cells that synthesizes, stores and releases the product. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Part)` `Natural Object` `(→ Instance)` Duct | The channel that carries an exocrine secretion to a surface — absent in the endocrine gland, which is what makes it endocrine. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Part)` `Natural Object` `(→ Instance)` Capsule and Septa | The connective envelope and its partitions, which divide the gland into lobes and lobules and carry vessels and nerves. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Component)` `Mechanism` | Grouping: the mechanism operating within the gland. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Component)` `Mechanism` `(→ Instance)` Secretion Mechanism | Synthesis, packaging, and release: the cellular machinery that turns raw material into the secreted product. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Occurrence)` `Natural Process` | Grouping: the processes occurring in the gland. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Occurrence)` `Natural Process` `(→ Instance)` Secretion Cycle | The repeated sequence of production, storage, release, and rest by which the gland delivers its product at a rate. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Attribute)` `Property` | Grouping: the quantities that characterise a gland. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Attribute)` `Property` `(→ Instance)` Secretion Product | What the gland makes — serous, mucous, oily, or hormonal — which fixes what the secretion can do at the target. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Attribute)` `Property` `(→ Instance)` Secretion Rate | How much product leaves per unit time; the quantity the control loop actually sets. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Attribute)` `Property` `(→ Instance)` Release Mode | Merocrine, apocrine, or holocrine — whether the cell survives the act of secretion. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Attribute)` `Property` `(→ Instance)` Route | Exocrine, endocrine, or mixed — where the secretion goes, and therefore what it can reach. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Bound)` `Constraint` | Grouping: what bounds the gland's behaviour. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Bound)` `Constraint` `(→ Instance)` Duct Continuity | An exocrine gland secretes only while its duct is open; obstruction converts the product into a retained, damaging load. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Bound)` `Constraint` `(→ Instance)` Vascular Supply | An endocrine gland needs a blood flow to carry the product away; without it the hormone has no route. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Gland `(→ Bound)` `Constraint` `(→ Instance)` Feedback Loop | The rate is bounded by the response it produces — the target's state feeds back on the gland that acts on it. |

## Which are the kinds of gland?

> Ordered by **where the secretion goes**, because that is the division that decides what the product can act on. The mode of release is a second axis and cuts across the rows: the same route carries merocrine, apocrine and holocrine glands.

| Kind | Route | Description | Case |
| --- | --- | --- | --- |
| **Exocrine** | Duct to an epithelial surface | The product leaves the body or enters a lumen; it acts where it lands | Sweat, salivary, mammary, sebaceous glands |
| **Endocrine** | Ductless, into the blood | The product is a hormone; it acts on every cell carrying its receptor | Thyroid, adrenal cortex, pituitary, pancreatic islets |
| **Mixed** | Both routes in one organ | One organ carries exocrine tissue and endocrine tissue side by side | Pancreas (acini + islets); liver (bile + endocrine secretion) |
| **Paracrine** | Into the local intercellular space | The product acts on neighbouring cells without entering the blood — a signalling mode more than a gland architecture | Somatostatin from pancreatic delta cells |
| **Exocrine, single-celled** | One cell, one duct | A secretory cell embedded in an epithelium, not organized into a glandular body | Goblet cells of the respiratory and intestinal lining |

## QA

### Is a gland an organ?

> Not always, and the distinction is worth keeping. A gland is a **functional** class — a system that makes and releases a secretion. An organ is a structural particular. A large gland (thyroid, pancreas) is an organ; a sweat gland is a component distributed through the skin; a goblet cell is a single secretory cell. All three are glands; only the first is an organ. See [Organ](/view.html?p=notes/nature/life/organism/organ.md) and [Organ System](/view.html?p=notes/nature/life/organism/organ-system.md).

### Why is the pancreas both an exocrine and an endocrine gland?

> Because it carries two secretory populations with different routes in one capsule: the acini send digestive enzymes through ducts into the intestine, while the islets of Langerhans release insulin and glucagon into the blood. The mixed row in the table is not a compromise — it is the ordinary case of an organ whose parts serve two systems at once, which is also why the same organ is filed under both the digestive and the endocrine systems.

### Is a hormone a secretion?

> Yes — the endocrine product is a secretion whose route is the blood rather than a duct. That is why the endocrine glands are the corpus's entry point to the hormones: the gland is the natural system, the hormone is the molecule it secretes, and the receptor is the target's side of the same relation.

### Why keep the note at the organism level rather than in the human corpus?

> Because nothing in it is human-specific. The human corpus holds the **particular** glands — thyroid, pancreas, pituitary, ovaries, testes — and the endocrine system that organizes them; the general concept sits beside `organ`, `organ-system` and `tissue`, where the body-part vocabulary is assembled. A gland of a fish and a gland of a human are the same natural element at the same level of organization.

## References

- [Philosophia Naturalis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-naturalis-et-operis.md) (schema owner)
- [Organ](/view.html?p=notes/nature/life/organism/organ.md) · [Organ System](/view.html?p=notes/nature/life/organism/organ-system.md) · [Tissue](/view.html?p=notes/nature/life/organism/tissue.md) — the structural vocabulary the gland belongs to
- [Endocrine System](/view.html?p=notes/nature/life/organism/human/endocrine-system.md) — the system that organizes the endocrine glands
- [Thyroid](/view.html?p=notes/nature/life/organism/human/thyroid.md) · [Pancreas](/view.html?p=notes/nature/life/organism/human/pancreas.md) · [Pituitary](/view.html?p=notes/nature/life/organism/human/pituitary.md) — the particular glands
- [Hormone](/view.html?p=notes/nature/life/organism/human/hormone.md) — the endocrine product
- Bloom, W., & Fawcett, D. W. (1994). *A textbook of histology* (12th ed.). Chapman & Hall.
- Junqueira, L. C., & Carneiro, J. (2005). *Basic histology: Text and atlas* (11th ed.). McGraw-Hill.
- Ross, M. H., & Pawlina, W. (2011). *Histology: A text and atlas* (6th ed.). Lippincott Williams & Wilkins.
- Young, B., & Heath, J. W. (2000). *Wheater's functional histology* (4th ed.). Churchill Livingstone.
- [Gland](https://en.wikipedia.org/wiki/Gland)
