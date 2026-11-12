---
tags: [note, mathematics, geometry, rotation]
qa:
 - What kind of epistemic element is a mathematical rotation?
---

# Rotation

> A **rotation** is the isometry that fixes one point — the centre — and turns every ray through it by the same angle $\theta$, carrying every point of the plane around the centre along an arc of the same radius. It moves a figure without changing its shape, its size or its orientation: the two figures differ only by where they sit.

## Definition

In the Euclidean plane, the rotation about the origin by angle $\theta$ is the map

$$R_\theta:\ \mathbb{R}^2 \to \mathbb{R}^2, \qquad R_\theta(x) = \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \ \cos\theta\end{pmatrix} x,$$

and a rotation about the point $c$ is the conjugate $x \mapsto c + R_\theta(x - c)$. The matrix is **orthogonal** ($R_\theta^{\mathsf{T}}R_\theta = I$) with **determinant $+1$** — the condition that separates a rotation from a reflection, which is orthogonal with determinant $-1$.

Every point moves on a circle centred at $c$; the centre itself is the only fixed point. A rotation is therefore specified by three data: the **centre**, the **angle** $\theta$, and the **sense** (counter-clockwise positive, by convention).

## Classification

- **By angle** — the identity ($\theta = 0$), the quarter turn ($\pi/2$), the half turn ($\pi$, also called central inversion in the plane), and every intermediate angle; all except the identity have no fixed point other than the centre.
- **By dimension** — in the plane a centre and an angle; in space an **axis** and an angle (every spatial rotation fixes a line, not only a point — Euler's theorem).
- **By composition rule** — the set of all planar rotations with composition is the group $SO(2)$; rotations by multiples of $2\pi/n$ form the cyclic subgroup $C_n$, which is the rotational symmetry group of the regular $n$-gon ([Symmetry](/view.html?p=notes/epistemica/mathematical/symmetry.md)).

## Property

| Property | Statement |
| --- | --- |
| Isometry | preserves every distance — no length changes |
| Angle-preserving | preserves both the magnitude and the *sign* of the [angle](/view.html?p=notes/epistemica/mathematical/geometry/angle.md) between vectors |
| Orientation-preserving | unlike reflection, a rotation does not mirror; a right hand stays a right hand |
| Area and volume | preserved; this is why a rotation gives a congruence rather than a similarity |
| Composition | angles add: $R_\alpha \circ R_\beta = R_{\alpha+\beta} = R_\beta \circ R_\alpha$ — rotations about the same centre commute |
| Reflections | every rotation is the composition of **two reflections** in lines through its centre, and the angle is twice the angle between them |
| Inverse | $R_\theta^{-1} = R_{-\theta}$; a rotation is never idempotent unless it is the identity |

## Kind of Epistemic Element

The note's QA asks what kind of element a mathematical rotation *is*. It is an **`Epistemic Construction`** — a mathematical construct inside the representational system **Geometry**: a distinguished element of the transformation group against which the properties of a shape are read. Concretely, it is typed as a `Construct` inside the geometry's construction corpus, not as a `Property` (it is an operation, not a predicated feature) and not as an `Epistemic Method` (it is a construction, not a procedure for doing inquiry). The distinction matters because a rotation *acts on* figures, and anything that acts belongs with the constructions, while anything carried by a figure belongs with its properties — the rotation preserves the shape's properties and is not one of them.

## Space of Rotations

The rotations of the plane, with composition, form the group $SO(2)$, which is topologically a **circle** — a rotation is completely fixed by its angle, and the angle is one real number modulo $2\pi$.

In three dimensions the rotations form $SO(3)$, which is the real projective space $\mathbb{RP}^3$: every rotation is an axis–angle pair, and the axis-and-angle representation identifies $\theta$ with $2\pi - \theta$ about the reversed axis, so the space is the ball of radius $\pi$ with antipodal boundary points glued. Its double cover is the unit quaternions, which is why rotation is computed with quaternions when a composition of many rotations must stay free of singularities. The algebraic treatment of these groups is in [Orthogonal Group](/view.html?p=notes/epistemica/mathematical/structure/algebra/orthogonal-group.md).

## References

- [Rotation](https://en.wikipedia.org/wiki/Rotation)
- [Rotation - Mathematics](https://en.wikipedia.org/wiki/Rotation_(mathematics))
- [Rotation Matrix](https://en.wikipedia.org/wiki/Rotation_matrix) — the matrix representation used above
- [Euclidean Geometry](/view.html?p=notes/epistemica/mathematical/geometry/euclidean-geometry.md) — the system the rotation acts in
- [Angle](/view.html?p=notes/epistemica/mathematical/geometry/angle.md) — the quantity a rotation has magnitude in
- [Symmetry](/view.html?p=notes/epistemica/mathematical/symmetry.md) — rotations as the symmetries that fix a figure's centre
- [Geometric Shape](/view.html?p=notes/epistemica/mathematical/geometry/geometric-shape.md) — shape as what survives the rotation group
- [Triangle](/view.html?p=notes/epistemica/mathematical/geometry/triangle.md) — the figure whose symmetries are counted in rotations
- [Orthogonal Group](/view.html?p=notes/epistemica/mathematical/structure/algebra/orthogonal-group.md) — the algebraic home of $SO(2)$ and $SO(3)$
