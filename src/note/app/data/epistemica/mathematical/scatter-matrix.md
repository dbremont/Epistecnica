---
tags: [inference, linear-algebra]
---

# Scatter Matrix

 : Matrix (Matrix%20171c0f5171ec80c58898c4e26151fbb8.md), Covariance Matrix (Covariance%20Matrix%2013cc0f5171ec800db8ebedc83ae4ebef.md)

> The **scatter matrix** is a way to summarize the *spread (or dispersion)* of a dataset in multiple dimensions. It's especially important in **Fisher’s Linear Discriminant Analysis (LDA)**, **PCA**, and other multivariate statistical techniques.
> 

> Note: The **scatter matrix will always be a square matrix**.
> 

## 🧠 Core Idea

> In **1D**, you use **variance** to measure how spread out data is.
> 

> In **multidimensional space**, you use the **scatter matrix**, which generalizes the concept of variance and covariance.
> 

## 🧾 Formulation

Given a set of $n$ vectors $x_i \in \mathbb{R}^d$, and the **mean vector** $\mu \in \mathbb{R}^d$: 

$S = \sum_{i=1}^{n} (x_i - \mu)(x_i - \mu)^T$

Where:

- Each $x_i \in \mathbb{R}^d$ is a **column vector** of $d$ features.
- $(x_i - \mu)(x_i - \mu)^T$ is an **outer product** of a $d \times 1$ vector with itself, producing a $d \times d$ matrix.

Therefore:

- $S \in \mathbb{R}^{d \times d}$: always **square**.
- The matrix entries represent **variance and covariance** between the $d$ variables.
- The **diagonal** elements represent **variances** of each feature.
- The **off-diagonal** elements represent **covariances** between features.

## 📘 What It Represents

| **Matrix Entry** | **Interpretation** |
| --- | --- |
| **$S_{ii}$** | Variance of the i-th variable |
| **$S_{ij}, i \ne j$** | Covariance between variables $i$  and $j$ |
| **Overall structure** | Orientation and scale of the data cloud in $\mathbb{R}^d$ |
| **Eigenvectors** | Principal directions of variation |
| **Eigenvalues** | Amount of variation in each principal direction (before normalization) |

## 🧠 Interpretation in Practice

- **PCA**: You find the eigenvectors of the scatter matrix to identify the principal components (directions of max variance).
- **Fisher's LDA**: You compare **within-class** and **between-class** scatter matrices to find directions that best separate classes.
- **Multivariate statistics**: The scatter matrix is central to understanding **spread**, **correlation**, and **redundancy** in features.

## 🧭 Geometric Insight

Think of a scatter matrix as defining the shape of an **ellipsoid** that encloses your data points:

- The **axes** of the ellipsoid = eigenvectors (directions of spread)
- The **lengths** of the axes = eigenvalues (how much it spreads)

## 📘 Case Study

Suppose:

$x_1 = \begin{bmatrix} 2 \\ 3 \end{bmatrix},\quad
x_2 = \begin{bmatrix} 4 \\ 5 \end{bmatrix},\quad
x_3 = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$

Then the mean:

$\mu = \frac{1}{3}(x_1 + x_2 + x_3) = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$

Now compute each outer product:

$(x_1 - \mu)(x_1 - \mu)^T = 
\begin{bmatrix} -1 \\ -1 \end{bmatrix}
\begin{bmatrix} -1 & -1 \end{bmatrix} = 
\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$

Similarly, for $x_2$ and $x_3$:

$(x_2 - \mu)(x_2 - \mu)^T = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}, \quad
(x_3 - \mu)(x_3 - \mu)^T = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$

Add them:

$S = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} + 
    \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} + 
    \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} =
\begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}$

$S = \begin{bmatrix}
\text{Var}(X_1) & \text{Cov}(X_1, X_2) \\
\text{Cov}(X_2, X_1) & \text{Var}(X_2)
\end{bmatrix}$

## References

- https://en.wikipedia.org/wiki/Scatter_matrix
- [Variance](../observational/variance.md)
