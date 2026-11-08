---
tags: [note, mathematics, framework, geometry]
order: 0
---

# Geometry

> **A Geometry** constitutes an **abstract formal system** developed for the qualitative and quantitative characterization of spatial form and structure, primarily through the representation of shape, size, and relative position. Its structure was progressively generalized to encompass broader spatial relations—such as curvature, continuity, and dimensionality—through extensions of its representational and deductive frameworks.

> **Note: The concepts of line** and angle are abstract. Different geometries can define and formalize them differently. One of the greatest developments in geometry was the realization — whether conscious or not — that these concepts **could be operationalized** within distinct **axiomatic frameworks**.

> **What is the essence of geometry?** Geometry is the mathematical language for encoding the spatial structure of reality. It abstracts properties such as distance, position, shape, size, orientation, and curvature into idealized objects—points, lines, planes, curves, and geometric figures—allowing us to reason about space independently of any particular physical object.

## Formulation

$\text{Geometry}=( \text{Points}, \text{Model of Space})$:

Where:

1. **Points** — the basic objects of the geometry.
2. **Model of Space** — the structure that characterizes how points relate to each other (distance, angles, incidence, curvature, topology, transformations, etc.).

## **Model of Space**

> **Model of Space** — the structure that characterizes how points relate to each other (distance, angles, incidence, curvature, topology, transformations, etc.).
> 

| **Category** | **Element** | **Description** |
| --- | --- | --- |
| **Metric (Measurement)** | Distance / Metric | Measure of separation between points |
|  | Angle | Rotational relation between lines or vectors |
|  | Area / Volume / Length | Measures of size for objects, surfaces, curves |
|  | Norms | Generalized vector or function size |
|  | Curvature | Local or global bending of space |
|  | Geodesics | Shortest paths between points |
| **Topological (Connectivity)** | Connectivity | Path-connectedness, loops, holes |
|  | Compactness / Boundedness | Finite extent or closure |
|  | Continuity / Smoothness | Differentiability of curves, surfaces, or maps |
|  | Homology / Homotopy | Algebraic characterization of holes, loops |
| **Incidence (Combinatorial)** | Incidence Relations | Which points lie on lines, planes, or subspaces |
|  | Adjacency / Neighborhoods | Local linking of elements |
|  | Graph / Simplicial Complex | Discrete representation of space |
| **Transformation & Symmetry** | Isometries | Transformations preserving distance |
|  | Affine Transformations | Preserve parallelism, not necessarily distance |
|  | Conformal / Projective Transformations | Preserve angles or incidence |
|  | Group Actions / Symmetry Groups | Algebraic structure defining invariances |
| **Dimensional & Orientational** | Dimensionality | Number of independent coordinates |
|  | Orientation | Handedness or consistent basis ordering |
|  | Foliations / Stratification | Decomposition into lower-dimensional subspaces |
| **Algebraic & Analytic** | Coordinate Systems | Coordinate representations |
|  | Algebraic Geometry | Spaces defined by polynomial equations |
|  | Vector & Inner Product Spaces | Enable linear combinations, projections |
|  | Manifolds / Differentiable Structures | Smooth spaces enabling calculus |
|  | Tensors / Differential Forms | Describe curvature, flux, fields |
| **Probabilistic / Stochastic** | Measure & Integration | Assign size or probability to subsets |
|  | Random Fields / Stochastic Processes | Spaces with probabilistic distributions |
|  | Ergodicity / Mixing | Statistical behavior under dynamics |

### Distance

> A measure of separation between points, which can define notions of length, metric properties, and geodesics. Examples include Euclidean distance, hyperbolic distance, and Manhattan distance.
> 

> See more in [Metric Space](/view.html?p=notes/epistemica/mathematical/space/metric-space.md).l
> 

### Angle

> A measure of the rotation between intersecting lines or vectors, used to define congruence, orthogonality, and directional relationships.
> 

> See more here [Angle](/view.html?p=notes/epistemica/mathematical/geometry/angle.md).
> 

### Metric Properties

> Additional properties derived from distance and angle, such as area, volume, length of curves, and norms.
> 

### Incidence

> Relations that describe which points lie on which lines, planes, or higher-dimensional objects, foundational in projective and affine geometries.
> 

### Curvature

> Describes how space bends locally or globally. Includes Gaussian curvature, sectional curvature, and Ricci curvature, which determine local geometric properties and global shape.
> 

### Topology

> Captures qualitative spatial properties invariant under continuous deformations, such as connectedness, compactness, holes, and boundaries.
> 

### Transformations

> The set of allowable operations that map the space onto itself while preserving some structure. Examples: rigid motions, affine transformations, conformal mappings, and diffeomorphisms.
> 

### Dimensionality

> The number of independent coordinates needed to specify a point in the space. Can vary between 1D, 2D, 3D, or higher-dimensional manifolds.
> 

### Symmetry

> Structural invariances under transformations, such as reflection, rotation, translation, or more abstract group actions. Symmetry informs conserved quantities and geometric classification.
> 

### Connectivity

> How points or regions are linked together; includes path-connectedness, simply connectedness, and the existence of loops or cycles.
> 

### Continuity / Smoothness

> Degree to which objects, curves, or surfaces in space are differentiable or continuous, important in differential geometry and analysis on manifolds.
> 

### What is the recursive instance decomposition of this epistemic instance?

> **Boundary.** This table decomposes one epistemic instance — Geometry as the representational system the geometrical corpus is written in — into the elements its inscriptions are built from, the constitutive substrate that decides what a geometry is (the note's *Model of Space*), the geometries that realize the system, and the properties the system carries. The first row declares the path; every other row extends it. The frameworks the note lists — differential, algebraic, discrete, computational, analytic, synthetic, convex, conformal, topological — are `Epistemic Framework` elements read over several geometries, not parts of this system, so they stay in `## Framework` (under `geometry/framework/`) and are linked rather than grown. The probabilistic lane (measure and integration, random fields, ergodicity) belongs to the probability corpus and is reached the same way.

> **Stopping rule.** A row is terminal when it names a concrete element, axiom system, transformation, coordinate assignment, convention, formation rule, geometry, or property. No geometry is decomposed into its own theorems, and no framework is grown here.

> **Identity.** Instance Tree Path holds instances only — never epistemic element types; every path is unique and no type segment terminates a branch. The three classical geometries differ in one `Foundation` instance, so the parallel postulate occurs twice — once as the system's own foundation and once under each geometry that asserts its own reading of it — and each occurrence carries its own path.

> **Typing.** The root path declares the role once: `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry. Geometry is the sign system itself, not an `Epistemic Framework` — a framework is a set of elements read as one lens, and this note's `framework` tag is a corpus tag, not a typing. `readable as` an `Epistemic Construction` → `Concept` when the system is taken as a constructed mathematical object, and `readable as` a `Property`-bearing element in the sense of the guide's `Has Property` row: length, angle, curvature, and dimension are predicated of it, not parts of it.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry | The geometrical sign system: the points, the figures written from them, and the model of space that says how they relate. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` | Grouping: the combinable constituents of the system — what a geometrical inscription is written from. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Point | A location with no size and no dimension — the primitive every other element is written from. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Line | A straight 1-D figure extending without end in both directions. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Line Segment | The part of a line between two points — the element a polygon side is written with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Ray | A half-line: one endpoint, unbounded in one direction. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Plane | A flat 2-D surface extending without end — the ambient element of planar geometry; see [Plane](/view.html?p=notes/epistemica/mathematical/geometry/plane.md). |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Hyperplane | The $(n-1)$-dimensional flat that slices an $n$-space; see [Hyperplane](/view.html?p=notes/epistemica/mathematical/geometry/hyperplane.md). |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Space | The whole ambient set of points a geometry is declared over — $\mathbb{R}^n$, $H^n$, $S^n$, or a manifold. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geodesic | The straight line generalized: the shortest path the space's metric admits. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape | The composite element — the form a point set carries, read as an orbit under the geometry's transformation group; its own tree is [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md). |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` | Grouping: the rules and structures that make a set of points a geometry — the note's Model of Space. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axioms a geometry is declared from. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Euclid's Postulates | The five postulates of the Elements: incidence, extension, the circle, right angles, and the parallel postulate. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Hilbert's Axioms | The twentieth-century repair of Euclid — incidence, order, congruence, continuity, and parallelism, in five groups. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Tarski's Axioms | A first-order axiomatization of Euclidean geometry in the language of betweenness and equidistance. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Incidence Axioms | The weakest layer: which points lie on which lines, and how many. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Parallel Postulate | Through a point off a line exactly one parallel passes — the axiom whose denial gives the other classical geometries. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Metric Axioms | Positivity, symmetry, the triangle inequality, and separation — what makes a distance a distance; see [Metric Space](/view.html?p=notes/epistemica/mathematical/space/metric-space.md). |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` | Grouping: the maps the geometry admits — naming the group is naming the geometry's sameness. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Isometry | A map preserving distance — the rigid motion the Euclidean plane is read up to. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Similarity | An isometry composed with a uniform scaling: angles survive, lengths scale. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Affine Transformation | Invertible affine maps: parallelism survives, distance does not. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Projective Transformation | Fractional-linear maps: only incidence and the cross-ratio survive. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Conformal Transformation | A map preserving angles — the structure complex geometry and Möbius geometry share. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Diffeomorphism | A smooth bijection with smooth inverse — the equivalence of differentiable structures. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Transformation Rule` (→ Instance) Group Action | The abstract form of every rule above: a group acting on the point set, whose orbits are the shapes. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` | Grouping: the meaning assignment from coordinates and symbols to points and quantities. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Cartesian Coordinates | The orthogonal grid: a point becomes an $n$-tuple of signed distances. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Polar Coordinates | Radius and angle: the assignment that turns rotations into translations of the angle coordinate. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Barycentric Coordinates | Weights on the vertices of a simplex — the assignment that makes affine combinations meaningful. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Homogeneous Coordinates | One extra coordinate: the assignment that writes projective maps as linear ones. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Metric Tensor | An inner product on each tangent space — the assignment that turns displacement into length. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Cross-Ratio | The projective invariant: a number assigned to four collinear points that no projection changes. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Interpretation` (→ Instance) Measure Assignment | The rule giving subsets a size — area, volume, or probability, depending on the normalization. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Convention` | Grouping: the stabilized choices that fix a presentation without changing the geometry. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Dimension Convention | Which $n$ the space is declared over, and whether a boundary counts as part of it. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Orientation Convention | Which handedness is called positive — the choice a signed volume presupposes. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Signature Convention | The signs attached to the metric's eigenvalues, as in the Lorentzian $-+++$ reading. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Convention` (→ Instance) Unit Convention | The scale a length is reported in — a presentation choice the geometry itself does not fix. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Formation` | Grouping: the rules of well-formed combination that decide what counts as an object of the space. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Well-Formed Figure | Which point sets are admitted as figures at all — a shape is defined only on these. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Incidence Structure | The abstract incidence geometry: points, lines, and the relation of lying on. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Simplicial Complex | A space assembled from vertices, edges, triangles, and their higher analogues. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Manifold Atlas | A space covered by coordinate charts with smooth transitions — the object differential geometry works on. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Constitutive Substrate` (→ Part) `Formation` (→ Instance) Foliation | A decomposition of the space into lower-dimensional leaves, stacked without crossing. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Euclidean Geometry | Flat space with the parallel postulate: distance and angle behave as in the plane; see [Euclidean Geometry](/view.html?p=notes/epistemica/mathematical/geometry/euclidean-geometry.md). |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Euclidean Geometry (→ Part) `Constitutive Substrate` | Grouping: the model of space this geometry is read with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Euclidean Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axiom that distinguishes this geometry from its neighbours. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Euclidean Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Parallel Postulate | The unique-parallel reading — the axiom that fixes the Euclidean model. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Hyperbolic Geometry | Constant negative curvature: parallels diverge and a triangle's angles sum to less than $180^\circ$. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Hyperbolic Geometry (→ Part) `Constitutive Substrate` | Grouping: the model of space this geometry is read with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Hyperbolic Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axiom that distinguishes this geometry from its neighbours. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Hyperbolic Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Hyperbolic Parallel Postulate | Through a point off a line more than one parallel passes. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Elliptic Geometry | Constant positive curvature: no parallels exist and a triangle's angles sum to more than $180^\circ$. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Elliptic Geometry (→ Part) `Constitutive Substrate` | Grouping: the model of space this geometry is read with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Elliptic Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axiom that distinguishes this geometry from its neighbours. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Elliptic Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) No-Parallel Postulate | Any two lines meet — the axiom that leaves no parallel at all. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Projective Geometry | Incidence without distance: points at infinity close the plane, and the cross-ratio is the invariant. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Projective Geometry (→ Part) `Constitutive Substrate` | Grouping: the model of space this geometry is read with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Projective Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axiom that distinguishes this geometry from its neighbours. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Projective Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Projective Incidence Axioms | Every two lines meet in exactly one point, and every two points determine exactly one line. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Affine Geometry | Parallelism without angle or length — the geometry of the affine group. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Affine Geometry (→ Part) `Constitutive Substrate` | Grouping: the model of space this geometry is read with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Affine Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axiom that distinguishes this geometry from its neighbours. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Affine Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Affine Incidence Axioms | Parallels are unique and never meet; no metric is asserted. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Riemannian Geometry | A smooth manifold with a metric tensor: lengths, angles, and curvature vary from point to point. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Riemannian Geometry (→ Part) `Constitutive Substrate` | Grouping: the model of space this geometry is read with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Riemannian Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axiom that distinguishes this geometry from its neighbours. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Riemannian Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Riemannian Metric Axioms | A smoothly varying positive-definite inner product on each tangent space. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Finsler Geometry | A Riemannian generalization whose tangent-space norm need not come from an inner product. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Finsler Geometry (→ Part) `Constitutive Substrate` | Grouping: the model of space this geometry is read with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Finsler Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axiom that distinguishes this geometry from its neighbours. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Finsler Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Finsler Norm Axioms | A smoothly varying norm, positively homogeneous and convex, on each tangent space. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Symplectic Geometry | The geometry of phase space: a closed non-degenerate 2-form, and the structure Hamiltonian mechanics preserves. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Symplectic Geometry (→ Part) `Constitutive Substrate` | Grouping: the model of space this geometry is read with. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Symplectic Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` | Grouping: the axiom that distinguishes this geometry from its neighbours. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Instance) Symplectic Geometry (→ Part) `Constitutive Substrate` (→ Part) `Foundation` (→ Instance) Symplectic Form Axioms | A closed non-degenerate 2-form $\omega$ on an even-dimensional manifold. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Length | The measure the metric assigns to a curve — a derived quantity, not an element. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Angle | The rotational relation between two elements, measurable once a metric or a conformal structure is fixed. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Area | The 2-D measure a region carries — defined only where a measure assignment exists. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Volume | The 3-D measure of a solid — the same assignment one dimension up. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Metric | The rule quantifying separation: present in metric geometries, absent in projective ones. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Curvature | The local or global bending of the space — zero, positive, or negative, and the discriminator between the classical geometries. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Dimension | The number of independent coordinates — the parameter by which the geometries are stratified. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Orientation | A consistent handedness: whether the space admits a globally consistent basis ordering. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Compactness | Whether every open cover has a finite subcover — the closed-and-bounded reading in Euclidean space. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Connectedness | Whether the space is one piece, and whether its loops can be contracted. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Smoothness | The differentiability class the space supports — what differential geometry needs and discrete geometry does without. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Has Property) `Property` (→ Instance) Symmetry | The invariance group of the space itself, as against the shapes it carries. |

## Abstract Kernel

> 

| **Category** | **Abstraction** | **Description** |
| --- | --- | --- |
| Elemental | Point | A location in space with no size or dimension. |
|  | Line | A straight one-dimensional figure extending infinitely in both directions. |
|  | Plane | A flat two-dimensional surface extending infinitely in all directions. |
|  | Space |  |
| **[Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md)** | Circle | A set of points equidistant from a center point. |
|  | Triangle | A three-sided polygon with three vertices and three angles. |
|  | Polygon | A closed shape with straight sides (e.g., square, pentagon, hexagon). |
| **Solid** | Cube | A three-dimensional shape with six square faces. |
|  | Sphere | A perfectly round three-dimensional object where all points are equidistant from the center. |
|  | Cylinder | A three-dimensional shape with two parallel circular bases connected by a curved surface. |
| **Measurement** | Length | The measure of distance between two points. |
|  | Angle | The measure of rotation between two intersecting lines (in degrees or radians). |
|  | Area | The measure of space within a two-dimensional boundary. |
|  | Volume | The measure of space occupied by a three-dimensional object. |
| **Transformation** | Translation (Shift) | Moving an object without rotating or resizing it. |
|  | Rotation | Turning an object around a fixed point (or axis in 3D). |
|  | Reflection (Flip) | Creating a mirror image of an object over a line or plane. |
|  | Scaling (Dilation) | Resizing an object uniformly or non-uniformly. |
| **Advanced** | Vector | A quantity with both magnitude and direction (used in physics and geometry). |
|  | Coordinate System | A system (e.g., Cartesian, Polar) to define positions in space. |
|  | Topology | Study of properties preserved under continuous deformations (e.g., stretching). |
|  | Symmetry | Invariance under a group of transformations. |
|  | Metric | A rule for quantifying distance between points. |
|  | Dimension | The number of coordinates needed to describe a point. |
|  | Manifold | A space that **locally** resembles **Euclidean space**. |
|  | Geodesic | ChatGPT said:A **geodesic** is the generalization of a "straight line" to curved spaces. It represents the shortest path between two points in a given geometry or manifold, taking into account the space's curvature and metric. |

## Geometry

> $\text{Geometry}=( \text{Points}, \text{Model of Space})$.
> 

> A **Geometry** is a system to say look here is a set of points; and a set of **rules**.
> 

| Geometry | **Description** | **Space** | **Model of the Space** |
| --- | --- | --- | --- |
| **Euclidean Geometry** | Studies shapes and figures in flat, two- and three-dimensional space, based on Euclid's postulates. | $\mathbb{R}^n$, flat space | Distance and angle measurements; parallelism; rigid motions preserve shape. |
| **Hyperbolic Geometry** | Geometry of negatively curved spaces where parallel lines diverge. | Hyperbolic space ($H^n$) | Hyperbolic distance metric; angle sum of triangle < 180°; parallel lines diverge. |
| **Elliptic Geometry** | Geometry on positively curved surfaces where no parallel lines exist. | Spherical / elliptic space ($S^n$) | Distance along great circles; angle sum of triangle > 180°; no parallel lines. |
| **Projective Geometry** | Studies properties invariant under projection; removes the notion of distance. | Projective space ($P^n$) | Incidence relations; cross-ratio invariant; points at infinity. |
| **Affine Geometry** | Generalizes Euclidean geometry by preserving parallelism but not angles or lengths. | Affine space ($A^n$) | Parallelism preserved; ratios along parallel lines; affine transformations. |
| Riemannian Geometry | Geometry of smooth manifolds with a smoothly varying inner product on tangent spaces. | Riemannian manifolds | Metric tensor defines lengths, angles, areas, volumes; geodesics and curvature. |
| **Finsler Geometry** | Generalizes Riemannian Geometry with norms that may vary point by point. | Finsler manifolds | Distance from a point defined by a norm on each tangent space; possibly non-quadratic. |

## Framework

> Note: These are not geometries itself $( \text{Points}, \text{Model of Space})$, but a general set of tools to deal with a specific or even classes of geometries.
> 

| **Framework** | **Description** | Geometry(s) |
| --- | --- | --- |
| [**Differential Geometry**](/view.html?p=notes/epistemica/mathematical/geometry/framework/differential-geometry.md) | Uses calculus to study smooth curves, surfaces, and manifolds. | Riemannian Geometry, Lorentzian Geometry, Classical Euclidean Geometry (smooth version) |
| [**Algebraic Geometry**](/view.html?p=notes/epistemica/mathematical/geometry/framework/algebraic-geometry.md) | Studies solutions to polynomial equations using algebraic methods. | Affine Geometry, Projective Geometry, Complex Geometry |
| **Discrete Geometry** | Studies combinatorial properties of discrete sets of geometric objects. | Combinatorial Geometry, Lattice Geometry, Polyhedral Geometry |
| [**Computational Geometry**](/view.html?p=notes/epistemica/mathematical/geometry/framework/computational-geometry.md) | Focuses on algorithms to solve geometric problems. | Euclidean Geometry, Convex Geometry, Graph Drawing Geometry |
| [**Analytic Geometry**](/view.html?p=notes/epistemica/mathematical/geometry/framework/analytical-geometry.md) | Represents geometric objects using coordinates and equations. | Euclidean Geometry, Affine Geometry, Coordinate-Based Geometries |
| **Synthetic Geometry** | Studies geometry based on axioms and logical reasoning rather than coordinates. | Euclidean Geometry, Projective Geometry, Hyperbolic Geometry |
| **Convex Geometry** | Studies convex sets and their properties. | Euclidean Geometry (Convex subsets), Affine Geometry, Functional Analysis Geometry |
| **Conformal Geometry** | Studies transformations preserving angles. | Complex Geometry, Riemannian Geometry, Möbius Geometry |
| **Topological Geometry** | Studies properties invariant under continuous deformations. | Topology, Manifold Theory, Knot Theory |

## QA

- How a **neural network** can induce a **new geometry**? A neural network induces a new geometry by:
    - Transforming input data into embeddings that lie on a learned manifold.
    - Defining a metric or distance function in the embedding space.
    - Applying geometric constraints or priors through architecture and loss functions.
    - Discovering emergent geometric structures in latent spaces.
- Note. New Geometry → New Theory of Optimization !!!

## References

- https://en.wikipedia.org/wiki/Geometry
- https://en.wikipedia.org/wiki/Symplectic_geometry
- https://ocw.mit.edu/courses/18-950-differential-geometry-fall-2008/
- https://ocw.mit.edu/courses/18-969-topics-in-geometry-dirac-geometry-fall-2006/
- https://ocw.mit.edu/courses/18-238-geometry-and-quantum-field-theory-spring-2023/
- https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/
- [https://old.reddit.com/r/math/comments/1bgvw2w/what_would_be_the_modern_definition_of_geometry/kv9s0u8/](https://old.reddit.com/r/math/comments/1bgvw2w/what_would_be_the_modern_definition_of_geometry/kv9s0u8/)


- Trigonometry (Trigonometry%201d6c0f5171ec80529c03fd3d402539db.md),
- Euclidean  Geometry (Euclidean%20Geometry%20858b34433a204b55bb716919101bdcc6.md),
- Space (Space%2019fc0f5171ec80a88882f0b8b4d96331.md),
- Manifold (Manifold%200a4e49f73dc6401b986c5ea752d80e82.md),
- Differential Geometry (Differential%20Geometry%20d543872c434348ec8c1e44264d4bd12f.md),
- Topology (Topology%2000244dc03b6546dfa5c60959b8f007ed.md)




