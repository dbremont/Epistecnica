---
tags: [space]
---

# Metric Space

 : Euclidean  Geometry (Euclidean%20Geometry%20858b34433a204b55bb716919101bdcc6.md), Positive-definite Kernel (Positive-definite%20Kernel%2018ec0f5171ec807a9014c83ecdf07ad9.md), Measure (Measure%20273c0f5171ec80ae812dc3c73aad95dc.md), Inner Product (Inner%20Product%20171c0f5171ec80439aa0fc448d33b98a.md)

> A **metric space** is a set of points equipped with a metric, which is a function that defines a distance between any two points in the set, satisfying the properties of non-negativity, identity of indiscernibles, symmetry, and the triangle inequality.
> 

## Properties

A **metric space** is a set XX along with a distance function (or metric) d:X×X→Rd: X \times X \to \mathbb{R} that satisfies specific properties. Below is a table summarizing the key properties of metric spaces.

| **Property** | **Description** | **Mathematical Expression** | **Example** |
| --- | --- | --- | --- |
| **Non-negativity** | The distance between any two points is always non-negative. | d(x,y)≥0d(x, y) \geq 0, for all x,y∈Xx, y \in X | In the Euclidean space Rn\mathbb{R}^n, d(x,y)=∥x−y∥≥0d(x, y) = \| x - y \| \geq 0. |
| **Identity of Indiscernibles** | The distance between two points is zero if and only if the points are the same. | d(x,y)=0d(x, y) = 0 if and only if x=yx = y. | In Rn\mathbb{R}^n, d(x,y)=0d(x, y) = 0 means x=yx = y. |
| **Symmetry** | The distance between two points is the same in either direction. | d(x,y)=d(y,x)d(x, y) = d(y, x) for all x,y∈Xx, y \in X. | In Rn\mathbb{R}^n, ∥x−y∥=∥y−x∥\| x - y \| = \| y - x \|. |
| **Triangle Inequality** | The distance between two points is less than or equal to the sum of the distances through a third point. | d(x,z)≤d(x,y)+d(y,z)d(x, z) \leq d(x, y) + d(y, z) for all x,y,z∈Xx, y, z \in X. | In Rn\mathbb{R}^n, ∥x−z∥≤∥x−y∥+∥y−z∥\| x - z \| \leq \| x - y \| + \| y - z \|. |
| **Boundedness** | A metric space is **bounded** if there exists a real number MM such that the distance between any two points is less than MM. | ∃M>0\exists M > 0 such that d(x,y)<Md(x, y) < M for all x,y∈Xx, y \in X. | The space Rn\mathbb{R}^n with the Euclidean metric is unbounded. |
| **Completeness** | A metric space is **complete** if every Cauchy sequence in the space converges to an element within the space. | A sequence (xn)(x_n) is Cauchy if ∀ϵ>0,∃N\forall \epsilon > 0, \exists N such that d(xn,xm)<ϵd(x_n, x_m) < \epsilon for all n,m≥Nn, m \geq N. | The space of real numbers R\mathbb{R} with the usual metric is complete. |
| **Compactness** | A metric space is **compact** if every sequence has a convergent subsequence. | A space is compact if it is both closed and bounded in finite-dimensional spaces. | The closed interval [0,1][0, 1] in R\mathbb{R} with the usual metric is compact. |
| **Openness/Closedness** | A set A⊂XA \subset X is **open** if for every point in AA, there is a neighborhood around it entirely contained in AA; it is **closed** if it contains all its limit points. | AA is open if for every x∈Ax \in A, ∃ϵ>0\exists \epsilon > 0 such that B(x,ϵ)⊆AB(x, \epsilon) \subseteq A. | The set (0,1)(0, 1) is open in R\mathbb{R} with the usual metric, while [0,1][0, 1] is closed. |
| **Convergence of Sequences** | A sequence (xn)(x_n) in XX **converges** to x∈Xx \in X if for every ϵ>0\epsilon > 0, there exists an NN such that d(xn,x)<ϵd(x_n, x) < \epsilon for all n≥Nn \geq N. | lim⁡n→∞xn=x\lim_{n \to \infty} x_n = x if d(xn,x)→0d(x_n, x) \to 0 as n→∞n \to \infty. | In R\mathbb{R}, the sequence xn=1nx_n = \frac{1}{n} converges to 0. |
| **Continuity of Functions** | A function f:X→Yf: X \to Y between two metric spaces is **continuous** if the preimage of every open set is open. | lim⁡x→x0f(x)=f(x0)\lim_{x \to x_0} f(x) = f(x_0). | The function f(x)=x2f(x) = x^2 is continuous on R\mathbb{R}. |
| **Isometry** | A map between metric spaces f:X→Yf: X \to Y is an **isometry** if it preserves the distance, i.e., dX(x,y)=dY(f(x),f(y))d_X(x, y) = d_Y(f(x), f(y)). | f(x,y)f(x, y) is an isometry if for all x,y∈Xx, y \in X, dX(x,y)=dY(f(x),f(y))d_X(x, y) = d_Y(f(x), f(y)). | The identity map on Rn\mathbb{R}^n is an isometry. |

---

### Additional Concepts:

1. **Separation Axioms**: A metric space is often called **Hausdorff** if for any two distinct points, there exist disjoint open neighborhoods around each point.
2. **Connectedness**: A metric space is **connected** if it cannot be divided into two disjoint, non-empty open sets. It is **path-connected** if there is a continuous path between any two points.
3. **Metric Subspace**: A subset of a metric space  is a **metric subspace** if the metric on the subset is the restriction of the metric on.

### References

- [Metric space](https://en.wikipedia.org/wiki/Metric_space)
- https://en.wikipedia.org/wiki/Complete_metric_space
