---
tags: [technique]
---

# Naming


> **Naming** refers to the process of assigning identifiers or labels to entities such as variables, functions, files, or resources, facilitating their identification, reference, and management within software systems or data structures.
> 

## Formulation

**Naming** can be formulated as a **mapping relation**

**Name → Referent**,

where a *name* is a symbolic token drawn from a defined **name space**, and the *referent* is an entity in some **object space** (resources, processes, files, values, capabilities, etc.).

More formally, a naming system defines:

- A **name space** `N` (set of valid names).
- An **object space** `O` (set of named entities).
- A **resolution function** `R: N → O ∪ {⊥}` mapping names to objects or failure.
- A **generation function** `G: O → N*` mapping objects to one or more names (optional in pure reference schemes).

A naming system therefore operationalizes the invariant:

**Resolution ∘ Generation ≈ Identity**,

except where ambiguity, aliasing, or multi-homing are explicitly allowed by design.

## Foundation

> Foundationally, naming systems arise from three fundamental constraints in computing:
(1) Indirection, (2) Identity, and (3) Coordination.
> 

> **Indirection** is the requirement that references must remain stable even when the underlying object’s representation, location, or state changes, forcing naming systems to introduce a symbolic layer that decouples *what is named* from *where or how it is realized*.
> 

> **Identity** is the requirement that objects must be distinguishable and persistently referenceable across time, processes, and contexts, forcing naming systems to define explicit rules for sameness, persistence, aliasing, and equivalence.
> 

> **Coordination** is the requirement that multiple agents (processes, users, machines, or distributed nodes) must be able to refer to shared objects in a consistent and conflict-free manner, forcing naming systems to define systematic mechanisms for name creation, delegation, authority, and resolution.
> 

## Evaluation Model

> An evaluation model provides the formal criteria and analytic dimensions for assessing a naming system’s fitness for purpose within a particular computational environment.
It decomposes naming quality into functional, structural, operational, and socio-technical dimensions.
> 

| **Dimension** | **Criteria** | **Description** |
| --- | --- | --- |
| **Functional** | **Uniqueness** | Ensures each name denotes exactly one object within the system; prevents ambiguity and conflicting bindings. |
|  | **Non-ambiguity / Deterministic Resolution** | A name must always resolve to the same object under the same context; resolution must be deterministic. |
|  | **Expressiveness** | Degree to which names can encode, expose, or support the semantics required by the domain or system. |
|  | **Stability / Persistence** | Names should remain valid as the system evolves, enabling long-lived references. |
|  | **Location-Independence (if desired)** | Names should not encode physical or topological placement unless the system requires it. |
|  | **Content Sensitivity (if desired)** | Ability of names to represent or reflect properties of the underlying content (e.g., content hashes). |
| **Structural** | **Namespace Organization** | Clarity and robustness of hierarchical, flat, or graph-structured namespaces; supports scoping and boundary control. |
|  | **Scalability of the Name Space** | Capacity to grow with the system without collisions or degradation in precision; supports large populations. |
|  | **Extensibility** | Ability to evolve the naming grammar or name space without breaking existing references. |
|  | **Semantic Opacity / Transparency** | How much of the internal structure is exposed by the name; relates to encapsulation and cognitive load. |
|  | **Collision Resistance** | Probability and protection mechanisms against accidental name duplication, especially in concurrent or distributed generation. |
| **Operational** | **Ease of Generation** | Cost, complexity, and concurrency characteristics of generating new names; supports automation and parallelism. |
|  | **Resolution Efficiency** | Time and computational cost of name → object mapping; includes indexing, caching, lookup paths, and distribution. |
|  | **Update & Mutation Cost** | Ease of renaming, migrating, or refactoring names across systems. |
|  | **Fault Tolerance** | Behavior under partial failures (network partitions, stale caches, inconsistent replicas). |
|  | **Security & Forgery Resistance** | Difficulty of guessing, spoofing, or forging names; protection against namespace attacks. |
|  | **Operational Overhead** | Resource usage associated with generation, storage, distribution, and resolution. |
| **Socio-Technical** | **Human-Readability** | How easily names convey meaning to operators, developers, or analysts; affects comprehension and error rates. |
|  | **Consistency & Convention Alignment** | Conformance to organizational or industry naming conventions; improves coordination and shared expectations. |
|  | **Cognitive Load** | Mental effort required to interpret, locate, or construct names. |
|  | **Administrative Simplicity** | Ease of governance, auditing, delegation, and lifecycle management across teams or institutions. |
|  | **Domain Alignment** | Fit between the naming scheme and the vocabulary or ontology of the target domain. |
|  | **Social Persistence** | Stability of names across organizational changes (teams, ownership, roles), ensuring references remain meaningful. |

## Naming Scheme

> Naming schemes in computer systems refer to the conventions used to name and identify entities in the system.
> 

> A  naming model comprises the definition of its name space, the mapping algorithm used to assign names to resources, and the universe of values representing all possible names within the model.
> 

> **Name Space:** The set of all possible names or identifiers that can be assigned to resources within the system.
> 

> **Name Mapping Algorithm:** The algorithm or method used to map names from the name space to specific resources or entities within the system.
> 

> **Universe of Values:** The set of all possible values that can be assigned to names within the name space.
> 

A naming foundation typically defines:

- **Syntax** (valid form of names)
- **Semantics** (meaning of names in terms of referents)
- **Resolution model** (binding, lookup, caching)
- **Authority model** (who controls name creation and delegation)
- **Consistency model** (how resolution behaves over time and space)

### Evaluation

> What are the criteria for evaluating a naming scheme?
> 

| **Criteria** | **Description** | **Note** |
| --- | --- | --- |
| **Uniqueness** | Ensures each name refers to exactly one object. | Fundamental requirement; prevents ambiguity. |
| **Non-ambiguity** | A given name always maps to the same object. | Stability in resolution is essential. |
| **Scalability** | Scheme maintains performance and uniqueness as the system grows. | Critical in distributed or large-scale systems. |
| **Human-readability** | Names can be meaningfully interpreted by operators or developers. | Often traded off against compactness. |
| **Compactness / Efficiency** | Names do not waste space or bandwidth. | Matters for storage, network, and performance. |
| **Stability / Persistence** | Names remain valid over time despite system changes. | Important for long-lived references. |
| **Location-independence** | Names do not encode physical or network location. | Enables mobility and abstraction; not always desired. |
| **Semantic opacity** | Degree to which the name reveals internal structure. | “Opaque” names support encapsulation. |
| **Collision resistance** | Minimizes likelihood of two objects receiving the same name. | Relevant in parallel creation environments. |
| **Resolution efficiency** | Speed and cost of converting a name → object. | Affects lookup latency (e.g., DNS vs. direct pointers). |
| **Ease of generation** | Complexity of creating new valid names. | Important for automation and concurrency. |
| **Namespace organization** | How clearly the scheme defines hierarchy, scoping, and boundaries. | Good organization prevents naming conflicts. |
| **Administrative simplicity** | Ease of managing, delegating, and auditing names. | Especially relevant in multi-team or multi-domain systems. |
| **Extensibility** | Ability to evolve without breaking existing names. | Future-proofing against new formats or scale. |
| **Security / Forgery resistance** | Difficulty of guessing, spoofing, or forging names. | Relevant in access-controlled systems. |

### Strategy

> Which are the types by strategy of names schemes?
> 

| **Naming Scheme Type** | **Description** | **Case(s)** |
| --- | --- | --- |
| **Opaque / Arbitrary Names** | Names carry no semantic meaning; purely identifiers. | UUIDs, PIDs, cryptographic hashes. |
| **Semantic / Descriptive Names** | Names encode human-meaningful information. | Domain names, file paths (`/usr/bin`), variable names. |
| **Hierarchical Naming** | Names arranged in a tree or multi-level structure. | DNS, file systems, class name packages (`java.util.*`). |
| **Flat Naming** | Single-level namespace with no hierarchy. | MAC addresses, numeric IDs, distributed UUIDs. |
| **Location-Independent Names** | Names do not embed physical/network location. | Content-addressable storage, Git SHA-1, object IDs. |
| **Location-Dependent Names** | Names encode where the object is located. | IP addresses, memory addresses, file descriptors. |
| **Content-Based Names** | Name is derived from the content itself. | Hash-based systems (Git, IPFS, CAS). |
| **Attribute-Based Names** | Names are defined by a set of attributes or key-value pairs. | LDAP DNs, database queries, search-based identifiers. |
| **Path-Based Names** | Identity = traversal path through a structure. | File system paths, URL paths, XPath. |
| **Relative Names** | Name interpretation depends on the current context. | `.` `..` in file systems, relative URLs. |
| **Global Names** | Valid and unique across the entire system or world. | Domain names, MAC addresses, ISBNs. |
| **Local Names** | Valid only within a certain scope or subsystem. | Local variables, temporary IDs, container PIDs. |

### Technique

> How to generate GUUI’s?
> 

> Note: This is basically an operational technique.
> 

| Naming Algorithm | Description | Example |
| --- | --- | --- |
| Sequential Naming | Assigns names or identifiers sequentially based on a predefined order or sequence, often incrementing a numeric value or appending suffixes to existing names. | File001.txt, File002.txt |
| Hash-based Naming | Generates names or identifiers by applying hash functions to data or attributes of resources, ensuring uniqueness and distribution across the name space. | MD5 hash, SHA-256 hash |
| UUID Generation | Generates universally unique identifiers (UUIDs) using algorithms that ensure uniqueness across distributed systems, often based on random or time-based methods. | UUID v4 (random UUID), UUID v1 (time-based UUID) |
| Timestamp-based Naming | Incorporates timestamps or time-based values into names or identifiers, providing ordering and temporal context for resources. | Log20220407.txt, Image2022-04-18.jpg |
| Content-based Naming | Derives names or identifiers from the content or attributes of resources, such as file contents, metadata, or characteristics, ensuring uniqueness based on resource properties. | Content-based hash, Content-based naming conventions |
| Semantic Naming | Uses meaningful or descriptive names based on the semantics or purpose of resources, enhancing understandability and context in naming schemes. | Invoice1234.pdf, CustomerRecord_JohnDoe |
| GUID Generation | Creates globally unique identifiers (GUIDs) based on algorithms that guarantee uniqueness across space and time, often using system or network information as input. | COMB GUID, Sequential GUID |
| Coordinated Naming | Names are allocated through a centralized authority or a distributed consensus protocol, ensuring global uniqueness through coordination rather than independent generation. | DNS, Raft-generated IDs, Zookeeper sequential znodes, IANA MAC OUI allocation |

### Case Study

| **Naming Scheme** | **Description** | **Characterization** | **Instance(s)** |
| --- | --- | --- | --- |
| **DNS (Domain Name System)** | Human-readable, hierarchical naming mapping domains to IPs through distributed resolution. | **Structured, Location-Independent** | `google.com` |
| **IP Addresses (IPv4 / IPv6)** | Numeric network addresses used for routing; topology-dependent. | **Location-Dependent, Structured** | `192.0.2.1` • `2001:db8::8a2e:370:7334` |
| **MAC Addresses** | Hardware identifiers globally unique to each network interface. | **Pure (Opaque), Flat, Global** | `00:1A:2B:3C:4D:5E` |
| **URI (Uniform Resource Identifier)** | General syntax for resource identification via schemes. | **Structured, Potentially Location-Independent** | `https://example.com/a` |
| **URN (Uniform Resource Name)** | Persistent, location-independent names for resources. | **Pure/Structured, Location-Independent** | `urn:isbn:0451450523` |
| **URL (Uniform Resource Locator)** | Identifier encoding how and where to access a resource. | **Structured, Partially Location-Dependent** | `https://example.com/a` |
| **GUID** | Microsoft/COM variant of globally unique 128-bit identifier. | **Pure (Opaque), Flat, Global** | `{3F2504E0-4F89-41D3-9A0C-0305E82C3301}` |
| **UUID** | Standard RFC 4122 unique identifiers (multiple generation strategies). | **Pure (Opaque), Flat, Global** | `f47ac10b-58cc-4372-a567-0e02b2c3d479` |
| **GUIDv4 / UUIDv4** | Version 4 UUID: 122 random bits → maximal entropy and independence. | **Pure (Opaque), Flat, Global** | `2f1e4c80-2c7a-4e8f-b0af-9d2b87a4e4bc` |
| **Git Object ID (SHA-1 or SHA-256)** | Content-addressable identifier: hash of file/tree/commit contents. | **Content-Based, Pure, Global (within repo)** | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| **IPFS CID (Content Identifier)** | Multibase, multihash identifier for content-addressable objects in IPFS. | **Content-Based, Structured, Location-Independent** | `bafybeigdyrzt3...` |
| **Filesystem Paths (POSIX/NTFS)** | Hierarchical names referencing files through directory traversal. | **Structured, Path-Based, Location-Independent (within FS)** | `/usr/bin/python3` |
| **Process IDs (PIDs)** | Kernel-assigned numeric identifiers for processes. | **Pure (Opaque), Flat, Local** | `pid = 1423` |
| **File Descriptors (Unix)** | Per-process small integer identifying an open file/pipe/socket. | **Pure (Opaque), Local, Ephemeral** | `fd = 3` |
| **Inode Numbers (POSIX FS)** | Unique identifiers for file metadata structures within a filesystem. | **Pure (Opaque), Flat (per FS), Location-Independent** | `inode = 128347` |

## Operationalization

### Tip(s)

> A set of useful tips when naming.
> 

| **Tip** | **Description** | **Note** | **Case** | **Counter-Case** |
| --- | --- | --- | --- | --- |
| **Use Clear Semantics** | Names should directly express the entity’s purpose or meaning. | Improves readability and reduces ambiguity. | `UserSessionManager` clearly states purpose. | `USM` or `ThingHandler` hides meaning. |
| **Prefer Consistency** | Follow consistent patterns for similar entities. | Patterns act as cognitive shortcuts. | `CreateUser`, `DeleteUser`, `UpdateUser`. | `AddUser`, `RemoveUser`, `PatchProfile` (mixed verbs). |
| **Keep Names Proportionate** | Complexity of name should match importance of entity. | Avoids both under- and over-naming. | A core module named `AuthorizationService`. | Over-naming trivial things: `BackgroundOperationTimestampedPayloadWrapper`. |
| **Use Stable Dimensions** | Name using properties that remain true even if the implementation changes. | Reduces renaming churn and semantic drift. | `BillingAddress` (domain-defined). | `StripeBillingAddress` (technology-specific). |
| **Avoid Overloading** | Don’t reuse one term for multiple different concepts. | Prevents conceptual collisions. | Use `Task` solely for asynchronous jobs. | Using `Task` for async jobs *and* UI checklist items. |
| **Think in Systems** | Name according to the object’s role within the architecture. | Builds systemic coherence. | `GatewayService`, `CoreAPI`, `DataIngestor`. | Arbitrary names like `ServerX`, `MasterBox`, `PipeThing`. |
| **Use Domain Language** | Prefer vocabulary used by real domain experts. | Aligns code with real-world semantics. | `Invoice`, `LedgerEntry`, `AuditTrail`. | Calling an invoice `BillObject`. |
| **Favor Brevity Without Loss** | Concise but semantically rich names. | Reduces cognitive noise. | `AuthToken`. | `T`, `Obj`, `X1`—too cryptic. |
| **Expose the Right Abstraction** | Use names matching conceptual level (interface vs impl). | Keeps the architecture clean. | `PaymentProvider` (abstraction), `StripeProvider` (implementation). | Using `Stripe*` everywhere. |
| **Choose Names That Support Searching** | Use distinctive names that produce precise search results. | Enhances greppability and tooling support. | `OrderCancellationPolicy`. | `Policy`, `Manager`, `Handler`—too generic. |
| **Signal Behavior Through Verbs** | Use strong, precise verbs for functions or commands. | Clarifies operational intent. | `CalculateChecksum`, `NormalizeHeader`. | `HandleData`, `ProcessThing`, `DoWork`. |
| **Prefer Whole Words Over Abbreviations** | Avoid abbreviations unless standardized or unambiguous. | Ensures universal readability. | `Configuration`, `UserRepository`. | `Cfg`, `UsrRepo`, `CfgMngr`. |
| **Optimize for the Reader, Not the Writer** | Naming prioritizes long-term comprehension, not short-term typing. | Reader-centric naming increases maintainability. | `isAuthorized` is explicit and clear. | `chkAuth`, `authz()`—writer convenience only. |
| **Name the Concept, Not the Incidental Details** | Reflect enduring conceptual identity, not temporary implementation. | Makes names resilient to refactoring. | `UserSession`. | `CacheUserTokenV2`. |
| **Prefer Positive Boolean Names** | Boolean names should describe the condition under which they are *true*. | Avoids cognitive friction and double negation. | `isEnabled`, `shouldUpdateCache`. | `notFound`, `disableUpdate` used inside negated conditions. |
| **Prefix Booleans with “Is,” “Has,” or “Can”** | Use conventional prefixes to make truth semantics instantly recognizable. | Establishes predictable cognitive pattern recognition. | `isAvailable`, `hasPermission`, `canRetry`. | Bare nouns like `available`, `permission`, `retry`—ambiguous boolean meaning. |

### Pitfalls

> What are the most common pitfalls that namers incur while naming?
> 

> Take the tips; and negate the tips.
> 

| **Pitfall** | **Description** | **Note** | **Case** |
| --- | --- | --- | --- |
| **Ambiguous Naming** | A name can be interpreted in multiple incompatible ways. | Leads to miscommunication, misuse, and divergent assumptions. | `Handler` — could refer to events, HTTP, errors, threads, etc. |
| **Over-Specific Names** | Names encode transient implementation details (vendor, algorithm, format). | Forces renaming when those details inevitably change. | `MySQLUserRepository` later switches to PostgreSQL. |
| **Inconsistent Style** | Mixing conventions (verbs, suffixes, casing, noun forms). | Breaks recognizability and pattern-based cognition. | `get_user`, `GetUserData`, `userFetch`. |
| **Overloaded Names** | Reusing the same term for different concepts. | Collapses distinct mental models, causing confusion. | `Session` used for cookies, DB connections, and chat rooms. |
| **Redundant Noise** | Adding words that carry no semantic information. | Creates visual noise and hides signal. | `UserDataInformationObject`. |
| **Premature Abstraction** | Assigning abstract names to concrete or trivial constructs. | Makes the code appear more general than it is. | Naming a simple wrapper `ResourceProvider`. |
| **Pattern Drift** | Unintentional divergence from established naming norms. | Causes fragmentation and breaks expectation scaffolding. | A module has `ServiceA`, `ServiceB`, then someone adds `WorkerFoo`. |
| **Domain Misalignment** | Names contradict established terminology of the real domain. | Causes confusion and friction with domain experts. | Calling a “ledger entry” a “transaction blob.” |
| **Cutesy or Clever Naming** | Using jokes, puns, memes, or cultural references. | Ages poorly and becomes incomprehensible. | `KrakenReleaser`, `ChaosMonkeyFixer`. |
| **Double Negation** | A name is negated, then used in negated form in logic. | Forces the reader to mentally invert the condition twice. | `let updateCache = (x not in S); if (!updateCache) ...` |
| **Semantic Drift** | The name implies semantics that the implementation no longer matches. | One of the most dangerous traps: the code “looks right but lies.” | `updateCache` suggests a write action but is used as a boolean guard. |
| **Partial Semantics** | A name encodes only part of the actual condition, hiding additional logic. | Causes misinterpretation of invariants and intent. | `approved(x)` means `income(x) && age(x)` but is used as if it meant only income. |

## Case Study

> Let see a set of cases in Programming Languages STL.
> 

| **Category** | **Name** | **Description** | **Evaluation** | **Alternative(s)** |
| --- | --- | --- | --- | --- |
| Extraction & Access | `.unwrap()` | Extracts value but panics on absence/error. | Misleadingly safe verb; catastrophic hidden semantics. | `.expect()`, `.into_value()`, `.try_unwrap()`, value_or_error(), unwrap_or_panic() …. |
|  | `dict.get()` | Returns `None` if missing, colliding with valid `None`. | Conflates absence with value; loses information. | `get_or_default()`, `get_optional()`, `try_get()` |
|  | `map[key]` (C++) | Inserts default if key missing. | Lookup name that mutates; violates access semantics. | `at()`, `find()`, `try_get()` |
|  | `find()` | Returns index or sentinel. | Magic sentinel; ambiguous structural meaning. | `find_index()`, `try_find()`, `index_of()` |
|  | `set.count()` | Returns 0 or 1, not cardinality. | Misleads users expecting cardinality. | `contains()`, `has()`, `present()` |
| Mutation | `remove()` (C++ alg) | Partitions range; doesn’t remove. | Semantic inversion; infamous footgun. | `partition_out()`, `filter_in_place_hint()`, `remove_if_mark()` |
|  | `vector::erase()` | Invalidates iterators. | Hidden structural side effects. | `erase_and_invalidate()`, `delete_at()` |
|  | `push()` / `pop()` | Same verbs on incompatible containers. | Overloaded semantics across types. | `enqueue()/dequeue()`, `append()/take_last()` |
|  | `splice()` (JS) | Deletes, inserts, mutates in place. | Overloaded; multi-step behavior hidden. | `insert_at()`, `delete_at()`, `replace_range()` |
|  | `StringBuilder.append()` | Mutates shared buffer. | Hides aliasing/global side effects. | `append_mut()`, `concat_to()` |
| Construction & Conversion | `clone()` (Java) | Shallow copy. | Misleads about depth/safety. | `shallow_copy()`, `copy()` |
|  | `copy()` (Python list) | Shallow copy. | Misleading intuitive expectation. | `shallow_copy()`, `deep_copy()` |
|  | `new Date()` (JS) | Parse + timezone + object creation. | Overloaded behavior. | `Date.now()`, `Date.from_string()` |
|  | `from()` (Rust) | Conversion may be lossy/surprising. | Verb too broad. | `try_from()`, `convert()`, `coerce()` |
|  | `as` (C#/Rust) | Unchecked cast/coercion. | Looks benign; hides failure risk. | `unsafe_cast()`, `coerce_unchecked()` |
| Iteration & Control Flow | `next()` | Throws, blocks, or returns sentinel depending on lib. | Inconsistent behavior. | `try_next()`, `next_or_none()` |
|  | `hasNext()` | Breaks for fused/drained iterators. | Misleading state model. | `can_advance()`, `is_exhausted()` |
|  | `yield` | Divergent semantics across langs. | Inconsistent control-flow expectations. | (Language keyword—no replacement) |
|  | `wait()` | Requires lock discipline not expressed. | Hidden preconditions. | `wait_on(lock)`, `block_until()` |
|  | `notify()` | Nondeterministic wakeups. | Implies deterministic selection. | `signal_one()`, `signal_waiter()` |
|  | `notifyAll()` | Wakes all but doesn’t guarantee order. | Implies deterministic broadcast. | `broadcast()` |
| String Processing | `trim()` | ASCII-only in some libs. | Not Unicode-safe. | `trim_unicode()`, `strip()` |
|  | `split()` | Regex vs literal depends on lang. | High semantic inconsistency. | `split_regex()`, `split_literal()` |
|  | `substr()` (JS) | Differs from `substring()`. | Ambiguous, error-prone. | `slice()` |
|  | `replace()` | First/all occurrences depends on runtime. | Under-specified semantic scope. | `replace_first()`, `replace_all()` |
|  | `toString()` | Not canonical or reversible. | Imprecise, misleading. | `to_repr()`, `to_debug()` |
| Numerics & Randomness | `random()` | PRNG float; not secure. | Ambiguous domain; encourages misuse. | `random_uniform()`, `random_secure()` |
|  | `pow()` | Type coercions vary. | Violates type guarantees. | `pow_int()`, `pow_float()`, `exp_log()` |
|  | `abs()` | Overflow on minimum integers. | Misleading safety. | `abs_safe()`, `magnitude()` |
|  | `floorDiv()` | Non-Euclidean division. | Mathematical mismatch. | `euclid_div()`, `truncate_div()` |
| Concurrency | `Thread.stop()` | Abrupt kill. | Catastrophically unsafe. | `request_stop()`, `cancel()` |
|  | `async` (JS) | Rewrites semantics. | Name hides control-flow transformation. | (Keyword—no replacement) |
|  | `volatile` | Meaning varies across languages. | Semantic inconsistency. | `atomic_flag()`, `seq_cst()` |
|  | `mutex.lock()` | May block/deadlock. | Under-specified side effects. | `lock_or_error()`, `lock_blocking()` |
| Filesystem | `touch()` | Creates file AND updates timestamp. | Overloaded meaning. | `create_if_missing()`, `update_timestamp()` |
|  | `open()` | May create/truncate depending on flags. | Name hides destructive modes. | `open_read()`, `open_write()`, `open_create()` |
|  | `chmod()` | Mode representation unclear. | Representational opacity. | `set_permissions()` |
|  | `rm -f` | “Force” ignores errors. | Semantic inversion. | `remove_ignore_errors()` |
| Collections | `queue.pop()` (Python) | Returns item but doesn’t pop. | Inverts “pop.” | `get()`, `dequeue()` |
|  | `heapq.heappushpop()` | Combined push and pop. | Opaque concatenated semantics. | `push_then_pop()`, `replace_root()` |
|  | `list.sort()` | In-place, but name looks pure. | Mutation hidden. | `sort_in_place()`, `sorted_list()` |
|  | `Deque.remove()` | Removes first occurrence only. | Under-specified. | `remove_first()`, `delete_first()` |

### .unwrap

> Why it’s a bad name? `.unwrap` is a bad name because it **sounds safe while secretly causing a runtime crash if the value is missing, misleading developers and hiding risk**.
> 

> Alternative names are value_or_error(), unwrap_or_panic() ….
> 

## QA

### **Is there a truly collision-independent naming scheme?**

> A *collision-independent* naming scheme would guarantee **with absolute certainty** that two independently generated names can *never* be equal.
> 

> A Trully indepdent collifison free - is not possible - becuase the combinatinos of the elemnts names will be finite.
> 

| Scheme Type | Collision-Free? | Independent? | Case(s) |
| --- | --- | --- | --- |
| **Independent + Finite space** | ❌ No | ✔ Yes | UUIDv4, random IDs |
| **Independent + Infinite space** | ❌ No | ✔ Yes | Unbounded counters (but can overlap between generators) |
| **Coordinated + Finite/Infinite space** | ✔ Yes | ❌ No | DNS, distributed consensus |
| **Truly collision-independent** | 🚫 Impossible | — | — |

## References

- See `dns.md`
- [Names in Distributed Systems](https://www.cl.cam.ac.uk/teaching/0809/DistSys/5-naming.pdf)
- [Naming in Distributed Systems](https://dsg.tuwien.ac.at/linksites/teaching/courses/VerteilteSysteme/pdfs/ds-ws-2014-lecture4_naming_Truong.pdf)
- Tanenbaum & Van Steen, Distributed Systems: Principles and
- [Distributed Sequence Number Generation?](https://stackoverflow.com/questions/2671858/distributed-sequence-number-generation)
- [Domain Name Service (DNS)](note.html?n=technica/computation/telecom/domain-name-service-dns.md)
- [Reference](https://app.notion.com/p/Reference-1e4c0f5171ec80c5bb7bed49e387d528?pvs=21)
- [Name](note.html?n=technica/computation/language-system/conceptual-model-language-system/name.md)
- Cognition -  [Name](https://app.notion.com/p/Name-283c0f5171ec800ca9e0dce8f1f6b659?pvs=21)
- [How to name things?](https://app.notion.com/p/How-to-name-things-195c0f5171ec8034a452ea87863f653b?pvs=21)
- [https://www.sciencedirect.com/science/article/abs/pii/S0010028511000132](https://www.sciencedirect.com/science/article/abs/pii/S0010028511000132)
- Lawrie, D., Morrell, C., Feild, H., & Binkley, D. (n.d.). Whats in a Name? A Study of Identifiers. 14th IEEE International Conference on Program Comprehension (ICPC’06). doi:10.1109/icpc.2006.51
- Saltzer, J., Kaashoek, M. F. (2009). Principles of Computer System Design: An Introduction. Morgan Kaufmann.
- https://etcd.io/
- https://blog.cloudflare.com/18-november-2025-outage/