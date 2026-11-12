---
tags: [note, mathematics, geometry, triangle]
---

# Triangle

> A **triangle** is the three-sided polygon: the closed plane figure bounded by three straight segments meeting pairwise at three points. It is the smallest polygon, the only one whose shape its side lengths fix, and therefore the unit of every triangulation — of a surface, a survey, a truss, or a mesh.

## Definition

A triangle is a simple polygon with three vertices. Taking the polygonal definition ([Polygon](/view.html?p=notes/epistemica/mathematical/geometry/polygon.md)) at $n = 3$:

$$T = (v_0, v_1, v_2), \qquad v_i \in \mathbb{R}^2,$$

with edges $e_i = \overline{v_i v_{i+1}}$, indexed mod 3. The simplicity condition of the polygon definition reduces to a single requirement here: the three vertices must not be **collinear**, since only then do the three segments bound a non-empty region.

$$v_0, v_1, v_2 \ \text{non-collinear} \iff \det\begin{pmatrix} x_0 & y_0 & 1 \\ x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \end{pmatrix} \ne 0$$

The signed area of the triangle is half that determinant — the same quantity a surveyor computes as the *double meridian distance*.

## Formulation

$$\text{Triangle} = (\text{three non-collinear vertices},\ \text{three edges},\ \text{three interior angles})$$

A triangle is fixed, up to congruence, by any of these data sets: three sides (SSS); two sides and the included angle (SAS); two angles and a side (ASA); one side and two adjacent angles (AAS); or two sides and a non-included angle *when* the resulting configuration is unique (the ambiguous SSA case, which can give two triangles, one, or none).

## Property

Write the sides $a, b, c$ opposite the vertices $A, B, C$.

| Property | Statement |
| --- | --- |
| Angle sum | $A + B + C = \pi$ — the Euclidean reading; on a sphere it is $\pi$ plus the spherical excess |
| Exterior angle | the exterior angle at a vertex equals the sum of the two opposite interior angles |
| Triangle inequality | $a < b + c$, and correspondingly for the other sides — the condition for three lengths to admit a triangle at all |
| Area | $K = \tfrac12 bh$; $K = \tfrac12 ab \sin C$; $K = \sqrt{s(s-a)(s-b)(s-c)}$ (Heron, $s = \tfrac{a+b+c}{2}$) |
| Law of cosines | $c^2 = a^2 + b^2 - 2ab\cos C$ — reducing to the Pythagorean relation at $C = \pi/2$ |
| Law of sines | $\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} = 2R$ |
| Circumradius | $R = \dfrac{a}{2\sin A} = \dfrac{abc}{4K}$ |
| Inradius | $r = \dfrac{K}{s}$ |
| Euler line | centroid, circumcentre and orthocentre are collinear; the centroid divides the segment in ratio $2 : 1$ |
| Rigidity | the side lengths fix the shape — the only polygon with this property, hence the bracing of triangulated frameworks ([Structural Mechanics](/view.html?p=notes/technica/discipline/structural-mechanics.md)) |

## Theorems

- **Interior angle sum** — $A + B + C = \pi$ (Euclid I.32; proved from the parallel postulate, and false without it).
- **Exterior angle** — the exterior angle at a vertex equals the sum of the two opposite interior angles (Euclid I.16).
- **Congruence criteria** — SSS, SAS, ASA, AAS.
- **Similarity criteria** — AA, SSS, SAS.
- **Pythagorean theorem** — the right-triangle case of the law of cosines ([Pythagorean Theorem](/view.html?p=notes/epistemica/mathematical/geometry/pythagorean-theorem.md)).
- **Ceva and Menelaus** — concurrence of cevians and collinearity of transversal points.
- **Nine-point circle** — the midpoints, feet of altitudes, and midpoints of the orthocentre-to-vertex segments lie on one circle.

## Taxonomy

Triangles split along three independent axes — by side, by angle, and by commensurability or proportion — so a triangle belongs to one kind per axis. **Isosceles right** belongs to two axes at once, which is why the decomposition below gives it two paths rather than nesting it under one.

| Axis | Kinds |
| --- | --- |
| By side | Equilateral, Isosceles, Scalene |
| By angle | Acute, Right, Obtuse |
| By side and angle | Isosceles Right, 30-60-90 |
| By commensurability | Heronian (integer sides and area), Equable (area equals perimeter) |
| By proportion | Golden |

## Instance Decomposition

> **Boundary.** This table decomposes one epistemic instance — the triangle as an element of the geometrical sign system — down to the triangle kinds it admits and the properties and constituents it carries. The shape's own combinatorics do not grow here: each kind is decomposed by the [Geometric Shape Atlas](/corpus/notes/epistemica/mathematical/geometry/atlas.html), which renders one entry per kind.

> **Stopping rule.** A row is terminal when it names a concrete figure form (a triangle kind) or a named geometric constituent of the shape (a vertex, a median, a named invariant). No kind is decomposed into its own combinatorics.

> **Identity.** Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique, and no type segment terminates a branch. The kinds form a **lattice**, not a tree: an isosceles right triangle is both isosceles and right, so it occurs twice — once under Isosceles (the side constraint) and once under Right (the angle constraint) — and each occurrence carries its own path.

> **Typing.** The root path declares the role once: `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle. The same typing is declared in [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md); this note grows the subtree that note stops at.

| Instance Tree Path | Description |
| --- | --- |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle | The 3-sided polygon: three non-collinear vertices, three edges, three interior angles — the simplest rigid shape and the unit of every triangulation. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` | Grouping: the combinable constituents of the figure — what an edge, a vertex, or a constructed line contributes to the shape. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Vertex | A point where two sides meet; three of them, non-collinear. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Side | A straight segment between two vertices; three of them, closed end to end. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Interior Angle | The angle at a vertex inside the figure; the three sum to $\pi$. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Exterior Angle | The angle between one side extended and the adjacent side; one per vertex, summing to $2\pi$. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Median | The segment from a vertex to the midpoint of the opposite side; the three concur at the centroid. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Altitude | The perpendicular from a vertex to the line of the opposite side; the three concur at the orthocentre. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Angle Bisector | The segment splitting a vertex angle; the three concur at the incentre. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Perpendicular Bisector | The line of points equidistant from a side's endpoints; the three concur at the circumcentre. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Part) `Representation Element` (→ Instance) Midsegment | The segment joining two side midpoints; parallel to the third side and half its length. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Property` | Grouping: the invariants and derived quantities the shape carries. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Property` (→ Instance) Angle Sum | The sum of the interior angles, $\pi$ in the Euclidean plane and $\pi$ plus the excess on a sphere. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Property` (→ Instance) Triangle Inequality | Each side is shorter than the sum of the other two — the admission test for three lengths. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Property` (→ Instance) Area | The enclosed region's measure: half base times height, Heron's formula, or half the product of two sides and the sine of their angle. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Property` (→ Instance) Perimeter | The sum of the three sides. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Property` (→ Instance) Circumradius | The radius of the circle through the three vertices, $R = abc / 4K$. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Property` (→ Instance) Inradius | The radius of the inscribed circle, $r = K / s$. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Property` (→ Instance) Symmetry | The reflection axis of the isosceles triangle, three axes for the equilateral, none for the scalene. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Observable` | Grouping: what a measurement registers of the shape. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Observable` (→ Instance) Side Length | A registered side; three of them fix the shape up to congruence. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Has) `Observable` (→ Instance) Included Angle | A registered angle between two sides — the surveyor's bearing difference. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Equilateral Triangle | Three equal sides and three $60^\circ$ [angles](/view.html?p=notes/epistemica/mathematical/geometry/angle.md); regular, and a similarity class of its own. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Isosceles Triangle | Two equal sides and two equal base angles — one axis of symmetry. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Isosceles Triangle (→ Kind) Isosceles Right Triangle | The $45^\circ$–$45^\circ$–$90^\circ$ shape, with sides in ratio $1 : 1 : \sqrt{2}$ — the isosceles constraint with a right angle added. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Isosceles Triangle (→ Kind) Golden Triangle | Isosceles with leg-to-base ratio $\varphi$; its angles are $72^\circ$ and $36^\circ$, and it repeats inside the pentagon. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Scalene Triangle | No equal sides, no symmetry. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Right Triangle | One $90^\circ$ angle; its sides satisfy $a^2 + b^2 = c^2$ ([Pythagorean Theorem](/view.html?p=notes/epistemica/mathematical/geometry/pythagorean-theorem.md)). |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Right Triangle (→ Kind) Isosceles Right Triangle | The same $45^\circ$–$45^\circ$–$90^\circ$ shape under the angle constraint — the second occurrence that makes the kinds a lattice. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Right Triangle (→ Kind) 30-60-90 Triangle | The half-equilateral: sides in ratio $1 : \sqrt{3} : 2$, the triangle of every drafting set. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Acute Triangle | All angles below $90^\circ$; the circumcentre falls inside the triangle. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Obtuse Triangle | One angle above $90^\circ$; the circumcentre falls outside. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Heronian Triangle | Integer sides and integer area — the $3$-$4$-$5$ triangle is the smallest. |
| `Epistemic Element` (→ Kind) `Epistemic Representation` (→ Has) `Representational System` (→ Instance) Geometry (→ Part) `Representation Element` (→ Instance) Geometric Shape (→ Instance) Planar Shapes (→ Instance) Polygon (→ Instance) Triangle (→ Kind) Equable Triangle | Area numerically equal to perimeter — the constraint that fixes one family out of all triangles. |

## References

- https://en.wikipedia.org/wiki/Triangle
- [Euclidean Geometry](/view.html?p=notes/epistemica/mathematical/geometry/euclidean-geometry.md) — the system this figure is drawn in
- [Polygon](/view.html?p=notes/epistemica/mathematical/geometry/polygon.md) — the family the triangle belongs to
- [Angle](/view.html?p=notes/epistemica/mathematical/geometry/angle.md), [Diagonal](/view.html?p=notes/epistemica/mathematical/geometry/diagonal.md), [Trigonometry](/view.html?p=notes/epistemica/mathematical/geometry/trigonometry.md)
- [Pythagorean Theorem](/view.html?p=notes/epistemica/mathematical/geometry/pythagorean-theorem.md)
- [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md) — the decomposition this note extends
- [Geometric Shape Atlas](/corpus/notes/epistemica/mathematical/geometry/atlas.html) — one entry per triangle kind
- Euclid, *Elements*, Book I (definitions and propositions 1–32).
