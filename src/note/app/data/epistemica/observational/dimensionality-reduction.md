---
tags: [representation, technique]
---

# Dimensionality Reduction

 : Autoencoder (Autoencoder%20b28b738cfe5d467b90d4630f29b6c0a4.md), Principal Component Analysis (PCA) (Principal%20Component%20Analysis%20(PCA)%20b3fb537909bd4339bcf53a9387bfe9de.md), UMAP (Uniform Manifold Approximation and Projection) (UMAP%20(Uniform%20Manifold%20Approximation%20and%20Projectio%20347c0f5171ec805c99f5c8f23f5f7e2f.md)

> Data: Data Set -> Data Set
> 

> **Data Reduction Techniques:** Methods for reducing data dimensionality, such as feature selection and feature extraction.
> 

> For a comprehensive view on re-representation see ([Representation](../mathematical/representation.md)).
> 

## Techniques

> Data: Data Set -> Data Set
> 

> Dimension reduction techniques are a set of methods used to reduce the number of variables or dimensions in a dataset while still retaining the majority of the information present in the original dataset. This is accomplished by identifying and eliminating the dimensions that contribute the least to the overall variance in the dataset.
> 

| **Technique** | **Type** | **Description** | **Supervised / Unsupervised** |
| --- | --- | --- | --- |
| **Principal Component Analysis (PCA)** | Linear Dimension Reduction | Finds orthogonal axes capturing maximum variance, reduces dimensionality by projecting data onto these axes. | Unsupervised |
| **Singular Value Decomposition (SVD)** | Matrix Factorization | Decomposes data matrix into product of three matrices, useful for dimensionality reduction and noise reduction. | Unsupervised |
| **Linear Discriminant Analysis (LDA)** | Linear Dimension Reduction | Finds linear combinations of features that best separate classes, maximizing class separability. | Supervised |
| **t-Distributed Stochastic Neighbor Embedding (t-SNE)** | Nonlinear Dimension Reduction | Visualizes high-dimensional data by preserving local structures in low-dimensional embeddings. | Unsupervised |
| **Non-negative Matrix Factorization (NMF)** | Matrix Factorization | Factorizes data into non-negative basis vectors and coefficients, useful for parts-based representation. | Unsupervised |
| **Independent Component Analysis (ICA)** | Blind Source Separation | Finds statistically independent components, often used in signal processing and feature extraction. | Unsupervised |
| **Random Projection** | Randomized Linear Reduction | Projects data onto a lower-dimensional random subspace, computationally efficient for large data. | Unsupervised |
| **Autoencoders** | Neural Network-based | Neural networks trained to reconstruct input from compressed representations (latent space). | Unsupervised |
| **Uniform Manifold Approximation and Projection (UMAP)** | Nonlinear Dimension Reduction | Preserves global and local data structure, faster than t-SNE, suitable for visualization and clustering. | Unsupervised |
| **Self-Organizing Map (SOM)** | Neural Network-based | Maps high-dimensional data onto a 2D grid preserving topological properties, useful for clustering and visualization. | Unsupervised |
| **Latent Semantic Analysis (LSA)** | Matrix Factorization | Applies SVD to text data to capture semantic structure in lower dimensions, widely used in NLP. | Unsupervised |
| **Isomap** | Manifold Learning | Preserves geodesic distances in data lying on a nonlinear manifold, for nonlinear dimension reduction. | Unsupervised |
| **Factor Analysis** | Statistical Modeling | Models observed variables as linear combinations of latent factors plus noise, reducing dimensionality. | Unsupervised |
| **Kernel PCA** | Kernelized Nonlinear PCA | Extends PCA to nonlinear mappings using kernel trick, capturing nonlinear structures. | Unsupervised |
| **Compactification (Topological Data Analysis)** | Topological Approach | Maps high-dimensional data into a compact, often lower-dimensional space while preserving topological features. | Unsupervised |
| **Feature Selection** | Filtering/Wrapper Methods | Selects a subset of the most relevant features based on criteria (e.g., mutual information, variance). | Supervised / Unsupervised |
| **Manifold Learning** | Nonlinear Dimension Reduction | Algorithms like Locally Linear Embedding (LLE) that assume data lies on a low-dimensional manifold. | Unsupervised |
| **Deep Variational Autoencoders (VAE)** | Probabilistic Neural Network | Learns probabilistic latent variables for dimensionality reduction with generative modeling capabilities. | Unsupervised |

## References

- Fodor, I. K. (2002). A survey of dimension reduction techniques.
- [Dimensionality Reduction](https://www.wikiwand.com/en/Dimensionality_reduction)
- Independent Component Analysis:
    - [Independent component analysis](https://www.wikiwand.com/en/Independent_component_analysis) - Fodor, I. K. (2002). A survey of dimension reduction techniques.
    - [Dimensionality Reduction](https://www.wikiwand.com/en/Dimensionality_reduction)
    - [Z-transform](https://www.wikiwand.com/en/Z-transform)
    - [Harmonic Analysis](https://www.wikiwand.com/en/Harmonic_analysis)
    - [Fourier Transform](https://www.wikiwand.com/en/Integral_transform)
    - [Transformation](https://www.wikiwand.com/en/Transformation_(function))
    - [Compression](https://www.wikiwand.com/en/Compression)
- https://en.wikipedia.org/wiki/Compactification_(mathematics)
- https://en.wikipedia.org/wiki/Compactification_(physics)
- https://en.wikipedia.org/wiki/Compact_space
