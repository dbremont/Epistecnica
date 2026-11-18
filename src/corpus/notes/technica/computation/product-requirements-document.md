---
tags: [note, product-requirements-document, requirements, specification, product-management, technical-element]
---

# Product Requirements Document

> A **Product Requirements Document** (PRD) is the document that states what a product must do — for its users, its market, and its business — and deliberately does not state how it will do it. It is the requirements-side artifact: it fixes the problem and the acceptance, and leaves the solution to the interface designers and engineers who receive it.

> Its defining rule is a prohibition. The document must *not* anticipate or define the product's implementation, because a PRD that has already chosen the mechanism removes the expertise it was written to employ. That negative constraint is what separates the PRD from the functional or technical specification that follows it: the PRD says what must be true of the product, the functional specification says how the product will be built to make it true.

> The article this note reads is short and its two load-bearing claims — the what-not-how rule and the component list below — are marked there as uncited. The note therefore records them as the article's formulation of the practice rather than as settled doctrine, and marks where the practice itself is contested: a document whose identity is a prohibition is cheap to state, hard to enforce, and unenforceable without the development regime around it.

## Formulation

### What technical element type does this technical instance belong to?

**A Product Requirements Document belongs to `Technical Specification` as its primary kind** — the [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) defines the type as the *precise statement of requirements, parameters, performance, and interface conditions used to define and verify a solution*, and the PRD is that statement at the requirements end: it fixes what the solution must satisfy and is the baseline against which the delivered product is validated.

The typing turns on what the document is **not**. The guide's `Technical Blueprint` is a *generative description prescribing how to create, assemble, or configure an artifact* — and the PRD is precisely the artifact that refuses to prescribe. Its own rule excludes the blueprint reading, which is unusual: most technical documents are typed by what they contain, this one also by what it forbids itself to contain. It is equally not a `Technical Requirement`, because it is the *container* of a requirement set — together with scope, stakeholders, market assessment, assumptions, constraints, dependencies, a high-level plan, and an evaluation plan — rather than a single required state.

Readable secondarily as a `Technical Element Set` — the requirements-document family (product requirements, marketing requirements, user requirements, functional specification) that a development regime assembles — and as a `Technical Blueprint` **only in the degenerate case** where the document has swallowed the design and prescribes the mechanism. That case is the concept's characteristic failure, and the note keeps it as a diagnostic rather than a second root.

### What is this technical instance?

> The document a product organisation writes before it commissions a solution. The article places it in a chain: a user, a client, or the company's marketing department states the requirements from the user's point of view — in that last case the artifact is often called a **Marketing Requirements Document** (MRD); the requirements are then analysed by the (potential) maker from a more technical point of view, broken down and detailed in a **Functional Specification**, sometimes called a Technical Requirements Document. The PRD is the hand-over point of that chain, and its competence is exactly the competence of a hand-over: it must be complete enough to be actionable and silent enough to leave the solution open.

> Its form follows the development regime, and the article names the two that matter. In a **cascading** (waterfall) model the requirements are defined at the very beginning, in their entirety, and development does not begin until they are ready — the PRD is a contract signed before work. In an **agile** model they are formulated initially at a higher level, enough for prioritisation, and elaborated in detail at the beginning of each cycle — the PRD is a standing frame that is re-instantiated per iteration, and its granularity, not its existence, is what changes.

> **Its components.** Title and author; purpose and scope from both the technical and the business side; stakeholder identification; market assessment and target demographics; product overview and use cases; the requirement set — functional, usability, technical (security, network, platform, integration, client), environmental, support, interaction; assumptions; constraints; dependencies; high-level workflow plans, timelines, and milestones; and an evaluation plan with performance metrics. The article adds the honest qualification that not every PRD has all of these, and that a PRD for a manufactured good drops the software-specific elements and adds its own — manufacturing requirements in that case. The component list is thus a **template for a class**, not a definition of the class.

> **Its failure modes**, as the article lists them: the document is written without a complete understanding of what the customer wants; the information in it is incomplete or inaccurate and is not updated as it changes; requirements are communicated unclearly between stakeholders and users; and the timeframes it sets are unrealistic. The three technical problems it is claimed to prevent are the mirror image — architecture mismatching the product requirements, overlooked technical dependencies, and underestimated implementation complexity — and the claim is worth stating as a claim: the document prevents them only where it is read, and the article's own evidence is a list rather than a measurement.

### What is the recursive instance decomposition of this technical instance?

> Boundary: one requirements document, decomposed at middle depth — its identification and frame, its stakeholders, the demand-side evidence, the product narrative, the requirement set typed by the guide's requirement kind, the conditions it declares, the plan and the evaluation it commits to, and the evaluation that uses it as its baseline.
>
> Stopping rule: a row is terminal when it names a document section, a requirement kind, a declared condition, a plan element, a metric, or an evaluation.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document | Root: the requirements-side specification of a product — what it must do for its users, its market, and its business, with the implementation deliberately left open. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Part)` Front Matter | Grouping: the identification and the frame that tell a reader whose document this is and what it does not cover. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Part)` Front Matter `(→ Has)` Title And Author | The document's identity and its owner — the section that makes the rest attributable and therefore reviewable. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Part)` Front Matter `(→ Has)` Purpose And Scope | What the product is for, stated from both the technical and the business side, and the boundary of what this document decides — the section that makes the what-not-how rule enforceable. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Stakeholder Identification | The parties whose needs the product answers and whose agreement the document needs — users, clients, the commercial side, the makers. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Market Assessment | Grouping: the demand-side evidence, which is what distinguishes the product-side document from the engineering-side one. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Market Assessment `(→ Has)` Target Demographic | The population the product is for, stated as a segment rather than as an average user. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Product Overview | Grouping: the narrative of the product before its requirements, told as scenarios rather than as features. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Product Overview `(→ Has)` Use Case | One scenario of use: an actor, a goal, and the interaction that reaches it — the unit in which requirements become arguable. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` `Technical Requirement` | Grouping: the requirement set, typed by the guide's requirement kind; each member is an instance of `Technical Requirement`, not a type of its own. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` `Technical Requirement` `(→ Instance)` Functional Requirement | What the product must do: the services, behaviours, and functions it must provide. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` `Technical Requirement` `(→ Instance)` Usability Requirement | How effectively the intended users must be able to use it — the requirement kind that carries the user's point of view into the document. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` `Technical Requirement` `(→ Instance)` Product Technical Requirement | The article's "technical requirements": security, network, platform, integration, and client constraints — the software-specific members that a non-software PRD drops. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` `Technical Requirement` `(→ Instance)` Environmental Requirement | The conditions of use the product must survive or satisfy — the field in which a product's context stops being assumed and becomes a requirement. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` `Technical Requirement` `(→ Instance)` Support Requirement | What the product needs in order to be sustained after delivery — maintenance, service, and the organisation that provides them. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` `Technical Requirement` `(→ Instance)` Interaction Requirement | How the product must work with other systems — the requirement kind at which scope stops at the product boundary and the interface begins. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Assumption | What the document takes as given without warranting it — the section that makes the document's fragility reviewable. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Constraint | What the solution may not do: budget, regulation, platform, deadline, and the limits inherited from the organisation. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Dependency | What the product requires from outside itself — other systems, teams, suppliers, or decisions that must land before this one can. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Workflow Plan | Grouping: the delivery commitment at the granularity a requirements document may carry — intent, not scheduling. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Workflow Plan `(→ Has)` Milestone | A dated checkpoint of the delivery — the only schedule element the PRD keeps, the detailed plan being the project plan's business. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Evaluation Plan | Grouping: how the delivered product will be judged against the document. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Has)` Evaluation Plan `(→ Has)` Performance Metric | A measurable quantity by which success is decided — the clause that makes the rest of the document testable rather than aspirational. |
| `Technical Element` `(→ Kind)` `Technical Specification` `(→ Instance)` Product Requirements Document `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Validation` `(→ Instance)` Product Acceptance Validation | Does what was built fulfil the need the document stated? The PRD is the warrant of that question, not the answer to it. |

### What is a critical conceptual evaluation of this `technical element instance`?

> **Verdict.** The PRD is a genuine technical artifact with a sharp identity and a weak definition. Its identity is a **prohibition** — the document must state what without stating how — and that prohibition does more conceptual work than any of its components: it distinguishes the artifact from the functional specification above it (the maker's answer), from the marketing requirements document below it (the market's input), and from the project plan beside it (the schedule). Its weakness is that the prohibition is unenforceable from inside the document: nothing in a PRD records whether its author respected it, the component list varies by organisation and domain, and the article that defines it does so without citations. The concept therefore describes a **role in a development regime** more reliably than it describes a text, which is why agile development changes its granularity without abolishing it and why a document written to satisfy a process rather than to communicate is the concept's characteristic failure.

| Criterion | Verdict | Diagnostic Focus |
| --- | --- | --- |
| Conceptual Identification | Strong | Distinguished from the functional/technical specification (the makers' how), from the MRD (the market's input), and from the project plan (the schedule); the test is whether the document decides what must be true of the product while leaving the mechanism open. |
| Definitional Clarity | Weak–Moderate | The one-sentence definition is clear; the component list is a template for a class and the article marks both the definition and the list uncited. "Requirements" is doing the work, and the corpus already uses that word for a typed element. |
| Conceptual Determinacy | Moderate | The boundary rule is a prohibition, which decides clear cases sharply and borderline ones badly: a PRD that names a mandated platform, a regulatory mechanism, or a reference architecture has begun to prescribe, and the concept cannot say where the line falls. |
| Internal Consistency | Moderate–Strong | Purpose, scope, requirement set, and evaluation plan cohere as one argument; the tension is structural rather than internal — the document must be complete and must not decide, and completeness pushes toward deciding. |
| Representational Adequacy | Moderate | The decomposition covers the article's components and the requirement kinds the corpus already types, but it cannot represent the *quality* of the writing, which is where the artifact succeeds or fails. |
| Discriminative Power | Strong | It separates the requirements-side document from the solution-side one, which is the distinction practitioners actually argue about; weaker against a well-written product brief or a lean canvas. |
| Operationalizability | Moderate–Strong | The components are checkable and the evaluation plan is measurable; nothing records whether the what-not-how rule was kept. |
| Temporal Stability | Weak | Stable as a role from the mid-twentieth-century engineering-process tradition into software; unstable as a text, since agile re-granularises it per cycle and some shops replace it with a backlog and a one-pager. |
| Performative Effects | Strong | The document allocates authority: writing a PRD is how the product side claims the right to decide the what, and the engineering side's counter-claim (the specification) is the reason the prohibition exists. |
| Misuse Resistance | Weak | The failure mode is built in — a PRD can be produced to satisfy a gate rather than to communicate, and the concept cannot tell the two apart; the article's "common problems" list is a symptom list, not a test. |
| Purpose Adequacy | Strong | For product management in a development regime it does exactly what it claims: it hands over a problem with an acceptance, and it is the baseline of validation rather than verification. |

## QA

### Is a PRD a specification?

> Yes in type, no in position. It is typed as a `Technical Specification` because it is a precise statement of what a solution must satisfy, and it is the baseline of the product's validation. It is not the specification the engineers work from: that is the functional or technical specification, which answers the PRD's what with a how. The corpus's [Specification](/view.html?p=notes/technica/computation/specification.md) note holds the requirement kinds both documents draw on; the difference between them is which end of the requirements-to-solution arrow each one fixes.

### Why must a PRD avoid saying how?

> Because the document's purpose is to preserve the solution space it hands over. If the author has already chosen the mechanism, the engineers' and designers' expertise is reduced to execution, and the document has silently become a specification — with the additional cost that its author now owns a decision they were not positioned to make. The rule is also the concept's weak point: it is stated as a norm with no test, and the article marks it uncited, so in practice the prohibition is enforced by review culture rather than by the document.

### How does a PRD differ from a marketing requirements document?

> By who writes it and what it is for. The MRD is the market-side statement — what the market wants, stated by marketing or by the client — and the article treats the PRD as the document that may *be* an MRD when the marketing department authors it. The PRD is the requirements document the makers receive; the MRD is one of its possible provenances. The distinction is institutional rather than conceptual, which is why the same text can be both.

### Does agile development abolish the PRD?

> No — it changes its granularity. The article's own contrast is between the cascading model, where the requirements are fixed in their entirety before development begins, and the agile model, where they are formulated at a higher level to allow prioritisation and elaborated at the start of each cycle. What agile removes is the *signed contract* reading of the document, not the requirements statement; what it adds is the demand that the statement be re-instantiated rather than frozen. A team that writes no requirements at all has not replaced the PRD, it has moved the requirements into conversation and into the backlog.

### Is it a technical element or a management artifact?

> Both, and the typing picks the technical side. The document directs a transformation of reality — it states what a product must satisfy — so it is a `Technical Specification`; the business case, the budget, and the staffing are management artifacts and are not parts of it. The article's component list includes market assessment and timelines, which is where the two sides touch: those sections are *context for* the requirements, not requirements, and a PRD that grows into a business plan has crossed the same line as one that grows into a specification.

## References

- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/philosophia-artium-technicarum-et-operis.md) (the type vocabulary and the decomposition grammar)
- [Philosophia Conceptuum et Operis](/view.html?p=notes/philosophia-conceptuum-et-operis.md) (the evaluation criteria)
- [Specification](/view.html?p=notes/technica/computation/specification.md) (the requirement kinds this document's requirement set instantiates)
- [Product Development](/view.html?p=notes/technica/computation/product-development.md) (the discipline the document belongs to)
- [Documentation](/view.html?p=notes/technica/computation/system/documentation.md) (the document-kind registry it is listed in)
- [Software Specification](/view.html?p=notes/technica/computation/system/design/software-specification.md) (the solution-side counterpart)
- [Agile Model](/view.html?p=notes/technica/computation/system/design/agile-model.md) (the regime that re-granularises the document)
- [Waterfall Model](/view.html?p=notes/technica/computation/system/design/waterfall-model.md) (the regime that fixes it in its entirety before work)
- [Technica Atlas](/corpus/notes/technica/atlas.html) (the forest this decomposition feeds)
- [Product requirements document](https://en.wikipedia.org/wiki/Product_requirements_document)
