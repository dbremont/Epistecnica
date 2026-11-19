---
tags: [note, mathematics, linear-algebra]
---

# Linear Map

> A **linear map** is a map between vector spaces that preserves the two operations that constitute them — addition and scalar multiplication. $T : V \to W$ over a field $K$ is linear when $T(u + v) = T(u) + T(v)$ and $T(\alpha v) = \alpha\,T(v)$ for all $u, v \in V$ and $\alpha \in K$; the two conditions collapse into one: $T(\alpha u + \beta v) = \alpha T(u) + \beta T(v)$.

> **Is this the heart of linear algebra?** Yes — if the heart is the object the theory is about. Linear algebra is the study of vector spaces and the structure-preserving maps between them; a matrix is what such a map becomes once a basis is chosen. The matrix is the map's *coordinate shadow*, not the map. The same map has as many matrices as there are pairs of bases, related by $M' = S^{-1} M S$, and any statement about $M$ that is not invariant under that replacement is a statement about the coordinates rather than about the map. Conversely, the theorems that carry the subject — rank–nullity, the spectral theorem, the singular-value decomposition — are statements about maps that become *computable* in a basis. The basis is an instrument; the map is the object. The qualification is practice: when linear algebra means numerical computation, the matrix is the working object and the map is the warrant for the algorithms.

## Definition

A linear map is a **homomorphism of vector spaces**: it preserves zero ($T(0) = 0$), negation, and every finite linear combination, so that

$$T\left(\sum_i \alpha_i v_i\right) = \sum_i \alpha_i\, T(v_i).$$

Two maps are equal when they agree on every vector of the domain. Because a linear map is determined by its values on a basis, a finite-dimensional map is fixed by finitely many data — which is exactly why it can be written as a matrix.

## Structure preserved, structure lost

Linearity preserves the linear structure and nothing else: it need not preserve length, angle, orthogonality, or the distinction between distinct directions. Two subspaces measure what the map does to that structure:

- the **kernel** (null space) $\ker T = \{v : T(v) = 0\}$ — the directions the map collapses;
- the **image** (range) $\operatorname{im} T = \{T(v) : v \in V\}$ — the directions the map reaches.

From them: $T$ is injective iff $\ker T = \{0\}$; $T$ is surjective iff $\operatorname{im} T = W$; $T$ is an isomorphism iff both. When $V$ is finite-dimensional, **rank–nullity** holds:

$$\dim V = \dim \ker T + \dim \operatorname{im} T.$$

The kernel is a subspace of the domain and the image a subspace of the codomain; neither is an arbitrary subset, and that is the content of the theorem.

## Matrix representation

Fix a basis $\mathcal{B} = (v_1, \dots, v_n)$ of $V$ and $\mathcal{C} = (w_1, \dots, w_m)$ of $W$. The matrix of $T$ is the array $M$ whose $j$-th column holds the coordinates of $T(v_j)$ in $\mathcal{C}$:

$$T(v_j) = \sum_{i=1}^{m} M_{ij}\, w_i.$$

Then the action of the map on coordinates is ordinary matrix–vector multiplication: if $x$ is the coordinate vector of $v$ in $\mathcal{B}$, the coordinate vector of $T(v)$ in $\mathcal{C}$ is $Mx$. Composition becomes matrix multiplication, and the identity map becomes the identity matrix — the correspondence is a functor from finite-dimensional vector spaces to matrices.

The representation is not canonical. Replacing $\mathcal{B}$ by $\mathcal{B}' = \mathcal{B}S$ and $\mathcal{C}$ by $\mathcal{C}' = \mathcal{C}R$ gives

$$M' = R^{-1} M S.$$

For an endomorphism with the same basis on both sides, $R = S$ and $M' = S^{-1} M S$: the matrices of one map in different bases are **similar**, and the invariants of the map — determinant, trace, characteristic polynomial, eigenvalues with multiplicity — are exactly the quantities preserved by similarity. This is the precise sense in which "the matrix is not the map".

## Composition, identity, and the category reading

Linear maps compose: if $T : U \to V$ and $S : V \to W$ are linear, so is $S \circ T : U \to W$, and composition is associative. Every space has an identity map $\mathrm{id}_V$, which is linear and neutral for composition. Vector spaces over a fixed field, with linear maps as arrows, therefore form a **category** — $\mathbf{Vect}_K$ — and linear algebra is the study of that category's finite-dimensional part. Isomorphisms are the bijective linear maps; a finite-dimensional space is isomorphic to $K^n$, but not canonically so, and the non-canonicity is the content of the change-of-basis formula.

## Kinds of linear map

| Kind | Domain and codomain | What it is |
| --- | --- | --- |
| **Linear operator** (endomorphism) | $T : V \to V$ | A linear map of a space to itself; the setting of eigenvalues and the spectral theorem. The corpus keeps this as [Linear Operator](/view.html?p=notes/epistemica/mathematical/structure/linear/linear-operator.md). |
| **Linear functional** | $T : V \to K$ | A linear map to the field — a scalar-valued measurement on the space; the dual space is the space of these. See [Linear Functional](/view.html?p=notes/epistemica/mathematical/mapping/linear-functional.md). |
| **Automorphism** | $T : V \to V$ bijective | An invertible endomorphism: a change of basis is exactly an automorphism of the space. |
| **Multilinear map** | $T : V_1 \times \cdots \times V_n \to W$ | Linear in each argument separately, not jointly — the tensor product is what linearises it. See [Multilinear Map](/view.html?p=notes/epistemica/mathematical/structure/linear/multilinear-map.md). |

The map is also the general notion of which [Map](/view.html?p=notes/epistemica/mathematical/mapping/map.md) is the root, and of which the [Linear Operator](/view.html?p=notes/epistemica/mathematical/structure/linear/linear-operator.md) is the endomorphic special case.

## References

- Axler, S. (2015). *Linear algebra done right* (3rd ed.). Springer. — linear maps first, matrices as their representation; the argument for the emphasis this note takes.
- Halmos, P. R. (1958). *Finite-dimensional vector spaces* (2nd ed.). Van Nostrand. — the canonical treatment of the map as the object and the matrix as its basis-dependent description.
- Strang, G. (2016). *Introduction to linear algebra* (5th ed.). Wellesley–Cambridge. — the computational counterweight: the four fundamental subspaces read directly off the matrix.
- [Linear map — Wikipedia](https://en.wikipedia.org/wiki/Linear_map)
- [Linear Algebra](/view.html?p=notes/epistemica/mathematical/structure/linear/linear-algebra.md) — the aggregate this note is the central object of
- [Linear Operator](/view.html?p=notes/epistemica/mathematical/structure/linear/linear-operator.md) · [Linear Functional](/view.html?p=notes/epistemica/mathematical/mapping/linear-functional.md) · [Multilinear Map](/view.html?p=notes/epistemica/mathematical/structure/linear/multilinear-map.md)
- [Map](/view.html?p=notes/epistemica/mathematical/mapping/map.md) — the root notion; [Matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/matrix.md) — the coordinate representation
