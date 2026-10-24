---
tags: [framework]
---

# Network Science


> **Network Science** is an interdisciplinary field that  aims to develop a toolbox—combining mathematical, statistical, and computational methods—for representing and analyzing systems composed of interconnected elements.
> 

> A **Network System** in refers to a collection of interconnected elements or nodes, often represented mathematically as a graph, where the relationships between nodes convey meaningful information about the structure, dynamics, or interactions within a complex system.
> 

## Breviarium

> 

## Representation

> **Network Models** are mathematical or computational representations of relationships and interactions between entities, often depicted as nodes and edges, used to analyze and understand the structure, dynamics, and behaviors of complex systems.
> 

### Concept

| **Concept** | **Description** |
| --- | --- |
| **Network Effects** | The phenomenon where the value of a product, service, or platform increases as more users or participants join the network. |
| **Small-world Phenomenon** | The observation that most nodes in a network can be reached from any other node through a relatively small number of intermediate connections, often characterized by short average path lengths. |
| **Scale-free Networks** | Networks in which the degree distribution follows a power-law distribution, meaning a small number of nodes (hubs) have a disproportionately large number of connections. |
| **Clustering Coefficient** | The tendency for nodes in a network to form clusters or groups with a higher density of connections within clusters than between clusters. |
| **Epidemic Spreading** | The spread of diseases, information, or behaviors through a network, where nodes become infected or adopt a new behavior based on interactions with their neighbors. |
| **Cascade Effects** | The propagation of an event or change through a network, triggering a series of subsequent events or changes among connected nodes. |
| **Community Structure** | The organization of nodes into cohesive communities or modules within a network, where nodes within the same community are more densely connected than nodes in different communities. |
| **Resilience and Robustness** | The ability of a network to maintain its structural integrity and functionality in the face of disturbances, failures, or attacks. Characterized by measures such as connectivity and redundancy. |
| **Centrality** | The importance or prominence of nodes within a network, often measured by metrics such as degree centrality, betweenness centrality, or eigenvector centrality. |
| **Homophily** | The tendency for nodes in a network to form connections with similar nodes based on shared attributes, such as interests, demographics, or behaviors. |
| **Diffusion of Innovations** | The spread of new ideas, technologies, or practices through a network, where adoption by one node influences the likelihood of adoption by neighboring nodes. |
| **Network Formation** | The process by which networks are created or evolve over time, driven by preferential attachment, triadic closure, or homophily. |
| **Network Robustness** | Refers to a network's ability to withstand random failures or targeted attacks without losing connectivity or functionality. |
| **Feedback Loops** | Describe how changes in one part of the network can loop back to influence subsequent behavior, leading to self-reinforcing or self-regulating dynamics. |
| **Synchronization** | Phenomena observed in networks of coupled oscillators, where nodes adjust their dynamics to achieve coordinated behavior, seen in biological, physical, and engineered systems. |
| **Community Structure** | Networks often exhibit community structure, where nodes are more densely connected within communities than between them, leading to modular organization. |
| **Network Motifs** | Recurring patterns or subgraphs found in complex networks, representing building blocks of network architecture with specific functional roles. |
| **Spillover Effects** | The impact of changes or events in one part of the network that affect other parts or nodes not directly involved in the initial change. |
| **Percolation Effects** | The process and effects of how changes or disruptions spread through a network, often used to analyze the robustness and connectivity of the network. |
| **Community** | A group of nodes in a network that are more densely connected to each other than to nodes outside the group, forming a distinct module or cluster. |

### Template

> **Abstract network models** serve as simplified representations of real-world networks, allowing researchers to study fundamental properties and dynamics without considering specific details.
> 

| **Type of Model** | **Model Name** | **Description** |
| --- | --- | --- |
| **Dynamic Network Models** | **Dynamic Network Models** | Capture the temporal evolution of networks by representing changes in network structure over time, allowing for the study of network dynamics, growth, and adaptation. |
| **Random Graph Models** | **Erdős-Rényi (ER) Model** | A classic random graph model where edges between nodes are placed randomly with a fixed probability. |
|  | **Watts-Strogatz Model** | Introduces small-world properties by rewiring edges in a regular lattice with a certain probability. |
|  | **Barabási-Albert (BA) Model** | Generates scale-free networks with preferential attachment, where new nodes attach to existing nodes with a high degree. |
|  | **Stochastic Block Models (SBMs)** | Generative models that partition nodes into groups or communities and assign probabilities for edges based on group memberships. |
|  | **Exponential Random Graph Models (ERGMs)** | Statistical models specifying probability distributions over network structures based on network features or motifs. |
|  | **Random Geometric Graph Model** | Places nodes randomly in a space and connects nodes within a certain distance threshold, leading to networks with spatial structure and properties. |
| **Geometric Network Models** | **Spatial Random Networks** | Nodes are distributed continuously, and edges are formed based on distance thresholds or spatial constraints. |
|  | **Delaunay Triangulation** | Connects nodes in a planar point set such that no point is inside the circumcircle of any triangle formed by the connected nodes. |
|  | **Spatial Network Models** | Incorporates spatial constraints or geographic distances to generate networks, such as those on grids, lattices, or geographical maps. |
| **Hierarchical Network Models** | **Fractal Networks** | Network structures with self-similar patterns at different scales, exhibiting hierarchical organization. |
|  | **Tree Networks** | Hierarchical networks with branching structures resembling trees, often used to model organizational or information flow structures. |
| **Stochastic Block Models (SBM)** | **SBM with Homophily** | Nodes are grouped into blocks, and edges are formed based on block memberships with additional probabilities for within-block connections. |
|  | **SBM with Heterophily** | Similar to homophily SBM but includes additional probabilities for between-block connections. |
| **Agent-Based Models (ABM)** | **Schelling's Segregation Model** | Simulates the emergence of segregation patterns in a population based on individual preferences for neighbors with similar characteristics. |
|  | **Axelrod's Cultural Diffusion Model** | Simulates the spread of cultural traits through social interactions, with agents adopting or adapting traits based on similarity or differences. |
| **Percolation Models** | **Site Percolation** | Nodes of a lattice-based network are occupied with a certain probability, leading to the emergence of connected clusters. |
|  | **Bond Percolation** | Edges of a lattice-based network are occupied with a certain probability, determining the existence of connected pathways. |
| **Network Growth Models** | **Copying Model** | New nodes copy a subset of edges from existing nodes, forming networks with community structure. |
|  | **Duplication-Divergence Model** | New nodes duplicate existing nodes and their edges, with the possibility of edge divergence, leading to the emergence of modular networks. |
|  | **Forest Fire Model** | A dynamic network growth model where new nodes are added iteratively and form connections with existing nodes based on a "burning" process, leading to heavy-tailed degree distributions. |
| Specialized Network Models | **Configuration Model** | Constructs networks by randomly assigning stubs (half-edges) to nodes and then connecting stubs to form edges, allowing for the specification of arbitrary degree distributions. |
|  | **Multiplex Networks** | Represent networks with multiple layers or types of interactions between nodes, capturing different aspects of complex systems such as social interactions, transportation networks, or biological systems. |
|  | **Threshold Models** | Model the spread of behaviors, opinions, or diseases through networks by specifying thresholds for activation or adoption, where nodes become active if a sufficient number of neighbors are active. |
|  | **Scale-Free Networks** | Scale-free network models, like the Barabási-Albert model, create networks where new nodes preferentially attach to existing nodes with high degrees, leading to the emergence of hubs and power-law degree distributions. |
|  | **Small-World Networks** | Small-world network models, exemplified by the Watts-Strogatz model, start with a regular lattice structure and introduce random rewiring of edges to create short-average path lengths while preserving high clustering. |
|  | **Percolation Models** | Percolation models study the emergence of giant connected components or phase transitions in random or structured networks under conditions of connectivity thresholds. |
|  | **Diffusion Models** | Diffusion models simulate the spreading of contagions, information, or innovations through networks, incorporating factors such as transmission rates, network structure, and agent behavior. |
|  | **Hierarchical Networks** | Hierarchical network models represent networks with nested or hierarchical structures, capturing multi-scale organization and modularity. |
|  | **Multiplex Networks** | Multiplex network models represent networks with multiple layers or types of connections, reflecting the diverse interactions observed in complex systems. |
|  | **Temporal Networks** | Temporal network models incorporate time-varying connections or dynamics into network representations, allowing for the study of evolving network structures and temporal patterns of interactions. |

## Structure

> 

| **Feature** | **Description** |
| --- | --- |
| **Interconnected Components** | The system consists of multiple entities or components that interact with each other. |
| **Complex Relationships** | There are intricate and often nonlinear relationships among components that can be represented by edges in a network. |
| **Data on Interactions** | Availability of data that describes the nature and strength of interactions or connections between components. |
| **Network Topology** | The system has a defined structure or pattern in terms of how components are connected, which can be mapped as a network. |
| **Dynamic Interactions** | Components in the system exhibit dynamic interactions that change over time, suitable for modeling with evolving networks. |
| **Modularity** | The system can be divided into modules or clusters of interconnected components, making it amenable to network-based analysis. |
| **Hierarchical Structure** | The system exhibits hierarchical relationships among components, which can be effectively modeled using network layers or levels. |
| **Flow or Transfer Mechanisms** | There are mechanisms for the transfer or flow of resources, information, or influence between components. |
| **Feedback Loops** | The system includes feedback mechanisms where the output of one component affects other components, relevant for network modeling of cyclical influences. |
| **Scalability** | The system’s complexity scales with the number of components or interactions, suitable for large-scale network modeling. |
| **Emergent Behavior** | The system demonstrates emergent properties arising from the interactions of its components, which can be studied through network dynamics. |
| **Interaction Patterns** | The system exhibits identifiable patterns in the interactions between components, which can be captured and analyzed using network metrics. |
| **Complex Dependencies** | Components in the system are dependent on one another in complex ways, making network representation useful for understanding these dependencies. |

## Dynamics

> 

> **Percolation** (from Latin percolare, “to filter” or “trickle through”), in physics, chemistry and materials science, refers to the movement and filtering of fluids through porous materials. It is described by Darcy’s law. Broader applications have since been developed that cover connectivity of many systems modeled as lattices or graphs, analogous to connectivity of lattice components in the filtration problem that modulates capacity for percolation.
> 

## Inference

> What can be learned? How can it be learned?
> 

> Inference in complex networks refers to the process of **extracting latent knowledge**, **predicting missing or future information**, and **uncovering underlying mechanisms** that shape the structure and dynamics of the network. This involves applying statistical, probabilistic, and machine learning techniques to answer core scientific questions about the system modeled by the network.
> 

### 🧠 **What Can Be Learned?**

◾ **Structure Discovery**

- **Link prediction**: Identify missing or future connections (e.g., unknown protein–protein interactions, future social ties).
- **Community detection**: Infer modular structure—functional groups, social clusters, biological pathways.
- **Hierarchical structure**: Reveal multiscale patterns and nested communities.

◾ **Node and Edge Properties**

- **Node classification**: Infer labels (e.g., disease genes, user interests).
- **Edge weights or types**: Estimate strengths or types of relationships (friendship vs. collaboration).

◾ **Dynamic Rules**

- **Diffusion models**: Learn how information, diseases, or influence spread through the network.
- **Interaction mechanisms**: Estimate parameters of models like epidemic thresholds or contagion cascades.

◾ **Causal Structure**

- **Granger causality networks**, **Bayesian network structure learning**, or **structural equation modeling** are used to infer causal relationships from observational data embedded in network form.

◾ **Network Generative Processes**

- Learn the process by which the network was created:
    - Preferential attachment
    - Homophily
    - Geometric constraints

### ⚙️**How Can It Be Learned?**

◾ **Statistical Methods**

- **Exponential Random Graph Models (ERGMs)**: Estimate probabilities of edge formation under constraints.
- **Stochastic Block Models (SBMs)**: Learn group memberships and inter-group connection probabilities.
- **Latent Space Models**: Embed nodes in a hidden space where proximity determines connection likelihood.

◾ **Probabilistic Graphical Models**

- **Bayesian networks** (directed)
- **Markov random fields** (undirected)
- Used for modeling dependencies and conducting inference over uncertain structures.

◾ **Machine Learning Techniques**

- **Graph Neural Networks (GNNs)**: Deep learning models that generalize convolution to graphs. Useful for node classification, graph classification, link prediction.
- **Autoencoders and embeddings**: Learn low-dimensional latent representations (e.g., node2vec, DeepWalk) for downstream inference tasks.

◾ **Optimization-Based Approaches**

- Inference often involves solving:
- Likelihood maximization
- Regularized matrix/tensor factorization (e.g., for recommendation or missing link inference)
- Community detection via modularity optimization or spectral clustering

◾ **Dynamic and Temporal Models**

- Time-varying graphs require methods like:
    - Dynamic stochastic block models
    - Recurrent GNNs
    - Temporal point processes

### 📈 **Applications of Network Inference**

| **Domain** | **Inference Goal** | **Method Example** |
| --- | --- | --- |
| Neuroscience | Infer brain modules and connectivity patterns | Dynamic SBMs, GNNs |
| Epidemiology | Reconstruct transmission chains | Bayesian inference, contact tracing |
| Genomics | Identify regulatory relationships between genes | GRN inference using probabilistic models |
| Social Science | Predict friendships, influence, or polarization | Link prediction, opinion dynamics modeling |
| Internet Science | Detect botnets, cyberattacks | Anomaly detection in temporal graphs |

## Network Computation

> Computing over networks involves performing various computations, analyses, and algorithms on network data to extract insights, identify patterns, and solve problems.
> 

| **Method Category** | **Method** | **Description** |
| --- | --- | --- |
| **Graph Algorithms** | **Shortest Path** | Find the shortest path between nodes, using algorithms like Dijkstra's or Bellman-Ford. |
|  | **Minimum Spanning Tree** | Compute the minimum spanning tree connecting all nodes with the minimum total edge weight. |
|  | **Graph Traversal** | Systematically traverse nodes or edges using methods like depth-first search (DFS) or breadth-first search (BFS). |
|  | **Centrality Measures** | Calculate metrics like degree centrality, betweenness centrality, or eigenvector centrality to identify critical nodes in a network. |
|  | **Community Detection** | Identify clusters or communities within the network using algorithms like modularity optimization or spectral clustering. |
| **Network Analysis** | **Network Metrics** | Compute network-level metrics such as density, diameter, clustering coefficient, and assortativity. |
|  | **Network Motif Analysis** | Identify recurring patterns or subgraphs (motifs) that are overrepresented compared to random networks. |
|  | **Graph Matching** | Compare and align networks to find similarities or differences using graph isomorphism or similarity measures. |
| **Machine Learning and Statistical Methods** | **Network Embedding** | Learn low-dimensional representations of nodes or edges, capturing structural and relational information. |
|  | **Network Classification and Prediction** | Classify nodes or predict links based on topology and attributes using methods like logistic regression or graph neural networks. |
|  | **Statistical Inference** | Apply statistical methods for inference, including network models, hypothesis testing, or Bayesian inference. |
| **Optimization and Game Theory** | **Network Optimization** | Solve optimization problems like network flow, facility location, or routing using techniques like linear or integer programming. |
|  | **Network Games** | Model strategic interactions or decision-making among nodes, studying phenomena like network formation or the evolution of cooperation. |
| **Simulation and Modeling** | **Network Simulation** | Simulate dynamic processes or phenomena on networks, such as epidemic spreading or network evolution. |
|  | **Agent-Based Modeling** | Simulate interactions among individual agents within a network, studying emergent behavior and collective dynamics. |

## Statistics on Network

> Statistics of complex networks is an interdisciplinary field that uses tools from **graph theory**, **statistical physics**, and **applied statistics** to characterize, analyze, and model real-world networks. This area is central in understanding systems in **biology**, **technology**, **social science**, and **information science**.
> 

| **Category** | **Statistical Tool/Method** | **Purpose / Application** | **Graph Type / Use Case** |
| --- | --- | --- | --- |
| **Descriptive Statistics** | Degree Distribution | Analyze how many connections each node has | Social networks, web graphs |
|  | Clustering Coefficient | Measures local density or cohesion | Social networks, protein interaction networks |
|  | Assortativity | Correlation of node degrees | Social networks, citation networks |
|  | Path Length & Diameter | Measures graph reachability and efficiency | Transportation, communication networks |
| **Inferential Statistics** | Exponential Random Graph Models (ERGMs) | Model probability of graph configurations | Social networks, organizational networks |
|  | Stochastic Block Models (SBMs) | Identify latent groups or communities | Community detection, fraud detection |
|  | Hypothesis Testing for Motifs | Test for over/under-representation of subgraphs | Biological networks, metabolic networks |
| **Regression / ML** | Graph Regression Models | Predict node or edge attributes using topological features | Finance, biology, social science |
|  | Node Embedding + Regression (e.g. node2vec + Lasso) | Learn node features for supervised tasks | Link prediction, classification |
| **Bayesian Methods** | Bayesian Graphical Models | Probabilistic modeling of dependencies between nodes | Gene regulatory networks, influence networks |
|  | Latent Space Models | Infer hidden positions of nodes in a latent space | Political networks, social affinity graphs |
| **Network Sampling & Estimation** | Respondent-Driven Sampling (RDS) | Sampling hard-to-reach populations from networks | Epidemiology, public health |
|  | Snowball Sampling | Chain-referral sampling technique | Hidden populations, offline social graphs |
|  | Subgraph Estimation | Estimating global properties from partial observations | Large-scale web graphs, infrastructure networks |
| **Time Series & Dynamics** | Temporal Exponential Random Graph Models (TERGMs) | Models evolution of network structure over time | Longitudinal social networks |
|  | Dynamic Stochastic Block Models | Detect evolving communities | Time-varying citation networks |
|  | Change Point Detection in Graphs | Identify structural shifts in evolving networks | Finance, security |
| **Topological Data Analysis** | Persistent Homology | Study shape of data (cycles, holes) across scales | Brain networks, sensor networks |
|  | Betti Numbers | Quantify number of n-dimensional holes | High-dimensional or multi-layer graphs |
| **Resampling Methods** | Graph Bootstrap | Assess uncertainty in network metrics | Small or noisy networks |
|  | Permutation Tests on Graphs | Test significance of observed structure | Brain connectivity, social influence |

## Mathematics on Network

> 

| **Mathematical Area** | **Tool / Concept** | **Purpose / Application** | **Graph Type / Use Case** |
| --- | --- | --- | --- |
| **Graph Theory** | Adjacency & Incidence Matrices | Encode graph structure for algebraic operations | All complex graphs |
|  | Graph Isomorphism | Determine structural equivalence between graphs | Pattern recognition, compiler design |
|  | Planarity & Kuratowski’s Theorem | Analyze embeddability in 2D plane | Circuit design, geographic networks |
|  | Chromatic Number & Coloring | Minimize conflicts (e.g. resource allocation) | Scheduling, frequency assignment |
| **Linear Algebra** | Spectral Graph Theory (Eigenvalues of Laplacian) | Analyze graph connectivity, clusters, and diffusion | Clustering, image segmentation |
|  | Singular Value Decomposition (SVD) | Dimensionality reduction for graph data | Embeddings, recommendation systems |
|  | Matrix Powers | Compute walks of fixed lengths | Path enumeration, reachability analysis |
| **Algebraic Topology** | Homology (e.g., simplicial or clique complex) | Study higher-order structures (cycles, holes) | Brain networks, social triads |
|  | Persistent Homology | Analyze topological features across scales | Temporal or multi-layer networks |
| **Group Theory** | Automorphism Groups | Study graph symmetries and invariants | Chemical compounds, network motifs |
|  | Cayley Graphs | Construct graphs from group elements | Algebraic graph theory, discrete geometry |
| **Combinatorics** | Enumeration of Paths, Cycles, Trees | Count graph configurations | Chemical isomers, electrical networks |
|  | Inclusion-Exclusion Principle | Count constrained subgraphs | Motif discovery, path counting |
|  | Generating Functions | Encode combinatorial properties | Random graphs, network growth models |
| **Calculus / Analysis** | Graph Laplacian Operator | Model diffusion, flow, and vibration | Heat diffusion, power grids |
|  | Discrete Harmonic Functions | Smoothness and signal processing on graphs | Graph signal processing, denoising |
|  | Green’s Function on Graphs | Solve difference equations, measure influence | Electrical networks, ranking systems |
| **Probability Theory** | Random Walks on Graphs | Model exploration and diffusion | PageRank, Markov chains |
|  | Markov Chains & Transition Matrices | Stochastic modeling on graphs | Epidemic modeling, recommendation systems |
|  | Percolation Theory | Study connectivity under random removal | Robustness, epidemiology |
| **Dynamical Systems** | Discrete-Time Graph Dynamics | Model node/edge state changes | Opinion dynamics, contagion models |
|  | Coupled Oscillator Models | Synchronization phenomena on networks | Power grids, biological rhythms |
|  | Stability & Bifurcation Analysis | Understand behavior of dynamic systems on graphs | Control, consensus algorithms |
| **Geometry** | Graph Embeddings in Euclidean/Hyperbolic Space | Visualize and cluster graph structure | Network visualization, latent position models |
|  | Gromov Hyperbolicity | Measure global curvature of graphs | Internet graphs, tree-likeness analysis |
|  | Spectral Embedding | Represent graph nodes in a geometric space | Graph drawing, similarity search |
| **Information Theory** | Entropy of Graphs | Quantify structural complexity | Network compression, anomaly detection |
|  | Graph Compression via Minimum Description Length (MDL) | Optimal encoding of graph structure | Community detection, model selection |

## Case Study

> a **Set of Modelling Case Studies**.
> 

> **Network models** are versatile tools used to capture and study various phenomena and effects in different domains.
> 

> **Network phenomena** are observable patterns, behaviors, or dynamics that emerge from the interactions between nodes (individual entities) within a network.
> 

| **Domain** | **Application** | **Graph Structure** | **Note** |
| --- | --- | --- | --- |
| **Neuroscience** | Brain connectivity | Nodes = brain regions; Edges = synaptic/functional connections | Human Connectome Project; studies of epilepsy, Parkinson’s |
| **Genomics** | Gene regulatory networks | Nodes = genes; Edges = regulatory interactions | Modeling expression dynamics, e.g., yeast gene circuits |
| **Proteomics** | Protein–Protein Interactions (PPI) | Nodes = proteins; Edges = interactions | STRING database; disease module discovery |
| **Metabolic Networks** | Cellular metabolism | Nodes = metabolites; Edges = biochemical reactions | KEGG database; pathway optimization |
| **Physics** | Percolation and criticality | Nodes = sites; Edges = connectivity | Modeling superconductivity, diffusion thresholds |
| **Ecology** | Food webs | Nodes = species; Edges = feeding relationships | Analysis of energy flow and extinction cascades |
| **Conservation Biology** | Habitat fragmentation | Nodes = habitat patches; Edges = migration paths | Graph theory in corridor design |
| **Sociology** | Social interaction networks | Nodes = individuals; Edges = relationships | Zachary's karate club; diffusion of opinions |
| **Epidemiology** | Disease transmission | Nodes = people/agents; Edges = contact events | SIR models on scale-free graphs (e.g., COVID-19 modeling) |
| **Urban Planning** | Transportation systems | Nodes = stations/intersections; Edges = routes | Subway networks; traffic optimization in smart cities |
| **Electrical Engineering** | Power grid resilience | Nodes = substations; Edges = power lines | North American power grid model; blackout propagation |
| **Materials Science** | Atomic lattices & nanomaterials | Nodes = atoms; Edges = bonds | Graphene sheet modeling; topological defects |
| **Chemistry** | Reaction networks | Nodes = chemical species; Edges = reactions | Autocatalytic cycles; combustion mechanism modeling |
| **Web Science** | Hyperlink structure of the WWW | Nodes = webpages; Edges = hyperlinks | PageRank algorithm; Bow-Tie model of the web |
| **Bibliometrics** | Citation & co-authorship networks | Nodes = papers/authors; Edges = citations/collaborations | Science of science studies |
| **Computer Networks** | Autonomous systems & Internet topology | Nodes = routers/systems; Edges = IP links | BGP routing analysis; resilience testing |
| **Astronomy** | Cosmic web and galaxy clusters | Nodes = galaxies; Edges = gravitational ties | Sloan Digital Sky Survey; dark matter mapping |
| **Information Science** | Knowledge graphs & semantics | Nodes = concepts/entities; Edges = relationships | Google Knowledge Graph; ontology alignment |
| **Finace** | Models interconnections between financial institutions, market structures, and systemic risks to understand and mitigate financial crises. |  |  |
| **Recommendation System** |  |  |  |
| **Supply Chain Management** |  |  |  |
| **Cultural and Knowledge Networks** |  |  |  |

## ? QA

🧠 **Foundational Questions: What is a Network?**

1. **What are the representational powers of a network?**
    - What kinds of systems can be modeled as networks, and what kinds cannot?
    - How do networks compare to other modeling formalisms like tensors, systems of equations, or logical circuits?
2. **How do different types of networks (e.g., directed, weighted, temporal, multilayer, hypergraphs) affect what can be expressed or modeled?**
3. **What are the minimal formal components required for a network to be meaningfully defined (nodes, edges, rules)?**
4. **What structural patterns (e.g., degree distributions, motifs, modularity) can networks represent, and how are these meaningful for the system being modeled?**

🔁 **Dynamics: Networks in Time**

1. **How can we represent and simulate the dynamics of processes on networks (e.g., diffusion, epidemics, synchronization)?**
2. **What’s the distinction between *dynamics on networks* (e.g., spreading processes) vs *dynamics of networks* (e.g., link rewiring, node appearance)?**
3. **How can temporal networks and dynamic graphs model systems that change structure over time (e.g., mobile networks, neural plasticity)?**
4. **What kinds of differential or stochastic equations are naturally expressible on networks, and what constraints do network topologies place on their solution spaces?**

📐 **Structure: Measuring and Analyzing Networks**

1. **What are the most informative topological descriptors of a network, and how are they related to system behavior?**
    - Centrality measures
    - Clustering coefficients
    - Path lengths
    - Spectral properties (eigenvalues of adjacency or Laplacian matrices)
2. **How do structural patterns constrain or enable certain types of dynamics (e.g., how modularity impacts resilience or control)?**
3. **What is the relationship between local node-level rules and global network-level behavior?**
4. **How can graph entropy, complexity measures, or statistical mechanics be used to characterize networks?**

🧬 **Function: Networks as Mechanisms**

1. **How do different network topologies affect system robustness, efficiency, adaptability, and evolvability?**
2. **How can networks encode memory, control, or computation?**
3. **How do networks mediate the flow of energy, information, or material in physical, biological, or social systems?**

🧠 **Inference & Learning**

1. **Given partial or noisy data, how can we infer the underlying network structure or its parameters?**
2. **How can machine learning be used to model network dynamics or classify networks?**
3. **What are graph neural networks (GNNs), and what new representational power do they provide?**
4. **What are the limits of learnability and predictability in network-based systems?**

🔗 **Interconnected Systems: Multiscale and Multilayer Networks**

1. **How do networks interact across scales (e.g., genes–cells–organs–organisms–ecosystems)?**
2. **What are interdependent or multilayer networks, and how do failures or signals cascade across them?**
3. **How do we model feedback loops between network structure and node dynamics in adaptive or co-evolving networks?**

🧩 **Applications & Modeling**

1. **How do domain-specific constraints (biological, social, economic) shape the topology and evolution of real-world networks?**
2. **How can we design or modify networks to optimize specific functions (e.g., control, resilience, fairness, cost)?**
3. **How does the structure of a technological network (e.g., power grid, internet, supply chain) affect national or global systemic risk?**

🧰 **Epistemology and Theory-Building**

1. **To what extent is "network" a useful abstraction across domains, versus a metaphor or simplification?**
2. **Can there be a general theory of networks akin to thermodynamics or information theory?**
3. **What are the fundamental limits of what can be modeled or predicted using networks?**
4. **How do network science and complexity theory relate, overlap, or diverge?**
5. **Is there a formal way to compare two networks from different domains (e.g., brain vs internet) and determine if they are "structurally or functionally similar"?**

## References

- [Network Effect](https://en.wikipedia.org/wiki/Network_effect)
- [Network Theory](https://en.wikipedia.org/wiki/Network_theory)
- **"Random Graphs" by Paul Erdős and Alfréd Rényi (1959):** Introduced the concept of random graphs and laid the foundation for the study of complex networks.
- **"Small Worlds: The Dynamics of Networks between Order and Randomness" by Duncan J. Watts and Steven H. Strogatz (1998):** Introduced the concept of small-world networks and the Watts-Strogatz model.
- **"Emergence of Scaling in Random Networks" by Albert-László Barabási and Réka Albert (1999):** Presented the Barabási-Albert model, explaining the emergence of scale-free networks.
- **"The Structure and Function of Complex Networks" by M. E. J. Newman (2003):** A review paper that discusses various aspects of complex networks, including their structure and common properties.
- **"Community Structure in Social and Biological Networks" by M. Girvan and M. E. J. Newman (2002):** Introduced a method for detecting community structure in networks.
- **"Network Motifs: Simple Building Blocks of Complex Networks" by R. Milo et al. (2002):** Describes network motifs, recurring patterns in complex networks.
- **"The Spread of Behavior in an Online Social Network" by Damon Centola (2010):** Investigates the dynamics of behavior adoption in social networks.
- **"Network Science" by Albert-László Barabási (2016):** A comprehensive book on network science that covers various models and applications.
- **"Graph Convolutional Networks" by Thomas N. Kipf and Max Welling (2017):** Introduces graph convolutional networks, a powerful technique for deep learning on graph-structured data.
- Dorogovtsev, Sergey N., Alexander V. Goltsev, and José FF Mendes. "Critical phenomena in complex networks." *Reviews of Modern Physics* 80.4 (2008): 1275.
- https://trenton3983.github.io/posts/intro-network-analysis/
- [Graph](../mathematical/graph.md)
- https://github.com/dbremont/algorithms
- [Graph Data Model ](https://app.notion.com/p/Graph-Data-Model-1afc0f5171ec809fb444fd2da46e183f?pvs=21)
- [Graph Neural Networks (GNN)](note.html?n=technica/ais/system/architecture/graph-neural-networks-gnn.md)
- https://github.com/dbremont/algorithms/tree/main/cm/network
