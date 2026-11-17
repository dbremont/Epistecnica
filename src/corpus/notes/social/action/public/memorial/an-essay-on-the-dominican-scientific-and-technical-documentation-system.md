---
tags: [note, social, memorial, science-policy, documentation, open-science]
qa:
 - What problem does this system solve — and is it a problem of research capacity or of the memory of research?
 - What can the scope of such a system be, and what must it refuse to be?
 - What incentive structure should guide the system, given that voluntary deposit has failed wherever it was tried?
---

# An Essay on the Dominican Scientific and Technical Documentation System

> The Dominican Republic has a **science system** and does not have a **documentation system**. Ley 139-01 of 13 August 2001 created the *Sistema Nacional de Educación Superior, Ciencia y Tecnología* — with the ministry that is now MESCYT, the competitive fund FONDOCYT (Art. 94), and INDOTEC, IDIA and the Academia de Ciencias de la República Dominicana integrated into it (Art. 26) — and that system produces research, theses, technical reports and statistics. What it does not have is the layer that records, preserves, indexes and makes findable what it produces.

> The gap is not research capacity. It is the **memory of research**, and it is invisible precisely because nothing is missing from the laboratory: the experiment runs, the thesis is defended, the report is delivered, and then the object exists in one drawer on one campus. A country that cannot find its own work cannot build on it, cannot evaluate it, and cannot be found by anyone else.

## 1. What problem does this system solve?

Five functions make up a documentation system, and the country holds only the heritage halves of them:

| Function | What it does | Dominican holder |
| --- | --- | --- |
| Deposit and registration | The object is lodged, dated and given a permanent address | none for scientific output |
| Cataloguing and authority control | Names, subjects and versions are made consistent | Biblioteca Nacional, for published books |
| Preservation | The object survives its medium and its institution | Archivo General de la Nación, for archives |
| Access and interoperability | The record is findable, harvestable and citable | scattered, per university |
| Measurement | The national output can be counted and compared | none |

Scientific and technical documentation — theses, journal articles, technical reports, datasets, conference papers — belongs to none of those institutions. It is the output of a system created in 2001 that was given money, institutions and a mandate to produce knowledge, and was never given the machinery to keep it.

The problem therefore has a precise shape, and it is not "we publish too little". It is:

1. **No aggregator.** Institutional repositories exist at several universities; nothing harvests them, and no national portal exists that a foreign researcher could search.
2. **Theses are campus-bound.** A thesis defended at one university is invisible at the next one, and invisible to the ministry that funded the programme.
3. **No persistent identifiers by policy.** Without a DOI registration route and an ORCID expectation, Dominican work cannot be reliably cited or attributed, and therefore cannot be counted.
4. **No preservation policy.** A repository is not an archive: without a mandate, format migration and replication, today's portal is tomorrow's broken links.
5. **Grey literature is collected nowhere.** Project final reports, standards and datasets fall outside both legal deposit and the universities' scope.
6. **International consequence.** Regional aggregators work through national nodes — LAReferencia by node, SciELO by national collection — so without a national layer Dominican output reaches them only through individual repositories or not at all, and is invisible to precisely the scholars who would cite it.

Research that cannot be found is paid for twice: once to produce it, and again by everyone who repeats it.

## 2. What can the scope of such a system be?

The scope has to be drawn as tightly as the function list, because systems of this kind die of scope creep from three directions: they become ranking agencies, second repositories, or digitisation programmes for heritage. The boundary that decides everything is a single rule — **harvest, do not build**.

| In scope | Out of scope |
| --- | --- |
| Theses and dissertations | Custody of the universities' repositories |
| National journals, current and back issues | Heritage books and manuscripts (Biblioteca Nacional) |
| Final reports of publicly funded projects | Administrative archives (Archivo General de la Nación) |
| Technical reports and standards (INDOTEC, IDIA) | Evaluation of scientific *quality* — the system records, it does not rank |
| Research data, at a later stage | Publication services and peer review |
| Metadata aggregation and one public search | Owning the copyright of what it indexes |

The last exclusion is the one that must be stated politically, not technically. A documentation system that begins to rank what it records acquires the incentive to stop recording what would rank badly.

## 3. What incentive structure should guide the system?

This is the section the proposal turns on, because the technical design is easy and the incentives are not. Voluntary deposit has been tried in every country that has tried anything, and it fails for one reason: deposit costs the author time and returns the benefit to everyone else.

The structure that works ties the deposit to something the depositor already wants:

- **Money before mandate.** Deposit is a condition of disbursement for FONDOCYT grants and publicly funded postgraduate theses. The mandate is credible because it is attached to a payment that has not yet been made.
- **The mandate must be funded.** A documentation overhead line on each grant — a fraction of a percent — pays for the curation the mandate creates. An unfunded mandate is a form of theft from the researcher, and it produces empty repositories with excellent policies.
- **Visibility returned to the depositor.** The aggregator must send traffic back to the institutional repository, not absorb it. If the national layer captures the audience, the universities have no reason to maintain their end.
- **Credit where the author feels it.** A DOI and an ORCID assertion convert deposit into citability. "Deposit your work" is a request; "your work will be citable by name and addressable forever" is an offer.
- **Penalties on institutions, not on individuals.** The author's employer is accountable for its repository's harvestability; the author is not accountable for a metadata schema. Sanctioning the author reproduces the problem the system exists to solve.

The free-rider problem is the one to name explicitly: a university that does not deposit still benefits from a national index. The incentive that fixes it is that the index reports, per institution, what it harvested — public coverage ratios are a cheaper sanction than any regulation.

## 4. How is a solution to be evaluated?

At design time, before anything is built, six criteria decide whether the proposal is real:

| Criterion | Question | Passing mark |
| --- | --- | --- |
| Coverage | Does it reach the output that exists, or only the output that is convenient? | Funded projects and theses covered first |
| Interoperability | Is it harvestable by others, or a silo with a search box? | OAI-PMH and a published metadata profile |
| Duty to the source | Does it return traffic and credit to the depositing institution? | Links resolve to the institutional record |
| Preservation | What survives the portal? | A stated term, a format policy, and an exit plan |
| Cost | What does one record cost to acquire, curate and serve? | Comparable to regional peers |
| Reversibility | Can the country leave the vendor without leaving its data? | Open formats, full export, no lock-in |

The last criterion is not hypothetical: a national system that cannot be exported is a national system held hostage by whoever built it.

## 5. How is the operation to be evaluated?

Running metrics, chosen so that none of them can be improved by doing less:

- **Deposit rate** — funded projects and theses with a deposited output, as a ratio, per institution and per year.
- **Latency** — median days from defence or project close to a findable record.
- **Harvest health** — proportion of institutional repositories responding, and the dead-link rate of the aggregated records.
- **Reach** — proportion of national output appearing in regional aggregation, and citations to deposited work.
- **Cost per record** — and its trend, which is the only honest measure of whether curation is scaling.

The rate that must *not* be the headline is international citation, because it rewards the disciplines that publish abroad and penalises exactly those — engineering, agriculture, public health — whose output is the grey literature the system exists to collect.

## 6. What are the case studies?

Comparators worth reading, each for a different reason:

| Case | Model | Lesson |
| --- | --- | --- |
| **Portugal — RCAAP** | National harvester over university repositories | The purest "harvest, do not build"; the universities kept custody and gained reach |
| **Spain — RECOLECTA** | Harvester run by the science foundation with the university libraries | Funded by the research agency, governed with the repositories |
| **Brazil — BDTD and Oasisbr** | National thesis library and national aggregator, built through IBICT | Central build works where an institute has the mandate and the budget |
| **Argentina — SNRD** | National repository system tied to open-access legislation | Mandate-first: the law and the deposit condition came before the portal |
| **Peru — ALICIA** | National repository under the science council | A late starter's problem: the policy arrives after the repositories have chosen incompatible profiles |

The Dominican case is closest to Peru's, which is why the Peruvian experience is the most useful: the profiles and the mandate have to be written together, or the aggregation is a translation exercise for ever.

## 7. What is the history of such systems?

The idea is a century old and has been reinvented twice, which is worth knowing before proposing a third invention.

- **1895–1930, the documentation movement.** The International Institute of Bibliography at Brussels — Otlet and La Fontaine, later the International Federation for Documentation — proposes the universal bibliographic record, and the national documentation centre is born as its unit of implementation.
- **1971, UNISIST.** UNESCO's intergovernmental programme for scientific and technical information makes "a national system for scientific and technical information" a standard piece of state machinery, with a national focal point, a union catalogue and a referral service.
- **1983, the Dominican entry.** Reglamento No. 1255 creates CONACITE, the Consejo Nacional de Ciencia y Tecnología, dependent on the Presidency — the country's one attempt at the UNISIST-style body. It is absorbed into the 2001 law's system, and the documentation function is not carried over.
- **1997–2003, the open-access turn.** SciELO (1997–98) makes a national journal collection feasible; the Budapest, Bethesda and Berlin declarations (2002–03) make deposit a norm; OAI-PMH makes harvesting a protocol instead of a negotiation.
- **2008–2016, the aggregator turn.** National harvesters — RCAAP, RECOLECTA, the Brazilian and Argentine systems — and the regional federation LAReferencia (2012), which aggregates the national nodes rather than the repositories directly.
- **2021, the open-science frame.** UNESCO's Recommendation on Open Science turns the whole chain — records, data, code, evaluation — into an instrument the state is expected to have a policy about.

The Dominican question is therefore not "should we invent this?" It is "which of the two historical forms do we adopt?" — the UNISIST national centre, which is centralised and needs a bureaucracy, or the harvested aggregator, which is decentralised and needs a mandate. The second is cheaper, and it is the one the country's existing repositories make possible.

## References

- International Institute of Bibliography. (1895). *Manuel de documentation bibliographique*. Brussels. — the documentation movement that made the national documentation centre a unit of state
- UNESCO. (1971). *UNISIST: Study report on the feasibility of a world science information system*. Paris: UNESCO. — the programme that standardised the national scientific-information system
- Poder Ejecutivo de la República Dominicana. (1983). *Reglamento No. 1255, que crea e integra el Consejo Nacional de Ciencia y Tecnología (CONACITE)*. — the Dominican entry, cited in the recitals of the 2001 law that absorbed it
- Congreso Nacional de la República Dominicana. (2001). *Ley No. 139-01 de Educación Superior, Ciencia y Tecnología*. Santo Domingo. — SNESCYT, MESCYT, FONDOCYT (Art. 94), and the integration of INDOTEC, IDIA and the Academia de Ciencias (Art. 26)
- Weibel, S., Kunze, J., Lagoze, C., & Wolf, M. (1998). *Dublin Core metadata for resource discovery* (RFC 2413). Internet Engineering Task Force. — the element set a national metadata profile is written on
- Lagoze, C., & Van de Sompel, H. (2001). The Open Archives Initiative: Building a low-barrier interoperability framework. In *Proceedings of the First ACM/IEEE-CS Joint Conference on Digital Libraries* (pp. 54–62). — the protocol that makes "index, do not duplicate" an engineering choice
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016). The FAIR guiding principles for scientific data management and stewardship. *Scientific Data*, 3, 160018. — the standard the aggregator is judged by
- UNESCO. (2021). *Recommendation on Open Science*. Paris: UNESCO. — the current international frame
- [LA Referencia](https://www.lareferencia.info/) — the regional federation of national nodes: the model the proposal adopts
- [SciELO](https://www.scielo.org/) — the national-collection model for journals
- [A Model for Science and Technology Funding](/view.html?p=notes/social/action/public/memorial/a-model-for-science-and-technology-funding.md) — the funding side this note assumes, and the overhead line it proposes
- [An Essay on Dominican Macroeconomic Stability](/view.html?p=notes/social/action/public/informe/an-essay-on-dominican-macroeconomics-stability.md) — the country-study register kept on the informe shelf
