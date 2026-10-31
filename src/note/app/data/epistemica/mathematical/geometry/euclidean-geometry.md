---
tags: [geometry]
---

# Euclidean  Geometry

 : Polygon (Polygon%20185c0f5171ec805c9745e0c18c2a33f5.md), Diagonal (Diagonal%20185c0f5171ec808f8075d43d61c4bfc6.md), Angle (Angle%20178c0f5171ec808fac84f62329514e7a.md), Coordinate System (Coordinate%20System%207763fb7722714fa6a95098fd9f1cae44.md), Metric Space (Metric%20Space%20a96a5c7274d445188d654c88e86e43a0.md), Trigonometry (Trigonometry%201d6c0f5171ec80529c03fd3d402539db.md), Geometry (Geometry%201acc0f5171ec809ab11ad964fbff6df1.md), Triangle (Triangle%201e8c0f5171ec80b196cbdba6b560cea8.md), Plane (Plane%20247c0f5171ec80ccab77d110057bebbd.md), Euclidean Space (Euclidean%20Space%2032ac0f5171ec809c896dc23d0c539093.md)

> **Classical Geometry** focuses on the **construction** and properties of shapes using axioms and deductive reasoning, modern geometry frequently incorporates algebraic and analytical methods. Analysis, in particular, plays a crucial role in solving complex geometric problems, such as in differential geometry, where calculus is used to study curves, surfaces, and their properties. Thus, geometry is not inherently separate from analytical methods; rather, analysis expands its toolkit, enabling the solution of more abstract and higher-dimensional problems.
> 

> Geometry consists of an **underlying topological space** (a manifold, for example) and some ***structure* on this space**. The structure is an analogy of some tool – such as a ruler or compass – that enables you to see *more*  than what the topology sees. It might be something that  enables you,  for example, to “measure angles and distances” (Riemannian geometry), or
 “just to measure angles” (Conformal geometry), or “to see what are  lines and what are not lines” (Projective geometry), or some other, more  abstract analog of a “ruler and compass”.
> 

> The **perimeter** is the total length of the boundaries of a two-dimensional shape or figure, calculated by summing the lengths of all its sides.
> 

> A **scaled copy** of an image is a copy that may be larger or smaller, but isn't distorted. [Useful to Find Angles]
> 

> **Vertex**: … [You can use calculus to get this].
> 

## Abstract Kernel

> 

| **Abstraction** | **Properties** |
| --- | --- |
| **Point** | No dimensions; defined by a location in space. |
| **Line** | One-dimensional; extends infinitely in both directions; defined by two points. |
| **Line Segment** | A portion of a line bounded by two endpoints; has a definite length. |
| **Ray** | A part of a line that starts at a point and extends infinitely in one direction. |
| **Angle** | Formed by two rays sharing a common endpoint (the vertex); measured in degrees or radians. |
| **Triangle** | A three-sided polygon defined by three vertices and three edges; sum of interior angles equals 180°. |
| **Quadrilateral** | A four-sided polygon with four vertices; can be convex or concave. |
| **Circle** | A set of points equidistant from a center point; defined by radius and diameter. |
| **Ellipse** | A closed curve where the sum of the distances from two foci is constant; defined by major and minor axes. |
| **Polygon** | A closed figure formed by three or more straight line segments. |
| **Regular Polygon** | A polygon with all sides and angles equal (e.g., equilateral triangle, square). |
| **Parallelogram** | A four-sided figure with opposite sides parallel and equal in length; includes rectangles and rhombuses. |
| **Trapezoid** | A four-sided figure with at least one pair of parallel sides. |
| **Rhombus** | A parallelogram with all sides of equal length; diagonals bisect each other at right angles. |
| **Square** | A regular quadrilateral with four equal sides and four right angles. |
| **Rectangle** | A quadrilateral with opposite sides equal and four right angles. |

## Angle

> Formed by two rays sharing a common endpoint (the vertex); measured in degrees or radians.
> 

- Relations between sided of polygons, an angle?
- …

## Space Model

> aka Euclidean Space
> 

> A finite-dimensional space defined by Euclidean geometry, including notions of distance and **angle**.
> 

> An object exists in a space, but that object can often be viewed as a space itself, depending on how you define it.
> 

QA:

- What makes a **space Euclidean**?
- What is the goal of **modelling a space**?
- Which building blocks are used to endow a set of points with structure so that it **becomes a space**?
- What is the connection between objects and space? Let's say a line in the 2d plane.
- Which are the representational powers of E**uclidean space?**
- Which are the representational limits of E**uclidean space?**

### What makes a **space `Euclidean`**?

> A space is **Euclidean** if it satisfies the properties of **Euclidean geometry**, which were originally formulated by Euclid in his *Elements*.
> 

- **Flatness (Zero Curvature):** The space has zero intrinsic curvature. Parallel lines remain equidistant and never intersect. The sum of angles in a triangle is always **180°**.
- **Dimensionality**:  A Euclidean space can have any finite number of dimensions n, denoted as **$\mathbb{R}^n$**.
- Cartesian Coordinate System: Distances and angles can be computed using simple algebraic formulas.
- Inner Product Structure (Dot Product)
- Euclidean Distance Metric
- Affine Structure
- Homogeneity: The space is **homogeneous**: it looks the same at every point (no preferred location).
- Isotropy: It is **isotropic**: it looks the same in every direction (no preferred direction).
- Group of Transformations (Euclidean Group)

## Figure Taxonomy

> A **geometrical figure** is any set of points in space that forms a shape or configuration with specific spatial properties such as length, area, angle, or curvature.
> 

> A **geometrical figure** is a subset of Euclidean space (ℝ², ℝ³, etc.) defined by specific geometric relations (e.g., distance, alignment, angle) among its points, typically constructed from basic elements like points, lines, and curves.
> 

| **Dimension** | **Type** | **Subtype** | **Examples** |
| --- | --- | --- | --- |
| **0D** | Point | — | Point PP |
| **1D** | Linear Elements | Line, Line Segment, Ray | Line ABAB, Segment CDCD, Ray EFEF |
|  | Angle | By measure | Acute, Right, Obtuse, Straight, Reflex |
| **2D** | Curved Figures | Circle, Ellipse, Conics | Circle, Ellipse, Parabola, Hyperbola |
|  | Polygonal Figures | By sides | Triangle, Quadrilateral, Pentagon, ... |
|  |  | Triangle types | Equilateral, Isosceles, Scalene, Right, Obtuse, Acute |
|  |  | Quadrilateral types | Square, Rectangle, Rhombus, Parallelogram, Trapezoid |
|  |  | Regular / Irregular | Regular Hexagon, Irregular Octagon |
|  |  | Convex / Concave | Convex Pentagon, Star Polygon (Concave) |
| **3D** | Polyhedra | Regular (Platonic solids) | Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron |
|  |  | Other Polyhedra | Rectangular Prism, Triangular Prism, Pyramids |
|  | Solids of Revolution | — | Sphere, Cylinder, Cone, Torus |
| **Other** | Classification Tags | Symmetry | Rotational, Reflective, Translational symmetry |
|  |  | Construction | Compass-and-straightedge figures, Algebraic (e.g., conics), Transcendental |
|  |  | Convexity | Convex vs Concave |

## **Modeling with Geometry**

> Mapping real-world objects to abstract geometrical figures, and then using the properties and relationships of those figures to analyze, predict, or optimize aspects of the real objects.
> 

### Method

> This process summarizes mathematical modeling with geometry by abstracting real objects into figures, formalizing problems, solving them within the model, and interpreting the results back into real-world meaning.
> 

🔹 Steps in Geometric Modeling:

1. **Abstraction** Identify the essential shape or structure of a real object and represent it using geometric primitives (points, lines, curves, polygons, solids, etc.).
2. **Idealization** Ignore irregularities, imperfections, or unnecessary complexity to focus on key spatial properties—e.g., assuming a tire is a perfect circle.
3. **Formalization** Use geometric rules, theorems, or coordinate systems to describe relationships, positions, angles, distances, or volumes.
4. **Computation & Inference** Perform measurements, calculations, or simulations using geometry to draw conclusions—e.g., find the area, optimize layout, or simulate movement.
5. **Interpretation & Application** Translate the **abstract results** back to the real-world context to inform design, engineering, prediction, or explanation.

### Case Studies

> **Note:** These are unverified and potentially inaccurate examples generated with **ChatGPT**, but the overall direction and conceptual framing are correct.
> 

| **Civilization / Period** | **Domain** | **Abstraction (Real → Geometric)** | **Formalization (Problem → Model)** | **Inference (Model → Solution)** | **Interpretation (Back to Reality)** |
| --- | --- | --- | --- | --- | --- |
| **Egypt** | Land Reallocation | Irregular farmland → Rectangles & triangles | Area formulas from practical geometry (e.g., Herodotus' reports) | Area calculations post-Nile flood | Reassign land, levy taxes, resolve disputes |
| **Babylon** | Field Surveying | Field corners → Right triangles | Pythagorean triples (e.g., 3-4-5) used to verify right angles | Correct layout of land boundaries and plots | Ensured fair division, consistent property limits |
| **India (Vedic)** | Ritual Agriculture | Altars as symbolic maps of land & cosmos → Squares, rectangles, circles | Śulba Sūtras: constructions using cords and pegs | Convert squares to circles, scale altars | Harmonize farming rituals with cosmic geometry |
| **China** | Irrigation Layout | Canal systems → Grid and radial geometries | Early coordinate concepts, symmetry, and modular planning | Optimize flow and coverage of water supply | Increase agricultural yield and regional stability |
| **Greece** | Agricultural Terraces | Terraced hills → Trapezoids and planes | Used Euclidean geometry to stabilize slopes and manage runoff | Measured incline angles and area distribution | Enabled farming on mountainous terrain |
| **Rome** | Centuriation (Land Division) | Agricultural land → Square and rectangular grids | Applied orthogonal grid layout (centuriae of ~710m per side) | Systematic land partition and alignment via surveying instruments | Efficient tax, military, and inheritance systems |
| **Maya** | Calendar-based Agriculture | Seasons and planting cycles → Geometric alignments with celestial objects | Observed solar angles, constructed geometrically aligned temples | Predicted solstices/equinoxes using shadow and angle geometry | Scheduled planting and harvest with seasonal precision |
| **Andean (Inca)** | Terrace Agriculture | Hillsides → Stepped platforms modeled as stacked polygons | Practical slope, drainage, and soil volume calculations | Engineered water flow and retained soil | Sustained high-altitude agriculture across rugged terrain |
| **Mesopotamia** | Field Measurement | Fields as rectangles and trapezoids | Cuneiform tablets with area/length tables (e.g., Plimpton 322) | Solved for unknown lengths and areas | Used for taxation, crop estimation, and legal contracts |
| **Hebrews** | Agricultural Laws | Boundaries and fallow cycles → Conceptual geometric zones | Defined property limits using linear distances and shared landmarks | Enforced sabbatical year rules and tithes | Codified land use and equitable distribution in religious law |
| **⚜️ Medieval Europe** | Monastic Agriculture | Farmlands and cloisters → Gridded plots, rectangular gardens, radial layouts | Geometry of cloister design + land division in *Domesday Book* surveys | Estimated areas for crop rotation and water channels | Supported self-sustaining agriculture, coordinated estate management |

## Polygon

![](https://cdn1.byjus.com/wp-content/uploads/2019/09/types-of-regular-polygon.png)

### Definitions

> **Polygons**  — closed shapes formed by a finite number of straight line segments.
> 

> A **regular** polygon is a special type with sides that are all the same length and angles that are the same size.
> 

> **Irregular** polygon — a polygon with sides and/or angles that are **not all equal**.
> 

> A **polygon** with **n** sides is sometimes called an **n-gon**.
> 

> The angle along a **straight line** is 180°.
> 

> An **exterior angle** is formed when a side of a polygon (or any geometric figure) is extended outwards, creating an angle between that extended side and an adjacent side
> 

> An **interior angle** is the angle formed between two adjacent sides of a polygon or a geometric figure that lies within the figure itself.
> 

### Axiom

> Each **exterior angle** of a **regular** **n-gon** measures $\frac{360°} {n}$.
> 

> Each interior angle of a **regular** **n-gon** measures  $180° - \frac{360} {n}$.
> 

> **Parallel lines** are lines in the same plane that never intersect, no matter how far they are extended.
> 

> Axiom:  All Right Angles are equal**. What is a right angle?**
> 

> **Vertical angles** are pairs of angles that are opposite each other when two lines cross. They are always equal in measure.
> 

### Theorem

> [**Theorem**]  The sum of all exterior angles is 360°.
> 

> Note. When we say *“the sum of the exterior angles of a triangle is 360°,”* we mean the sum of **one exterior angle at each vertex**—specifically, the exterior angles that lie **outside the triangle and do not overlap**. Each vertex has two possible exterior angles (one on each side), but the sum of *both* exterior angles per vertex is not considered. Only one exterior angle per vertex is counted to get the total of 360°.
> 

> [To be Proven] The measure of a triangle's **exterior** angle is the sum of the two opposite **interior** angle measures.
> 

> [To be Proven]  The sum of the interior angles of a triangle is 180°.
> 

## Circumference

> … This is the **Pythagorean theorem**, and it expresses the relationship between the side lengths of any **right** triangle.
> 

> An **arc of a circumference** is a continuous part of the boundary of a circle, defined by two endpoints on the circle and the portion of the circle between those points.
> 
- How to get **Pi**?
- How to get the diameter?
- How to get the **arc** from the **angles**?
- How to deduce the area of the **circumference**?
- …

![](https://www.piday.org/wp-content/uploads/2020/02/Circle-Graphic-1024x576.png)

## Triangle

> 

> [TO BE PROVEN] This is the **Pythagorean theorem**, and it expresses the relationship between the side lengths of any **right** triangle. See more in  [Pythagorean Theorem](note.html?n=epistemica/mathematical/geometry/pythagorean-theorem.md).
> 

## Rhombus

> 

## Trapezoid

> 

## References

- [What is (a) geometry?](https://math.stackexchange.com/questions/192055/what-is-a-geometry)
- [What is Geometry?](https://scgp.stonybrook.edu/archives/29958)
- https://en.wikipedia.org/wiki/Geometry
- [Hyperplane](https://en.wikipedia.org/wiki/Hyperplanehttps://mathworld.wolfram.com/Hyperplane.html)
- [Conformal Map](https://en.wikipedia.org/wiki/Conformal_map)
- [Erlangen Program](https://en.wikipedia.org/wiki/Erlangen_program)
- [Hypersurface](https://en.wikipedia.org/wiki/Hypersurface)
- [Hyperplane separation theorem](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem)
- [Arrangement of hyperplanes](https://en.wikipedia.org/wiki/Arrangement_of_hyperplanes)
- [What is the significance of non-commutative geometry in mathematics?](https://mathoverflow.net/questions/88184/what-is-the-significance-of-non-commutative-geometry-in-mathematics)
- https://en.wikipedia.org/wiki/Analytic_geometry
- https://en.wikipedia.org/wiki/Polyhedron
- https://en.wikipedia.org/wiki/Prism_(geometry)
- https://news.ycombinator.com/item?id=41831617
- https://en.wikipedia.org/wiki/Convex_polygon
- https://en.wikipedia.org/wiki/Sphere
- https://en.wikipedia.org/wiki/Angle
- [Euclidean  Geometry](note.html?n=epistemica/mathematical/geometry/euclidean-geometry.md)
- [Contour Map](note.html?n=epistemica/mathematical/contour-map.md))
- [Conformal map](note.html?n=epistemica/mathematical/conformal-map.md))
- [Coordinate System](note.html?n=epistemica/mathematical/coordinate-system.md))
- [**Differential Geometry**](note.html?n=epistemica/mathematical/geometry/differential-geometry.md)
- [Computational Geometry](note.html?n=epistemica/science/computational-geometry.md)
- https://www.youtube.com/watch?v=6s1CI3uuhko
- [**Inner Product Space**](note.html?n=epistemica/mathematical/space/inner-product-space.md)
- https://en.wikipedia.org/wiki/Euclidean_space
