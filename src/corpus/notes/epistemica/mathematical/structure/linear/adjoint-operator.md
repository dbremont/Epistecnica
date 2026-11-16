---
tags: [note, mathematics, linear-algebra, operator]
---

# Adjoint Operator

> The **adjoint** of a linear operator $T$ is the operator $T^*$ that moves $T$ to the other side of the inner product: $\langle Tx, y \rangle = \langle x, T^* y \rangle$ for every $x$ in the domain of $T$ and $y$ in the domain of $T^*$.

> The definition is relative to the inner product, not to a basis — change the geometry and the adjoint changes with it. That is why it generalises the transpose (in a Euclidean space with an orthonormal basis the adjoint *is* the conjugate transpose), and why it is the object that lets symmetry, orthogonality and self-adjointness be stated without coordinates.

## Formulation

Given a linear operator $T$ on a Hilbert space $H$ with inner product $\langle \cdot, \cdot \rangle$,

$$ \langle Tx, y \rangle = \langle x, T^* y \rangle \qquad \text{for all } x \in \mathcal{D}(T), \; y \in \mathcal{D}(T^*). $$

The adjoint is unique where it exists: the identity fixes it completely, so an operator has at most one adjoint.

### Finite dimensions

For $A \in \mathbb{C}^{n \times n}$ the adjoint is the **conjugate transpose**,

$$ A^* = \overline{A}^{\mathsf{T}}, $$

written $A^\dagger$ in the physics literature and satisfying

$$ \langle Ax, y \rangle = \langle x, A^* y \rangle \qquad \text{for all } x, y \in \mathbb{C}^n. $$

Over $\mathbb{R}$ with an orthonormal basis it reduces to the transpose.

### Infinite dimensions

If $T$ is densely defined on $H$, then $T^*$ may be **unbounded**, and it is defined only on a subdomain $\mathcal{D}(T^*) \subseteq H$. The domain is part of the object rather than a technicality: two operators agreeing on a dense set can have different adjoints, and formal manipulation of the inner product is exactly where that difference is lost.

## Geometric reading

The adjoint is the transpose **with respect to the geometry of the space**. It reverses the direction in which the operator acts while leaving intact the inner product — the only structure that says what "the same direction" means. In a Euclidean space that produces the transpose; under a different inner product it produces something else, which is why the geometric reading and the matrix formula coincide only in an orthonormal frame.

## Why the abstraction exists

1. **It preserves the inner product.** The adjoint is what keeps the language of angles, projections and orthogonality available in spaces where coordinates are not.
2. **It makes quantum observables real.** Observables are represented by self-adjoint operators; self-adjointness is the condition that forces the spectrum — and therefore every measured value — to be real.
3. **It lets differential operators be analysed.** The formal adjoint is what carries boundary conditions into the theory, and what makes weak formulations of elliptic problems possible.
4. **It carries the spectral theorems.** The spectral theorem is a statement about self-adjoint and normal operators, and normality is defined through the adjoint: $T^*T = TT^*$.
5. **It organises functional analysis.** Duality, bounded and unbounded operator theory, and the weak topologies are all expressed through adjoints.

## Related

- [Self-adjoint Operator](self-adjoint-operator.md) — the case $T = T^*$, where the operator is its own adjoint and the spectrum is real.
- [Hermitian Matrix](hermitian-matrix.md) — the finite-dimensional instance of self-adjointness.
- [Spectral Theorem](spectral-theorem.md) — the result that the adjoint makes statable.
- [Linear Operator](linear-operator.md) — the object the adjoint is taken of.
- [Hilbert Space](../../space/hilbert-space.md) — the setting in which the inner product, and therefore the adjoint, exists.

## QA

- What is the reason for the existence of this abstraction?
- What is the **conjugate transpose**?

## References

- https://en.wikipedia.org/wiki/Hermitian_adjoint
- https://math.stackexchange.com/questions/3578769/definition-of-adjoint-operator-asking-for-intuition
- https://mathworld.wolfram.com/Adjoint.html
- https://mathoverflow.net/questions/6552/what-is-an-intuitive-view-of-adjoints-version-2-functional-analysis
