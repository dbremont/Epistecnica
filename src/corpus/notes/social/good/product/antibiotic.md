---
tags: [note, social, pharma, drug, antibiotic, antimicrobial, medicine]
qa:
 - Is an antibiotic defined by what it is made of, by what it kills, or by how it kills?
 - Why does selectivity — a target the human cell does not have — matter more for antibiotics than for any other drug class?
 - Is resistance a failure of the drug or a consequence of using it?
 - Why is a broad-spectrum antibiotic not automatically better than a narrow one?
---

# Antibiotic

> An **antibiotic** is a drug that kills or inhibits bacteria by acting on a target the bacterial cell has and the human cell does not: the cell wall, the bacterial ribosome, the bacterial topoisomerase, the folate pathway, the bacterial membrane or the bacterial RNA polymerase. It is a **class defined by action**, not by structure — a β-lactam, an aminoglycoside and a quinolone share almost no chemistry, and share the property that matters.

> The class is the clearest case in pharmacology of a drug whose effect is not only on the patient. Every dose selects the bacteria that survive it, so the antibiotic is a common-pool resource consumed by use: the more it is used, the less it works, and the cost falls on everyone who needs it later.

## Formulation

### What technical element type does this technical instance belong to?

**An antibiotic belongs to the `Constitutive Technical Object` technical element type — a kind of drug substance, the active principle of an antibacterial pharmaceutical product.**

It is constitutive because the substance is what carries the action and is never delivered alone: it is formulated, dosed and prescribed, and the product is what the patient receives. Readable secondarily as a `Technical Element Set` when the class is read as an arsenal — the families, the spectrum, the stewardship rule and the resistance surveillance are distinct elements held together by one purpose. Those readings are prose here, not additional roots.

It is distinct from a **fine chemical** (the same molecule read by its specification), from a **pharmaceutical product** (the formulated article), and from a **disinfectant** (a biocide applied outside the body, with no selective target and no systemic dose).

### What is this technical instance?

> The antibacterial families — natural, semisynthetic and synthetic — read by their mechanism: the β-lactams that stop the cell wall from cross-linking, the glycopeptides that bind its precursor, the aminoglycosides and tetracyclines and macrolides that stop the ribosome at different sites, the quinolones that trap the DNA-enzyme complex, the sulfonamides that block the folate pathway, the polymyxins that disrupt the membrane, and the oxazolidinones and rifamycins that stop transcription. Each family has a spectrum, a route, a toxicity and a resistance profile, and the choice among them is a decision about the pathogen, the site and the patient.

### What is the recursive instance decomposition of this technical instance?

> Boundary: the drug class — its kinds by mechanism, the properties by which a member is chosen, the mechanism it runs, and the population-and-prescriber bound that makes resistance a property of the class rather than of the molecule. The formulation and the disease are separate elements.
>
> Stopping rule: a row is terminal when it names a family, a mechanism, a measured property or a named bound.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.
>
> Verbs: the drug *inhibits* its target; the prescriber *selects* the family; the population *selects* the resistant variant.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technical Object` → Antibiotic | The antibacterial drug class, defined by a target absent in the human cell. |
| `Constitutive Technical Object` → Antibiotic → `Constitutive Technical Object` | Grouping: the families, read by mechanism. |
| `Constitutive Technical Object` → Antibiotic → `Constitutive Technical Object` → Cell-Wall Synthesis Inhibitor | β-lactams and glycopeptides: the wall is built, cross-linked or bound, and the cell lyses. |
| `Constitutive Technical Object` → Antibiotic → `Constitutive Technical Object` → Ribosome Inhibitor | Aminoglycosides, tetracyclines, macrolides, lincosamides and oxazolidinones: protein synthesis stops at a bacterial-specific site. |
| `Constitutive Technical Object` → Antibiotic → `Constitutive Technical Object` → Nucleic-Acid Synthesis Inhibitor | Quinolones and rifamycins: replication and transcription are blocked. |
| `Constitutive Technical Object` → Antibiotic → `Constitutive Technical Object` → Folate Pathway Inhibitor | Sulfonamides and trimethoprim: the bacterial folate synthesis route is interrupted. |
| `Constitutive Technical Object` → Antibiotic → `Constitutive Technical Object` → Membrane Disruptor | Polymyxins and daptomycin: the bacterial membrane is made permeable. |
| `Constitutive Technical Object` → Antibiotic → `Technical Mechanism` | Grouping: how the family produces its effect. |
| `Constitutive Technical Object` → Antibiotic → `Technical Mechanism` → Selective Toxicity | The target exists in the bacterium and not in the human cell — the property the whole class depends on. |
| `Constitutive Technical Object` → Antibiotic → `Technical Mechanism` → Bactericidal Action | The drug kills rather than merely arrests growth — required where host defence cannot clear the infection. |
| `Constitutive Technical Object` → Antibiotic → `Technical Mechanism` → Bacteriostatic Action | The drug arrests growth and leaves clearance to the immune system — sufficient, and sometimes preferable, in the right site. |
| `Constitutive Technical Object` → Antibiotic → `Technical Parameter` | Grouping: the properties by which a member is chosen. |
| `Constitutive Technical Object` → Antibiotic → `Technical Parameter` → Spectrum | The range of organisms covered — narrow, broad, Gram-positive, Gram-negative, anaerobic, mycobacterial. |
| `Constitutive Technical Object` → Antibiotic → `Technical Parameter` → Pharmacokinetics | Absorption, distribution, metabolism and excretion — what decides the dose and the interval. |
| `Constitutive Technical Object` → Antibiotic → `Technical Parameter` → Tissue Penetration | Whether the drug reaches the site of infection — the reason a susceptible organism can still fail to respond. |
| `Constitutive Technical Object` → Antibiotic → `Technical Parameter` → Toxicity | The adverse effects that limit the dose — renal, hepatic, neurological, haematological. |
| `Constitutive Technical Object` → Antibiotic → `Technical Constraint` | Grouping: the bounds the class works inside. |
| `Constitutive Technical Object` → Antibiotic → `Technical Constraint` → Resistance | The heritable loss of susceptibility, selected by use and transferred between organisms. |
| `Constitutive Technical Object` → Antibiotic → `Technical Constraint` → Resistance Gene Pool | The shared reservoir of resistance determinants that makes one drug's use affect another's usefulness. |
| `Constitutive Technical Object` → Antibiotic → `Technical Constraint` → Stewardship | The prescribing rule that treats the drug as a common-pool resource rather than a private one. |

## The Families

| Family | Representative | Target | Spectrum | Character |
| --- | --- | --- | --- | --- |
| **Penicillins** | Amoxicillin, benzylpenicillin | Cell-wall transpeptidase | Narrow to moderate; many Gram-positive | The original β-lactam; β-lactamase is its recurring defeat |
| **Cephalosporins** | Ceftriaxone, cefepime | Cell-wall transpeptidase | Broad, generation-dependent | The hospital workhorses |
| **Carbapenems** | Meropenem | Cell-wall transpeptidase | Very broad | Reserved for resistant Gram-negatives |
| **Glycopeptides** | Vancomycin | Cell-wall precursor | Gram-positive only | The MRSA standard, with a narrow margin |
| **Aminoglycosides** | Gentamicin | 30S ribosome | Gram-negative aerobes | Concentration-dependent killing; nephro- and ototoxic |
| **Tetracyclines** | Doxycycline | 30S ribosome | Broad | Cheap, oral, and increasingly resisted |
| **Macrolides** | Azithromycin | 50S ribosome | Atypical and Gram-positive | The respiratory standby |
| **Lincosamides** | Clindamycin | 50S ribosome | Gram-positive and anaerobes | Good tissue penetration; colitis risk |
| **Oxazolidinones** | Linezolid | 50S initiation complex | Gram-positive | Reserved for resistant Gram-positives |
| **Quinolones** | Ciprofloxacin | DNA gyrase / topoisomerase IV | Broad | Potent, and constrained by serious adverse effects |
| **Sulfonamides / trimethoprim** | Co-trimoxazole | Folate pathway | Moderate | The classic sequential blockade |
| **Nitroimidazoles** | Metronidazole | Anaerobic DNA | Anaerobes and protozoa | The anaerobic workhorse |
| **Polymyxins** | Colistin | Membrane lipopolysaccharide | Gram-negative | The last line, and nephrotoxic |
| **Rifamycins** | Rifampicin | RNA polymerase | Mycobacteria and Gram-positives | Used in combination to protect it |

## Selectivity

> The reason antibiotics work is that their targets are bacterial: the peptidoglycan wall does not exist in human cells, the bacterial ribosome differs enough from the human one that a drug can bind it selectively, and the folate-synthesis pathway is absent in humans, who obtain folate from the diet. Selectivity is not a bonus property of the class; it is the definition of a useful antibiotic, and the drug that loses it is a toxin.

> Selectivity also explains the limits. A drug with no human analogue can be very safe and still fail, because the target can be intracellular, the drug may not penetrate an abscess, or the organism may be in a biofilm where the drug cannot reach it. The clinical failure of a "sensitive" organism is usually a pharmacology problem, not a resistance problem.

## Spectrum

| Spectrum | Covers | Cost of using it |
| --- | --- | --- |
| **Narrow** | One genus or group | Requires an accurate diagnosis; spares the flora |
| **Extended** | Gram-positive and some Gram-negative | The usual empirical compromise |
| **Broad** | Gram-positive, Gram-negative, often anaerobes | Collateral damage to the microbiome and the resistance pool |
| **Reserved** | Last-line agents for resistant organisms | Toxicity, cost, and the duty to keep them useful |

> Broad is not better. An empirical broad-spectrum drug is a decision made before the diagnosis, and it should be narrowed when the culture returns — the practice called de-escalation. Every unnecessary broad-spectrum day selects resistance in the patient's own flora and feeds the shared gene pool.

## Resistance

> Resistance is not an accident that happens to a drug; it is the predictable result of using it. Four mechanisms recur, and most are transferable:

| Mechanism | How it works | Example |
| --- | --- | --- |
| **Enzymatic inactivation** | The drug is destroyed before it reaches the target | β-lactamases against penicillins |
| **Target modification** | The target is mutated or replaced so the drug no longer binds | Ribosomal methylation; altered penicillin-binding proteins |
| **Reduced accumulation** | Efflux pumps expel the drug, or the membrane admits less of it | Efflux in *Pseudomonas*; porin loss in *Klebsiella* |
| **Bypass** | The organism acquires an alternative pathway | Acquired folate-synthesis enzymes |

> The determinants travel on plasmids, transposons and integrons, so resistance selected by one drug can disable another that shares the mechanism. That is why the constraint is stated on the **class** rather than on the molecule, and why agricultural use of antibiotics — a large share of global consumption — is part of the same problem.

## Stewardship

> The antibiotic is a **common-pool resource**: rival in use, non-excludable in benefit, and depleted by the use that consumes it. The stewardship rule follows: use the narrowest effective agent, at the right dose and duration, after the diagnosis, and reserve the last-line drugs for the organisms that need them. It is an unusual technical rule because it asks the prescriber to accept a cost now for a benefit that falls on someone else later.

> The pipeline compounds it. A new antibiotic is expensive to develop and, once approved, is deliberately used as little as possible — the opposite of the commercial incentive that pays for the development. That mismatch, not the biology, is why the class is short of new mechanisms.

## References

- [Antibiótico](https://es.wikipedia.org/wiki/Antibi%C3%B3tico)
- [Antibiotic](https://en.wikipedia.org/wiki/Antibiotic)
- [Antimicrobial resistance](https://en.wikipedia.org/wiki/Antimicrobial_resistance)
- [Beta-lactam antibiotic](https://en.wikipedia.org/wiki/Beta-lactam_antibiotic) · [Aminoglycoside](https://en.wikipedia.org/wiki/Aminoglycoside) · [Quinolone antibiotic](https://en.wikipedia.org/wiki/Quinolone_antibiotic)
- [Drug](/view.html?p=notes/social/good/product/drug.md) — the class this note specializes
- [Pharmaceutical Product](/view.html?p=notes/social/good/product/pharmaceutical-product.md) — the formulated article the antibiotic is delivered in
- [Pathogen](/view.html?p=notes/nature/life/organism/pathogen.md) — the target population, and why it evolves
- [Discovery of Penicillin](/view.html?p=notes/epistemica/observation/experiment/discovery-of-penicillin.md) — the experiment that opened the class
- [Fine Chemical](/view.html?p=notes/social/good/product/fine-chemical.md) — the substance read by its specification instead of its action
- [Health Industry](/view.html?p=notes/technica/production/industry/health/health-industry.md) — the production system behind the class
