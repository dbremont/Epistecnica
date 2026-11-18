---
tags: [note, mathematics, topology, algebra, persistent-homology, tda]
qa:
 - Why is a persistence module a functor rather than a sequence of spaces?
 - What does the interval decomposition buy, and exactly where does it stop working?
 - Is the parameter of a persistence module a time, a scale, or a filtration index?
---

# Persistence Module

> A **persistence module** is the algebraic object that records how the homology of a space changes as a parameter moves: a functor from an ordered index set to vector spaces, with a linear map for every comparison of indices. It is the structure persistent homology computes, and the reason topological data analysis can be done with linear algebra rather than with topology.

> The definition is a diagram, not a space. For each value of the parameter there is a vector space; for each pair of ordered values there is a map between the corresponding spaces; and the maps must agree with composition. Everything the theory says follows from that one requirement — the parameters are comparable, and the maps commute.

## Definition

> Let $T$ be a totally ordered set — the **indexing set**, usually $\mathbb{R}$, $\mathbb{Z}$ or $\mathbb{N}$ — and $K$ a field. A **single-parameter persistence module** is a functor
> $$M : T \longrightarrow \mathbf{Vec}_K$$
> from the poset category of $T$ to the category of vector spaces over $K$ and linear maps. Concretely, it is a pair $(V,\pi)$ with a vector space $V_z$ for each $z \in T$ and a linear map $\pi_{y,z} : V_y \to V_z$ for each $y \le z$, such that
> $$\pi_{y,z} \circ \pi_{x,y} = \pi_{x,z} \qquad \text{for all } x \le y \le z.$$

> For a discrete index set the module is the diagram
> $$\cdots \to M_{-1} \to M_0 \to M_1 \to M_2 \to \cdots$$
> and the module is often named after its index set: a $T$-module, a $\mathbb{Z}$-module, an $\mathbb{R}$-module.

> **Multiparameter.** Let $P = T_1 \times \cdots \times T_n$ be a product of totally ordered sets, ordered coordinatewise. A **multiparameter persistence module** is a functor $M : P \to \mathbf{Vec}_K$. The single-parameter case is $n=1$; the $n \ge 2$ case is where the theory changes character.

## Examples

| Module | Definition | What it records |
| --- | --- | --- |
| **Homology module** $H_i(F)$ | For a filtration $F : P \to \mathbf{Top}$, set $H_i(F)_z = H_i(F_z)$, with maps induced by the inclusions | The features of dimension $i$ and the scale at which they appear and disappear |
| **Interval module** $\mathbb{I}_J$ | $K$ on an interval $J \subseteq P$, $0$ outside; identity maps inside | A single feature alive exactly on $J$ — the atom of the decomposition |
| **Free module** $Q_a$ | $K$ on the upset $\{z : z \ge a\}$, $0$ below; identity maps | A feature born at $a$ and never dying — a ray |

> The homology module is the one that matters in practice: given a point cloud and a filtration that thickens it, applying homology at each scale produces a persistence module whose interval decomposition is the **barcode** — the multiset of intervals in which each topological feature lives.

## Properties

> A module is **pointwise finite-dimensional** (p.f.d.) if every $V_z$ is finite-dimensional. Over $\mathbb{N}$ it is of **finite type** if, in addition, the maps $M_{N,n}$ become isomorphisms for all $n$ beyond some $N$ — the structure stabilises. Over $\mathbb{R}$ one asks for a finite number of distinct spaces and the stabilisation at both ends: **essentially discrete** and **essentially finite**.

> **The structure theorem.** Every p.f.d. persistence module indexed over a totally ordered set decomposes as a direct sum of interval modules:
> $$M \;\cong\; \bigoplus_{J \in \mathcal{J}(M)} \mathbb{I}_J .$$
> The multiset $\mathcal{J}(M)$ is unique, and it is the barcode. This is the result that makes persistent homology computable: the module is read off as a list of intervals, and comparing two data sets becomes comparing two barcodes.

> **Where it stops.** For a multiparameter module there is, in general, no decomposition into interval modules — the indecomposables are richer, and no finite invariant of the same kind exists. That is not a technicality: it is the reason multiparameter persistence is hard, and why the field measures similarity with the **interleaving distance** rather than by decomposing.

> **Complexity.** Single-parameter persistent homology is polynomial. Multidimensional persistent homology is exponential in the worst case, which is why the multiparameter theory is mostly about invariants — ranks, the interleaving distance, approximations — rather than about exact decompositions.

## History

> The structure was introduced by **Zomorodian and Carlsson (2005)** as an application of graded modules over a polynomial ring: the persistence of a filtration is the algebra of a module, and the barcode is its decomposition. **Carlsson and Zomorodian (2009)** extended it to several parameters. **Crawley-Boevey (2015)** proved the structure theorem for pointwise finite-dimensional modules over $\mathbb{R}$, and **Botnan and Crawley-Boevey (2019)** generalized it to arbitrary totally ordered index sets by importing the decomposition theory of representations of quivers.

## References

- Zomorodian, A., & Carlsson, G. (2005). Computing persistent homology. *Discrete & Computational Geometry*, 33(2), 249–274. https://doi.org/10.1007/s00454-004-1146-y — the module framing and the algorithm
- Carlsson, G., & Zomorodian, A. (2009). The theory of multidimensional persistence. *Discrete & Computational Geometry*, 42(1), 71–93. https://doi.org/10.1007/s00454-009-9176-0
- Crawley-Boevey, W. (2015). Decomposition of pointwise finite-dimensional persistence modules. *Journal of Algebra and Its Applications*, 14(5), 1550066. https://doi.org/10.1142/S0219498815500668
- Botnan, M. B., & Crawley-Boevey, W. (2020). Decomposition of persistence modules. *Proceedings of the American Mathematical Society*, 148(11), 4581–4596. https://doi.org/10.1090/proc/14790
- Chazal, F., de Silva, V., Glisse, M., & Oudot, S. (2016). *The structure and stability of persistence modules*. Springer. — the standard reference
- Oudot, S. Y. (2015). *Persistence theory: From quiver representations to data analysis*. AMS.
- [Persistent Homology](/view.html?p=notes/epistemica/observational/persistent-homology.md) — the method the module formalises
- [Representation Theory](/view.html?p=notes/epistemica/mathematical/structure/algebra/representation-theory.md) — the algebra the decomposition belongs to
- [Dimensionality Reduction](/view.html?p=notes/epistemica/observational/dimensionality-reduction.md) — the other reading of the shape of data
- [Persistence module](https://en.wikipedia.org/wiki/Persistence_module)
