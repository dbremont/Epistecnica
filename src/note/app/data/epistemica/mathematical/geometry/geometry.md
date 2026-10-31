---
tags: [framework, geometry]
order: 0
---

# Geometry

 : Trigonometry (Trigonometry%201d6c0f5171ec80529c03fd3d402539db.md), Euclidean  Geometry (Euclidean%20Geometry%20858b34433a204b55bb716919101bdcc6.md), Space (Space%2019fc0f5171ec80a88882f0b8b4d96331.md), Manifold (Manifold%200a4e49f73dc6401b986c5ea752d80e82.md), Differential Geometry (Differential%20Geometry%20d543872c434348ec8c1e44264d4bd12f.md), Topology (Topology%2000244dc03b6546dfa5c60959b8f007ed.md)

> **<<A Geometry>>>** constitutes an **abstract formal system** developed for the qualitative and quantitative characterization of spatial form and structure, primarily through the representation of shape, size, and relative position. Its structure was progressively generalized to encompass broader spatial relations—such as curvature, continuity, and dimensionality—through extensions of its representational and deductive frameworks.
> 

> **Note: The concepts of line** and angle are abstract. Different geometries can define and formalize them differently. One of the greatest developments in geometry was the realization — whether conscious or not — that these concepts **could be operationalized** within distinct **axiomatic frameworks**.
> 

> **What is the essence of geometry?** Geometry is the mathematical language for encoding the spatial structure of reality. It abstracts properties such as distance, position, shape, size, orientation, and curvature into idealized objects—points, lines, planes, curves, and geometric figures—allowing us to reason about space independently of any particular physical object.
> 

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

> See more in [Metric Space](note.html?n=epistemica/mathematical/space/metric-space.md).l
> 

### Angle

> A measure of the rotation between intersecting lines or vectors, used to define congruence, orthogonality, and directional relationships.
> 

> See more here [Angle](note.html?n=epistemica/mathematical/geometry/angle.md).
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

## Abstract Kernel

> 

| **Category** | **Abstraction** | **Description** |
| --- | --- | --- |
| Elemental | Point | A location in space with no size or dimension. |
|  | Line | A straight one-dimensional figure extending infinitely in both directions. |
|  | Plane | A flat two-dimensional surface extending infinitely in all directions. |
|  | Space |  |
| **[Shape](note.html?n=epistemica/mathematical/geometry/geometric-shape.md)** | Circle | A set of points equidistant from a center point. |
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
| **Differential Geometry** | Uses calculus to study smooth curves, surfaces, and manifolds. | Riemannian Geometry, Lorentzian Geometry, Classical Euclidean Geometry (smooth version) |
| **Algebraic Geometry** | Studies solutions to polynomial equations using algebraic methods. | Affine Geometry, Projective Geometry, Complex Geometry |
| **Discrete Geometry** | Studies combinatorial properties of discrete sets of geometric objects. | Combinatorial Geometry, Lattice Geometry, Polyhedral Geometry |
| **Computational Geometry** | Focuses on algorithms to solve geometric problems. | Euclidean Geometry, Convex Geometry, Graph Drawing Geometry |
| **Analytic Geometry** | Represents geometric objects using coordinates and equations. | Euclidean Geometry, Affine Geometry, Coordinate-Based Geometries |
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
