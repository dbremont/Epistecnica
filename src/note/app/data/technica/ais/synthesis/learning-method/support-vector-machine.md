---
tags: [learning-system]
---

# Support Vector Machine

 : Kernel Method (Kernel%20Method%2018ec0f5171ec802a8703f3da90ba7eb3.md)

> The **Support Vector Machine (SVM)** is one fundamental method in machine learning, but it encompasses several variations or extensions of the basic approach, which are used for different tasks.
> 

> **Note:** Both **kernel-based** and **non-kernel-based** formulations of the method exist.
> 

## QA

- …

## Variations

> 

| **SVM Variant** | **Type** | **Use Case** | **Key Idea** |
| --- | --- | --- | --- |
| **Linear SVM** | Classification | Binary or multi-class classification with linearly separable data | Finds a hyperplane that maximizes the margin between classes. |
| **Non-Linear SVM** (Kernel SVM) | Classification | Classification tasks where data is not linearly separable | Uses kernel functions (e.g., RBF, Polynomial) to map data into a higher-dimensional space for linear separation. |
| **Support Vector Regression (SVR)** | Regression | Predicting continuous values (e.g., price prediction) | Finds a function that approximates data within a margin and allows some deviation. |
| **Nu-SVM** | Classification / Regression | Controls the number of support vectors and margin errors | A variant where the **nu** parameter defines the upper bound on margin errors and the lower bound on support vectors. |
| **One-Class SVM** | Anomaly Detection | Outlier detection or novelty detection | Learns a boundary that defines "normal" data, used for identifying outliers or rare events. |

## References

- [KNN vs SVM](https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.ipynb)
- [Support Vector Machines (SVM)](https://www.wikiwand.com/en/Support_vector_machine)
- [Random note on k-Nearest Neighbor lookups on embeddings](https://twitter.com/karpathy/status/1647025230546886658)
