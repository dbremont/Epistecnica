---
tags: [epistemology, ontology, method]
---

# Reality Epistemic Element Set (REES)

> Reality is the total set of phenomena, entities, and processes that exist or occur, independently of an observer's perception or conceptualization, and which can, in principle, interact, change, or produce effects.

> The Reality Epistemic Element Set is the primary catalog and entry point for the scaffolding and systematic investigation of the phenomenology of reality: the recursively typed inventory of the epistemic elements by which an inquirer orients, accesses, represents, constructs, operates on, evaluates, communicates, and sustains knowledge of reality — together with the reflexive elements by which that inventory turns back on the knowing it enables.

This note is the local companion of the canonical guide
[Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md),
which owns the schema, the Permitted Link Forms table, and the worked
Arithmetic case. REES applies that grammar across the whole of reality
rather than to one domain; it states the universal taxonomy and binds each
type to at least one generic instance. Domain catalogues (causality,
mathematical, observational, simulation, optimization, and their siblings)
are recursive expansions of the branches below, not alternatives to them.

The **complete decomposition** lives in the **[REES atlas](data/epistemica/rees.html)** — the
viewer over the tree store [`rees.json`](data/epistemica/rees.json). This note states the
schema, the formulation, and the backbone; the atlas carries the full,
ever-expanding tree with outline, card, table, and node-inspector views.

## Formulation

### What is this epistemic instance?

> The Reality Epistemic Element Set is an organized inquiry system: the
> typed inventory of the epistemic elements involved in the investigation,
> representation, modeling, and explanation of phenomena of reality,
> including the recursive examination of these elements and the nature,
> conditions, and limits of knowing itself.

It is an `Aggregate` in the sense of the canonical guide: a structured
collection of epistemic elements organized as a coherent epistemic whole.
Its root instance is *Reality Inquiry* — the ongoing, cross-domain,
self-auditing practice of turning reality into warranted description. It is
not a domain (it names no segment of reality as its target), and it is not
a single construction (it contains every kind of epistemic element); it is
the scaffolding under which any domain inquiry can be grown.

### What epistemic element type does this epistemic instance belong to?

> `Aggregate`.

Reality Inquiry is a structured collection of epistemic elements, so it
is an `Aggregate` over the inquiry branches. Its children are
typed by those branches — `Epistemic Orientation`,
`Epistemic Agency`, `Epistemic Target`, `Epistemic Access`,
`Epistemic Representation`, `Epistemic Construction`,
`Epistemic Operation`, `Epistemic Evaluation`,
`Epistemic Communication`, `Epistemic Infrastructure`,
`Epistemic Context` — plus the `Ontic` branch of the Ontic Order, which
supplies the parsed reality the inquiry addresses. Read as a technical
system, an inquiry is *readable as* a `Technical Element Set` under the
technicarum grammar; that reading is kept as `readable as …` prose and
decomposed separately.

### Is the type of this `epistemic element instance` ambiguous?

No at the root: `Aggregate` is the only type that covers a whole inquiry
system. Ambiguity appears only in the branches, where the guide's
disambiguation rule applies — an element that could be read under more than
one type takes one primary type and records the rest as `readable as …`.
Two recurring ambiguities are worth stating up front:

- **Access vs. Representation.** An observation interface is `Access`; the
  record it yields is `Access`; what happens to that record once encoded in
  a sign system is `Representation`. The interface does not represent; the
  system does.
- **Construction vs. Representation.** Every representation is also a
  construction (representing a target is constructing an artifact about it),
  but not every construction is a representation: a dataset, a laboratory
  notebook, or an institution are constructions whose representational
  content is secondary.

### What is the recursive instance decomposition of this epistemic instance?

> The table below is the **backbone**: the root *Reality Inquiry*, its twelve
> branches (eleven inquiry branches plus the `Ontic` branch of the Ontic
> Order), the reflexive root, and the *Disciplines* root that indexes the
> organized inquiry systems the other branches presuppose. The **complete,
> ever-expanding decomposition** — every branch grown down to its generic
> instances — is not held in this note: it is the tree store
> [`rees.json`](data/epistemica/rees.json), rendered by the
> **[REES atlas](data/epistemica/rees.html)**. Read the note for the schema and the
> backbone; open the atlas for the full tree and its views.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Reality Inquiry | The organized inquiry system into reality: orientation, agency, target, access, representation, construction, operation, evaluation, communication, infrastructure, context, and its ontic ground. |
| `Aggregate` → Reality Inquiry → `Epistemic Orientation` | Grouping: the directing structure of inquiry. |
| `Aggregate` → Reality Inquiry → `Epistemic Agency` | Grouping: entities and organized activities performing epistemic operations. |
| `Aggregate` → Reality Inquiry → `Epistemic Target` | Grouping: the addressed domain of inquiry. |
| `Aggregate` → Reality Inquiry → `Epistemic Access` | Grouping: means by which the target becomes registrable. |
| `Aggregate` → Reality Inquiry → `Epistemic Representation` | Grouping: structures through which content is encoded and manipulated. |
| `Aggregate` → Reality Inquiry → `Epistemic Construction` | Grouping: artifacts produced to organize, preserve, explain, or extend knowledge. |
| `Aggregate` → Reality Inquiry → `Epistemic Operation` | Grouping: operations and procedures transforming epistemic content. |
| `Aggregate` → Reality Inquiry → `Epistemic Evaluation` | Grouping: evaluative processes assessing constructions and operations. |
| `Aggregate` → Reality Inquiry → `Epistemic Communication` | Grouping: transmission, inscription, and coordination of content. |
| `Aggregate` → Reality Inquiry → `Epistemic Infrastructure` | Grouping: material, computational, informational, institutional structures enabling inquiry. |
| `Aggregate` → Reality Inquiry → `Epistemic Context` | Grouping: surrounding conditions within which inquiry is situated. |
| `Aggregate` → Reality Inquiry → `Ontic` | Grouping: the parsed reality the inquiry addresses — the Ontic Order (segments, entities, processes, events, properties, relations, states, structures, causes). |
| `Aggregate` → Reflexive Inquiry | Inquiry taking its own practice, conditions, and limits as its target. |
| `Aggregate` → Disciplines | The organized inquiry systems other branches presuppose: the disciplines indexed as one epistemic whole. |
| `Aggregate` → Disciplines → Mathematics | The organized inquiry into abstract structure, quantity, space, and change, pursued through deduction from stated axioms. |
| `Aggregate` → Disciplines → Statistics | The organized inquiry into variation, uncertainty, and inference from data. |
| `Aggregate` → Disciplines → Computer Science | The organized inquiry into effective computation: what can be computed, by which procedures, and at what cost. |
| `Aggregate` → Disciplines → Logic | The organized inquiry into valid inference: which conclusions follow necessarily from which premises. |
| `Aggregate` → Disciplines → Philosophy | The organized inquiry into the most general structures of reality, knowledge, and value. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> REES is scaffolding, not a doctrine. It states the universal taxonomy and
> binds each type to a generic instance; it does not decide any particular
> decomposition.

- **Strength.** It gives one typed index spanning the whole of inquiry, so a
  domain catalogue can be grown link by permitted link without inventing a
  vocabulary per domain. Because the root is an `Aggregate` over the
  inquiry branches, the same twelve branches apply whether the target is a
  physical phenomenon, a formal system, or the inquiry itself.
- **Risk of over-extension.** A universal schema can absorb too much: if
  every practice is filed as an instance, the distinctions that carry
  explanatory weight (access vs. construction, standard vs. criterion) are
  flattened. The rule against branch-terminating type segments and the
  requirement that every leaf resolve to an instance are the guard.
- **Boundary with the technical.** Inquiry is also work, and its tools,
  protocols, and institutions are readable as technical elements. REES keeps
  the epistemic reading primary and defers the technical reading to the
  technicarum grammar; the two must not be merged.
- **Self-application.** The reflexive layer below is not an appendix: an
  inventory that cannot account for how it itself was assembled is
  incomplete. REES therefore turns its branches back on inquiry as a target.

## The Two Orders

> An epistemic element type is read under two orders, and the same element
> can be read under both.

- **Inquiry** — orientation, agency, target,
  access, representation (including constitution), construction, operation,
  evaluation, communication, infrastructure, and conditions, plus
  `Aggregate` collections. It answers: how does an inquirer turn reality
  into warranted description?
- **Ontic Order** — the *parsed reality* order: the segments, entities,
  processes, events, properties, relations, states, structures, and causes
  the inquiry addresses. It answers: what is there to be known?

They are mutually constraining duals of the same act. Ontology constrains
what can be known; epistemology constrains how the known is accessed and
represented. REES roots the inquiry branches at `Aggregate` → Reality
Inquiry and the Ontic Order under the `Ontic` branch, and licenses their
exchange through the guide's `Permitted Link Forms` table: an
`Epistemic Target` decomposes to a `Segment of Reality` and an
`Observable`, and an `Ontic` process is what an `Explanation` cites.

## The Reflexive Layer

> The set turns back on itself: inquiry is also a target, and the
> conditions and limits of knowing are themselves epistemic elements. The
> reflexive layer reuses the branches above with inquiry as the addressed
> reality.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Reflexive Inquiry | Inquiry taking its own practice, conditions, and limits as its target. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Target` | Grouping: inquiry as the addressed target. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Target` → Knowing Gap | Deficiency in the account of how knowing works. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Target` → Limit of Knowing | Boundary beyond which the regime cannot register. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Target` → Instrument Effect | The target as altered by the act of registering it. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Standard` | Grouping: standards applied to inquiry itself. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Standard` → Self-Application Standard | A standard stands only if the inquiry that states it also meets it. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Standard` → Reflexivity Standard | An account stands only if it can describe its own production. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Construction` | Grouping: accounts of inquiry. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Construction` → Epistemology | Account of the nature, conditions, and limits of knowing. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Construction` → Methodology | Account of how inquiry should proceed. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Construction` → Ontology | Account of what exists, in service of what can be known. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Evaluation` | Grouping: assessments of accounts of inquiry. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Evaluation` → Philosophical Critique | Assessment of an account of knowing against its own claims. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Evaluation` → `Validation` | Grouping: checks discharging doubt about accounts of inquiry. |
| `Aggregate` → Reflexive Inquiry → `Epistemic Evaluation` → `Validation` → Reflexive Test | An account of knowing is tried against the practice it describes. |

## The Research Circuit

> The branches above are walked as a circuit, not a sequence: each station
> feeds the next and receives its corrections. The circuit is
> Why? → Who? → What? → How accessed? → What is done? → What is produced?
> → How judged? → Under what conditions? → What supports it? → back to
> Why?

| Station | Branch | Element |
| --- | --- | --- |
| Why? | Epistemic Orientation | Purpose, Question, Goal, Gap |
| Who? | Epistemic Agency | Agent, Act, Activity |
| What? | Epistemic Target | Domain, Segment, Observable, Object |
| How accessed? | Epistemic Access | Interface, Encoding, Record |
| How represented? | Epistemic Representation | System, Element, Substrate |
| What is done? | Epistemic Operation | Action, Organization |
| What is produced? | Epistemic Construction | Description, Model, Explanation, Theory |
| How judged? | Epistemic Evaluation | Standard, Criterion, Validation, Error, Feedback |
| Who is told? | Epistemic Communication | Inscription, Publication, Coordination |
| Under what conditions? | Epistemic Context | Condition, Historical, Social |
| What supports it? | Epistemic Infrastructure | Tool, Repository, Institution, Substrate |

## Entry Map

> REES is the index; the domain catalogues are its recursive expansions, and
> the philosophical guides are its schema.

- **The full tree** — the [REES atlas](data/epistemica/rees.html) renders the complete, ever-expanding decomposition from the tree store [rees.json](data/epistemica/rees.json): outline, branch cards, an element search, and a node inspector.
- **Guides** — [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) (schema owner) and [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md) (the technical complement).
- **Universal index** — Naturgnosis Epistemic Space at [http://localhost:8011/epistemica/](http://localhost:8011/epistemica/) carries the full instance graph; REES is the local mastery layer over it.
- **Orientation & target catalogues** — [Modelado](note.html?n=epistemica/theory/practice/modelling.md), [Causality](note.html?n=epistemica/causality.md), [Decision Making](note.html?n=epistemica/decision-making.md).
- **Access & representation catalogues** — [Observational](note.html?n=epistemica/observational.md), [Signal Processing](note.html?n=epistemica/signal-processing.md), [System of Units of Measurement](note.html?n=epistemica/system-of-units-of-measurement.md).
- **Discipline catalogues** — [Mathematics](note.html?n=epistemica/discipline/mathematics.md), [Statistics](note.html?n=epistemica/discipline/statistics.md), [Computer Science](note.html?n=epistemica/discipline/computer-science.md), [Logic](note.html?n=epistemica/discipline/logic.md), [Philosophy](note.html?n=epistemica/discipline/philosophy.md).
- **Operation & construction catalogues** — [Mathematical](index.html?dir=epistemica/mathematical), [Computational Science](note.html?n=epistemica/computational-science.md), [Simulation](note.html?n=epistemica/simulation.md), [Optimization](note.html?n=epistemica/optimization.md), [Natural Computing](note.html?n=epistemica/natural-computing.md), [Statistical Mechanics](note.html?n=epistemica/construction/statistical-mechanics.md).
- **Evaluation & reflexive catalogues** — [Exploratory Data Analysis](note.html?n=epistemica/exploratory-data-analysis-eda.md), [Formal Concept Analysis](note.html?n=epistemica/formal-concept-analysis-fca.md), [Complexity Science](note.html?n=epistemica/complexity-science.md), [Dynamical Intelligence](note.html?n=epistemica/dynamical-intelligence.md).

## QA

### Is REES a domain or an inventory?

> An inventory. It names no segment of reality as its target; it names the
> types of element any domain inquiry is built from. Targeted catalogues
> are its recursive expansions.

### How does REES differ from the philosophia guide?

> The guide owns the grammar — the schema, the `Permitted Link Forms`
> table, and the worked case. REES applies that grammar universally and
> binds each type to generic instances. They are the same project read at
> two levels, which is why the guide is cited as canonical and REES as the
> local companion.

### Why does it include the Ontic Order?

> Because every epistemic move presupposes an ontic parsing, and every ontic
> distinction earns its keep through epistemic use. Keeping the two orders
> in one inventory is what makes the schema a single instrument rather than
> two.

### How does REES relate to the technical?

> An inquiry is also work. Its tools, protocols, and institutions are
> readable as technical elements under the technicarum grammar. REES keeps
> the epistemic reading primary and records the technical reading as
> `readable as …` prose; it does not merge the two trees.

## Relation to Naturgnosis

> Naturgnosis holds the universal instance index across its spaces; REES
> holds the local mastery scaffolding. Legitimate and useful to distinct
> work.

The distinction is one of function:

- **As a representation** (Naturgnosis): the complete graph is the better
  artifact — thousands of nodes, queryable, deep-linkable, cross-domain.
  Use it to look up, traverse, and cite instances.
- **As a construction** (REES): hand-authored cognitive scaffolding — the
  universal taxonomy with generic instances and the permitted-link grammar
  in one readable table — is what makes the schema legible and teachable.
  Use it to reason about the structure of inquiry and to grow a new
  catalogue consistently.
- **Complementary sets.** Naturgnosis answers "which instances exist and
  how are they related"; REES answers "what types must an inquiry
  instantiate, and in what order". The two share the philosophia grammar,
  so an instance named here can be resolved upstream and vice versa.

## References

- [REES atlas](data/epistemica/rees.html) — the complete, ever-expanding decomposition (views over [rees.json](data/epistemica/rees.json))
- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md)
- [Naturgnosis Epistemic Space](http://localhost:8011/epistemica/)
- [Modelado](note.html?n=epistemica/theory/practice/modelling.md)
- [Causality](note.html?n=epistemica/causality.md)
- [Observational](note.html?n=epistemica/observational.md)
- [Mathematics](note.html?n=epistemica/discipline/mathematics.md)
- [Statistics](note.html?n=epistemica/discipline/statistics.md)
- [Computer Science](note.html?n=epistemica/discipline/computer-science.md)
- [Logic](note.html?n=epistemica/discipline/logic.md)
- [Philosophy](note.html?n=epistemica/discipline/philosophy.md)
- Reality, Ontology, Observer, Nature — no dedicated note yet; see the Formulation questions above
