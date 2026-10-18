---
tags: [inference, linear-algebra]
---

# Covariance Matrix

 : Scatter Matrix (Scatter%20Matrix%20207c0f5171ec80cd9dd4c3514f714cb3.md)

> In this note, we explore the concept of a covariance matrix, which represents the **covariances** between a set of vectors.
> 

![](https://media.geeksforgeeks.org/wp-content/uploads/20230822231834/image-(2).png)

## 🗂️ Index

## ❓ QA

- …

## **✅ Note Quality Evaluation**

> (**⭐⭐⭐⭐⭐**)  → Does this note adhere to the prototype structure? If it is incomplete, in what way? See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21).
> 

## 📘 Breviarium

> A comprehensive exploration of the topic.
> 

> **Nucleus (🧬)** → Deepest Essence (What is the deepest essence?)
> 

> **Telos (🎯)** → Intent (What is it for? Toward what end is it directed?)
> 

> **Techne (🛠️)** → Function / Used (By what craft or process is it made to work?)
> 

> **Idoneitas (📏)** → Suitability (How well is it fitted for its purpose?)
> 

> **Limites** (🚧) → Limits (What are its boundaries? What constraints define its operation?)
> 

> **Contextus (🌐)** → Context (What is the historical, cultural, or situational context in which this study occurs?)
> 

## 🧠 Autovaluatio

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

## Formulation

The **covariance matrix** of a random vector $\mathbf{X} = [X_1, X_2, \dots, X_n]^\top \in \mathbb{R}^n$ is the **symmetric** and **positive semi-definite** matrix $\Sigma \in \mathbb{R}^{n \times n}$ defined as: 

$\Sigma = \operatorname{Cov}(\mathbf{X}) = \mathbb{E}\left[(\mathbf{X} - \mathbb{E}[\mathbf{X}])(\mathbf{X} - \mathbb{E}[\mathbf{X}])^\top\right]$

Each element $\Sigma_{ij}$ of the matrix represents the **covariance between the i-th and j-th components** of $\mathbf{X}$:

$\Sigma_{ij} = \operatorname{Cov}(X_i, X_j)$

- The **diagonal entries** $\Sigma_{ii}$ correspond to the **variances** of the individual components.
- The **off-diagonal entries** reflect the **pairwise linear dependencies** between different components.
- Since $\Sigma = \Sigma^\top$, the matrix is symmetric.
- $\Sigma \succeq 0$, meaning it is **positive semi-definite**—i.e., for all $\mathbf{z} \in \mathbb{R}^n$, $\mathbf{z}^\top \Sigma \mathbf{z} \geq 0$.

## Formulation N-X

Let $\mathbf{X}^{(1)} \in \mathbb{R}^{d_1}, \mathbf{X}^{(2)} \in \mathbb{R}^{d_2}, \dots, \mathbf{X}^{(N)} \in \mathbb{R}^{d_N}$ be $N$ random vectors (possibly of different dimensions). The **joint covariance structure** among them can be expressed as a **block matrix**:

$\Sigma =
\begin{bmatrix}
\operatorname{Cov}(\mathbf{X}^{(1)}, \mathbf{X}^{(1)}) & \cdots & \operatorname{Cov}(\mathbf{X}^{(1)}, \mathbf{X}^{(N)}) \\
\vdots & \ddots & \vdots \\
\operatorname{Cov}(\mathbf{X}^{(N)}, \mathbf{X}^{(1)}) & \cdots & \operatorname{Cov}(\mathbf{X}^{(N)}, \mathbf{X}^{(N)})
\end{bmatrix}
\in \mathbb{R}^{(d_1 + \cdots + d_N) \times (d_1 + \cdots + d_N)}$

Each block $\operatorname{Cov}(\mathbf{X}^{(i)}, \mathbf{X}^{(j)}) \in \mathbb{R}^{d_i \times d_j}$  is defined as: $\operatorname{Cov}(\mathbf{X}^{(i)}, \mathbf{X}^{(j)}) = \mathbb{E}\left[(\mathbf{X}^{(i)} - \mathbb{E}[\mathbf{X}^{(i)}])(\mathbf{X}^{(j)} - \mathbb{E}[\mathbf{X}^{(j)}])^\top\right]$

## Case Study

Let's say that we have some data:

Rows = observations, Columns = variables (X and Y)

$A = \begin{bmatrix}
2 & 3 \\
4 & 7 \\
6 & 11 \\
\end{bmatrix}$

Step 2: Compute the mean of each variable

- Mean of X: $\bar{X} = \frac{2 + 4 + 6}{3} = 4$
- Mean of Y: $\bar{Y} = \frac{3 + 7 + 11}{3} = 7$

Step 3: Subtract the mean (center the data)

$A_{\text{centered}} = \begin{bmatrix}
2 - 4 & 3 - 7 \\
4 - 4 & 7 - 7 \\
6 - 4 & 11 - 7 \\
\end{bmatrix}
= \begin{bmatrix}
-2 & -4 \\
0 & 0 \\
2 & 4 \\
\end{bmatrix}$

Step 4: Compute the covariance matrix

Let  $X$ be the centered matrix:

$X = \begin{bmatrix}
-2 & -4 \\
0 & 0 \\
2 & 4 \\
\end{bmatrix}$

Covariance matrix:

$\text{Cov}(X) = \frac{1}{n - 1} X^\top X$

Here,  $n = 3$, so:
$\text{Cov}(X) = \frac{1}{2}
\begin{bmatrix}
-2 & 0 & 2 \\
-4 & 0 & 4 \\
\end{bmatrix}
\begin{bmatrix}
-2 & -4 \\
0 & 0 \\
2 & 4 \\
\end{bmatrix}
= \frac{1}{2}
\begin{bmatrix}
8 & 16 \\
16 & 32 \\
\end{bmatrix}
= \begin{bmatrix}
4 & 8 \\
8 & 16 \\
\end{bmatrix}$

## References

- [General Topic Note Template](https://app.notion.com/p/General-Topic-Note-Template-1cec0f5171ec801e86e6c894702cfe23?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- https://en.wikipedia.org/wiki/Covariance_matrix
- [Covariance](../observational/covariance.md)
- [Covariance Matrix](covariance-matrix.md)
