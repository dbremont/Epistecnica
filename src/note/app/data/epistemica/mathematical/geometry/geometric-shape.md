---
tags: [geometry]
---

# Geometric Shape

> A **geometric shape** is the **form** of a point set — what remains of a figure once its position, orientation, and (depending on the question) its size are quotiented out. Formally, it is not the set itself but the **equivalence class** of sets related by a chosen group of transformations.

> A shape is therefore never absolute: **the group decides what counts as the same shape**. Rigid motions give congruence, similarities admit rescaling, affine maps allow shearing, and homeomorphisms reduce shape to pure topology.

## Definition

Let $S \subseteq \mathbb{R}^n$ be a point set (a *figure*) and $G$ a group acting on $\mathbb{R}^n$. Two figures $S$ and $T$ have the **same shape** (with respect to $G$) when there is $g \in G$ with

$$T = g(S).$$

The **shape** of $S$ is then its orbit $G \cdot S$ — the equivalence class, not the representative.

Three notions are routinely conflated:

| Notion | What it fixes | Varies |
| --- | --- | --- |
| **Figure / body** | the actual point set and its placement | nothing |
| **Shape** | form under $G$ | position, orientation (and scale, if $G$ allows) |
| **Size** | a metric quantity (area, volume, diameter) | form |

A **geometric property** is a predicate that is constant on each orbit — it *is* an invariant of the shape. Anything that depends on the chosen representative (its coordinates, its centroid) is a property of the figure, not of the shape.

## Formulation

$$\text{Geometric Shape} = (\text{Point set}, \text{Equivalence relation induced by } G)$$

The equivalence relation is the whole content of the definition, so the same figure has many shapes at once, one per group:

| Transformation group $G$ | Same shape when | Preserved | Example |
| --- | --- | --- | --- |
| **Isometries** (Euclidean group) | congruent | distance, angle, area, curvature | two congruent triangles |
| **Similarities** | similar | angles, ratios of lengths, shape up to scale | two circles of different radius |
| **Affine maps** | affinely equivalent | parallelism, ratios along parallel lines, convexity | circle ↔ ellipse |
| **Projective maps** | projectively equivalent | incidence, cross-ratio | conic sections of a cone |
| **Homeomorphisms** | topologically equivalent | connectedness, genus, Euler characteristic | sphere ↔ cube |
| **Ambient isotopies** | same embedding type | knot/link type | unknot ↔ trefoil (no) |

The hierarchy is nested: isometry $\subset$ similarity $\subset$ affine $\subset$ projective, and every one of them refines homeomorphism. **Reading a property as shape-dependent or shape-independent is a choice of group, not a fact about the figure.**

## Component

| Component | Description | Invariant under |
| --- | --- | --- |
| **Boundary** | the set separating interior from complement | homeomorphism |
| **Interior** | the open region enclosed | homeomorphism |
| **Vertices / corners** | points where the boundary is not smooth | similarity (as a set) |
| **Edges / faces** | the pieces of a polygonal or polyhedral boundary | combinatorial equivalence |
| **Holes / genus** | number of independent loops or handles | homeomorphism |
| **Curvature** | local bending of the boundary or surface | isometry |
| **Symmetry group** | transformations mapping the shape to itself | similarity (up to conjugation) |
| **Centroid / bounding box** | location and extent of a representative | *not* a shape invariant |

## Taxonomy

**By dimension of the ambient space**

| Dimension | Shapes | Examples |
| --- | --- | --- |
| **Elemental (degenerate)** | point, line, [plane](note.html?n=epistemica/mathematical/geometry/plane.md), [hyperplane](note.html?n=epistemica/mathematical/geometry/hyperplane.md) | a line has no interior in $\mathbb{R}^2$ |
| **1-D** | curves, polylines, circles | circle, arc, spline |
| **2-D** | polygons, disks, ellipses, fractal boundaries | [triangle](note.html?n=epistemica/mathematical/geometry/triangle.md), [polygon](note.html?n=epistemica/mathematical/geometry/polygon.md), circle |
| **3-D** | polyhedra, quadrics, surfaces | tetrahedron, cube, sphere, cylinder, cone, torus |
| **n-D** | polytopes, simplices, balls | simplex $\Delta^n$, hypercube |

**By regularity and structure**

- **Convex / concave** — every segment between two points stays inside, or not.
- **Regular / irregular** — all sides and all [angles](note.html?n=epistemica/mathematical/geometry/angle.md) equal (regular polygon, Platonic solid).
- **Simple / self-intersecting** — the boundary does not cross itself, or does.
- **Bounded / unbounded** — finite extent or not.
- **Orientable / non-orientable** — a consistent choice of side exists (plane vs Möbius strip).
- **Smooth / piecewise-linear / fractal** — differentiability class of the boundary.

A figure may be a **shape set** rather than a single connected shape (an arrangement of pieces), in which case the decomposition into components is itself part of the shape data.

## Invariants

| Property | Isometry | Similarity | Affine | Projective | Homeomorphism |
| --- | --- | --- | --- | --- | --- |
| Distance / length | ✓ | ✗ | ✗ | ✗ | ✗ |
| Angle | ✓ | ✓ | ✗ | ✗ | ✗ |
| Area (up to factor) | ✓ | ✗ | ✗ | ✗ | ✗ |
| Cross-ratio | ✓ | ✓ | ✓ | ✓ | ✗ |
| Convexity | ✓ | ✓ | ✓ | ✗ | ✗ |
| Incidence | ✓ | ✓ | ✓ | ✓ | ✗ |
| Euler characteristic | ✓ | ✓ | ✓ | ✓ | ✓ |
| Genus / number of holes | ✓ | ✓ | ✓ | ✓ | ✓ |
| Connectedness | ✓ | ✓ | ✓ | ✓ | ✓ |
| Symmetry group type | ✓ | ✓ | ✓ | ✗ | ✗ |

The bottom rows are the **topological invariants**: they survive every continuous deformation, which is why the same shape is studied by [topology](note.html?n=epistemica/mathematical/topology.md) as by geometry.

## Shape Space

Because a shape is an orbit, the collection of all shapes is itself a space: quotient the space of figures by the group. Quotienting translations, rotations, and scale yields a **shape space** — a finite-dimensional manifold on which every shape is a single point.

| Construction | Quotients out | Structure |
| --- | --- | --- |
| **Kendall shape space** | translation, rotation, scale | a manifold (or orbifold) with a Riemannian metric |
| **Procrustes distance** | as above, via optimal alignment | the geodesic distance on it |
| **Pre-shape space** | translation, scale only | a sphere, before rotation is removed |

This turns shape comparison into a metric question: two shapes are *close* when the alignment-and-deformation cost between them is small. Practical descriptors approximate that distance — moments and Fourier descriptors, medial axes, curvature signatures, and persistent homology of the boundary.

## Relations

- [Geometry](note.html?n=epistemica/mathematical/geometry/geometry.md) — the ambient framework; a geometry is the pair (points, model of space).
- [Angle](note.html?n=epistemica/mathematical/geometry/angle.md), [Triangle](note.html?n=epistemica/mathematical/geometry/triangle.md), [Polygon](note.html?n=epistemica/mathematical/geometry/polygon.md) — elementary planar shapes and their invariants.
- [Plane](note.html?n=epistemica/mathematical/geometry/plane.md), [Hyperplane](note.html?n=epistemica/mathematical/geometry/hyperplane.md) — the elemental shapes that bound and slice others.
- [Topology](note.html?n=epistemica/mathematical/topology.md) — shape up to continuous deformation.
- [Manifold](note.html?n=epistemica/mathematical/manifold.md) — the local model of shape spaces themselves.
- [Symmetry Group](note.html?n=epistemica/mathematical/symmetry-group.md) — the stabilizer of a shape inside its transformation group.
- [Convex Hull](note.html?n=epistemica/mathematical/convex-hull.md) — the smallest convex shape containing a figure.
- [Coordinate System](note.html?n=epistemica/mathematical/coordinate-system.md) — the representation a shape is written in, which the shape itself does not fix.

## QA

- **Is a shape intrinsic or extrinsic?** Both readings are legitimate: intrinsic geometry asks what an inhabitant of the shape can measure (lengths, angles, curvature along the surface), extrinsic geometry asks how the shape sits in the ambient space. A cylinder's intrinsic shape is flat, its extrinsic shape is curved.
- **Do all geometries agree on "shape"?** No — and that is the point. An affine geometry cannot tell a circle from an ellipse; a projective geometry cannot tell any two conics apart. "Same shape" is only meaningful once the group is named.
- **Is a shape a set?** Not literally: the set is a representative, the shape is the orbit. This is why two figures with different coordinates, orientations, or sizes can be the very same shape.

## References

- https://en.wikipedia.org/wiki/Shape
- https://en.wikipedia.org/wiki/Congruence_(geometry)
- https://en.wikipedia.org/wiki/Similarity_(geometry)
- https://en.wikipedia.org/wiki/Procrustes_analysis
- https://en.wikipedia.org/wiki/Euler_characteristic
