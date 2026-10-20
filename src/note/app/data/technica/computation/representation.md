# Representation

> This note explores one of the central ideas in computation: **representation**.
> 

> **Representation** can be defined as the way data, objects, or processes are encoded, structured, and manipulated within a computational system. It is the bridge between abstract concepts and their concrete realization in symbols, data structures, or physical states.
> 

QA:

- How do we represent “inner” elements — the system’s own structures, states, and processes?
- How do we represent “outer” elements — the environment, inputs, and entities beyond the system itself?
- What constraints do different representational schemes impose on what can be modeled or computed?
- Which  is the “technique space”  that aids Representation?
- How to think deeply about the representation - interaction agent (human, machine)?
    - Is it better to have many functions operating over a **small number of shared data structures**, or fewer functions tied to many **specialized data structures**?
    - Let’s clear the language a bit -  by  one **data structure** - we mean a type of data structure - and by specialized data structure we mean many types of data structures.

## Formulation

> How does representation function within a computational process?
> 

> A **representation** is a central part of any **computational process**—it provides the structure through which information is encoded, manipulated, and interpreted.
> 

> A **computational process** is guided by representations, which grant it a kind of operational awareness, and these representations transform as the process advances.
> 

> **Representations** may be permanent or ephemeral, existing either throughout the computation and beyond or only transiently.
> 

> A **representation domain** is the *category or class of data/phenomena* that a representational system encodes, structures, and manipulates.
> 

> **Representation Systems** are used to encode a particular data from a given domain.
> 

- What’s the function of representation in “Computational Systems”?
- Which used Representations?

## Representation System

> A **representation system** refers to a set of rules, symbols, or formats used to represent and encode information or knowledge in a computer or computational system. It defines how data is structured, organized, and stored, allowing the computer to manipulate, process, and interpret the represented information effectively.
> 

| **Category** | **Representation System** | **Target** | **Implementation** |
| --- | --- | --- | --- |
| **Data Encoding** | Binary | Represent raw digital data | Bits in memory, logic gates, CPU registers |
|  | Hexadecimal | Represent binary data compactly | Memory dumps, debugging tools, low-level programming |
|  | Base64 | Encode binary data for text transmission | Email, JSON, web APIs |
| **Textual Data** | ASCII | Represent basic English characters | Text files, string types in programming languages |
|  | Unicode / UTF-8 | Represent multi-language characters | Internationalized text processing, databases, web |
|  | Markdown / LaTeX | Represent formatted text or documents | Document processing, academic publishing |
| **Structured Data** | JSON | Represent hierarchical data | Web APIs, configuration files, programming libraries |
|  | XML | Represent tagged data with metadata | Data exchange, configuration, SOAP APIs |
|  | YAML | Represent human-readable structured data | DevOps configs, pipelines, application settings |
| **Visual Data** | Bitmap (Raster) | Represent pixel-based images | PNG, JPEG, GPU rendering, image editing software |
|  | Vector Graphics | Represent scalable images | SVG, CAD drawings, illustration tools |
|  | 3D Models | Represent 3D objects | OBJ, STL, game engines, 3D rendering software |
| **Mathematical Data** | Symbolic Notation | Represent formulas and algebraic expressions | Mathematica, SymPy, LaTeX |
|  | Numerical Arrays | Represent numerical computations | NumPy, MATLAB, tensors |
| **Knowledge Representation** | RDF Triples | Represent entities and relationships | Semantic web, SPARQL queries, graph databases |
|  | Ontologies (OWL) | Represent structured domain knowledge | Reasoners, knowledge graphs, AI knowledge bases |
|  | Concept Maps | Represent conceptual relationships | Educational software, mind mapping |
| **Audio Data** | PCM | Represent uncompressed audio | WAV files, audio buffers, digital audio hardware |
|  | MP3 / AAC | Represent compressed audio | Media players, streaming services, codecs |
|  | MIDI | Represent musical notes | Music software, synthesizers |
| **Temporal / Signal Data** | Time Series | Represent sequential data over time | Pandas, NumPy arrays, signal processing libraries |
|  | Sensor Signals | Represent readings from physical devices | IoT systems, DSP libraries, real-time monitoring |
| **Feature Representation** | Dense Embeddings | Represent features for ML tasks | Tensor libraries, feature vectors, NLP embeddings |
|  | Sparse Representations | Represent high-dimensional data efficiently | Sparse matrices, recommender systems, NLP |
| **Executable Instructions** | Source Code | Represent human-readable programs | Text files, IDEs, compilers |
|  | Bytecode | Represent platform-independent executable code | JVM, .NET CLR, interpreters |
|  | Machine Code | Represent CPU instructions | Executable binaries, CPU instruction sets |

## Technique Space

- Representation Invariant: …. Why not called it a Property? …
    - Constraint Technique
    - Validation Technique
    - Rule
    - Joint Invariant
    - Consistency
    - Boolean Function
- Encoding
    - Digital’s Numeric System
    - Symbolic Encoding
    - Sub Symbolic Encoding
    - Structure Encoding
- File Format
- Representation Transformation Technique
- Indexing
- Compression
- Augmentation
    - Error Detection & Correction Code
    - …
- Abstract Specification
- Security Technique
- Interoperability  Technique
- Redundancy Technique
- Versioning Technique

## Representation Principle

> "The Representation Principle: Once a problem is described using an appropriate representation, the problem is almost solved." -- P. H. Winston
> 

> "Rule 5: Data dominates. If you've chosen the right data structures and organized things well, the algorithms will almost always be self-evident. Data structures, not algorithms, are central to programming." -- Rob Pike
> 

> "What are tensors? The facts of the universe." -- Lillian
> 

> “Smart data structures and dumb code works a lot better than the other way around." -- Guy Steele
> 

> "Show me your [code] and conceal your [data structures], and I shall continue to be mystified. Show me your [data structures], and I won't usually need your [code]; it'll be obvious." -- Fred Brooks
> 
- **Invariants:** Properties that remain constant across transformations or operations (e.g., "The sum of inputs equals the sum of outputs" in a financial system).
- **Abstraction:** Hiding complex implementation details behind a simpler interface.
- **Encapsulation:** Bundling data and the methods that operate on it together.
- **Orthogonality:** Minimizing interactions between unrelated features in a representation.
- **Efficiency:** Balancing time (computation), space (storage), and communication overhead.
- **Expressiveness:** The ability of a representation to capture the necessary complexity and nuance of the domain.

## Property

> Which are the properties associated with representation of data?
> 

| **Property** | **Description** | **Values** | **Tag(s)** |
| --- | --- | --- | --- |
| Persistency | Determines whether data remains after program/system termination. | Ephemeral (volatile), Persistent (durable) | Logical, Systemic |
| Durability | Guarantees survival of committed data after crashes or power loss. | Durable, Non-durable | Logical, Systemic |
| Consistency | Ensures data satisfies structural/logical constraints. | Consistent, Inconsistent | Logical, Operational |
| Recoverability | Ability to restore a valid state after failure. | Recoverable, Unrecoverable | Logical, Systemic |
| Atomicity | Operations occur entirely or not at all. | Atomic, Non-atomic | Operational, Logical |
| Accessibility | How easily data can be located and retrieved. | Direct, Indexed, Sequential | Operational, Performance |
| Mutability | Whether stored data can be changed in place. | Mutable, Immutable | Logical, Structural |
| Portability | Degree to which data format is system-agnostic. | Platform-independent, Platform-dependent | Systemic, Physical |
| Scarcity | Ratio of filled to empty representational space. | Sparse, Dense | Structural, Physical |
| Structure Type | Arrangement of elements and their relationships. | Linear, Non-linear, Composite, Hybrid | Structural |
| Dimensionality | Number of independent access dimensions. | 1D, 2D, ND | Structural |
| Homogeneity | Whether all elements share the same type/schema. | Homogeneous, Heterogeneous | Structural, Semantic |
| Ordering | Whether sequence/arrangement of elements matters. | Ordered, Unordered, Partially ordered | Structural |
| Indexability | Whether elements can be accessed via identifiers or keys. | Indexable, Non-indexable | Operational, Structural |
| Cardinality | Number of elements or relationships. | Finite, Infinite, Bounded, Unbounded | Structural, Formal |
| Connectivity | Degree of explicit inter-element links. | Loose, Tight, Hierarchical, Networked | Structural |
| Cyclicity | Whether structures contain cycles. | Acyclic, Cyclic | Structural, Formal |
| Arity | Number of links per node. | Unary, Binary, n-ary, Variable | Structural |
| Recursiveness | Whether structure definition refers to itself. | Recursive, Non-recursive | Structural, Formal |
| Partitionability | Can structure be subdivided into independent parts. | Partitionable, Non-partitionable | Structural, Performance |
| Referential Integrity | Validity of internal references or pointers. | Maintained, Broken | Logical, Systemic |
| Complexity | Time/space complexity of basic operations. | O(1), O(log n), O(n) | Operational, Performance |
| Operation Set | Core supported operations. | Insert, Delete, Search, Traverse, Update | Operational |
| Idempotency | Whether repeated operations yield same result. | Idempotent, Non-idempotent | Operational, Formal |
| Determinism | Whether identical inputs yield identical states. | Deterministic, Non-deterministic | Operational, Formal |
| Concurrency Control | How simultaneous accesses are managed. | Lock-based, Lock-free, Transactional | Operational, Systemic |
| Concurrency Safety | Thread/process safety. | Thread-safe, Non-thread-safe | Operational, Performance |
| Consistency Model | Visibility rules for concurrent updates. | Strong, Eventual, Causal, Session | Operational, Systemic |
| Serializability | Can concurrent ops be viewed as sequential. | Serializable, Non-serializable | Operational, Systemic |
| Transactionality | Support for transactional semantics. | Transactional, Non-transactional | Operational, Systemic |
| Reentrancy | Safe re-invocation before completion. | Reentrant, Non-reentrant | Operational |
| Adaptivity | Self-reorganization under workload changes. | Adaptive, Static | Operational, Performance |
| Fault Tolerance | Ability to continue after partial failure. | Fault-tolerant, Fragile | Systemic, Performance |
| Memory Layout | How elements are arranged in memory. | Contiguous, Linked, Paged | Physical |
| Alignment | Conformity to word or cache boundaries. | Aligned, Misaligned | Physical, Performance |
| Endianness | Byte order of multi-byte elements. | Little-endian, Big-endian | Physical |
| Compression | Data footprint reduction strategy. | Lossless, Lossy, None | Physical, Performance |
| Fragmentation | Degree of space inefficiency from allocation. | Low, High | Physical, Performance |
| Cacheability | How well it exploits CPU cache hierarchy. | Cache-friendly, Cache-unfriendly | Physical, Performance |
| Spatial Locality | Access of nearby memory locations. | High, Low | Physical, Performance |
| Temporal Locality | Reuse of recently accessed data. | High, Low | Physical, Performance |
| Serialization Format | Representation for I/O or transmission. | Binary, Textual (JSON, XML), Custom | Physical, Systemic |
| Alignment Granularity | Minimum unit of atomic access. | Byte, Word, Block | Physical |
| Paging Behavior | Interaction with virtual memory. | Page-resident, Paged-out | Physical, Performance |
| Memory Overhead | Extra metadata/pointer cost per element. | Low, Medium, High | Physical, Performance |
| Block Size (Granularity) | Fundamental physical storage unit. | Fixed, Variable | Physical |
| Data Locality Model | Distribution across nodes/disks. | Local, Distributed, Sharded | Systemic, Performance |
| Throughput | Operations per second under workload. | Low, Medium, High | Performance |
| Latency | Time per operation. | Low, Moderate, High | Performance |
| Scalability | Performance with increasing data or concurrency. | Scalable, Non-scalable | Performance, Systemic |
| Elasticity | Ability to grow/shrink resources dynamically. | Elastic, Rigid | Performance, Systemic |
| Parallelizability | Can be decomposed into parallel tasks. | High, Moderate, Low | Performance |
| Load Balancing | Evenness of workload distribution. | Balanced, Skewed | Performance, Systemic |
| Bottleneck Sensitivity | Tendency to degrade due to single-point limits. | Low, High | Performance |
| I/O Efficiency | Suitability for disk/network operations. | I/O-optimized, Memory-optimized | Performance |
| Energy Efficiency | Power cost per operation. | Efficient, Inefficient | Performance |
| Abstraction Level | Conceptual level of structure. | Concrete, Abstract | Semantic |
| Interpretability | Ease of human understanding of content/semantics. | High, Low | Semantic |
| Symbolic Density | Information per representational unit. | High, Low | Semantic |
| Expressiveness | Range of concepts representable. | Expressive, Limited | Semantic |
| Representation Invariance | Whether different encodings preserve semantics. | Invariant, Variant | Semantic |
| Schema Evolution | Ability to evolve structure without breaking compatibility. | Flexible, Rigid | Semantic, Systemic |
| Extensibility | Ease of adding new attributes or fields. | Extensible, Closed | Semantic, Systemic |
| Validation Strictness | Enforcement of semantic constraints. | Strict, Weak, None | Semantic |
| Composability | Ability to embed into larger abstractions. | Composable, Isolated | Semantic |
| Polymorphism | Whether same operations apply to different types. | Polymorphic, Monomorphic | Semantic |
| Versioning | Tracks history or revisions. | Versioned, Non-versioned | Systemic |
| Synchronization | Coordination across replicas/nodes. | Synchronous, Asynchronous | Systemic |
| Replication | Number of stored copies for redundancy. | Single, Replicated, Sharded | Systemic |
| Distribution | Spread across multiple nodes or sites. | Centralized, Distributed, Federated | Systemic |
| Migration | Ease of moving data between systems. | Portable, Static | Systemic |
| Audibility | Traceability of changes. | Auditable, Opaque | Systemic |
| Security | Protection against unauthorized access. | Encrypted, Plain, Access-controlled | Systemic |
| Integrity Checking | Mechanisms to verify correctness. | Checksums, Hashes, Signatures | Systemic |
| Lifecycle Stage | Current operational phase. | Creation, Active, Archived, Deleted | Systemic |
| Compliance | Adherence to standards/regulations. | Compliant, Non-compliant | Systemic |
| Closure | Whether operations yield same type. | Closed, Non-closed | Formal |
| Isomorphism | Existence of structure-preserving bijection. | Isomorphic, Non-isomorphic | Formal |
| Completeness | Whether structure captures all valid states. | Complete, Incomplete | Formal |
| Well-Foundedness | Whether no infinite descending chains exist. | Well-founded, Non-well-founded | Formal |
| Idempotent Operations | Whether repeated operations stabilize state. | Yes, No | Formal |
| **Balanced** | A **Balanced Data Structure** maintains elements evenly (e.g., balanced tree) to guarantee efficient operations like search, insert, delete, usually in logarithmic time complexity. | Balanced, Unbalanced | Structural, Performance, Formal |

## In-Memory Data Structure

> See more in [In-Memory Representation](note.html?n=technica/computation/representation/conceptual-model-computational-representation/in-memory-representation.md).
> 

## Disk Data Structure

> How to represent data outside memory?
> 

> See more in [Out-Memory Data Structure](note.html?n=technica/computation/representation/conceptual-model-computational-representation/out-memory-data-structure.md).
> 

> See https://en.wikipedia.org/wiki/External_memory_algorithm
> 

| **Technique** | **Description** | **Use** |
| --- | --- | --- |
| **B-Tree** | Balanced hierarchical index optimized for block-based storage; minimizes disk I/O by grouping keys within pages. | Used in database indexes, filesystem directories, and metadata structures (e.g., NTFS, HFS+). |
| **Journal (Write-Ahead Log, WAL)** | Sequential log recording all intended changes before committing them to main storage; ensures atomicity and recoverability. | Used in journaling filesystems (ext4, NTFS) and databases (PostgreSQL, SQLite) for crash consistency. |
| **Log-Structured File Structure** | Treats the entire disk as an append-only log; writes are batched and sequential to minimize random I/O and simplify recovery. | Used in SSD-optimized systems like LFS and F2FS, improving write performance and durability. |
| **File Format** | Structured layout defining how data, metadata, and relationships are stored within a single file. Determines parsing, portability, and I/O efficiency. | Used in document storage, media containers, and serialized database files (e.g., CSV, Parquet, SQLite file). |

## Conceptual Model

Conceptual Model: Computational Representation

## QA

### How to think deeply about the representation - interaction agent (human, machine)?

> Is it better to have many functions operating over a **small number of shared data structures**, or fewer functions tied to many **specialized data structures**?
> 

> Let’s clear the language a bit -  by  one **data structure** - we mean a type of data structure - and by specialized data structure we mean many types of data structures.
> 

- This appears to be a false dichotomy: forcing an ill-suited specialized data structure to model a state can conflict with human cognition and lead to semantic distortion.
- Having a representation scheme such as JSON does not imply unstructured data; rather, it defines a structured, hierarchical format with well-defined compositional rules.
- A unified representation scheme like JSON can function as a common substrate over which richer semantic structures and transformations can be defined, enabling composability and reuse across systems - is **algebraic representational scheme.**
- The key insight is that a rich algebra over a shared representation often scales more effectively than isolated, incompatible representational “islands” of bespoke structure.
- Decision Principle:
    - Is this representation scheme - representations are go in to be  widely used?
    - Will it be used to interact with other machines?
    - When does this representation scheme show its limits, and where does it become too restrictive or overly constrained?

## References

- [Property](https://app.notion.com/p/Property-271c0f5171ec80498865e3db652beafb?pvs=21)
- [Representation](https://app.notion.com/p/Representation-4afbffa763ec46eeb10d8c87c248edf1?pvs=21)
- https://en.wikipedia.org/wiki/Data_structure
- https://gist.github.com/dbremont/914cdbcf861238742ea1d41c7bf0d08e#file-courses-md
- https://en.wikipedia.org/wiki/Computer_number_format
- [Conflict-free Replicated Data Type (**CRDT**)](note.html?n=technica/computation/concurrency/conceptual-model-coordination/conflict-free-replicated-data-type-crdt.md)
- https://en.wikipedia.org/wiki/Comparison_of_data-serialization_formats
- Piantadosi, S. T. (2021). The computational origin of representation. 31(1), 1.