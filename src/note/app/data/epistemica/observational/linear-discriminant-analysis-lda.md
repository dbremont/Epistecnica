---
tags: [learning-system]
---

# Linear Discriminant Analysis (LDA)

 : Variance (Variance%201cfc0f5171ec80f5a7f1c535bbde6e1c.md), Covariance (Covariance%201cfc0f5171ec80aead47fc52bbd5c430.md)

> Linear Discriminant Analysis (LDA) is a statistical set of  methods used for both dimensionality reduction and classification. It models class-conditional distributions under the assumption of shared covariance and seeks a projection that maximizes class separability. Variants and extensions of LDA form a broader family of related techniques.
> 

> LDA is a **statistically grounded, simple, and interpretable approach** that uses strong priors about data distributions and linearity. Neural networks are **data-driven, flexible, and nonlinear models** that minimize explicit priors but trade off interpretability and require more data and compute.
> 

QA:

- …

## QA:

- What makes a method LDA?
- Discriminative Projection Philosophy: At its heart, LDA seeks a projection of data that maximizes class separability. This is done by **maximizing the ratio of between-class variance to within-class variance**.
- Linear (or Pseudo-Linear) Decision Boundaries:  LDA itself results in linear boundaries in the original space.
- LDA as a Prototype or Reference Method:  Many of the variants (e.g., Kernel LDA, Sparse LDA) are explicit extensions of classical LDA: …
- Note:  There is a not clear guide;   but it must share features with Classical LDA.
- Note: Should I Focus on method or the underlying classification problem? I Should Focus on the problem; not the tool.

## Pre-Requisites

- [ ]  Vector
- [ ]  Matrix
- [ ]  Dot Product
- [ ]  Covariance Matrix
- [ ]  Mean
- [ ]  Variance
- [ ]  Covariance
- [ ]  Discriminant Analysis

## Tool Set

| Method | Covariance Assumption | Dim. Reduction | Nonlinear? | Use Case |
| --- | --- | --- | --- | --- |
| LDA | Shared | Yes | No | General-purpose classification |
| QDA | Class-specific | No | No | When classes have different shapes |
| RDA | Weighted mix of LDA & QDA | No | No | Trade-off control between bias/variance |
| Shrinkage LDA | Shared, regularized | Yes | No | High-dimensional, small-sample settings |
| HDA | Class-specific | Yes | No | Like QDA + Dim. reduction |
| Sparse/Penalized LDA | Shared, sparse projection | Yes | No | Feature selection |
| Kernel LDA | Shared, in kernel space | Yes | Yes | Nonlinear separation |
| Mixture Discriminant Analysis | Mixture of Gaussians | Yes | Yes | Multimodal class distributions |

## Fisher’s Linear Discriminant

> Classical LDA.
> 

> Fisher’s Linear Discriminant is a **supervised dimensionality reduction and classification technique** used primarily for binary classification. The goal is to find a **linear projection** of the input data onto a one-dimensional space such that the separation between two classes is maximized.
> 

### **Problem Setup**

Given two classes of data points:

- Class 1 samples: $\{\mathbf{x}_1^{(1)}, \mathbf{x}_2^{(1)}, \ldots, \mathbf{x}_{N_1}^{(1)}\}$
- Class 2 samples: $\{\mathbf{x}_1^{(2)}, \mathbf{x}_2^{(2)}, \ldots, \mathbf{x}_{N_2}^{(2)}\}$

where each $\mathbf{x}_i^{(k)} \in \mathbb{R}^d$.

### **Objective**

Find a projection vector $\mathbf{w} \in \mathbb{R}^d$ such that when the data points are projected onto $\mathbf{w}$,

$y = \mathbf{w}^T \mathbf{x}$ the **class separability** is maximized.

Intuition Behind the Discriminant

- We want the projected means of the two classes to be as far apart as possible.
- At the same time, we want the **variance within each class along $\mathbf{w}$** to be as small as possible (i.e., the classes are tightly clustered after projection).

Formalizing the Objective

1. Compute the **mean vectors** of each class: 
    - $\mathbf{m}_1 = \frac{1}{N_1} \sum_{i=1}^{N_1} \mathbf{x}_i^{(1)},$
    - $\mathbf{m}_2 = \frac{1}{N_2} \sum_{i=1}^{N_2} \mathbf{x}_i^{(2)}$
2. Compute the **within-class scatter matrices**:
    - $S_1 = \sum_{i=1}^{N_1} (\mathbf{x}_i^{(1)} - \mathbf{m}_1)(\mathbf{x}_i^{(1)} - \mathbf{m}_1)^T$
    - $S_2 = \sum_{i=1}^{N_2} (\mathbf{x}_i^{(2)} - \mathbf{m}_2)(\mathbf{x}_i^{(2)} - \mathbf{m}_2)^T$
3. Define the **total within-class scatter matrix**: $S_W = S_1 + S_2$
4. Compute the **between-class scatter matrix**: $S_B = (\mathbf{m}_1 - \mathbf{m}_2)(\mathbf{m}_1 - \mathbf{m}_2)^T$

### Fisher Criterion

Fisher’s Linear Discriminant finds $\mathbf{w}$ that maximizes the following ratio:

$J(\mathbf{w}) = \frac{\mathbf{w}^T S_B \mathbf{w}}{\mathbf{w}^T S_W \mathbf{w}}$

- The numerator $\mathbf{w}^T S_B \mathbf{w}$ measures the **squared distance between projected means**.
- The denominator $\mathbf{w}^T S_W \mathbf{w}$ measures the **projected within-class variance**.

### Solution for $\mathbf{w}$

Maximizing  $J(\mathbf{w})$  is a **Rayleigh quotient** problem. The maximum is obtained when $\mathbf{w}$ is proportional to: $\mathbf{w} = S_W^{-1} (\mathbf{m}_1 - \mathbf{m}_2)$

- $S_W^{-1}$ acts to normalize by the within-class scatter.
- $\mathbf{m}_1 - \mathbf{m}_2$ is the direction of maximum class mean difference.

### Classification Rule

After projection, classify a new sample $\mathbf{x}$ by thresholding its projection:  $y = \mathbf{w}^T \mathbf{x}$

A typical decision boundary is at the midpoint between the projected class means:

$y_0 = \frac{\mathbf{w}^T \mathbf{m}_1 + \mathbf{w}^T \mathbf{m}_2}{2}$  If $y > y_0$, classify as Class 1; otherwise Class 2.

### Key Properties and Remarks

- **FLD assumes the two classes share the same covariance structure**, thus $S_W$ combines the covariances.
- The method is optimal for **linearly separable classes under Gaussian assumption with equal covariance**.
- Unlike PCA, which finds directions of maximal variance irrespective of class labels, FLD explicitly uses label information to maximize class separation.
- Can be generalized to multi-class problems using generalized eigenvalue problems or by reducing the problem to multiple one-vs-rest classifiers.

### Case Study

> Let's walk through **Fisher’s Linear Discriminant** (FLD) step by step using a **handmade dataset with 10 rows and 3 columns** (two features + one class label).
> 

**Dataset**

> We'll construct a small dataset with **2 classes: A and B**, and **2 features: x₁ and x₂**.
> 

| x₁ | x₂ | Class |
| --- | --- | --- |
| 2 | 3 | A |
| 3 | 3 | A |
| 2 | 4 | A |
| 3 | 4 | A |
| 4 | 5 | A |
| 7 | 8 | B |
| 8 | 8 | B |
| 7 | 9 | B |
| 8 | 9 | B |
| 9 | 10 | B |

**Class Statistics**

Split the data:

Class A:

$X_A = 
\begin{bmatrix}
2 & 3 \\
3 & 3 \\
2 & 4 \\
3 & 4 \\
4 & 5 \\
\end{bmatrix}$

Class B:

$X_B = 
\begin{bmatrix}
7 & 8 \\
8 & 8 \\
7 & 9 \\
8 & 9 \\
9 & 10 \\
\end{bmatrix}$

**Compute the Mean Vectors**

Mean of Class A:

$\mu_A = \frac{1}{5}(2+3+2+3+4,\ 3+3+4+4+5) = \frac{1}{5}(14,\ 19) = (2.8,\ 3.8)$

Mean of Class B:

$\mu_B = \frac{1}{5}(7+8+7+8+9,\ 8+8+9+9+10) = \frac{1}{5}(39,\ 44) = (7.8,\ 8.8)$

**Step 4: Compute the Within-Class Scatter Matrix $S_W$**

Each class scatter matrix:

$S_i = \sum_{x \in X_i} (x - \mu_i)(x - \mu_i)^T$

For Class A:

$\text{Centered} = 
\begin{bmatrix}
-0.8 & -0.8 \\
0.2 & -0.8 \\
-0.8 & 0.2 \\
0.2 & 0.2 \\
1.2 & 1.2 \\
\end{bmatrix}$

Then:

$S_A = \sum (x - \mu_A)(x - \mu_A)^T =
\begin{bmatrix}
0.64 & 0.64 \\
0.04 & -0.16 \\
0.64 & 0.04 \\
0.04 & 0.04 \\
1.44 & 1.44 \\
\end{bmatrix}
\Rightarrow S_A = 
\begin{bmatrix}
2.8 & 2.0 \\
2.0 & 2.8 \\
\end{bmatrix}$

For Class B (similar method):

$S_B = 
\begin{bmatrix}
2.8 & 2.0 \\
2.0 & 2.8 \\
\end{bmatrix}$

So the **within-class scatter matrix**:

$S_W = S_A + S_B = 
\begin{bmatrix}
5.6 & 4.0 \\
4.0 & 5.6 \\
\end{bmatrix}$

**Step 5: Compute the Optimal Projection Vector $w$**

Fisher’s criterion: $w \propto S_W^{-1} (\mu_B - \mu_A)$

Compute:

$\mu_B - \mu_A = 
\begin{bmatrix}
7.8 - 2.8 \\
8.8 - 3.8
\end{bmatrix} = 
\begin{bmatrix}
5 \\
5
\end{bmatrix}$

Now compute $S_W^{-1}$:

Let’s calculate:

$S_W^{-1} = \frac{1}{\text{det}(S_W)}$ 

$\begin{bmatrix}
5.6 & -4.0 \\
-4.0 & 5.6
\end{bmatrix}$

Where:

$\text{det}(S_W) = 5.6 \cdot 5.6 - 4.0 \cdot 4.0 = 31.36 - 16 = 15.36$

$S_W^{-1} = \frac{1}{15.36}$

$\begin{bmatrix}
5.6 & -4.0 \\
-4.0 & 5.6
\end{bmatrix}$

Now multiply:

$w \propto S_W^{-1} (\mu_B - \mu_A) = \frac{1}{15.36}
\begin{bmatrix}
5.6 & -4.0 \\
-4.0 & 5.6
\end{bmatrix}$

$\begin{bmatrix}
5 \\
5
\end{bmatrix}
= \frac{1}{15.36}
\begin{bmatrix}
(5.6 - 4.0) \cdot 5 \\
(-4.0 + 5.6) \cdot 5
\end{bmatrix}$

= $\frac{1}{15.36}
\begin{bmatrix}
8 \\
8
\end{bmatrix}$

$w = \frac{8}{15.36}
\begin{bmatrix}
1 \\
1
\end{bmatrix} \propto
\begin{bmatrix}
1 \\
1
\end{bmatrix}$

So the optimal projection direction is along the vector $w = [1, 1]^T$.

**Project the Data**

Project each $x = [x_1, x_2]^T$ onto the line  $y = w^T x = x_1 + x_2$

Projections (Class A):

| x₁ | x₂ | y = x₁ + x₂ |
| --- | --- | --- |
| 2 | 3 | 5 |
| 3 | 3 | 6 |
| 2 | 4 | 6 |
| 3 | 4 | 7 |
| 4 | 5 | 9 |

Projections (Class B):

| x₁ | x₂ | y = x₁ + x₂ |
| --- | --- | --- |
| 7 | 8 | 15 |
| 8 | 8 | 16 |
| 7 | 9 | 16 |
| 8 | 9 | 17 |
| 9 | 10 | 19 |

**Step 7: Interpretation**

We can now see a **clear separation**:

- Class A projections: 5–9
- Class B projections: 15–19

This large gap between the two projected classes confirms that **Fisher's Linear Discriminant found a direction that maximally separates the classes.**

## **Quadratic Discriminant Analysis (QDA)**

> 

## Regularized Discriminant Analysis (RDA)

> 

## Shrinkage LDA

> 

## **Penalized / Sparse LDA**

> 

## Kernel LDA

> 

## Mixture Discriminant Analysis (MDA)

> 

## References

- [Matrix](../mathematical/matrix.md)
- [Vector](../mathematical/vector.md)
- [Variance](variance.md)
- [Scatter Matrix](../mathematical/scatter-matrix.md)
- [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)
- [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis#cite_note-cohen-9)
- [An illustrative introduction to Fisher's Linear Discriminant](https://sthalles.github.io/fisher-linear-discriminant/)
- [‣](https://app.notion.com/p/10e598edb790817d880ae42fdc1a10a6?pvs=21)
