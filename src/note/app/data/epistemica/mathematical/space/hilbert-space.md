---
tags: [analytical, linear-algebra, space]
---

# Hilbert Space

> A **Hilbert space** is a complete inner product space: a real or complex vector space equipped with an inner product whose induced norm makes every Cauchy sequence converge inside the space.

## Formulation

Let $H$ be a vector space over $\mathbb{R}$ or $\mathbb{C}$ with inner product $\langle \cdot, \cdot \rangle$, and let

$$
\lVert x \rVert := \sqrt{\langle x, x \rangle}
$$

be the norm it induces. Then $H$ is a **Hilbert space** when the metric $d(x,y) = \lVert x - y \rVert$ is complete: every Cauchy sequence in $H$ converges to an element of $H$.

Equivalently, a Hilbert space is a Banach space whose norm satisfies the **parallelogram law**

$$
\lVert x + y \rVert^2 + \lVert x - y \rVert^2 = 2\lVert x \rVert^2 + 2\lVert y \rVert^2.
$$

Completeness is what separates a Hilbert space from a mere inner product space; the inner product is what separates it from a general Banach space.

## Properties

- **Projection theorem.** Every nonempty closed convex subset of a Hilbert space has a unique element of minimal norm; for a closed subspace $M$, every $x \in H$ splits uniquely as $x = m + m^\perp$ with $m \in M$ and $m^\perp \in M^\perp$, so $H = M \oplus M^\perp$.
- **Riesz representation.** Every continuous linear functional $\varphi$ on $H$ is of the form $\varphi(x) = \langle x, y \rangle$ for a unique $y \in H$.
- **Orthonormal bases.** Every Hilbert space admits a maximal orthonormal set. A separable Hilbert space has a countable orthonormal basis and is isometrically isomorphic to $\ell^2$.
- **Adjoints.** Every bounded linear operator $T : H \to H$ has a unique adjoint $T^*$ satisfying $\langle Tx, y \rangle = \langle x, T^*y \rangle$.
- **Spectral theory.** Self-adjoint and normal operators on a Hilbert space admit spectral decompositions, generalizing the diagonalization of Hermitian matrices.

## Examples

| **Hilbert Space** | **Definition** | **Common Applications** |
| --- | --- | --- |
| **Finite-dimensional spaces** | $\mathbb{R}^n$ or $\mathbb{C}^n$ with the standard inner product $\langle x, y \rangle = \sum_{i=1}^n x_i \overline{y_i}$. | Linear algebra, geometry, numerical methods |
| **$L^2$-space** | Square-integrable functions: $L^2(X,\mu) = \{f : X \to \mathbb{C} \mid \int_X \lvert f \rvert^2 \, d\mu < \infty\}$, with $\langle f, g \rangle = \int_X f \overline{g} \, d\mu$. | Fourier analysis, quantum mechanics, probability |
| **Hilbert sequence space $\ell^2$** | Square-summable sequences: $\ell^2 = \{(x_n) \mid \sum_{n=1}^\infty \lvert x_n \rvert^2 < \infty\}$. | Signal processing, series expansions, numerical analysis |
| **Sobolev spaces $H^k$** | $H^k(\Omega) = W^{k,2}(\Omega)$: functions whose weak derivatives up to order $k$ lie in $L^2(\Omega)$. | Partial differential equations, variational methods, image processing |
| **Hardy space $H^2$** | Holomorphic functions on the unit disk with square-summable Taylor coefficients, equivalently with bounded $L^2$ norms on circles $\lvert z \rvert = r < 1$. | Complex analysis, control theory, signal processing |
| **Bergman space $A^2$** | Holomorphic functions on the unit disk with $\int_{\mathbb{D}} \lvert f \rvert^2 \, dA < \infty$. | Complex geometry, operator theory |
| **Dirichlet space** | Holomorphic functions on the unit disk with finite Dirichlet integral $\int_{\mathbb{D}} \lvert f' \rvert^2 \, dA < \infty$. | Potential theory, harmonic analysis |
| **Reproducing kernel Hilbert space (RKHS)** | A Hilbert space of functions on which every evaluation functional $f \mapsto f(x)$ is continuous. | Machine learning (SVMs, Gaussian processes), harmonic analysis |
| **Fock space** | Symmetric or antisymmetric Fock space built from a one-particle Hilbert space; its Segal–Bargmann representation consists of entire functions with Gaussian weight. | Quantum field theory, quantum optics, many-body physics |
| **Hilbert–Schmidt operators** | Compact operators $T$ with $\sum_n \lVert T e_n \rVert^2 < \infty$ for an orthonormal basis $(e_n)$, forming a Hilbert space under $\langle S, T \rangle_{HS} = \sum_n \langle S e_n, T e_n \rangle$. | Integral equations, quantum mechanics, operator theory |
| **Weighted $L^2$-spaces** | $L^2(X, w \, d\mu)$ with a positive weight $w$, inner product $\langle f, g \rangle = \int_X f \overline{g} \, w \, d\mu$. | Sturm–Liouville theory, orthogonal polynomials, statistics |

## References

- [Space](note.html?n=epistemica/mathematical/space/space.md)
- [Inner Product](note.html?n=epistemica/mathematical/inner-product.md)
- [Inner Product Space](note.html?n=epistemica/mathematical/space/inner-product-space.md)
- [Metric Space](note.html?n=epistemica/mathematical/space/metric-space.md)
- [Cauchy Sequence](note.html?n=epistemica/mathematical/cauchy-sequence.md)
- [Normed Vector Space](note.html?n=epistemica/mathematical/space/normed-vector-space.md)
- [Banach Space](note.html?n=epistemica/mathematical/space/banach-space.md)
- [Function Space](note.html?n=epistemica/mathematical/space/function-space.md)
- [Sobolev Space](note.html?n=epistemica/mathematical/space/sobolev-space.md)
- [Hardy Space](note.html?n=epistemica/mathematical/space/hardy-space.md)
- [Reproducing Kernel Hilbert Space](note.html?n=epistemica/mathematical/space/reproducing-kernel-hilbert-space.md)
- [Operator](note.html?n=epistemica/mathematical/operator.md)
- [Linear Operator](note.html?n=epistemica/mathematical/linear-operator.md)
- [Adjoint Operator](note.html?n=epistemica/mathematical/adjoint-operator.md)
- [Self-adjoint Operator](note.html?n=epistemica/mathematical/self-adjoint-operator.md)
- [Compact Operator](note.html?n=epistemica/mathematical/compact-operator.md)
- [Spectrum](note.html?n=epistemica/mathematical/spectrum.md)
- [Linear Functional](note.html?n=epistemica/mathematical/linear-functional.md)
- [Quantum Framework](note.html?n=epistemica/science/quantum-framework.md)
- [Quantum Field Theory (QFT)](note.html?n=epistemica/construction/quantum-field-theory-qft.md)

- [Hilbert space - Wikipedia](https://en.wikipedia.org/wiki/Hilbert_space)
- [Hilbert Space - Mathworld](https://mathworld.wolfram.com/HilbertSpace.html)
- [Hilbert Space - ncatlab](https://ncatlab.org/nlab/show/Hilbert+space)
- Rudin, W. (1991). *Functional Analysis* (2nd ed.). McGraw-Hill.
- Conway, J. B. (1990). *A Course in Functional Analysis* (2nd ed.). Springer.
- Folland, G. B. (1999). *Real Analysis: Modern Techniques and Their Applications* (2nd ed.). Wiley.
