# Adjoint Operator

 : Hermitian Matrix (Hermitian%20Matrix%20207c0f5171ec80cab327ff0d0be438c9.md), Self-adjoint Operator (Self-adjoint%20Operator%20172c0f5171ec80228e56caf24b8e3a56.md), Linear Operator (Linear%20Operator%20171c0f5171ec80e88b2fd6f9c6fae223.md), Hilbert Space (Hilbert%20Space%20bae2e35aecc54cec8ea6e2de5ae11e3b.md)

> Note:  The Adjoint of an operator is another operator.
> 

## Formulation

Given a linear operator $T$ acting on a **Hilbert space** $H$, the **adjoint** of $T$, denoted $T∗T^*$, is defined via the **inner product**:  $\langle Tx, y \rangle = \langle x, T^*y \rangle \quad \text{for all } x \in \mathcal{D}(T),\ y \in \mathcal{D}(T^*)$

- The inner product $\langle \cdot, \cdot \rangle$ is key: it determines how the operator "moves" relative to the geometry of the space.
- $T∗T^*$ is the **unique operator** (if it exists) such that this identity holds.

## 🔍 Finite-Dimensional Case (Matrices)

Let $A \in \mathbb{C}^{n \times n}$. Then the **adjoint** of $A$ is: $A^\dagger = \overline{A}^T$

It satisfies: $\langle Ax, y \rangle = \langle x, A^* y \rangle \quad \text{for all } x, y \in \mathbb{C}^n$

## 🔹 Geometric Intuition

The adjoint tells you **how the operator interacts with the inner product** — it reflects the idea of **reversing the direction** of action under an inner-product-preserving transformation.

- Think of it like a **“transpose with respect to the geometry”** of the space.

## 🔹 In Infinite Dimensions

If $T$ is a densely defined operator on a Hilbert space $H$, then:

- $T∗T^*$ may be **unbounded**, and
- It may be **defined only on a subdomain** $\mathcal{D}(T^*) \subseteq H$

## References

- https://math.stackexchange.com/questions/3578769/definition-of-adjoint-operator-asking-for-intuition
- https://mathworld.wolfram.com/Adjoint.html
- https://mathoverflow.net/questions/6552/what-is-an-intuitive-view-of-adjoints-version-2-functional-analysis
