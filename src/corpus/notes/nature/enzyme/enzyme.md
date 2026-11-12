---
tags: [note, nature, substance-matter, biology, biomaterial, matter, enzyme]
qa:
 - Is an enzyme a substance or a process?
 - What makes a biocatalyst a catalyst, and what makes it more than one?
 - Why can an enzyme accelerate a reaction enormously and still fail at the wrong pH?
 - Does the active site fit the substrate, or does it fit the transition state?
 - What does the EC number classify — the enzyme, or the reaction?
 - What survives of "vital force" after Buchner ground up yeast?
---

# Enzyme

> **Enzymes** are proteins — in a few cases RNA — that catalyse the reactions of living chemistry. They are not consumed by the reaction they accelerate, they act at ordinary temperature and pressure in water, and they do so with a specificity and a rate acceleration that no synthetic catalyst of comparable size matches. The word is a compromise: *enzyme* means "in yeast", and for thirty years after its coinage the people who studied enzymes did not believe they were proteins at all.

## Formulation

### What natural element type does this enzyme instance belong to?

**An enzyme, read as a natural instance, belongs to `Ontic Element (→ Kind) Substance (→ Kind) Substance / Matter` — a stuff-kind individuated by composition, and by the arrangement of that composition in a pocket that catalyses.**

It is also an instance of `Entity` when a single molecule is counted or tracked, which is what "one enzyme molecule" names. Readable secondarily as a `Building Block` — the unit a metabolic pathway or a regulatory network is assembled from, which is how the [Human Biomolecular Architecture](/view.html?p=notes/nature/human/biomolecular-architecture.md) note meets it. Readable again as a `Mechanism`, since an enzyme *causes* conversion; but the enzyme is the bearer of the causing, not the causing itself, so the mechanism reading stays prose. Those readings are prose here, not second roots.

### What is this natural instance?

> An enzyme is a folded polypeptide — or, in the ribozymes, a folded RNA — whose tertiary structure brings a small set of residues into a specific spatial arrangement, the **active site**, such that a particular reaction proceeds there far faster than it would in solution. Everything else about the enzyme follows from that: the specificity is the shape of the pocket, the rate is the stabilisation of the transition state inside it, and the regulation is the ability of other molecules to change that pocket's shape or accessibility from a distance.
>
> The enzyme is a **substance, not a process**. It persists between turnovers, it can be purified, crystallised and weighed, and it can be present in a cell while being catalytically silent. The catalysis it performs is a process the substance participates in — which is exactly why this note's decomposition attributes the conversion to an `(→ Occurrence)` row while the enzyme itself is decomposed as a thing.
>
> One boundary of the type is worth stating because the classification section below gets mistaken for it. **The seven EC classes are a taxonomy over enzymes, not parts of an enzyme.** No enzyme contains a "hydrolase part"; a hydrolase *is* an enzyme whose catalytic arrangement happens to cleave a bond with water. The classes therefore belong in the taxonomy, not in the decomposition — this note's tree decomposes one enzyme, and the section that follows classifies the family.

### What is the recursive instance decomposition of this natural instance?

> Boundary: one enzyme — its chain or chains, the active site and what is in it, the catalytic chemistry those produce, the regulation interfaces on its surface, the turnover cycle it runs, and the properties that follow. The substrate, the product, the pathway the enzyme belongs to and the cell that expresses it are associated, not parts.
>
> Stopping rule: a row is terminal when it names a structural feature, a catalytic mode, a step, or a kinetic parameter whose own decomposition lives elsewhere.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the residue and the bond are **micro**; the folded chain, the active site and the turnover cycle are **meso**. Limitation checklist for the segment: **Many-Body coupling** (the fold is a property of thousands of coupled interactions), **Partial Observability** (the transition state is inferred, never observed; intermediate states are short-lived), **Non-Repeatability** (a single turnover is a one-off event, only the ensemble is reproducible), **Scale**.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme | Bound root instance: a folded macromolecule that catalyses a reaction at its active site. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` | Grouping: the structural constituents of one enzyme. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Polypeptide Chain | The folded chain — or chain set, when the enzyme is a multimer. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Polypeptide Chain `(→ Part)` `Building Block` | Grouping: the structural levels of the chain. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Polypeptide Chain `(→ Part)` `Building Block` `(→ Instance)` Amino Acid Sequence | The primary structure that the fold is determined by. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Polypeptide Chain `(→ Part)` `Building Block` `(→ Instance)` Tertiary Fold | The three-dimensional arrangement that brings the catalytic residues together from distant points on the sequence. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Active Site | The pocket in which the reaction is catalysed. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Active Site `(→ Part)` `Building Block` | Grouping: the components of the site. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Active Site `(→ Part)` `Building Block` `(→ Instance)` Catalytic Residues | The few side chains that perform the chemistry. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Active Site `(→ Part)` `Building Block` `(→ Instance)` Binding Pocket | The geometry that selects and holds the substrate. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Active Site `(→ Part)` `Building Block` `(→ Instance)` Cofactor or Prosthetic Group | Any non-amino-acid species the chemistry needs — a metal ion, a coenzyme, a tightly bound organic group. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Part)` `Natural Object` `(→ Instance)` Regulation Interface | The surface sites through which other molecules change the enzyme's behaviour. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Component)` `Mechanism` | Grouping: the catalytic means the site provides. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Component)` `Mechanism` `(→ Instance)` Transition-State Stabilisation | Binding the activated complex more tightly than the ground state — the source of the rate acceleration. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Component)` `Mechanism` `(→ Instance)` Acid–Base Catalysis | Donating and accepting protons at the right moment through ionisable side chains. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Component)` `Mechanism` `(→ Instance)` Metal-Ion Catalysis | Lewis-acid and redox chemistry supplied by a bound metal. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Occurrence)` `Natural Process` | Grouping: the cycle the enzyme runs. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Occurrence)` `Natural Process` `(→ Instance)` Catalytic Turnover | One passage of the enzyme through substrate binding, chemical step and product release. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Occurrence)` `Natural Process` `(→ Instance)` Induced Fit | The conformational change on binding that lets the site close around the substrate. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Attribute)` `Property` | Grouping: the properties that follow from structure and mechanism. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Attribute)` `Property` `(→ Instance)` k_cat | The catalytic constant — maximum turnovers per second when saturated. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Attribute)` `Property` `(→ Instance)` K_m | The substrate concentration at which the rate is half its maximum. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Attribute)` `Property` `(→ Instance)` Stereospecificity | Discrimination between mirror-image substrates, which the lock-and-key image was coined to explain. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Situation)` `Environment` | The conditions the enzyme works in and is sensitive to. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Instance)` Enzyme `(→ Situation)` `Environment` `(→ Instance)` Cellular Compartment | Where the enzyme is, which decides what it can meet. |

## What is an enzyme?

An enzyme is a **catalyst that is a macromolecule**. The catalyst part is straightforward: it lowers the activation energy of a reaction by providing a path through a stabilised transition state, and it emerges unchanged afterwards. The macromolecule part is what makes it biological: it is a folded chain whose shape, and the arrangement of a few residues in a pocket on that shape, is what does the catalysis.

That pocket is the **active site**. It binds the substrate, holds it in the geometry the reaction needs, and — on the account Pauling gave in 1948 — it is complementary not to the substrate but to the transition state the substrate must become. The enzyme is not a template for what the molecule is; it is a template for what the molecule is about to be.

Enzymes are also **regulated**. A catalyst that ran flat out whenever its substrate appeared would be useless to a cell; enzyme activity is switched by allosteric binding, by covalent modification, by proteolytic activation and by compartmentalisation. The note [Enzyme Regulation](/view.html?p=notes/nature/enzyme/enzyme-regulation.md) takes that side.

## What types of enzyme exist?

The International Union of Biochemistry and Molecular Biology classifies every enzyme by the reaction it catalyses, and issues each a four-part **EC number** whose first part is the class. There are **seven** classes. Six have been in place since the first Enzyme List of 1961; the seventh, **Translocases**, was added in 2018, because none of the existing six could describe enzymes whose job is to move ions or molecules across a membrane — they had been filed as ATPases under the hydrolytic class, which misdescribed what they do.

| Class | Name | Reaction catalysed | Typical examples |
| --- | --- | --- | --- |
| **EC 1** | Oxidoreductases | Electron transfer: AH₂ + B → A + BH₂ | Dehydrogenases, oxidases, peroxidases, catalase |
| **EC 2** | Transferases | Group transfer: AX + B → BX + A | Kinases (phosphate), aminotransferases (amino groups), glycosyltransferases |
| **EC 3** | Hydrolases | Bond cleavage by water: A–B + H₂O → AH + BOH | Proteases, amylases, lipases, phosphatases, nucleases |
| **EC 4** | Lyases | Bond cleavage *without* water or oxidation, often making a double bond or a ring | Decarboxylases, aldolases, RuBisCO (the carbon-fixing enzyme) |
| **EC 5** | Isomerases | Intramolecular rearrangement: A → B | Glucose isomerase, mutases, racemases, protein disulfide isomerase |
| **EC 6** | Ligases | Joining two molecules, paid for by NTP hydrolysis | DNA ligase, aminoacyl-tRNA synthetases, ubiquitin ligases |
| **EC 7** | Translocases | Movement of a solute across a membrane, side 1 → side 2 | ATP synthases, ion pumps, ABC transporters |

Three details are worth keeping. First, **RuBisCO is a lyase, not a ligase** — it fixes carbon dioxide onto ribulose bisphosphate by a cleavage-and-addition step, not by coupling to ATP — and it is the most abundant enzyme on Earth. Second, **lyases and ligases are easy to confuse by name**: a lyase *breaks* a bond without water, a ligase *forms* one and pays for it. Third, **the EC number classifies the reaction, not the protein**: an enzyme that evolves a second activity may be renumbered, and old numbers are retired rather than reused.

## History of the concept

> The literature is read in year order here, because the idea of the enzyme was built and then dismantled twice: first when it was declared that a catalyst could work without the organism being alive, and later when the catalyst turned out to be a protein.

- **1833 — the first preparation.** Payen and Persoz isolated from malt a substance that liquefied starch and called it *diastase*: the first enzyme separated, sixty years before anyone knew what enzymes were made of.
- **1878 — the word.** Kühne coined *enzyme* ("in yeast") to distinguish the separable catalysts from the living organism that produced them.
- **1894 — the lock and the key.** Fischer explained the stereospecificity of enzymes with the image that enzyme and substrate must fit "like lock and key" — a rigid complementarity, which stood for sixty years.
- **1897 — not alive.** Buchner ground brewer's yeast with sand and pressed out a cell-free juice that fermented sugar to alcohol. *Zymase* worked outside the cell, and with it the vitalist claim that fermentation required a living organism collapsed. "Enzyme" stopped meaning a property of yeast and started meaning a substance.
- **1903–1913 — kinetics.** Henri derived the rate law for an enzyme–substrate complex from mass action; Michaelis and Menten simplified and demonstrated it on invertase. The equation that bears their names is more properly the **Henri–Michaelis–Menten** equation, and their own paper cites Henri.
- **1925 — the equation fixed.** Briggs and Haldane replaced Michaelis and Menten's rapid-equilibrium assumption with the **steady-state** approximation, which is the derivation textbooks now teach.
- **1926–1930 — enzymes are proteins.** Sumner crystallised urease and said so; Northrop and Kunitz crystallised pepsin, then trypsin, and the protein nature of enzymes became consensus. Sumner and Northrop shared the Nobel Prize in 1946.
- **1948 — why catalysis works.** Pauling proposed that enzymes bind the **transition state** more tightly than the substrate, so that the energy barrier is lowered by the binding energy itself.
- **1958 — the key bends.** Koshland's induced-fit model let the active site reshape on binding, which also explained how subunits in one complex could talk to one another.
- **1963–1970 — control.** Monod, Changeux and Jacob, then Monod, Wyman and Changeux, gave allostery its first formal model; Perutz gave haemoglobin its stereochemical mechanism in 1970.
- **1961–2018 — the taxonomy.** The Enzyme List of 1961 fixed six classes; EC 7 was added in 2018.

## Enzyme Space

| Enzyme | Enzyme class | Catalytic activity | Typical substrate | Product | Biological role |
|---|---|---|---|---|---|
| Amylase | Hydrolase | Starch hydrolysis | Starch | Maltose, oligosaccharides | Carbohydrate digestion |
| Pepsin | Hydrolase | Protein hydrolysis | Proteins | Peptides | Protein digestion |
| Trypsin | Hydrolase | Peptide bond hydrolysis | Polypeptides | Smaller peptides | Protein digestion |
| Lipase | Hydrolase | Ester bond hydrolysis | Triglycerides | Fatty acids, glycerol | Lipid digestion |
| Lactase | Hydrolase | Glycosidic bond hydrolysis | Lactose | Glucose, galactose | Lactose digestion |
| Sucrase | Hydrolase | Glycosidic bond hydrolysis | Sucrose | Glucose, fructose | Carbohydrate digestion |
| Catalase | Oxidoreductase | Hydrogen peroxide decomposition | Hydrogen peroxide | Water, oxygen | Oxidative protection |
| Peroxidase | Oxidoreductase | Peroxide reduction | Hydrogen peroxide, electron donor | Water, oxidized donor | Oxidative protection |
| Cytochrome c oxidase | Oxidoreductase | Electron transfer to oxygen | Electrons, oxygen | Water | Cellular respiration |
| Hexokinase | Transferase | Phosphoryl group transfer | Glucose, ATP | Glucose-6-phosphate, ADP | Glycolysis |
| DNA polymerase | Transferase | DNA chain synthesis | DNA template, dNTPs | DNA | DNA replication |
| RNA polymerase | Transferase | RNA chain synthesis | DNA template, NTPs | RNA | Transcription |
| Pyruvate kinase | Transferase | Phosphoryl group transfer | Phosphoenolpyruvate, ADP | Pyruvate, ATP | Glycolysis |
| Carbonic anhydrase | Lyase | Reversible CO₂ hydration | CO₂, water | Bicarbonate, protons | CO₂ transport and pH regulation |
| Aldolase | Lyase | Carbon–carbon bond cleavage | Fructose-1,6-bisphosphate | Glyceraldehyde-3-phosphate, DHAP | Glycolysis |
| Fumarase | Lyase | Reversible hydration | Fumarate, water | Malate | Citric acid cycle |
| Citrate synthase | Transferase | Carbon–carbon bond formation | Acetyl-CoA, oxaloacetate | Citrate | Citric acid cycle |
| Phosphoglucomutase | Isomerase | Intramolecular phosphate transfer | Glucose-1-phosphate | Glucose-6-phosphate | Carbohydrate metabolism |
| Triose phosphate isomerase | Isomerase | Aldose–ketose interconversion | DHAP | Glyceraldehyde-3-phosphate | Glycolysis |
| Protein disulfide isomerase | Isomerase | Disulfide bond rearrangement | Proteins with disulfide bonds | Rearranged protein disulfide bonds | Protein folding |
| Ubiquitin ligase | Ligase | Covalent bond formation | Ubiquitin, target protein | Ubiquitinated protein | Protein degradation regulation |
| DNA ligase | Ligase | Phosphodiester bond formation | DNA fragments | Joined DNA | DNA replication and repair |
| Glutamine synthetase | Ligase | ATP-dependent amide bond formation | Glutamate, ammonia | Glutamine | Nitrogen metabolism |

## QA

**Is an enzyme a substance or a process?** A substance. It is a folded macromolecule with mass, structure and a lifetime spanning many turnovers; it can be purified and crystallised, and it can sit in a cell catalytically silent. The catalysis it performs is a process the substance runs, which is why the decomposition above gives the conversion an `(→ Occurrence)` row rather than typing the enzyme as a process.

**What makes a biocatalyst a catalyst, and what makes it more than one?** It is a catalyst in the ordinary sense: it accelerates a reaction without being consumed, by lowering the barrier through transition-state stabilisation. It is *more* than a catalyst in three respects — it is **specific** (it selects among similar substrates), it is **regulated** (its own activity is switched by molecules that are not its substrate), and it is **synthesised**, so its activity and its abundance are separately controlled. A synthetic catalyst has none of the last three.

**Does the EC class belong in the decomposition?** No. The seven classes are a taxonomy over enzymes, not parts of one, and the section above carries them. An enzyme does not contain a "hydrolase part"; it is a hydrolase because of what its active site does.


## References

- [Protein](/view.html?p=notes/nature/bio/molecular/protein.md)
- [Enzyme Regulation](/view.html?p=notes/nature/enzyme/enzyme-regulation.md)
- [Enzyme Catalysis](/view.html?p=notes/nature/enzyme/enzyme-catalysis.md)
- [Enzyme Activity / Kinetics (E, kcat, Km)](/view.html?p=notes/nature/enzyme/enzyme-activity-kinetics-e-kcat-km.md)
- [Enzyme Assays](/view.html?p=notes/nature/enzyme/enzyme-assays.md)
- [Glucose](/view.html?p=notes/nature/bio/molecular/glucose.md)
- [Starch](/view.html?p=notes/nature/bio/molecular/starch.md)
- [RuBisCO](https://en.wikipedia.org/wiki/RuBisCO)

- https://enzyme.expasy.org/
- https://www.brenda-enzymes.org/
- https://www.rhea-db.org/


- Payen, A., & Persoz, J.-F. (1833). Mémoire sur la diastase, les principaux produits de ses réactions et leurs applications aux arts industriels. *Annales de Chimie et de Physique, 53*, 73–92.
- Fischer, E. (1894). Einfluss der Configuration auf die Wirkung der Enzyme. *Berichte der Deutschen Chemischen Gesellschaft, 27*(3), 2985–2993. https://doi.org/10.1002/cber.18940270364
- Buchner, E. (1897). Alkoholische Gährung ohne Hefezellen (Vorläufige Mitteilung). *Berichte der Deutschen Chemischen Gesellschaft, 30*, 117–124. https://doi.org/10.1002/cber.18970300121
- Henri, V. (1903). *Lois générales de l'action des diastases*. Librairie Scientifique A. Hermann.
- Michaelis, L., & Menten, M. L. (1913). Die Kinetik der Invertinwirkung. *Biochemische Zeitschrift, 49*, 333–369.
- Briggs, G. E., & Haldane, J. B. S. (1925). A note on the kinetics of enzyme action. *Biochemical Journal, 19*(2), 338–339. https://doi.org/10.1042/bj0190338
- Sumner, J. B. (1926). The isolation and crystallization of the enzyme urease. *Journal of Biological Chemistry*. [Unverified: volume and pages]
- Northrop, J. H. (1930). Crystallization of pepsin. *Science*. [Unverified: volume and pages]
- Pauling, L. (1948). Nature of forces between large molecules of biological interest. *Nature, 161*(4097), 707–709. https://doi.org/10.1038/161707a0
- Koshland, D. E., Jr. (1958). Application of a theory of enzyme specificity to protein synthesis. *Proceedings of the National Academy of Sciences, 44*(2), 98–104. https://doi.org/10.1073/pnas.44.2.98
- Monod, J., Changeux, J.-P., & Jacob, F. (1963). Allosteric proteins and cellular control systems. *Journal of Molecular Biology, 6*, 306–329.
- Monod, J., Wyman, J., & Changeux, J.-P. (1965). On the nature of allosteric transitions: A plausible model. *Journal of Molecular Biology, 12*(1), 88–118. https://doi.org/10.1016/S0022-2836(65)80285-6
- Perutz, M. F. (1970). Stereochemistry of cooperative effects in haemoglobin: Haem–haem interaction and the problem of allostery. *Nature, 228*(5273), 726–734. https://doi.org/10.1038/228726a0
- McDonald, A. G., & Tipton, K. F. (2023). Enzyme nomenclature and classification: The state of the art. *The FEBS Journal, 190*(9), 2214–2231. https://doi.org/10.1111/febs.16274
- Tipton, K. (2018). Translocases (EC 7): A new EC class. *Enzyme Nomenclature News*. International Union of Biochemistry and Molecular Biology.


