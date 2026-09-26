# Philosophia Artium Technicarum et Operis

> In this note, we will analyze the concept of purposeful (agentic) operation and its primary driver —  technique.

> This note seeks to systematize a philosophy of technique and operation that can serve as a conceptual foundation for organizing the ideas used to explain operation and praxis across diverse fields and tasks.

> It’s the complement of Philosophia Naturalis.

## Formulation

### What is the nature of the `technique`?

> Technique is an organized method for achieving a desired transformation through purposeful action.

### What is the role of the `technique` in human experience?

> Technique enables agents to systematically transform, construct, and control aspects of reality to achieve desired states.

### What is a `technical element`?

> It is a concept that denotes an element participating in the technical dimension of change experienced by humans or other purposeful agents. Note: This is a deliberately loose definition of the reality denoted by the concept.

### What grounds `technical practice`?

> Technical practice is grounded in the purposive interaction of agents with reality through knowledge, resources, constraints, and techniques.

> Foundation - **Reality -** The ontological substrate comprising the physical, biological, informational, and social structures that constrain and respond to technical intervention. Steel beam, fluid flow, electric grid, living tissue, user population, software runtime environment.

## How can we characterize the technical aspect of human experience?

> A taxonomy (conceptual structure) that renders the *intervention-oriented* and *fabrication-oriented* practice of agents intelligible.

> **Note:** Different names may be used to refer to generic composites of technical elements, such as *Technical Domain*, *Technical Ecosystem*, *Technical System*, or similar concepts. Each of these terms carries its own specific semantics. For the sake of simplicity and generality, however, we use the term **`Technical Element Set`** as the generic type. The specific semantics are then provided by the particular set itself, rather than being encoded in the generic type. The  only exception to this is the `Technical Practice` which  is a type element set - for the sake of understanding.

> Recursion is introduced by allowing a composite to have another composite as an instance: a `Technical Element Set` may contain `Technical Element Set`s (a CI/CD practice within a DevOps set). Nesting composites in composites is what makes the type tree recursive.

> **Note on relations :** Regarding instance decomposition and the recursive view of the technical element type tree, the relations between elements are not specified in this document and are intentionally left open for now.

> Decomposition lives in the Recursive view below: the specializations of `Technical Element Set` — `Technical Practice`, `Technical Ecosystem`, `Technical Domain` — appear as its subtypes there only.

> Each type with its category, role description, and instances.

### Tabular View

| **Technical Category** | **Technical Element Type** | **Description (Role)** | **Instance(s)** |
| --- | --- | --- | --- |
| **Composite** | Technical Element Set | A collection of technical elements. | Semiconductor manufacturing ecosystem; modern LLM ecosystem |
| **Technical Context** | Technical Problem | Discrepancy between a current or projected state and a desired technical state that calls for intervention. | Reducing query latency below 200 ms under 10× load |
|  | Technical Purpose | Intended ultimate effect or value of the technical endeavor. | Transport passengers; cure an infection; provide real-time financial data |
|  | Technical Constraint | Bound on technical action imposed by reality, resources, regulations, or other conditions. | Material strength; power budget; latency floor; regulatory restriction |
|  | Technical Resource | Input required or consumed by technical activity. | Silicon wafers; electricity; RAM; labor-hours; capital |
| **Requirements & Definition** | Technical Requirement | Formalized desired state, need, or performance objective a solution must satisfy. | 99.99% uptime; <50 dB noise |
|  | Technical Specification | Precise statement of requirements, parameters, performance, and interface conditions used to define and verify a solution. | API response time <200 ms p99; −40°C to +85°C operating range |
|  | Technical Parameter | Variable whose value characterizes or controls a technical object or process. | Voltage; timeout; CPU frequency; thread count; tolerance |
|  | Technical Standard | Normative specification governing form, function, safety, interoperability, or performance. | POSIX; HTTP; ISO standards; electrical codes |
| **Knowledge & Methodology** | Technical Knowledge | Accumulated propositions, models, principles, methods, and know-how used to understand and intervene in technical reality. | Networking knowledge; materials science; operating-system knowledge |
|  | Technical Research | Systematic investigation aimed at discovering technical knowledge, principles, methods, materials, or capabilities. | Novel battery chemistry; new semiconductor process |
|  | Technical Principle | General rule governing construction or operation of technical systems. | Least privilege; redundancy; fail-safe; separation of concerns |
|  | Technical Framework | Overarching logic for structuring technical problems and generating or evaluating solutions. | Systems engineering; TRIZ; control theory; FMEA |
|  | Technical Strategy | Context-sensitive regime for planning, sequencing, prioritizing, and allocating technical work. | Agile; waterfall; prototyping-first; blue-green deployment |
|  | Technical Institution | Durable social structure that organizes, governs, or sustains technical practice and knowledge. | IEEE; FAA; corporate R&D division; standards body |
| **Agents & Competence** | Technical Agent | Entity capable of executing Techniques using tools, resources, and knowledge. | Engineer; robot; compiler; build pipeline |
|  | Technical Labor | Purposive expenditure of human cognitive or physical effort in technical activity. | Programming; machining; electrical installation |
|  | Technical Competence | Acquired capacity to reliably execute technical processes and techniques. | Surgeon’s procedural skill; engineer’s systems expertise |
| **System Structure** | Technical Architecture | Fundamental structural organization of a technical system, including components, relationships, boundaries, and governing principles. | Client-server; microkernel; microservices; layered architecture |
|  | Technical Blueprint | Generative description prescribing how to create, assemble, or configure an artifact. | Engineering drawing; source code; CAD model; IaC template |
|  | Technical Configuration | Particular arrangement of components, parameters, versions, and settings determining operational state. | FreeBSD kernel configuration; Kubernetes deployment configuration |
|  | Technical Interface | Defined boundary through which technical elements exchange matter, energy, information, or control. | API; electrical connector; CLI; network protocol |
|  | Production Virtual Technical Object | A technical object whose operative structure is primarily informational or computational and whose operation is realized through computation. | LLM, database, algorithm, simulation |
|  | Production Technical Object | Technical object produced within a production system and intended to enable action or further production. | Aircraft; server; turbine; software product |
|  | Constitutive Technical Object | Component or sub-assembly constituting a larger technical object or system. | CPU; battery cell; bearing; database schema |
|  | Production Technical System | Organized set of production technical objects whose interaction realizes a technical capability. | Power plant; computer system; manufacturing line |
| **System Relations** | Technical Dependency | Relation in which one technical element requires another for production, operation, or maintenance. | Application → operating system → hardware |
|  | Technical Interaction | Relation through which technical elements affect one another during operation or transformation. | Sensor → controller → actuator |
| **Mechanism & Capability** | Technical Capability | Value-producing possibility enabled by a technical function. | Network communication; secure authentication; high-speed computation |
|  | Technical Mechanism | Physical, procedural, or logical arrangement through which a function or transformation is produced. | Milling; refactoring; soldering; garbage collection |
|  | Technical Property | Characteristic attributable to a technical object, process, or system. | Mass; latency; modularity; reliability |
|  | Technical Quality | Degree to which desirable technical properties are possessed under relevant conditions. | Reliability; maintainability; efficiency; safety |
|  | Technical Performance | Realized quantitative behavior under specified conditions. | 10 Gbit/s throughput; 99.99% availability |
| **Technique** | Technical Task | Discrete unit of planned technical work assigned to an agent. | Implement authentication; calibrate sensor |
|  | General Technique | Generalized method for performing a class of technical operations. | TIG welding; unit testing; photolithography |
|  | Operative Technique | Situated application of a technique by an agent to a particular technical situation. | Applying TIG welding to a specific aluminum joint |
|  | Constitutive Technique | A technique embodied in a technical element that constitutes part of its technical organization, establishing an internal dynamic logic through which the element operates and fulfills its technical role. | Parsing, optimization, code generation |
|  | Technical Act | Primitive Technique performed by an agent on reality or a technical object. | Cutting; welding; compiling; deploying; measuring |
|  | Technical Interface & Actuation | Boundary and means through which an agent encodes intent and acts upon a technical object or reality. | CNC spindle + G-code; robotic gripper + controller |
| **Technical Control** | Technical Feedback | Information about intervention effects or system state that enables adjustment and error correction. | Sensor reading; build error; crash report; quality inspection |
|  | Technical Evaluation | Systematic determination of properties, performance, adequacy, or conformity. | Benchmarking; inspection; testing |
|  | Verification | Evaluation of whether an artifact conforms to its specification or blueprint. | Unit tests; static analysis; dimensional inspection |
|  | Validation | Evaluation of whether an artifact fulfills its intended purpose or solves the intended problem. | User validation; operational trials |
|  | Technical Hazard | Condition or source capable of producing an undesirable or harmful technical outcome. | Exposed voltage; thermal runaway; race condition |
|  | Technical Risk | Possibility and consequence of an undesirable technical outcome under uncertainty. | Structural failure risk; security breach risk |
|  | Technical Trade-off | Relationship in which improvement in one property or objective constrains another. | Performance vs. energy consumption; flexibility vs. complexity |
|  | Technical Failure | State or event in which a technical object or process fails to perform a required function or satisfy a specification. | Crash; structural fracture; thermal runaway |
|  | Technical Security | Principles and practices concerned with protecting systems against unauthorized or adversarial actions. | Access control; encryption; authentication |
| **Lifecycle & Continuity** | Technical Maintenance | Activity performed to preserve or restore an artifact's functional state. | Patching; lubrication; recalibration; replacement |
|  | Technical Service | Technical capability delivered to an external agent or system through an operational interface. | DNS resolution; payment processing; electricity delivery |
|  | Technical Lifecycle | Temporal trajectory of a technical object from conception through production, operation, maintenance, modification, and retirement. | Design → production → deployment → operation → retirement |
|  | Technical Evolution | Historical change in technical artifacts, processes, knowledge, and capabilities over time. | Vacuum tubes → transistors → integrated circuits |
|  | Technical Obsolescence | Condition in which a technical artifact loses technical, economic, or social viability relative to alternatives. | Legacy operating system; obsolete communication protocol |


### Recursive view

> The table below renders each technical element type at its full tree path: every segment is a type — categories do not belong to the tree; they live only in the Tabular view. Row order follows the Tabular view for readability and carries no grammatical meaning.

> **Note:** This tree is a **generative grammar** for the instance tree used to represent decomposition. It defines the abstract type tree whose intermediate nodes serve as **structuring elements** for the corresponding instance tree: an instance decomposition is well-formed when every instance row's type path in the fourth column is a path the grammar generates.

> **Note:** The links between nodes mean containment-in-scope only — a child type may occur scoped inside its parent type. They do not represent specified relations at this level. Their relational semantics are intentionally left unspecified for now.

> **Recursion rule:** any `Technical Element Set` may contain any `Technical Element Set` or any technical element type at any depth. The two `...` rows at the top of the table state this closure explicitly as schema notation — they are not concrete types: `...` means zero or more intervening Set nestings, and `{any Technical Element Type}` means any terminal type from this table. Every prefix of every concrete path below is itself a valid path.

> **Spines:** the grammar has two deep spines — a Technique spine (`Technical Practice > Technical Task > General Technique > Operative Technique > Constitutive Technique > Technical Act > Technical Interface & Actuation`) and a System spine (`Production Technical System > Production Technical Object > Constitutive Technical Object > Production Virtual Technical Object`) — plus three Set specializations (`Technical Practice`, `Technical Ecosystem`, `Technical Domain`) and flat facet types that attach directly under a Set. An instance table may land at any depth of a spine; intermediate levels are structuring types, never skipped in the type path itself.

> **Note on `Technical Activity`:** it does not appear in this tree. An Activity is the temporal instantiation of a Practice — operation rather than structure — and a fully specified Practice leaves it no additional structural role (see QA below).

| **Technical Element Type Tree Path** | **Description (Role)** | **Instance(s)** |
| --- | --- | --- |
| `(root) > Technical Element Set` | A collection of technical elements. | Semiconductor manufacturing ecosystem; modern LLM ecosystem |
| `(root) > Technical Element Set > ... > Technical Element Set` | Recursive nesting: a set contained in a set at any depth — the recursive form. | CI/CD practice within a DevOps set |
| `(root) > Technical Element Set > ... > {any Technical Element Type}` | The general form: any technical element type may occur at any depth beneath a set — this denotes every possible type path. | e.g. a Technical Task nested three sets deep |
| `(root) > Technical Element Set > Technical Practice` | Repeatable, organized pattern of technical work integrating activities, techniques, principles, standards, and tools. | CI/CD; TDD; SRE; preventive maintenance |
| `(root) > Technical Element Set > Technical Ecosystem` | Coherent ensemble read through its actors and exchanges. | Semiconductor manufacturing ecosystem; modern LLM ecosystem |
| `(root) > Technical Element Set > Technical Domain` | Bounded field of technical reality defined by problems, purposes, phenomena, and intervention targets. | Structural engineering; semiconductor fabrication; machine learning; database systems |
| `(root) > Technical Element Set > Production Technical System` | Organized set of production technical objects whose interaction realizes a technical capability. | Power plant; computer system; manufacturing line |
| `(root) > Technical Element Set > Production Technical System > Production Technical Object` | Technical object produced within a production system and intended to enable action or further production. | Aircraft; server; turbine; software product |
| `(root) > Technical Element Set > Production Technical System > Production Technical Object > Constitutive Technical Object` | Component or sub-assembly constituting a larger technical object or system. | CPU; battery cell; bearing; database schema |
| `(root) > Technical Element Set > Production Technical System > Production Technical Object > Constitutive Technical Object > Production Virtual Technical Object` | A technical object whose operative structure is primarily informational or computational and whose operation is realized through computation. | LLM, database, algorithm, simulation |
| `(root) > Technical Element Set > Technical Practice > Technical Task` | Discrete unit of planned technical work assigned to an agent. | Implement authentication; calibrate sensor |
| `(root) > Technical Element Set > Technical Practice > Technical Task > General Technique` | Generalized method for performing a class of technical operations. | TIG welding; unit testing; photolithography |
| `(root) > Technical Element Set > Technical Practice > Technical Task > General Technique > Operative Technique` | Situated application of a technique by an agent to a particular technical situation. | Applying TIG welding to a specific aluminum joint |
| `(root) > Technical Element Set > Technical Practice > Technical Task > General Technique > Operative Technique > Constitutive Technique` | A technique embodied in a technical element that constitutes part of its technical organization, establishing an internal dynamic logic through which the element operates and fulfills its technical role. | Parsing, optimization, code generation |
| `(root) > Technical Element Set > Technical Practice > Technical Task > General Technique > Operative Technique > Constitutive Technique > Technical Act` | Primitive Technique performed by an agent on reality or a technical object. | Cutting; welding; compiling; deploying; measuring |
| `(root) > Technical Element Set > Technical Practice > Technical Task > General Technique > Operative Technique > Constitutive Technique > Technical Act > Technical Interface & Actuation` | Boundary and means through which an agent encodes intent and acts upon a technical object or reality. | CNC spindle + G-code; robotic gripper + controller |
| `(root) > Technical Element Set > Technical Problem` | Discrepancy between a current or projected state and a desired technical state that calls for intervention. | Reducing query latency below 200 ms under 10× load |
| `(root) > Technical Element Set > Technical Purpose` | Intended ultimate effect or value of the technical endeavor. | Transport passengers; cure an infection; provide real-time financial data |
| `(root) > Technical Element Set > Technical Constraint` | Bound on technical action imposed by reality, resources, regulations, or other conditions. | Material strength; power budget; latency floor; regulatory restriction |
| `(root) > Technical Element Set > Technical Resource` | Input required or consumed by technical activity. | Silicon wafers; electricity; RAM; labor-hours; capital |
| `(root) > Technical Element Set > Technical Requirement` | Formalized desired state, need, or performance objective a solution must satisfy. | 99.99% uptime; <50 dB noise |
| `(root) > Technical Element Set > Technical Specification` | Precise statement of requirements, parameters, performance, and interface conditions used to define and verify a solution. | API response time <200 ms p99; −40°C to +85°C operating range |
| `(root) > Technical Element Set > Technical Parameter` | Variable whose value characterizes or controls a technical object or process. | Voltage; timeout; CPU frequency; thread count; tolerance |
| `(root) > Technical Element Set > Technical Standard` | Normative specification governing form, function, safety, interoperability, or performance. | POSIX; HTTP; ISO standards; electrical codes |
| `(root) > Technical Element Set > Technical Knowledge` | Accumulated propositions, models, principles, methods, and know-how used to understand and intervene in technical reality. | Networking knowledge; materials science; operating-system knowledge |
| `(root) > Technical Element Set > Technical Research` | Systematic investigation aimed at discovering technical knowledge, principles, methods, materials, or capabilities. | Novel battery chemistry; new semiconductor process |
| `(root) > Technical Element Set > Technical Principle` | General rule governing construction or operation of technical systems. | Least privilege; redundancy; fail-safe; separation of concerns |
| `(root) > Technical Element Set > Technical Framework` | Overarching logic for structuring technical problems and generating or evaluating solutions. | Systems engineering; TRIZ; control theory; FMEA |
| `(root) > Technical Element Set > Technical Strategy` | Context-sensitive regime for planning, sequencing, prioritizing, and allocating technical work. | Agile; waterfall; prototyping-first; blue-green deployment |
| `(root) > Technical Element Set > Technical Institution` | Durable social structure that organizes, governs, or sustains technical practice and knowledge. | IEEE; FAA; corporate R&D division; standards body |
| `(root) > Technical Element Set > Technical Agent` | Entity capable of executing Techniques using tools, resources, and knowledge. | Engineer; robot; compiler; build pipeline |
| `(root) > Technical Element Set > Technical Labor` | Purposive expenditure of human cognitive or physical effort in technical activity. | Programming; machining; electrical installation |
| `(root) > Technical Element Set > Technical Competence` | Acquired capacity to reliably execute technical processes and techniques. | Surgeon’s procedural skill; engineer’s systems expertise |
| `(root) > Technical Element Set > Technical Architecture` | Fundamental structural organization of a technical system, including components, relationships, boundaries, and governing principles. | Client-server; microkernel; microservices; layered architecture |
| `(root) > Technical Element Set > Technical Blueprint` | Generative description prescribing how to create, assemble, or configure an artifact. | Engineering drawing; source code; CAD model; IaC template |
| `(root) > Technical Element Set > Technical Configuration` | Particular arrangement of components, parameters, versions, and settings determining operational state. | FreeBSD kernel configuration; Kubernetes deployment configuration |
| `(root) > Technical Element Set > Technical Interface` | Defined boundary through which technical elements exchange matter, energy, information, or control. | API; electrical connector; CLI; network protocol |
| `(root) > Technical Element Set > Technical Dependency` | Relation in which one technical element requires another for production, operation, or maintenance. | Application → operating system → hardware |
| `(root) > Technical Element Set > Technical Interaction` | Relation through which technical elements affect one another during operation or transformation. | Sensor → controller → actuator |
| `(root) > Technical Element Set > Technical Capability` | Value-producing possibility enabled by a technical function. | Network communication; secure authentication; high-speed computation |
| `(root) > Technical Element Set > Technical Mechanism` | Physical, procedural, or logical arrangement through which a function or transformation is produced. | Milling; refactoring; soldering; garbage collection |
| `(root) > Technical Element Set > Technical Property` | Characteristic attributable to a technical object, process, or system. | Mass; latency; modularity; reliability |
| `(root) > Technical Element Set > Technical Quality` | Degree to which desirable technical properties are possessed under relevant conditions. | Reliability; maintainability; efficiency; safety |
| `(root) > Technical Element Set > Technical Performance` | Realized quantitative behavior under specified conditions. | 10 Gbit/s throughput; 99.99% availability |
| `(root) > Technical Element Set > Technical Feedback` | Information about intervention effects or system state that enables adjustment and error correction. | Sensor reading; build error; crash report; quality inspection |
| `(root) > Technical Element Set > Technical Evaluation` | Systematic determination of properties, performance, adequacy, or conformity. | Benchmarking; inspection; testing |
| `(root) > Technical Element Set > Verification` | Evaluation of whether an artifact conforms to its specification or blueprint. | Unit tests; static analysis; dimensional inspection |
| `(root) > Technical Element Set > Validation` | Evaluation of whether an artifact fulfills its intended purpose or solves the intended problem. | User validation; operational trials |
| `(root) > Technical Element Set > Technical Hazard` | Condition or source capable of producing an undesirable or harmful technical outcome. | Exposed voltage; thermal runaway; race condition |
| `(root) > Technical Element Set > Technical Risk` | Possibility and consequence of an undesirable technical outcome under uncertainty. | Structural failure risk; security breach risk |
| `(root) > Technical Element Set > Technical Trade-off` | Relationship in which improvement in one property or objective constrains another. | Performance vs. energy consumption; flexibility vs. complexity |
| `(root) > Technical Element Set > Technical Failure` | State or event in which a technical object or process fails to perform a required function or satisfy a specification. | Crash; structural fracture; thermal runaway |
| `(root) > Technical Element Set > Technical Security` | Principles and practices concerned with protecting systems against unauthorized or adversarial actions. | Access control; encryption; authentication |
| `(root) > Technical Element Set > Technical Maintenance` | Activity performed to preserve or restore an artifact's functional state. | Patching; lubrication; recalibration; replacement |
| `(root) > Technical Element Set > Technical Service` | Technical capability delivered to an external agent or system through an operational interface. | DNS resolution; payment processing; electricity delivery |
| `(root) > Technical Element Set > Technical Lifecycle` | Temporal trajectory of a technical object from conception through production, operation, maintenance, modification, and retirement. | Design → production → deployment → operation → retirement |
| `(root) > Technical Element Set > Technical Evolution` | Historical change in technical artifacts, processes, knowledge, and capabilities over time. | Vacuum tubes → transistors → integrated circuits |
| `(root) > Technical Element Set > Technical Obsolescence` | Condition in which a technical artifact loses technical, economic, or social viability relative to alternatives. | Legacy operating system; obsolete communication protocol |

## How to decompose any technical instance?

> A technical instance is decomposed by identifying the concrete technical elements that constitute, configure, support, interface with, operate, control, or sustain that particular instance. Each identified element is then classified according to its technical element type and may itself be recursively decomposed according to the decomposition rules of that type.

> **Note:** Instance Tree Path leaves are always concrete instances, while intermediate nodes provide structure, and type-tree paths belong only to the Recursive View - so the intermediate nodes - can be Instance - a more general one - or `technical element type`.

> See the worked case in QA below (### (Case Study) What is the recursively decomposed instance tree of a CRM System?).

| Instance Tree Path | Description | Technical Category | Technical Element Type Tree Path |
| --- | --- | --- | --- |
|  |  |  |  |

## QA

### What  type of technical element is a LLM?

> An LLM is a **virtual informational technical object**: an engineered computational artifact whose structure is constituted primarily by software, learned parameters, representations, and computational procedures rather than by directly observable physical structure. Its technical functions are realized through computation executed on physical infrastructure.
> 

### On the bad use of the term ‘Technology’?

> **Technology** — properly, the systematic study, knowledge, or theory of **technique and technical elements**; in everyday language, however, *technology* is commonly used metonymically to refer to the **technical elements themselves**—especially technical objects, systems, and artifacts.
> 

### What is the **most abstract formulation** that operation can take?

- Requirements → Technique → Product (Good, Service).
- Desired Difference → Controlled Transformation → Realized Difference.

### What is the relationship between `Technical Function` and `Technical Capability`?

> Note: **Technical Capability** and **Technical Function** are closely related and overlapping. **Function** is the raw concept: *what the artifact does*. **Capability** refers to the **value or possibility enabled by that function**: *what the function makes possible*.
> 

### Is every function realized through a mechanism?

> **Yes.** A function is realized by a mechanism that produces the required effect. However, **mechanism is a more abstract concept than process**: the same mechanism can realize different functions, depending on how it is organized or operated.
> 

### Is a mechanism identical to an underlying process?

> **No.** A mechanism is not necessarily identical to a single underlying process. A mechanism may **coordinate or combine multiple processes** to realize a function. Conversely, the same underlying process may participate in different mechanisms and contribute to different functions.
> 

### What is the relation between Function, Mechanism and Process?

> **Function** = what is achieved.
> 

> **Mechanism** = how the function is realized.
> 

> **Process** = an organized sequence of transformations or events that may constitute part of the mechanism.
> 

### What is the relation between 'Technical Capability' and 'Technical Function'?

> A Technical Capability is a latent functionality: a function that a technical element is capable of exercising but is not currently exercising. A Technical Function is a capability being exercised in operation.
> 

> A technical decomposition describes the **structure** of a technical element, not its real-time operation; therefore, **specifying its technical function is not necessary**.
> 

### What is the relation between `Technical Practice` and `Technical Activity`?

> **Technical Practice** is the pattern; **Technical Activity** is the pattern exercised in time. A Practice organizes *what* recurs — activities, techniques, principles, standards, tools; an Activity is one scheduled exercising of it — brief → build → launch → monitor → close. Every Activity belongs to a Practice the way every exercised Function belongs to a Capability: the same duality, temporal instead of modal.
> 

### Do we actually need `Technical Activity` as a technical element in the decomposition of a technical element, or is it already covered by `Technical Practice`, similar to the relationship between `Technical Function` and `Technical Capability`?

> **No.** A fully specified `Technical Practice`—including its Tasks, Techniques, Acts, standards, and control gates—leaves no additional structural role for `Technical Activity` to contribute. An Activity is the **temporal instantiation of a Practice**: it describes the Practice as it is actually being performed over time. Like `Technical Function`, it therefore describes **operation rather than structure** and is not necessary for the structural decomposition of a technical element.


### Why is the category `Technical Element Set` required?

> A **Technical Element Set** is required to represent coherent technical ensembles whose members belong to different technical element types but are related through a common technical object, standard, capability, production process, or technical domain.
> 

> Without this category, the taxonomy can describe the individual elements of such an ensemble, but it lacks a type for representing **the ensemble itself as a technical entity of organization**.
> 

> **Take as example:** the OpenAPI technical ecosystem. It comprises the OpenAPI Specification (OAS), OpenAPI documents, annotations, generators, plugins, libraries, validation tools, documentation tools, and generated artifacts. These elements have different technical element types, but are related through the common purpose of specifying, producing, validating, documenting, and consuming API interfaces. The **Technical Element Set** category provides a type for representing this coherent ensemble as a whole.
> 

### Why shouldn't `Technical Knowledge` be a technical element type?

Technical Knowledge should not be a technical-element type because knowledge is already represented by the taxonomy as a distinct ontological category; making it a technical element would conflate the knowledge about a technical reality with the technical reality itself.> 

### (Case Study) What is the recursively decomposed instance tree of a CRM System?

> Worked decomposition of a CRM System, grown from the marketing-note subtree to full intermediate detail. Read it against the contract above: `CRM System` and `CRM application` are intermediate type elements giving structure (system scoping its production object; the application grouping its records beneath it); `Contact record`, `Consent record`, and `Lifecycle stage` are intermediate type elements further structuring their attributes beneath them, and `Contact attribute schema`, `Dedupe mechanism`, `Stage-transition automation`, `Forms API`, and `Import API` structure a third level of fields, rules, and contracts beneath them; the remaining rows are final-node instances — concrete fields, tokens, formats, schedules, and measured values — and `HubSpot CRM` and `Salesforce` are exemplar leaves realizing the application, with one concrete deployment identifier each. Deployment-specific values and named vendors appear only in rows marked exemplar.

| Instance Tree Path | Description | Technical Category | Technical Element Type Tree Path |
| --- | --- | --- | --- |
| Marketing Technical Practice > CRM System | Production system of record for contacts, consent, and lifecycle stage. | System Structure | `(root) > Technical Element Set > Production Technical System` |
| Marketing Technical Practice > CRM System > CRM application | Vendor-neutral production object realizing the system of record; deployments realize this object. | System Structure | `(root) > Technical Element Set > Production Technical System > Production Technical Object` |
| Marketing Technical Practice > CRM System > CRM application > Schema version | Version of the contact-and-consent schema the application enforces (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > CRM application > Contact record | Constitutive object holding one addressable contact. | System Structure | `(root) > Technical Element Set > Production Technical System > Production Technical Object > Constitutive Technical Object` |
| Marketing Technical Practice > CRM System > CRM application > Contact record > Contact attribute schema | Field contract: identifiers, consent flags, lifecycle stage. | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > CRM application > Contact record > Contact attribute schema > Identifier field | Addressable key of the record, e.g. email (exemplar values per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > CRM application > Contact record > Contact attribute schema > Consent flag field | Boolean flags recording consent state per contact (exemplar values per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > CRM application > Contact record > Contact attribute schema > Lifecycle stage field | Stage attribute carried on the record, mirroring the lifecycle configuration (exemplar values per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > CRM application > Contact record > Dedupe mechanism | Merge logic resolving duplicate identities. | Mechanism & Capability | `(root) > Technical Element Set > Technical Mechanism` |
| Marketing Technical Practice > CRM System > CRM application > Contact record > Dedupe mechanism > Match rule | Rule declaring which field comparisons constitute identity, e.g. email-exact plus name-fuzzy. | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > CRM application > Contact record > Dedupe mechanism > Survivorship rule | Rule declaring which record's values survive a merge. | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > CRM application > Contact record > Contact verification | Check that a record conforms to the attribute schema and is deliverable. | Technical Control | `(root) > Technical Element Set > Verification` |
| Marketing Technical Practice > CRM System > CRM application > Consent record | Constitutive object holding opt-in evidence per contact (exemplar entries per deployment). | System Structure | `(root) > Technical Element Set > Production Technical System > Production Technical Object > Constitutive Technical Object` |
| Marketing Technical Practice > CRM System > CRM application > Consent record > Opt-in timestamp | Proof-of-consent attribute (exemplar values per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > CRM application > Consent record > Consent source | Origin of the consent: form, import, or manual entry (exemplar per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > CRM application > Consent record > Consent basis | Lawful basis recorded for the processing, e.g. consent, contract, legitimate interest. | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > CRM application > Consent record > Retention window | How long consent evidence is kept, e.g. 24 months (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > CRM application > Consent record > Preference-center boundary | Boundary through which a contact reviews and withdraws consent. | System Structure | `(root) > Technical Element Set > Technical Interface` |
| Marketing Technical Practice > CRM System > Lifecycle stage | Stage marker moving contacts from lead to customer (exemplar stages per deployment). | System Structure | `(root) > Technical Element Set > Technical Configuration` |
| Marketing Technical Practice > CRM System > Lifecycle stage > Stage definition | Ordered stage list, e.g. lead, qualified, opportunity, customer (exemplar stages per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > Lifecycle stage > Stage-entry criterion | Condition a contact must satisfy to enter a stage. | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > Lifecycle stage > Stage-transition automation | Rule-driven moves on behavior or operator acts. | Mechanism & Capability | `(root) > Technical Element Set > Technical Mechanism` |
| Marketing Technical Practice > CRM System > Lifecycle stage > Stage-transition automation > Behavior trigger | Observed behavior firing a transition, e.g. form submit (exemplar per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > Lifecycle stage > Stage-transition automation > Transition rule | Rule mapping triggers and operator acts onto stage moves. | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > Lifecycle stage > Progression capability | Value realized: moving contacts from lead to customer. | Mechanism & Capability | `(root) > Technical Element Set > Technical Capability` |
| Marketing Technical Practice > CRM System > Forms API | Capture boundary for web-originated contacts. | System Structure | `(root) > Technical Element Set > Technical Interface` |
| Marketing Technical Practice > CRM System > Forms API > Form field mapping | Contract binding form fields onto contact attributes. | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > Forms API > Forms auth token | Credential authorizing submissions (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > Forms API > Submission endpoint | Endpoint receiving form payloads. | System Structure | `(root) > Technical Element Set > Technical Interface` |
| Marketing Technical Practice > CRM System > Forms API > Submission rate limit | Maximum accepted submissions per interval (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > Import API | Bulk-ingestion boundary for lists (exemplar files per deployment). | System Structure | `(root) > Technical Element Set > Technical Interface` |
| Marketing Technical Practice > CRM System > Import API > Import file format | Accepted list-file format and column contract, e.g. CSV. | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > Import API > Import column map | Mapping of file columns onto contact attributes (exemplar per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Specification` |
| Marketing Technical Practice > CRM System > Import API > Import schedule | Cadence of bulk ingestion, e.g. nightly (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > Import API > Import validation | Check that an ingested file conforms to the import format before its rows enter the application. | Technical Control | `(root) > Technical Element Set > Validation` |
| Marketing Technical Practice > CRM System > Contact-base audit | Periodic determination of record quality across the contact base. | Technical Control | `(root) > Technical Element Set > Technical Evaluation` |
| Marketing Technical Practice > CRM System > Duplicate-contact rate | Measured share of duplicate identities in the base (exemplar measured value per deployment). | Mechanism & Capability | `(root) > Technical Element Set > Technical Quality` |
| Marketing Technical Practice > CRM System > Read availability | Realized availability of contact reads (exemplar measured value per deployment). | Mechanism & Capability | `(root) > Technical Element Set > Technical Performance` |
| Marketing Technical Practice > CRM System > Nightly snapshot backup | Backup preserving a restorable functional state, run nightly (exemplar schedule per deployment). | Lifecycle & Continuity | `(root) > Technical Element Set > Technical Maintenance` |
| Marketing Technical Practice > CRM System > Contact resolution service | Contact-lookup capability delivered to the campaign pipeline through an operational interface. | Lifecycle & Continuity | `(root) > Technical Element Set > Technical Service` |
| Marketing Technical Practice > CRM System > CRM application > HubSpot CRM | Exemplar production CRM realizing the application. | System Structure | `(root) > Technical Element Set > Production Technical System > Production Technical Object` |
| Marketing Technical Practice > CRM System > CRM application > HubSpot CRM > HubSpot portal identifier | Deployment identifier of the HubSpot portal (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |
| Marketing Technical Practice > CRM System > CRM application > Salesforce | Exemplar production CRM realizing the application. | System Structure | `(root) > Technical Element Set > Production Technical System > Production Technical Object` |
| Marketing Technical Practice > CRM System > CRM application > Salesforce > Salesforce org identifier | Deployment identifier of the Salesforce org (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Element Set > Technical Parameter` |

### How to decompose an instance that belongs to multiple element types?

> By default, a **multi-root forest**: one root per candidate type, each root growing its own well-formed tree. No instance row ever carries two types — the fourth column holds exactly one type path per row. Ambiguity is resolved by multiplication of trees, not by compromise typing.

> A technical element can belong to many types: OpenAPI is a `Technical Standard` readable as a `Technical Element Set`; JobRunr is a `Constitutive Technical Object` readable as a `Technical Element Set` and as a `Production Technical System`; Biotechnology is a `Technical Domain` readable as a `Technical Element Set`. Each reading gets its own root and its own tree: the OpenAPI-as-Standard tree decomposes spec versions and objects (normative content), while the OpenAPI-as-Set tree decomposes documents, tooling, and practices (ecosystem members). Well-formedness per tree is unchanged — every fourth-column path must be a grammar path; leaves are instances, intermediate nodes give structure.

> When the root typing is ambiguous, ask the user for disambiguation instead of guessing. If no answer comes, build the **default root**: a primary type chosen from the Tabular view above (the "How can we characterize the technical aspect of human experience?" table), recorded as the note's primary belonging in the "What technical element type does this technical instance belong to?" Formulation answer, with secondary readings kept as `readable as …` prose. The default root is therefore always explicit in the note itself.

### Which note schema used - in order to document a technical element?

```bash
# (Technical Element)

> (Intro)

## Formulation

### What technical element type does this technical instance belong to?
### What is this technical instance?
### What is the recursive instance decomposition of this technical instance?

## References

- ...
```

## References

- https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Onto/Synontic/Technique/
- https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Facet/Technical/Technology/
- Agency
- Problem
- https://plato.stanford.edu/entries/questions/
- Ontology
> `Mechanism` is to dynamics, what `program` is to  computation.
