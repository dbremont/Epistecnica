---
tags: [note, healthcare, medical-device, regulation]
qa:
 - Is a medical device a healthcare product even though it has no active substance?
 - What decides whether an article is a medicine or a device?
 - Why is a prefilled syringe both, and which regime wins?
 - Why does a diagnostic test count as a product at all?
 - What does traceability add that safety and efficacy do not?
 - Where does a disinfectant stop being a healthcare product?
---

# Healthcare Product

> A **healthcare product** is an article made for a health purpose — preventing, diagnosing, treating, monitoring or replacing a body function — and placed on the market under a healthcare regime. It is the umbrella over medicines, devices and diagnostics: what unites them is not the substance or the mechanism but the claim and the regime, since the same piece of engineering can be regulated as a device in one claim and as a medicine in another.

## Formulation

### What technical element type does this technical instance belong to?

**A healthcare product belongs to the `Technical Element (→ Kind) Production Technical Object (→ Kind) Physical Production Technical Object` technical element type — a delivered material good whose operative structure is material and whose operation is realized through a physical effect.**

It is the object the healthcare production system delivers, not the system itself: the manufacturer, the quality system and the authorised site are the system; the article on the shelf is the product. Readable secondarily as a `Technical Element Set` — the article plus its packaging, labelling and instructions — and as a `Constitutive Technical Object` when it is read as the constituent of a care pathway.

### What is this technical instance?

> **The classification turns on the principal mode of action, not on the technology.** A medicine acts pharmacologically, immunologically or metabolically; a device acts physically or mechanically, and its pharmacological, immunological or metabolic action is ancillary. That single criterion decides which regime an article enters, and it is why a scalpel and a statin are both healthcare products while only one of them is a drug.

| Product class | Principal mode of action | Regime | Example |
| --- | --- | --- | --- |
| Pharmaceutical product | Pharmacological, immunological or metabolic | Medicinal-product authorisation | Atorvastatin tablets, MMR vaccine |
| Medical device | Physical or mechanical, with no pharmacological principal action | MDR 2017/745; FDA 510(k) or PMA | Pacemaker, hip implant, syringe |
| In vitro diagnostic product | Physical or chemical action on a specimen outside the body | IVDR 2017/746 | PCR assay, glucose test strip |
| Combination product | Both, in one article | Drug–device route, one lead authority | Prefilled syringe, drug-eluting stent, inhaler |
| Borderline: biocide or disinfectant | Chemical action on the environment, not on the patient | Biocidal Products Regulation | Hand disinfectant, surface disinfectant |

> **Devices are classified by risk, not by function.** The regulatory class rises with the invasiveness, the duration of contact and the criticality of the organ reached — a tongue depressor and a heart valve are both devices and sit at opposite ends of the same scale. That is what makes the class a property of the article's use rather than of its engineering.

> **Combination products are the hard case, and they are settled by the lead.** A prefilled syringe is a device containing a medicine; an inhaler is a device that delivers one; a drug-eluting stent is a device whose drug is ancillary. The regime is chosen by which component supplies the principal action, and the other component is then regulated as part of that whole — which is why the same molecule can be authorised twice, once as a medicine and once as a device component.

> **The product is defined by its dossier and its traceability.** Safety and efficacy are demonstrated, but the article is also identified: the unique device identifier or the batch number ties this physical object to its manufacturing history, its sterilisation record and its field actions. A recall is impossible without it, and that is why traceability is a release property of the article rather than a convenience of logistics.

> **Where the boundary stops.** A cosmetic is a healthcare product only when a medicinal claim is made for it; a food supplement is a food unless it is presented for a medical purpose; a disinfectant acts on the environment and stays outside the patient-facing classes, sitting in the biocidal regime instead.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one healthcare product — the product classes it falls into, the constituents that make the article, the properties by which it is released, and the regimes that govern it. The production system that makes it, the patient who receives it and the disease it addresses are associated elements with their own notes, not parts of the article.
>
> Stopping rule: a row is terminal when it names a product class, a constituent of the article, a release property or a governing standard. The pharmacology of a medicine belongs to the drug note, and the engineering of a device to the device literature.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Typing reads from the nearest enclosing type segment.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` | Grouping: the type a healthcare product is read under — the delivered material good. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product | Bound root instance: the article made for a health purpose and released under a healthcare regime. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Kind)` `Physical Production Technical Object` | Grouping: the product classes the article falls into. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Pharmaceutical Product | The medicinal article — atorvastatin tablets, MMR vaccine — acting pharmacologically, immunologically or metabolically. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Medical Device | The physical article — pacemaker, hip implant, syringe — acting mechanically or physically, classed by risk. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` In Vitro Diagnostic Product | The specimen-testing article — PCR assay, glucose strip — acting on material taken from the body. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Combination Product | The article joining a medicine and a device — prefilled syringe, drug-eluting stent, inhaler — regulated by its lead component. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Part)` `Constitutive Technical Object` | Grouping: the constituents assembled into the article. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Active Component | The substance that carries the action in a medicine, or the mechanism that carries it in a device. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Device Material Set | The materials chosen for contact with tissue — polymer, metal, ceramic — and their biocompatibility evidence. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Packaging and Labelling | The sterile barrier, the label and the unique device identifier that tie the article to its batch. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Instructions for Use | The declared indication, dose or procedure, and the warnings that limit them. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Has)` `Technical Property` | Grouping: the properties fixed at release. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Has)` `Technical Property` `(→ Instance)` Safety | The demonstrated absence of unacceptable harm under the declared use, assessed against ISO 14971. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Has)` `Technical Property` `(→ Instance)` Efficacy or Performance | The demonstrated effect in the claimed indication — clinical efficacy for a medicine, performance for a device. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Has)` `Technical Property` `(→ Instance)` Biocompatibility | The tolerance of the materials by living tissue, established before any patient contact. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Has)` `Technical Property` `(→ Instance)` Sterility | The absence of viable micro-organisms, guaranteed by the sterile barrier rather than by the last test. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Has)` `Technical Property` `(→ Instance)` Traceability | The identifier that links the physical article to its batch, its history and its field actions. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Governed By)` `Technical Standard` | Grouping: the regimes and standards that govern the article. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Governed By)` `Technical Standard` `(→ Instance)` Medical Device Regulation | MDR 2017/745 (EU) — classification, conformity assessment, clinical evaluation and post-market surveillance of devices. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Governed By)` `Technical Standard` `(→ Instance)` In Vitro Diagnostic Regulation | IVDR 2017/746 (EU) — the same regime applied to specimen-testing products. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Governed By)` `Technical Standard` `(→ Instance)` Quality Management Standard | ISO 13485 and 21 CFR 820 — the quality system under which the article is designed, made and released. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Governed By)` `Technical Standard` `(→ Instance)` Risk Management Standard | ISO 14971 — the process that turns hazards into assessed risks and drives the design and the labelling. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Kind)` `Physical Production Technical Object` `(→ Instance)` Healthcare Product `(→ Governed By)` `Technical Standard` `(→ Instance)` Marketing Authorisation | The decision that places the article on the market for a stated indication, dose and population. |

### What is a critical conceptual evaluation of this `technical element instance`?

The concept under evaluation is **Healthcare Product**, defined above as *the article made for a health purpose and released under a healthcare regime*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: separated from the pharmaceutical product (one kind), the cosmetic and the supplement (no medicinal claim) and the biocide (acts on the environment) by the claim-and-regime test. Definitional Clarity — **pass**: the definition names the purpose and the regime, both documentary and checkable. Conceptual Determinacy — **pass with qualification**: the umbrella is deliberately wider than its kinds, so membership is settled by the *principal mode of action*, which is an assessment rather than a property of the object; the definition handles this by making the regime, not the engineering, the criterion. Internal Consistency — **pass**: the kinds partition the class by that criterion and do not overlap, except for combination products, which are declared as the overlap. Representational Adequacy — **pass**: covers the classes, the constituents, the release properties and the regimes; the engineering of devices and the pharmacology of medicines are delegated to their notes. Purpose Adequacy — **pass**: every leaf is a class, a constituent, a property or a regime — usable as a market-entry checklist.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from pharmaceutical product (a kind), cosmetic and supplement (no claim) and biocide (acts on the environment). |
| Definitional Clarity | pass | Purpose and regime are named; both are documentary and checkable against a dossier. |
| Conceptual Determinacy | qualified | Membership is an assessment of principal mode of action, not a property of the object; the regime is the criterion, which removes the drift. |
| Internal Consistency | pass | The kinds partition the class; combination products are the declared overlap rather than an inconsistency. |
| Representational Adequacy | pass | Classes, constituents, release properties and regimes are present; device engineering and drug pharmacology are delegated. |
| Purpose Adequacy | pass | Leaves resolve to classes, constituents, properties and regimes — a workable market-entry checklist. |

## References

- [Medical device](https://en.wikipedia.org/wiki/Medical_device) (classification by risk and the device/medicine boundary)
- [Medication](https://en.wikipedia.org/wiki/Medication) (the medicinal-product reading of the same umbrella)
- Regulation (EU) 2017/745 on medical devices. *Official Journal of the European Union*, L 117. https://eur-lex.europa.eu/eli/reg/2017/745/oj
- Regulation (EU) 2017/746 on in vitro diagnostic medical devices. *Official Journal of the European Union*, L 117. https://eur-lex.europa.eu/eli/reg/2017/746/oj
- ISO 13485:2016 *Medical devices — Quality management systems — Requirements for regulatory purposes*; ISO 14971:2019 *Medical devices — Application of risk management to medical devices*.
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) (schema owner)
- [Philosophia Conceptuum et Operis](/view.html?p=notes/philosophia-conceptuum-et-operis.md) (evaluation criteria)

## Related

- [Pharmaceutical Product](/view.html?p=notes/technica/general/cto/product/pharmaceutical-product.md) — the medicinal kind of healthcare product.
- [Drug](/view.html?p=notes/technica/general/cto/product/drug.md) — the active substance a medicinal product carries.
- [Fine Chemical](/view.html?p=notes/technica/general/cto/product/fine-chemical.md) — the specification-sold substance at the head of the chain.
- [Pharmaceutical Pipeline](/view.html?p=notes/technica/general/cto/industry/pharma-pipeline.md) — the production system behind the medicinal class.
- [Biotech Production Ecosystem](/view.html?p=notes/technica/general/cto/industry/biotech-production-ecosystem.md) — the production ecosystem biological products depend on.
- [Laboratory Tooling](/view.html?p=notes/technica/general/cto/industry/laboratory-tooling.md) — the instruments the diagnostic class is built around.
- [Human](/view.html?p=notes/nature/human/human.md) — the organism the article is used on.
