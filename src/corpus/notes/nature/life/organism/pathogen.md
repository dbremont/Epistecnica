---
tags: [note, nature, biology, pathogen, disease, organism]
qa:
 - Is a pathogen a kind of organism or a role an organism plays?
 - A virus is not autopoietic and a prion is not alive. What do they share with a fungus that makes the same word fit?
 - Does virulence belong to the pathogen or to the interaction?
---

# Pathogen

> A **pathogen** is an agent — an organism, a virus or a prion — that causes disease in a host: it enters or contacts the host, reproduces or accumulates at the host's expense, and produces dysfunction that the host cannot contain. The word names a **role**, not a taxonomic kind: the same fungus is a pathogen on one host and a saprophyte on another, and a bacterium that is harmless in the soil can be lethal in a wound.

> That relational character is the whole reason the concept is hard. A pathogen is defined by what it does to a host, not by what it is; and what it does depends on the host's state, the dose, the route and the environment. The category is therefore a node in an interaction, and the interaction is the object.

## Formulation

### What natural element type does this pathogen instance belong to?

**Pathogen belongs to `Ontic Element (→ Kind) Entity` — a unit treated as a thing that can be counted, referred to and related — readable as an `Agent`, the entity that acts on the host.**

The role reading is the precise one: a pathogen is an organism (or virus, or prion) **considered under its capacity to cause disease**. It is not a `Substance` (the pathogen is the entity, not the stuff it is made of), not a `Natural System` (it can be a single cell), and not a taxonomic kind — the classes below are the taxa that most often play the role, not the role itself.

The boundary against a **parasite** is convention and degree: parasitism is the general way of life, pathogenicity is the subset that damages the host enough to produce disease. The boundary against a **saprophyte** is the host's state: the same organism decomposes dead tissue and attacks living tissue when the plant is wounded or stressed.

### What is this natural instance?

> Viruses, viroids and prions at the non-cellular edge; bacteria, fungi and oomycetes, protozoa, and helminths at the cellular one — plus the phytoplasmas and nematodes that specialise on plants. What they share is not a body plan but an operation: they multiply in or on a host, obtain resources from it, and damage it — by consuming it, by killing its cells, by producing toxins, by blocking its transport, or by provoking a response that harms the host itself.

### What is the recursive instance decomposition of this pathogen instance?

> Boundary: the role and the entities that play it — the classes, the attributes that decide whether an encounter becomes a disease, and the mechanisms by which damage is done, with the host and environment as the bound. The host's own defence belongs to the plant or animal note; the disease as a process is read as the causal chain in the Plant Health section of the host note.
>
> Stopping rule: a row is terminal when it names a class of agent, a measured attribute, a named mechanism or a named bound.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique. Level of organization: the virion, spore or cell is **micro**; the infection and the host population are **meso**; the epidemic and the reservoir landscape are **macro**. Limitation checklist for the segment: **Complexity** (host, agent and environment interacting), **Nonlinearity** (a threshold dose and an immune response), **Uncertainty** (strain variation and imperfect diagnosis), **Partial Observability** (latent and asymptomatic carriage), **Scale** (the same agent is a cell, an infection and an epidemic), **Measurement Disturbance** (sampling and isolation select the organisms they detect).

| Instance Tree Path | Description |
| --- | --- |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen | The disease-causing role, read across the entities that play it. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class | Grouping: the kinds of entity that play the role. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class `(→ Instance)` Virus | Obligate intracellular replicator; not autopoietic, filed at the organism borderline by convention. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class `(→ Instance)` Viroid | A naked circular RNA that replicates in the host — smaller than a virus, and a plant pathogen. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class `(→ Instance)` Prion | A misfolded protein that propagates its conformation — the non-living edge of the class. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class `(→ Instance)` Bacterium | Prokaryotic cell: the wound, food and respiratory pathogen of the class. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class `(→ Instance)` Fungus and Oomycete | Filamentous or single-celled eukaryotes: the largest share of plant disease. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class `(→ Instance)` Protozoan | Single-celled eukaryote, including the vector-borne parasites of humans and animals. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class `(→ Instance)` Helminth | Parasitic worm: a multicellular animal pathogen, and a crop pest at the nematode end. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Kind)` Pathogen Class `(→ Instance)` Phytoplasma | Wall-less bacterium restricted to phloem and insect vectors — a plant pathogen class of its own. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Attribute)` | Grouping: the properties that decide whether an encounter becomes disease. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Attribute)` `(→ Instance)` Host Range | The set of hosts the agent can infect — narrow specialists and broad generalists. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Attribute)` `(→ Instance)` Virulence | The degree of damage the agent produces in a given host — a property of the interaction, not of the agent alone. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Attribute)` `(→ Instance)` Transmission Route | Contact, airborne, water, food, vector, seed or wound — the route fixes the control. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Attribute)` `(→ Instance)` Infectious Dose | The number of agents needed to establish infection — the reason exposure is a variable. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Attribute)` `(→ Instance)` Environmental Survival | How long the agent persists outside the host — the reservoir's memory. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Component)` `Mechanism` | Grouping: how the agent produces damage. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Component)` `Mechanism` `(→ Instance)` Adhesion and Colonisation | Attachment to the host surface and establishment in its tissue. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Component)` `Mechanism` `(→ Instance)` Toxin Production | Molecules that damage host cells, block transport or disrupt membranes. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Component)` `Mechanism` `(→ Instance)` Immune Evasion | Concealment, suppression or subversion of the host's defence. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Component)` `Mechanism` `(→ Instance)` Nutrient Extraction | Withdrawal of water, sugars or minerals through a feeding structure. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Bound)` `Environment` | Grouping: the conditions that decide whether the encounter becomes disease. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Bound)` `Environment` `(→ Instance)` Susceptible Host | The host state — genetics, age, wounds, stress — that admits the agent. |
| `Ontic Element` `(→ Kind)` `Entity` `(→ Instance)` Pathogen `(→ Bound)` `Environment` `(→ Instance)` Favourable Conditions | Temperature, moisture and vectors that let the agent reach and establish. |

## The Classes

| Class | Cell | Replication | Typical hosts | Example |
| --- | --- | --- | --- | --- |
| **Virus** | None | Host machinery | Plants, animals, bacteria | Tobacco mosaic virus; influenza |
| **Viroid** | None | Host machinery | Plants | Potato spindle tuber viroid |
| **Prion** | None | Conformational | Animals | Bovine spongiform encephalopathy |
| **Bacterium** | Prokaryotic | Binary fission | All | *Salmonella*; *Xylella* |
| **Fungus / Oomycete** | Eukaryotic | Spores and hyphae | Plants, animals | *Magnaporthe*; *Phytophthora* |
| **Protozoan** | Eukaryotic | Division | Animals, humans | *Plasmodium* |
| **Helminth** | Eukaryotic, multicellular | Eggs and larvae | Animals, plants (nematodes) | *Ascaris*; root-knot nematode |
| **Phytoplasma** | None (wall-less) | In phloem and vector | Plants | Aster yellows phytoplasma |

> The classes differ in everything except the role. That is why "pathogen" is a useful word and a poor taxonomy: it groups a prion with a fungus because both make a host ill, and it separates two fungi because one of them lives on dead wood.

## Transmission

| Route | How it works | Control lever |
| --- | --- | --- |
| **Contact** | Direct surface-to-surface transfer | Hygiene, spacing, pruning |
| **Airborne** | Spores or droplets carried by air | Ventilation, filters, resistant varieties |
| **Water and soil** | Splash, irrigation, soilborne inoculum | Drainage, rotation, solarisation, clean stock |
| **Food and water (animal)** | Ingestion of contaminated material | Hygiene, cooking, source control |
| **Vector** | An insect, mite or nematode carries the agent | Vector control, netting, resistant varieties |
| **Seed and propagule** | The agent travels inside or on the seed | Certified seed, testing, treatment |
| **Wound** | The agent enters through injury | Handling, pruning, insect control |

## Virulence and the Disease Triangle

> Disease is not a property of the pathogen. It is the outcome of three populations meeting: a **susceptible host**, a **virulent agent** and a **favourable environment**. Remove any one and there is no disease — which is why the same pathogen is devastating in one season and absent in the next, and why resistance breeding, sanitation and climate each change the outcome without changing the agent.

> **Virulence** is the degree of damage in a particular host, and it is under selection: an agent that reproduces fast may kill its host before it transmits, and an agent that is too mild may be outcompeted. The intermediate strategy — moderate damage, efficient transmission — is what evolution tends to find, and the exceptions are the interesting cases.

## One Health

> The same agents cross the boundaries between crops, livestock, wildlife and people. *Salmonella* in the food chain, influenza in poultry and pigs, antimicrobial resistance in the environment, and the vector-borne diseases that follow a changing climate are one problem in four hosts. That is why the concept is read at the population level as much as at the cell: the pathogen is a node in a network of hosts, vectors and reservoirs, and control at one node is only as good as the weakest link in the chain.

## References

- [Pathogen](https://en.wikipedia.org/wiki/Pathogen)
- [Virus](https://en.wikipedia.org/wiki/Virus) · [Viroid](https://en.wikipedia.org/wiki/Viroid) · [Prion](https://en.wikipedia.org/wiki/Prion)
- [Bacteria](https://en.wikipedia.org/wiki/Bacteria) · [Fungus](https://en.wikipedia.org/wiki/Fungus) · [Oomycete](https://en.wikipedia.org/wiki/Oomycete) · [Protozoa](https://en.wikipedia.org/wiki/Protozoa) · [Helminth](https://en.wikipedia.org/wiki/Helminth)
- [Phytoplasma](https://en.wikipedia.org/wiki/Phytoplasma) · [Nematode](https://en.wikipedia.org/wiki/Nematode)
- [Disease triangle](https://en.wikipedia.org/wiki/Disease_triangle) · [Virulence](https://en.wikipedia.org/wiki/Virulence)
- [Plant](/view.html?p=notes/nature/life/organism/plant/plant.md) — the host, and the Plant Health section that carries the causal chain the agent enters
- [Virulence Factor](/view.html?p=notes/nature/life/organism/bacteria/virulence-factor.md) — the molecules of the mechanism
- [Pathogenesis](/view.html?p=notes/nature/life/organism/bacteria/pathogenesis.md) — the process from exposure to symptom
- [Plant Health Technical Set](/view.html?p=notes/technica/general/plant-health-technical-set.md) — the apparatus that diagnoses and controls
- [Agricultural Science](/view.html?p=notes/miscellanea/discipline/agricultural-science.md) — the discipline that studies the populations
- [How to decompose any natural instance?](/view.html?p=notes/philosophia-naturalis-et-operis.md) — the tabular and recursive views, the level gate and the Limitation checklist
- [Philosophia Naturalis et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-naturalis-et-operis.md) — the schema and the table contract
