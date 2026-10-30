---
tags: [representation, technique]
qa:
  - How do we represent “inner” elements — the system’s own structures, states, and processes?
  - How do we represent “outer” elements — the environment, inputs, and entities beyond the system itself?
  - What constraints do different representational schemes impose on what can be modeled or computed?
  - Which is the “technique space” that aids Representation?
  - How to think deeply about the representation–interaction agent (human, machine)?
  - Is it better to have many functions operating over a small number of shared data structures, or fewer functions tied to many specialized data structures?
---

# Representation

> This note explores one of the central ideas in computation: **computational representation**.

> **Representation** is the way data, objects, or processes are encoded, structured, and manipulated within a computational system. It is the bridge between abstract concepts and their concrete realization in symbols, data structures, or physical states.

> The note proceeds in the order the technica guide fixes: bind the instance, type it, test the typing, decompose it, evaluate the concept. The scheme inventory, the technique space, and the property catalogue below are the note's model, kept as catalogues that the decomposition points at.

## Formulation

### What is this technical instance?

> A **computational representation** is a *structure-carrying encoding realized in a computationally manipulable carrier*: a triple ⟨domain *D*, carrier *C*, encoding *e: D → C*⟩ together with a decoding *d: C → D*, such that the operations the practice actually performs commute — for every operation *f* the practice needs on *D*, some operation *g* on *C* satisfies *d(g(e(x))) = f(x)*.

> Fidelity is therefore operation-relative, never absolute. A representation is faithful exactly up to the diagrams it makes commute, and **lossy** names the squares that fail: JPEG drops detail the visual system is unlikely to miss, IEEE 754 drops exact reals beyond its significand, UTF-8 drops nothing but pays in code units. "Faithful" without a named operation set is not a claim but a slogan.

> The word *computational* does the scoping work: the carrier must admit effective operations — construction, storage, comparison, transformation — that a machine can perform. A painted portrait, a mental image, or a physical scale model becomes a computational representation only when it is inscribed in a computable carrier. The scope excludes exactly the cases that would otherwise make the term vacuous.

> Four things are routinely called "a representation" and must be kept apart: the **scheme** (the rules: JSON, UTF-8, IEEE 754), the **artifact** (the encoded datum: this file, this byte string), the **map** (the encoder and decoder pair), and the **relation** (the commuting square that makes the other three a representation). The definition names the relation; the catalogues below name schemes and artifacts.

> A **representation system** — the informal register for the scheme — is a set of rules, symbols, or formats used to encode information in a computational system; it fixes how data is structured, organized, and stored, and therefore what can be manipulated, compared, and interpreted. **Representations may be permanent or ephemeral**: a persisted file outlives the process, a stack frame does not, and persistence changes the cost of a fidelity failure but not its nature.

### What technical element type does this technical instance belong to?

**Computational Representation belongs to the `Technical Element Set` technical element type — `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set — readable as `Technical Mechanism` and, where a scheme is standardized, as a `Technical Standard`.**

```text
Technical Element
└── (→ Kind) Technical Element Set
    └── (→ Instance) Computational Representation Set (the schemes, the carriers, and the practice that builds them)
        (→ Governed By) Technical Standard  — the standardized specimens: IEEE 754, UTF-8, JSON
        (→ Kind) Technical Mechanism        — the encoding arrangement: carrier, encoder, decoder
        readable as Technical Interface     — the encode-decode boundary
```

It is a set because the note's subject is an ensemble rather than one artifact: the scheme family, the standardized specimens, the carriers that host them, the specifications that fix them, and the practice that builds and maintains them. What holds the ensemble together is one technical object — the encoded carrier — and one function — structure carried across a boundary. A scheme *implements* the encoding arrangement, the arrangement is typed as a `Technical Mechanism` and gets its own root, an encoded artifact *realizes* both, and a published standard *specifies* one.

> **Caution.** "Representation" is not a kind of object. Nothing is a representation intrinsically; a byte string is one only under an encoding relation. The type attribution is to the ensemble and to the arrangement, never to the carrier alone.

### Is the type of this `technical element instance` ambiguous?

Yes, and the ambiguity is between genuinely different technical elements:

- **Mechanism** — the arrangement: carrier plus encoder, decoder, and the operations that preserve the needed diagrams.
- **Element Set** — the family of schemes and their ecosystem: JSON, XML, Protobuf, IEEE 754, UTF-8, and the data structures that carry them.
- **Standard** — the normative documents that fix a scheme's grammar and canonical form (RFC 8259, IEEE 754-2019, RFC 3629).
- **Interface** — the encode-decode boundary through which one practice hands structure to another.

The guide's default for a multi-typed instance is multi-root decomposition, and this note **keeps the ambiguity instead of resolving it**: the ensemble reading (`Technical Element Set`) and the arrangement reading (`Technical Mechanism`) are both legitimate, because the note carries the practice of building representations alongside the representations themselves. The forest below therefore has two roots — the set root first, since the note's subject is the ensemble, and the mechanism root second, for the arrangement and its attributes. The `Technical Standard` reading appears as a branch; the `Technical Interface` reading stays prose.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this forest decomposes one vendor-neutral computational representation twice — as an ensemble (`Technical Element Set`: the schemes, the standards, the carriers, the specifications, the practice that produces them, and what they enable) and as an arrangement (`Technical Mechanism`: the domains it carries, the principles, constraints, parameters, and interfaces that fix it, and the qualities, tensions, failures, and checks that judge it). Named formats and measured values appear only as leaves; the full scheme inventory and the property catalogue stay in the sections below.

> Stopping rule: a row is terminal when it names a concrete scheme, a named standard, a carrier structure, a technique, or a check that a practice runs.

> Identity: the Instance Tree Path is the stable identifier of each row; every path in this table is unique.

> Links: every path starts at `Technical Element` and every link names its relationship type — `Kind` down the type chain, `Instance` onto an instance, and `Has`, `Governed By`, `Constrained By`, `Evaluated By`, `Maintained By`, `Enables`, `Acts On`, `Evolves Through` for the branch relationships. No bare arrow remains.

> Verbs: a scheme *implements* the mechanism; an encoded artifact *realizes* it; a standard *specifies* it; a carrier *hosts* it.

| Instance Tree Path | Description |
| --- | --- |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set | Structure-carrying encoding read as an ensemble: the schemes, the standardized specimens, the carriers that host them, the specifications that fix them, and the practice that builds and maintains them. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` | Grouping: the scheme family — the instances that would otherwise hang untyped under the ensemble. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Data Encoding Scheme Set | Raw digital data: bits, notation, and transport alphabets. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Data Encoding Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode raw digital data. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Data Encoding Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Binary Encoding | Raw bits as the universal carrier underneath every other scheme. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Data Encoding Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Hexadecimal Notation | Two characters per byte for dumps, addresses, and debuggers. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Data Encoding Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Base64 Encoding | Six-bit alphabet carrying binary over text-only channels. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Textual Scheme Set | Characters and documents. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Textual Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode characters and documents. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Textual Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` ASCII | Seven-bit character set for basic Latin text. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Textual Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Unicode | Coded character set spanning the world's scripts. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Textual Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Markdown | Plain-text document markup readable as written. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Textual Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` LaTeX | Typesetting markup for mathematical and structured documents. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set | Records, trees, and tables. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode records, trees, and tables. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` JavaScript Object Notation (JSON) | Textual hierarchical values, the default interchange scheme. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Extensible Markup Language (XML) | Tagged tree with attributes and namespaces. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` YAML | Indentation-based configuration data. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Comma-Separated Values (CSV) | Delimited tabular rows with a header convention rather than a schema. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Protocol Buffers (Protobuf) | Schema-driven binary messages with generated accessors. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` MessagePack | Compact binary object notation. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Structured Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Apache Avro | Schema-carrying record serialization for data pipelines. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Visual Data Scheme Set | Images and geometry. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Visual Data Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode images and geometry. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Visual Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Raster Bitmap | Pixel grid with a colour model and a sampling lattice. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Visual Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Vector Graphics | Paths, shapes, and transforms, resolution-independent by construction. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Visual Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` 3D Mesh | Vertices, faces, and materials describing a solid. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Mathematical Scheme Set | Formulas and arrays. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Mathematical Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode formulas and arrays. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Mathematical Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Symbolic Notation | Expressions as trees of operators and operands. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Mathematical Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Numerical Array | Dense n-dimensional numbers with a dtype and a shape. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Mathematical Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Tensor Layout | Strided multidimensional storage, the carrier under array and array-like schemes. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Knowledge Scheme Set | Entities and relations. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Knowledge Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode entities and relations. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Knowledge Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` RDF Triple | Subject-predicate-object statements forming a graph. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Knowledge Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` OWL Ontology | Class and property axioms supporting inference. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Knowledge Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Concept Map | Labelled concepts joined by typed relations. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Audio Scheme Set | Sound, sampled and symbolic. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Audio Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode sound. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Audio Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` PCM | Sampled waveform: amplitude quantized on a fixed clock. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Audio Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` MP3 | Perceptual audio coding discarding masked detail. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Audio Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` MIDI | Symbolic musical events rather than a waveform. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Temporal Data Scheme Set | Time-indexed values. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Temporal Data Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode time-indexed values. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Temporal Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Time Series | Ordered observations with a time index and a fixed sampling rule. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Temporal Data Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Sensor Signal | Sampled physical measurements with units and calibration. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Feature Scheme Set | Engineered and learned features. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Feature Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode features. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Feature Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Dense Embedding | Fixed-width learned vector standing in for an object. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Feature Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Sparse Representation | Mostly-zero high-dimensional vector, cheap to store and compare. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Executable Scheme Set | Instructions. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Executable Scheme Set `(→ Has)` `Technical Mechanism` | Grouping: mechanisms that encode instructions. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Executable Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Source Code | Human-written program text. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Executable Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Bytecode | Portable instruction stream for a virtual machine. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Element Set` `(→ Instance)` Executable Scheme Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Machine Code | Native instruction encoding for a named instruction set. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` | Grouping: standardized schemes. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` IEEE 754 | Binary floating-point interchange: sign, exponent, significand, and the rounding rules that make results reproducible. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` UTF-8 | Variable-width Unicode encoding whose code units never collide with ASCII. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` JavaScript Object Notation (JSON) | Textual hierarchical values with a small grammar and a wide implementation base. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` Extensible Markup Language (XML) | Tagged trees with attributes, namespaces, and schema languages. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` Protocol Buffers (Protobuf) | Schema-driven binary messages compiled into typed accessors. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` MessagePack | Compact binary object notation preserving the JSON data model. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` Apache Parquet | Columnar file format carrying schema, encodings, and column statistics. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` JPEG | Lossy image coding by block transform, quantization, and entropy coding. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Standard` `(→ Instance)` WebP | Image coding offering lossy and lossless modes over the same container. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` | Grouping: the carriers that host the encoded structure. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier | Grouping: carriers realized in working memory. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` | Grouping: carrier mechanisms realized in working memory. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Contiguous Array | Elements at a fixed stride, addressable by arithmetic. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Linked Structure | Nodes joined by references, cheap to splice and costly to scan. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Hash Table | Keyed buckets reached through a hash function. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Balanced Tree | Ordered nodes with bounded height, so search stays logarithmic. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Trie | Prefix-indexed characters or paths, sharing common beginnings. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Graph Structure | Vertices with arbitrary adjacency. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Succinct Data Structure | Compressed layout supporting rank and select without decompression. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Probabilistic Data Structure | Approximate membership or counts in bounded space. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Concurrent Map | Keyed access shared across threads under a stated consistency rule. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Iterator | Access discipline over a sequence, decoupled from its layout. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Stream | Bounded-memory access over a sequence that may never end. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Out-Of-Memory Carrier | Grouping: carriers realized outside working memory. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Out-Of-Memory Carrier `(→ Has)` `Technical Mechanism` | Grouping: carrier mechanisms realized outside working memory. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Out-Of-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` B-Tree Index | Block-aligned hierarchy minimizing reads from secondary storage. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Out-Of-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Write-Ahead Log | Append-only record of intended changes written before they land. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` Out-Of-Memory Carrier `(→ Has)` `Technical Mechanism` `(→ Instance)` Log-Structured Store | Append-only segments compacted in the background. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Specification` | Grouping: specifications that fix a scheme. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Specification` `(→ Instance)` Format Grammar | Productions deciding which carriers are well-formed. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Specification` `(→ Instance)` Schema Definition | Declared shape of one payload: types, required fields, cardinality. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Specification` `(→ Instance)` Canonical Encoding Rule | Rule selecting one representative among carriers that decode alike. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Governed By)` `Technical Specification` `(→ Instance)` Round-Trip Contract | The guarantee that decoding an encoded value returns an equivalent value. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` | Grouping: the organized work of building and maintaining representations. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice | Grouping: the organized work that produces and maintains representations. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` | Grouping: the tasks that make up the practice. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Scheme Selection | Deciding which scheme a domain and an operation set call for. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Scheme Selection `(→ Has)` `General Technique` | Grouping: techniques for choosing a scheme. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Scheme Selection `(→ Has)` `General Technique` `(→ Instance)` Candidate Scheme Comparison | Weighing fidelity, cost, readability, and interoperability before committing. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Encoding | Writing domain structure into the carrier. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Encoding `(→ Has)` `General Technique` | Grouping: techniques that write structure into the carrier. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Encoding `(→ Has)` `General Technique` `(→ Instance)` Bit-Level Encoding | Placing values at fixed positions and widths. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Encoding `(→ Has)` `General Technique` `(→ Instance)` Structural Encoding | Turning records, sequences, and links into layouts. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Encoding `(→ Has)` `General Technique` `(→ Instance)` Symbolic Encoding | Naming values with discrete symbols and a grammar. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Encoding `(→ Has)` `General Technique` `(→ Instance)` Sub-Symbolic Encoding | Distributing a value over continuous coordinates. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Decoding | Recovering domain structure from the carrier. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Decoding `(→ Has)` `General Technique` | Grouping: techniques that recover structure from the carrier. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Decoding `(→ Has)` `General Technique` `(→ Instance)` Parsing | Recognizing grammar and building structure from a token stream. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Decoding `(→ Has)` `General Technique` `(→ Instance)` Deserialization | Materializing typed records from a carrier according to a schema. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Compaction | Buying footprint with compute or fidelity. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Compaction `(→ Has)` `General Technique` | Grouping: techniques that trade footprint for compute or fidelity. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Compaction `(→ Has)` `General Technique` `(→ Instance)` Run-Length Encoding | Replacing repeated values with counts. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Compaction `(→ Has)` `General Technique` `(→ Instance)` Dictionary Coding | Replacing repeated tokens with short indexes. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Compaction `(→ Has)` `General Technique` `(→ Instance)` Entropy Coding | Assigning shorter codes to likelier symbols. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Compaction `(→ Has)` `General Technique` `(→ Instance)` Transform Coding | Decorrelating values before quantizing them. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Compaction `(→ Has)` `General Technique` `(→ Instance)` Quantization | Discarding distinctions below a stated tolerance. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Indexing | Adding access structure over a carrier. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Indexing `(→ Has)` `General Technique` | Grouping: techniques that add access structure over a carrier. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Indexing `(→ Has)` `General Technique` `(→ Instance)` Hash Indexing | Building direct access through a hash function. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Indexing `(→ Has)` `General Technique` `(→ Instance)` Tree Indexing | Building ordered access with logarithmic search. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Indexing `(→ Has)` `General Technique` `(→ Instance)` Prefix Indexing | Sharing key prefixes to shorten lookup. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Augmentation | Adding structure that the payload would otherwise carry implicitly. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Augmentation `(→ Has)` `General Technique` | Grouping: techniques that add redundancy or implicit structure. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Augmentation `(→ Has)` `General Technique` `(→ Instance)` Error Detection Coding | Adding redundancy that exposes corruption. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Augmentation `(→ Has)` `General Technique` `(→ Instance)` Error Correction Coding | Adding redundancy that repairs corruption. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Interoperation | Moving structure between schemes and versions. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Interoperation `(→ Has)` `General Technique` | Grouping: techniques that move structure between schemes and versions. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Interoperation `(→ Has)` `General Technique` `(→ Instance)` Transcoding | Rewriting one carrier into another while preserving the operation set. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Interoperation `(→ Has)` `General Technique` `(→ Instance)` Canonicalization | Reducing all equivalent carriers to one representative. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Technical Task` `(→ Instance)` Interoperation `(→ Has)` `General Technique` `(→ Instance)` Version Negotiation | Choosing a mutually understood schema revision before exchanging carriers. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Constitutive Technique` | Grouping: techniques embodied in the practice itself. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Constitutive Technique` `(→ Instance)` Round-Trip Discipline | Holding the encoder and decoder to the same operation set, so encode then decode is the identity where it must be. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Practice` `(→ Instance)` Computational Representation Practice `(→ Has)` `Constitutive Technique` `(→ Instance)` Invariance Maintenance | Keeping the scheme's semantics fixed while its carriers, versions, and implementations change. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Enables)` `Technical Capability` | Grouping: what the mechanism makes possible. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Enables)` `Technical Capability` `(→ Instance)` Semantic Preservation Capability | Structure can cross a boundary — memory to disk, process to process, vendor to vendor — and remain operable on the far side. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Maintenance` | Grouping: work that keeps representations usable. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Maintenance` `(→ Instance)` Schema Migration | Moving stored carriers onto a new structure while preserving the operation set. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Maintenance` `(→ Instance)` Format Migration | Replacing a scheme with its successor across an installed base. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Maintained By)` `Technical Maintenance` `(→ Instance)` Re-Encoding Pass | Rewriting carriers to restore canonical form or recover lost compaction. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Evolves Through)` `Technical Evolution` | Grouping: historical change in schemes and carriers. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Evolves Through)` `Technical Evolution` `(→ Instance)` Numeric Encoding Lineage | BCD to IEEE 754 to bfloat16 and the narrow floating formats, each trading range and precision for throughput. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Evolves Through)` `Technical Evolution` `(→ Instance)` Character Encoding Lineage | ASCII to the ISO 8859 family to Unicode and UTF-8, each widening the repertoire and paying in code units. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Evolves Through)` `Technical Evolution` `(→ Instance)` Exchange Format Lineage | CSV to XML to JSON to schema-driven binary formats, trading readability for size and typing. |
| `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Evolves Through)` `Technical Evolution` `(→ Instance)` Learned Representation Shift | Hand-engineered feature schemes giving way to embeddings and latent vectors, where the encoding relation is fitted rather than specified. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism | The same encoding read as an arrangement: the domains it carries, the principles, constraints, parameters, and interfaces that fix it, and the qualities, tensions, failures, and checks that judge it. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` | Grouping: the domains whose structure is carried. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` `(→ Instance)` Numeric Domain | Reals, integers, and fixed-point quantities, encoded under a numeric format. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` `(→ Instance)` Textual Domain | Characters, strings, and documents, encoded under a character set and a markup. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` `(→ Instance)` Structural Domain | Records, collections, and hierarchies: the shapes a program manipulates. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` `(→ Instance)` Relational Domain | Entities and typed links, encoded as graphs, tables, or triples. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` `(→ Instance)` Spatial Domain | Images, geometry, and three-dimensional scenes. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` `(→ Instance)` Temporal Domain | Sequences, signals, and time series indexed by time or order. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` `(→ Instance)` Audio Domain | Sampled waveforms and symbolic musical events. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Acts On)` `Technical Domain Reality Model` `(→ Instance)` Executable Domain | Programs and their instructions: source, bytecode, machine code. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Governed By)` `Technical Principle` | Grouping: principles the mechanism obeys. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Governed By)` `Technical Principle` `(→ Instance)` Structure Before Algorithm | Pike and Brooks: choose the carrier so the intended operations are cheap and the code becomes obvious. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Governed By)` `Technical Principle` `(→ Instance)` Representation Invariance | Re-encoding without losing the needed operations leaves the practice unchanged; if it does not, the scheme was carrying semantics. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Governed By)` `Technical Principle` `(→ Instance)` Compositional Closure | Encoded values compose into encoded values of the same scheme, so larger structures need no new mechanism. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Governed By)` `Technical Principle` `(→ Instance)` Carrier And Interpretation Separation | The carrier fixes structure only; units, meaning, and permitted operations come from the consuming practice. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Governed By)` `Technical Principle` `(→ Instance)` Canonical Equality | One value, one encoding, so equality on the carrier decides equality on the domain. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Governed By)` `Technical Principle` `(→ Instance)` Representation Principle | Winston: describe the problem in the right representation and the solution is nearly given. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Constraint` | Grouping: bounds the mechanism operates under. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Constraint` `(→ Instance)` Information-Loss Bound | What the carrier's value set cannot express; every lossy scheme is lossy against this bound. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Constraint` `(→ Instance)` Carrier Capacity | Bits, code units, or cells the carrier offers per element. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Constraint` `(→ Instance)` Encoding Cost | Time and space paid by encoding, decoding, and comparison. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Constraint` `(→ Instance)` Interpretation Requirement | Every scheme needs a reader; a carrier without a decoder carries nothing. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Constraint` `(→ Instance)` Compatibility Window | Range of producer and consumer versions a scheme spans without transcoding. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Parameter` | Grouping: parameters that fix a scheme's realization. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Parameter` `(→ Instance)` Bit Width | Width of the numeric or code unit the scheme fixes. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Parameter` `(→ Instance)` Byte Order | Byte sequence within a multi-byte unit, little- or big-endian. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Parameter` `(→ Instance)` Precision Allocation | Split of a fixed budget between significand and exponent. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Parameter` `(→ Instance)` Schema Version | Declared revision of the structure the carrier implements. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Parameter` `(→ Instance)` Canonicalization Mode | Whether the encoder emits one canonical form or any equivalent form. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Interface` | Grouping: boundaries of the mechanism. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Interface` `(→ Instance)` Encode-Decode Boundary | Where domain structure becomes carrier structure and back. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Interface` `(→ Instance)` Wire Boundary | Transmission boundary: framing, framing overhead, and the byte-level contract. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Interface` `(→ Instance)` Human-Read Boundary | Where a human reads the carrier directly, as with markdown, LaTeX, or a JSON config file. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` | Grouping: determinations about a representation. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Verification` | Grouping: conformance checks. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Verification` `(→ Instance)` Round-Trip Fidelity Check | Encoding and decoding returns an equivalent value over the declared operation set. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Verification` `(→ Instance)` Canonical Form Check | Every equivalent value maps to the one representative the scheme declares. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Verification` `(→ Instance)` Schema Conformance Check | The carrier satisfies the grammar and the declared schema. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Verification` `(→ Instance)` Cross-Decoder Parity Check | Independent decoders accept the carrier and agree on its value. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Validation` | Grouping: adequacy checks. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Validation` `(→ Instance)` Semantic Adequacy Assessment | The preserved operation set is the one the practice actually needs. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Validation` `(→ Instance)` Downstream Task Metric | The representation carries enough structure for the task that consumes it. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Validation` `(→ Instance)` Human Interpretability Assessment | A reader can recover the domain structure from the carrier unaided. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Evaluated By)` `Technical Evaluation` `(→ Kind)` `Validation` `(→ Instance)` Interoperability Acceptance Test | Independent producers and consumers exchange carriers without transcoding. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Trade-off` | Grouping: tensions the mechanism resolves. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Trade-off` `(→ Instance)` Fidelity Versus Compactness | Exact carriers cost bits; cheap carriers drop distinctions. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Trade-off` `(→ Instance)` Readability Versus Density | Textual schemes stay inspectable and pay in size and parse cost. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Trade-off` `(→ Instance)` Generality Versus Efficiency | Shared general schemes compose widely and specialize poorly. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Trade-off` `(→ Instance)` Stability Versus Evolvability | A frozen grammar keeps old readers working and blocks new structure. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Constrained By)` `Technical Trade-off` `(→ Instance)` Uniformity Versus Specialization | Few shared carriers with many operations, or many tailored carriers with few. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Failure` | Grouping: states in which the representation does not deliver. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Failure` `(→ Instance)` Information Loss | The carrier cannot express a distinction the domain has. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Failure` `(→ Instance)` Precision Loss | A representable distinction is rounded away by a finite budget. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Failure` `(→ Instance)` Encoding Ambiguity | Several carriers decode alike, so equality and hashing stop deciding. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Failure` `(→ Instance)` Schema Drift | Producer and consumer disagree about the structure the carrier implements. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Failure` `(→ Instance)` Decode Fault | The carrier is malformed or the decoder is wrong, and structure is not recovered. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Property` | Grouping: characteristics attributable to a representation. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Property` `(→ Instance)` Representational Fidelity | How much of the needed operation set survives the round trip. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Property` `(→ Instance)` Compactness | Bits, bytes, or cells per unit of domain structure. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Property` `(→ Instance)` Canonicality | Whether equivalent values share one carrier form. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Property` `(→ Instance)` Portability | Whether the scheme survives a change of platform, language, or vendor. |
| `Technical Element` `(→ Kind)` `Technical Mechanism` `(→ Instance)` Computational Representation Mechanism `(→ Has)` `Technical Property` `(→ Instance)` Schema Evolvability | Whether the structure can change without breaking existing carriers. |

### What is a critical conceptual evaluation of this `technical element instance`?

> **Concept under evaluation:** *Computational Representation*, under the precising definition declared above — a structure-carrying encoding ⟨*D*, *C*, *e*, *d*⟩ over a computationally manipulable carrier, faithful exactly over the operations whose diagrams commute. Criteria and ratings follow the *Philosophia Conceptuum et Operis*.

> **Verdict.** The scope word is the concept. Stripped of *computational*, "representation" is a role: anything can represent anything under some encoding, and the term then names the carrier, the scheme, the map, and the relation indifferently. With the scope and the commuting-square criterion the concept becomes checkable — a candidate is a computational representation of *D* exactly when a named operation set survives encoding and decoding.

> **Verdict.** The typing carries the same diagnosis. The subject cannot be given a single root without loss, because "representation" names a role that an arrangement, an ensemble of schemes, an artifact, and a standard can each play. The forest keeps both roots rather than electing one and calling the rest prose.

> **Verdict.** The definition is exact where the note's inherited tables are loose. The scheme inventory lists schemes and targets, the property catalogue lists carrier attributes; neither states the relation that makes them representations. The leakage follows: a data structure, a file format, a serialized record, a model's latent vector, and a JPEG all receive the same noun while carrying quite different guarantees.

> **Verdict.** As a design primitive the concept is Purpose-adequate and operationally strong; as an account of meaning it is not. Encoding and decoding fix structure, never interpretation: bytes become a temperature only inside a practice that supplies units, permitted operations, and error tolerance. "Data dominates" compresses this into a heuristic — choose the carrier so the intended operations are the cheap ones — not into a law.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| Conceptual Identification | Moderate | The scope word separates computational from painted or mental representations, but the noun still covers the scheme, the artifact, the map, and the relation, and the note must say which it means at each use. |
| Definitional Clarity | Strong at the core | Domain, carrier, encoder, decoder, and the commuting-square criterion are explicit and checkable; the informal register ("the way data is encoded") is not. |
| Conceptual Determinacy | Moderate | Membership is decided by an operation set: name the operations and borderline cases resolve — a cached object, a learned embedding, a compressed archive. Leave the operations unnamed and nothing resolves. |
| Definitional Completeness | Moderate | The definition states what makes something a representation but not what disqualifies it; the exclusions — no decoder, no preserved operation — have to be supplied by the reader. |
| Internal Consistency | Strong | The four components and the fidelity criterion do not compete; operation-relative fidelity follows from them rather than sitting beside them. |
| Structural Coherence | Weak in the inherited model | The kept catalogues organise by medium and by property, the decomposition organises by technical role, and the same scheme appears in several registers. Only the decomposition is typed. |
| Extensional Fidelity | Moderate | Canonical members are clean; leakage at compressed archives, at latent vectors, and at in-memory values, which are carriers rather than representations until an operation set is named. |
| Intensional Adequacy | Strong | Carrier, encoding, and operation preservation are the properties that matter for computation; nothing essential to the concept is missing from them. |
| Ontological Adequacy | Strong as mechanism, weak applied to the artifact | The concept denotes an arrangement, not an object; calling a file "a representation" names the artifact by one role it happens to play. |
| Discriminative Power | Strong | Separates representation from data structure (the carrier), from format (the scheme's specification), and from meaning (the interpretation), which is the distinction the field keeps losing. |
| Granularity Adequacy | Moderate | The mechanism level fits design and inspection; it is too coarse for "is this encoding faithful here", which needs the concrete operation set. |
| Conceptual Distinctiveness | Moderate | Distinct from data structure and from format by the relation it names; not distinct from "encoding" or "model" in ordinary use. |
| Boundary Differentiation | Moderate | Clear against a data structure and a file format; blurred against a *model*, since a model is a representation plus an interpretation and the two are usually named together. |
| Ontological Parsimony | Strong | Four components and no new entities; scheme, artifact, and map are the ordinary vocabulary of the field. |
| Operationalizability | Strong | Round-trip, canonical-form, and cross-decoder tests decide most membership questions mechanically. |
| Purpose Adequacy | Split | Adequate as a design and verification primitive; inadequate as an explanation of meaning, which the concept deliberately refuses to fix. |

## Representation System

> A **representation system** refers to a set of rules, symbols, or formats used to represent and encode information or knowledge in a computer or computational system. It defines how data is structured, organized, and stored, allowing the computer to manipulate, process, and interpret the represented information effectively.
> 

> This is the scheme inventory: each row names a scheme, the target domain it carries, and an implementation that realizes it. The typed reading is the decomposition above — these families are the `Technical Element Set` grouping under Computational Representation Set (Data Encoding Scheme Set and its siblings), and the standardized specimens appear under `Technical Standard`.

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

> These are the techniques the practice branch types: `Technical Task` → Scheme Selection, Encoding, Decoding, Compaction, Indexing, Augmentation, Interoperation, each carrying the `General Technique`s that implement it.

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

> The representation-specific subset is typed in the decomposition (`Technical Property` branch). This table is the full attribute inventory, and it deliberately reaches further: many of its rows describe the carrier — the data structure that hosts the representation — rather than the representation relation itself.

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
> Typed reading: `Technical Element` `(→ Kind)` `Technical Element Set` `(→ Instance)` Computational Representation Set `(→ Has)` `Technical Mechanism` `(→ Instance)` In-Memory Carrier.
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

## QA

### Is a data structure a representation?

> No, or only derivatively. A **data structure** is the carrier; a **representation** is the carrier together with the encoding relation and the domain it carries. The same array is a representation of temperatures, of pixels, or of nothing at all — the structure alone does not say which, and nothing follows about fidelity until an operation set is named.

### Is a model’s latent vector a representation in the same sense as JSON?

> Yes in form, no in access. Both are structure-carrying encodings in computable carriers. JSON’s relation is **specified** and public — a grammar, a schema, canonical forms; an embedding’s relation is **learned** and only partly inspectable — weights plus a decoder you must also trust. Both are representations; only one is specified, and that difference is what interpretability names.

> A latent vector also fails the “what does it mean” question in a way JSON does not: the coordinates have no named domain, so the domain *D* has to be inferred rather than read off the scheme.

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
- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- Piantadosi, S. T. (2021). The computational origin of representation. 31(1), 1.
