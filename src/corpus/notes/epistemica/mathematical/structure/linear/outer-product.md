---
tags: [note, mathematics, linear-algebra]
---

# Outer Product

> The **outer product** of two vectors is the product that does not contract them. Where the [inner product](/view.html?p=notes/epistemica/mathematical/structure/linear/inner-product.md) pairs $u$ and $v$ into a single number, the outer product keeps both whole and lays one against the other, returning a matrix: for $u \in \mathbb{R}^m$ and $v \in \mathbb{R}^n$, the $m \times n$ matrix $u v^{\mathsf T}$ whose entry in row $i$, column $j$ is $u_i v_j$.

> The object is the rank-one case of the [tensor product](/view.html?p=notes/epistemica/mathematical/tensor/tensor.md), and it earns a note of its own because of what it builds: almost every matrix that is assembled *from data* rather than specified by hand is a sum of outer products — the scatter matrix, the covariance matrix, the Gram matrix, the rank-one projector, the pure-state [density matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/density-matrix.md).

## Definition

For column vectors $u \in \mathbb{R}^m$ and $v \in \mathbb{R}^n$ the outer product is

$$u v^{\mathsf T} = \begin{pmatrix} u_1 v_1 & u_1 v_2 & \cdots & u_1 v_n \\ u_2 v_1 & u_2 v_2 & \cdots & u_2 v_n \\ \vdots & \vdots & \ddots & \vdots \\ u_m v_1 & u_m v_2 & \cdots & u_m v_n \end{pmatrix}, \qquad (u v^{\mathsf T})_{ij} = u_i v_j.$$

The dimensions need not agree: $u$ and $v$ may live in spaces of different dimension, and the result is the linear map $v \mapsto \langle v, x\rangle u$ written in coordinates — an operator, not a number. In the index-free notation of [tensor](/view.html?p=notes/epistemica/mathematical/tensor/tensor.md) calculus it is the **dyad** $u \otimes v$, and in the bra–ket notation of quantum mechanics the same object is written $|u\rangle\langle v|$.

## The two products

Three different operations are called "product" of two vectors, and the corpus separates them deliberately.

| Product | Notation | Takes | Returns | What it does |
| --- | --- | --- | --- | --- |
| **Inner** — dot, scalar | $\langle u, v\rangle = v^{\mathsf T} u$ | vectors of the **same** dimension | scalar | contracts the pair into one number: a length, an angle, a projection |
| **Outer** — dyadic, tensor | $u v^{\mathsf T}$ | vectors of **any** dimensions | $m \times n$ matrix of rank one | expands the pair into an operator: keeps both directions |
| **Kronecker** | $A \otimes B$ | two matrices | block matrix | the tensor product at matrix level; on two column vectors it lists the outer product's entries as one column, $u \otimes v = \operatorname{vec}(v u^{\mathsf T})$ |

The order of the operands is the first thing the outer product loses: $u v^{\mathsf T}$ and $v u^{\mathsf T}$ are transposes of one another, equal only when the two are parallel. The inner product, by contrast, is symmetric in the real case — which is the algebraic mark of the one that contracts.

## Properties

| Property | Statement |
| --- | --- |
| **Rank** | $\operatorname{rank}(u v^{\mathsf T}) = 1$ for nonzero $u, v$: every column is a multiple of $u$, every row a multiple of $v^{\mathsf T}$ |
| **Trace** | $\operatorname{tr}(u v^{\mathsf T}) = v^{\mathsf T} u = \langle u, v\rangle$ — the inner product is the outer product's trace, which is why the two are not unrelated products but the two readings of one contraction |
| **Transpose** | $(u v^{\mathsf T})^{\mathsf T} = v u^{\mathsf T}$ |
| **Action on a vector** | $(u v^{\mathsf T})x = u\,(v^{\mathsf T} x) = \langle v, x\rangle\, u$: read $x$ against $v$, then scale $u$ |
| **Bilinearity** | linear in each argument separately — $(\alpha u + u')v^{\mathsf T} = \alpha u v^{\mathsf T} + u'v^{\mathsf T}$ — and not commutative |
| **Projector** | $\dfrac{u u^{\mathsf T}}{u^{\mathsf T} u}$ is the [orthogonal projector](/view.html?p=notes/epistemica/mathematical/structure/linear/projection-matrix.md) onto $\operatorname{span}\{u\}$: symmetric, idempotent, rank one |
| **Decomposition** | every matrix is a sum of outer products, $A = \sum_i \sigma_i u_i v_i^{\mathsf T}$ — the [singular value decomposition](/view.html?p=notes/epistemica/mathematical/structure/linear/singular-value-decomposition-svd.md) — and the number of nonzero terms is its rank |
| **Rank-one content** | a matrix is an outer product exactly when its rank is one; the rank-$r$ case is a sum of $r$ of them, which is what makes the decomposition above possible at all |

## Where the corpus already uses it

| Construction | Form | Reading |
| --- | --- | --- |
| [Scatter matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/scatter-matrix.md) | $S = \sum_i (x_i - \mu)(x_i - \mu)^{\mathsf T}$ | one observation contributes one outer product; their sum is the dispersion |
| [Covariance matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/covariance-matrix.md) | the same sum scaled by $1/(n-1)$ | the centered outer product as the unit of covariance |
| [Gram matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/gram-matrix.md) | $G = XX^{\mathsf T}$, so $G_{ij} = \langle x_i, x_j\rangle$ | the same data read as inner products, built from outer products |
| [Projection matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/projection-matrix.md) | $P = u u^{\mathsf T}/(u^{\mathsf T}u)$ | a single dyad, normalised so that $P^2 = P$ |
| [Density matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/density-matrix.md) | $\rho = \lvert\psi\rangle\langle\psi\rvert$ | the pure state as a dyad: the bra–ket outer product |
| [Singular value decomposition](/view.html?p=notes/epistemica/mathematical/structure/linear/singular-value-decomposition-svd.md) | $A = \sum_i \sigma_i u_i v_i^{\mathsf T}$ | any matrix resolved into the outer products it is made of |

## References

- https://en.wikipedia.org/wiki/Outer_product
- [Inner product](/view.html?p=notes/epistemica/mathematical/structure/linear/inner-product.md) — the product that contracts: the other reading of the same pair of vectors
- [Matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/matrix.md) — the object an outer product produces, and the Kronecker product table beside it
- [Tensor](/view.html?p=notes/epistemica/mathematical/tensor/tensor.md) — the rank-one case of the tensor product, in index-free form
- [Gram matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/gram-matrix.md) · [Scatter matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/scatter-matrix.md) · [Covariance matrix](/view.html?p=notes/epistemica/mathematical/structure/linear/covariance-matrix.md) — the constructions that are sums of outer products
