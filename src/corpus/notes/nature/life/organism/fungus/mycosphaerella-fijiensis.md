---
tags: [note, nature, organism, fungus, plant-pathology, agriculture]
qa:
 - The teleomorph name (*Mycosphaerella fijiensis*) still leads the literature, but the one-fungus-one-name rule makes the anamorph (*Pseudocercospora fijiensis*) current. Which name should the corpus use for the organism, and which for the disease?
 - Black Sigatoka displaced yellow Sigatoka in many places. Was that competition between pathogens, a consequence of the susceptible cultivars planted, or both?
 - Is the fungicide treadmill a property of the pathogen or of the monoculture it is sprayed on?
---

# Mycosphaerella fijiensis

> ***Mycosphaerella fijiensis*** (anamorph ***Pseudocercospora fijiensis***) is an ascomycete fungus that causes **black leaf streak**, the disease known in the banana trade as **black Sigatoka** — the most destructive foliar disease of bananas and plantains. It infects the leaves of *Musa* species and cultivars, producing streaks that expand into necrotic lesions, destroying the photosynthetic area and reducing bunch weight and fruit quality.

> The disease is a case study in the cost of genetic uniformity. The commercial Cavendish cultivars are triploid, parthenocarpic and clonally propagated, so a pathogen that defeats one plant's defences faces no genetic variation across the plantation. The response has been chemical — protectant and systemic fungicide programmes running to dozens of applications a year — and the pathogen has answered with resistance, which is why black Sigatoka is also the strongest agronomic argument for breeding resistant bananas.

## Formulation

### What natural element type does this natural instance belong to?

`Organism` at **micro** level of organization (Existential) — a self-maintaining, reproducing filamentous fungus, read here as a pathogen of *Musa*. It is not the disease: the disease is the interaction, and it belongs to the host's pathology note and to the [Pathogen](/view.html?p=notes/nature/life/organism/pathogen.md) reading of the role. It is not a `Substance` and not a `Phenomenon`: the fungus is a body, the epidemic is what the body does across a population.

The taxonomic position is: phylum Ascomycota, class Dothideomycetes, order Capnodiales, family Mycosphaerellaceae. The **teleomorph** (sexual stage) was described as *Mycosphaerella fijiensis*; the **anamorph** (asexual stage) is *Pseudocercospora fijiensis*. Under the one-fungus-one-name rule the anamorph name is the current name of the species, while the teleomorph name remains the one the phytopathological literature uses for the disease cycle. The corpus keeps both, and says which is which rather than silently choosing.

### What is this natural instance?

> The fungus that drew the brown streaks on the underside of a banana leaf in Fiji in the 1960s, reached Honduras in the 1970s, and is now present in most banana-producing regions of the tropics — a pathogen that spreads as wind-borne ascospores, lands on a leaf, and kills the leaf's capacity to feed the bunch.

The life cycle has two spore types that do different work. **Ascospores** are produced sexually in pseudothecia in the necrotic lesions and released into the air; they are the long-distance inoculum and the reason the disease moves across valleys and between plantations. **Conidia** are produced asexually in sporodochia and spread by rain splash; they are the within-plant and within-plantation inoculum. The latent period — infection to visible symptom — runs on the order of two to three weeks, and the lesion expands from a narrow streak to a dark, coalescing blotch that kills the leaf.

The host range is narrow: *Musa* species and cultivars, with differences in susceptibility — plantains and some East African highland bananas are highly susceptible, and the Cavendish clones that dominate export trade are susceptible enough to require the fungicide programme. The disease was first recognised in Fiji in the 1960s, spread through the Pacific and Southeast Asia, reached the Americas in the 1970s, and is now reported across the humid tropics. It displaced **yellow Sigatoka** (*Mycosphaerella musicola*) in many of the areas it entered.

### What is the recursive instance decomposition of this natural instance?

> Boundary: the fungus as an organism — its taxonomic position, its infective and dispersal structures, the host relation, and the epidemiological quantities that decide an outbreak. The disease as a process belongs to the banana production note; the chemical control programme belongs to the technical practice.
>
> Stopping rule: a row is terminal when it names a structure, a measured quantity, or a named relation.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the hypha and the spore are **micro**; the lesion and the plantation are **meso**; the regional epidemic is **macro**.

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Substantive` `(→ Kind)` `Organism` `(→ Kind)` Fungus `(→ Kind)` Mycosphaerella fijiensis | The ascomycete pathogen of *Musa*; teleomorph *M. fijiensis*, anamorph *P. fijiensis*. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Part)` `Building Block` `(→ Kind)` Hypha | The filamentous growing body: septate, branched, growing through the leaf tissue. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Part)` `Building Block` `(→ Kind)` Ascospore | The sexual spore, formed in a pseudothecium in the lesion, released to the air; the long-distance inoculum. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Part)` `Building Block` `(→ Kind)` Conidium | The asexual spore, borne in a sporodochium, spread by rain splash; the local inoculum. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Has)` `Adaptation` `(→ Instance)` Host Specialisation | The narrow host range on *Musa*: the fungus infects banana and plantain, not the surrounding flora. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Has)` `Adaptation` `(→ Instance)` Fungicide Resistance | The selected capacity to survive the DMI and QoI chemistry used against it — an adaptation produced by the control programme. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Participation)` `Living Process` `(→ Instance)` Leaf Infection | Germination on the leaf surface, penetration, and colonisation of the mesophyll — the process that produces a lesion. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Attribute)` `Property` `(→ Instance)` Latent Period | The interval from infection to visible symptom, on the order of two to three weeks — the quantity that sets the epidemic's tempo. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Attribute)` `Property` `(→ Instance)` Spore Load | The number of ascospores and conidia produced per lesion per unit time — the quantity that sets the epidemic's force. |
| `Organism` `(→ Kind)` Mycosphaerella fijiensis `(→ Bound)` `Constraint` `(→ Kind)` `Natural Constraint` `(→ Instance)` Leaf Wetness | The free water on the leaf surface without which spores do not germinate; the environmental bound on infection. |

**Limitations.** *Scale* — the organism is a hypha, the disease is a lesion, the problem is a regional epidemic; the note must say which level it is speaking at. *Partial Observability* — latent infections are invisible until symptoms appear, so the epidemic is always ahead of the record. *Nonlinearity* — the fungicide programme selects resistance, which changes the pathogen while the control is being applied. *Uncertainty* — the spread record is uneven across regions, and the dates of first detection are detection dates, not arrival dates.

## References

- Stover, R. H. (1980). Sigatoka leaf spots of bananas and plantains. *Plant Disease*, 64(8), 750–756. — the comparative account of yellow and black Sigatoka.
- Churchill, A. C. L. (2011). *Mycosphaerella fijiensis*, the black leaf streak pathogen of banana: Progress towards understanding pathogen biology and detection, disease development, and the challenges of control. *Molecular Plant Pathology*, 12(4), 307–328. — the modern reference review.
- Marin, D. H., Romero, R. A., Guzmán, M., & Sutton, T. B. (2003). Black Sigatoka: An increasing threat to banana cultivation. *Plant Disease*, 87(3), 208–222. — the disease and its management in the Americas.
- Ploetz, R. C. (2000). Black Sigatoka. *Pesticide Outlook*, 11(1), 19–23. — the fungicide dependence and the resistance problem, stated plainly.
- [Mycosphaerella fijiensis — Wikipedia](https://en.wikipedia.org/wiki/Mycosphaerella_fijiensis)
- [Black Sigatoka — Wikipedia](https://en.wikipedia.org/wiki/Black_Sigatoka)
- [Banana](/view.html?p=notes/technica/production/industry/agriculture/banana/readme.md) — the production system the disease constrains
- [Fungus](/view.html?p=notes/nature/life/organism/fungus/fungus.md) · [Spore](/view.html?p=notes/nature/life/organism/spore.md) · [Pathogen](/view.html?p=notes/nature/life/organism/pathogen.md)
