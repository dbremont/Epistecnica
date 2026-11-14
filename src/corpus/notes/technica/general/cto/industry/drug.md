---
tags: [note, pharma, drug, pharmacology]
qa:
 - Is a drug the same thing as a pharmaceutical product?
 - What separates a drug from a fine chemical when the molecule is identical?
 - Why does a vaccine not count as a drug in the pharmacological sense?
 - Why can a drug not be made completely safe?
 - Why do some drugs take weeks to act while others act in seconds?
 - What makes a molecular target a target?
---

# Drug

> A **drug** is the active principle of a medicine: a substance that, once in a living organism, binds a molecular target and changes what that target does. It is the molecule read by its **action**, not by its specification — potency at a receptor rather than assay on a certificate, a therapeutic index rather than an impurity profile. The same substance is a fine chemical on the loading dock and a drug in the pharmacopoeia.

## Formulation

### What technical element type does this technical instance belong to?

**A drug belongs to the `Constitutive Technical Object` technical element type — the active substance constituting a pharmaceutical product.**

It is constitutive because the molecule is never delivered alone: it is formulated with excipients, put in a dosage form, packaged and authorised, and the product is what the patient receives. The drug is the part that carries the action.

Readable secondarily as a `Technical Resource` (an input consumed by formulation) and as a `Production Technical Object` (the substance the pharmaceutical plant delivers). Both readings are prose here, not additional roots.

### What is this technical instance?

> **A drug is defined by what it does, not by what it is made of.** Two molecules of the same mass and the same functional groups can differ in whether they are a drug at all, because the definition is relational: a target, an affinity, an effect. A substance becomes a drug when its binding to a biological target produces a change worth wanting, and the whole of pharmacology is the study of how far that change can be pushed before it becomes damage.

> **The boundary against a fine chemical is the claim, not the molecule.** An active pharmaceutical ingredient is a fine chemical: high purity, a monograph, GMP. The drug reading adds the pharmacological question — what does it bind, how strongly, how selectively, and at what dose does the binding stop being therapeutic — and that question is not answered by the specification sheet.

> **The boundary against a pharmaceutical product is formulation.** A drug is a substance; a pharmaceutical product is an article. The product adds excipients, a dosage form, a container, a shelf life and an authorisation, and it is the product that carries the indication on its label.

> **Targets.** Nearly every drug acts by binding one of a small number of molecular target classes, and the class fixes what the drug can do.

| Biological target | Function | Example of pharmaceutical action |
| --- | --- | --- |
| **Receptors (proteins)** | Receive and respond to chemical signals. | Activate or block receptors. |
| **Enzymes (proteins)** | Catalyze biochemical reactions. | Inhibit or activate enzymes. |
| **Ion channels (proteins)** | Regulate the movement of ions across cell membranes. | Open or block channels. |
| **Transporters (proteins)** | Move molecules across membranes. | Block or modify molecular transport. |
| **Nucleic acids (DNA/RNA)** | Store and express genetic information. | Interfere with DNA replication or RNA function. |
| **Cell membranes** | Separate and regulate cellular environments. | Modify membrane properties. |

> The classes are not symmetric in what they buy. **Receptors** are the most selective target — a β-adrenoceptor blocker such as propranolol acts at a site shaped to distinguish it from dozens of similar receptors — and agonism and antagonism are the two directions a receptor drug can take. **Enzymes** give inhibition a measurable output, which is why statins on HMG-CoA reductase are the textbook case: the drug lowers a synthesised product, and the dose is read off the product's level. **Ion channels** act fast enough for local anaesthetics, which block voltage-gated sodium channels and stop an impulse before it propagates. **Transporters** are the target of the SSRIs, which block the serotonin transporter and leave transmitter in the cleft. **Nucleic acids** are the target of alkylating chemotherapy, which cross-links DNA, and of antisense and siRNA drugs, which remove an RNA message. **Membranes** are the least specific target, and the drugs that use them pay for it: amphotericin B binds ergosterol and works because fungal membranes contain a sterol human membranes do not.

> **What a drug can do.** Alter physiological function (analgesics, NSAIDs, antihypertensives), treat disease (antibiotics, antivirals), modify mood and cognition (SSRIs, stimulants), replace a deficiency (insulin, thyroid hormone) and prevent a condition (prophylactic antimalarials; vaccines, though those act through the immune system rather than through a drug target).

> **What a drug cannot do.** It cannot cure every disease — Alzheimer's and advanced cancers lack a definitive cure — and it does not work equally for everyone: pharmacogenomic variation changes both the exposure and the target. It does not fix the conditions that produced the disease, so an antihypertensive manages a pressure rather than a diet. It does not always act at once: an SSRI takes weeks to change mood while a local anaesthetic acts in seconds, because one waits on receptor adaptation and the other blocks a channel directly. And it cannot be completely safe, because a target that matters to the disease usually matters somewhere else too.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one drug substance — the kinds of substance the term covers, the mechanisms through which it acts on its targets, the properties by which it is characterised, and the standards that govern it. The formulation it enters, the fine chemical it may also be, and the organism it acts on are associated elements with their own notes, not parts of the drug.
>
> Stopping rule: a row is terminal when it names a kind of drug substance, a target-mediated mechanism, a pharmacological property, or a governing standard. Receptor pharmacology and signal-transduction detail belong to the physiology notes.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Typing reads from the nearest enclosing type segment.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` | Grouping: the type a drug is read under — the active substance constituting a pharmaceutical product. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug | Bound root instance: the active principle that binds a biological target and changes its behaviour. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Kind)` `Constitutive Technical Object` | Grouping: the kinds of drug substance. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Kind)` `Constitutive Technical Object` `(→ Instance)` Small-Molecule Drug | A synthetic or natural molecule of low molecular weight — aspirin, metformin, atorvastatin. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Kind)` `Constitutive Technical Object` `(→ Instance)` Biological Drug | A protein, antibody or nucleic acid made in a living system — insulin, trastuzumab, an mRNA therapeutic. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Kind)` `Constitutive Technical Object` `(→ Instance)` Prodrug | An inactive precursor converted to the active substance in the body — enalapril to enalaprilat, codeine to morphine. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` | Grouping: the target-mediated mechanisms through which the substance acts. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` `(→ Instance)` Receptor-Mediated Action | Agonism or antagonism at a receptor — propranolol blocking β-adrenoceptors. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` `(→ Instance)` Enzyme Inhibition | Blocking a catalytic site or an allosteric site — statins on HMG-CoA reductase. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` `(→ Instance)` Enzyme Activation | Increasing a catalytic rate — fibrates acting on lipoprotein lipase. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` `(→ Instance)` Ion-Channel Modulation | Opening or blocking a channel — local anaesthetics on voltage-gated sodium channels. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` `(→ Instance)` Transporter Blockade | Blocking or reversing a carrier — SSRIs on the serotonin transporter. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` `(→ Instance)` Nucleic-Acid Interference | Damaging or silencing DNA and RNA — alkylating chemotherapy, antisense oligonucleotides, siRNA. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` `(→ Instance)` Membrane Disruption | Changing membrane permeability or integrity — amphotericin B binding ergosterol, osmotic diuretics such as mannitol. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Mechanism` `(→ Instance)` Physical Neutralisation | Acting without a molecular target — antacids neutralising gastric acid. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Property` | Grouping: the pharmacological properties by which the substance is characterised. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Property` `(→ Instance)` Potency | The dose needed for the effect, read from the concentration–response curve. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Property` `(→ Instance)` Selectivity | The margin between the intended target and the others the substance also binds. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Property` `(→ Instance)` Half-Life | The time for the plasma concentration to halve — what fixes the dosing interval. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Property` `(→ Instance)` Therapeutic Index | The ratio of the toxic to the effective dose — the measure of how much room the drug has. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Has)` `Technical Property` `(→ Instance)` Lipophilicity | The octanol–water partition that governs absorption and membrane crossing; Lipinski's rule of five bounds it for oral drugs. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Governed By)` `Technical Standard` | Grouping: the standards that govern the substance. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Governed By)` `Technical Standard` `(→ Instance)` Pharmacopoeial Monograph | The identity, assay and impurity tests the substance must pass — USP, Ph. Eur., JP. |
| `Technical Element` `(→ Kind)` `Production Technical Object` `(→ Part)` `Constitutive Technical Object` `(→ Instance)` Drug `(→ Governed By)` `Technical Standard` `(→ Instance)` Controlled-Substance Schedule | The legal schedule that fixes how the substance may be prescribed, dispensed and stored. |

### What is a critical conceptual evaluation of this `technical element instance`?

The concept under evaluation is **Drug**, defined above as *the active principle of a medicine: a substance that binds a molecular target and changes what that target does*. The evaluation applies the criteria of [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md).

**Verdicts.** Conceptual Identification — **pass**: separated from the fine chemical (same molecule, read by specification), the pharmaceutical product (the formulated article) and the vaccine (an immune intervention rather than a target-binding substance) by the definition's own test. Definitional Clarity — **pass**: the definition names the relation (binding a target), not a property of the molecule, so it is checkable. Conceptual Determinacy — **pass with qualification**: "drug" is a functional category, so a substance can enter and leave it with the indication and the dose; the definition avoids the problem by making the target relation the criterion rather than the substance class. Internal Consistency — **pass**: the target classes and the mechanism rows are the same classification read from two sides. Representational Adequacy — **pass**: covers the substance kinds, the mechanisms, the properties and the governing standards, and stops at the physiology it acts on. Purpose Adequacy — **pass**: every leaf is a substance kind, a mechanism, a property or a standard — usable as a pharmacology checklist.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | pass | Distinguished from fine chemical (specification), pharmaceutical product (article) and vaccine (immune mechanism). |
| Definitional Clarity | pass | The definition is relational — binding a target and changing it — and therefore testable. |
| Conceptual Determinacy | qualified | Membership is functional, so a substance can move in and out with indication and dose; the target relation is the criterion, not the substance class. |
| Internal Consistency | pass | The six target classes of the table and the mechanism rows of the tree are one classification read from two sides. |
| Representational Adequacy | pass | Substance kinds, mechanisms, properties and standards are present; the physiology acted on is left to its own notes. |
| Purpose Adequacy | pass | Leaves resolve to kinds, mechanisms, properties and standards — directly usable as a pharmacology checklist. |

## References

- [Drug](https://en.wikipedia.org/wiki/Drug) (the substance definition and the pharmacological reading)
- [Active ingredient](https://en.wikipedia.org/wiki/Active_ingredient) (the API reading of the same substance)
- [Pharmacodynamics](https://en.wikipedia.org/wiki/Pharmacodynamics) (the target classes and the concentration–response relation)
- Lipinski, C. A., Lombardo, F., Dominy, B. W., & Feeney, P. J. (1997). Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings. *Advanced Drug Delivery Reviews, 23*(1–3), 3–25. https://doi.org/10.1016/S0169-409X(96)00423-1
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) (schema owner)
- [Philosophia Conceptuum et Operis](/view.html?p=notes/philosophia-conceptuum-et-operis.md) (evaluation criteria)

## Related

- [Fine Chemical](/view.html?p=notes/technica/general/cto/industry/fine-chemical.md) — the same substance read by its specification rather than its action.
- [Pharmaceutical Product](/view.html?p=notes/technica/general/cto/industry/pharmaceutical-product.md) — the formulated article the drug is delivered in.
- [Pharmaceutical Pipeline](/view.html?p=notes/technica/general/cto/industry/pharma-pipeline.md) — the regulated system that turns the molecule into a medicine.
- [Human](/view.html?p=notes/nature/human/human.md) — the organism the drug acts on.
- [Neuron](/view.html?p=notes/nature/human/neuron.md) — the cell whose channels, receptors and transporters most drugs target.
- [Synapse in Nervous System](/view.html?p=notes/nature/human/synapse-in-nervous-system.md) — where the receptor and transporter targets sit.
