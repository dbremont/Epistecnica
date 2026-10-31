---
tags: [learning-system]
---

# Mixture Model

 : Clustering Model (Clustering%20Model%207b89d6294a944f2287f74058a5e24894.md), Classification (Classification%204fc227ef54a448f68876795fc51d30c8.md)

> **Mixture Models:** Model data as a combination of multiple probability distributions, such as Gaussian mixture models for clustering.
> 

> A **mixture model** is a statistical framework that models a complex probability distribution as a weighted sum of simpler **component distributions**, where each component represents a distinct subpopulation or latent class, and the weights correspond to the mixing proportions of these components within the overall population.
> 

> **It's a set of techniques to model datasets** in which sub-sets have been generated using different probability distribution.
> 

> A **mixture model** is a statistical framework used to represent datasets where observations are generated from multiple subpopulations, each characterized by its own distinct probability distribution, and the overall dataset is modeled as a **combination** (or **mixture**) of these distributions.
> 

## List of Models

> 

| **Mixture Model** | **Components** | **Common Algorithms** |
| --- | --- | --- |
| **Gaussian Mixture Model (GMM)** | Gaussian (Normal) Distributions | Clustering, density estimation, anomaly detection |
| **Dirichlet Process Mixture Model (DPMM)** | Infinite Gaussian Mixtures | Markov Chain Monte Carlo (MCMC), Variational Inference |
| **Bernoulli Mixture Model (BMM)** | Bernoulli Distributions | Binary data clustering (e.g., image segmentation) |
| **Multinomial Mixture Model** | Multinomial Distributions | Topic modeling, text analysis |
| **Poisson Mixture Model (PMM)** | Poisson Distributions | Count data clustering (e.g., traffic modeling) |
| **Hidden Markov Model (HMM)** | Mixture of Markov Chains | Forward-Backward, Viterbi, Baum-Welch |
| **Finite Mixture Model (FMM)** | Finite number of probability distributions | EM, Gibbs Sampling |
| **Latent Class Analysis (LCA)**  | … | … |
| **Latent Profile Analysis
(LPA)** | … | … |

## Mixture Model Function Signatures

> Which types of function signatures are supported by mixture models?
> 

| **Function Signature** | **Meaning** | **Example Use Case** |
| --- | --- | --- |
| $f: \mathbb{R}^d \to \mathbb{R}_{\geq 0}$ | Unconditional density | Modeling population distribution |
| $f: \mathbb{R}^n \to \mathcal{P}(\mathbb{R}^m)$ | Conditional output distribution | Predicting uncertain continuous outputs |
| $f: \mathbb{R}^n \to \mathbb{R}^m$ (mean or MAP) | Deterministic regression | Point prediction with uncertainty model |
| $f: \mathbb{R}^n \to \{1, ..., K\}$ | Hard cluster assignment | Clustering |
| $f: \mathbb{R}^n \to \Delta^{K-1}$ | Soft (probabilistic) cluster membership | Soft classification |
| $f: Z \to \mathbb{R}^d$ | Latent-to-observed generation | Data synthesis from latent space |

## Limitation

> Which functions can it model?
> 

> What are the limitations of mixture models?
> 

## References

- https://en.wikipedia.org/wiki/Mixture_model
- http://bactra.org/notebooks/mixture-models.html
- https://stephens999.github.io/fiveMinuteStats/mixture_models_01.html
- https://github.com/dbremont/algorithms/blob/main/om/gmm.ipynb
- https://en.wikipedia.org/wiki/Multivariate_random_variable
- https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm
- https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/mixture/_base.py#L172
- https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm
