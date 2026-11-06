# Chemical Space


> **Chemical space** refers to the vast, multidimensional set of all possible chemical compounds, including both known molecules and hypothetical ones that could potentially exist.
> 

## Space Dimension

> How to map a molecule to the space (molecule fingerprinting)? How to map a point in the space to a molecule?
> 

> Each molecule is a point in this multidimensional descriptor space.
> 

> Chemical space is often conceptualized as a high-dimensional space where each dimension corresponds to a molecular descriptor or property, such as:
> 

| **Descriptor Category** | **Description** | **Example Descriptors** |
| --- | --- | --- |
| **Physicochemical Properties** | Quantitative measures of molecular physical and chemical characteristics | Molecular weight, LogP (hydrophobicity) |
| **Hydrogen Bonding** | Capacity to donate or accept hydrogen bonds | Number of hydrogen bond donors/acceptors |
| **Topological Indices** | Graph-based descriptors reflecting molecular connectivity and shape | Wiener index, Balaban index |
| **Functional Groups** | Presence or absence of specific chemical groups | Hydroxyl, amine, carboxyl |
| **Electronic Properties** | Electron distribution related descriptors | Partial charges, polarizability |
| **Geometric Descriptors** | 3D shape and spatial arrangement parameters | Molecular volume, surface area |

## **Applications**

- **Drug discovery:** Searching chemical space for molecules with desired biological activities.
- **Materials science:** Identifying new materials with specific properties.
- **Cheminformatics:** Visualization, navigation, and clustering of chemical space using computational methods.
- **De novo design:** Algorithms generate molecules to explore uncharted regions of chemical space.

## **Challenges**

- **Vastness:** Impossible to enumerate or test every molecule.
- **Sampling:** Need efficient algorithms to explore relevant regions of chemical space.
- **Representation:** Choice of descriptors or fingerprints affects how chemical space is understood and navigated.

## Chemical Taxonomy

> **Chemical Taxonomy** refers to the systematic classification of chemical substances based on their structural, functional, physicochemical, or biosynthetic properties. It provides a hierarchical or categorical framework to organize the vast diversity of chemical entities—ranging from small molecules to polymers, from natural products to synthetic compounds.
> 

### Formal

| **Category** | **Taxonomy** | **Description** |
| --- | --- | --- |
| **Ontology-Based** | **ChEBI** | Structured biological ontology with formal class hierarchies and relationships. |
| **Automated Structural** | **ClassyFire** | Rule-based hierarchical classification from molecular structure (superclass, class, subclass). |
| **Biomedical** | **MeSH (Chemicals)** | Vocabulary of biomedical chemicals: drugs, toxins, hormones, etc. |
| **Cheminformatics** | **PubChem Classifications** | Structural, functional, and property-based clusters used in cheminformatics. |
| **Functional / Pathway** | **KEGG Compound** | Molecules classified by roles in metabolic and signaling pathways. |
| **Pharmacological** | **ATC System** | Drug classification based on therapeutic application and target system. |
| **Regulatory / Industrial** | **CAS Registry, EC Number, UNII** | Formal IDs and classifications for regulatory, safety, and commercial purposes. |
| **Natural Products** | **NPClassifier** | Classifies natural compounds by biosynthetic origin (e.g., alkaloids, polyketides). |

### Informal

| **Category** | **Taxonomy/System** | **Description** |
| --- | --- | --- |
| **By Functional Group** | *Alcohols, Ketones, Amines* | Grouped by presence of key functional groups; widely used in organic chemistry. |
| **By Structural Motif** | *Aromatics, Heterocycles* | Based on core molecular architecture like rings or fused systems. |
| **By Molecular Class** | *Polymers, Surfactants* | Used in materials and industrial chemistry for broad types of substances. |
| **By Application Domain** | *Dyes, Explosives, Drugs* | Based on usage or industry (e.g., medicinal, agricultural, electronic). |
| **By Physical Properties** | *Volatile, Hydrophobic* | Heuristic grouping for laboratory handling and modeling. |
| **By Biosynthetic Origin** | *Terpenes, Alkaloids* | Common in natural product and metabolomics contexts. |
| **By Toxicity or Risk** | *Carcinogens, Irritants* | Informal grouping for safety or regulatory shorthand. |

| **Taxonomy Type** | **Subspace** | **Basis / Origin / Description** |
| --- | --- | --- |
| **Inorganic Compounds** | **Oxides** | Oxygen-containing inorganic compounds |
|  | **Salts** | Ionic compounds from acid–base reactions |
|  | **Acids & Bases** | Proton donors/acceptors |
|  | **Coordination Compounds** | Metal-ligand complexes |
|  | **Alloys** | Metallic mixtures |
|  | **Ions and Electrolytes** | Charged species in solution or solid phase |
|  | **Gases** | Volatile small molecules |
| **Organic Structures** | **Hydrocarbons** | Carbon skeletons (saturated/unsaturated/aromatic) |
|  | **Heteroatom-Containing** | Atoms other than C/H (e.g., N, O, halogens) |
|  | **Carbonyl Compounds** | Carbon double bonded to oxygen (C=O) |
|  | **Aromatic Compounds** | Compounds with delocalized π-systems |
|  | **Organometallics** | Compounds with metal–carbon bonds |
|  | **Fluorinated Compounds** | Highly fluorinated organics for stability |
|  | **PAHs (Polycyclic Aromatic Hydrocarbons)** | Multi-ring aromatics, often environmental pollutants |
|  | **Silicon-Based Molecules** | Organosilicon compounds |
|  | **Surfactants** | Amphiphilic molecules with self-assembly behavior |
| **Natural Products** | **Alkaloids** | Amino acid-derived; nitrogen-containing |
|  | **Terpenes** | Made from isoprene units |
|  | **Phenolics** | Derived from shikimate or phenylpropanoid pathways |
|  | **Polyketides** | Derived from acetate units |
|  | **Glycosides** | Sugar-linked small molecules |
|  | **Toxins / Venoms** | Toxic bioactive natural products |
|  | **Endogenous Metabolites** | Naturally occurring small molecules in metabolism |
| **Biomacromolecules** | **Peptides / Oligopeptides** | Short amino acid chains |
|  | **Proteins** | Large polypeptides with tertiary/quaternary structure |
|  | **Nucleotides / Nucleic Acids** | DNA/RNA bases and polymers |
|  | **Carbohydrates** | Sugars and polysaccharides |
|  | **Lipids** | Fatty acids, steroids, phospholipids |
|  | **Polymers** | Long repeating units (natural or synthetic) |
|  | **Macrocycles** | Large ring systems with conformational rigidity |
| **Pharmaceutical Space** | **Small Molecules** | Drug-like compounds (<900 Da) |
|  | **Synthetic Drugs** | Medicinally optimized, often structure-driven molecules |
|  | **Prodrugs** | Inactive compounds that metabolize into active forms |
|  | **Scaffold-Based Classes** | Groups based on shared core ring/backbone structures |
|  | **Fragment-Like Molecules** | Very small molecules (<300 Da) used in fragment-based drug discovery |
| **Reactive / Functional** | **Reactive Intermediates** | Short-lived species in reaction mechanisms |
|  | **Fluorophores / Chromophores** | Light-responsive molecules used in spectroscopy/imaging |
| **Structure** |  |  |
|  | **Elemental Substances** |  |
|  | **Binary Compounds** |  |
|  | **Ternary and Higher** |  |
|  | **Coordination Compounds** |  |
|  | **Polyatomic Ions** |  |
|  | **Polymers** |  |
|  | **Crystalline Solids** |  |
|  | **Amorphous Solids** |  |
| Applications |  |  |
|  |  |  |
|  | **Biochemicals** |  |
|  | **Pharmaceuticals** |  |
|  | **Petrochemicals** |  |
|  | **Agrochemicals** |  |
|  | **Industrial Chemicals** |  |
|  | **Explosives** |  |
|  | **Dyes / Pigments** |  |
|  | **Nanomaterials** |  |
|  | **Semiconductors** |  |

## Related Concepts

- **Chemical Universe:** Sometimes used interchangeably with chemical space, but can imply all conceivable molecules without regard to stability or synthesizability.
- **Drug-like Chemical Space:** A smaller, more focused subset of chemical space with properties suitable for drug candidates (e.g., Lipinski’s rule of five).
- **Molecular Descriptors:** Numeric or categorical values summarizing molecular structure/properties, used to define coordinates in chemical space.

## References

- [https://en.wikipedia.org/wiki/Chemical_space](https://en.wikipedia.org/wiki/Chemical_space)
- https://en.wikipedia.org/wiki/Cheminformatics
- Reymond, Jean-Louis. "The chemical space project." Accounts of chemical research 48.3 (2015): 722-730.
- Gromski, Piotr S., et al. "How to explore chemical space using algorithms and automation." Nature Reviews Chemistry 3.2 (2019): 119-128.
- Oprea, Tudor I., and Johan Gottfries. "Chemography: the art of navigating in chemical space." Journal of combinatorial chemistry 3.2 (2001): 157-166.
- https://en.wikipedia.org/wiki/List_of_chemical_classifications
- [https://pubchem.ncbi.nlm.nih.gov/](https://pubchem.ncbi.nlm.nih.gov/)
- https://en.wikipedia.org/wiki/List_of_chemical_databases
- https://library.ch.cam.ac.uk/list-useful-databases
- https://www.ebi.ac.uk/chembl/
- http://crdd.osdd.net/chemdatabase.php
- https://go.drugbank.com/
