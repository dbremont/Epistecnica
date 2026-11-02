---
tags: [actor, interaction-unit, agents, social-element]
---

# Actor

> An **Actor** is a bounded entity capable of interaction — agentive, cognitive/reflexive, relational, nested, state-carrying. It is the root of the social typology of who acts: individuals who decide, collectives that act as one, institutions that wield authority, and the functional forms — research, finance, trade, industry, education, party, firm — through which they engage the world.

The corpus partitions actor notes by constitution: `public/` carries the state and public actors and their elements, `private/` the societal actors, `action/` the Social Action branch, and the generic type hubs — [Organization](note.html?n=social/collective/actor/organization.md), [Firm](note.html?n=social/collective/actor/firm.md), [Research Actor](note.html?n=social/collective/actor/research.md), [Finance Actor](note.html?n=social/collective/actor/finance.md), [Human](note.html?n=social/collective/actor/human.md), [Family](note.html?n=social/collective/actor/family.md) — sit at the actor root. Mixed families (`research`, `finance`) grow one tree per reading and are split by public authority, with a hub entry at the root linking both halves.

## Formulation

### What social element type does this social instance belong to?

**Actor belongs to the `Interaction Unit` social element type (Agents category)** — the grammar's root slot for bounded entities capable of interaction. Its layer is **Ontic** where the actor exists extra-mentally (humans, organizations, polities) and **Synontic** where it exists through shared recognition (personas, virtual communities, jurisdictions carried as roles). Its facet is social-general: the dominant causal mechanism is coordinated agency as such, prior to any economic, political, or ideational scoping.

It is not an `Agency` (the structured capacity to form intentions, select actions, and integrate feedback — what an actor acts *with*), not a `Social Role` (the expectation-tag binding an actor to conduct — what an actor acts *as*), and not an `Institution` (the stabilized system of rules — what an actor acts *within*). An actor carries agencies, occupies roles, and inhabits institutions; the tree below types the carriers, never the carried.

### What is this social instance?

> An actor fixes *who hangs together and how*: the boundary of the entity, the agency through which it intends and selects, the membership or constituency it carries, and the relations binding it to other actors. The typology below classifies actors by constitution (individual, collective, institutional), by function (research, finance, trade, industry, education, party, firm), and by capacity (agency) — every leaf resolving to an already-decomposed entry.

### What is the recursive instance decomposition of this social instance?

> Boundary: one generic Actor — its recursive subtype classification plus its direct constituents, following the agentic spine `Interaction Unit -> Agency -> Social Action -> Activity`. The first row binds the grammar root; every row after roots at `Actor`. Subtype detail already worked in a linked entry is not duplicated here.
>
> Recursion rule: a `Type` grouping may nest under any subtype (`type → subtype → type → sub-subtype`), as deep as the classification requires — the same licensed recursion as `Social Compound` nesting in compounds.
>
> Stopping rule: a row is terminal when it names a type, a subtype, an agency, a role, a tie, or a practice, or when it links an already-decomposed entry.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Interaction Unit` `(→ Part)` Actor | Bounded entity capable of interaction: agentive, cognitive/reflexive, relational, nested, state-carrying. |
| Actor `(→ Kind)` Individual Actor | Actor deciding as one mind: a human, a persona. |
| Actor `(→ Kind)` Individual Actor `(→ Kind)` Human | Biological individual of the species Homo sapiens, bearing cognition, language, and culture; carries personhood as rights, duties, and accountability. |
| Actor `(→ Kind)` Individual Actor `(→ Kind)` Persona | Performed or attributed self carried through shared recognition across encounters. |
| Actor `(→ Kind)` Collective Actor | Actor acting as one through membership, rules, and joint agency. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization | Bounded compound unit with identity, membership, and rules acting as one. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Social Group | Interacting aggregate with unity but without membership or rules. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Family | Kinship unit binding members through descent, alliance, and obligation. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Household | Co-resident unit provisioning daily life from a common stock. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Virtual Community | Networked collective coordinating without co-location. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Network Collective | Actor constituted by its ties: alliances, supply webs, patronage. |
| Actor `(→ Kind)` Institutional Actor | Actor wielding stabilized authority over a domain. |
| Actor `(→ Kind)` Institutional Actor `(→ Kind)` Polity | Political community organized under a common authority. |
| Actor `(→ Kind)` Institutional Actor `(→ Kind)` Nation-State | Sovereign polity binding territory, population, and rule. |
| Actor `(→ Kind)` Institutional Actor `(→ Kind)` Jurisdiction | Bounded domain of legitimate authority. |
| Actor `(→ Kind)` Functional Actor | Actor defined by the function it performs in social reproduction. |
| Actor `(→ Kind)` Functional Actor `(→ Kind)` Research Actor | Actor producing or funding inquiry: institutes, laboratories, agencies. |
| Actor `(→ Kind)` Functional Actor `(→ Kind)` Finance Actor | Actor allocating capital and settling claims: banks, funds, exchanges. |
| Actor `(→ Kind)` Functional Actor `(→ Kind)` Trade Actor | Actor promoting and governing exchange across borders. |
| Actor `(→ Kind)` Functional Actor `(→ Kind)` Industry Actor | Actor organizing production in a sector or territory. |
| Actor `(→ Kind)` Functional Actor `(→ Kind)` Education Actor | Warranted body transmitting certified knowledge across generations. |
| Actor `(→ Kind)` Functional Actor `(→ Kind)` Party | Political organization fielding candidates and programs in collective choice. |
| Actor `(→ Kind)` Functional Actor `(→ Kind)` Firm | Bounded collective converting capability into exchangeable value. |
| Actor `(→ Part)` Agency | Grouping: structured capacities forming intention and selecting action. |
| Actor `(→ Part)` Agency `(→ Kind)` Deliberative Agency | Structured capacity weighing alternatives and committing to a course. |
| Actor `(→ Part)` Agency `(→ Kind)` Executive Agency | Structured capacity carrying decisions into execution. |
| Actor `(→ Part)` Social Relation / Network | Grouping: structured ties binding actors to one another. |
| Actor `(→ Part)` Social Relation / Network `(→ Part)` Membership Tie | Structured tie binding a member to the collective it belongs to. |
| Actor `(→ Part)` Social Relation / Network `(→ Part)` Alliance Tie | Structured tie binding actors in joint pursuit. |
| Actor `(→ Part)` Social Role | Grouping: expectation-tags actors occupy. |
| Actor `(→ Part)` Social Role `(→ Component)` Role Occupancy | Binding of an actor, a context, and an interpretation to behavior. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization | Organization wielding delegated public authority under law. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Ministry | Government organization responsible for a major policy domain and its associated administrative functions. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Department | Administrative organization or subdivision responsible for a defined governmental function or domain. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Agency | Organization established or designated to perform specified governmental or administrative functions. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Council | Collegial body established to deliberate, coordinate, advise, govern, or make decisions within a defined domain. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Commission | Body established to investigate, regulate, administer, coordinate, or perform a specified public function. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Board | Collegial governing, supervisory, advisory, or decision-making body; see [Board](note.html?n=social/collective/actor/board.md). |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Authority | Public body entrusted with specific powers, often regulatory, supervisory, or administrative. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Secretariat | Organization or administrative unit providing coordination, executive support, or administration for a government, council, or other body. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Office | Organizational unit or institution assigned a defined governmental responsibility. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Directorate | Administrative unit responsible for a particular function or operational domain. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Administration | Organization or organizational complex responsible for administering a public domain, program, or jurisdiction. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Bureau | Administrative organization or subdivision responsible for a specialized function. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Institute | Organization established to conduct specialized activities such as research, technical work, training, or public service. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Public Corporation | Public-sector corporate entity established to conduct designated commercial, financial, infrastructural, or other activities. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Public Service | Organized administrative structure responsible for delivering a defined public service. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Tribunal | Public adjudicative body responsible for resolving disputes or determining matters within its jurisdiction. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Court | Judicial body exercising legally established adjudicative authority. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Prosecutor's Office | Public organization or office responsible for prosecution and related legal functions. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Inspectorate | Organization or unit responsible for inspection, compliance verification, or oversight. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Ombudsman's Office | Institution or office responsible for investigating complaints and protecting individuals against specified forms of maladministration or abuse. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Task Force | Temporarily or specially constituted body assigned a defined objective. |
| Actor `(→ Kind)` Collective Actor `(→ Kind)` Organization `(→ Kind)` Public Organization `(→ Kind)` Committee | Collegial body established to deliberate, advise, coordinate, supervise, or decide on specified matters. |

## References

- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [Organization](note.html?n=social/collective/actor/organization.md) (collective actor hub: the full subtype tree)
- [Firm](note.html?n=social/collective/actor/firm.md) (economic subtype of Organization)
- [Social Group](note.html?n=social/collective/actor/private/group/group.md) (interacting aggregate — not an organization)
- [Human](note.html?n=social/collective/actor/human.md) (biological individual; carries personhood)
- [Family](note.html?n=social/collective/actor/family.md) (kinship unit)
- [Public Organization](note.html?n=social/collective/actor/public/public-organization.md) (government subtype; carries the agency-space QA)
- [Education Actor](note.html?n=social/collective/actor/education-actor.md) (warranted teaching body)
- [Laboratory](note.html?n=social/collective/actor/laboratory.md) (research host unit)
- [Public Research Institutes](note.html?n=social/collective/actor/public/catalog/pri.md) (public-research role)
- [Research Actor](note.html?n=social/collective/actor/research.md) (research-functional subtype hub: the research actor family)
- [Finance Actor](note.html?n=social/collective/actor/finance.md) (finance-functional subtype hub: the finance actor family)
- [Political Party](note.html?n=social/collective/actor/political-party.md) (political subtype)
- [Sociedad de Amantes del País](note.html?n=social/collective/actor/sociedad-de-amantes-del-pais.md) (learned-society type)
- [China](note.html?n=social/collective/actor/public/polity/chn/prc/china.md) (nation-state instance)
- Graph nodes of the same names: `person`, `firm`, `organization`, `public-organization`, `sreni` (Social Space, dataset `social`)
