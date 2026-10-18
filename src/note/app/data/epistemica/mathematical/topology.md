---
tags: [framework, topology]
---

# Topology

 : Geometry (Geometry%201acc0f5171ec809ab11ad964fbff6df1.md)

> Topology is the study of **shapes and their global structures**, focusing on properties that remain invariant under **transformations or re-arrangement** (ignoring local properties).
> 

> Open Set: …
> 

> Close Set: …
> 

> Topology: Space → Topological Structure (Space).
> 

> Why would you want to give endow a `space` with a topological structure?
> 

> Which are the topological properties?
> 

> Can we have topology on discrete sets? Graphs, Trees, Matroids, …?
> 

> Topology in physics is like a **coarse-grained map** of the system: it tells you **what cannot change continuously**, which is essential for understanding stable states, defects, and quantized observables.
> 

> Topology captures structure, not magnitude
> 

QA:

- Why this axioms capture the idea of closeness and continuity? What closeness means in **this context**?
- What elements should the axioms of a topology should capture?
    - **Basic structure** (open sets, the whole space, the empty set).
    - **Openness and closure properties** (unions, finite intersections).
    - **Separation** (how distinct points behave).
    - **Continuity** (without requiring distances).
    - **Convergence** (limits, sequences, and filters).
    - **Compactness** (generalizing finiteness).
    - **Connectedness** (determining "gaps" in space).
    - **Extensibility** (allowing advanced structures like manifolds or function spaces).

## Introduction

```bash
     ┌─────────────┐
     │   Objects   │
     │             │
     │ - Topological spaces (X, T)
     │ - Open / closed sets
     │ - Compact / connected sets
     │ - Continuous functions
     │ - Limit points, neighborhoods
     └───────┬─────┘
             │
             ▼
     ┌─────────────┐
     │  Problems   │
     │             │
     │ - Is a set compact, connected, dense?
     │ - Does a function preserve continuity?
     │ - Can the space be metrized or embedded?
     │ - What are convergence / limit properties?
     │ - What algebraic invariants exist? (π₁, homology)
     └───────┬─────┘
             │
             ▼
     ┌─────────────┐
     │ Techniques  │
     │             │
     │ - Closure / interior operations
     │ - Compactness arguments (finite subcovers)
     │ - Connectedness and separation tests
     │ - Continuity preimage checks
     │ - Sequence, net, filter analysis
     │ - Algebraic topology constructions
     └───────┬─────┘
             │
             ▼
     ┌─────────────┐
     │  Results    │
     │             │
     │ - Classification of spaces (Hausdorff, compact, etc.)
     │ - Continuity and convergence theorems
     │ - Fixed point theorems
     │ - Algebraic invariants (π₁, homology groups)
     │ - Robustness under deformation (homeomorphisms)
     └─────────────┘

```

## Formal Definition

> A topology $\mathcal{T}$ on a set $X$ is a subset of the power set $\mathcal{P}(X)$ that satisfies the three axioms above. The pair $(X, \mathcal{T})$ is called a **topological space**.
> 

A **topology** on a set $X$ is a collection $\mathcal{T}$ of subsets of $X$ (called **open sets**) that satisfies the following three axioms:

- **The empty set and the whole space are open:** $\emptyset \in \mathcal{T}, \quad X \in \mathcal{T}$
- **Closed under arbitrary unions:** If $\{ U_i \}_{i \in I}$ is a collection of open sets in $\mathcal{T}$, then their union is also in $\mathcal{T}$: $\bigcup_{i \in I} U_i \in \mathcal{T}$
- **Closed under finite intersections:** If $U_1, U_2, \dots, U_n$ are open sets in $\mathcal{T}$, then their intersection is also in $\mathcal{T}$: $\bigcap_{i=1}^{n} U_i \in \mathcal{T}$

## Topological Space

> A **topological space** is a set of points, along with a **topology**, which is a collection of **open subsets** that satisfies specific axioms allowing for the definition of continuous deformation and other topological properties.
> 

| **Topological Structure** | **Description** |
| --- | --- |
| **Topological Space** | A set equipped with a **topology**, which is a collection of open sets that satisfies certain axioms (e.g., unions and finite intersections are open). |
| **Metric Space** | A topological space where distances between points are defined by a metric, inducing a topology based on open balls. |
| **Hausdorff Space** | A topological space where any two distinct points have disjoint neighborhoods, allowing for separation of points. |
| **Compact Space** | A topological space where every open cover has a finite subcover, a crucial concept in real analysis and continuous functions. |
| **Connected Space** | A space that cannot be divided into two disjoint open sets, meaning there is no "gap" in the space. |
| **Locally Compact Space** | A space where every point has a neighborhood that is compact, often used in analysis and algebraic topology. |
| **Manifold** | A topological space that locally resembles Euclidean space (i.e., each point has a neighborhood homeomorphic to \(\mathbb{R}^n\)). |
| **Path-Connected Space** | A space where any two points can be connected by a continuous path, important for studying homotopy in algebraic topology. |
| **Homotopy Type** | A classification of spaces based on their "shape," where two spaces are homotopy equivalent if they can be continuously deformed into one another. |
| **Homology** | An algebraic structure assigned to a topological space to study its shape through chains, cycles, and boundaries. |
| **Cohomology** | Similar to homology but focuses on cochains, cocycles, and coboundaries, and it allows studying spaces using algebraic methods. |
| **Simplicial Complex** | A combinatorial object made up of vertices, edges, and higher-dimensional simplices, used to study the topology of spaces discretely. |
| **Covering Space** | A space that "covers" another space in a way that locally looks like a product space, used in the study of fundamental groups and algebraic topology. |
| **Fiber Bundle** | A space that locally looks like a product of two spaces, often used in differential geometry and gauge theory in physics. |
| **Tychonoff Space** | A completely regular space where points can be separated from closed sets by continuous functions. |
| **Topological Group** | A group equipped with a topology where the group operations (multiplication and inversion) are continuous. |
| **Topological Vector Space** | A vector space equipped with a topology that makes vector addition and scalar multiplication continuous. |
| **Lie Group** | A group that is also a smooth manifold, with group operations being smooth (differentiable), essential in geometry and theoretical physics. |
| **Discrete Topology** | A topology where every subset is open, making it the "finest" topology. |
| **Indiscrete Topology** | A topology where only the empty set and the entire set are open, making it the "coarsest" topology. |
| **Product Topology** | The topology on a product of two topological spaces, where open sets are generated by products of open sets from each space. |
| **Quotient Topology** | A topology on a set of equivalence classes induced by a continuous surjective map, commonly used in algebraic topology. |
| **Alexandrov Topology** | A topology where arbitrary intersections of open sets are still open, commonly used in theoretical computer science and order theory. |
| **Zariski Topology** | A topology often used in algebraic geometry, where the closed sets are the zero sets of polynomials, making it a "coarse" topology. |
| **Stone-Cech Compactification** | A construction that adds "points at infinity" to a space to make it compact, widely used in functional analysis and general topology. |

## $\R$

> $\text{Topology} : \R -> \text{Topological Space}$
> 

| **Property** | **Description** |
| --- | --- |
| **Hausdorff** | Any two distinct points in $\mathbb{R}$ can be separated by disjoint open sets. |
| **Connectedness** | $\mathbb{R}$ cannot be split into two disjoint open sets; it's also path-connected. |
| **Completeness** | Any Cauchy sequence in $\mathbb{R}$ converges to a limit in $\mathbb{R}$. |
| **Lindelöf Property** | Every open cover of $\mathbb{R}$ has a countable subcover. |
| **Second-Countability** | $\mathbb{R}$ has a countable basis for its topology (e.g., open intervals with rational endpoints). |
| **Separability** | $\mathbb{R}$ has a countable dense subset (e.g., the rational numbers $\mathbb{Q}$. |
| **Locally Euclidean** | Every point in $\mathbb{R}$ has a neighborhood homeomorphic to an open subset of $\mathbb{R}$. |
| **Non-Compactness** | $\mathbb{R}$ is not compact as it is unbounded, but closed intervals$[a, b]$ are compact. |
| **Metrizability** | The topology of $\mathbb{R}$ can be defined using a metric e.g., $d(x, y) = |x - y|$ |
| **Contractibility** | $\mathbb{R}$ can be continuously contracted to a point (trivial fundamental group). |
| **Monotonicity of Open Sets** | Open sets in $\mathbb{R}$ are unions of disjoint open intervals. |
| **No Compactness at Infinity** | $\mathbb{R}$ is not compact, though bounded subsets may have compact closures. |

## Toolbox

| **Concept/Tool** | **Description** |
| --- | --- |
| **Open Sets** | Fundamental building blocks of topologies. Define which points are "close" without a notion of distance. |
| **Closed Sets** | Complements of open sets. Important in defining limits and closures. |
| **Neighborhoods** | Sets that contain an open set around a point. Used to define continuity and convergence. |
| **Bases and Sub-bases** | Collections of open sets that generate a topology through unions and intersections. |
| **Interior, Closure, Boundary** | **Interior:** largest open set inside a set. <br> **Closure:** smallest closed set containing it.<br>**Boundary:** points on the edge of the set. |
| **Limit Points/Accumulation** | Points that can be approached by sequences (or nets) in the set. |
| **Compactness** | A set is compact if every open cover has a finite subcover. Generalizes finiteness in topological spaces. |
| **Connectedness** | A space is connected if it cannot be divided into two disjoint open sets. |
| **Continuity** | A function is continuous if the preimage of any open set is open. Fundamental in studying topological spaces. |
| **Homeomorphisms** | Bijective, continuous functions with continuous inverses. Define when spaces are topologically equivalent. |
| **Topological Invariants** | Properties that remain unchanged under homeomorphisms (e.g., connectedness, compactness, genus of a surface). |
| **Metric Spaces** | Spaces where distances between points are defined, inducing a topology through open balls. |
| **Hausdorff Property** | A space is Hausdorff if any two distinct points can be separated by disjoint open sets. |
| **Separation Axioms (T0, T1, T2, etc.)** | A hierarchy of conditions that describe how points and sets can be separated by open sets. |
| **Product Topology** | The topology on a product of spaces where open sets are products of open sets from each space. |
| **Quotient Topology** | The topology on a quotient space where sets are identified or "glued" together. |
| **Subspace Topology** | A topology on a subset of a topological space, induced from the larger space. |
| **Manifolds** | Spaces that locally resemble Euclidean space. Central in differential topology and geometry. |
| **Homotopy and Homotopy Equivalence** | Studies continuous deformations between spaces. Two spaces are homotopy equivalent if one can be continuously deformed into the other. |
| **Fundamental Group** | Captures the idea of loops in a space. An important algebraic invariant in topology. |
| **Covering Spaces** | Spaces that "cover" another space in a way that locally looks like a product. Important in studying fundamental groups. |
| **Compactification** | Techniques to make non-compact spaces behave like compact ones (e.g., one-point compactification). |
| **CW Complexes** | Spaces built out of cells of different dimensions. Used in algebraic topology to study spaces combinatorially. |
| **Simplicial Complexes** | Combinatorial structures made of vertices, edges, triangles, etc., used to study topological spaces. |
| **Homology and Cohomology** | Tools from algebraic topology that assign algebraic objects (e.g., groups) to spaces, revealing deeper properties. |
| **Poincaré Duality** | Relates homology and cohomology, a key concept in the study of manifolds. |
| **Fiber Bundles** | A space that looks locally like a product of two spaces, but globally can be twisted. |
| **Tychonoff Theorem** | The product of any collection of compact spaces is compact. A key result in topology. |
| **Stone-Čech Compactification** | A way to embed a space into a compact space. Used in functional analysis and topology. |
| **Metrizability** | Criteria for determining if a topology can be induced by a metric. |
| **Topological Groups** | Groups that are also topological spaces, where the group operations are continuous. |
| **Baire Category Theorem** | In a complete metric space, the intersection of countably many dense open sets is dense. Important in analysis. |

## **Properties of Spaces**

> **Topologists** are interested in **properties of spaces** that remain invariant under continuous deformations, such as stretching or bending, but not tearing or gluing. These properties reveal deep insights into the structure and behavior of the spaces.
> 

> Here are the main properties that topologists study:
> 

| **Property** | **Description** |
| --- | --- |
| **Continuity** | The core idea in topology, where a function is continuous if the preimage of any open set is open. |
| **Connectedness** | A space is connected if it cannot be divided into two disjoint non-empty open sets. |
| **Compactness** | A space is compact if every open cover has a finite subcover. Generalizes finiteness in topology. |
| **Convergence** | Topologists study how sequences (or nets) of points behave, especially in terms of limits. |
| **Separation Axioms** | Conditions that describe how distinct points or sets can be separated by neighborhoods or open sets. |
| **Hausdorff Property** | A space is Hausdorff if distinct points have disjoint neighborhoods, ensuring uniqueness of limits. |
| **Homotopy** | Continuous deformation of spaces. Spaces that can be deformed into each other are homotopy equivalent. |
| **Homology** | Studies spaces through algebraic objects like groups, reflecting how spaces can be "broken down." |
| **Compactification** | Methods of extending spaces to make them compact. |
| **Manifold Structure** | Spaces that locally resemble Euclidean spaces, used in differential topology and geometry. |
| **Path Connectedness** | A stronger form of connectedness, where any two points can be connected by a continuous path. |
| **Boundaries** | Boundaries of sets within the space, critical in defining open, closed, and compact sets. |
| **Local Properties** | Properties that hold in neighborhoods around each point, such as local compactness or local connectedness. |
| **Dimension** | The number of independent directions in a space, important in classifying spaces. |
| **Metric Properties** | When spaces have a metric, properties like distance, convergence, and compactness in metric terms. |
| **Topological Invariants** | Features of spaces that are preserved under homeomorphisms, like Euler characteristic or genus. |
| **Fundamental Group** | An algebraic structure associated with loops in a space, revealing its topological complexity. |
| **Covering Spaces** | Spaces that "cover" another in a way that reveals how the structure is repeated. |
| **Tychonoff Property** | Ensures compact spaces retain compactness in infinite product spaces, as in Tychonoff's theorem. |
| **Baire Property** | Relates to the intersection of dense open sets, important in functional analysis and topology. |

## References

- [Fundamental group](https://en.wikipedia.org/wiki/Fundamental_group)
- https://en.wikipedia.org/wiki/Topology
- https://en.wikipedia.org/wiki/List_of_topologies
- https://en.wikipedia.org/wiki/Topological_property
- https://en.wikipedia.org/wiki/Topological_deep_learning
- https://en.wikipedia.org/wiki/Topological_quantum_field_theory
- Frawley, W. (1978). Topological Linguistics. 11.
- Topology https://www.topologywithouttears.net/topbook2023.pdf
- [‣](https://app.notion.com/p/10e598edb79081cc9dc5e2f61987a266?pvs=21)
- https://en.wikipedia.org/wiki/Atlas_(topology)
- https://en.wikipedia.org/wiki/List_of_topologies
- https://news.ycombinator.com/item?id=44041738
- https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/
- https://colah.github.io/posts/2014-10-Visualizing-MNIST/
- https://colah.github.io/posts/2015-01-Visualizing-Representations/
- https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- https://nbviewer.org/gist/yoavg/d76121dfde2618422139
- https://ocw.mit.edu/courses/18-s190-introduction-to-metric-spaces-january-iap-2023/
- https://ocw.mit.edu/courses/18-901-introduction-to-topology-fall-2004/
- https://www.youtube.com/watch?v=PXIcas22MtQ&list=PLLq_gUfXAnkl8bjQh-hGQ9u24xZP9x0dx
- https://www.youtube.com/watch?v=G7ixOJDCGPc
