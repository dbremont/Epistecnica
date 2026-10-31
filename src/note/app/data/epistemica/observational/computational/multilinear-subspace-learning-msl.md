---
tags: [data-representation, learning-system]
---

# Multilinear Subspace Learning (MSL)


> Learn Data Representations.
> 

> **Multilinear Subspace Learning (MSL)** is a framework for learning *low-dimensional representations* of **high-order data** (e.g., tensors like videos, 3D images, or multi-sensor recordings) by exploiting their inherent *multilinear (multiway) structure*.
> 

> **Multilinear Subspace Learning (MSL)** is about **finding low-dimensional subspaces** for data that is naturally represented as **tensors** (i.e., multiway arrays) rather than as vectors.
> 

## Breviarium

Summary of the Core MSL Problem:

Find matrices  $\{U^{(n)}\}_{n=1}^N$ such that:

- The tensors are **projected** into low-dimensional spaces,
- Important properties (variance, class separability, structure) are **preserved** or **enhanced**,
- The optimization usually involves **alternating least squares (ALS)** or **gradient-based methods** across modes.

## Setup

- You have a set of tensor samples: $\{ \mathcal{X}_i \in \mathbb{R}^{I_1 \times I_2 \times \dots \times I_N} \}_{i=1}^M$
    
    where:
    
    - MM = number of samples,
    - $\mathcal{X}_i$ = the iith tensor,
    - $N$ = tensor order (number of modes),
    - $I_n$ = dimensionality along mode $n$.
- The goal is to find projection matrices: $\{ U^{(n)} \in \mathbb{R}^{I_n \times d_n} \}_{n=1}^N$
    
    where:
    
    - $d_n \ll I_n$ is the reduced dimensionality for mode nn,
    - $U^{(n)}$ are orthonormal (usually ($I(U^{(n)})^\top U^{(n)} = I$ ).

## Formulation

### **Multilinear** Projection

> Each tensor is projected via a **multilinear projection**:
> 

$\mathcal{Y}_i = \mathcal{X}_i \times_1 (U^{(1)})^\top \times_2 (U^{(2)})^\top \times_3 \cdots \times_N (U^{(N)})^\top$

where:

- $\times_n$ denotes the **n-mode product** between a tensor and a matrix.

Result:

- Each projected tensor $\mathcal{Y}_i$  has size  $\times d_2 \times \cdots \times d_N$.

### Objective Function

Different variants of MSL define different objective functions. A general template is: $\min_{\{U^{(n)}\}} \; \sum_{i=1}^M \mathcal{L}\left( \mathcal{X}_i, \mathcal{Y}_i \right)$

where:

- $\mathcal{L}$ measures the loss, e.g., reconstruction error, discriminative loss, or other criteria depending on the MSL method.

**Common loss choices:**

- **Reconstruction loss** (like PCA):
    
    $\mathcal{L}\left( \mathcal{X}_i, \mathcal{Y}_i \right) = \left\| \mathcal{X}_i - \mathcal{Y}_i \times_1 U^{(1)} \times_2 U^{(2)} \times_3 \cdots \times_N U^{(N)} \right\|_F^2$
    
    (Frobenius norm)
    
- **Fisher discrimination loss** (for classification tasks):
    - Maximize **between-class scatter**, minimize **within-class scatter** in tensor space.

### **Tucker Decomposition**

> Tucker decomposition is a **higher-order generalization of matrix SVD/SVD** for tensors. It approximates an *N*-way tensor by a **core tensor** and **factor matrices** along each mode. Below is its formal definition, properties, and connections to other methods.
> 

Given an *N*-th order tensor $\mathcal{X} \in \mathbb{R}^{I_1 \times I_2 \times \dots \times I_N}$, its **Tucker decomposition** is:

$\mathcal{X} \approx \mathcal{G} \times_1 U^{(1)} \times_2 U^{(2)} \times_3 \dots \times_N U^{(N)}$

where:

- $\mathcal{G} \in \mathbb{R}^{R_1 \times R_2 \times \dots \times R_N}$ is the **core tensor** (captures interactions between subspaces).
- $U^{(n)} \in \mathbb{R}^{I_n \times R_n}$ are **factor matrices** (subspace bases for each mode).
- $\times_n$ is the **n-mode product** (matrix multiplication along mode $n$.

**Explicit Element-wise Form**
$x_{i_1 i_2 \dots i_N} \approx \sum_{r_1=1}^{R_1} \sum_{r_2=1}^{R_2} \dots \sum_{r_N=1}^{R_N} g_{r_1 r_2 \dots r_N} \cdot u^{(1)}{i_1 r_1} u^{(2)}{i_2 r_2} \dots u^{(N)}_{i_N r_N}$

## References

- 
- https://en.wikipedia.org/wiki/Multilinear_subspace_learning
- https://en.wikipedia.org/wiki/Tucker_decomposition
- Ledyard R. Tucker (September 1966). "Some mathematical notes on three-mode factor analysis". Psychometrika. 31 (3): 279–311. doi:10.1007/BF02289464. PMID 5221127.
- Kolda & Bader (2009). *Tensor Decompositions and Applications*.
- De Lathauwer et al. (2000). *A Multilinear Singular Value Decomposition*.
