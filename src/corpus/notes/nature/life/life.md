---
tags: [note, nature, biology, organism, ontology]
---

# Life

> **Life** is the ontic family of life: the kinds of natural element whose instance is a living organization, the parts it is made of, the information it carries and the processes it runs. It is filed by **ontic kind**, never by field of study — there is no `genetics/`, `biochemistry/` or `ecology/` here, because those are disciplines (epistemic readings), not elements of reality. The element is the *organism*, the *genome*, the *protein*; the field that studies it belongs to `epistemica/epistemic/discipline/`. The ecosystems organisms form are a different kind — a `Natural System`, not an organism — and are filed at `nature/ecosystem/`.

## Formulation

### What natural element type does this natural instance belong to?

The family spans the guide's kinds, each dir holding the kind it names:

| Dir | Kind (naturalis guide) | Instances |
| --- | --- | --- |
| `organism/` | `Substantive (→ Kind) Organism` — self-maintaining, reproducing organization (autopoietic) | organism, living system, multicellular/unicellular, autopoiesis |
| `organism/virus/` | *readable as* Organism — a virion is not autopoietic, so it is filed under the organisms by convention, marked as the borderline case | virus, virus taxonomy, prion |
| `organism/bacteria/` | `Organism` | bacteria, archaea, prokaryotes, microbial taxonomy, pathogens |
| `organism/protist/` | `Organism` | protists, protozoa |
| `organism/fungus/` | `Organism` | fungi, fungal taxonomy, yeast |
| `organism/plant/` | `Organism` | plants, their taxonomies, species, growth and nutrition |
| `organism/animal/` | `Organism` | animal taxonomy, species, locomotion, nutrition |
| `genome/` | the inherited information an organism carries (a `Property`-bearing structure, not a kind of its own) | gene, genome, DNA, RNA, chromosome, heredity, replication |
| `molecular/` | `Substance / Matter` at molecular scale | protein, lipid, carbohydrate, metabolite |
| `cell/` | `Natural Object` — the bounded body inside an organism | cell, membrane, organelles, division, death |
| `organism/human/` | `Organism` — the human instance, with its body, physiology, cognition and behaviour | human, organ systems, hormones, perception, memory, emotion |
| `process/` | `Process (→ Kind) Living Process` | evolution, metabolism, morphogenesis, growth |

### What is this natural instance?

> The part of reality that maintains itself, copies itself with variation, and builds its parts out of ordinary matter: an organism and the cells that compose it, the genome it passes on, the molecules those cells assemble, and the processes by which it lives. The unifying question is autopoiesis: what separates a living system from a chemistry that merely persists?

### What is the recursive instance decomposition of this natural instance?

> Boundary: the kinds that make up the family, one level per kind, each leaf naming the dir that decomposes it further. The organisms are decomposed by their own notes; the cross-cutting kinds (genome, molecular, cell, process) are decomposed once and referenced from each organism. The ecosystems the organisms form are not a branch of this tree — they are a `Natural System`, decomposed in [Ecosystems](/view.html?p=notes/nature/ecosystem/ecosystems.md).
>
> Identity: paths begin at `Ontic Element`, one labelled link per row; grouping types are `` `code` ``, instances Title Case.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` Organism | Self-maintaining, reproducing organization. Meso. |
| `Substantive` `(→ Kind)` Organism `(→ Part)` `Natural Object` | Grouping: the bounded bodies that compose an organism. |
| `Substantive` `(→ Kind)` Organism `(→ Part)` `Natural Object` `(→ Kind)` Cell | The membrane-bounded body carrying out the organism's operations. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Part)` `Natural Object` `(→ Kind)` Cell `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` | Grouping: the molecular constituents of the cell. |
| `Substantive` `(→ Kind)` Organism `(→ Part)` `Natural Object` `(→ Kind)` Cell `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Protein | Folded chain of amino acids carrying out the cell's work. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Part)` `Natural Object` `(→ Kind)` Cell `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Lipid | Amphiphilic molecule building membranes and storing energy. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Part)` `Natural Object` `(→ Kind)` Cell `(→ Part)` `Building Block` `(→ Has)` `Substance / Matter` `(→ Instance)` Carbohydrate | Sugar or polysaccharide: fuel and structural fibre. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Attribute)` `Property` | Grouping: what an organism carries. |
| `Substantive` `(→ Kind)` Organism `(→ Attribute)` `Property` `(→ Instance)` Genome | The inherited sequence an organism copies into its offspring. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Participation)` `Living Process` | Grouping: the transformations an organism performs. |
| `Substantive` `(→ Kind)` Organism `(→ Participation)` `Living Process` `(→ Instance)` Metabolism | The chemical transformations sustaining the organism's state. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Participation)` `Living Process` `(→ Instance)` Evolution | Heritable change of a lineage across generations. Macro. |
| `Substantive` `(→ Kind)` Organism `(→ Participation)` `Living Process` `(→ Instance)` Morphogenesis | The process that shapes the organism's form. Meso. |
| `Substantive` `(→ Kind)` Organism `(→ Kind)` Virus | Borderline member: a capsid-borne sequence that replicates only inside a host cell. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Kind)` Bacterium | Prokaryotic organism lacking a nucleus. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Kind)` Protist | Eukaryotic organism not a fungus, plant or animal. Micro. |
| `Substantive` `(→ Kind)` Organism `(→ Kind)` Fungus | Heterotrophic eukaryotic organism growing as filaments or single cells. Meso. |
| `Substantive` `(→ Kind)` Organism `(→ Kind)` Plant | Photosynthetic multicellular organism anchored to a substrate. Meso. |
| `Substantive` `(→ Kind)` Organism `(→ Kind)` Animal | Motile multicellular heterotroph feeding on other organisms. Meso. |

**Limitations.** *Complexity* and *Emergence* — every level (cell, organism, ecosystem) has properties none of its parts has. *Scale* — the same note name recurs at two levels (a cell in an organism, an organism as a cell in a colony). *Partial Observability* — the genome is read, not observed; a population is sampled, not enumerated.

**What is deliberately not here.** `organism/human/` holds the human instance of the same family — body, physiology, cognition and behaviour — filed inside the organisms because a human is an organism, not a sibling of life. `nature/ecosystem/` holds the systems organisms form with their environment, which are a `Natural System` rather than an organism. `matter/` holds the substances organisms are made of. `enzyme/` is its own dir, cross-linked from `molecular/`. Field names (`genetics`, `biochemistry`, `ecology`, `microbiology`) are refused: they are epistemic disciplines, and their notes live under `epistemica/`.

## References

- [How to decompose any natural instance?](/view.html?p=notes/philosophia-naturalis-et-operis.md)
- [Matter](/view.html?p=notes/nature/matter/matter.md) — the substances the family is built from
- [Physical Object](/view.html?p=notes/nature/body/physical-object.md) — the body side of the same ontic layer
- [Ecosystems](/view.html?p=notes/nature/ecosystem/ecosystems.md) — the systems organisms form with their environment, now on their own shelf
- [Human](/view.html?p=notes/nature/life/organism/human/human.md) — the human instance of the family
