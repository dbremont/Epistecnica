---
tags: [functional, linear-algebra]
---

# Norm

 : Linear Space (Linear%20Space%20b935942a1a064729b3f2be42d174923a.md), Inner Product Space (Inner%20Product%20Space%20ccdaf9b41b20443cb416c7b1bd5e4ef7.md), Linear  Algebra (Linear%20Algebra%20d4ca395ec6c545c1bf2387d2fbdc732f.md), Inner Product (Inner%20Product%20171c0f5171ec80439aa0fc448d33b98a.md)

> A norm generalizes the idea of "length" to any vector space. It tells you **how big**, **long**, or **far from zero** a vector is.
> 

QA:

- How does the notion of **“norm”** help in **addressing convergence problems** involving vectors and matrices?
- What is the origin of the concept?
- When the concept was formalized?
- List of uses of the concept of a **“norm”** taught mathematics.
- Which are the different norms and their uses
- …

## Definition

> A **norm** is a function that assigns a strictly positive length or size to each vector in a vector space. Formally, for a vector space $V$ over a field $\mathbb{F}$ (typically $\mathbb{R}$ or $\mathbb{C}$), a norm is a function $\|\cdot\|: V \to \mathbb{R}$ that satisfies the following properties for all vectors $\mathbf{x}, \mathbf{y} \in V$ and scalar $\alpha \in \mathbb{F}$:
> 
1. **Non-Negativity**: $\|\mathbf{x}\| \geq 0$, and $\|\mathbf{x}\| = 0$ if and only if $\mathbf{x} = \mathbf{0}$.
2. **Scalability**: $\|\alpha \mathbf{x}\| = |\alpha| \cdot \|\mathbf{x}\|$.
3. **Triangle Inequality**: $\|\mathbf{x} + \mathbf{y}\| \leq \|\mathbf{x}\| + \|\mathbf{y}\|$.

## List of Norms

> Norms are used to measure the magnitude or length of vectors and generalize the concept of distance in vector spaces. Common examples include the **Euclidean norm** (L2 norm), **Manhattan norm** (L1 norm), and **maximum norm** (L∞ norm).
> 

> Norms are functions that measure the size or length of vectors, matrices, or functions. They are essential in regularization, distance metrics, and convergence analysis.
> 

Below is a table summarizing various **norms** used in mathematics, machine learning, and optimization. 

| **Norm Type** | **Object** | **Definition** | **Use Cases** | **Properties** |
| --- | --- | --- | --- | --- |
| **L1 Norm (Manhattan Norm)** | Vector | $||\mathbf{x}||_1 = \sum{i=1}^n$ | Sparse signal recovery, Lasso regression, robust statistics | Non-negative, scalable, promotes sparsity, satisfies triangle inequality |
| **L2 Norm (Euclidean Norm)** | Vector | $||\mathbf{x}||_2 = \sqrt{\sum{i=1}^n x_i^2}$ | Least squares optimization, machine learning, physics | Non-negative, scalable, smooth penalty, satisfies triangle inequality |
| **Lp Norm (Hölder Norm)** | Vector | $*||\mathbf{x}||_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p}*$ | Generalization of vector norms, used in optimization and machine learning | Non-negative, scalable, satisfies triangle inequality for $p ≥ 1$ |
| **L∞ Norm (Max Norm)** | Vector | $\|\mathbf{x}\|_\infty = \max(|x_1|, |x_2|, \dots, |x_n|)$ | Minimax problems, control theory, outlier detection | Non-negative, scalable, focuses on the largest element, satisfies triangle inequality |
| **Frobenius Norm** | Matrix | $\|\mathbf{A}\|F = \sqrt{\sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^2}$ | Matrix factorization, regularization, signal processing | Non-negative, scalable, submultiplicative, satisfies triangle inequality |
| **Nuclear Norm** | Matrix | $|\mathbf{A}|* = \sum_{i=1}^k \sigma_i$  (sum of singular values) | Low-rank matrix recovery, matrix completion, robust PCA | Non-negative, scalable, convex, promotes low-rank solutions |
| **Mahalanobis Norm** | Vector | $|\mathbf{x}|_M = \sqrt{(\mathbf{x} - \mathbf{\mu})^T \mathbf{S}^{-1} (\mathbf{x} - \mathbf{\mu})}$ | Outlier detection, multivariate statistics, machine learning | Measures distance relative to a distribution, accounts for covariance |
| **Spectral Norm** | Matrix | $|\mathbf{A}|2 = \sigma{\text{max}}(\mathbf{A})$  (largest singular value) | Matrix analysis, control theory, optimization | Non-negative, scalable, measures maximum stretch of a matrix |
| **Hamming Norm** | Vector | $|\mathbf{x}|_H = \text{Number of non-zero elements in } \mathbf{x}$ | Coding theory, error detection, sparse representations | Counts non-zero elements, measures sparsity |
| **Total Variation Norm** | Vector,  Matrix | It’s really an umbrella term of a set of norms. | Image processing, signal denoising, regularization | Measures total change in a signal, promotes piecewise smoothness |
| **Operator Norm** | Matrix | $||\mathbf{A}||_{\text{op}} = \sup_{||\mathbf{x}||=1} ||\mathbf{A}\mathbf{x}|
|$ | Functional analysis, linear algebra, optimization | Non-negative, scalable, measures maximum amplification of a matrix |

## **Total Variation Norm**

> The **Total Variation (TV) Norm** is a mathematical concept used primarily in signal processing, image processing, and optimization. It measures the total change or variation in a signal or image, making it particularly useful for tasks like denoising, edge detection, and regularization.
> 

| **Definition** | **Norm Type** | **Use Cases** | **Properties** |
| --- | --- | --- | --- |
| For a discrete 1D signal $\mathbf{x} = (x_1, x_2, \dots, x_n)$, the Total Variation Norm is defined as:

$\|\mathbf{x}\|_{\text{TV}} = \sum_{i=1}^{n-1} |x_{i+1} - x_i|$ | 1D Signals (Discrete Case) | Signal denoising,  Signal smoothing,  Edge detection in 1D signals | Measures total change in a 1D signal,  Non-negative, Scalable, Satisfies triangle inequality |
| For a 2D image $\mathbf{x} = (x_1, x_2, \dots, x_n)$, the Total Variation Norm is defined as:
$\|\mathbf{x}\|{\text{TV}} = \sum_{i=1}^{n-1} |x_{i+1} - x_i|$
This measures the sum of absolute differences between neighboring pixels in both horizontal and vertical directions. | 2D Images (Discrete Case) | Image denoising, Edge detection in images, Medical imaging, Regularization in image processing | Measures total change in a 2D image,  Non-negative, Scalable,  Preserves edges, Promotes piecewise smoothness |
| For a continuous function  $f$, the Total Variation Norm is defined as:
$\|f\|_{\text{TV}} = \int |f'(x)| \, dx$. This measures the integral of the absolute value of the derivative of $f$. | Continuous Functions | Analysis of continuous signals  - Functional analysis  - Regularization in continuous domains |  |

## Vector Norms

> 

## Operator Norms

> 

## Matrix Norms

> 

## Function Norms

> 

## Sequence Norms

> 

## Tensor Norms

> 

## References

- https://en.wikipedia.org/wiki/Total_variation
- https://en.wikipedia.org/wiki/Banach_space
- https://en.wikipedia.org/wiki/Hilbert_space
- https://en.wikipedia.org/wiki/Inner_product_space
- https://en.wikipedia.org/wiki/Dot_product
- https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality
- https://en.wikipedia.org/wiki/Inner_product_space#Norm
- https://en.wikipedia.org/wiki/Norm_(mathematics)
- https://encyclopediaofmath.org/wiki/Norm
- https://en.wikipedia.org/wiki/Normed_vector_space
- https://en.wikipedia.org/wiki/Matrix_norm
- https://en.wikipedia.org/wiki/Operator_norm
- https://en.wikipedia.org/wiki/Lp_space
- https://en.wikipedia.org/wiki/Normed_vector_space
- https://mathworld.wolfram.com/L1-Norm.html
- https://mathworld.wolfram.com/L2-Norm.html
- https://ekamperi.github.io/machine%20learning/2019/10/19/norms-in-machine-learning.html
- [‣](https://app.notion.com/p/10f598edb79080219456c7eb4cb94b94?pvs=21)
- [‣](https://app.notion.com/p/10f598edb79080859494e0b77bfac198?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081fcb9d0efe68593746e?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081eda6b7fa4657d9ef65?pvs=21)
- [‣](https://app.notion.com/p/10e598edb7908182b327ce39ed53f212?pvs=21)
- [‣](https://app.notion.com/p/10e598edb79081e08ce6cdec3f280866?pvs=21)
- Videos
    - https://www.youtube.com/watch?v=DkyM93Wgh_0
    - https://www.youtube.com/watch?v=af3wvva1dus
    - https://www.youtube.com/watch?v=wyoS89J3ap4
    - https://www.youtube.com/watch?v=sFq2zyDCy5Q
    - http://njohnston.ca/publications/introduction-to-linear-and-matrix-algebra/
    - https://www.youtube.com/playlist?list=PLRDl2inPrWQW1QSWhBU0ki-jq_uElkh2a
    - https://www.youtube.com/watch?v=5fN2J8wYnfw
    - https://www.youtube.com/watch?v=homSXANJZ5w
    - https://www.youtube.com/watch?v=G2RKg1pHApc
    - https://www.youtube.com/watch?v=h7zmVMWMawo
    - https://www.youtube.com/watch?v=-r8KYlSLlFw
    - https://www.youtube.com/watch?v=elg_PEwplw0&list=PLBEl4BT8wUgNKTl0bgy6BMQXAShRZor5l&index=1
    - https://www.youtube.com/watch?v=SCTWQ_W1Cw8
- https://math.stackexchange.com/questions/465414/who-introduced-the-term-norm-into-mathematics
- https://jeff560.tripod.com/n.html [Search For Norm]
