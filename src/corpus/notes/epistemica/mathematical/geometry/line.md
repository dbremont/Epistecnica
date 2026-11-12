---
tags: [note, mathematics, geometry]
---

# Line

> A **line** is the straight, one-dimensional, unbounded geometric shape: the set of points traced by a point moving in a fixed direction, or the affine subspace of dimension one. It has no endpoints, no thickness, and zero curvature; in Euclidean geometry two distinct points determine exactly one line.

> **Typing.** The line is an instance of the `Elemental Shapes` branch of `Geometric Shape`: an `Epistemic Representation` → `Representational System` (Geometry) → `Representation Element` → `Geometric Shape`. Its type is unambiguous as a shape, but the term "line" is model-relative — Euclidean, affine, projective, and metric lines are different instances of the same shape role.

## Definition

A line is a primitive object in Euclidean geometry and a derived object in analytic, affine, and projective geometry:

- **Euclidean.** The unique straight path through two distinct points, extended without bound in both directions. It is not a segment (which is bounded) and not a ray (which has one endpoint).
- **Analytic.** In $\mathbb{R}^2$, the solution set of a linear equation $Ax + By + C = 0$ with $(A,B) \neq (0,0)$; in parametric form $P(t) = P_0 + t\mathbf{d}$, with $t \in \mathbb{R}$ and $\mathbf{d} \neq \mathbf{0}$.
- **Affine/vector.** A one-dimensional affine subspace $L = p + \mathbb{R}d$ of a vector space, with direction $d \neq 0$ and base point $p$.
- **Projective.** An affine line completed by one point at infinity, giving a projective line $\mathbb{P}^1$; all lines in a projective plane meet, including parallels.
- **Metric/geodesic.** In a Riemannian manifold, the generalization of the Euclidean line is the geodesic: a curve whose tangent is parallel along itself and which locally minimizes length. "Straight" is therefore model-relative, not an absolute property.

A line is not the same as a **line segment** (bounded, with two endpoints), a **ray** (one endpoint, one unbounded direction), or a **curve** (which may bend). The term is also model-dependent: a Euclidean line, an affine line, a projective line, and a hyperbolic geodesic are different objects even when they are all drawn as "straight."

## Categorization

| Category | Type | Description | Representation / invariant |
| --- | --- | --- | --- |
| By model of space | **Euclidean line** | The straight, infinite line of Euclidean geometry. | $Ax + By + C = 0$; unique through two points. |
| | **Affine line** | A one-dimensional affine subspace, with a distinguished direction but no origin. | $p + \mathbb{R}d$; invariant under affine maps. |
| | **Projective line** | An affine line plus its point at infinity. | Homogeneous coordinates; all lines meet. |
| | **Hyperbolic line** | A geodesic in hyperbolic geometry. | Unique through two points; angle sums fall short of $\pi$. |
| | **Spherical line** | A great circle: the geodesic on a sphere. | Closed, finite length, two antipodal intersections. |
| | **Algebraic line** | A degree-one algebraic curve, the simplest linear variety. | Zero set of a linear polynomial. |
| By relative position | **Coincident** | Two names for the same line. | Infinitely many common points. |
| | **Parallel** | Coplanar lines that never meet. | Equal direction, distinct offset; meet at infinity projectively. |
| | **Intersecting / secant** | Lines that meet at exactly one point. | One common point; concurrent if three or more share it. |
| | **Perpendicular** | Intersecting lines whose directions are orthogonal (they form a $90^\circ$ angle). | Direction vectors have zero inner product. |
| | **Skew** | Non-coplanar lines in three or more dimensions that never meet. | No common point; not parallel. |
| | **Transversal** | A line meeting two or more given lines. | Generates corresponding, alternate, and same-side angles. |
| By relation to a curve | **Secant line** | A line meeting a curve in two or more points. | A chord is the segment between two intersections. |
| | **Tangent line** | A line touching a curve at a point with the curve's local direction. | Matches the first derivative; limit of secants. |
| | **Normal line** | A line perpendicular to the tangent at a point. | Direction is the normal vector. |
| By representation | **Slope-intercept** | $y = mx + b$ in the plane, for non-vertical lines. | Slope $m$, intercept $b$. |
| | **Point-slope** | $y - y_1 = m(x - x_1)$. | Passes through $(x_1,y_1)$ with slope $m$. |
| | **General / standard** | $Ax + By + C = 0$. | Handles vertical lines; normal vector $(A,B)$. |
| | **Parametric / vector** | $P(t) = P_0 + t\mathbf{d}$. | Base point and direction; works in any dimension. |
| | **Normal form** | $x\cos\theta + y\sin\theta = p$. | Distance $p$ from the origin, normal angle $\theta$. |
| | **Homogeneous** | $ax + by + cz = 0$ in projective coordinates. | Projective line; handles points at infinity. |
| By ambient dimension | **Line in the plane** | A one-dimensional subset of $\mathbb{R}^2$; a hyperplane there. | Codimension 1. |
| | **Line in 3-space** | A one-dimensional subset of $\mathbb{R}^3$; intersection of two non-parallel planes. | Codimension 2; skew pairs exist. |
| | **Line in $n$-space** | A one-dimensional affine subspace of $\mathbb{R}^n$. | Codimension $n-1$. |
| By orientation | **Horizontal** | Parallel to the $x$-axis. | Slope $0$; $y = b$. |
| | **Vertical** | Parallel to the $y$-axis. | Undefined slope; $x = a$. |
| | **Oblique** | Neither horizontal nor vertical. | Non-zero, finite slope. |
| | **Coordinate axis** | A line through the origin along a basis direction. | $x$-axis, $y$-axis, $z$-axis. |
| By metric character | **Spacelike line** | A line whose tangent has positive squared length in a Lorentzian metric. | Outside the light cone. |
| | **Null / lightlike line** | A line whose tangent has zero squared length. | Light ray; lies on the light cone. |
| | **Timelike line** | A line whose tangent has negative squared length. | Inside the light cone; possible worldline. |

## Properties

- **One-dimensional.** A line has one intrinsic degree of freedom; a point on it is fixed by one parameter.
- **Straight.** Its curvature is zero; its tangent direction is constant.
- **Unbounded.** It has no endpoints and infinite length in Euclidean space.
- **No thickness.** It has zero area in the plane and zero volume in space.
- **Determined by two points.** In Euclidean and affine geometry, two distinct points determine exactly one line.
- **Shortest path.** In Euclidean geometry, the segment between two points on a line is the shortest path between them; the line is the geodesic.
- **Symmetry.** A line is invariant under translations along itself, reflections across it, and rotations about it in three dimensions.
- **Simply connected and contractible.** As a topological space it is homeomorphic to $\mathbb{R}$, hence connected, simply connected, and contractible.
- **Complete but not compact.** It is a complete metric space with the Euclidean metric, but it is not compact.

## Relations

- **Point** — the primitive incidence object; a line is a set of points.
- **Line Segment** — the bounded part of a line between two points.
- **Ray** — a half-line with one endpoint.
- [Plane](/view.html?p=notes/epistemica/mathematical/geometry/plane.md) — in the plane, a line is a hyperplane; two non-parallel planes in 3-space intersect in a line.
- [Hyperplane](/view.html?p=notes/epistemica/mathematical/geometry/hyperplane.md) — the higher-dimensional generalization; in $\mathbb{R}^2$ a hyperplane is a line.
- [Angle](/view.html?p=notes/epistemica/mathematical/geometry/angle.md) — the separation between two intersecting lines or rays.
- [Geodesic](/view.html?p=notes/epistemica/mathematical/geometry/geodesic.md) — the generalization of the straight line to curved spaces.
- [Coordinate System](/view.html?p=notes/epistemica/mathematical/geometry/coordinate-system.md) — the representation in which a line receives an equation or slope.
- [Euclidean Geometry](/view.html?p=notes/epistemica/mathematical/geometry/euclidean-geometry.md) — the axiomatic setting of the straight line.
- [Projective Geometry](/view.html?p=notes/epistemica/mathematical/geometry/projective-geometry.md) — the setting where parallel lines meet at infinity.
- [Polygon](/view.html?p=notes/epistemica/mathematical/geometry/polygon.md) — a closed chain of line segments.
- [Triangle](/view.html?p=notes/epistemica/mathematical/geometry/triangle.md) — three lines pairwise intersecting at its vertices.
- [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md) — the decomposition in which the line is an elemental shape.
- [Geometry](/view.html?p=notes/epistemica/mathematical/geometry/geometry.md) — the ambient framework of points and the model of space.

## References

- https://en.wikipedia.org/wiki/Line_(geometry)
- https://mathworld.wolfram.com/Line.html
- https://en.wikipedia.org/wiki/Affine_space
- https://en.wikipedia.org/wiki/Projective_line
- https://en.wikipedia.org/wiki/Geodesic
- https://en.wikipedia.org/wiki/Line_(geometry)#Equations_of_a_line
