---
tags: [geometry]
---

# Hyperplane

 : Plane (Plane%20247c0f5171ec80ccab77d110057bebbd.md)

> A **hyperplane** is a flat surface that has one fewer dimension than the space it is in. For example, in three-dimensional space, a hyperplane is a two-dimensional plane; in two-dimensional space, it's a one-dimensional line. More generally, in an n-dimensional space, a hyperplane is an object of dimension $n - 1$. It divides the space into two halves and is defined by a single linear equation. Although we often picture them as lines or planes, hyperplanes exist in any number of dimensions and play a fundamental role in geometry, algebra, and many applied fields like optimization and machine learning.
> 

## ⚙️ Formulation

> In geometry and linear algebra, a **hyperplane** is a generalization of the concept of a **plane** to **higher-dimensional spaces**.
> 

> A hyperplane in an n-dimensional space (e.g., $\mathbb{R}^n$) is a flat, affine subspace of dimension $n - 1$.
> 

That is:

- In $\mathbb{R}^2$, a hyperplane is a **line** (1D).
- In $\mathbb{R}^3$, a hyperplane is a **plane** (2D).
- In $\mathbb{R}^n$, a hyperplane is an (n - 1) dimensional object.

### 🧮 **Algebraic Form**

> Note: If you note a line lives in two dimensions; so why is her call 1D,  a line is called **1-dimensional (1D)** not because of the space it's drawn in, but because of its **intrinsic degrees of freedom**.
> 

A hyperplane in $\mathbb{R}^n$ is defined by a **linear equation**: $a_1x_1 + a_2x_2 + \dots + a_nx_n = b$

where:

- $(a_1, a_2, \dots, a_n) \neq (0, \dots, 0)$ is the **normal vector** to the hyperplane,
- $b \in \mathbb{R}$ is a scalar offset.

### 🧭 **Geometric Intuition**

A hyperplane:

- **Divides space** into two half-spaces.
- It has one fewer **dimension**—understood here as the number of **degrees of freedom**, not as spatial coordinates for location—than the space it resides in.
- Is **flat** (no curvature) and **infinite** in extent within its dimension.

## 📊 **Applications**

- In **machine learning**, hyperplanes define **decision boundaries** in classifiers like support vector machines (SVMs).
- In **optimization**, hyperplanes define **constraints** in linear programming.
- In **projective geometry**, hyperplanes are critical in defining **duality** and **intersections**.

## Relations

| **Concept** | **Relation to Hyperplanes** |
| --- | --- |
| **Linear Algebra** | Hyperplanes are solution sets to linear equations in $\mathbb{R}^n$. They are affine subspaces of dimension $n-1$. |
| **Vector Spaces** | A hyperplane can be defined as the **kernel (nullspace)** of a non-zero linear functional $f: \mathbb{R}^n \to \mathbb{R}$. |
| **Dual Spaces** | Every hyperplane corresponds to a linear functional. The hyperplane is the **zero set** of a covector. |
| **Convex Geometry** | Hyperplanes are used to define **half-spaces**, **convex hulls**, and support **separating theorems** (e.g., separating two convex sets). |
| **Optimization (Linear Programming)** | Hyperplanes define the **constraints** in LP problems; feasible regions are intersections of half-spaces. |
| **Machine Learning** | In SVMs and perceptrons, hyperplanes act as **decision boundaries** that separate classes. |
| **Differential Geometry** | Tangent hyperplanes approximate curved manifolds locally (e.g., tangent planes to surfaces). |
| **Topology & Manifolds** | Hyperplanes can be seen as **codimension-1 submanifolds** (codimension = difference between ambient and subspace dimension). |
| **Projective Geometry** | Hyperplanes define **projective duals**: points ↔ hyperplanes; they are also the “infinity boundaries” of affine space. |
| **Measure Theory** | Hyperplanes have **zero measure** in $\mathbb{R}^n$, just like lines in $\mathbb{R}^2$, or planes in $\mathbb{R}^3$. |
| **Algebraic Geometry** | Hyperplanes are the simplest **algebraic varieties** of degree 1: the zero sets of linear polynomials. |
| **Combinatorics (Hyperplane Arrangements)** | The study of how hyperplanes intersect, partition space, and form combinatorial structures (e.g., regions, faces). |
| **Information Theory** | Decision boundaries in classification, based on entropy or mutual information, often correspond to hyperplanes. |

## References

- https://en.wikipedia.org/wiki/Hyperplane
- https://mathworld.wolfram.com/Hyperplane.html
- https://mathworld.wolfram.com/LinearTransformationKernel.html
- https://en.wikipedia.org/wiki/Arrangement_of_hyperplanes
- https://math.stackexchange.com/questions/3175938/how-is-this-a-coherent-definition-of-hyperplane
