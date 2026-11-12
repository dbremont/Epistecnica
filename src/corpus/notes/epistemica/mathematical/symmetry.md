---
tags: [note, mathematics, geometry, symmetry]
---

# Symmetry

> A figure or structure is **symmetric** when some transformation maps it onto itself: rotate a square by a quarter turn and it lands on itself; reflect an isosceles triangle in its altitude and you cannot tell it was moved; translate a frieze by one period and the pattern repeats. Symmetry is not the transformation but the **invariance** — the property of being unchanged by it — and the set of all such transformations, with composition, is the object's **symmetry group**.

## Definition

Let $S \subseteq \mathbb{R}^n$ be a figure and $G$ a group of transformations acting on $\mathbb{R}^n$ (isometries, similarities, affine or projective maps — the group is the choice, and it decides what counts). A **symmetry of $S$** is a $g \in G$ with

$$g(S) = S.$$

The **symmetry group** of $S$ in $G$ is the stabilizer

$$\operatorname{Sym}_G(S) = \{\, g \in G \mid g(S) = S \,\} \le G,$$

a subgroup of $G$ by construction: the identity fixes every figure, and if $g$ and $h$ both fix $S$ then so do $h^{-1}$ and $gh$. Symmetry is therefore a **property of the figure**, carried by a group — it is an invariant of the shape in the sense of [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md), and it changes when the group changes: a rectangle has four symmetries among isometries but a diagonal reflection among similarities-of-its-projective-completion.

## Line of Symmetry

A **line of symmetry** (or **axis of symmetry**) is a line $\ell$ such that reflection in $\ell$ maps the figure onto itself:

$$\sigma_\ell(S) = S.$$

Reflection in a line through $p_0$ with unit normal $n$ acts on a point $x$ as

$$\sigma_\ell(x) = x - 2\big((x - p_0)\cdot n\big)\,n,$$

the component of $x - p_0$ along $n$ reversed. A line of symmetry is exactly a **fixed line** of that reflection: every point of $\ell$ satisfies $\sigma_\ell(x) = x$.

**The folding test.** A physical reading that is also a proof: if the figure can be folded along $\ell$ so that the two halves coincide exactly, then $\ell$ is a line of symmetry. Every point of one half lands on a point of the other, which is what "reflection fixes the set" means.

**How many axes a figure has**

| Figure | Lines of symmetry | Why |
| --- | --- | --- |
| Scalene triangle | 0 | no side pair equal, so no reflection fixes it |
| Isosceles triangle | 1 | the axis through the apex and the base midpoint |
| Equilateral triangle | 3 | one through each vertex and the opposite midpoint |
| Rectangle (non-square) | 2 | the two lines through the midpoints of opposite sides |
| Rhombus (non-square) | 2 | the two diagonals |
| Square | 4 | the two midlines and the two diagonals |
| Regular $n$-gon | $n$ | one through each vertex (odd $n$) or each vertex pair (even $n$) |
| Circle | infinitely many | every line through the centre |
| Parallelogram (non-rhombus, non-rectangle) | 0 | it is centrally symmetric, not axially |

**Two structural facts.**

1. **Finitely many axes, one common point.** A bounded figure that is not a circle has finitely many lines of symmetry, and every one of them passes through a single point — the figure's centre — which is also fixed by every rotational symmetry. Two distinct reflection axes of a finite figure therefore meet at the centre, and their composition is a rotation.
2. **Axes and rotations are counted together.** A regular $n$-gon has $n$ reflection axes and $n$ rotations (including the identity, by $\tfrac{2\pi}{n}$ steps); its symmetry group is the dihedral group $D_n$ of order $2n$. The isosceles triangle has one axis and no rotation beyond the identity: it is $D_1$.

## Other Symmetries

Symmetry is not only reflection. The isometries of the plane give four kinds, and a figure may have any of the first three; the fourth preserves a pattern only when it is infinite.

| Type | Transformation | Fixed set | Example |
| --- | --- | --- | --- |
| Axial symmetry | reflection in a line $\ell$ | the line $\ell$ | isosceles triangle in its altitude |
| Rotational symmetry | rotation by $\theta = \tfrac{2\pi k}{n}$ about a point | the centre point | the triangle through $120^\circ$, the square through $90^\circ$ |
| Translational symmetry | translation by a period vector $t$ | none for a bounded figure; the infinite pattern maps to itself | a frieze or wallpaper pattern |
| Glide reflection | reflection followed by a translation along the axis | none | the herringbone of a brick wall |

A **rotational symmetry of order $n$** is one whose repeated application returns the figure to itself exactly $n$ times in a full turn, and for a finite figure the rotational symmetries are the rotations about its centre by multiples of $2\pi/n$: the cyclic group $C_n$.

## Symmetry Group of a Figure

For a bounded figure in the plane, the symmetry group is always finite and always fixes the centre point. The finite subgroups of the planar Euclidean group are exactly:

| Group | Elements | Figures |
| --- | --- | --- |
| Trivial | identity only | scalene triangle, parallelogram, any asymmetric figure |
| $C_n$ | $n$ rotations | a pinwheel, a swastika-like figure with no reflection axis |
| $D_n$ | $n$ rotations and $n$ reflections | regular $n$-gon, equilateral and isosceles triangles ($n = 3$, $n = 1$), square ($n = 4$) |

So the classification of a figure's symmetry is the classification of its group: *what subgroup of the isometries fixes it*. The algebraic treatment of these groups is in [Symmetry Group](/view.html?p=notes/epistemica/mathematical/structure/algebra/symmetry-group.md); the physical use of invariance — conservation laws, gauge symmetry — is the separate reading in [Symmetry (natural)](/view.html?p=notes/nature/symmetry.md), and the symmetric reduction of a problem by exploiting its symmetries is [Symmetry Reduction](/view.html?p=notes/epistemica/mathematical/method/reduction/symmetry-reduction.md).

## Taxonomy

| Figure | Symmetry group | Lines of symmetry | Rotational order |
| --- | --- | --- | --- |
| Scalene triangle | trivial | 0 | 1 |
| Isosceles triangle | $D_1$ | 1 | 1 |
| Equilateral triangle | $D_3$ | 3 | 3 |
| Isosceles right triangle | $D_1$ | 1 | 1 |
| General parallelogram | $C_2$ | 0 | 2 |
| Rectangle | $D_2$ | 2 | 2 |
| Rhombus | $D_2$ | 2 | 2 |
| Square | $D_4$ | 4 | 4 |
| Regular $n$-gon | $D_n$ | $n$ | $n$ |
| Circle | $O(2)$ | $\infty$ | $\infty$ |
| Tetrahedron (3-D) | $T_d$ | — | — |
| Cube / octahedron (3-D) | $O_h$ | — | — |
| Icosahedron / dodecahedron (3-D) | $I_h$ | — | — |

The 3-D rows are the Platonic solids, whose symmetry groups are the finite rotation-and-reflection groups of space; their axial and rotational symmetries are counted in planes and axes rather than lines.

## References

- https://en.wikipedia.org/wiki/Symmetry
- https://en.wikipedia.org/wiki/Reflection_symmetry
- https://en.wikipedia.org/wiki/Symmetry_group
- https://en.wikipedia.org/wiki/Point_groups_in_two_dimensions
- [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md) — shape as an orbit under a transformation group; symmetry as its stabilizer
- [Polygon](/view.html?p=notes/epistemica/mathematical/geometry/polygon.md) — the figures whose symmetries the table counts
- [Triangle](/view.html?p=notes/epistemica/mathematical/geometry/triangle.md) — the isosceles and equilateral axes
- [Rotation](/view.html?p=notes/epistemica/mathematical/geometry/rotation.md) — the other isometry that generates symmetry
- [Angle](/view.html?p=notes/epistemica/mathematical/geometry/angle.md) — the quantity a rotation preserves
- [Euclidean Geometry](/view.html?p=notes/epistemica/mathematical/geometry/euclidean-geometry.md) — the system the symmetries act in
