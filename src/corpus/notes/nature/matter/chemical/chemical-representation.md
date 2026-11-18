---
tags: [note, nature, substance-matter, chemistry, representation, technique]
---

# Chemical Representation

> **Chemical representation** is the use of symbols, diagrams, and formulas to convey the structure, composition, and properties of chemical substances.
>

## Representation Frameworks

> …
>

| **Representation Type** | **Description** | **Example** |
| --- | --- | --- |
| **Chemical Formula** | Shows the types and ratios of atoms in a compound using element symbols and subscripts. | $\text{H}_2\text{O}$,  $\text{C}6\text{H}{12}\text{O}_6$ |
| **Structural Formula** | Illustrates the arrangement of atoms and bonds in a molecule, often using lines for covalent bonds. | $\text{H} - \text{O} - \text{H}$ |
| **Lewis Structure** | Uses dots around atomic symbols to represent valence electrons, highlighting bonding and lone pairs. | $\text{H} : \text{O} : \text{H}$ |
| **Molecular Model Diagram** | 3D models that show spatial relationships between atoms, like ball-and-stick or space-filling models. | Ball-and-stick model of methane |
| **Skeletal Formula** | Simplifies organic molecules by using lines for bonds and omitting hydrogen atoms attached to carbons; often used in organic chemistry. | Skeletal formula of benzene |

## Structural Representation

> A formula states the composition; a **structural representation** states the *arrangement* — which atom is bonded to which, and how. The family runs from a drawing a chemist reads at a glance to a string a database indexes, and each member trades something away.

### Lewis structures

> A Lewis structure draws the **valence electrons**: dots for lone pairs, a line or a pair of dots for a shared pair, brackets and a charge for an ion. It is the representation of *bonding bookkeeping* — which atoms have an octet, where the formal charges sit, which resonance forms are equivalent.

| It captures | It loses |
| --- | --- |
| Connectivity and bond order | Three-dimensional geometry |
| Lone pairs and formal charge | Delocalisation (resonance must be drawn as several forms) |
| Octet and its exceptions (odd-electron species, hypervalent molecules) | Any distinction between resonance structures, which are one object |

> Resonance is the classic lesson: the molecule is a resonance hybrid, the drawings are not. A representation that must be read as a *set* of structures is already telling the reader that a single drawing is insufficient.

### Structural formulas

> A structural formula makes the atoms and bonds explicit — full (every atom and bond drawn), condensed ($\mathrm{CH_3CH_2OH}$), or skeletal (a line drawing where vertices are carbons and hydrogens on carbon are omitted). The conventions — the zig-zag, the suppressed hydrogens, the stereochemical wedges and dashes — are what make a drawing unambiguous without writing every atom.

> The boundary against a plain formula is the point of the whole family: $\mathrm{C_2H_6O}$ is either ethanol or dimethyl ether, and only the structural form tells you which. Composition is a ratio; structure is a graph.

### Discrete symbolic representation

> The **discrete symbolic** forms turn the structure into a finite string or record that a machine can store, compare and canonicalise:

| Notation | What it is | Why it exists |
| --- | --- | --- |
| **SMILES** | A linear ASCII string: atoms, bonds, branches in parentheses, ring closures by digits | Compact, human-writable, ubiquitous in cheminformatics |
| **InChI** | An IUPAC normalised identifier with layers for formula, connectivity, hydrogen, charge and stereochemistry | A canonical key for databases and search — the same molecule gives the same string |
| **WLN** | The older Wiswesser line notation | Historical: the first widely used line notation |
| **Connection table (CTfile, MOL/SDF)** | An explicit atom list and bond list with attributes | The full graph, readable by drawing software and modelling tools |

> The connection table is the underlying object; SMILES and InChI are two ways of writing it down. The reason InChI exists as a separate notation is **canonicalisation**: a graph has many valid SMILES strings, and a database needs one. A representation that is not canonical cannot be a key.

### Three-dimensional models

> Ball-and-stick and space-filling models carry what no line drawing can: the actual spatial arrangement, the van der Waals surface, the steric clash. They are **perceptual** representations rather than symbolic ones — nothing in them is a token that a parser reads — which is why they are used for teaching and for visual inspection, and never as the primary record of a structure.

## Representing a Molecular Structure

> The problem the family solves is the same in every member: a molecule is a **graph** — atoms as vertices, bonds as edges with order and stereochemistry — and every representation is a map from that graph to something a reader or a machine can handle.

| Question | Lewis | Structural formula | SMILES | InChI | 3D model |
| --- | --- | --- | --- | --- | --- |
| Encodes connectivity | yes | yes | yes | yes | implicitly |
| Encodes bond order | yes | yes | yes | in layers | implicitly |
| Encodes stereochemistry | rarely | wedges | `@`/`/` | stereo layer | yes |
| Encodes geometry | no | no | no | no | yes |
| Machine-readable | no | no | yes | yes | yes (coordinates) |
| Canonical | — | — | no | **yes** | no |

> Two consequences follow. **Human readability and machine precision pull apart**: the drawing is the best representation for a chemist and the worst for a database; the InChI is the reverse. And **canonicalisation is the hard part**: deciding that two representations denote the same substance is graph isomorphism, and the canonical form is the answer that makes search and deduplication possible. The corpus's chemical databases are built on the discrete symbolic forms for exactly this reason.

> The limit worth naming: none of these representations carries the *electronic* structure fully — the Lewis structure is a bookkeeping device, the connection table a graph, the 3D model a set of coordinates. The quantum-mechanical description is a different object, and the chemical representation is the compression that makes the molecule tractable.

## References

- [Structural formula](https://en.wikipedia.org/wiki/Structural_formula)
- [SMILES](https://en.wikipedia.org/wiki/SMILES) — the Daylight line notation
- [InChI](https://www.iupac.org/standing-committees/committee-on-chemis/current-projects/inchi/) — the IUPAC canonical identifier
- [Chemical table file (CTfile)](https://en.wikipedia.org/wiki/Chemical_table_file) — the connection-table formats
- https://en.wikipedia.org/wiki/Chemical_database
- https://chem.libretexts.org/Courses/College_of_the_Canyons/Chem_201%3A_General_Chemistry_I_OER/03%3A_Molecules_and_Compounds/3.02%3A_Representation_of_Chemical_Compounds
- Warr, W. A. (2011). Representation of chemical structures. *Wiley Interdisciplinary Reviews: Computational Molecular Science*, *1*(4), 557-579.
- Hoffmann, R., & Laszlo, P. (1991). Representation in chemistry. Angewandte Chemie International Edition in English, 30(1), 1-16.

## Provenance

- Notion export: `Modelo/Nature/Conceptual Model Natural System/Chemical Representation 13dc0f5171ec808cafccd8f7fc6cc3dd.md`
