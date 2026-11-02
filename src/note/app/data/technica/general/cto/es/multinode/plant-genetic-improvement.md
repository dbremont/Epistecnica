---
tags: [plant, breeding, genetics, genome-editing]
---

# Plant Genetic Improvement

> **Plant Genetic Improvement** is the set of practices that turns germplasm into a new variety. It is not one method: breeding, marker and genomic tooling, transformation, genome editing, testing, seed production, and the regulation that admits the lot are separate practices held together by one purpose, and any of them alone yields no sellable variety. Framing: the Spanish encyclopedia article [Mejoramiento genético](https://es.wikipedia.org/wiki/Mejoramiento_gen%C3%A9tico) — increase productivity, resistance, adaptation and product quality by modifying the genotype, managing genetic resources by selection, and conserving long-term variability. That article carries a maintenance banner for missing published references, so it is used here as orientation and every technical claim is anchored in the literature listed in [References](#references); its bibliography is the source of the historical works below.
>
> The plant half of the article's scope is the cut: animal breeding is out. What is also out: the crop regime the variety is planted into ([Plant Cultivation](note.html?n=technica/general/cto/es/multinode/plant-cultivation-technical-domain-set.md)), the inquiry that warrants knowing the genotype and the phenotype ([Agricultural Science](note.html?n=epistemica/discipline/agricultural-science.md)), and the institutions that own and certify the seed (social, not technical here). The plant as a living system is natural; this note decomposes the apparatus that changes it, not the organism (Ambiguity Resolution (`guideline/ambiguity_resolution.md`)).

## Formulation

### What technical element type does this technical instance belong to?

**Plant Genetic Improvement belongs to the `Technical Element Set` technical element type — a collection of technical elements scoped to one bounded field, which here is the production of a new variety.**

```text
Technical Element Set
└── Plant Genetic Improvement (bounded field: turn germplasm into a released variety)
```

The taxonomy defines no `Technical Practice Set` or `Improvement` type: such names are generic composites, and the generic type is `Technical Element Set`, whose specific semantics are carried by the particular set rather than by the type. It is a set and not a single `General Technique` because a crossing, an editor, a trial network, and a seed plant are different technical element types that only co-operate inside the program that holds them. The `Technical Element Set` grouping below the root is admitted by the No-repetition exception: it scopes the instance family of the eight practice sets that would otherwise hang untyped off the root's own segment, and it appears exactly once.

Its members are of different types by necessity — `General Technique` crossing and editing, `Constitutive Technical Object` vectors and germplasm, `Technical Mechanism` trait and marker linkage, `Production Technical System` the breeding program, `Technical Standard` certification and biosafety, `Technical Institution` the bank and the authority — and are coherent as a set because all of them serve one end: a variety that can be grown, certified, and sold.

Secondary readings, kept as prose rather than compromise typing: the whole program as a facility is a `Production Technical System` (the crossing block, nursery, trial network, and seed plant working as one installation); one mating or one transformation performed on a stated parent is an `Operative Technique`; the site, season, and pathogen population the selection must satisfy are a `Technical Domain Reality Model`. Each takes its own root in its own decomposition; no row below carries two types.

### What is this technical instance?

> A breeder, a biotechnologist, a molecular geneticist, a trial statistician, a seed technician, and a regulator working one accession from germplasm to certified seed: crossing and selection or marker and genomic prediction or transformation and editing to reach the trait, multi-location trials to read it against a target population of environments, release and seed multiplication to deliver it, and the standards and institutions that make the lot admissible. The ends are fixed — yield stability, resistance, adaptation range, product quality, and the conservation of the variability the next cycle will need — and the method is chosen per end, per species, and per regulatory regime.

Why the method varies, in the article's own terms: the plant must first be shown to carry usable variation, and where natural variation is insufficient the variation is created — by intra- or interspecific hybridization, by heterosis, by mutation, by polyploidy induction, by somatic hybridization, or by genetic engineering. Inter-populational variation carries the adaptive traits; intra-populational variation carries the economic traits. The resistance targets split biotic (insects, fungi, bacteria, viruses) from abiotic (climate and edaphic: salinity, extreme heat and cold, water deficit, photoperiod, frost). The market targets split organoleptic from quantitative (protein, oil) from post-harvest life. Those three splits are what the trait-target set below is organized along, and they are why this is a set of practices: each split selects a different technical route.

Lineage: domestication and farmer selection → mass, line, and pedigree selection with written pedigrees → controlled hybridization and heterosis in the field → cytogenetics, polyploidy, and mutation breeding → molecular markers and marker-assisted selection → transformation of the nuclear genome → genome editing, and with it de novo domestication of a wild genome without a single cross.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one practice ensemble, decomposed at middle depth — the shared spine (purpose, requirement, evolution), eight practice sets worked to instance leaves, and no deployment exemplars. A branch that would need a concrete cultivar, event, or seed lot takes one in its own decomposition.
>
> Typing reads from the instance path: each set resolves to the enclosing `Technical Element Set` grouping, and everything below a set resolves to its nearest enclosing type segment. Expansion is licensed by `(root) := <<Technical Element>> -> ... -> Technical Element Set`. Every backticked type segment groups instances and terminates on none; every leaf resolves to a technical instance.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Plant Genetic Improvement | The set of practices that turns germplasm into a new variety: breeding, genome-modifying methods, the laboratory and field apparatus that carry them, and the testing, release, and regulation that admit the seed. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` | Grouping: the eight practice sets of the improvement domain. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` | Grouping: the technical evolution of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` → Domestication And Artificial Selection | Keeping the better plant as seed, without any theory of it. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` → Mass And Line Selection Era | Systematic selection among populations and pure lines with written records. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` → Controlled Hybridization And Heterosis Era | Mating chosen parents to exploit heterozygosity in the field. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` → Cytogenetics And Polyploidy Era | Chromosome behaviour and chromosome doubling as working tools. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` → Mutation Breeding Era | Induced change, selected as a random source of new variants. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` → Molecular Marker Era | Linked markers replacing phenotype in the selection decision. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` → Transformation Era | Introducing a chosen construct rather than waiting for a variant. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Evolution` → Genome Editing And De Novo Domestication Era | Rewriting a stated sequence, and building a crop genome from a wild one. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Purpose` | Grouping: the technical purpose of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Purpose` → Yield Stability Objective | Raise and stabilize yield per unit of input across sites and seasons. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Purpose` → Biotic Resistance Objective | Carry resistance to the pests and pathogens that cost the product. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Purpose` → Abiotic Adaptation Objective | Widen the tolerance range for water, heat, cold, and salinity. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Purpose` → Product Quality Objective | Reach the organoleptic, quantitative, and post-harvest qualities the buyer pays for. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Purpose` → Variability Conservation Objective | Keep the genetic variability the next cycle will need. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Requirement` | Grouping: the technical requirement of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Requirement` → Yield Target | The stated production level the candidate must meet. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Requirement` → Resistance Target | The named disease, pest, or race the candidate must resist. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Requirement` → Adaptation Range Target | The stated tolerance window the candidate must hold across. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Requirement` → Quality Target | The composition or shelf-life figure the candidate must deliver. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Requirement` → Distinctness Uniformity And Stability Target | The criterion a released variety must satisfy to be registrable. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set | Crossing and selection practised without molecular tools: the genotype manipulated by mating, selfing, and picking the better plant. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Production Technical System` | Grouping: the production technical system of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Production Technical System` → Isolation Cage | Enclosure excluding pollen from neighbours during crossing. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Production Technical System` → Pollen Storage Unit | Controlled storage keeping pollen viable to schedule the cross. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Production Technical System` → Screen House | Insect-proof house for seedling and clone maintenance. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Production Technical System` → Seed Drying And Storage Room | Drying and cold storage holding seed lots between generations. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` | Grouping: the general technique of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Controlled Crossing | Generalized method of mating two chosen parents and recording the pedigree. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Hand Emasculation | Removing anthers before self-pollination to force the intended pollen. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Detasseling | Removing the tassel of the female parent in a maize field before anthesis. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Controlled Pollination Bag | Bag isolating the emasculated flower until the intended pollination. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Bulk Pollination | Mixing pollen masses to realise a population cross rather than a pair cross. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Introgression And Backcrossing | Repeated mating to a recurrent parent, keeping the donor trait and recovering the recurrent background. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Recurrent Selection | Repeated selection of the best individuals to accumulate favourable alleles in a population. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Mass Selection | Harvesting seed from the best individuals of a standing population without progeny testing. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Pedigree Selection | Keeping a written genealogy and selecting among the resulting rows. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Single Plant Selection | Propagating one chosen plant and testing its progeny. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `General Technique` → Line Selection | Comparing established pure lines on performance, keeping the winner. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Constitutive Technique` | Grouping: the constitutive technique of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Constitutive Technique` → Genome Editing Set | Embodied editing machinery carried by the vector: nuclease, guide, and repair template. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Constitutive Technique` → Transformation Set | Embodied delivery machinery carried by the vector and the strain: borders, cassette, vir genes. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Constitutive Technique` → Marker-Assisted Set | Embodied linkage knowledge carried by the marker panel used for selection. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Technical Parameter` | Grouping: the technical parameter of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Technical Parameter` → Selection Intensity | Fraction of the population kept as parents, the pressure of one cycle. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Technical Parameter` → Generation Interval | Time from one selection decision to the next, the clock of the program. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Technical Parameter` → Heritability Estimate | Share of the observed variance that is genetic and therefore selectable. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Breeding Set → `Technical Parameter` → Genetic Gain Per Year | Mean improvement per unit time, the score of the whole program. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set | The instrument layer that turns a phenotype into a predicted breeding value: markers, genotyping, phenotyping, and the models fitted over them. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Production Technical Object` | Grouping: the production technical object of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Production Technical Object` → SNP Genotyping Array | Fixed panel reading thousands of loci per sample. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Production Technical Object` → Short-Read Sequencer | Instrument producing the reads a variant call is built from. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Production Technical Object` → Phenotyping Platform | Imaging and weighing station registering traits without hand measurement. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Production Technical Object` → Growth Chamber | Controlled enclosure where uniform plants are raised for trait comparison. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Production Technical Object` → Reference Genome Assembly | The scaffold every variant and coordinate is reported against. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Production Technical Object` → Marker Database | Curated map from marker to locus to trait effect. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `General Technique` | Grouping: the general technique of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `General Technique` → Marker-Assisted Selection | Selecting on a marker tightly linked to the trait instead of on the phenotype. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `General Technique` → Marker-Assisted Backcrossing | Tagging the donor segment so each backcross is scored for it. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `General Technique` → Recombinant Selection | Picking recombinants that keep the trait and shed the linkage drag around it. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `General Technique` → Genomic Selection | Predicting breeding value from markers across the whole genome. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `General Technique` → Genomic Prediction | Fitting a model that predicts phenotype from genotype for untested material. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `General Technique` → Association Mapping | Localizing trait-associated loci from unrelated samples. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `General Technique` → Pangenome Analysis | Reading structural variation across a species by comparing genomes. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Mechanism` | Grouping: the technical mechanism of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Mechanism` → Qtl Estimate | Located region and its estimated effect on the trait. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Mechanism` → Linkage Drag | Unwanted donor genes carried with the trait, and the cost of removing them. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Mechanism` → Allele Effect Estimate | The substitution effect of one allele over another. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Mechanism` → Multi-Trait Selection Index | Weighted combination of traits into a single ranking for selection. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Parameter` | Grouping: the technical parameter of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Parameter` → Marker Informativeness | How reliably the marker reports the trait in this population. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Parameter` → Selection Accuracy | Correlation between predicted and realized breeding value. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Parameter` → Training Population Size | Size of the population the prediction model is fitted on. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Marker And Genomic Tooling Set → `Technical Parameter` → Prediction Accuracy | Held-out accuracy of the genomic model on new material. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set | Modification of the genome itself: delivering a construct, cutting and rewriting a stated site, and confirming the edit. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` | Grouping: the general technique of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Agrobacterium-Mediated Transformation | Using the soil bacterium to carry T-DNA into the plant cell and integrate it. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Binary Vector Delivery | Transferring the T-DNA from a helper and a binary vector pair into Agrobacterium. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Floral Dip Transformation | Immersing inflorescences in an Agrobacterium suspension at flowering. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Biolistic Transformation | Bombarding tissue with DNA-coated particles. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Chloroplast Transformation | Targeting the plastid genome to reach the maternal cytoplasm. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Protoplast Transformation | Introducing DNA into wall-less cells, then regenerating the plant. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Somatic Embryogenesis And Regeneration | Regenerating a whole plant from a transformed explant through the embryogenic route. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Selection And Regeneration Medium | Selective culture keeping only the cells that took the construct. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Cas9 Nuclease Editing | Double-strand break at a guide-matched site, repaired by non-homologous joining. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Knock-In By Homology-Directed Repair | Using a supplied template so the cut site is rewritten, not merely broken. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Base Editing | Enzymatically converting one base without cutting both strands. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Prime Editing | Writing a stated sequence change through a reverse-transcriptase guide. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → Multiplex Editing | Running several guides in one plant to change several loci at once. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → TALEN Editing | Repeat-variable-sequence nuclease as an alternative programmable cutter. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `General Technique` → De Novo Domestication | Rewriting a wild or unadapted genome into a crop genome, trait by trait, without crossing. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technique` | Grouping: the constitutive technique of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technique` → Codon Optimization | Rewriting a coding sequence for the host's expression machinery. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technique` → Inducible Promoter System | Switching the cassette on or off after integration. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technique` → Selectable Marker Removal | Excising the marker once the edit is confirmed. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technique` → Vector Backbone Minimization | Shipping only the sequence required, lowering the transgene footprint. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technical Object` | Grouping: the constitutive technical object of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technical Object` → Binary Vector | Plasmid carrying the T-DNA borders and the expression cassette. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technical Object` → T-DNA Border And Linker | The 25 bp borders and the linker delimiting what transfers. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technical Object` → Cas9 Expression Cassette | Coding sequence and promoter expressing the nuclease in the plant. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technical Object` → Single-Guide RNA | The spacer-plus-scaffold RNA that addresses the nuclease to one site. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technical Object` → Selectable Marker Gene | Gene whose product confers survival on the selective medium. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Constitutive Technical Object` → Trait Cassette | The payload expressing the intended agronomic trait. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Act` | Grouping: the technical act of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Act` → Transform | Deliver the construct into explant tissue under the stated strain and medium. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Act` → Regenerate From Explant | Drive the transformed cell into a whole plant under selection. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Act` → Screen Transformed Line | Reject plants that did not take the construct, by marker or reporter. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Act` → Confirm Molecular Edit | Sequence the target site and establish the intended change and its boundaries. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Act` → Chimerism Test | Check whether a regenerated plant carries the edit in all its tissues or only some. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Parameter` | Grouping: the technical parameter of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Parameter` → Transformation Efficiency | Transformed explants per bombarded or dipped explant. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Parameter` → Edit Efficiency | Edited plants per regenerated plants, per target. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Parameter` → Off-Target Rate | Editing at unintended homologous sites. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Parameter` → Regeneration Success Rate | Whole plants recovered per transformed cell line. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Parameter` → Somaclonal Variation Rate | Unintended change appearing from culture and regeneration. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Constraint` | Grouping: the technical constraint of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Constraint` → Recalcitrancy | Species that will not regenerate from culture, blocking the whole route. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Constraint` → Transgene Silencing | The plant suppressing the introduced expression after integration. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Constraint` → Genome Size Limit | Delivery and regeneration failing beyond a practical genome size. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Constraint` → Transformation Event Chimerism | A regenerated plant carrying more than one transformation event. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Transformation And Genome Editing Set → `Technical Constraint` → Polyploidy Of The Recipient | Copy number of the recipient, which changes what an edit means. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set | The ends the improvement is for, in the three splits the framing gives: biotic stress, abiotic stress, and market quality. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` | Grouping: the technical mechanism of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Fungal Resistance | Resistance to fungal pathogens, by defence genes or by receptor genes. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Bacterial Resistance | Resistance to bacterial pathogens, commonly by a trans-acting resistance gene. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Viral Resistance | Resistance expressed through pathogen-derived RNA or coat-protein interference. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Insect Resistance | Resistance to insect pests, by a toxin transgene or by a plant receptor. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Nematode Resistance | Resistance to root-knot and cyst nematodes. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Durable Broad-Spectrum Resistance | Resistance intended to hold across locations and pathogen races. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Drought Tolerance | Yield or viability held under water deficit. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Heat Tolerance | Fertility and yield held above the damaging temperature. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Cold And Frost Tolerance | Survival and sowing capacity under low temperature. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Salinity Tolerance | Growth held under salt in soil or irrigation water. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Flood Tolerance | Survival of submergence or of the waterlogging after it. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Nutrient Use Efficiency | More product per unit of applied nitrogen, phosphorus, or water. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Organoleptic Quality | Taste, aroma, and texture as the buyer judges them. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Quantitative Composition | Stated protein, oil, or sugar content in the product. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Post-Harvest Shelf Life | Days the product keeps its market value after harvest. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Nutrient Biofortification | Raising a nutrient in the edible part rather than in the feed. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Processing Quality | Milling, baking, or textile behaviour of the harvested product. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Trait Target Set → `Technical Mechanism` → Flowering And Ornamental Traits | Time to flower, flower colour, and vase life. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set | The material the program starts from and the population structure it reasons about: accessions, variation, and the environments the result must serve. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` | Grouping: the constitutive technical object of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` → Landrace | A farmer-maintained population carrying local adaptation. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` → Wild Relative | A related wild species as the donor of a trait the crop lost. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` → Inbred Strain | A nearly homozygous line as the recurrent parent of a hybrid. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` → Breeding Line | A numbered selection under evaluation in the program. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` → Hybrid | An F1 whose heterozygosis is the trait, maintained by recombination each season. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` → Mutant Line | A line carrying induced or spontaneous change. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` → Transgenic Line | A line carrying an introduced construct at a characterized locus. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Constitutive Technical Object` → Edited Line | A line carrying a targeted sequence change, with no foreign sequence. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Resource` | Grouping: the technical resource of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Resource` → Inter-Populational Variation | Variation between provenances, the largest source of adaptive diversity. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Resource` → Intra-Population Variation | Variation among individuals of one population, the source of economic traits. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Resource` → Induced Variation | Variation created on purpose by crossing, mutation, ploidy, or editing. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Resource` → Ex Situ Accession | The stored sample that keeps a population alive outside its field. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Domain Reality Model` | Grouping: the technical domain reality model of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Domain Reality Model` → Target Population Of Environments | The set of sites and seasons the variety must perform in. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Domain Reality Model` → Genotype-Environment Interaction Structure | How the ranking of genotypes changes from environment to environment. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Domain Reality Model` → Production Environment Model | The target production system the variety has to fit. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set | The apparatus that decides whether a candidate is real: trial designs, evaluations, and the feedback that returns to the next generation. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Practice` | Grouping: the technical practice of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Practice` → Multi-Location Trial | The same entries grown across sites and seasons to expose interaction. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Practice` → Randomised Complete Block Trial | Randomization within blocks so field variation is not read as treatment. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Practice` → Replicated Trial | Repeated observations of the same plot to separate plot from error. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Practice` → Advance Line Trial | Comparing the surviving selections with the check varieties. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Practice` → Disease Screening Trial | Deliberate inoculation to read resistance against the named race. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Practice` → Uniformity Trial | Uniform trial rows to measure grain quality and milling behaviour. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Evaluation` | Grouping: the technical evaluation of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Evaluation` → Multi-Environment Trial Analysis | Fitting genotype, environment, and their interaction over a trial series. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Evaluation` → Stability Analysis | Measuring whether a line holds its performance rather than averaging it away. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Evaluation` → Genetic Gain Estimate | Measuring the improvement per unit time against the check. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Evaluation` → Off-Target Confirmation | Screening the rest of the genome for unintended edits. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Evaluation` → Trait Validation | Confirming the trait in the field, not only in the screenhouse. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Evaluation` → Gene Flow Monitoring | Tracking the transgene or the allele beyond the intended crop. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Feedback` | Grouping: the technical feedback of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Feedback` → Phenotype Data Return | Trial data fed back into the breeding program as the next ranking. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Feedback` → Trial Failure Reading | The failed candidate returning the reason it was dropped. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Feedback` → Marker-QTL Discrepancy | A marker that fails to report the trait in this population. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Testing And Evaluation Set → `Technical Feedback` → Edit Confirmation Failure | A regenerated line that carries no edit, or an unintended one. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Constraint` | Grouping: the technical constraint of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Constraint` → Narrow Genetic Base | A crop whose parents come from one lineage, and the exhaustion that follows. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Constraint` → Genetic Drag | Unwanted traits carried along with the wanted one through backcrossing. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Constraint` → Ex Situ Conservation Gap | Accessions lost from the store that the next program will need. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Germplasm And Population Set → `Technical Constraint` → Seed System Availability | Whether clean seed of the new variety can be produced at all. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set | Turning a candidate into seed a farmer can buy: release, multiplication through the classes, and the certification that grades each lot. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` | Grouping: the general technique of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` → Varietal Release | The decision admitting a candidate to the catalogue of cultivars. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` → Seed Multiplication | Growing a variety up the classes from breeder seed to commercial seed. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` → Breeder Seed Stage | The first seed, kept by the breeder and never sold. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` → Foundation Seed Stage | Seed grown under supervision from the breeder seed. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` → Commercial Seed Stage | The certified class grown for sale. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` → Hybrid Seed Production | Growing a hybrid whose heterozygosity is bought and cannot be replanted equivalently. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` → Seed Treatment And Coating | Protection and handling quality applied before sowing. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `General Technique` → Isolation And Roguing | Distance and off-type removal keeping the lot true to type. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Production Technical Object` | Grouping: the production technical object of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Production Technical Object` → Seed Multiplication Plot | The field block that turns one class of seed into the next. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Production Technical Object` → Isolation Field | Spaced or barrier-isolated block for hybrid and self-incompatible material. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Production Technical Object` → Seed Processing Plant | Drying, cleaning, grading, and treating the harvested lot. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Production Technical Object` → Cold Storage For Seed Lots | Storage holding germination over the season gap. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Technical Standard` | Grouping: the technical standard of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Technical Standard` → Seed Certification Standard | The generation, isolation, and purity rules a lot is graded against. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Technical Standard` → Variety Registration Criterion | The distinctness, uniformity, and stability test for admission. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Technical Standard` → Isolation Distance Requirement | The stated separation a cross-pollinating crop must keep. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Release And Seed Production Set → `Technical Standard` → Seed Lot Purity Requirement | The species and off-type ceiling a certified lot may contain. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set | The rules, bodies, and residual risks that decide what may be released, where it may go, and who may use it. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Standard` | Grouping: the technical standard of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Standard` → Biosafety Regulation | The national rule stating what may be released and under what containment. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Standard` → Cartagena Protocol Compliance | The transboundary rule governing movement of living modified material. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Standard` → Genetically Modified Crop Authorization | The market authorization a specific event must hold. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Standard` → Plant Breeders' Rights | The right that rewards the breeder and licenses the variety's use. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Standard` → Patent On An Edited Plant | Property claimed over a specific edited plant or its method. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Standard` → Import And Border Control Rule | The condition under which planting material may enter a country. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Standard` → Containment And Monitoring Rule | What must be monitored after release, and for how long. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Institution` | Grouping: the technical institution of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Institution` → Breeding Institute | The organization that runs the program and holds the lines. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Institution` → Germplasm Bank | The store that keeps the variation the program starts from. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Institution` → Variety Registration Authority | The body that admits or refuses a variety. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Institution` → Biosafety Committee | The body that rules on a living modified event. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Institution` → Intellectual Property Office | The office granting the breeders' right or the patent. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Institution` → Seed Inspection Service | The service that certifies the lot in the field and the bag. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Constraint` | Grouping: the technical constraint of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Constraint` → Regulatory Constraint | Release held or restricted by an approval that has not been granted. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Constraint` → Acceptance Constraint | A variety technically sound and refused by growers or buyers. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Constraint` → Cost Of Compliance | Trial, isolation, and certification cost that decides whether a smallholder can buy seed. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Constraint` → Liability And Compensation Regime | Who pays when the variety fails in the field. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Risk` | Grouping: the technical risk of this set. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Risk` → Gene Flow To Wild Relatives | Alleles moving into wild populations, and back. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Risk` → Unintended Allergen Introduction | A new protein appearing in an edible part. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Risk` → Pleiotropic Undesirable Effect | One edit changing a trait nobody asked for. |
| `Technical Element Set` → Plant Genetic Improvement → `Technical Element Set` → Governance And Regulation Set → `Technical Risk` → Trait Breakdown Under New Races | Resistance that stops holding against an evolving pathogen. |

## QA

### What techniques enable plant genome modification, and what biological processes are used to regenerate a genome-modified plant from the modified cells?

> **Part one — the techniques that change the genome.** Modification starts by getting DNA, or a cutting device, into a living plant cell; the routes are `Agrobacterium-Mediated Transformation` (with `Binary Vector Delivery` and `Floral Dip Transformation`), where the soil bacterium carries the `T-DNA Border And Linker` and the `Trait Cassette` into the nucleus (Klümper & Munkvold, 1998; Innes et al., 1994); `Biolistic Transformation`, for tissue or species the bacterium will not take; `Protoplast Transformation`, for large inserts into wall-less cells; and `Chloroplast Transformation`, which edits the maternal plastid genome and buys high expression with containment that nuclear transformation does not give. From there the technique no longer adds a gene but rewrites one: `Cas9 Nuclease Editing` cuts a guide-matched site and lets non-homologous joining turn the cut into a knockout, or uses the cell's own repair to `Knock-In By Homology-Directed Repair` from a supplied template (Jinek et al., 2012; Cong et al., 2013); `Base Editing` and `Prime Editing` change a stated base and a stated sequence without a double-strand break (Komor et al., 2016; Anzalone et al., 2019); `Multiplex Editing` runs several guides at once, and `TALEN Editing` is the alternative programmable cutter (Belhaj et al., 2013). `De Novo Domestication` is the same machinery aimed the other way — rewriting a wild or unadapted genome into a crop genome, trait by trait, with no crossing at all (McCallum et al., 2012). What makes each of these a technique rather than a wish is the apparatus that carries it: the constructs are `Constitutive Technical Object` (Binary Vector, T-DNA Border And Linker, Cas9 Expression Cassette, Single-Guide RNA, Selectable Marker Gene, Trait Cassette), the run is a `Technical Act` chain (Transform → Regenerate From Explant → Screen Transformed Line → Confirm Molecular Edit → Chimerism Test), and the yield of the run is declared as `Transformation Efficiency`, `Edit Efficiency`, `Off-Target Rate`, and `Regeneration Success Rate`.
>
> **Part two — the biology that gets a modified cell back into a plant.** The tree above names the regeneration *operations* — `Somatic Embryogenesis And Regeneration`, `Selection And Regeneration Medium`, `Regenerate From Explant`, `Chimerism Test` — but not the processes that make them work; those are given here, because they are the reason a plant and not a bacterium is the substrate of this whole set. The premise is **totipotency**: a differentiated plant cell keeps the complete genome, so one transformed somatic cell carries everything needed to rebuild the organism, and the whole problem reduces to making that cell divide, organize, and finish. The process has four stages.
>
> 1. **Dedifferentiation to callus.** An explant — a leaf disc, a cotyledon, an immature embryo, a root segment — is placed on a growth-regulator medium (auxin and cytokinin) and reverts to an unpatterned, rapidly dividing cell mass. This is the stage at which the construct or the cut is retained, and at which *every* cell is a potential founder, which is why the transformation event is diluted here and must be resolved later.
> 2. **Re-differentiation, by one of two routes.**
>
>    | Route | Sequence | Typical use |
>    | --- | --- | --- |
>    | **Somatic embryogenesis** | embryogenic callus → globular → heart → torpedo → cotyledonary embryo → maturation and desiccation | dicots; embryos come from single cells, so a regenerated plant is usually not chimeric |
>    | **Organogenesis** | shoot induction from callus → rooting of the shoot → hardening | monocots, and species whose embryogenic route is unreliable |
>
>    Both routes end at the same boundary: an in-vitro plantlet that is physiologically adapted to a sterile, humid, low-light plate, not to a field.
> 3. **Selection and chimera resolution.** The `Selection And Regeneration Medium` — a selectable marker plus the matching agent — kills the cells that did not take the construct, which is what makes the modified cell *the* founder of the regenerated plant rather than one cell among many. Where the event is not fixed in the meristem, the regenerated plant is a mosaic: two tissues may differ, and only the transformed sector is heritable. `Chimerism Test` establishes which case you have, and the fix is to sub-clone — take an axillary bud or a single somatic embryo — until the plant is uniform.
> 4. **Acclimatization.** The plantlet is weaned off the sterile medium: humidity down, light up, gradually, until the cuticle and the stomata can carry a normal transpiration load. This is the hand-off to cultivation, and it is the same operation the propagation practice calls `Hardening-Off` in [Plant Cultivation Technical Domain Set](note.html?n=technica/general/cto/es/multinode/plant-cultivation-technical-domain-set.md) — an improvement that ends at a test tube has delivered nothing.
>
> What bounds the whole sequence is the same for every route. **Recalcitrancy**: the response is species- and genotype-dependent, and the species that will not regenerate block every technique above, which is what `Regeneration Success Rate` registers. **Somaclonal variation**: the culture itself mutates the plant, so a regenerated line carries changes nobody asked for, and has to be crossed back into an elite background before it is a candidate — which is why an editing route is normally run together with a crossing programme from the Breeding Set. **Transgene silencing**: the plant can switch the introduced expression off after integration. And **transformation event chimerism**: one regenerated plant carrying more than one independent event, which then segregates unpredictably in the field.

## References

### Framing

- [Mejoramiento genético](https://es.wikipedia.org/wiki/Mejoramiento_gen%C3%A9tico) — Wikipedia (es), used as orientation only; the article carries a maintenance banner for missing published references, so it is not treated as a source of record here.
- [Mejoramiento genético de animales](https://es.wikipedia.org/wiki/Mejoramiento_gen%C3%A9tico#V%C3%A9ase_tambi%C3%A9n) — the animal half of the same article, out of the cut of this note.

### Historical works

- Bateson, W., & Punnett, R. C. (1911). *Mendelism: An introduction to the study of heredity*. Macmillan.
- Boveri, T. (1909). *Ergebnisse über die Konstitution der chromatischen Substanz des Zellkerns*. Jerold.
- Darwin, C. (1859). *On the origin of species by means of natural selection*. John Murray.
- Mendel, G. J. (1866). *Experiments on plant hybridization* (English translation, 1965). Harvard University Press. (Original work: "Versuche über Pflanzenhybridation", Verhandlungen des naturforschenden Vereins in Brünn.)
- Nilsson-Ehle, W. (1908). *Kreuzungsuntersuchungen an dem Hafer und dem Weizen*. Gleerups.
- Sturtevant, E. H. (1913). The linear arrangement of six sex-linked factors in *Drosophila*, as shown by their mode of association. *Journal of Experimental Zoology, 14*(1), 43–59.
- Sutton, W. E. (1902). On the morphology of the chromosome group in *Brachystola magna*. *Biological Bulletin, 4*, 24.
- Vavilov, N. I. (1926). Studies on the origin of cultivated plants (English translation, 1951). Chronica Botanica.

### Books and manuals

- Acquaah, G. (2012). *Principles of plant genetics and breeding* (2nd ed.). Wiley-Blackwell.
- Allard, R. W. (1960). *Principles of plant breeding*. John Wiley & Sons.
- Falconer, D. S. (1981). *Introduction to quantitative genetics* (2nd ed.). Oliver & Boyd.
- Griffiths, A. J. F., Wessler, S. R., Lewontin, R. C., & Gelbart, W. M. (2008). *An introduction to genetic analysis* (9th ed.). Macmillan.
- Kloppenburg, D. J. (2009). *Plant breeding systems* (2nd ed.). Springer. — Attribution note: taken from the framing article's bibliography, which lists Richards, A. J. (1997). *Plant breeding systems* (2nd ed., Chapman & Hall); verify the author and edition against the record before citing.
- Tinker, N. A., & Butler, M. C. (1988). *Principles of crop improvement*. Longman.

### Papers

- Anzalone, A. V., Koblan, L. W., & Liu, D. R. (2019). Programmable deletion, replacement, integration and inversion of large DNA sequences with twin prime editing. *Nature, 577*, 852–856.
- Barrangou, R., Fremaux, C., Deveau, H., Botelho, M. A., Wintermute, M. W., & Chylinski, K. (2007). CRISPR provides acquired resistance against viruses in prokaryotes. *Science, 315*, 1709–1712.
- Belhaj, K., et al. (2013). A multipurpose toolkit to generate advanced genome engineering in plants. *Cell, 163*(1), 21–31.
- Collard, B. C. Y., & Mackill, D. J. (2008). Marker-assisted selection: an approach for precision plant breeding in the twenty-first century. *Philosophical Transactions of the Royal Society B, 363*(1441), 557–572.
- Cong, L., Zhang, F., et al. (2013). Multiplex genome engineering using CRISPR/Cas systems. *Science, 339*(6121), 819–823.
- Evenson, R. E., & Gollin, D. (2003). Assessing the impact of the Green Revolution, 1960 to 2000. *Science, 300*(5620), 1059–1063.
- Finlay, K. W., & Wilkinson, G. N. (1963). The analysis of adaptation in a breeding programme. *Australian Journal of Agricultural Research, 14*(6), 742–754.
- Griffing, B. (1954). Genotype-environment interaction. *Australian Journal of Agricultural Research, 5*(3), 463–473.
- Innes, J., Harrison, B. D., Leaver, C. J., & Bevan, M. W. (1994). *The production and uses of genetically transformed plants*. Chapman & Hall.
- Jinek, M., Chylinski, K., Fonfara, I., Hauer, M., Doudna, J. A., & Charpentier, E. (2012). A programmable dual-RNA-guided DNA endonuclease in adaptive bacterial immunity. *Science, 337*(6096), 816–821.
- Khush, G. S. (2001). Green revolution: an end to the beginning. *Crop Science, 41*(3), 637–642.
- Klümper, A., & Munkvold, K. (1998). The genetics of plant transformation. *The Plant Journal, 15*(1), 1–10.
- Komor, A. C., et al. (2016). Programmable editing of a target base in genomic DNA without double-stranded DNA cleavage. *Nature, 533*(7603), 420–423.
- McDonald, M. B., & Copeland, L. O. (1997). *Seed production: Principles and practices*. Chapman & Hall.
- McCallum, E., et al. (2012). Targeted mutagenesis in plants. *Nature Reviews Genetics, 13*(11), 700–711.
- Miedaner, T., & Korzun, V. (2012). Marker-assisted selection for disease resistance in wheat and barley breeding. *Phytopathology, 102*(6), 560–566.
- Nishimasu, H., et al. (2014). Crystal structure of Cas9 in complex with guide RNA and target DNA. *Cell, 156*(5), 935–949.
- Sprague, G. F., & Russell, W. A. (1942). Performance of six corn hybrids in relation to fertility levels. *Agronomy Journal, 34*(5), 431–464.
- Sobral, B. W. S. (Ed.). (1996). *The impact of plant molecular genetics*. Birkhäuser.
- Varshney, R. K., Bohra, A., & Yu, J. (2021). Genetic improvement of crops: Accelerated breeding strategies. *Trends in Plant Science, 26*(6), 631–649.
- Xu, X., & Crouch, J. H. (2008). Marker-assisted selection in plant breeding: From publications to practice. *Crop Science, 48*(2), 391–407.
- Yilmaz, N., et al. (2019). Genome editing in plants and crops. *Nature Biotechnology, 37*(11), 1328–1331.

### Standards and regulatory instruments

- Cartagena Protocol on Biosafety. (2000). Secretariat of the Convention on Biological Diversity, Montreal.
- International Seed Testing Association. (2021). *International rules for seed testing*. ISTA. — Edition year to be confirmed against the current ISTA publication.
- International Union for the Protection of New Varieties of Plants. (1991). *UPOV Convention 1991*. UPOV, Geneva.
- Codex Alimentarius Commission. (1995). *Codex maximum residue limits for pesticides* (CXC 193-1995). FAO/WHO Codex Alimentarius Commission. — Reference number to be confirmed against the current Codex list.

### Encyclopedia cross-references

- [Plant breeding](https://en.wikipedia.org/wiki/Plant_breeding)
- [Selective breeding](https://en.wikipedia.org/wiki/Selective_breeding)
- [Cultivar](https://en.wikipedia.org/wiki/Cultivar)
- [Inbred strain](https://en.wikipedia.org/wiki/Inbred_strain)
- [Heterosis](https://en.wikipedia.org/wiki/Heterosis)
- [Hybrid seed](https://en.wikipedia.org/wiki/Hybrid_seed)
- [Backcrossing](https://en.wikipedia.org/wiki/Backcrossing)
- [Polyploidy](https://en.wikipedia.org/wiki/Polyploidy)
- [Mutation breeding](https://en.wikipedia.org/wiki/Mutation_breeding)
- [Heritability](https://en.wikipedia.org/wiki/Heritability)
- [Marker-assisted selection](https://en.wikipedia.org/wiki/Marker-assisted_selection)
- [Genomic selection](https://en.wikipedia.org/wiki/Genomic_selection)
- [Genetic engineering](https://en.wikipedia.org/wiki/Genetic_engineering)
- [Agrobacterium tumefaciens](https://en.wikipedia.org/wiki/Agrobacterium_tumefaciens)
- [CRISPR](https://en.wikipedia.org/wiki/CRISPR)
- [Gene editing](https://en.wikipedia.org/wiki/Gene_editing)
- [Genetically modified crops](https://en.wikipedia.org/wiki/Genetically_modified_crops)
- [Plant genetic resources](https://en.wikipedia.org/wiki/Plant_genetic_resources)
- [Gene bank](https://en.wikipedia.org/wiki/Gene_bank)

### Reference hygiene

Entries above are in APA style. Historical works and the well-known papers are given with the details recorded in the framing article's bibliography and in the standard literature; items marked with an attribution note (Kloppenburg/Richards) and the standards items with an edition note (ISTA, Codex) must be checked against the primary record before this note is treated as a bibliography of record.

## Related notes

- [Plant Cultivation Technical Domain Set](note.html?n=technica/general/cto/es/multinode/plant-cultivation-technical-domain-set.md) — the regime the improved variety is planted into; its Varietal Improvement Set is this note's container
- [Agricultural Science](note.html?n=epistemica/discipline/agricultural-science.md) — the inquiry behind QTL estimation, genomic prediction, and trial design
- [Earth Science](note.html?n=epistemica/discipline/earth-science.md) — the G × E structure and the climate and soils that set the adaptation range
- [Biotechnology](note.html?n=technica/general/cto/es/multinode/biotechnology.md) — the wider ensemble this set sits in
- Ambiguity Resolution (`guideline/ambiguity_resolution.md`) — the instrument technically, the organism naturally
- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md)
