---
tags: [note, epistemology, ontology, method]
---

# Philosophia Artium Epistemicarum et Operis

> Reality is the total set of phenomena, entities, and processes that exist or occur, independently of an observer’s perception or conceptualization, and which can, in principle, interact, change, or produce effects.

> Philosophia Artium Epistemicarum is the scaffolding used to parse, and render intelligible, reality.

> This note is a guide connecting Reality (Nature) with its Representation — modeling, computation, formal systems, algorithms, observers, and representations. It is the complement of Philosophia Artium Technicarum et Operis: where that note systematizes intervention in reality, this one systematizes how reality becomes intelligible.

## Formulation

### What is the nature of epistemic practice?

> Epistemology: (Reality; Ontology) → Description & Validation.

> An epistemic act is any operation performed by an observer to construct, transform, evaluate, or apply knowledge about reality.

> The goal of epistemology is (1) to construct and maintain the scaffolding mechanisms of inquiry, and (2) to construct, validate, and derive the set of constructions about a domain — the Domain Epistemic Artifact Set (DESA) — that represents reality.

### What is the role of the `episteme` in human experience?

> The episteme renders reality intelligible: it compresses observations into descriptions that explain, predict, and enable intervention — and it disciplines thinking through formal artifacts rather than mental representations alone.

> Humanity identifies aspects of reality worth describing by discovering recurring patterns that enable explanation, prediction, intervention, or compression of experience. A worthy aspect compresses observations of reality by minimizing description length while maximizing our ability to intervene.

### What ground 'epistemic practice'?

> Epistemic practice is grounded in an observer-independent reality accessed through observation and inference.

> **Ontology and epistemology are the right hand and left hand of knowledge construction: they are mutually constraining duals of the same epistemic act.**
>
> - **Ontology** = what *is* (constraint space of reality)
> - **Epistemology** = how it is *accessed/represented* (constraint space of knowing)
> - They are not separate domains, but **co-dependent operators on the same reality-model interface.**

### What is the reality we seek to represent?

> Observer-independent reality: it exists whether perceived or modeled; it is composed of entities and processes with causal effects; it is dynamic and interconnected, producing emergent patterns; and it is accessible — imperfectly — through observation and inference constrained by what actually exists.

> Reality is cut for inquiry into segments; each segment is then decomposed in the naturalis or social grammar, never here.

### At which level of organization do we inquire?

> The hierarchical stratification of structural and functional components, from microscopic interactions to emergent macroscopic behaviors — crucial when modeling systems with multiscale dynamics, memory, or adaptive laws.

- **Micro-level:** Individual elements and their local interactions.
- **Meso-level:** Subsystems, modules, clusters of interactions.
- **Macro-level:** Emergent patterns, global behavior, systemic properties.
- Systems thinking is **hierarchical**: different questions require different levels of analysis.

### What is the ontology of the target?

> What is reality like? Which elements make it up? How do we identify them? How do we think deeply about change — and about change as an element of reality itself? Ontology answers by constraining what can be known; its constructs for parsing (segments, entities, processes, phenomena) appear below as the target elements a domain `Has`, and its full template belongs to the naturalis grammar.

### What Is a `Epistemic Element`?

> An Epistemic Element is anything that occupies a role in the practice by which reality is made intelligible: the reality cut as a target; the practice that investigates it; the constructions it produces; or anything that enables, constrains, evaluates, communicates, or conditions that practice.

> Its boundaries are broad by design — a domain, an activity, a notation, a dataset, and an ontic segment sit in the same category — but they are not empty: an element qualifies when its absence, substitution, or alteration changes what inquiry can reach, produce, or warrant, and the types order what it admits. The term denotes the category; the elements it covers are its instances.

#### What is the fundamental structure of an epistemic element's `Decomposition Tree`?

```text
Epistemic Element (parent)
  (→ <Relationship Type>) <Epistemic Element>*  (son)
```

#### Which are some ideas to guide the decomposition of an `epistemic element`?

> A reference table defining the permitted link forms that govern and standardize the recursive decomposition of an `Epistemic Element` into its constituent and related epistemic elements.

> **Note:** If an `Epistemic Element` appears as a parent in a decomposition tree, only the child elements explicitly permitted by this reference table may be included, unless the child elements are defined by a template specified using `<<...>>`.
>
> **Note:** This kind of structure neither completes nor normates a decomposition. The table states only which parent–child links are permitted; it decomposes nothing by itself, and it does not dictate what any particular element must decompose into. A decomposition is complete only for a bound root instance, grown link by permitted link until every leaf resolves to an instance.

> **Note:** The generic form `<<Epistemic Element>> (→ <Relationship Type>) <<Epistemic Element>>` shown in the structure above describes the shape every row takes; it licenses nothing by itself. Only the specific rows below license a link, and a link no row names is not permitted.

| Permitted Link Form | Description | Tags |
| --- | --- | --- |
| `Epistemic Element (→ Kind) Epistemic Element Set` | Classifies an element as a coherent aggregate of epistemic elements. | Classification; Set |
| `Epistemic Element Set (→ Member) <<Epistemic Element>>` | Identifies a member of the aggregate; membership, not composition. | Composition; Set |
| `Epistemic Element Set (→ Kind) Epistemic Practice` | Classifies a set as an organized pattern of inquiry carried on by agents — the doing. | Classification; Set |
| `Epistemic Element Set (→ Kind) Epistemic Framework` | Classifies a set as a group of epistemic elements read together as one lens. | Classification; Set |
| `Epistemic Element (→ Has Property) Property` | Identifies a predicated feature of the parent element; the type binds to its instances. | Predication; Property |
| `Epistemic Element (→ Kind) Epistemic Activity` | Classifies a situated bundle of inquiry doings, read as a root in its own right. | Classification; Activity |
| `Epistemic Practice (→ Member) Epistemic Practice` | Identifies a sub-practice as a member of the aggregate: field, sub-field, laboratory, school, tradition, or specialty. | Composition; Member |
| `Epistemic Practice (→ Has) Epistemic Activity` | Identifies a situated bundle of inquiry doings that applies one or more methods. | Composition; Activity |
| `Epistemic Activity (→ Has) Epistemic Method` | Identifies a generalized method the activity applies. | Composition; Activity |
| `Epistemic Activity (→ Part) Epistemic Act` | Identifies a primitive inquiry act the activity bundles. | Composition; Activity |
| `Epistemic Activity (→ Has) Epistemic Orientation` | Identifies the orientation a situated activity poses for itself. | Composition; Activity |
| `Epistemic Method (→ Part) Epistemic Method` | Identifies a step or sub-method of a larger method. | Composition; Method |
| `Epistemic Practice (→ Has) <<Epistemic Lane>>` | Identifies a lane the practice carries. | Composition; Practice |
| `Epistemic Practice (→ Addresses) Segment of Reality` | Identifies the bounded portion of reality the practice works on — the cut. | Composition; Practice |
| `Epistemic Practice (→ Has) Observable` | Identifies a feature of the addressed segment the practice can register. | Composition; Practice |
| `Epistemic Practice (→ Has) Epistemic Framework` | Identifies the lens system the practice reasons with. | Composition; Practice |
| `Epistemic Practice (→ Produces) Epistemic Construction` | Identifies a construction the practice leaves behind. | Composition; Practice |
| `Epistemic Element (→ Kind) <<Epistemic Lane>>` | Classifies an element as one of the inquiry lanes. | Classification; Lane |
| `Epistemic Orientation (→ Has) <<Orientation Element>>` | Identifies a directing element of the orientation. | Orientation; Purpose |
| `Epistemic Agency (→ Has) Epistemic Agent` | Identifies an entity capable of performing epistemic acts. | Agency; Agent |
| `Epistemic Agent (→ Kind) Epistemic Collective` | Classifies an agent as a body whose members inquire jointly. | Agency; Collective |
| `Epistemic Collective (→ Member) Epistemic Agent` | Identifies a member agent of the collective. | Agency; Member |
| `Epistemic Agency (→ Has) Epistemic Role` | Identifies a position an agent occupies within the practice. | Agency; Role |
| `Epistemic Access (→ Has) Observation Interface` | Identifies a boundary mechanism coupling a segment to registration. | Access; Interface |
| `Observation Interface (→ Part) <<Observation Element>>` | Identifies an interface constituent. | Composition; Access |
| `Epistemic Access (→ Has) Observation Encoding` | Identifies the format in which a registered observation is carried. | Access; Encoding |
| `Epistemic Access (→ Has) Observation Record` | Identifies a registered representation of an observed aspect. | Access; Record |
| `Observation Record (→ Represents) Observable` | Identifies the observable feature a record stands for. | Access; Representation |
| `Epistemic Representation (→ Has) Representational System` | Identifies a sign system within which representations are formed and interpreted. | Representation; System |
| `Representational System (→ Part) Representation Element` | Identifies a combinable constituent of the system. | Representation; Element |
| `Representational System (→ Part) Constitutive Substrate` | Identifies the rules and structures constituting the system. | Representation; Substrate |
| `Constitutive Substrate (→ Part) <<Constitutive Element>>` | Identifies a constituting rule or structure. | Representation; Substrate |
| `Epistemic Element (→ Kind) Epistemic Construction` | Classifies a construction: an artifact produced to organize, preserve, explain, or extend knowledge about a target. | Classification; Construction |
| `Epistemic Construction (→ Kind) <<Epistemic Construction>>` | Classifies a construction kind without asserting which kind before it is bound. | Classification; Construction |
| `Epistemic Construction (→ Part) Epistemic Construction` | Identifies a constituent construction: a theory holds models, a model holds constructs. | Composition; Construction |
| `Epistemic Construction (→ Has) Representational System` | Identifies the sign system the construction is written in. | Construction; Representation |
| `Epistemic Construction (→ Represents) <<Represented Aspect>>` | Identifies what the construction stands for. | Construction; Representation |
| `Epistemic Construction (→ Derived From) Observation Record` | Identifies the records the construction was built from. | Construction; Derivation |
| `Epistemic Construction (→ Evaluated By) Validation` | Identifies the check that discharges doubt about the construction. | Construction; Evaluation |
| `Epistemic Construction (→ Governed By) Epistemic Standard` | Identifies the standard the construction must satisfy. | Construction; Evaluation |
| `Epistemic Element (→ Kind) Epistemic Act` | Classifies a primitive act of inquiry, read as a root in its own right. | Classification; Action |
| `Epistemic Act (→ Kind) <<Action Element>>` | Classifies a primitive act of inquiry. | Action; Classification |
| `Inference (→ Kind) Deduction` | Classifies a derivation in which the conclusion follows necessarily. | Action; Inference |
| `Epistemic Act (→ Transforms) Epistemic Construction` | Identifies the construction an act produces or rewrites. | Action; Construction |
| `Epistemic Act (→ Governed By) Epistemic Standard` | Identifies the standard the act must satisfy. | Action; Evaluation |
| `Epistemic Evaluation (→ Has) <<Evaluation Element>>` | Identifies an evaluative constituent. | Evaluation; Standard |
| `Epistemic Element (→ Kind) Epistemic Feedback` | Classifies feedback read as a root in its own right. | Classification; Evaluation |
| `Epistemic Communication (→ Has) <<Communication Element>>` | Identifies a communication constituent. | Communication; Inscription |
| `Epistemic Infrastructure (→ Has) <<Infrastructure Element>>` | Identifies an infrastructure constituent. | Infrastructure; Tool |
| `Epistemic Context (→ Has) Epistemic Condition` | Identifies a surrounding condition within which inquiry is interpreted. | Context; Conditions |
| `Epistemic Guidance (→ Has) <<Guidance Element>>` | Identifies a directive constituent that steers inquiry. | Guidance; Directive |
| `Epistemic Organization (→ Has) <<Organization Element>>` | Identifies an arrangement constituent that coordinates inquiry work. | Organization; Arrangement |
| `Epistemic Framework (→ Has) Epistemic Tool` | Identifies a tool the lens carries. | Composition; Framework |
| `Epistemic Framework (→ Has) Epistemic Construction` | Identifies a construct the lens carries. | Composition; Framework |

### Which are the available expansions of the slots?

> A slot (`<<…>>`) is bound to a **type**, never to an instance. Each row names one type the slot may take.

| Slot | Expansion | Description |
| --- | --- | --- |
| `<<Epistemic Element>>` | any type licensed in this guide | Binds the parent or child of the generic link form; the specific rows decide which pairs are permitted. |
| `<<Relationship Type>>` | any label in the relationship table | Names the relation asserted; the permitted table decides which labels may join which types. |
| `<<Epistemic Lane>>` | `Epistemic Orientation` | Why: the standingly posed purposes, questions, and gaps that direct the practice, and the ones an activity poses for itself. |
| `<<Epistemic Lane>>` | `Epistemic Agency` | Who: the agents and roles that carry the practice. |
| `<<Epistemic Lane>>` | `Epistemic Access` | How registered: the interfaces, encodings, and records the practice works through. |
| `<<Epistemic Lane>>` | `Epistemic Representation` | In what: the notations and representational systems the practice reads and writes. |
| `<<Epistemic Lane>>` | `Epistemic Evaluation` | How judged: the standards, criteria, errors, checks, and feedback. |
| `<<Epistemic Lane>>` | `Epistemic Communication` | How shared: inscription, publication, and coordination. |
| `<<Epistemic Lane>>` | `Epistemic Infrastructure` | What supports it: tools, repositories, and institutions. |
| `<<Epistemic Lane>>` | `Epistemic Context` | Under what conditions: the surrounding conditions of the practice. |
| `<<Epistemic Lane>>` | `Epistemic Guidance` | Under what direction: the principles, protocols, and methodologies that steer inquiry. |
| `<<Epistemic Lane>>` | `Epistemic Organization` | Arranged how: the programmes, projects, workflows, schedules, and divisions of labour that coordinate inquiry. |
| `<<Orientation Element>>` | `Epistemic Purpose` | The intended ultimate effect or value of the inquiry. |
| `<<Orientation Element>>` | `Epistemic Question` | A formulated question directing inquiry toward a gap. |
| `<<Orientation Element>>` | `Epistemic Goal` | A desired epistemic outcome toward which inquiry is directed. |
| `<<Orientation Element>>` | `Epistemic Gap` | A deficiency in available knowledge relative to the target. |
| `<<Guidance Element>>` | `Epistemic Principle` | A general rule that guides inquiry without being an end or a norm of judgment. |
| `<<Guidance Element>>` | `Epistemic Protocol` | The course an inquiry is laid down to follow, prescribed rather than performed. |
| `<<Guidance Element>>` | `Epistemic Methodology` | A directive account of how methods are chosen, combined, and justified. |
| `<<Organization Element>>` | `Epistemic Programme` | A coordinated set of inquiry projects under one objective. |
| `<<Organization Element>>` | `Epistemic Project` | A bounded unit of organized inquiry with an end and a term. |
| `<<Organization Element>>` | `Epistemic Workflow` | An arrangement of inquiry acts into a reproducible sequence. |
| `<<Organization Element>>` | `Epistemic Schedule` | An arrangement of inquiry work in time. |
| `<<Organization Element>>` | `Epistemic Division of Labour` | An allocation of inquiry roles and acts across agents. |
| `<<Observation Element>>` | `Transduction` | The conversion of a segment's state into a registrable signal. |
| `<<Observation Element>>` | `Sampling` | The selection of which occurrences or positions are registered. |
| `<<Constitutive Element>>` | `Convention` | A stabilized notational or interpretative choice. |
| `<<Constitutive Element>>` | `Formation` | A rule of well-formed combination. |
| `<<Constitutive Element>>` | `Transformation Rule` | A rule licensing the rewrite of well-formed expressions into other well-formed expressions. |
| `<<Constitutive Element>>` | `Foundation` | The axioms or principles a system is founded on. |
| `<<Constitutive Element>>` | `Interpretation` | A meaning assignment from symbols to what they denote. |
| `<<Epistemic Construction>>` | `Description` | A structured affirmation about a segment of reality. |
| `<<Epistemic Construction>>` | `Record` | An observation persisted as an addressable entry. |
| `<<Epistemic Construction>>` | `Dataset` | A structured collection of records for analysis. |
| `<<Epistemic Construction>>` | `Concept` | A constructed discriminator of aspects of the segment. |
| `<<Epistemic Construction>>` | `Model` | A construction enabling prediction or explanation of the segment. |
| `<<Epistemic Construction>>` | `Explanation` | A description clarifying cause, mechanism, or relation. |
| `<<Epistemic Construction>>` | `Prediction` | A description asserting an unobserved state or outcome. |
| `<<Epistemic Construction>>` | `Theory` | A system of constructs and claims about the segment. |
| `<<Epistemic Construction>>` | `Trajectory` | An ordered sequence of states attributed to the segment. |
| `<<Represented Aspect>>` | `Segment of Reality` | The bounded portion of reality a construction stands for. |
| `<<Represented Aspect>>` | `Observable` | A registrable feature of the segment a construction encodes. |
| `<<Action Element>>` | `Inference` | A derivation of content from premises. |
| `<<Action Element>>` | `Observation` | The registration of a state through an interface. |
| `<<Action Element>>` | `Measurement` | The assignment of a value to an observable under a scale. |
| `<<Action Element>>` | `Classification` | The assignment of an instance to a type. |
| `<<Action Element>>` | `Computation` | A rule-governed transformation of represented content. |
| `<<Action Element>>` | `Comparison` | A judgment of identity, difference, or order between two items. |
| `<<Evaluation Element>>` | `Epistemic Standard` | The norm against which an artifact or act is judged. |
| `<<Evaluation Element>>` | `Epistemic Criterion` | The property on which the judgment turns. |
| `<<Evaluation Element>>` | `Epistemic Constraint` | A bound on what the inquiry can achieve or hold. |
| `<<Evaluation Element>>` | `Epistemic Error` | A deviation of an artifact or act from its standard. |
| `<<Evaluation Element>>` | `Validation` | A check that tests an artifact against reality. |
| `<<Evaluation Element>>` | `Verification` | A check that tests an artifact against its blueprint. |
| `<<Evaluation Element>>` | `Epistemic Feedback` | The return of an evaluation into the next act. |
| `<<Communication Element>>` | `Epistemic Inscription` | A persistent rendering of epistemic content. |
| `<<Communication Element>>` | `Epistemic Publication` | The release of content to a readership. |
| `<<Communication Element>>` | `Epistemic Coordination` | The alignment of several agents' epistemic work. |
| `<<Infrastructure Element>>` | `Epistemic Tool` | An implement that extends what an agent can do. |
| `<<Infrastructure Element>>` | `Information Repository` | A store consulted instead of recomputed. |
| `<<Infrastructure Element>>` | `Epistemic Institution` | A body that sustains inquiry across generations. |

## How to decompose any epistemic element?

> A decomposition recursively expands an epistemic instance tree from its root: bind the root instance, then grow its subtree by attaching only links the `Permitted Link Forms` table allows, down to instance leaves. The reference tables above are scaffolding — necessary but not sufficient, and never normative: they say which links *may* appear, not which decomposition is correct for any given element. Choosing instances, depth, and stopping point remains the decomposer's work on the instance itself.

> See the worked case in QA below (### (Case Study) What is the recursively decomposed instance tree of Arithmetic?). Read the case table as the worked in-path-typed tree: the empty table here is filled the same way, typing each row from its nearest enclosing grouping segment and naming every link with its relationship type.

> The ontic questionnaire belongs to the naturalis or social grammar; this guide starts on the other side of it — with the practice that cuts the segment.

> Note: Instance rows in the Instance Tree Path name instances, never types. Type names appear only as backticked grouping segments and never terminate a branch.

> **Constructing the instance path:** (1) bind the root — name the instance being decomposed; (2) extend — append each child by exactly one link the `Permitted Link Forms` table licenses, labelling it `(→ Relationship Type)`; (3) type — resolve each segment to its nearest enclosing grouping segment, declaring the root's type once; (4) check — every leaf resolves to an instance, no bare type terminates a branch, and no bare arrow remains.

**Rules:**

- **Form of the Table:** `Instance Tree Path | Description`.
- **Instance Tree Path**: A unique, recursively extended path identifying an instance within the decomposition tree. It begins at the root node `Epistemic Element`, descends the licensed kind chain to the instance's type, and appends each successive child through an explicitly labeled relationship, using the form Parent Instance (→ Relationship Type) Child Instance. Each successive path must preserve the complete path from the root to the current instance.
- **Relationship Labeling:** Every link between a parent and child names its relationship type, styled `(→ Kind)`, `(→ Has)`, `(→ Part)`, `(→ Instance)`, `(→ Addresses)`, `(→ Produces)`, or another label from the relationship table. A bare arrow is not permitted. Typing reads from grouping segments, never from the link: an instance resolves to its nearest enclosing grouping segment's type, with the decomposition root's type declared once.
- **Grouping Segments:** Every backticked grouping segment names a type licensed by the `Permitted Link Forms` table. A type that is not a row there may not appear in a tree, even when the relationship itself is permitted.
- **One Type per Distinction:** Do not type the same distinction twice. A discipline is an `Epistemic Practice`, never an `Epistemic Discipline` row. A set disaggregates by `Member` for the members it is a group of, or by `Has` for what it carries and associates; `Part` is reserved for structured wholes — a method's steps, a construction's constituents.
- **Permitted Links:** Every relationship must conform to a link form allowed by the `Permitted Link Forms` table. A link form licenses a possible relationship; it does not establish that the relationship actually exists in the instance being decomposed. `Instance` binds a type segment to an instance and needs no entry in that table.
- **Act Metadata:** Which method prescribes an act, and which activity performs it, is recorded as metadata on the act's node — never as a further link in its path. The path records composition alone; a method's act-set is not grown as a branch, because the acts are carried by the activity that runs them (see "How is the method that prescribes an act recorded?" in QA).
- **Recursive Expansion:** Any epistemic instance identified in the tree may itself be decomposed recursively.
- **Decomposition Scope:** Select the aspects of the instance that need to be represented. A decomposition need not include every conceivable aspect of epistemic reality; it must adequately cover the aspects relevant to its stated purpose.
- **Stopping Condition:** Stop expanding a branch when its instance is sufficiently specified for the decomposition's purpose, when further expansion is unnecessary, or when the available evidence does not justify additional decomposition. A leaf is a stopping point in the current decomposition, not necessarily an intrinsically indivisible element. Every leaf must resolve to an epistemic instance.
- **Completeness:** A decomposition is complete relative to its declared scope and stopping criteria, not merely because every branch terminates. Relevant constituents, relations, structures, processes, states, and other aspects must not be omitted simply because the tree is syntactically valid.
- **Unlicensed or Uncertain Relationships:** If a necessary relationship is not covered by the reference table, do not silently invent a permitted link or substitute an unrelated one. Identify the gap and extend the reference table when justified. If the existence of a relationship is uncertain, mark that uncertainty rather than presenting the relationship as established.
- **Instance Identity:** Distinguish different instances even when they share the same type or description. The full `Instance Tree Path` identifies an instance's position within the particular decomposition; it does not, by itself, establish a globally unique identity outside that tree.
- **Path Stability:** Because the path is the identity of the occurrence, it changes only by addition. Grow a tree by appending to the right; never rename, reorder, or re-parent an existing segment in place. When an instance must move, write its new path and mark the old row `superseded by <new path>` instead of rewriting it, so the tree records the correction rather than erasing the decision. Two rows carrying the same path are one occurrence; two paths are two occurrences, even under the same name.
- **Tree Structure:** Each non-root row must extend an existing parent path by exactly one child relationship. The same instance may appear in multiple branches when it plays different roles in the decomposition; each occurrence must have its own path. Ensure a rich set of intermediate (internal) nodes — both types and instances — aiding understanding: composition, representation, transformation, validation, or other useful structural relationships.
- **Acyclicity:** No path may return to an instance it already contains. The structure is a tree; a relationship that would close a loop belongs to another tree, linked rather than grown.
- **Kind Trees:** When the purpose is to say what kinds a type admits — the kinds of `Model`, the kinds of `Epistemic Tool` — root the tree at the type and use `Kind` links only. A kind tree stops at types, never at instances, and the leaf-instance rule does not apply to it. It is a second instrument, not an instance decomposition, and the two are never mixed in one table.
- **Non-Normativity of Reference Tables:** The reference tables constrain which link forms may be used. They do not prescribe a universal decomposition order, determine which children must be included, or guarantee that a decomposition is conceptually adequate.
- **Well-formedness:** an instance decomposition is well-formed when every non-root row extends an existing path by exactly one link the `Permitted Link Forms` table licenses, every grouping segment carries a licensed type, and every leaf resolves to an instance. Any row may serve as a decomposition root for recursive decomposition.
- **Naming Guidelines:**
  * **Naming:** Name every instance node in Title Case.
  * **Composite Instance Naming**: Name an ensemble — a set, a practice, a domain, or a construction corpus — with the suffix Set (Epistemic Element Set, Drug Modelling Set), etc.
* **Description:** Describe what the instance is, what role it plays, or why it is included in the decomposition. A grouping row says what the group holds and by which principle it is grouped; repeating the path is not a description. Descriptions clarify the instance but do not substitute for explicit relationship labels.

| Instance Tree Path | Description |
| --- | --- |
|  |  |


## QA

### Why is this note relevant?

> To reflect on and create a guide involving ontology and epistemology, with the goal of clarifying the target of study.

### Do I need a Theory of Modelling? Or should that theory emerge from ontology and epistemology?

> For now, the node of modeling is only a placeholder — for a theory of epistemology and ontology.

### What is the relationship between Ontology and Epistemology?

> They are mutually constraining duals of the same epistemic act: ontology constrains what can be known; epistemology constrains how the known is accessed and represented.

### Why use formal artifacts instead of relying on mental representations?

> To discipline our thinking.

| **Purpose** | **Description** |
| --- | --- |
| **Prediction** | Forecast behavior or outcomes under different conditions. |
| **Explanation** | Explain underlying mechanisms leading to observed phenomena. |
| **Design** | Design or optimize systems for specific purposes. |
| **Evaluation** | Assess performance and effectiveness. |
| **Exploration** | Explore complex systems difficult to study directly. |
| **Communication** | Communicate complex ideas understandably. |

### How do we figure out how nature works in practice?

> Not by looking randomly at isolated aspects, nor by relying uncritically on derived artifacts such as mathematical formalisms that represent a system only indirectly. Instead: ground inquiry in experiments, attend to deviations from current theory, and focus on unexplained processes, phenomena, or event streams — using discrepancies to locate gaps in understanding.

### Which aspects of reality are worth describing?

> Those exhibiting recurring patterns that enable explanation, prediction, intervention, or compression of experience — e.g. motion, mass, force, opportunity cost, trade-offs, Production–Possibility Frontier. **(Reader: notice the recursion here.)**

> Two different kinds of artifacts compress reality, and they must not be confused:
>
> - **Fundamental descriptive artifacts (concepts/aspects)** — concepts directly describing recurring structures of reality, enabling compression; meaningful standalone (motion, mass, force, opportunity cost). These identify **what** is described.
> - **Epistemic scaffolding tools** — frameworks supporting construction, organization, and reasoning about descriptions (numbers, geometry, logic, probability, calculus, graphs). These provide **how** descriptions are represented and manipulated.

### What is an epistemic act?

> Any primitive act performed by an observer to construct, transform, evaluate, or apply knowledge about reality. `Epistemic Act` is the doing root; `Inference`, `Observation`, `Measurement`, `Classification`, `Computation`, and `Comparison` are its kinds, with `Deduction` a kind of inference.

### What is an epistemic activity?

> A situated bundle of inquiry doings that applies one or more methods — a field season, a modelling run, a proof campaign, a classification batch. The bundle is the unit: which methods were run, which acts were performed together, in which sitting, toward what joint result. Activity is neither a synonym for the practice nor a synonym for the act; it carries the situated side that a method, being general, cannot.

### What is an `Epistemic Method`?

> A generalized routine a class of activities runs: the reproducible order of acts that a competent agent can be taught and can decompose into sub-methods. It is general where the activity is situated — the same method run in two sittings is one method and two activities. A method prescribes acts but never contains them: the acts belong to the activity that performs them (see "How is the method that prescribes an act recorded?").

### What is the relation between `Epistemic Practice`, `Epistemic Activity`, `Epistemic Method`, and `Epistemic Act`?

> **Four levels of one doing.** `Epistemic Practice` is the whole that recurs and endures — activities, methods, acts, roles, standards, instruments, and notations, together with the lanes that carry them; it is what a discipline, laboratory, school, or specialty *is*. `Epistemic Activity` is one situated exercising of it — the bundle in time, which applies a method or several. `Epistemic Method` is the generalized routine a class of activities runs, applied through primitive acts. `Epistemic Act` is the granular act itself. Practice answers *what is carried on*; activity answers *what is happening now*; method answers *how it is done*; act answers *what is being done*. Every activity belongs to a practice, every activity applies a method, and every activity performs the acts its method prescribes. That prescription is metadata, not a link: which method lays an act down is recorded on the act's node, while the path shows the activity that performed it.

### How is the method that prescribes an act recorded?

> As node metadata on the act, not as a link. There is no `Prescribes` link form and no `Method (→ Part) Act`: an act is composed into the activity that performs it, while which method lays it down and which sitting executes it are attributes of the act's node. Keeping the prescription out of the path keeps one tree per doing — the activity shows what was performed together, the method shows what is teachable, and the act's metadata ties the two without growing a second branch.

### Do we need `Epistemic Activity` as an epistemic element in the decomposition?

> **Yes — the earlier answer of no is reversed.** A fully specified practice names its methods and acts, but leaves unsaid which of them were performed together, in which sitting, toward what joint result: the bundle is load-bearing. Socialium reached the same conclusion and retired `Practice` in favour of `Activity` (see "Do we actually need `Activity` and `Practice`?" there); epistemicarum keeps `Practice` because here the whole is a doing rather than an organization of actors, and adds `Activity` as the bundle inside it. The retired answer is kept as the history of the decision.

### What is the difference between standing and situated orientation?

> Two scopes, one lane. **Standing orientation** is what the practice is constituted to answer — its purpose, the questions that define the field, the open problems it institutionally maintains; it outlives any agent and any sitting, and `Epistemic Practice (→ Has) Epistemic Orientation` carries it. **Situated orientation** is the question a particular activity poses and the gap it is set against — "what is seven times eight, as yet uncomputed"; it is answered or abandoned when the sitting ends, and `Epistemic Activity (→ Has) Epistemic Orientation` carries it. The same lane type serves both because both are why-directed; the owner decides the scope. Filing a situated question on the practice makes it look permanent, which is why the Arithmetic case keeps its purpose at the practice and its question and gap at the sitting.

### Why is `Epistemic Role` an agency element?

> Because a role is a position an agent occupies, not a direction inquiry takes. Purpose, question, goal, and gap answer *why*; a role answers *who* — which agent stands where in the practice. Socialium files roles under the collective and moralis under the agent's office, so `Epistemic Agency (→ Has) Epistemic Role` is the matching home; leaving it in Orientation let the "why" lane carry an element that does not direct anything.

### Where does the ontic reading of a segment grow?

> In the naturalis or social grammar, and never here. The epistemica tree names the segment a practice addresses and stops: decomposing the segment into physical or social types would mix the inquiry with its target, and would have to be redone for every reading of the same segment. This guide licenses no link form for the ontic reading — the segment is named here and the tree that types it belongs to another note. A segment read both ways — a fishery as ecosystem and as market — gets one tree per reading, never two types on one row.

### Why is there no `Epistemic Domain`?

> Because it was the `Addresses` relation reified. Its description named a field — "field, sub-field, family, or specialty" — while its children were the target: the segment, its observables, and the lens. Its whole content was therefore the join of two types that already exist. Its sub-fields are member practices; its segment is what the practice addresses; its observables are what the practice registers; its framework is the lens the practice reasons with; and its `Has`-branch back to a practice was the inverse of `Addresses`, asserting nothing further. `Domain` survives only as ordinary English — the DESA is still built about a domain.

### What is an `Epistemic Framework`?

> A group of epistemic elements read together as one lens: a family of methods, the tools that run them, and the constructs they produce, taken as a single way of modelling — Monte Carlo methods read as one approach rather than as a list of techniques. It is a kind of `Epistemic Element Set`, which leaves the guide with two aggregates: the doing (`Epistemic Practice`) and the lens (`Epistemic Framework`). It is had by the practice, never by the target, and it directs nothing: socialium's `Framework` declares a course of action and sits under `Action Guidance`, whereas this one collects elements, which is why `Epistemic Guidance` here holds only principle, protocol, and methodology.

### How does `Segment of Reality` differ from `Observable`?

> The segment is the bounded portion of reality itself; an observable is a feature of that portion which can be registered. A fishery is a segment; its stock size is an observable. The segment is held once per reading of reality; observables multiply within the reading.

### Why is there no `Epistemic Task`?

> Because the two jobs a task did are already carried. The planned unit of work is the `Epistemic Method`; the allocation of work across agents is `Epistemic Organization (→ Has) Epistemic Division of Labour`. A third type standing between the activity and its method only restated, in weaker terms, what the method already is.

### Why is there no `Epistemic Procedure`?

> Because `Method` and `Procedure` were one distinction seen from two sides — general versus situated — and the situated side is the `Epistemic Activity`. Once activity is defined as the bundle that *applies* a method, "the same method, run here and there" is two activities sharing a method, and no procedure type is needed. What a procedure nested — steps and sub-routines — the method nests as sub-methods.

### Why does `Property` return as a predication type?

> Because the retirement answered a different question than the one a decomposition asks. `Observable` names a feature of a **segment of reality**, registered through an interface; `Epistemic Criterion` names the property a **judgment** turns on. Neither can carry a predicate that a construction asserts of its own instances — that a number is even, that a shape is convex, that a model is linear — because such a predicate is asserted by the grammar that carries the element, not measured off a segment and not used to judge an artifact. The three positions are disjoint:

| Type | What it names | Side |
| --- | --- | --- |
| `Observable` | A feature of a segment of reality, registered through an interface. | Ontic / access |
| `Epistemic Criterion` | The property a judgment turns on. | Evaluation |
| `Property` | A predicate asserted of an element by the grammar that carries it. | Predication |

> The type takes its own link, `Epistemic Element (→ Has Property) Property`, and `Has` was narrowed to elements and features so that the two labels do not overlap. A property binds to its instances — `Evenness`, `Convexity`, `Complexity` — and may be had by any element the table licenses, not only by a construction.

> The retired answer is kept as the history of the decision: `Property` was refused while it only restated the observable under a weaker name. It returns because a construction's own predicates had no home at all — the gap was real, and the reinstated type fills it rather than renaming what `Observable` already carried.

### Why is `Epistemic Blueprint` no longer a type?

> Because it named the encoding format of a construction, which `Representational System` already names, and the rules that constitute that format are the `Constitutive Substrate`'s own parts. The row had no decomposition of its own and never appeared in a tree; a construction now reaches its sign system by `Epistemic Construction (→ Has) Representational System`.

### Is multiplication an `Epistemic Act`, an `Epistemic Method`, or a constituent of the representation?

> A constituent of the representation, and that settles the other two by exclusion. An operation specifies a result, never an order of acts; `Computation` is "a rule-governed transformation of represented content", so it rewrites inscriptions and never reaches a bare quantity, and the rule licensing the rewrite is what the operation *is*. `Multiplication` therefore lives as a `Transformation Rule` — not as an `Epistemic Act` (the act is the `Computation` that fires the rule) and not as an `Epistemic Method` (a method is "the reproducible order of acts"; multiplication fixes no order, which is why `Shift-And-Add Multiplication`, `Lattice Multiplication`, and `Russian Peasant Multiplication` are methods and multiplication is not). It is not an `Epistemic Activity` either: two multiplications are two sittings and one rule.

> The layers must not be collapsed. The `Operator Glyph` `×` is inert — it marks which rule fires and is itself never transformed; the expression `7 × 8` is what the act rewrites; the rule licenses the rewrite; the `Interpretation` ties glyphs to quantities. Computation is syntactic throughout, which is why pupil, abacus, and machine execute one rule without any of them reaching a quantity directly.

> The test is in the Arithmetic case below: remove the `Multiplication Rule` and the system loses products while `Presburger Arithmetic` stays complete and decidable — a change in what the notation can express, not in what anyone does. `Deductive Inference Rule`, still carried as a bare substrate part in [Baruch Spinoza](/view.html?p=notes/social/collective/actor/private/persona/baruch-spinoza.md), is the same kind of element; no new link form was needed to admit it, since `Constitutive Substrate (→ Part) <<Constitutive Element>>` already carries it and the slot's expansions alone grew.

### How is a type retired?

> In one change set, in five steps: remove every `Permitted Link Form` row that names it; retype the trees that used it, so no orphan grouping segment survives; add a QA answer naming the retired type, what it meant, and where its work now lives; leave the name out of the vocabulary, since a grouping segment must be a licensed type; and never reuse the name for a new meaning. The guide carries its own history this way — `Epistemic Task`, `Epistemic Procedure`, `Epistemic Operation`, `Epistemic Action`, and `Epistemic Blueprint` are all retired by this procedure. `Property` was retired and later reinstated as a predication type (see "Why does `Property` return as a predication type?"); that is not a reuse of the retired meaning — the retired row named an element of a tree, the reinstated type names a predicate a tree asserts.

### Where do guidance and organization decompose?

> As lanes of the practice: `Epistemic Practice (→ Has) Epistemic Guidance` and `Epistemic Practice (→ Has) Epistemic Organization`. Guidance holds the directives that orient inquiry without being an end (`Epistemic Orientation`) or a norm of judgment (`Epistemic Evaluation`) — principle, protocol, methodology. Organization holds the arrangements that coordinate inquiry work rather than describe it — programme, project, workflow, schedule, division of labour. Neither is a `Has`-branch of `Epistemic Act`: socialium attaches guidance, organization, and instrumentation to the `Interaction Unit` because that grammar roots on actors, while this one roots on doings, so the practice owns them. Instrumentation needs no lane here — `Epistemic Tool` and `Observation Interface` already carry it.

### Why is `Organization` no longer a kind of `Epistemic Act`?

> Because an arrangement is not an act. The retired row `Organization (→ Kind) Principle` typed a rule as an arrangement and an arrangement as an act, twice over. A principle is a directive and now sits under `Epistemic Guidance`; the reproducible structure of acts that "arrangement of actions" once named is the `Epistemic Method`'s own decomposition; and the arrangement of inquiry work across agents and time is the `Epistemic Organization` lane.

### Why is `Epistemic Operation` now `Epistemic Act`?

> Two collapses, in sequence. `Operation` and `Action` named one thing at two levels — `Epistemic Operation (→ Kind) Action` — and `Action` and `Act` then named it again — `Epistemic Action (→ Kind) Act`. Each was a distinction without a difference. `Act` is the element, `Activity` the bundle, `Method` the routine, `Practice` the whole; `Operation` and `Action` survive only as ordinary English.

### What is a description?

> A structured affirmation about a segment of reality, carried by an epistemic construction.

### What is an explanation?

> A very special form of description — maybe the ultimate form — clarifying cause, mechanism, or relation.

### How do we validate our descriptions of reality?

> By testing the construction against reality: prediction error, replication, and failed or successful intervention.

### Which aspects of reality result from multiplicative interaction?

> **Interaction-derived quantities** are ontic aspects quantifying the **joint state** of two or more independent ontic variables: momentum, kinetic energy, angular momentum, gravitational force, heat, revenue, cost, wage bill, information gain.

### Which area of reality is best suited for studying in order to improve my epistemic practice?

> Physics is a training ground for rigorous modeling because it enforces precise, testable, and feedback-rich representations of reality. The value lies in transferring this epistemic discipline — rather than its specific models — into more complex domains like social systems.

### Which relationship types can be used to explicitly label the → operator?

| Category | Type | Description | Link Case for |
|---|---|---|---|
| Classification | `Kind` | Establishes a taxonomic relationship in which the child specifies what kind of element the parent is. | Classifying an element under a more specific type. |
| Composition | `Part` | Identifies a constituent that forms part of the parent element. | Decomposing a system, structure, or aggregate into its constituent elements. |
| Composition | `Member` | Identifies an element belonging to a set or aggregate, without asserting that it forms part of another element. | Disaggregating an aggregate — an `Epistemic Element Set`, a practice, a framework. |
| Composition | `Has` | Identifies an element or feature belonging to or associated with the parent. | Identifying components, attributes, or associated elements. |
| Predication | `Has Property` | Identifies a predicated feature the parent element carries or lacks — asserted of the element, not registered from it. | Asserting a characteristic of any element: a number is even, a shape is convex, a model is linear, a tool is deterministic. |
| Composition | `Instance` | Identifies a realization of a generalized type: a situated occurrence, a particular artifact, an exemplar notation, or a tool. | Connecting a type to what realizes it — a method to the activity that applies it, a system to the notation that embodies it. |
| Composition | `Addresses` | Identifies the domain a practice works on. | Connecting an `Epistemic Practice` to the cut it targets. |
| Composition | `Produces` | Identifies the construction a practice or act leaves behind. | Connecting an `Epistemic Practice` to its constructions. |
| Constitution | `Constituted By` | Identifies the elements, rules, or structures that constitute the identity or organization of the parent. | Decomposing a representational or conceptual system into its constitutive foundations. |
| Derivation | `Derived From` | Identifies the source from which an element is obtained or derived. | Identifying the premises, data, or elements from which another element originates. |
| Transformation | `Transforms` | Identifies an element that is transformed or produced through an act performed by the parent. | Representing transformations between input and output elements. |
| Representation | `Represents` | Identifies the reality, entity, or content represented by the parent. | Connecting a representation to its referent or represented target. |
| Causation | `Causes` | Identifies an element whose act or occurrence produces an effect in another element. | Representing causal relationships between phenomena or processes. |
| Regulation | `Regulates` | Identifies an element that controls, constrains, or modulates the behavior of another element. | Representing regulatory relationships and feedback structures. |
| Regulation | `Governed By` | Identifies the standard, rule, or normative framework an element is regulated by. | Connecting a construction or an act to the standard it must satisfy. |
| Evaluation | `Evaluated By` | Identifies the evaluation, verification, or validation applied to an element. | Connecting a construction or an act to the check that discharges doubt about it. |
| Dependence | `Depends On` | Identifies an element whose existence, behavior, or operation depends on another element. | Representing structural, functional, or operational dependencies. |
| Association | `Related To` | Establishes an association between elements when no more specific relationship applies. | Representing a relevant relationship that cannot be classified more specifically. |
| General | `Unspecified` | Establishes a relationship between two elements when the nature of their connection is relevant but has not yet been identified or classified. | Representing a known or suspected connection whose specific relationship type remains undetermined. |

> **Properties of the relationship types.** `Kind`, `Part`, `Depends On`, and `Derived From` are transitive; `Member` and `Instance` are not — a member of a member is not a member, and an instance of an instance is not an instance. No pair in this table is declared inverse: `Addresses` is asserted one way only, from practice to segment, and the realization relation carries one label, `Instance`, because a path runs from type to instance and never back. `Represents`, `Produces`, `Transforms`, `Causes`, `Regulates`, `Has Property`, `Governed By`, and `Evaluated By` are irreflexive; `Governed By` and `Evaluated By` are not transitive. No label is symmetric. `Related To` and `Unspecified` assert no properties at all; use them only when a more determinate label cannot be established.


### (Case Study) What is the recursively decomposed instance tree of Arithmetic?

> Worked decomposition of arithmetic as an organized inquiry system, grown from the epistemic-act definition above to full intermediate detail. 

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic | The organized inquiry whole of discrete quantity, read as the practice of exact reckoning and the segment it addresses. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` | Grouping: orientation of arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Purpose` | Grouping: purposes of the inquiry. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Purpose` (→ Instance) Exact Reckoning Purpose | Telos: determine exact discrete quantity — count, sum, product, quotient — leaving no remainder of doubt. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` | Grouping: agencies of arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Agent` | Grouping: agents performing reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Agent` (→ Instance) Reckoner | Entity counting, calculating, and proving; pupils, clerks, and mathematicians realize this agent. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Agent` (→ Kind) `Epistemic Collective` | Grouping: the bodies that carry reckoning jointly. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Agent` (→ Kind) `Epistemic Collective` (→ Instance) Schoolroom Reckoning Corps | The masters and pupils who carry arithmetic together, each accountable to the others for a count. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Agent` (→ Kind) `Epistemic Collective` (→ Instance) Schoolroom Reckoning Corps (→ Member) `Epistemic Agent` (→ Instance) Reckoner | The individual reckoner as a member of the corps. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Role` | Grouping: the positions agents occupy in the practice. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Agency` (→ Has) `Epistemic Role` (→ Instance) Recitation Master | Position charged with hearing recitations and correcting them. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Addresses) `Segment of Reality` | Grouping: the bounded portion of reality arithmetic addresses — collections of distinct items. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Addresses) `Segment of Reality` (→ Instance) Discrete Multitude | The segment itself: countable collections — heads of a flock, coins in a purse, days in a month. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Observable` | Grouping: features of the segment registrable for reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Observable` (→ Instance) Cardinality | The registrable feature: how many, independent of what is counted. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` | Grouping: the access regime through which multitude is registered. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` (→ Has) `Observation Interface` | Grouping: interfaces coupling multitude to count. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` (→ Has) `Observation Interface` (→ Instance) Tally Stick | Notched stick coupling a flock to the reckoner's count, one notch per head. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` (→ Has) `Observation Encoding` | Grouping: encodings of the count. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Access` (→ Has) `Observation Encoding` (→ Instance) Five-Bar Tally Encoding | Strokes grouped in fives for reading at a glance. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` | Grouping: representations of number. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` | Grouping: sign systems of arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System | Signs with place rules forming numerals; notations realize this system. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Instance) Hindu-Arabic Numerals | Exemplar notation realizing the system: place-valued decimal digits. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Instance) Roman Numerals | Exemplar notation realizing the system: additive letter signs. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` | Grouping: combinable constituents. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Decimal Digit | One of 0–9 combining into numerals. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Operator Glyph | `+ − × ÷ =` combining numerals into equations. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Forty-Two | The numeral token `42` denoting forty-two. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Representation Element` (→ Instance) Product Equation | The equation expression `7 × 8 = 56` as a checkable artifact. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` | Grouping: rules and structures constituting the system. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Convention` | Grouping: stabilized notational choices. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Decimal Convention | Ten symbols including zero; positions weigh powers. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Formation` | Grouping: rules of well-formed combination. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Numeral Formation Rule | How digits compose into well-formed numerals. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Successor | Next-after relation generating the number series. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` | Grouping: rules licensing the rewrite of well-formed expressions — the operations. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Addition Rule | Rewrite licence: `a + 0 ↦ a` and `a + S(b) ↦ S(a + b)`; the operation `Addition` exists as this licence, never as an act or a routine. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Multiplication Rule | Rewrite licence: `a × 0 ↦ 0` and `a × S(b) ↦ (a × b) + a`; the rule `Presburger Arithmetic` lacks, and the operation `Multiplication` lives nowhere else. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: axioms and foundings. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Addition Definition | Superseded by `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Addition Rule: addition recursed from successor is the operation itself, and an operation is a rewrite licence rather than a founding axiom. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) First-Order Arithmetic | Axiom system underlying formal reckoning: zero, successor, induction; axiom systems realize these axioms. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) First-Order Arithmetic (→ Instance) Peano Arithmetic | Exemplar axiom system realizing these axioms: induction over all predicates. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) First-Order Arithmetic (→ Instance) Presburger Arithmetic | Exemplar axiom system without multiplication: complete and decidable. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` | Grouping: meaning assignments. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Numeral System (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Decimal Place Encoding | Number → numeral mapping under decimal place value. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` | Grouping: the situated bundles of reckoning work. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Tally Session | One counting sitting in which a flock is tallied stroke by stroke. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Tally Session (→ Has) `Epistemic Method` (→ Instance) Tallykeeping Method | Generalized routine recording one stroke per item counted. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Tally Session (→ Part) `Epistemic Act` | Grouping: the primitive acts the sitting performs. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Tally Session (→ Part) `Epistemic Act` (→ Instance) Tallying Act | Primitive act marking one stroke per item counted. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session | One sitting in which a column addition is worked through. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Has) `Epistemic Method` (→ Instance) Column Arithmetic Method | Generalized method adding place-ordered numerals from the units column upward. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Has) `Epistemic Method` (→ Instance) Column Arithmetic Method (→ Part) `Epistemic Method` (→ Instance) Carry Step | Ten-for-one regrouping moving excess to the next place. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Has) `Epistemic Method` (→ Instance) Shift-And-Add Multiplication | Generalized routine reducing products to shifted additions. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Part) `Epistemic Act` (→ Kind) `Computation` (→ Instance) Reckoning | Rule-governed transformation of represented quantities. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Part) `Epistemic Act` (→ Kind) `Comparison` (→ Instance) Magnitude Comparison | Act judging greater, lesser, or equal between numerals. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Has) `Epistemic Orientation` | Grouping: the orientation the sitting poses for itself. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Question` | Grouping: the question the sitting directs reckoning toward. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Question` (→ Instance) Uncomputed Product | Formulated question directing reckoning toward the gap: what is seven times eight, as yet uncomputed. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Gap` | Grouping: the deficiency the sitting is set against. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Column Sum Session (→ Has) `Epistemic Orientation` (→ Has) `Epistemic Gap` (→ Instance) Missing Product Gap | Deficiency in available reckoning: the product not yet known, represented, or warranted. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Proof Campaign | A season of proofs carried out on the stated axioms. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Proof Campaign (→ Has) `Epistemic Method` (→ Instance) Proving Method | Generalized derivation of arithmetical propositions from stated axioms. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Proof Campaign (→ Has) `Epistemic Method` (→ Instance) Calculating Method | Generalized sequence of calculational acts toward exact reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Proof Campaign (→ Part) `Epistemic Act` (→ Kind) `Inference` | Grouping: derivations from premises. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Proof Campaign (→ Part) `Epistemic Act` (→ Kind) `Inference` (→ Kind) `Deduction` | Grouping: necessary derivations. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Activity` (→ Instance) Proof Campaign (→ Part) `Epistemic Act` (→ Kind) `Inference` (→ Kind) `Deduction` (→ Instance) Induction Proof | Proof by mathematical induction: base and step deriving the universal claim — deductive in epistemic standing. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Guidance` | Grouping: the directives steering reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Guidance` (→ Has) `Epistemic Principle` | Grouping: general rules guiding reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Guidance` (→ Has) `Epistemic Principle` (→ Instance) Induction Principle | What holds of zero and passes to successors holds of all numbers. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Guidance` (→ Has) `Epistemic Principle` (→ Instance) Commutativity Principle | Order-independence of addition and multiplication. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Organization` | Grouping: arrangements coordinating reckoning work. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Organization` (→ Has) `Epistemic Schedule` | Grouping: arrangements of reckoning work in time. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Organization` (→ Has) `Epistemic Schedule` (→ Instance) Recitation Rota | Rotation assigning pupils to recitation turns. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` | Grouping: the constructions arithmetic produces about discrete quantity — what the DESA does not leave unrecorded. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Number | A concept: the constructed discriminator of discrete multitude, order, and ratio — what the numerals denote. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Zero | A concept: the empty count constituted as a number, the addend that leaves every sum unchanged. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Kind) `Concept` (→ Instance) Number (→ Has Property) `Property` (→ Instance) Evenness | A property: the predicate a number carries when it divides into two exact halves. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Kind) `Description` (→ Instance) Sum Statement | A description: seven times eight are fifty-six, carried as a claim about the segment. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Kind) `Dataset` (→ Instance) Multiplication Table | A dataset: products indexed by factor, consulted instead of recomputed. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Produces) `Epistemic Construction` (→ Kind) `Explanation` (→ Instance) Carrying Explanation | An explanation: why regrouping ten ones into one ten preserves the sum. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` | Grouping: assessments of reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` | Grouping: standards judging arithmetic. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` (→ Instance) Correctness Standard | A computation stands only if independent recomputation agrees. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` (→ Instance) Proof Validity Standard | A proof stands only if each step follows by stated rule. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Standard` (→ Instance) Place-Value Standard | A numeral stands only if each place weighs its power of ten. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Criterion` | Grouping: evaluated properties. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Criterion` (→ Instance) Exactness Criterion | The result is exact or it is wrong; approximation has no standing here. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Constraint` | Grouping: limits on reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Constraint` (→ Instance) Working Memory Limit | Only so many partial products are held at once; the column relieves memory. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Error` | Grouping: deviations from the true value. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Error` (→ Instance) Dropped-Carry Error | Off-by-ten slip losing a carry, rendering seven times eight as fifty-four. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Validation` | Grouping: checks discharging doubt. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Validation` (→ Instance) Inverse Check | Division undoing multiplication to validate the product. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Validation` (→ Instance) Casting Out Nines | Modular-nine checksum validating long reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Feedback` | Grouping: evaluations returned to reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Evaluation` (→ Has) `Epistemic Feedback` (→ Instance) Recount After Mismatch | Recomputation ordered by a failed check. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` | Grouping: transmission of reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Inscription` | Grouping: persistent renderings. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Inscription` (→ Instance) Chalkboard Sum | Worked reckoning kept on the board for checking. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Publication` | Grouping: published reckonings. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Publication` (→ Instance) Reckoning Primer | Printed tables and rules teaching reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Communication` (→ Has) `Epistemic Publication` (→ Instance) Reckoning Primer (→ Instance) Liber Abaci | Exemplar primer realizing the genre: Fibonacci's 1202 transmission of place-valued reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` | Grouping: structures enabling reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Tool` | Grouping: tools of the reckoner. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Tool` (→ Instance) Calculator | Device performing calculation for the reckoner. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Tool` (→ Instance) Calculator (→ Instance) Abacus | Exemplar calculator realizing the tool: place-valued beads. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Information Repository` | Grouping: stored reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Information Repository` (→ Instance) Table Book | Bound addition and multiplication tables consulted instead of recomputed. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Institution` | Grouping: bodies sustaining reckoning. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Infrastructure` (→ Has) `Epistemic Institution` (→ Instance) Schoolroom | Instruction drilling reckoning across generations. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Context` | Grouping: the surrounding conditions under which reckoning is situated. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Context` (→ Has) `Epistemic Condition` | Grouping: the conditions under which reckoning is carried on. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Context` (→ Has) `Epistemic Condition` (→ Instance) Oral Transmission Condition | Reckoning must be held in memory and recited: no external store is assumed. |
| `Epistemic Element` (→ Kind) `Epistemic Element Set` (→ Kind) `Epistemic Practice` (→ Instance) Arithmetic (→ Has) `Epistemic Context` (→ Has) `Epistemic Condition` (→ Instance) Exactness Demand Condition | Exchange and accounting admit no approximation: a wrong count is a loss, not an estimate. |

### What Is a critical conceptual evaluation of `Epistemic Element`?

> Evaluated is the definition, not its use: "An `Epistemic Element` is anything that occupies a role in the practice by which reality is made intelligible — the reality cut as a target, the practice that investigates it, the constructions it produces, or what enables, constrains, evaluates, communicates, or conditions that practice. An element qualifies when its absence, substitution, or alteration changes what inquiry can reach, produce, or warrant; what passes no such test lies outside the category. Epistemic elements are typed as kinds of the Epistemic Order and, when composite, decompose into further epistemic elements through explicitly typed relationships."

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Specification** | | |
| Conceptual Identification | High | **Identity:** the differentia is stated — "occupies a role in the practice by which reality is made intelligible" — and the role list (target cut, practice, construction, enabling, constraining, evaluating, communicating, conditioning element) marks the category off from `Segment of Reality`, `Epistemic Practice`, and `Epistemic Framework`, which are positions inside it. |
| Definitional Clarity | Moderate–High | **Intelligibility:** the definiens is explicit and non-circular; the residual vagueness sits in "made intelligible" and "can reach, produce, or warrant", both of which require the inquiry to be named. |
| Conceptual Determinacy | Moderate–High | **Boundary rules:** the removal test decides borderline cases — a notation that changes what can be warranted is in, a set of data that changes what can be predicted is in, a distant fact no inquiry reaches is refused. |
| Definitional Completeness | Moderate–High | **Constitutive conditions:** membership condition, role list, test, exclusion principle, typing, and decomposition are all stated; an exhaustive list of exclusions is not. |
| Internal Consistency | High | **Logical integrity:** membership does not run through the type system; typing only classifies what the role test has already admitted, and decomposability follows membership instead of establishing it. |
| Structural Coherence | High | **Internal organization:** one criterion (role), one test (change on removal), two consequences (typing and decomposition), stated in that order, with no competing register. |
| Conceptual Tractability | High | **Evaluability:** name the inquiry, place the element in a role, test whether it changes anything; then type and decompose. |
| **Representational Adequacy** | | |
| Extensional Fidelity | Moderate–High | **Classification accuracy:** identical elements are admitted or refused by the role test; the extension of the kinds remains bound to the reference table. |
| Intensional Adequacy | High | **Defining properties:** the inquiry and the role positions are the stated defining properties, not a proxy for them. |
| Ontological Adequacy | High | **Kind of entity:** it defines elements; the category/instance distinction is carried explicitly, and an ontic segment enters only as the target role, never as a second category. |
| Discriminative Power | Moderate–High | **Relevant distinctions:** separates target cut, doing, lens, construction, and ontic segment — roles the earlier wording merged into "epistemic content". |
| Granularity Adequacy | High | **Level of abstraction:** role membership is level-free, and recursion fixes granularity per purpose. |
| Empirical Adequacy | Moderate | **Evidence:** the removal test is checkable case by case, though the definition itself is analytic rather than empirical. |
| Representational Coverage | High | **Domain coverage:** the role positions cover practices, activities, methods, acts, constructions, interfaces, standards, constraints, feedback, infrastructure, and the segments they address. |
| **Conceptual Economy** | | |
| Ontological Parsimony | Moderate–High | **Structural economy:** one criterion, one test, two consequences in a single sentence — at the cost of a longer definiens than the loose original. |
| Conceptual Distinctiveness | High | **Unique contribution:** role-plus-test is not the vocabulary of the neighbouring philosophiae. |
| Redundancy Control | High | **Conceptual overlap:** domain, practice, and framework are disjoint wholes, so the membership test does not repeat the typing rules; typing and decomposability each do one job. |
| Boundary Differentiation | Moderate–High | **Separation from neighbours:** domain, practice, framework, construction, and ontic segment are marked by role position rather than by table entry alone. |
| **Epistemic Performance** | | |
| Epistemic Leverage | High | **Analytical yield:** admission becomes a decision that can be made and audited before any typing or decomposition begins. |
| Inferential Productivity | Moderate | **Reasoning capacity:** it supports role-based inference — if a construction represents a segment, the access, standards, and practice that produced it exist — beyond the trivial "decomposes into epistemic elements". |
| Explanatory Power | Moderate | **Explanatory contribution:** it says why an element is epistemic: what can be understood or warranted changes without it. |
| Predictive Utility | Low–Moderate | **Anticipatory capacity:** it predicts role-mates, not behaviour. |
| Information Compression | Moderate | **Representational efficiency:** the admission rule is compressed into one sentence, longer than the loose original but usable. |
| Problem-Solving Utility | High | **Practical contribution:** admission and decomposition are both checkable operations. |
| **Integration and Generality** | | |
| Contextual Robustness | High | **Contextual stability:** no knower or experience clause; the definition holds where inquiry is distributed, institutional, or non-human. |
| Combinatorial Fluidity | Moderate–High | **System integration:** a role in one inquiry types cleanly into the shared link grammar; composition still depends on the reference table. |
| Relational Compatibility | Moderate | **Compatibility:** compatible across the epistemic, ontic, and social orders by re-reading an element under a role, though relation vocabulary remains unshared. |
| Cross-Domain Portability | High | **Domain transfer:** role-in-inquiry travels across domains without reformulation. |
| Scale Invariance | High | **Scale transfer:** roles apply at every scale, and composites recurse. |
| Temporal Stability | Moderate | **Historical continuity:** "made intelligible" is epoch-relative; what counts as an epistemic problem is historically redefined. |
| **Operational and Methodological Validity** | | |
| Operationalizability | High | **Procedural applicability:** name the inquiry, assign the role, test removal — then type and decompose. |
| Measurement Validity | Not applicable | **Construct representation:** no measurement is intended at the category level; measures sit beneath it as `Epistemic Standard` and `Epistemic Criterion`. |
| Reliability | Moderate–High | **Repeatability:** the test narrows divergence to what the inquiry is taken to be. |
| Inter-Subjective Reproducibility | Moderate | **Agreement:** clear cases converge; a contested purpose still needs a user question, which the guide already requires for ambiguous roots. |
| Falsifiability or Refutability | Moderate | **Exposure to criticism:** the test can fail — an element whose removal changes nothing is refused. |
| Sensitivity to Evidence | Moderate–High | **Revisability:** evidence about an inquiry can reclassify an element, or expose a missing role. |
| **Normative and Strategic Adequacy** | | |
| Purpose Adequacy | High | **Functional fit:** fit for admission, typing, and decomposition in one instrument. |
| Normative Justification | Not applicable | **Value justification:** no values are embedded; prescriptions enter through `Epistemic Standard` and the normative philosophia. |
| Strategic Effectiveness | High | **Intervention utility:** the role positions map onto the circuit questions (why, who, what, how accessed, what is done, what is produced, how judged, under what conditions, what supports it). |
| Performative Effects | Moderate | **Effects of classification:** admission still reorganises how an inquiry is taught, funded, and governed, now with a test behind it. |
| Misuse Resistance | Moderate | **Resistance to abuse:** the role test blocks mere relabelling, though "intelligible" can still be stretched by a determined user. |

### Which note schema used - in order to document an epistemic element?

```bash
# (Epistemic Element)

> (Intro)

## Formulation

### What is this epistemic instance?
### What epistemic element type does this epistemic instance belong to?
### Is the type of this `epistemic element instance` ambiguous?
### What is the recursive instance decomposition of this epistemic instance?
### What Is a critical conceptual evaluation of this `epistemic element instance`?

## References

- ...
```

## References

- [Philosophia Naturalis](https://app.notion.com/p/Philosophia-Naturalis-32ac0f5171ec807b9388c870ab664abf?source=copy_link)
- [Philosophia Artium Technicarum et Operis](/view.html?p=notes/meta/philosophia-artium-technicarum-et-operis.md)
- [Concept](/view.html?p=notes/technica/general/cto/concept.md)
- Reality (no dedicated note yet — see the Formulation question above)
- Ontology (no dedicated note yet — see the Formulation question above)
- Observer (no dedicated note yet)
- Nature (no dedicated note yet)
- https://en.wikipedia.org/wiki/Reality
- Schopenhauer, A. (2016). The World as Will and Representation, Volume 1.
- Unger, R. M. (2024). The world and us. Verso Books.
- Lange, F. A. (1865). History of Materialism and Criticism of Its Present Importance. Leipzig: Verlag von Duncker & Humblot.
- Feynman, R. P. (1963). The Feynman lectures on physics. 1, 46.
- Landau, L. D., & Lifshitz, E. M. (2013). Course of Theoretical Physics. Elsevier.
- https://www.youtube.com/watch?v=X4PdPnQuwjY&t=19s
- A Guide to Reading
- System
- Energy
- Epistemic Artifact
- Philosophy
- Modelling
