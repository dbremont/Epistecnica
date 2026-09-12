# Web Based Tool 'Conceptual Structure Typing Epistemic Practice' Interface

> Let’s design a **web-based*- tool for interacting with a dataset that represents the **Conceptual Structure of Epistemic Practice Typing**.

Which types of questions or used cases should the tools support?

- **Structural decomposition:*- The tool should answer questions that reveal how any epistemic entity is hierarchically composed into typed components, relations, and substructures within the epistemic graph.
- **Dependency analysis:*- The tool should answer questions that trace what epistemic entities, tools, constraints, or infrastructures must exist for a given artifact or process to be possible or valid.
- **Transformation pathways:*- The tool should answer questions that reconstruct the ordered sequence of epistemic operations by which inputs are converted into outputs across tools, artifacts, and processes.
- **Comparative analysis:*- The tool should answer questions that identify structural, functional, or inferential differences and similarities between two or more epistemic entities across their graph representations.
- **Functional role attribution:*- The tool should answer questions that determine what epistemic function a node or subgraph performs within a larger inference system, such as generation, validation, or control.
- **Constraint analysis:*- The tool should answer questions that identify the limiting conditions, uncertainties, or structural bottlenecks that restrict what can be inferred, constructed, or validated.
- **Feedback tracing:*- The tool should answer questions that track how information from validation signals, errors, or environmental responses propagates back into and modifies epistemic structures.
- **Validity evaluation:*- The tool should answer questions that determine how and why an epistemic artifact or process is considered justified, reliable, or acceptable under specific epistemic standards.
- **Generative inference:*- The tool should answer questions that infer what new epistemic artifacts, models, or structures can be systematically constructed from existing components and relations.
- **Counterfactual simulation:*- The tool should answer questions that evaluate how epistemic structures, outputs, or processes would change under hypothetical modifications of nodes, edges, or constraints.
- **Temporal evolution:*- The tool should answer questions that reconstruct how epistemic entities and their relations emerge, change, stabilize, or decay across time within the system.
- **Similarity and embedding analysis:*- The tool should answer questions that locate epistemic entities within a latent representational space defined by structural, functional, or inferential proximity.

Structure:

- **Overview*- – A panoramic entry point that orients the user by situating the entire conceptual structure within the broader landscape of epistemic practice, revealing its foundational categories and the questions it is designed to answer.
      - **Degree Distribution**: A statistical signature that quantifies the connective asymmetry of the epistemic system, revealing hub artifacts, bottleneck standards, or over‑constrained tools that silently shape inferential capacity.
      - Clustering Coefficient Distribution
      - Connected Components Structure
      - Hierarchical Depth Distribution
      - ...
- **Representation**: How do we represent the data in a way that reveals the structure of epistemic practice? Which epistemic artifacts enable intelligible inference from the dataset?
  - **Graph View**: – A non‑binary relational map that exposes the multi‑entity nature of epistemic acts, where a single hyperedge can jointly connect an artifact, its tool, its agent, and its constraint, thereby recovering the polyadic structure of actual practice.
    - Lenses
      - **Community Cluster Map**:  A macro‑scale topology that groups nodes by structural or functional affinity, making visible the emergent epistemic neighborhoods—such as “validation circuits” or “observation loops”—that would be invisible in a simple node‑link diagram.
      - Overlays
      - Heatmaps
      - Centrality
      - ....
    - Projections
      - **Graph Embedding**: A latent geometric projection that places every epistemic entity in a continuous space where proximity encodes structural similarity, enabling analogical reasoning, anomaly detection, and the discovery of functionally equivalent but non‑obvious elements.
      - ...
  - **Nodes Evolution Map**: ...
  - **Comparison Matrix View**: Contrast two or more instances of the same category (e.g., two different Epistemic Artifacts or two Tools).
  - **Query Interface**: – The analytic probe that allows the user to articulate graph‑pattern questions in terms of edge semantics, inheritance levels, and specific fields, converting the static knowledge graph into a reflectively searchable space of epistemic motifs.
  - **Specific Instance Level View**: A tool to help explore each node in the dataset.
  - **Timeline View**:  – A historicizing lens that recovers the temporal dimension of justification, revealing how standards emerged, how artifacts were revised, and how the validity of a claim is always path‑dependent and situated in a genealogy of prior acts.
- **Meta Epistemic Artifact Set**: A set of epistemic artifact about **'Conceptual Structure Typing Epistemic Practice'**.
  - Metric Set
  - Hierarchical Depth Distribution
  - Clustering Coefficient Distribution
- Admin Toolbox
  - Add new relationships between nodes.
  - ...
- **Documentation**: :  The reflexive layer that makes the representational choices themselves subject to epistemic scrutiny, explicating the edge‑type semantics, the inheritance hierarchy, the field definitions, and the data provenance so the map is never mistaken for the territory.
- **About**:  – The final act of intellectual situating that positions the tool and its taxonomy inside a research program, acknowledging the contingent, historically located act of schema design without which the entire apparatus would remain a disembodied mirror of itself.


### Overview

> Projection: A dataset projection is a formally defined transformation that maps a high-dimensional epistemic dataset into a structured visual or analytical coordinate system according to a chosen organizing principle, while preserving selected relational, categorical, temporal, or structural properties relevant to analysis.

> Lense: A lens is an overlay, modulation, or interpretive augmentation applied atop a dataset projection that alters visual encoding without fundamentally changing the underlying structural arrangement.

### Projection

| **Projection**                            | **Description**                                                                                                                                                                                     | **Lens(es)**                                                                                      |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Force Layout**                          | Organic spring-based topology that reveals natural clustering, emergent relational density, structural cohesion, and hidden topological communities. Best for observing overall network morphology. | Confidence Gradient, Edge Flow Animation, Family Edge Bundling, Centrality Sizing, Category Hulls |
| **Category Clusters**                     | Groups nodes by `category` enum to expose ontological composition, category size, intra-category density, and inter-category interaction structure.                                                 | Category Hulls, Constraint Heatmap, Confidence Gradient, Audit Staleness                          |
| **Inheritance Layers**                    | Stratifies nodes vertically or hierarchically by `inheritanceLevel`, revealing abstraction gradients, specialization depth, and conceptual hierarchy.                                               | Inheritance Depth Border, Observability Ghosting, Confidence Gradient                             |
| **Historical Timeline**                   | Positions nodes along temporal chronology using earliest historical emergence, exposing evolutionary emergence, historical clustering, and developmental sequencing of epistemic structures.        | Confidence Gradient, Audit Staleness, Edge Flow Animation                                         |
| **Domain Topology**                       | Clusters nodes according to shared `realityDomains`, revealing domain-specific concentration, interdisciplinary bridges, and cross-domain epistemic boundary objects.                               | Domain Overlap Threads, Category Hulls, Confidence Gradient                                       |
| **Radial Inheritance**                    | Organizes nodes concentrically by inheritance depth, with roots at the center and specialization radiating outward, emphasizing taxonomic specialization chains.                                    | Inheritance Depth Border, Observability Ghosting, Family Edge Bundling                            |
| **Relationship Family Flow**              | Groups nodes by dominant relationship family participation (`operational`, `constraint`, `representational`, etc.), revealing functional role ecosystems across ontology types.                     | Edge Flow Animation, Family Edge Bundling, Constraint Heatmap                                     |
| **Confidence Landscape**                  | Maps `confidenceScore` to radial certainty, with highly validated nodes central and uncertain nodes peripheral, exposing epistemic stability structure.                                             | Confidence Gradient, Audit Staleness, Noise Texture                                               |
| **Dependency DAG**                        | Restricts graph to dependency and causal edges (`depends_on`, `has_input`, `constrains`, etc.) to reveal operational production pipelines and causal structure.                                     | Edge Flow Animation, Family Edge Bundling, Constraint Heatmap                                     |
| **Chord / Adjacency Matrix**              | Macro-structural category-to-category relationship visualization showing aggregate interaction intensity between conceptual classes. Best for system-level architecture.                            | Confidence Gradient, Constraint Heatmap                                                           |
| **Geospatial Projection (if applicable)** | Maps nodes or domains to physical or geopolitical spatial coordinates where relevant, exposing geographic epistemic distributions.                                                                  | Domain Overlap Threads, Audit Staleness                                                           |
| **Multiscale Fractal View**               | Recursive visualization of nested epistemic structures across scales, exposing structural self-similarity and recursive organization.                                                               | Inheritance Depth Border, Confidence Gradient                                                     |
| **Semantic Similarity Embedding**         | Uses embedding or feature similarity to spatialize conceptually related nodes independent of explicit graph structure, revealing latent semantic neighborhoods.                                     | Domain Overlap Threads, Confidence Gradient, Noise Texture                                        |
| **Constraint Topography**                 | Spatializes nodes by degree and severity of constraining relationships, exposing bottlenecks, rigid zones, and permissive epistemic regions.                                                        | Constraint Heatmap, Audit Staleness                                                               |
| **Observability Gradient Projection**     | Positions nodes according to degree of direct observability vs. latent abstraction, revealing empirical accessibility gradients.                                                                    | Observability Ghosting, Confidence Gradient                                                       |


### Lense

| **Lens**                           | **Description**                                                                                                                                                     | **Projection(s)**                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Category Hulls**                 | Draws enclosing boundaries around category groupings, making categorical territories visually explicit and clarifying inter-category boundaries or overlaps.        | Category Clusters, Force Layout, Domain Topology, Relationship Family Flow                                    |
| **Constraint Heatmap**             | Colors nodes and/or edges based on density or severity of constraining relationships, revealing bottlenecks, rigid zones, or structurally over-constrained regions. | Dependency DAG, Category Clusters, Confidence Landscape, Constraint Topography                                |
| **Centrality Sizing**              | Scales node size according to graph-theoretic centrality (degree, betweenness, eigenvector, etc.), highlighting structurally influential concepts.                  | Force Layout, Dependency DAG, Domain Topology, Relationship Family Flow                                       |
| **Confidence Gradient**            | Applies color gradient to nodes according to `metadata.confidenceScore`, exposing certainty distribution and speculative frontiers.                                 | Nearly all projections; especially Force Layout, Historical Timeline, Confidence Landscape, Category Clusters |
| **Edge Flow Animation**            | Animates directional flow along edges to reveal operational, causal, or informational movement.                                                                     | Dependency DAG, Force Layout, Historical Timeline, Relationship Family Flow                                   |
| **Domain Overlap Threads**         | Draws faint soft-link threads between nodes sharing `realityDomains`, exposing latent domain affinity independent of explicit graph edges.                          | Domain Topology, Force Layout, Semantic Similarity Embedding                                                  |
| **Observability Ghosting**         | Modulates opacity based on degree of direct observability (`observable`, `partiallyObservable`, `latent`), making epistemic accessibility visually tangible.        | Radial Inheritance, Observability Gradient Projection, Force Layout, Historical Timeline                      |
| **Audit Staleness**                | Visualizes conceptual maintenance debt by encoding review recency via brightness, decay effects, or desaturation.                                                   | Confidence Landscape, Historical Timeline, Category Clusters, Force Layout                                    |
| **Noise Texture**                  | Applies uncertainty/noise patterns to artifact nodes according to `specific.noiseModel`, rendering data quality degradation perceptible.                            | Confidence Landscape, Semantic Similarity Embedding, Force Layout                                             |
| **Inheritance Depth Border**       | Uses border thickness or visual weight to encode inheritance depth, reinforcing specialization gradients.                                                           | Inheritance Layers, Radial Inheritance, Multiscale Fractal View                                               |
| **Family Edge Bundling**           | Bundles edges of similar type into coherent trunks, reducing visual clutter and exposing dominant relational highways.                                              | Force Layout, Dependency DAG, Radial Inheritance, Relationship Family Flow                                    |
| **Temporal Density Bands**         | Adds era bands or epoch shading to timeline projections, revealing macro-period clustering.                                                                         | Historical Timeline                                                                                           |
| **Domain Saturation Overlay**      | Colors nodes by number or diversity of domains they span, revealing narrow specialists vs. broad integrators.                                                       | Domain Topology, Force Layout                                                                                 |
| **Causal Cycle Highlighting**      | Detects and visually emphasizes dependency cycles or feedback loops.                                                                                                | Dependency DAG, Force Layout                                                                                  |
| **Speculative Frontier Glow**      | Highlights low-confidence but high-centrality nodes as potentially critical unresolved structures.                                                                  | Confidence Landscape, Force Layout                                                                            |
| **Normative Weight Overlay**       | Encodes presence of standards, governance, or normative force via iconography or edge emphasis.                                                                     | Category Clusters, Dependency DAG, Relationship Family Flow                                                   |
| **Abstraction Gradient**           | Colors or textures nodes by abstraction level independent of confidence, revealing conceptual stratification.                                                       | Inheritance Layers, Radial Inheritance, Semantic Similarity Embedding                                         |
| **Structural Fragility Indicator** | Highlights nodes whose removal would heavily fragment the graph, exposing systemic vulnerabilities.                                                                 | Force Layout, Dependency DAG, Domain Topology                                                                 |
| **Maintenance Burden Index**       | Combines audit staleness, dependency load, and confidence into a composite overlay showing conceptual debt hotspots.                                                | Confidence Landscape, Dependency DAG, Force Layout                                                            |
| **Epistemic Velocity Overlay**     | Represents rate of historical conceptual change or revision frequency where data exists.                                                                            | Historical Timeline, Confidence Landscape                                                                     |

### Generic Design Spec

Tech Stack:

- Vanilla HTML, JS,
- Can used libraries etc for Hypergraphs,  stype etc, but not frameworks
- Follow  a general design - for each page with footer - and asides for the toolbox.

Rules:

- The data is served by the sync server (`bin/sync.py`) — the only frontend-facing surface (`GET /api/nodes`, `GET /api/layout` via `app/js/api.js`). The browser never talks to CouchDB directly; CORS stays disabled on the DB.
- The view should be separate from the data.
- Be able to handle 100,000 nodes.
- Handle partial load of the element.
- `...`

AI Assist:

- The editor ships LLM-assisted authoring against a configurable OpenAI-compatible endpoint (default DeepSeek; token + model in Settings). The AI token lives only in the browser; the backend stays data-only (no AI endpoints, no key on the server).
- *AI Improve/Generate* (Enhance button) rewrites the selected node via a schema-bearing prompt (`relationships` is always stripped and preserved), shows a diff, and applies on review. Two transports: direct API calls (`Generate (API)`), or the manual **Copy Prompt** flow — copy the identical prompt into any external LLM chat and paste its JSON back (*Use Pasted Result*) through the same diff + Apply path. No API key is required for the manual transport.
- *AI Discover Relations* (Find Relations) suggests cross-node links for curation (API-only).

1. Design Philosophy

- **Editorial Density:** Information is presented with high signal-to-noise ratio. Whitespace is structural (dividers, padding), not decorative.
- **Epistemic Layering:** The UI mirrors the subject matter: a fixed, structural background (the graph substrate) with a foreground of human-readable narrative and data.
- **System Visibility:** The interface always communicates its underlying state (time, schema version, load state) via peripheral monospaced metadata.

2. Color Tokens

The palette relies on extreme dark values with two distinct semantic accents.
- **Backgrounds:** `--bg-void` (Deepest), `--bg-surface` (Elevated), `--bg-card` (Interactive).
- **Text:** `--text-primary` (Headers), `--text-secondary` (Body), `--text-muted` (Metadata/Labels).
- **Accents:**
    - `--accent-gold`: Used for structural/narrative elements (borders, eyebrows, primary hovers).
    - `--accent-cyan`: Used for computational/active elements (focus states, live data, highlights, links).
- **Borders:** `--border-subtle` (1px, low-opacity white). Used to define structure without visual weight.

3. Typography System

Three typefaces establish a strict hierarchy between narrative, function, and data.
- **Display (Cormorant Garamond):** Human context. Used for page titles, narrative quotes, and section headers. Often italicized for narrative voice.
- **Body (Inter):** Explanatory context. Used for descriptive paragraphs and standard UI text.
- **Mono (JetBrains Mono):** System context. Used for metadata, data values, system specs, inputs, and interactive triggers. Always uppercase for labels; standard case for values.

4. Layout & Structure

- **Content Widths:** Standard reading width `1000px`; Wide system width `1200px`.
- **Structural Dividers:** Use `1px solid var(--border-subtle)` for horizontal and vertical boundaries. Avoid heavy shadows; use hairline borders and background shifts to define elevation.
- **Narrative Accent:** When isolating a quote or core concept, apply a `1px solid var(--accent-gold)` left border.
- **Grid Matrices:** For dense data or navigation, use `gap: 1px; background: var(--border-subtle)` on the container to create hairline grid borders between child elements.

5. Generic Component Rules

- **Inputs (Query/Search):** Must use `--font-mono`. Background `--bg-surface`. Focus state transitions border to `--accent-cyan` with a subtle glow (`box-shadow: 0 0 15px rgba(91, 240, 231, 0.05)`).
- **Data Strips/Metrics:** Always format as `Value` (Mono, `1.5rem`, Cyan) over `Label` (Mono, `0.65rem`, Muted, Uppercase).
- **Interactive Cells/Cards:** Background `--bg-void`. Hover shifts background to `--bg-surface`. Active/Selected state shifts top border or text to `--accent-cyan`.
- **Chips/Tags:** Mono font, `0.6rem`, `--bg-card` fill. Hover/Active adopts Cyan text and border.

6. Interaction & Motion

- **Scroll Reveal:** Elements enter via `.reveal` class. Initial: `opacity: 0; translateY(20px)`. Visible: `opacity: 1; translateY(0)`. Transition: `0.8s ease-out`.
- **Hover Transitions:** Standard duration `0.3s ease`.
- **Focus States:** Never use default browser outlines. Replace with border-color shifts and subtle glows.

7. Atmospheric Layer

Every page must include the **Ambient Canvas** as a fixed background (`z-index: 0`). It renders a subtle, slow-moving constellation graph to reinforce the epistemic topology of the dataset without obstructing the UI.

### Home Page

- What is the goal of the Home Page? How this page should be evaluated? What should be the content of the page?

The Home Page is a high-level epistemic routing interface whose function is to:

> Transform an undifferentiated query or exploratory intent into a structured navigation into epistemic subspaces (overview, representation, query, timeline, etc.), while revealing the system’s global structure at minimal cognitive load.

> The Home Page is a meta-epistemic dispatcher that maps undifferentiated user intent into structurally appropriate epistemic subsystems while exposing only the minimal global signature necessary for orientation.

1. Goal of the Home Page

- Transform undifferentiated user intent into structured navigation across epistemic subsystems (Overview, Representation, Query, Timeline, Node Explorer)
- Act as a meta-epistemic routing interface for the entire system
- Provide minimal but sufficient global structural orientation
- Compress epistemic complexity into navigable entry points without exposing full analytical detail
- Map user intent → appropriate epistemic operation space

2. Formal Role Definition

- Distributional compressor of the full epistemic graph
- Routing surface into epistemic views and operations
- First-order abstraction filter over system complexity
- Meta-epistemic dispatcher for navigation decisions
- Intent-to-structure translation layer

3. Evaluation Criteria

- **Routing Efficiency**

  - User can reach any major subsystem (Overview / Representation / Query / Timeline / Node Explorer) in ≤2 interactions

- **Intent Resolution Accuracy**

  - Ambiguous user intent is correctly mapped to appropriate epistemic subsystem

- **Cognitive Load Compression**

  - User does not need prior system understanding to begin navigation

- **Structural Transparency**

  - System exposes available epistemic operations without exposing internal complexity

- **Non-Redundancy**

  - Does not replicate Overview metrics or Representation visualizations

4. Dataset Identity Strip

- Node count (|V|)
- Edge count (|E|)
- Category entropy (diversity of epistemic classes)
- Edge-type entropy (diversity of relations)
- Graph density (global connectivity indicator)

5. Primary Routing Layer

- Analyze Structure → Overview (diagnostics, topology, system structure)
- Explore Relations → Graph / embedding / neighborhood exploration
- Trace Knowledge Flow → Process / feedback / temporal dynamics
- Inspect Entity → Node-level epistemic artifact inspection
- Query System → Formal graph query interface
- Compare Entities → Structural comparison matrix

6. System Map Preview (Compressed Topology View)

- Macro clustering sketch (abstracted graph regions)
- Dominant node categories (high-frequency epistemic classes)
- Dominant edge types (most structurally influential relations)
- Hub regions (top-k degree nodes aggregated into clusters)

Constraints:

- Maximum 50–100 abstracted nodes
- No full graph rendering
- No deep interaction or traversal logic
- Only structural compression, not exploration

7. Active Epistemic Dynamics Snapshot

- Most connected epistemic artifacts (high-degree nodes)
- Dominant active tools (frequent transformation operators)
- Most constrained domains (constraint-heavy subspaces)
- Strongest feedback loops (dense validation cycles)
- Most central agents (control or coordination hubs)

Constraint:

- Not temporal history
- Not evolution tracking
- Pure structural activity density projection


8. Entry Guidance (Intent Disambiguation Layer)

- “I want to understand how this system works” → Overview
- “I want to see how things connect” → Graph View
- “I want to find why something fails” → Constraint Analysis
- “I want to understand evolution over time” → Timeline View
- “I want to inspect a node” → Node Explorer
- “I want to compare structures” → Comparison Matrix
- “I want to query relationships” → Query Interface

9. Excluded Content (Hard Separation Constraints)

- ❌ Full graph visualizations (Representation layer responsibility)
- ❌ Full statistical distributions (Overview responsibility)
- ❌ Node tooltips or local neighborhoods (Graph responsibility)
- ❌ Full query language UI (Query module responsibility)
- ❌ Temporal evolution charts (Timeline responsibility)
- ❌ Deep semantic interpretation of nodes (Node Explorer responsibility)

### Overview Design Spec

- What is the goal of the overview page? How this page should be evaluated? What should be the content of the page?

> The Overview is a projection of the epistemic graph into structural invariants that describe inference capacity, constraint structure, and control topology.

- Introduction

- Data Set Characterization:
  - Node count (|V|)
  - Edge count (|E|)
  - Edge-type entropy
  - Category entropy
  - Graph density
  - Average branching factor

- Graph Shape Signature
  - Degree Distribution (hub formation / decentralization)
  - Betweenness Centrality Distribution (control points of inference flow)
  - Clustering Coefficient Distribution (local closure of reasoning)
  - Connected Components Structure (fragmentation vs integration)
  - Hierarchical Depth Distribution (vertical epistemic stratification)

### Representation Design Spec

#### Graph View Design Spec

**Guiding questions:**

- What should be the Graph visualization goal?
- How this section should be evaluated? Which are the others visualization options or (toggles that the graph may be able to support?)
- Whick kinds of visual lenses can be created from the dataset?
  - Cluter
  - Heatmaps
  - Overlays
  - Centrality
  - ...
- Which projections or alternatives views can be supported?
  - Graph Embedding
  - Category projection
  - ...
- Which statistics (graph) -> R should we also show to aid the understanding of the graph?

**Functionalty Set:**

- Support native graph visualization using a force-directed rendering engine as the primary spatialization system.
- When hoover the nodes - show a sophisticated visualization.
- Hovering a node highlights all hyperedges incident to it.
- Visual Lenses (Interpretive Overlays)
  - Community Cluster Map – Groups nodes by structural/functional affinity (e.g., “validation circuits”, “observation loops”).
  - Domain Cluster Map -> ...
  - Overlays – Semi‑transparent layers that add contextual information (e.g., constraint severity, feedback strength).
  - Heatmaps – Color‑coded intensity maps over nodes/edges (e.g., eigenvector centrality, constraint density).
  - Centrality visualization – Visual encoding of degree, betweenness, or eigenvector centrality (e.g., node sizing, border thickness).
- Alterantives Views:
  - Graph embedding – Latent geometric projection where proximity encodes structural similarity (supports analogical reasoning and anomaly detection).
  - Category projection – Collapses hyperedges to show only nodes of a selected epistemic category (Artifact, Agent, Tool, etc.).
- Embedding space browser – After computing a graph embedding, provide a 2D/3D scatter plot where Euclidean distance ≈ structural dissimilarity. Brushing selects nodes in the main view.
-
- Nodes drawn as colour‑coded category glyphs (Artifact = square, Agent = diamond, Tool = hexagon, etc.).
- Support the search of nodes.
- Statistics Modal:
  - Graph Density
  - Node Count |V|
  - Fiedler Eigenvalue
  - Hyperedge Count |E|
  - Average Path Length
  - Connected Components Count
  - Average Hyperedge Cardinality
- Category toggles – Show/hide entire epistemic classes (e.g., hide all Constraints to expose only Artifacts and Tools).
- Edge‑type filtering – Display only edges of a selected type (depends_on, validates, encodes, etc.).
- Inheritance level pruning – Collapse or expand nodes based on depth in the type hierarchy.
- Epistemic role glossary – Hover over any edge type or category to see its formal definition (from your taxonomy).

**Node Tooltip:**

The tooltip is a local epistemic lens on a node:

It does not describe the node.
It exposes its position in the epistemic system.

So every tooltip must answer:

- What is this?
- What does it connect to?
- What does it depend on?
- How is it evaluated?
- What is its epistemic role?
- What is it's centrality? (Eigenvector Centrality)
- Revision tracking – Highlight nodes whose reviewHistory changed in a selected time window.