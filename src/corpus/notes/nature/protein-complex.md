---
tags: [note, nature, natural-system, biology, biochemistry, molecule, system]
qa:
 - When does a set of proteins stop being a set and start being a complex?
 - What holds a protein complex together, and how is that different from a crystal packing?
 - Why does a complex enable a function none of its subunits performs?
 - Is the ribosome a protein complex, a ribonucleoprotein, or a machine?
 - How does the cell keep assembly from producing garbage?
---

# Protein Complex

> A **protein complex** is a set of two or more polypeptide chains that associate with one another and act as one functional unit: the haemoglobin tetramer that cooperates in binding oxygen, the ribosome that translates, the proteasome that degrades, ATP synthase that turns a proton gradient into bond energy. What makes it a complex is not that the chains are near each other, but that the assembly is the unit that does the work.

## Formulation

### What natural element type does this protein complex instance belong to?

**A protein complex, read as a natural instance, belongs to `Ontic Element (→ Kind) Substantive (→ Kind) Natural System` — a bounded set of interacting components whose relations, not the components alone, carry the function.**

Readable secondarily as a **`Building Block`**: at the level of a larger structure — a membrane, a cytoskeleton, a pathway — the complex is one compositional unit, and that is how the note [Protein](/view.html?p=notes/nature/protein.md) meets it, under *Quaternary Structure*. Readable again as a **machine**, which is a technical and not a natural reading. Those readings are prose here, not second roots.

### What is this natural instance?

> A protein complex is delimited by three things at once: **composition** (which chains), **stoichiometry** (how many of each), and **geometry** (they are arranged in a particular way). Unlike a crystal, whose contacts are a consequence of packing, the contacts of a complex are the ones the organism preserves across evolution and disrupts by mutation. Unlike a sticky aggregate, a complex is *reproducibly* assembled and functionally necessary.
>
> The interactions holding it together are mostly non-covalent — hydrophobic burial of interfaces, hydrogen bonding, salt bridges — with occasional covalent reinforcement by disulfide bonds or by a metal ion that bridges two subunits. The interface is where most of the interesting genetics lives: a single substitution at a subunit contact can abolish cooperativity, or assemble a complex that no longer closes.
>
> Complexes are where proteins acquire properties their chains do not have. The haemoglobin tetramer binds oxygen cooperatively although no single globin chain can; the ribosome catalyses peptide-bond formation although neither its protein nor its RNA subunits do so alone; the proteasome degrades only after a regulatory particle recognises the substrate and opens the gate. That passage from component to collective function — the same passage the note [Protein](/view.html?p=notes/nature/protein.md) flags as *Quaternary Structure* — is the reason the complex needs its own decomposition rather than being listed as a property of its parts.
>
> The type boundary is real but contested. A **homomer** of identical chains is a complex; a **transient encounter** is not; a **membrane-bound assembly** is, but at that point the boundary between "protein complex" and "cell structure" starts to blur — which is why this note stops there and lets the cell and organelle notes take over.

### What is the recursive instance decomposition of this natural instance?

> Boundary: one assembly — its subunits, the interfaces between them, the mechanisms of assembly, the function the collective performs, and the states it passes through. The cell that hosts it, the pathway it belongs to, and the ligand it binds are associated, not parts.
>
> Stopping rule: a row is terminal when it names a subunit family, an interface type, a function, or a state whose own decomposition lives elsewhere.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: a subunit is **micro**; the assembled complex and its interfaces are **meso**; the pathway or organelle it acts inside is **macro**. Limitation checklist for the segment: **Many-Body coupling** (subunit interfaces interact), **Emergence** (the function is not in the parts), **Partial Observability** (transient and weak complexes vanish in purification), **Scale** (mega-dalton assemblies sit at the edge of what cryo-EM resolves).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex | Bound root instance: a reproducible assembly of polypeptide chains acting as one functional unit. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Part)` `Natural Object` | Grouping: the chains and the interfaces that constitute the assembly. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Part)` `Natural Object` `(→ Instance)` Subunit Set | The individual polypeptide chains, with their stoichiometry. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Part)` `Natural Object` `(→ Instance)` Subunit Set `(→ Part)` `Building Block` | Grouping: the compositional units of each chain. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Part)` `Natural Object` `(→ Instance)` Subunit Set `(→ Part)` `Building Block` `(→ Instance)` Folded Polypeptide Chain | One folded chain whose surface presents the residues that make contact. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Part)` `Natural Object` `(→ Instance)` Subunit Interface Set | The contact regions where subunits meet — where the assembly is decided. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Part)` `Natural Object` `(→ Instance)` Subunit Interface Set `(→ Part)` `Building Block` | Grouping: the unit that makes an interface. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Part)` `Natural Object` `(→ Instance)` Subunit Interface Set `(→ Part)` `Building Block` `(→ Instance)` Interface Patch | Buried surface whose shape complementarity selects the partner. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Component)` `Mechanism` | Grouping: the interactions that hold the assembly together. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Component)` `Mechanism` `(→ Instance)` Non-Covalent Association | Hydrophobic burial, hydrogen bonding and salt bridges across the interface. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Component)` `Mechanism` `(→ Instance)` Covalent Crosslinking | Disulfide bonds and bridging metal ions that fix a geometry the non-covalent contacts alone leave labile. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Component)` `Mechanism` `(→ Instance)` Allosteric Coupling | A change at one subunit site propagated through interfaces to change another subunit's affinity. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Occurrence)` `Natural Process` | Grouping: the transformations of the assembly. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Occurrence)` `Natural Process` `(→ Instance)` Assembly | The ordered path from separate chains to a closed assembly, controlled by chaperones and by proofreading. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Occurrence)` `Natural Process` `(→ Instance)` Allosteric Transition | The switching of the assembly between functional states. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Occurrence)` `Natural Process` `(→ Instance)` Disassembly | Cycles of dissociation and exchange that regulate and recycle complexes. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Attribute)` `Property` | Grouping: measurable attributes of the assembly. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Attribute)` `Property` `(→ Instance)` Stoichiometry | How many copies of each chain the assembly carries. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Attribute)` `Property` `(→ Instance)` Cooperativity | The gain in binding affinity that arises only from having several coupled sites. |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Natural System` `(→ Instance)` Protein Complex `(→ Attribute)` `Property` `(→ Instance)` Assembly Size | Total mass and subunit count, the first thing a purification or a tomogram reports. |

## References

- Perutz, M. F., et al. (1960). Structure of hæmoglobin: A three-dimensional Fourier synthesis at 5.5-Å resolution, obtained by X-ray analysis. *Nature, 185*, 416–422.
- Perutz, M. F. (1970). Stereochemistry of cooperative effects in haemoglobin: Haem–haem interaction and the problem of allostery. *Nature, 228*(5273), 726–734. https://doi.org/10.1038/228726a0
- Monod, J., Wyman, J., & Changeux, J.-P. (1965). On the nature of allosteric transitions: A plausible model. *Journal of Molecular Biology, 12*(1), 88–118. https://doi.org/10.1016/S0022-2836(65)80285-6
- Koshland, D. E., Némethy, G., & Filmer, D. (1966). Comparison of experimental binding data and theoretical models in proteins containing subunits. *Biochemistry, 5*, 365–385.
- Deisenhofer, J., Epp, O., Miki, K., Huber, R., & Michel, H. (1985). Structure of the protein subunits in the photosynthetic reaction centre of *Rhodopseudomonas viridis* at 3 Å resolution. *Nature, 318*, 618–624.
- Ban, N., Nissen, P., Hansen, J., Moore, P. B., & Steitz, T. A. (2000). The complete atomic structure of the large ribosomal subunit at 2.4 Å resolution. *Science, 289*(5481), 905–920. https://doi.org/10.1126/science.289.5481.905
- Gavin, A.-C., et al. (2002). Functional organization of the yeast proteome by systematic analysis of protein complexes. *Nature, 415*, 141–147.
- Gavin, A.-C., et al. (2006). Proteome survey reveals modularity of the yeast cell machinery. *Nature, 440*, 631–636.
- Hartl, F. U., & Hayer-Hartl, M. (2002). Molecular chaperones in the cytosol: From nascent chain to folded protein. *Science, 295*(5561), 1852–1858.

## Related

- [Protein](/view.html?p=notes/nature/protein.md)
- [Enzyme](/view.html?p=notes/nature/enzyme.md)
- [Biomolecule](/view.html?p=notes/nature/matter/biomolecule.md)

