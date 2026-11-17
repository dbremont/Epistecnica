---
tags: [note, nature, natural-system, biology, system, unfinished]
---

# Toxin

> **Note:** The concept of *toxin* is functional: it refers to a substance by virtue of its capacity to produce toxic effects. A toxin is therefore not a particular kind of substance defined by its composition, but one defined by its toxic activity.

## Formulation

### What is this ontic instance?

A toxin is a substance produced by a living organism that is harmful to another living organism at a dose the latter may actually encounter. Three clauses carry the whole definition, and each one does work. *Produced by a living organism* separates the toxin from the synthetic toxicant and from the mineral poison: arsenic is toxic and is not a toxin, and neither is dioxin. *Substance* keeps the term at the material level — a toxin is a molecule or a mixture of molecules, not a behaviour, a radiation, or an infection. *Harmful at an encountered dose* keeps the term functional and therefore dose-dependent: the same molecule is a toxin to a fish, a drug to a patient, and a reagent to a pharmacologist, and no compositional analysis decides which of those it is.

The consequence is that a toxin is not individuated by its chemistry. Two toxins with the same mechanism may share no structural feature, and a single structural family may contain toxins of ten different mechanisms. What individuates a toxin is the pair (molecule, target-in-context): the substance plus the living system it acts on. That is why the same compound appears under several headings in the literature — as a bacterial virulence factor, as a food contaminant, as a research tool, as a licensed drug — without contradiction.

### What ontic element type does this ontic instance belong to?

A toxin is a **Substance**: a continuous portion of matter individuated by its composition and its dispositions. Read against the natural-element taxonomy, the chain is `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin. The third step is a *kind* step, not a species step: the toxin kind is fixed by a disposition — the capacity to injure a living system — rather than by a composition class such as protein or alkaloid.

Readable as, but not primary:

- **readable as** a *Property* of matter — toxicity is a disposition, and a disposition is not a substance. This reading is true but too thin: it cannot carry the source, chemistry or mechanism of any particular toxin, and the whole comparative literature would disappear into it.
- **readable as** a *Natural Process* — poisoning, toxication, detoxification. This reading names what happens, not what is there; it belongs to the process branch of the decomposition, not to the root.
- **readable as** a *Technical Object* — a toxin purified, assayed, weaponised or licensed as a drug is a produced object. This is the technica reading of the same molecule and is filed in the technica corpus, not here.

### Is the type of this `ontic element instance` ambiguous?

Yes, in three places, and each ambiguity is resolvable by a decision rather than by a definition.

- **Toxin / toxicant / poison.** *Toxin* requires biological origin; *toxicant* does not; *poison* is the ordinary-language term covering both, and also covers the act of administering. The decision here: the note covers biologically produced substances, and admits a synthetic compound only where the literature treats it as the same substance class (for example, a synthetic analogue of a phycotoxin in a monitoring method).
- **Kind / instance.** "Toxin" names a kind; "botulinum neurotoxin serotype A" names an instance. The decomposition below is a kind-level tree whose leaves bind reference compounds; the full decomposition of one compound — its gene, fold, active site, pharmacokinetics — is the business of that compound's own note.
- **Substance / mixture.** Venoms and crude extracts are mixtures of substances; a single molecule is not. The tree keeps the substance as the unit and treats the mixture as an aggregation of substances plus a delivery system, which is why *venom* is a delivery term and does not appear as a toxin kind.

Unresolved and left open: whether prions and other non-replicating proteinaceous infectious agents belong to the kind. They are biologically produced, they are harmful, and they are not substances in the chemical sense the rest of the tree uses. The tree excludes them and records the exclusion here rather than widening the kind silently.

### Which limitation factors bound this description?

- **Complexity.** One molecule, many targets, several dose regimes. A toxin's identity is insufficient to predict its effect: the same compound acts differently by route, by species, by metabolic state.
- **Nonlinearity.** The dose–response is not reliably monotonic. Hormesis, thresholds, and cumulative effects under repeated exposure mean that a single acute LD₅₀ summarises almost nothing about chronic risk.
- **Partial observability.** Exposure in vivo is inferred, not observed: from biomarkers, from residues in a matrix, from symptoms. The parent compound in a sample may be the least toxic thing in it, because bioactivation happens in the host.
- **Uncertainty.** Species extrapolation, mixture effects, matrix effects and analogue blind spots in analytical methods each add error that no single study quantifies.
- **Many-body coupling.** Real exposure is to mixtures in a matrix — food, water, venom, dust — and the components interact pharmacokinetically and pharmacodynamically.
- **Scale.** The kind spans the molecule (binding site), the organ (target tissue), the organism (dose and route), the population (food chain, outbreak) and the ecosystem (algal bloom, crop contamination).

### What is the recursive instance decomposition of this ontic instance?

> Boundary: the toxin read as a functional kind of substance — the kind itself, the source classes, the chemical classes, the mechanism classes with their reference compounds, the properties by which toxins are compared, and the processes through which the harm is carried. The organism that makes a toxin, the organism it harms and the exposure pathway are related elements with their own notes, not parts of the kind. The molecular biology of a single toxin belongs to that toxin's own note; [nicotine](/view.html?p=notes/nature/life/molecular/nicotine.md) is the worked case of one compound decomposed in full.
>
> Stopping rule: a row is terminal when it names a kind, a reference compound, a measurable property, or a process.
>
> Identity: `Instance Tree Path` is the stable identifier of each row, and every path is unique. Level of organization: the molecule and its target site are **micro**; the organ, the organism and its defence are **meso**; the exposure route, the food chain and the population risk are **macro**. Limitation checklist exhibited by the kind: Complexity, Nonlinearity, Partial Observability, Uncertainty, Many-Body coupling, Scale.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin | Bound kind: stuff individuated by the capacity to harm a living system, not by composition. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Source Class | Grouping: the organism that makes it — the axis that fixes the ecology. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Source Class `(→ Kind)` Bacterial Toxin | Exotoxins secreted or injected by bacteria, and endotoxins released from their membranes. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Source Class `(→ Kind)` Fungal Toxin | Mycotoxins of moulds — aflatoxins, ochratoxins, trichothecenes, ergot alkaloids — the food-chain class. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Source Class `(→ Kind)` Plant Toxin | Phytotoxins made as defence: alkaloids, lectins, cyanogenic glycosides, terpenes. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Source Class `(→ Kind)` Animal Toxin | Zootoxins, delivered as venom by a bite or sting apparatus or carried in the tissues as a poison. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Source Class `(→ Kind)` Algal Toxin | Phycotoxins of dinoflagellates and cyanobacteria, concentrated up the food chain in shellfish and fish. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Chemical Class | Grouping: what it is made of — the axis that fixes stability and synthesis. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Chemical Class `(→ Kind)` Protein Toxin | Folded-chain toxins: pore formers, A–B toxins, ribosome inactivators, proteases. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Chemical Class `(→ Kind)` Peptide Toxin | Short disulfide-constrained peptides — conotoxins, microcystins — often more stable than proteins and more selective. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Chemical Class `(→ Kind)` Alkaloid Toxin | Nitrogen heterocycles that mimic or block neurotransmitters: tetrodotoxin, saxitoxin, nicotine, atropine. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Chemical Class `(→ Kind)` Polyketide Toxin | Polyketide-derived small molecules — aflatoxins, ochratoxins, okadaic acid — often requiring bioactivation. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Chemical Class `(→ Kind)` Glycolipid Toxin | Membrane glycolipids, of which lipid A of lipopolysaccharide is the reference case. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class | Grouping: what it does on reaching its target — the axis that fixes potency. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Pore-Forming Toxin | Inserts into membranes and assembles a channel; harm by osmotic and ionic collapse. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Pore-Forming Toxin `(→ Instance)` Alpha-Hemolysin | *Staphylococcus aureus* β-barrel heptamer; the reference pore former. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Pore-Forming Toxin `(→ Instance)` Anthrax Toxin | Protective antigen forms the pore through which lethal factor and edema factor enter. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Ion-Channel Blocker | Occupies the pore of a channel and stops conduction without damaging the membrane. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Ion-Channel Blocker `(→ Instance)` Tetrodotoxin | Site 1 of the voltage-gated sodium channel; the archetype of the class. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Ion-Channel Blocker `(→ Instance)` Saxitoxin | The same channel site reached from an algal source and concentrated by shellfish. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Ion-Channel Opener | Holds the channel open so the gradient runs down; persistent depolarisation. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Ion-Channel Opener `(→ Instance)` Batrachotoxin | Site 2 of the sodium channel; the poison-dart frog case. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Receptor Agonist | Mimics the endogenous ligand and keeps the receptor signalling. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Receptor Agonist `(→ Instance)` Nicotine | The plant alkaloid that opened the nicotinic receptor; a defence against insects and a drug in mammals. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Receptor Antagonist | Occupies the site without activating it; paralysis without excitation. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Receptor Antagonist `(→ Instance)` Alpha-Conotoxin | Subtype-selective blocker of nicotinic receptors; the scaffold that ziconotide's pharmacology descends from. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Protein-Synthesis Inhibitor | Disables the ribosome or an elongation factor; translation stops and the cell dies by attrition. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Protein-Synthesis Inhibitor `(→ Instance)` Ricin | Depurinates 28S rRNA; one A chain inactivates ribosomes catalytically. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Protein-Synthesis Inhibitor `(→ Instance)` Diphtheria Toxin | ADP-ribosylates elongation factor 2; the gene is carried by a lysogenic phage. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Protease Toxin | Cleaves one host protein and stops the pathway that protein carries. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Protease Toxin `(→ Instance)` Botulinum Neurotoxin | Cleaves SNAP-25, VAMP or syntaxin, blocking vesicle fusion; the most potent toxin known. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Protease Toxin `(→ Instance)` Tetanus Toxin | The same family, carried retrogradely to inhibitory interneurons: spastic rather than flaccid paralysis. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Enzyme Inhibitor | Binds the catalytic site of a phosphatase or kinase, so the modification it should remove accumulates. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Enzyme Inhibitor `(→ Instance)` Microcystin-LR | Inhibits protein phosphatases 1 and 2A; hepatotoxic and a tumour promoter. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Genotoxic Toxin | Unreactive until host metabolism converts it into a DNA-reactive electrophile. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Genotoxic Toxin `(→ Instance)` Aflatoxin B1 | CYP epoxidation gives the guanine adduct behind the TP53 hotspot mutation. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Immune Activator | The response itself is the injury: innate receptor engagement or superantigen bridging. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Kind)` Mechanism Class `(→ Kind)` Immune Activator `(→ Instance)` Lipopolysaccharide | Lipid A engages TLR4/MD-2; the driver of septic shock and the target of pyrogen testing. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Attribute)` Property | Grouping: the attributes by which toxins are compared. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Attribute)` Property `(→ Instance)` Potency | The dose at which the effect appears, spanning ten orders of magnitude across the kind. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Attribute)` Property `(→ Instance)` Target Selectivity | Which channel, receptor or enzyme subtype is engaged; the property that makes a toxin a tool. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Attribute)` Property `(→ Instance)` Route Dependence | The same substance is lethal by one route and inert by another; inhalation and injection bypass the gut barrier. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Attribute)` Property `(→ Instance)` Environmental Persistence | Heat stability and resistance to digestion decide whether cooking, storage or passage through the gut disarms it. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Attribute)` Property `(→ Instance)` Dose-Response Shape | Monotonic, thresholded, non-monotonic or cumulative: the form of the curve is a property of the substance in its context. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Occurrence)` Natural Process | Grouping: the processes through which the harm is carried. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Occurrence)` Natural Process `(→ Instance)` Toxication | Metabolic conversion of a pro-toxin into the reactive species — the step that leaves the parent compound innocent on a label. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Occurrence)` Natural Process `(→ Instance)` Detoxification | Conjugation, oxidation or excretion that clears the agent, and the genetic variation that makes it fast or slow. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Occurrence)` Natural Process `(→ Instance)` Target Binding | Occupation of the channel, receptor or enzyme site: the step whose affinity sets the potency. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Occurrence)` Natural Process `(→ Instance)` Membrane Damage | Pore assembly and lipid disruption, with osmotic collapse and calcium entry downstream. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Occurrence)` Natural Process `(→ Instance)` Cell Death | Apoptosis or necrosis following the primary lesion, at a delay set by the mechanism. |
| `Ontic Element` `(→ Kind)` `Substance` `(→ Kind)` `Substance / Matter` `(→ Kind)` Toxin `(→ Occurrence)` Natural Process `(→ Instance)` Immune Activation | Cytokine release, complement and inflammatory recruitment: the process by which the response becomes the disease. |

## What is th estructure of the toxin space?

> The space of toxins is cut by ten dimensions, and no single one of them orders it. A toxin is located by all of them at once: the same molecule sits at one point on each axis, and two toxins that share a source may share no mechanism. The dimensions below are the axes along which the literature actually compares toxins; a taxonomy that uses only one of them is a projection, not the space.

| Dimension | Description |
| --- | --- |
| **Origin** | Which organism makes it: bacterium, fungus, plant, animal, alga. This fixes the ecology, not the chemistry — a bacterial protein and a plant protein can share a mechanism down to the residue. |
| **Chemical class** | Protein, peptide, alkaloid, polyketide, terpenoid, glycolipid. This fixes stability, how it is synthesised, whether it survives cooking, and whether it can be made by fermentation or must be extracted. |
| **Molecular target** | The host molecule engaged: a voltage-gated channel, a nicotinic receptor, a SNARE protein, the ribosome, the cytoskeleton, DNA, a kinase, a phosphatase, the TLR4 complex. |
| **Mode of action** | What the toxin does on binding: forms a pore, blocks a pore, occupies a site, catalytically inactivates its target, damages membranes, or drives an immune response. |
| **Potency** | The dose at which the effect appears — LD₅₀, ED₅₀, Ki — spanning ten orders of magnitude, from nanograms per kilogram for botulinum neurotoxin to grams per kilogram for common plant alkaloids. |
| **Route** | How it enters: ingestion, inhalation, injection (bite, sting, wound), dermal contact, or maternal transfer. The same dose can be lethal by one route and inert by another. |
| **Kinetics** | Absorption, distribution, metabolic activation (toxication) or deactivation, and excretion. Aflatoxin B1 is far less harmful than its CYP-derived epoxide, and the epoxide is never the thing on the label. |
| **Dose–response shape** | Whether the response is monotonic, thresholded, non-monotonic (hormesis, the inverted U), or cumulative under repeated exposure. |
| **Selectivity** | Which species, tissue and cell type are hit. Selectivity is what turns a toxin into a drug and what makes animal models unreliable for human risk. |
| **Detectability** | Which assay finds it and at what limit: bioassay, immunoassay, mass spectrometry, receptor binding, or a cellular readout. |

## Which are the tokins in the tokin sapce?

> The rows below are exemplars, one or two per mechanism, chosen because each is the reference compound for its class. The dimension column is the projection of the axes above onto that row, which is why no two rows read alike.

| Toxin | Description | Dimension Characterization |
| --- | --- | --- |
| **Botulinum neurotoxin** | Zinc protease from *Clostridium botulinum* that cleaves SNAP-25, VAMP or syntaxin, blocking vesicle fusion at the neuromuscular junction; the most potent toxin known. | Bacterial · protein · SNARE protease · LD₅₀ ~1 ng/kg (mouse, i.p.) · oral or inhalational · flaccid paralysis · therapeutic at controlled dose |
| **Tetanus toxin** | The same protease family, carried retrogradely up motor neurons, cleaving VAMP in inhibitory interneurons; the loss of inhibition, not the loss of excitation, is the disease. | Bacterial · protein · protease · nanogram potency · wound route · spastic paralysis |
| **Tetrodotoxin** | Guanidinium alkaloid that plugs site 1 of voltage-gated sodium channels; the pufferfish toxin, and the reason fugu is a licensed knife skill. | Animal (and bacterial symbionts) · alkaloid · Naᵥ blocker · LD₅₀ ~10 µg/kg · oral · rapid paralysis · no antidote, supportive care only |
| **Saxitoxin** | The same channel site as tetrodotoxin, from dinoflagellates, concentrated by filter-feeding shellfish; paralytic shellfish poisoning. | Algal · alkaloid · Naᵥ blocker · µg/kg potency · oral · heat-stable · monitored by LC-MS/MS in shellfish |
| **α-Conotoxin** | Small disulfide-rich peptide from *Conus* venom that blocks nicotinic acetylcholine receptors by subtype; the scaffold behind ziconotide. | Animal · peptide · receptor antagonist · nM binding · injectional (sting) · subtype-selective · drug scaffold |
| **Ricin** | Type II ribosome-inactivating protein: the B chain binds galactose and lets the A chain depurinate 28S rRNA, shutting down translation. | Plant (*Ricinus communis*) · protein · ribosome inactivation · µg/kg by injection, far less by ingestion · catalytic (one A chain, many ribosomes) |
| **Diphtheria toxin** | A–B toxin that ADP-ribosylates elongation factor 2; the gene arrives with a lysogenic phage, so toxin production is a viral trait. | Bacterial · protein · enzyme inhibitor (eEF2) · ng/kg · respiratory or dermal · catalytic · vaccine-preventable |
| **Anthrax toxin** | Three-part system: protective antigen forms a pore that translocates lethal factor (a MAPKK protease) and edema factor (an adenylate cyclase). | Bacterial · protein · pore plus catalytic · pg/kg in combination · cutaneous or inhalational · the inhalational form is the biothreat |
| **Microcystin-LR** | Cyclic heptapeptide from cyanobacteria that inhibits protein phosphatases 1 and 2A; liver-specific because uptake is by organic-anion transporters. | Algal · peptide · enzyme inhibitor · µg/kg · oral (drinking water) · hepatotoxic · tumour promoter |
| **Aflatoxin B1** | Polyketide from *Aspergillus flavus*; the parent is largely inert until CYP450 epoxidises it into a DNA adduct, which is why chronic low dose is the real hazard. | Fungal · polyketide · genotoxic after bioactivation · µg/kg chronic · oral · IARC group 1 · food-chain contaminant |
| **Lipopolysaccharide** | Endotoxin of the Gram-negative outer membrane; the lipid A moiety engages TLR4/MD-2 and drives the cytokine cascade of septic shock. | Bacterial · glycolipid · immune activator · µg/kg · systemic · pyrogenic · heat-stable · a structural component, not a secreted toxin |
| **α-Hemolysin** | *Staphylococcus aureus* β-barrel pore former that assembles a heptamer in host membranes and lyses cells by osmotic collapse. | Bacterial · protein · pore former · µg/kg · tissue-invasive · stoichiometric, not catalytic |

## Mechanism of Toxic Action

> How is harm produced? Not by a single route: the mechanisms divide into those that act *stoichiometrically* — one molecule occupies one site — and those that act *catalytically* — one molecule disables many targets. That division explains the ten-order spread in potency better than any other single fact, because a catalyst needs to reach its target only once.

| Mechanism | Molecular action | Signature | Exemplar |
| --- | --- | --- | --- |
| **Pore formation** | Inserts into the membrane and assembles a channel, collapsing the ionic gradient. | Osmotic lysis, colloid osmotic swelling, calcium influx. | α-Hemolysin, anthrax protective antigen, streptolysin O |
| **Channel block** | Binds the selectivity filter or the outer pore of an ion channel and stops conduction. | Loss of excitability within seconds; no membrane damage. | Tetrodotoxin, saxitoxin (Naᵥ), ω-conotoxin (Caᵥ) |
| **Channel opening** | Locks the channel in the open state so the gradient runs down. | Persistent depolarisation, then inexcitability. | Batrachotoxin, grayanotoxin |
| **Receptor agonism** | Occupies an orthosteric site and mimics the endogenous ligand, often without desensitising. | Sustained signalling, then receptor down-regulation. | Nicotine at α4β2 nAChR, muscarine |
| **Receptor antagonism** | Occupies the site without activating it; competitive, or irreversible by covalent binding. | Paralysis without depolarisation. | α-Conotoxin, α-bungarotoxin |
| **Ribosome inactivation** | Depurinates a conserved adenine in 28S rRNA, so the ribosome can no longer bind elongation factors. | Translation arrest; a few A-chain molecules kill a cell. | Ricin, abrin, Shiga toxin |
| **Proteolysis of a host protein** | Cleaves a specific host substrate — a SNARE, a MAP kinase kinase — and the pathway it carries stops. | Loss of a single process (fusion, signalling) with the cell still alive. | Botulinum and tetanus neurotoxins, anthrax lethal factor |
| **Enzyme inhibition** | Binds the catalytic site of a phosphatase or kinase; the modification it should remove accumulates. | Cytoskeletal collapse, apoptosis, tumour promotion. | Microcystin-LR, okadaic acid |
| **Genotoxicity after bioactivation** | The parent is unreactive; host CYP enzymes convert it into an electrophile that adducts DNA. | Mutation spectrum with a hotspot, decades-long latency. | Aflatoxin B1, ochratoxin A |
| **Immune over-activation** | Engages an innate receptor or cross-links MHC and T-cell receptor, so the response itself is the injury. | Cytokine storm, hypotension, capillary leak. | Lipopolysaccharide (TLR4), staphylococcal superantigens |

> Two consequences follow. First, **antidote logic tracks the mechanism**: a channel blocker can sometimes be displaced by a competing ligand or washed out by perfusion, while a catalytic toxin needs the target resynthesised — which is why ricin and botulinum poisoning are managed supportively and immunologically rather than pharmacologically. Second, **the same mechanism is a drug target**: botulinum neurotoxin at nanogram doses treats dystonia and spasticity, ω-conotoxin MVIIA became the analgesic ziconotide, and the channel selectivity of conotoxins is a standard tool for identifying channel subtypes.

## QA

### Are there some heureitic to help to detect toxic sunstances?

> There is a ladder, and each rung answers a different question. Detecting a *known* toxin and discovering an *unknown* one are different problems, and most laboratory failures are a rung used for the wrong one.

1. **Clinical or ecological observation.** Symptoms, time course and exposure history narrow the candidate class before any instrument is used. A rapid-onset flaccid paralysis after a meal points to a channel or fusion blocker; a delayed hepatic injury points to a bioactivated hepatotoxin.
2. **Bioassay.** The mouse bioassay, or a larval or insect assay, establishes that *something* toxic is present without naming it; it remains the regulatory reference for botulinum and saxitoxin in several jurisdictions, and its weakness is exactly its strength — it sees analogues the antibody does not.
3. **Immunoassay.** ELISA and lateral-flow strips screen for one known epitope at low cost and high throughput. Fast, portable, and blind to anything the antibody was not raised against; cross-reactivity cuts both ways.
4. **Chromatography with mass spectrometry.** LC-MS/MS, and GC-MS for volatiles, is the confirmation rung: retention time plus fragmentation identifies the molecule and quantifies it. Targeted methods need a suspect list; untargeted acquisition plus spectral libraries is how new analogues are found.
5. **Functional and receptor assays.** Binding competition, patch clamp or a cell-viability readout measures activity rather than identity — the right rung when the question is "will this sample poison someone", not "what is in it".
6. **Structural identification.** NMR and high-resolution mass spectrometry for a compound with no entry in the library; this is the rung that turns a toxic sample into a new toxin.
7. **Computational and structural alerts.** Similarity to known toxicophores, docking against the target, and QSAR models prioritise candidates and flag metabolites that no assay covers — the toxication products are usually absent from the parent-compound library.
8. **Systems readouts.** Transcriptomic, proteomic and metabolomic signatures, organised as adverse-outcome pathways, detect the *effect* of an uncharacterised mixture and can separate a hazard from an adaptive response.

> Two cautions close the answer. **Assay scope is the limit of the claim**: an analytical method reports only compounds in its library, so "not detected" and "absent" are different statements. **Hazard is not risk**: detection of a toxin at a concentration below the effective dose for that exposure pathway establishes a hazard and not a risk, and the dose, route and kinetics axes above are what convert one into the other.

## Literature Review

> The literature on toxins is split by source rather than organised by mechanism, and the split has costs: the bacterial, mycotoxin, phycotoxin and venom literatures use different vocabulary, different potency units and different regulatory frameworks for the same chemical logic. The review below reads across them.

### What the word covers, and why the definition strains

The IUPAC glossary fixes the terms: a **toxin** is a substance produced by an organism and toxic to another, a **toxicant** is the broader class including synthetic agents, and **toxicity** is the capacity to cause injury (Duffus et al., 2007). The definition is functional, and the functional definition carries Paracelsus's problem with it — the dose makes the poison, so the same substance is a toxin, a drug and a nutrient at different exposures (Deichmann et al., 1986). The strain is visible in the lexicon: **venom** names a delivery system rather than a chemistry, **endotoxin** names a structural component rather than a secretion, and *toxin* in immunology names a superantigen. A taxonomy organised by composition therefore cannot hold the field together, which is why the space above is multi-dimensional.

### Mechanism: from stoichiometric to catalytic

The mechanistic literature divides along one axis that predicts potency. Pore-forming toxins are stoichiometric and architectural — they assemble in the membrane, and the lesion is the channel they make; the review by Dal Peraro and van der Goot remains the organising account of the family, from cholesterol-dependent cytolysins to the β-barrel hemolysins (Dal Peraro & van der Goot, 2016). Channel-blocking toxins are stoichiometric too, and their selectivity is what made them tools: tetrodotoxin's history is the history of the sodium channel (Narahashi, 2008), and the saxitoxin family shows the same site reached from an algal source with different pharmacokinetics (Wiese et al., 2010). The catalytic class is where the potency lives: botulinum and tetanus neurotoxins are zinc proteases that cleave a single SNARE protein, and the 1992 identification of synaptobrevin as the substrate reframed the clostridial diseases as proteolysis of the fusion machinery (Schiavo et al., 1992; Pirazzini et al., 2017). The same logic runs through ribosome-inactivating proteins, which depurinate 28S rRNA and shut down translation from a handful of molecules (Stirpe, 2004), and through the A–B toxins — diphtheria's ADP-ribosylation of elongation factor 2 and anthrax's translocation of a MAPKK protease plus an adenylate cyclase (Young & Collier, 2007; Henkel et al., 2010). Endotoxin sits at the opposite end: it need not enter a cell at all, and its harm is the receptor response it provokes (Raetz & Whitfield, 2002).

### Source biology and the coevolutionary account

Read by source, the field becomes an account of defence and counter-defence. Bacterial toxins are virulence factors whose genes often arrive by horizontal transfer — diphtheria toxin is phage-encoded — and whose regulation is tied to the infection context (Henkel et al., 2010). Mycotoxins are a food-chain problem: *Aspergillus* contamination of staple crops produces aflatoxins whose carcinogenicity is established through the CYP-activated epoxide and the TP53 mutation spectrum, in a fifty-year literature running from field epidemiology to mechanism (Bennett & Klich, 2003; Kensler et al., 2011). Plant toxins belong to chemical ecology, where the defensive function explains the diversity of alkaloids, cyanogenic glycosides and lectins better than any pharmacological classification does (Mithöfer & Boland, 2012). Venoms are the most studied case of an evolutionary arms race, with the "complex cocktail" view replacing the older one-toxin-one-effect picture: a single venom contains dozens of peptides recruited convergently and each tuned to a different target (Casewell et al., 2013).

### Dose, mixtures, and the limits of the single-toxin picture

The toxicological literature's own critique of itself is that single-substance, high-dose studies mislead. Hormesis — a stimulatory response at low dose and an inhibitory one at high dose — is widespread enough that Calabrese and Baldwin argued it should displace the monotonic default in risk assessment (Calabrese & Baldwin, 2003), and the argument is still contested on both mechanistic and regulatory grounds. Mixtures, matrix effects and chronic low-dose exposure are the normal case in food and environment, while the experimental literature is built on purified compounds and acute dosing. Bioactivation is where the gap matters most: the parent compound in a sample may be the least toxic thing in it.

### Detection, and the move to systems toxicology

Analytical detection has moved from the bioassay to targeted mass spectrometry to untargeted acquisition with spectral libraries, and each step narrows the blind spot while narrowing the claim: a targeted method cannot find what it was not built to find. In parallel, toxicology has moved from apical endpoints to pathway-level measurement — transcriptomic and high-content screening signatures organised as adverse-outcome pathways — in an attempt to predict hazard for compounds and mixtures that no targeted assay covers (Sturla et al., 2014). The two movements are complementary rather than competing: chemistry establishes identity, and pathway signatures establish effect.

### Toxins repurposed

The final movement is the one that complicates the word most: the same molecules are tools and drugs. Botulinum neurotoxin at controlled nanogram doses is a licensed therapeutic for dystonia and spasticity (Pirazzini et al., 2017); venom peptides became a drug-discovery platform, with ziconotide derived from a conotoxin and channel-subtype selectivity exploited across pharmacology (Lewis & Garcia, 2003). Selectivity — the property that makes a toxin dangerous to one target and harmless to another — is also the property that makes it useful, which is why the dimension that organises the mechanism table also organises the pharmacology.

## References

- [Toxin](https://en.wikipedia.org/wiki/Toxin)
- Bennett, J. W., & Klich, M. (2003). Mycotoxins. *Clinical Microbiology Reviews*, 16(3), 497–516. https://doi.org/10.1128/CMR.16.3.497-516.2003
- Calabrese, E. J., & Baldwin, L. A. (2003). Toxicology rethinks its central belief. *Nature*, 421(6924), 691–692. https://doi.org/10.1038/421691a
- Casewell, N. R., Wüster, W., Vonk, F. J., Harrison, R. A., & Fry, B. G. (2013). Complex cocktails: The evolutionary novelty of venoms. *Trends in Ecology & Evolution*, 28(4), 219–229. https://doi.org/10.1016/j.tree.2012.10.020
- Dal Peraro, M., & van der Goot, F. G. (2016). Pore-forming toxins: Ancient, but never really out of fashion. *Nature Reviews Microbiology*, 14(2), 77–92. https://doi.org/10.1038/nrmicro.2015.3
- Deichmann, W. B., Henschler, D., Holmstedt, B., & Keil, G. (1986). What is there that is not poison? A study of the Third Defense by Paracelsus. *Archives of Toxicology*, 58(4), 207–213. https://doi.org/10.1007/BF00297107
- Duffus, J. H., Nordberg, M., & Templeton, D. M. (2007). Glossary of terms used in toxicology, 2nd edition (IUPAC Recommendations 2007). *Pure and Applied Chemistry*, 79(7), 1153–1344. https://doi.org/10.1351/pac200779071153
- Henkel, J. S., Baldwin, M. R., & Barbieri, J. T. (2010). Toxins from bacteria. *Experientia Supplementum*, 100, 1–29. https://doi.org/10.1007/978-3-7643-8338-1_1
- Kensler, T. W., Roebuck, B. D., Wogan, G. N., & Groopman, J. D. (2011). Aflatoxin: A 50-year odyssey of mechanistic and translational toxicology. *Toxicological Sciences*, 120(S1), S28–S48. https://doi.org/10.1093/toxsci/kfq283
- Lewis, R. J., & Garcia, M. L. (2003). Therapeutic potential of venom peptides. *Nature Reviews Drug Discovery*, 2(10), 790–802. https://doi.org/10.1038/nrd1197
- Mithöfer, A., & Boland, W. (2012). Plant defense against herbivores: Chemical aspects. *Annual Review of Plant Biology*, 63, 431–450. https://doi.org/10.1146/annurev-arplant-042110-103854
- Narahashi, T. (2008). Tetrodotoxin: A brief history. *Proceedings of the Japan Academy, Series B*, 84(5), 147–154. https://doi.org/10.2183/pjab.84.147
- Pirazzini, M., Rossetto, O., Eleopra, R., & Montecucco, C. (2017). Botulinum neurotoxins: Biology, pharmacology, and toxicology. *Pharmacological Reviews*, 69(2), 200–235. https://doi.org/10.1124/pr.116.012658
- Raetz, C. R. H., & Whitfield, C. (2002). Lipopolysaccharide endotoxins. *Annual Review of Biochemistry*, 71, 635–700. https://doi.org/10.1146/annurev.biochem.71.110601.135414
- Schiavo, G., Benfenati, F., Poulain, B., Rossetto, O., Polverino de Laureto, P., DasGupta, B. R., & Montecucco, C. (1992). Tetanus and botulinum-B neurotoxins block neurotransmitter release by proteolytic cleavage of synaptobrevin. *Nature*, 359(6398), 832–835. https://doi.org/10.1038/359832a0
- Stirpe, F. (2004). Ribosome-inactivating proteins. *Toxicon*, 44(4), 371–383. https://doi.org/10.1016/j.toxicon.2004.05.004
- Sturla, S. J., Boobis, A. R., FitzGerald, R. E., Hoeng, J., Kavlock, R. J., Schirmer, K., Whelan, M., Wilks, M. F., & Peitsch, M. C. (2014). Systems toxicology: From basic research to risk assessment. *Chemical Research in Toxicology*, 27(3), 314–329. https://doi.org/10.1021/tx400410s
- Wiese, M., D'Agostino, P. M., Mihali, T. K., Moffitt, M. C., & Neilan, B. A. (2010). Neurotoxic alkaloids: Saxitoxin and its analogs. *Marine Drugs*, 8(7), 2185–2211. https://doi.org/10.3390/md8072185
- Young, J. A. T., & Collier, R. J. (2007). Anthrax toxin: Receptor binding, internalization, pore formation, and translocation. *Annual Review of Biochemistry*, 76, 243–265. https://doi.org/10.1146/annurev.biochem.75.103004.142728
