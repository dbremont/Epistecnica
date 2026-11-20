---
tags: [note, nuclear, energy, technical-domain, technical-element-set]
---

# Nuclear Technical Domain

> The **Nuclear Technical Domain** is the civil technical field that turns nuclear materials and reactions into useful energy, isotopes and services: the fuel cycle, fission reactors, fusion technology, waste management and decommissioning, radiation protection, and the safety and safeguards systems that bound them.

> It is not the **nuclear industry**. The industry is the social and economic organisation — utilities, vendors, fuel-cycle firms, contractors, regulators and markets — that owns and operates the technical elements. It is also not **Energy Technology** in general: energy technology is the cross-carrier ensemble, while this domain is the nuclear-specific field inside it. Worked per [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md).

## Formulation

### What technical element type does this technical instance belong to?

**The Nuclear Technical Domain belongs to the `Technical Element Set` technical element type — a collection of technical elements scoped to one bounded field, which here is the civil use of nuclear reactions and materials.**

```text
Technical Element Set
└── Nuclear Technical Domain (bounded field: nuclear material and reaction → useful energy, isotope or service)
```

It is a set rather than a `Production Technical System` because it owns no single reactor, plant or fuel-cycle site: the member sets own those, and what this scope adds is the family and its boundary. The `Technical Element Set` grouping below the root is admitted by the No-repetition exception, appears exactly once, and scopes the member sets that would otherwise hang untyped off the root.

**Civil and peaceful scope.** The domain is deliberately the civil field. Weapons design, military nuclear programmes and strategic-weapons policy are outside it. The industry may serve defence as an adjacent customer, but that relation is not a member of this domain and is not decomposed here. Safeguards, export controls and non-proliferation are in scope because they are technical and institutional conditions under which civil nuclear material and technology move.

**What is in.** The fuel cycle from conversion onward, fission reactor technology, fusion technology, waste management and decommissioning, radiation protection, isotope production, and the safety and safeguards systems that bound all of them.

**What is out.** Uranium extraction as a geological resource activity, which belongs to resource development; nuclear physics as knowledge, which belongs to epistemica; the firms, prices and politics of the industry, which belong to the social and production spaces; and weapons design and military programmes, which are excluded on scope.

### What is this technical instance?

> A domain, not a single plant: the fuel-cycle set converts and enriches uranium and fabricates fuel; the reactor set turns the fuel's heat into steam, process heat or propulsion; the fusion set works on a different reaction altogether; the waste set holds and retires what the chain leaves behind; the radiation-protection set measures and controls exposure; and the safety-and-safeguards set states the conditions under which the others may operate.

**What the members share.** Every member is bounded by the same physical and institutional conditions: neutron economy and criticality, decay heat, containment, radiation exposure, long-lived waste, and the safeguards and safety case that make the technology legitimate. They differ in what they transform — uranium into fuel, fuel into heat, heat into electricity, plasma into fusion conditions, waste into a stable form — but they are one domain because no member can be designed or operated without the others.

**Lineage:** natural uranium and early research reactors → enriched-fuel power reactors → commercial light-water fleets → reprocessing and vitrification → passive-safety and generation-III+ designs → small modular reactors and advanced non-light-water concepts → fusion experiments and the first engineering test machines.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one civil nuclear domain, decomposed at middle depth — the root, its six member sets, and the spine that states what the members share (evolution, purpose, reality model, requirements, standards, practices and lifecycle). No member is re-decomposed here: each has its own note or future note, and repeating a member's contents inside its parent is duplication, not structure.
>
> Typing reads directly from the instance path. Every backticked type segment groups instances and terminates on none; every leaf resolves to a technical instance.
>
> Stopping rule: a row is terminal when it names a member set, an era, a purpose, a model, a requirement, a standard, a practice, or a lifecycle phase.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element Set` → Nuclear Technical Domain | The civil domain: fuel cycle, fission, fusion, waste, radiation protection, and the safety and safeguards that bound them. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Element Set` | Grouping: the six member sets of the civil nuclear domain. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Element Set` → Nuclear Fuel Cycle Set | Conversion, enrichment, fuel fabrication and reprocessing: the front and back ends of the fission fuel path. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Element Set` → Fission Reactor Set | Reactor cores, moderation, control, cooling, containment and the balance of plant that turns fission heat into steam, process heat or propulsion. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Element Set` → Fusion Technology Set | Plasma confinement, heating, blanket and tritium handling: the engineering of a controlled fusion reaction rather than a fission chain. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Element Set` → Waste And Decommissioning Set | Conditioning, storage, disposal, dismantling and site remediation for radioactive material and retired facilities. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Element Set` → Radiation Protection And Isotope Set | Dosimetry, shielding, contamination control, and the production and handling of radioisotopes for medicine, industry and research. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Element Set` → Safety And Safeguards Set | Deterministic and probabilistic safety cases, confinement, emergency planning, material accountancy and the safeguards that keep civil material civil. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Evolution` | Grouping: the technical evolution of the domain. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Evolution` → Research Reactor Era | Small experimental machines proving criticality and the first controlled chain reactions. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Evolution` → Power Reactor Era | Commercial electricity from fission, built on light-water and graphite-moderated designs. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Evolution` → Fuel-Cycle Era | Enrichment, fabrication and reprocessing scaled into an industrial chain with its own logistics and liabilities. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Evolution` → Safety And Safeguards Era | Defence-in-depth, probabilistic risk assessment, international safeguards and the safety case as a design input. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Evolution` → Advanced Reactor Era | Passive safety, small modular reactors, high-temperature and fast-spectrum concepts. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Evolution` → Fusion Engineering Era | From plasma-physics experiments to engineering test machines with blankets, tritium and heat extraction. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Purpose` | Grouping: the technical purpose of the domain. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Purpose` → Electricity Purpose | Firm low-carbon electricity from fission heat. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Purpose` → Heat And Isotope Purpose | Process heat, district heat, desalination, research neutrons and radioisotopes. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Purpose` → Safety Purpose | Keep the reaction, the material and the exposure inside stated bounds across normal operation and accident. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Domain Reality Model` | Grouping: the models the domain works in. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Domain Reality Model` → Neutron Economy Model | The balance of neutrons, fissile inventory, moderation and absorption that fixes what a core can sustain. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Domain Reality Model` → Decay-Heat Model | The residual heat after shutdown that fixes cooling, containment and emergency-power requirements. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Domain Reality Model` → Radiation Transport Model | The path of radiation through shielding, structures and tissue that fixes dose and protection. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Domain Reality Model` → Project Economics Model | Capital cost, construction time, cost of capital, fuel and waste liabilities that decide whether a plant is buildable. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Requirement` | Grouping: the requirements that bound the domain. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Requirement` → Criticality Control | Keep fissile material below the configuration that sustains an unintended chain reaction. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Requirement` → Containment Requirement | Hold radioactive material inside successive barriers across normal operation and accident. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Requirement` → Decay-Heat Removal | Remove residual heat after shutdown without relying on a single active system. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Requirement` → Safeguards Requirement | Account for nuclear material and make diversion detectable. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Requirement` → Waste Isolation | Hold long-lived waste out of the biosphere for the period its hazard requires. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Standard` | Grouping: the standards the domain is held to. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Standard` → IAEA Safety Standards | The international safety requirements and guides that national regulators translate into licensing conditions. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Standard` → Safeguards Agreement | The material-accountancy and inspection regime that keeps civil material under international verification. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Standard` → Reactor Code | The design, construction and inspection codes that fix how pressure boundaries and safety systems are built. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Practice` | Grouping: the organized practices that operate the domain. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Practice` → Reactor Operation Practice | Conduct of operation, surveillance, outage work and configuration control across the plant lifecycle. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Practice` → Fuel-Cycle Practice | Safeguarded handling, enrichment, fabrication and reprocessing as a controlled material chain. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Practice` → Decommissioning Practice | Characterization, dismantling, waste routing and site remediation after shutdown. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Lifecycle` | Grouping: the lifecycle of a nuclear project. |
| `Technical Element Set` → Nuclear Technical Domain → `Technical Lifecycle` → Project Lifecycle | Siting, licensing, construction, commissioning, operation, outage, decommissioning and closure. |

## See also

- [Nuclear Industry](/view.html?p=notes/technica/production/industry/nuclear/readme.md) — the civil industry that owns and operates these technical elements.
- [An Essay on Industry — Nuclear Technology Emergence](/view.html?p=notes/social/koinomia/action/informe/an-essay-on-industry-nuclear-technology-emergence.md) — country paths through transfer, indigenization and dependency.
- [Energy Technology](/view.html?p=notes/technica/general/energy-technology.md) — the cross-carrier energy domain in which nuclear power is one carrier path.
- [Technology Transfer Market](/view.html?p=notes/social/coordinator/market/technology-transfer-market.md) — the market and safeguards conditions under which nuclear technology moves.

## References

- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md)
- [International Atomic Energy Agency — Safety Standards](https://www.iaea.org/resources/safety-standards)
- [International Atomic Energy Agency — Safeguards](https://www.iaea.org/topics/safeguards-and-verification)
- [World Nuclear Association](https://www.world-nuclear.org/)
- [OECD Nuclear Energy Agency](https://www.oecd-nea.org/)
- [U.S. Department of Energy — Office of Nuclear Energy](https://www.energy.gov/ne/office-nuclear-energy)
- [IAEA Power Reactor Information System](https://pris.iaea.org/)
