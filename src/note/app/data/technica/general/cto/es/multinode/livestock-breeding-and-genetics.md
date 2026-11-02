---
tags: [animal, breeding, genetics, livestock]
---

# Livestock Breeding And Genetics Set

> The **Livestock Breeding And Genetics Set** is the animal mirror of [Plant Genetic Improvement](note.html?n=technica/general/cto/es/multinode/plant-genetic-improvement.md). It changes the next generation rather than the current one: mating systems, selection, and the records that make selection possible. It is the member of [Animal Husbandry Technical Set](note.html?n=technica/general/cto/es/multinode/animal-husbandry-technical-set.md) that decides what the animals will be in five years' time, and it is the reason the dairy herd renews itself, the flock gains growth, and a population carries a resistance.
>
> Worked per [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md).

## Formulation

### What technical element type does this technical instance belong to?

**The Livestock Breeding And Genetics Set belongs to the `Technical Element Set` technical element type — a collection of technical elements scoped to one bounded field, which here is the genetic change of an animal population.**

It is a set and not a `General Technique` because a mating, a collection, a transfer, a genotyping, and an index computation are different technical element types, and because the one that does the deciding — selection — is an inference from records rather than an act. The `Technical Element Set` grouping below the root is admitted by the No-repetition exception and appears once. Secondary readings, kept as prose: an AI centre or a transfer clinic is a `Production Technical System`; one insemination of one ewe is an `Operative Technique`; heritability, the generation interval, and the genotype-by-environment structure are a `Technical Domain Reality Model` (decomposed in the root spine). No row carries two types.

### What is this technical instance?

> The whole apparatus by which an animal population is made over generations: the sires and dams chosen, the matings performed (naturally, by artificial insemination, or by moving embryos), the progeny and genomic records kept, the offspring weighed and indexed against contemporaries, and the candidates selected — so that the population's mean for a stated trait rises, measurably, generation over generation.
>
> The discipline is an argument with a biological clock. Selection can only be as fast as the animal's age at first breeding, so the generation interval sets the ceiling on progress; progress is also proportional to accuracy and to selection intensity; and both are bought with something, accuracy with recording, intensity with inbreeding. The whole set is the machinery for managing that trade.

**Why selection on animals is a different act from selection on plants.** On a plant, the individual selected is the individual that reproduces. On an animal, the merit of the individual is only knowable from the mean of its progeny, and the selection decision must be made before that evidence exists, or on a prediction that stands in for it. Every technique here — progeny test, genomic selection, embryo biopsy, differential test — is an attempt to decide sooner, on weaker evidence, and the accuracy figures are the honest statement of how weak.

**The central trade.** A population selected hard for production becomes uniform, and a uniform population has less capacity to respond to whatever the next change turns out to be. Selection therefore also selects away the variation that a later problem would have needed, which is the same tension the crop-side set faces in a different way, and is why inbreeding monitoring and genetic-trend evaluation are members here rather than afterthoughts.

Lineage: choosing the breeding animal by eye → writing the pedigree → weighing progeny and keeping the best → crossbreeding to combine → artificial insemination, which turns geography and herd size into a mating detail → embryo transfer, which separates a dam's genetics from her production → genomic selection, which decides before the animal has bred once → gene editing, in the species whose regulation permits it.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one ensemble at middle depth — the spine (evolution, purpose, reality model) and the breeding, insemination, record, and embryo technologies worked to instance leaves. No exemplars are carried: a farm's own index figures belong in its own decomposition.
>
> Typing reads from the instance path: the spine lands on flat facet types; the technologies resolve to the nearest enclosing type segment. Expansion is licensed by `(root) := <<Technical Element>> -> ... -> Technical Element Set`. Every backticked type segment groups instances and terminates on none; every leaf resolves to a technical instance.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Livestock Breeding And Genetics Set | What changes the next generation: mating systems, selection, and the records that make selection possible, applied to cattle, pigs, sheep, goats, and poultry. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` | Grouping: the technical evolution of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` → Animal Breeding Antiquity Era | Choosing the breeding animal by eye, from the flock, for size and strength. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` → Recorded Pedigree Era | Writing the mating down so that a family can be traced and an ancestor named. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` → Selective Breeding Era | Weighing the progeny of a mating and keeping the best, which turns breeding from guesswork into arithmetic. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` → Crossbreeding Era | Breeding across breeds to take one breed's hardiness and another's production, and to build a crossbred dam whose own performance is secondary. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` → Artificial Insemination Era | Collecting and freezing semen so that one bull's genes reach thousands of daughters, and a mating is no longer geographically constrained. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` → Embryo Transfer Era | Flushing and transferring embryos so that the female's reproductive capacity is separated from her own production. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` → Genomic Selection Era | Reading the genome to predict breeding value before the animal has bred once, which shortens the generation interval. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evolution` → Gene Editing Era | A stated change in a stated gene of a stated animal, in species where the regulatory frame allows it. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Purpose` | Grouping: the technical purpose of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Purpose` → Genetic Gain Purpose | A measurable improvement in the population's mean for a trait, per generation, which is the only figure that counts. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Purpose` → Fertility Purpose | Conception rates and calving intervals good enough that the pipeline of replacements is filled. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Purpose` → Disease-Resistance Purpose | A population that does not need the prophylactic or the antibiotic to stay in production. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Purpose` → Feed-Efficiency Purpose | Gain and milk solids per unit of feed, which in a feed-priced system decides the margin. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Purpose` → Longevity Purpose | A longer productive life, which raises lifetime output per animal raised. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Domain Reality Model` | Grouping: the technical domain reality model of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Domain Reality Model` → Breeding Value | The operative model: an animal's genetic merit is only knowable from the mean of its progeny, so selection is an inference from relatives. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Domain Reality Model` → Generation Interval | The operative model of how fast a genetic change can reach the population, set by age at first service and age at culling. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Domain Reality Model` → Heritability Of A Trait | The operative model in which a trait with low heritability responds to management and not to selection, and the two are routinely confused. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Domain Reality Model` → Genotype By Environment | The operative model in which the same sire's daughters rank differently in different herds, which is why breeding value is always stated for a production context. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Domain Reality Model` → Selection Differential And Accuracy | The operative model in which what is selected on and how accurately that selection reflects the merit are separate numbers. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` | Grouping: the production technical object of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Artificial Insemination Unit | The gun, straws, thawing device, and handling kit by which a mating is performed away from the bull. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Semen Storage Tank | The liquid-nitrogen tank in which frozen semen is held at a temperature that stops the semen's life without stopping its genetics. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Pregnancy Diagnosis Device | The ultrasound or blood test by which a mating is confirmed to have taken, months before the birth would show it. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Pedigree And Recording System | The database in which every animal's ancestry, index, and progeny test accumulate. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Breeding Value Report | The published index by which an animal is ranked, with its accuracy stated beside it. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Embryo Transfer Kit | The apparatus by which embryos are recovered from a donor and placed in a recipient. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Live Animal Weighing System | The platform and indicator on which a breeding animal is scored against the standard it will be selected on. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Semen Collection Unit | The collection apparatus by which a bull's genetics are captured once and used thousands of times. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → In Vitro Fertilisation Laboratory | The facility in which oocytes, sperm, and embryos are produced outside the animal. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Genotyping Platform | The laboratory that reads markers or sequence from a hair, a swab, or an ear punch, and produces the genomic selection data. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Production Technical Object` → Phenotyping Station | The place where an animal's performance is measured on a common basis, which is what makes a comparison a comparison. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` | Grouping: the general technique of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Natural Mating | The female served by the male kept for her, which is simple and which is also a genetic bottleneck. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Artificial Insemination | Depositing thawed semen in the female's tract at the detected time of ovulation. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Estrus Detection | Finding the female in standing heat, by observation, by tail paint, by a teaser, or by pedometer. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Multiple-Ovulation Embryo Transfer | Stimulating a donor to release several ova, fertilising them, and transferring the resulting embryos to recipients. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Embryo Biopsy And Reimplantation | Sampling a blastocyst for genotyping and returning it to the donor, so the animal is bred and the merit known in the same cycle. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Ovum Pick-Up And In Vitro Fertilisation | Recovering oocytes from a living donor and producing an embryo in glass, multiplying a scarce dam's genetics without breeding her. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Sexed Semen | Sorting the ejaculate by the sex chromosome, so the genetic merit of the bull is directed at the sex that returns it. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Crossbreeding | Mating across breeds to combine traits, and keeping a crossbred dam whose own performance is a cost. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Progeny Test | The mating that produces the record: the siblings and offspring of a candidate, whose mean is the animal's evidence. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Contemporary Grouping | Correcting performance records for the year, the herd, and the feed, so that an animal is not credited with its herd's weather. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Genomic Selection | Selecting on a prediction from the genome rather than on the phenotype, which allows selection of animals too young to have progeny. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Marker-Assisted Selection | Selecting on a marker known to be linked to the trait, which is cheaper than a progeny test for some traits. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Differential Sire Evaluation | Comparing sires by the performance of their daughters rather than by their own record, which is the fair test. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Laparoscopic Artificial Insemination | Placing semen directly at the ovulation, for the species or the female where ordinary insemination fails. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `General Technique` → Genetic Preservation By Cryopreservation | Freezing semen, embryos, or tissue so that a line survives its own population's turnover. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Act` | Grouping: the technical act of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Act` → Detect Heat | The primitive act on which every other act in the set depends; without it, none of the rest is timed. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Act` → Collect And Freeze Semen | The act by which a bull's genetics are captured once and used for years. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Act` → Thaw And Inseminate | The act of handling the frozen dose without losing it, and placing it in the female. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Act` → Diagnose Pregnancy | The act of confirming that a mating took, which converts an expense into an asset. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Act` → Weigh And Index | The act of recording an animal's performance against a common standard. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Act` → Sample For Genotyping | The act of taking a hair, a swab, or a punch and sending it to be read. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Act` → Flush And Transfer Embryo | The act by which a donor's genetics are moved to a recipient. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` | Grouping: the technical parameter of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Conception Rate | The share of services that produce a pregnancy, which is the pipeline's throughput. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Age At First Service | The age at which a female enters the breeding herd, and therefore her cost per kilogram of lifetime production. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Calving Interval | The days between calvings, which sets the pace of the whole pipeline. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Progeny Performance Index | The mean of a candidate's relatives' performance, corrected for the contemporaries. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Genomic Selection Accuracy | The correlation between the genomic prediction and the realised breeding value, stated so that the index is not read as certain. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Selection Intensity | The share of candidates selected, which is a choice and can be pushed until it costs fertility. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Inbreeding Coefficient | The probability that two alleles at a locus are identical by descent, which rises as the candidate list narrows. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Generation Interval | The years from an animal's birth to the birth of its selected offspring, which is the speed of genetic progress. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Semen Fertility Index | The conception rate a dose achieves, which decides the value of a bull's collection. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Parameter` → Weaning Weight And Age | The growth figure at which a young animal is judged and either kept or culled. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` | Grouping: the technical mechanism of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` → Spermatogenesis And Storage | The biology by which a bull produces the ejaculate and the sperm survive in the epididymis, which cryopreservation then suspends. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` → Fertilisation And Implantation | The sequence by which a service becomes a pregnancy, and where conception rate is lost. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` → Quantitative Trait Locus Effect | The statistical link between a genomic region and a trait, which is what genomic selection reads. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` → Dominance And Heterosis | The genetic effects that make a crossbred animal outperform both parents and that a purebred selection index undervalues. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` → Maternal Effect | The genetic contribution of the dam through the environment she provides to her offspring, which no sire's index captures. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` → Cytoplasmic And Mitochondrial Inheritance | The non-nuclear inheritance that a purely nuclear selection scheme cannot act on. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` → Selection Response | The population's change in the mean, which is the selection differential multiplied by the accuracy and shrunk by the generation interval. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Mechanism` → Frozen Semen Survival | The mechanism the whole artificial insemination system depends on, and the one quality control governs. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Feedback` | Grouping: the technical feedback of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Feedback` → Calving Return | The conception and calving rates that return to the heat-detection and the insemination practice. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Feedback` → Progeny Performance Return | The records of the candidates' offspring, which return to the index of their sire. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Feedback` → Genomic Prediction Return | The realised merit of animals selected on prediction alone, which returns to the accuracy figure. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Feedback` → Culling Return | The animals that failed to breed, which return to the selection and the replacement decision. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evaluation` | Grouping: the technical evaluation of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evaluation` → Progeny Test Evaluation | Judging a candidate by the mean of its offspring, which is the measurement breeding has always rested on. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evaluation` → Differential Evaluation | Comparing sires through their daughters so that the comparison is between the daughters' milk, not the sires'. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evaluation` → Genetic Trend Evaluation | Measuring whether the population's mean is actually rising, generation over generation. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evaluation` → Inbreeding Monitoring | Watching the inbreeding coefficient and the heterozygosity of the population, and acting before the diversity is gone. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Evaluation` → Blinding And Randomised Mating | Assigning sires to daughters at random and by rule, so the comparison is not made by the farmer's choice. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Constraint` | Grouping: the technical constraint of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Constraint` → Generation Interval Constraint | The animal cannot be selected on merit until it has performance, so genetic progress is bounded by age. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Constraint` → Genetic Variation Constraint | A population with no additive variation cannot be moved by selection, however well the records are kept. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Constraint` → Recording Constraint | No selection beyond what was measured; the ceiling on accuracy is the ceiling on recording. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Constraint` → Heritability Constraint | A low-heritability trait responds to management and not to selection, and the two must not be confused. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Constraint` → Trade And Breed-Regulation Constraint | The genetic material a country may import and breed from, which is set by law and not by biology. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Constraint` → Scale Constraint | A breed improvement that pays at one herd size may not pay at another, and the index is often for the wrong one. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Constraint` → Species Reproduction Constraint | Species whose females cannot be bred intensively, or cannot be inseminated, and which are therefore bred differently or not at all. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Risk` | Grouping: the technical risk of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Risk` → Inbreeding Depression Risk | Rising homozygosity costing fertility, growth, and survival, invisible until it is well advanced. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Risk` → Selection-Induced Vulnerability Risk | A population selected for one trait losing the robustness that was not selected for, and having no reserve when the environment changes. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Risk` → Conception Failure Risk | A bull whose semen is passed on a batch that fails, and the season it costs. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Risk` → Genetic-Drift Loss Risk | A small population losing variation by chance, and the options narrowing permanently. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Risk` → Undesirable-Correlation Risk | Improving a trait by moving an allele linked to something bad, which takes a generation to undo. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Risk` → Disease-Resistance Erosion Risk | A resistance bred into a population that the pathogen evolves past, which is the race the whole discipline runs. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Standard` | Grouping: the technical standard of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Standard` → Breed Standard | The written description a breed is measured against, which decides what a pedigree means. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Standard` → Recording And Reporting Standard | The agreed format and correction method by which a performance record becomes comparable. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Standard` → Genetic Evaluation Protocol | The rule by which a breeding value is computed, so that an index from one country means the same as an index from another. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Standard` → Import And Export Of Genetic Material Rule | The sanitary conditions under which breeding stock and semen cross a border. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Institution` | Grouping: the technical institution of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Institution` → Recording Service | The body that maintains the pedigree, computes the breeding value, and is what makes a farm's own records worth keeping. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Institution` → Breed Society | The body that maintains the studbook and the standard, and registers every animal. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Institution` → Artificial Insemination Centre | The body that collects, freezes, and distributes semen, and holds the bull. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Institution` → Embryo Transfer Unit | The clinic that performs the recovery and the transfer. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Institution` → Genomic Evaluation Centre | The laboratory that runs the genomic evaluation on which every national index is based. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Institution` → Veterinary Reproduction Service | The clinician who handles the difficult cases and the pathological fertility. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Service` | Grouping: the technical service of this set. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Service` → Semen Distribution Service | The cold chain that keeps frozen semen usable between the centre and the farm. |
| `Technical Element Set` → Livestock Breeding And Genetics Set → `Technical Service` → Genetic Evaluation Service | The periodic publication of indexes that makes selection possible at all. |

## References

- [Philosophia Artium Technicarum et Operis](note.html?n=meta/philosophia-artium-technicarum-et-operis.md) (decomposition schema; No-repetition and Composite Instance Naming rules)
- [Plant Genetic Improvement](note.html?n=technica/general/cto/es/multinode/plant-genetic-improvement.md) (the crop-side set this one mirrors)
- [Animal Husbandry Technical Set](note.html?n=technica/general/cto/es/multinode/animal-husbandry-technical-set.md) (the system this member belongs to)
- [Dairy Husbandry Set](note.html?n=technica/general/cto/es/multinode/dairy-husbandry.md) (the herd this breeding renews)
- [Animal Health Technical Set](note.html?n=technica/general/cto/es/multinode/animal-health-technical-set.md) (the disease pressure that selection is partly a response to)
