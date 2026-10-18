---
tags: [causal-discovery]
---

# Causal Discovery

Formula: 16

> **Causal Discovery** is the process of identifying **causal relationships** from data—going beyond mere correlations to determine **which variables influence others**, and how.
> 

| **Approach** | **Description** | **Examples/Methods** | **Strengths** | **Limitations** |
| --- | --- | --- | --- | --- |
| **Constraint-Based** | Infers causal relationships using conditional independence tests. | PC Algorithm   - FCI (Fast Causal Inference) | Handles latent variables (FCI). | Sensitive to errors in independence tests. |
| **Score-Based** | Searches for the causal graph that maximizes a scoring function. | GES (Greedy Equivalence Search) | Finds optimal models for given scores. | Computationally intensive for large datasets. |
| **Functional Causal Models (FCMs)** | Assumes specific functional relationships (e.g., linear or non-linear). | LiNGAM (Linear Non-Gaussian Acyclic Model)  - Additive Noise Models (ANMs) | Models non-linear relationships. | Requires assumptions about data distribution. |
| **Hybrid Approaches** | Combines constraint-based and score-based methods. | MMHC (Max-Min Hill Climbing) | Balances efficiency and accuracy. | May inherit weaknesses of both methods. |
| **Time-Series Causal Discovery** | Identifies causation in time-dependent data. | Granger Causality  - Transfer Entropy | Captures temporal relationships. | Assumes stationary processes. |
| **Interventional Data** | Uses data from experiments where variables are actively manipulated. | Do-calculus  - Targeted interventions | Strong causal guarantees. | Often requires expensive or infeasible experiments. |
| **Information-Theoretic** | Measures causal influence via information flow metrics. | Transfer Entropy  - Directed Information | Useful for complex systems (e.g., neuroscience). | Computationally demanding; may miss fine-grained causation. |

## References

- Spirtes, P., Glymour, C., & Scheines, R. (2001). Causation, prediction, and search. MIT press.
- Gmeiner, P. (2020). Information-Theoretic Approximation to Causal Models. arXiv preprint arXiv:2007.15047.
