---
tags: [discrete]
---

# Graph

 : Tree (Tree%201bcc0f5171ec806ea4a7c83038197f13.md), Hypergraph (Hypergraph%20111c0f5171ec80c39ee4ea4cc528e3ea.md), Planarity (Planarity%202eac0f5171ec8075970fdb7b746a15b3.md)

> In computer science and mathematics, a **graph** is a collection of nodes or vertices, and edges or links that connect pairs of nodes. **Graphs** are used to represent relationships between objects or entities, such as cities in a **transportation network**, websites in a **web graph**, or people in a **social network**.
> 

> A **graph** can be represented visually as a set of dots or circles (vertices) connected by lines or arcs (edges). The vertices can be labeled or numbered to indicate their identity or properties, and the edges can be weighted to represent the strength or importance of the connection.
> 

> **Graph Theory** is a branch of mathematics that studies the properties of graphs and their applications in various fields, such as computer science, operations research, and social sciences.
> 

> Graph theory is the study of graphs, which are mathematical structures used to model relationships between objects. Graph theory is used in computer science, social network analysis, and optimization problems. In nature, graph theory can be used to model the structure of biological networks, such as metabolic pathways and neural networks.
> 

> Network theory is the study of how nodes and edges connect to form complex systems. In nature, network theory can be used to study the structure of food webs, social networks, and transportation systems.
> 

> Graph: A collection of **vertices (nodes)** connected by **edges (links)**.
> 

> Vertex (Node): A fundamental unit of a graph, representing an entity.
> 

> Edge (Link): A connection between two vertices, representing a relationship.
> 

> **Degree of a Vertex: The number of edges connected to a vertex.**
> 

> Path: A sequence of vertices connected by edges.
> 

> Cycle: A path that starts and ends at the same vertex with no repeated edges.
> 

> Connected Graph: A graph where there is a path between every pair of vertices.
> 

> Tree: A connected graph with no cycles.
> 

> Bipartite Graph:  A graph whose vertices can be divided into two disjoint sets.
> 

> Complete Graph: A graph where every pair of vertices is connected by an edge.
> 

> Subgraph: A graph formed from a subset of vertices and edges of another graph.
> 

> Adjacency Matrix: A matrix representation of a graph, where rows and columns represent vertices.
> 

> Adjacency List:  A list representation of a graph, where each vertex has a list of neighbors.
> 

> Graph Traversal: Visiting all vertices in a graph systematically (e.g., BFS, DFS).
> 

> Breadth-First Search (BFS): A traversal algorithm that explores all neighbors at the present depth before moving deeper.
> 

> Depth-First Search (DFS): A traversal algorithm that explores as far as possible along each branch before backtracking.
> 

> Shortest Path: The path between two vertices with the minimum total edge weight.
> 

> Minimum Spanning Tree (MST): A subset of edges that connects all vertices with the minimum total edge weight.
> 

> Eulerian Path:  A path that visits every edge exactly once.
> 

> Hamiltonian Path: A path that visits every vertex exactly once.
> 

> Planar Graph: A graph that can be drawn on a plane without any edges crossing.
> 

> Graph Coloring: Assigning colors to vertices so that no two adjacent vertices share the same color.
> 

QA:

- …

## Representation

> 

| **Method** | **Description** | **Advantages** | **Use Cases** |
| --- | --- | --- | --- |
| **Adjacency Matrix** | A 2D array where rows and columns represent nodes, and values indicate edges. | Simple, fast for checking if an edge exists between nodes. | Dense graphs, small to medium-sized graphs. |
| **Adjacency List** | A list where each node has a list of its neighbors. | Space-efficient for sparse graphs. Easy to traverse neighbors. | Sparse graphs, large graphs with fewer edges. |
| **Edge List** | A list of all edges in the graph, typically as pairs of nodes. | Simple, compact representation. Useful for storing edge data. | Graphs with a simple structure, algorithms requiring edge-based data. |
| **Incidence Matrix** | A matrix where rows represent edges, and columns represent nodes. Each entry is 1 if the node is part of the edge, otherwise 0. | Can represent directed and undirected graphs. | Algorithms that require edge-node relationship data. |
| **Adjacency Set** | A set of neighbors for each node (similar to adjacency list but using sets). | Efficient for graphs with a lot of insertions/deletions. | Dynamic, mutable graphs. |
| **Object-Oriented (OO) Representation** | Uses objects to represent nodes and edges. Nodes have properties and methods to access adjacent nodes. | Rich, flexible, and suitable for graphs with additional metadata. | Complex graphs with additional data attached to nodes or edges. |
| **Sparse Matrix** | A matrix with a large number of zeros is stored efficiently using special techniques like compressed sparse row (CSR). | Efficient space usage for graphs with a large number of nodes and few edges. | Sparse graphs, especially when adjacency matrix representation is needed. |
| **Laplacian Matrix**  | .. | … | … |

## Property

> Which are the properties that belongs to graphs?
> 

| **Property** | **Description** |
| --- | --- |
| **Order** | Number of vertices: ( |
| **Size** | Number of edges: ( |
| **Directionality** | Whether edges are **directed** or **undirected**. |
| **Weightedness** | Whether edges (or vertices) carry numerical weights. |
| **Simplicity** | Whether the graph has no self-loops or parallel edges (simple vs. multigraph). |
| **Degree** | Number of incident edges to a vertex (in-degree / out-degree for directed graphs). |
| **Degree Distribution** | Statistical distribution of vertex degrees across the graph. |
| **Connectivity** | Whether every vertex is reachable from every other (connected, disconnected, strongly/weakly connected). |
| **Components** | Maximal connected subgraphs within a graph. |
| **Path Existence** | Whether paths exist between vertex pairs. |
| **Diameter** | Length of the longest shortest path between any two vertices. |
| **Radius** | Minimum eccentricity among all vertices. |
| **Eccentricity** | Maximum shortest-path distance from a vertex to any other vertex. |
| **Cyclicity** | Whether the graph contains cycles (acyclic vs. cyclic). |
| **Planarity** | Whether the graph can be drawn in the plane without edge crossings. |
| **Bipartiteness** | Whether vertices can be partitioned into two disjoint sets with edges only between sets. |
| **Regularity** | Whether all vertices have the same degree. |
| **Tree Structure** | Whether the graph is connected and acyclic. |
| **Density** | Ratio of existing edges to the maximum possible number of edges. |
| **Transitivity / Clustering Coefficient** | Likelihood that adjacent vertices are themselves connected. |
| **Centrality Measures** | Quantitative importance of vertices (degree, betweenness, closeness, eigenvector). |
| **Symmetry / Automorphisms** | Structural invariances under vertex relabeling. |
| **Flow Capacity** | Edge capacity constraints in flow networks. |
| **Labeling / Attributes** | Presence of labels or properties on vertices or edges. |

## Taxonomy

> Directed Graph: A graph where edges have a direction (from one vertex to another).
> 

> Undirected Graph: A graph where edges have no direction.
> 

> Weighted Graph: A graph where edges have weights (numerical values).
> 

> 

| **Graph Type** | **Description** | **Example Use Cases** |
| --- | --- | --- |
| **Undirected Graph** | Edges have no direction; connections are bidirectional. | Social Networks, Road Maps |
| **Directed Graph (Digraph)** | Edges have a direction (from one node to another). | Web Page Links, Workflow Models |
| **Weighted Graph** | Edges have weights (representing cost, distance, etc.). | Shortest Path (Dijkstra’s Algorithm), Neural Networks |
| **Unweighted Graph** | Edges do not have weights; only structure matters. | Basic Social Networks, Tree Structures |
| **Cyclic Graph** | Contains at least one cycle (a path returning to the starting node). | Feedback Systems, Networking Protocols |
| **Acyclic Graph (DAG)** | No cycles; used for dependencies and ordering. | Task Scheduling, Compiler Optimizations |
| **Tree** | A connected, acyclic graph with one root node. | File Systems, Decision Trees |
| **Forest** | A collection of disjoint trees. | Hierarchical Clustering, Network Design |
| **Bipartite Graph** | Nodes can be divided into two sets; edges connect only between sets. | Matching Problems, Recommender Systems |
| **Complete Graph** | Every node is connected to every other node. | Fully Connected Networks, Graph Theory |
| **Sparse Graph** | Few edges relative to nodes. | Large-Scale Networks, Road Maps |
| **Dense Graph** | Many edges relative to nodes. | Neural Networks, Fully Connected Systems |
| **Planar Graph** | Can be drawn without edges crossing. | Geographic Mapping, Circuit Design |
| **Connected Graph** | Every node is reachable from every other node. | Transportation Networks, Communication Systems |
| **Disconnected Graph** | Some nodes are not reachable from others. | Faulty Networks, Clustered Systems |
| **Hypergraph** | Edges can connect more than two nodes. | Database Relationships, Set Systems |
| **Multigraph** | Can have multiple edges between the same pair of nodes. | Transport Networks (multiple roads between cities) |
| **Expander Graph** | Highly connected but sparse, used for efficient communication. | Error Correction, Network Design |

## Problem Space

- Finding a Eulerian Path
- Finding a Hamiltonian Path

## Algorithm

> These are a class of problems related to graphs, such as finding the shortest path between two nodes, identifying cycles, and finding the maximum flow in a network.
> 
- **Dijkstra’s algorithm**: A shortest-path algorithm that finds the shortest path between a starting node and all other nodes in a weighted graph.
- **Bellman-Ford algorithm**: Another shortest-path algorithm that works on graphs with negative edge weights, but can be slower than Dijkstra’s algorithm.
- **Prim’s algorithm**: A minimum-spanning-tree algorithm that finds the minimum-weight tree that connects all nodes in a graph.
- **Kruskal’s algorithm**: Another minimum-spanning-tree algorithm that works by adding edges in order of increasing weight until all nodes are connected.
- **Floyd-Warshall algorithm**: An all-pairs shortest-path algorithm that finds the shortest path between all pairs of nodes in a weighted graph.
- **Topological sorting**: An algorithm that orders the nodes in a directed acyclic graph (DAG) such that every node appears before any node that depends on it.
- **Maximum flow algorithms**: These algorithms find the maximum flow between two nodes in a flow network, which models a system of pipes or channels with limited capacity.
- **Bipartite graph matching algorithms**: These algorithms find a maximum matching between two sets of nodes in a bipartite graph, which models a system where objects are divided into two distinct categories.

## Field

> Which field in math  - or other are provide a toolbox to analyze graphs?
> 

| Field | Description |
| --- | --- |
| **Classical Graph Theory** | Studies combinatorial properties of graphs, e.g., coloring, trees, cycles, connectivity. |
| **Extremal Graph Theory** | Focuses on maximal or minimal properties of graphs, such as Turán-type problems and Ramsey theory. |
| **Random Graphs** | Analyzes graph properties in probabilistic models, e.g., Erdős–Rényi graphs, thresholds, phase transitions. |
| **Algebraic Graph Theory** | Uses algebraic structures and invariants, such as groups, adjacency matrices, and automorphisms. |
| **Spectral Graph Theory** | Studies eigenvalues and eigenvectors of graph matrices (adjacency, Laplacian) for clustering, dynamics, and robustness. |
| **Topological Graph Theory** | Examines graph embeddings on surfaces and topological constraints, e.g., planarity and genus. |
| **Graph Signal Processing** | Applies Fourier-like analysis and filtering to signals defined on graph nodes. |
| **Network Science** | Empirically studies real-world networks, including centrality, community structure, and motif analysis. |
| **Dynamical Systems on Graphs** | Models dynamics of nodes and edges, e.g., epidemics, consensus, and synchronization. |
| **Optimization & Operations Research** | Uses combinatorial and continuous optimization for shortest paths, flows, matchings, and network design. |

## References

- [CS224W: Machine Learning with Graphs](http://web.stanford.edu/class/cs224w/)
- [Graph Neural Network](https://en.wikipedia.org/wiki/Graph_neural_network)
- [Graph Theory](https://en.wikipedia.org/wiki/Graph_theory)
- [Random Graph](https://en.wikipedia.org/wiki/Random_graph)
- [Vensim](https://vensim.com/)
- Sowa, John F. “Conceptual graphs for a data base interface.” IBM Journal of Research and Development 20.4 (1976): 336-357.
- Newman, M. (2010). Networks: An Introduction. Oxford: Oxford University Press.
- Newman, M. E. J. (2003). The Structure and Function of Complex Networks. SIAM Review, 45 (2), 167–256.
- Uzzi, B., Amaral, L. A., & Reed-Tsochas, F. (2007). Small-world networks and management science research: A review. European Management Review, 4 (2), 77–91. doi:10.1057/palgrave.emr.1500078
- Kronecker Graphs: An Approach to Modeling Networks https://cs.stanford.edu/~jure/pubs/kronecker-jmlr10.pdf
- Associative Arrays: Unified Mathematics for Spreadsheets, Databases, Matrices, and Graphs https://arxiv.org/pdf/1501.05709.pdf
- https://www.youtube.com/watch?v=uTUVhsxdGS8
- https://www.youtube.com/playlist?list=PLgKuh-lKre12YBy6mn8k8spPp19F-V8K9
- https://arxiv.org/abs/1609.08072
