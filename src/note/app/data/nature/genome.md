---
tags: [nature, natural-system, biology, system]
---

# Genome

> A **genome** is the complete set of an organism’s DNA, including all of its genes and non-coding sequences, that carries the instructions for growth, development, and function.
>

> …
>

## Index

## Genome Structure

> The complete set of genetic material in an organism, including all of its genes and non-coding sequences.
>

> **Size**: Varies widely between organisms (e.g., bacteria have smaller genomes compared to eukaryotes).
>

> **Density**: Eukaryotic genomes are less densely packed due to the presence of introns and non-coding regions, while prokaryotic genomes are more compact.
>

> **Repetitive Sequences**: Include transposable elements and satellite DNA, influencing genome evolution and stability.
>

### **Components of Genome Structure**

| **Component** | **Description** |
| --- | --- |
| **Chromosomes** | Large DNA molecules that contain genes; organized as linear structures in eukaryotes and circular in prokaryotes. |
| **Chromatin** | DNA packaged with histone proteins in eukaryotes, forming nucleosomes that compact into chromatin. |
| **Genes** | Functional units of heredity made up of sequences that code for proteins or functional RNA. |
| **Exons** | Coding sequences of a gene that are transcribed into mRNA and translated into proteins. |
| **Introns** | Non-coding sequences within a gene that are transcribed but removed during RNA processing. |
| **Regulatory Elements** | DNA sequences (promoters, enhancers, silencers) that control gene expression. |
| **5' Untranslated Region (5' UTR)** | The non-coding region upstream of the coding sequence that helps regulate translation. |
| **3' Untranslated Region (3' UTR)** | The non-coding region downstream of the coding sequence that affects mRNA stability and translation efficiency. |
| **Repetitive DNA** | Sequences that occur in multiple copies, including tandem repeats and transposable elements. |
| **Mitochondrial/Chloroplast DNA** | Small circular genomes found in organelles, inherited maternally in most species. |
| **Operon** | … |

### **Genome Structure in Different Organisms**

| **Organism Type** | **Genome Structure** |
| --- | --- |
| **Prokaryotes** | Typically consist of a single circular chromosome and may contain plasmids. |
| **Eukaryotes** | Composed of multiple linear chromosomes, with a more complex structure involving chromatin. |
| **Viruses** | Can have either DNA or RNA genomes, which can be single-stranded or double-stranded, and linear or circular. |

## Representations

> …
>

| **Format** | **File Extension** | **Description** | **Best For** | **Example Tools** |
| --- | --- | --- | --- | --- |
| **FASTA** | `.fna`, `.fa`, `.fasta` | Plain text format storing nucleotide/protein sequences with headers | Storing raw DNA/RNA/protein sequences | BLAST, BioPython, EMBOSS |
| **GenBank** | `.gb`, `.gbff` | Annotated genome format with sequence, genes, and metadata | Functional and comparative genomics | GenBank, SnapGene, Artemis |
| **GFF (General Feature Format)** | `.gff`, `.gff3` | Describes genomic features like genes, exons, and regulatory elements | Genome annotation and visualization | BEDTools, GMOD, IGV |
| **BED (Browser Extensible Data)** | `.bed` | Compact format listing genomic regions with start/end positions | Storing large feature sets, like SNPs and exons | UCSC Genome Browser, BEDTools |
| **VCF (Variant Call Format)** | `.vcf` | Stores genetic variations (SNPs, indels, structural variants) | Genome-wide association studies (GWAS), mutation analysis | GATK, bcftools, ANNOVAR |
| **SAM/BAM (Sequence Alignment/Map)** | `.sam`, `.bam` | Aligns sequencing reads to a reference genome (BAM is compressed SAM) | Storing and analyzing high-throughput sequencing data | SAMtools, IGV, BWA |
| **CRAM** | `.cram` | Compressed alternative to BAM, reducing file size | Storing sequencing alignments efficiently | SAMtools, CRAMtools |
| **BigWig** | `.bw` | Stores continuous numerical genome data (e.g., coverage tracks) | Visualizing sequencing depth, ChIP-seq, RNA-seq | UCSC Genome Browser, deepTools |
| **BigBed** | `.bb` | Compressed BED format for large genomic feature datasets | Genome browser visualization | UCSC tools, BEDTools |
| **GVF (Genome Variation Format)** | `.gvf` | Variant format with richer annotations than VCF | Storing and analyzing genome variants | Ensembl, NCBI tools |
| **AGP (A Golden Path)** | `.agp` | Describes genome assembly structure | Genome assembly representation | NCBI, AGP utilities |
| **JSON (BioJSON, GA4GH)** | `.json` | Structured genome data for API and web applications | Data sharing and programmatic access | GA4GH APIs, Ensembl REST API |
| **XML (BioXML, BSML)** | `.xml` | Stores biological sequence and annotation data in hierarchical format | Interoperability between databases | NCBI XML, BioPerl |

## References

- https://en.wikipedia.org/wiki/Genome
- https://en.wikipedia.org/wiki/Operon
- [FASTA Format](https://app.notion.com/p/FASTA-Format-1a1c0f5171ec808ab05dc204177d7fe5?pvs=21)
- https://en.wikipedia.org/wiki/Whole_genome_sequencing
- https://www.genomicsengland.co.uk/genomic-medicine/understanding-genomics

## Related

- [Gene](note.html?n=nature/gene.md)
- [Epigenome](note.html?n=nature/epigenome.md)
- [Leptospira](note.html?n=nature/leptospira.md)
- [Human Genome](note.html?n=nature/human-genome.md)
- [Living System](note.html?n=nature/living-system.md)

## Provenance

- Notion export: `Modelo/Nature/Conceptual Model Natural System/Genome 1a1c0f5171ec807eab03e14fd9d92da8.md`
