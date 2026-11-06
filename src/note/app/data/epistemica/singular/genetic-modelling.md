# Genetic Modelling


> Genetic modeling is the study of how genes and their interactions manifest in the observable traits and variation of organisms.
> 

> Note: Genetic modeling assumes traits result from genetics, environment, and their interactions, but the genome is more like a construction guide than a finished product—so the same genetic ‘program’ can produce very different outcomes.
> 

Key Questions:

- What is the relationship between genetic information and observable traits in an organism or population?
- How to use **genes information** to infer properties of the organism?
- What is the relationship between genetic information and observable traits in an organism or population?
- How do interactions among multiple genes (epistasis) influence traits?
- What is the `environment`?
- What is the relative contribution of genetics versus environment to trait variation?
- How do allele frequencies change over time within populations under selection, drift, or migration?
- How can genetic models predict the risk of disease or other complex traits in individuals?
- How can population-level genetic data inform predictions about individual phenotypes?
- How do mutations, recombination, and other genomic processes shape variation?
- How can computational models integrate multi-gene, multi-environment, and epigenetic data?
- How can genetic modeling guide breeding, conservation, or medical interventions?
- What does the term ‘Variation’ means? What type of variations are there?
- What does the term ‘Heritability’ means?
- How should we think about traits and genetics in a population with relatively fixed genetics, such as Sweden or Finland, comparing 1500 and 2020?

## Field

> Which are the Academic Field that do ‘Genetic Modelling’?
> 

| Field | Description | Note |
| --- | --- | --- |
| **Classical Genetics (Mendelian Genetics)** | Studies inheritance patterns of discrete traits and how alleles are transmitted across generations. | Foundation of all genetic modeling; focuses on single-gene traits. |
| **Quantitative Genetics** | Analyzes traits influenced by multiple genes and environmental factors, estimating heritability and genetic variance. | Key for understanding complex traits like height, yield, or behavior. |
| **Population Genetics** | Examines allele frequency changes over time in populations under the influence of selection, drift, mutation, and migration. | Central to evolution, conservation biology, and breeding programs. |
| **Genomics (Computational Genetics)** | Uses high-throughput sequencing data and computational models to map genes to traits, identify variants, and simulate genetic processes. | Includes GWAS, polygenic risk scores, and genome-wide simulations. |
| **Epigenetics** | Studies heritable changes in gene expression that do not involve changes in DNA sequence, such as methylation and histone modification. | Bridges genetics with environmental influences on trait expression. |
| **Systems Genetics** | Models the complex interactions between genes, proteins, and pathways to understand trait emergence. | Integrates network analysis, dynamic modeling, and multi-omics data. |

## Ontology

> Which is the structure of the investigated reality?
> 

| Element | Description | Tags | Ontological Nature |
| --- | --- | --- | --- |
| **Gene** | Basic unit of heredity; a DNA sequence encoding a functional product (protein or RNA). | Molecular, Hereditary, Genetic Information | Entity |
| **Allele** | Variant form of a gene at a specific locus. | Genetic Variation, Population Genetics | Entity |
| **Genome** | Complete set of genetic material in an organism. | Molecular, Systems, Blueprint | Entity |
| **Trait (Phenotype)** | Observable characteristic or feature of an organism, resulting from genes, environment, and interactions. | Phenotypic, Observable, Complex Trait | Property |
| **Environment** | All external factors influencing trait expression beyond DNA, including nutrition, climate, social and cultural context. | External Factor, Modifier, Context | Effective Idea - Approximation - Potential |
| **Epigenetic Modification** | Heritable change in gene expression not caused by DNA sequence alteration (e.g., methylation, histone modification). | Regulatory, Heritable, Environmental Interaction | Process / Property |
| **Population** | Group of interbreeding individuals in a defined area. | Demography, Genetics, Evolutionary Unit | Group |
| **Allele Frequency** | Proportion of a specific allele in a population. | Population Genetics, Evolution, Quantitative Measure | Property / Measure |
| **Heritability (h²)** | Fraction of phenotypic variation in a trait attributable to genetic variation in a population. | Quantitative Genetics, Variance, Trait Prediction | Property / Measure |
| **Genetic Interaction  (Epistasis)** | Phenomenon where the effect of one gene depends on the presence of one or more other genes. | Gene Interaction, Complex Trait, Systems | Interaction / Relation |
| **Mutation** | Permanent change in the DNA sequence. | Variation, Evolution, Molecular Event | Process / Event |
| **Recombination** | Exchange of genetic material during meiosis, generating novel allele combinations. | Genetic Variation, Evolution, Molecular Process | Process / Event |
| **Polygenic Trait** | Trait influenced by many genes, often with small effects. | Complex Trait, Quantitative Genetics | Property / Emergent Feature |

## Task Space

> Which are the types of modelling tasks?
> 

| Category | Task | Description | Goal |
| --- | --- | --- | --- |
| **Predictive Modeling** | Trait Prediction | Use genetic and environmental data to predict individual or population-level traits. | Forecast phenotypes, disease risk, or performance. |
| **Variance Decomposition** | Heritability Estimation | Quantify the relative contributions of genetics, environment, and their interactions to trait variation. | Understand sources of phenotypic variation. |
| **Population Modeling** | Allele Frequency Dynamics | Model changes in allele frequencies over generations under selection, drift, mutation, or migration. | Predict evolutionary trajectories and population diversity. |
| **Gene–Environment Interaction Analysis** | G×E Modeling | Analyze how genetic effects vary depending on environmental context. | Identify context-dependent genetic influences on traits. |
| **Functional Modeling** | Pathway / Network Analysis | Map genetic variants to biological pathways, regulatory networks, or systems affecting traits. | Understand biological mechanisms linking genes to phenotypes. |
| **Simulation** | Synthetic Populations | Create simulated populations or developmental scenarios to test hypotheses. | Explore theoretical outcomes, validate models, and study rare scenarios. |
| **Intervention Modeling** | Environmental Manipulation | Test effects of controlled environmental changes or interventions on traits. | Assess potential interventions, policy impacts, or treatment strategies. |
| **Association Studies** | GWAS / QTL Mapping | Identify genetic loci associated with traits using population data. | Discover candidate genes and genomic regions influencing traits. |
| **Polygenic Modeling** | Polygenic Risk Scores / Multi-gene Models | Aggregate effects of many small-effect variants to predict complex traits. | Improve predictive power for highly polygenic traits. |
| **Longitudinal & Developmental Modeling** | Growth Trajectories / Life-course Modeling | Model how traits develop over time under genetic and environmental influences. | Understand developmental dynamics and timing of genetic effects. |
| **Cross-population Modeling** | Comparative or Meta-population Studies | Compare genetic effects across populations or environments. | Evaluate generalizability of genetic models and detect population-specific effects. |

## Technique Space

> Which are the techniques used?
> 

| Technique | Description | Task | Evaluation |
| --- | --- | --- | --- |
| **Statistical Proxies** | Use measurable variables (e.g., socioeconomic status, education, nutrition) as indicators of broader environmental effects. | G×E modeling, Predictive modeling | Simple and practical, but may miss unmeasured factors; relies on quality of proxies. |
| **Longitudinal Studies** | Track traits and environmental exposures over time to capture developmental dynamics. | Longitudinal & developmental modeling, variance decomposition | Captures temporal effects; requires long-term data collection; expensive. |
| **Experimental Designs** | Randomized or controlled interventions to isolate causal effects. | Intervention modeling, G×E modeling | Provides causal inference; may be limited in scale or generalizability. |
| **Multi-level Models** | Integrate individual, family, and population-level factors in hierarchical models. | G×E modeling, trait prediction | Captures nested effects; computationally intensive; requires sufficient data. |
| **GWAS / QTL Mapping** | Identify genetic loci associated with traits using population-level genotype–phenotype data. | Association studies, predictive modeling | Effective for single-locus effects; limited for small-effect or rare variants. |
| **Polygenic Risk Scores (PRS)** | Aggregate effects of many small-effect variants to predict complex traits. | Polygenic modeling, trait prediction | Improves prediction for polygenic traits; accuracy depends on large reference datasets. |
| **Mixed Models / Linear Mixed Models (LMM)** | Account for both fixed and random effects (e.g., population structure, family relatedness). | Variance decomposition, G×E modeling, GWAS | Reduces confounding; widely used; assumptions may be restrictive. |
| **Simulation / Synthetic Populations** | Generate virtual populations or developmental scenarios under controlled assumptions. | Simulation, intervention modeling | Useful for testing hypotheses; results depend on model assumptions. |
| **Network / Pathway Analysis** | Model gene–gene, gene–environment, or protein–pathway interactions. | Functional modeling, G×E modeling | Captures complex interactions; requires high-quality omics data. |
| **Machine Learning / Predictive Models** | Use algorithms (e.g., random forests, neural networks) to predict traits from genetic and environmental data. | Predictive modeling, polygenic modeling | Can capture complex patterns; may overfit and lack interpretability. |
| **Meta-analysis / Cross-population Modeling** | Combine datasets across studies or populations to detect consistent effects. | Cross-population modeling, GWAS | Increases power and generalizability; heterogeneity may complicate results. |

## Environment

> How to think about the environment (nature)?
> 

> In genetic modeling, the **environment** includes all external factors that influence trait development **beyond DNA sequence**. This can range from nutrition, climate, social interactions, and cultural context to early-life experiences.
> 

> For very complex traits like ‘Cognitive Capacities,’ how can we even define or model the environment?
> 

> Note: **Since the environment** is, by definition, everything that may influence a trait and is often not fully known, we must make assumptions about it. When reading genetic modeling analyzes, pay close attention to how the environment is represented, as this can dramatically impact the study’s results.
> 

### Modelling

> How to techniques to model the environment?
> 

| Technique | Description |
| --- | --- |
| **Statistical Proxies** | Use measurable variables (e.g., socioeconomic status, education, nutrition) as indicators of broader environmental effects. |
| **Longitudinal Studies** | Track environmental exposures over time to model developmental trajectories and changes across life stages. |
| **Experimental Designs** | Employ randomized interventions or controlled studies to isolate specific environmental effects. |
| **Multi-level Models** | Integrate individual, family, and population-level factors to capture hierarchical and contextual influences. |

### Challenge(s)

> Which are the challenges in identifying the ‘Environment’?
> 

| Challenge | Description | Treatment |
| --- | --- | --- |
| **Multiplicity of Factors** | Environment is not a single variable but a constellation of influences that may interact with each other and with genes. | Use multi-factor models and statistical methods to capture interactions; decompose environment into measurable components. |
| **Measurement Difficulty** | Many environmental effects (e.g., parenting quality, cultural exposure) are hard to measure accurately or consistently. | Develop reliable proxies, standardized surveys, and longitudinal tracking; use repeated measurements to reduce noise. |
| **Dynamic Nature** | Environmental conditions can change over time, influencing development at different life stages. | Employ longitudinal studies and time-dependent modeling to capture temporal variation. |
| **Gene–Environment Interactions (G×E)** | Genes may have different effects depending on environmental context, complicating separation of genetic vs. environmental contributions. | Incorporate interaction terms in statistical models; use experimental or quasi-experimental designs when possible. |
| **Cultural and Social Dimensions** | In traits like cognition, social structures, education, and cultural practices are crucial but challenging to operationalize. | Use multi-level models integrating individual, family, and societal factors; consider qualitative and quantitative data integration. |

## Use

> Which are the current used of  of genetic - observable inferences?
> 

| Use | Description | Evaluation |
| --- | --- | --- |
| **Medical Genetics / Personalized Medicine** | Predict disease risk, drug response, or predisposition based on genetic information. | Highly impactful; increasingly accurate for monogenic disorders; polygenic traits still challenging. |
| **Breeding and Agriculture** | Guide selective breeding of plants and animals for desirable traits (yield, resistance, behavior). | Widely used; effectiveness depends on trait heritability and genetic knowledge. |
| **Evolutionary and Population Studies** | Understand how traits and genetic variation evolve over time in populations. | Core tool in evolutionary biology; relies on accurate population data. |
| **Conservation Biology** | Identify genetic diversity and guide preservation of endangered species. | Useful for maintaining genetic health of populations; limited by available genetic samples. |
| **Behavioral and Social Genetics** | Study genetic contributions to behavioral or cognitive traits. | Provides insight but limited by environmental confounding and ethical considerations. |
| **Functional Genomics / Systems Biology** | Link genetic variants to biological pathways and trait mechanisms. | Helps understand trait biology; requires integration of multi-omics data. |
| **Forensics and Ancestry** | Infer individual identity, familial relationships, or population origin. | Reliable for identification; ancestry inference can be probabilistic and population-dependent. |
| **Drug Discovery / Pharmacogenomics** | Identify genetic targets or predict adverse drug reactions. | Growing field; relies on accurate genotype–phenotype maps and large datasets. |

## Limitation

> Which are the limitations of genetic - observable inferences?
> 

| Limitation | Description | Note |
| --- | --- | --- |
| **Environmental Influence** | Traits are influenced not only by genetics but also by environmental factors, making predictions uncertain. | Particularly relevant for complex traits like behavior, height, or disease susceptibility. |
| **Epistasis and Gene Interactions** | Interactions among multiple genes can produce non-additive effects on traits. | Simple additive models may fail to capture these effects. |
| **Incomplete Genetic Knowledge** | Not all causal genes or variants for a trait are known. | Limits predictive accuracy, especially for polygenic traits. |
| **Population-Specific Effects** | Genetic effects may differ across populations due to allele frequency differences or gene–environment interactions. | Models trained on one population may not generalize. |
| **Pleiotropy** | A single gene may influence multiple traits. | Can complicate interpretation of gene–trait relationships. |
| **Epigenetic Modifications** | Heritable changes in gene expression can alter traits without changing DNA sequence. | Classical genetic models may miss these effects. |
| **Measurement and Data Noise** | Phenotypic traits and genotypes can be measured with error. | Reduces accuracy of inferred relationships. |
| **Limited Predictive Power for Complex Traits** | Polygenic traits with small-effect variants are difficult to predict accurately. | Requires large datasets and sophisticated statistical models. |

## References

- [Gene](https://app.notion.com/p/Gene-115c0f5171ec80abb2e2d855b7a787b0?pvs=21)
- https://en.wikipedia.org/wiki/Genetics
- [‣](https://app.notion.com/p/10e598edb7908141b53dd03620c3d5eb?pvs=21)
