---
tags: [technique]
---

# Regularization

 : Untitled (https://app.notion.com/p/69034ca51a45409880b146cd514b57c6?pvs=21)

> **Regularization** is a technique used in machine learning and statistical modeling to prevent **overfitting** by adding a penalty term to the model’s loss function. This penalty discourages overly complex models by constraining the magnitude of the model parameters (usually the weights).
> 

### 🔍 **Formal Definition**

> Let $\mathcal{L}(\theta)$ be the original loss function (e.g., Mean Squared Error for regression). Regularization modifies it to:  $(θ)\mathcal{L}_{\text{reg}}(\theta) = \mathcal{L}(\theta) + \lambda \cdot \Omega(\theta)$
> 
- $\Omega(\theta)$: regularization term (penalty function)
- $\lambda$: regularization strength (hyperparameter)
- $\theta$: model parameters

## 🧰 **Common Types of Regularization**

| Type | Description |
| --- | --- |
| **L1 (Lasso)** | **Lasso Regression (**Least Absolute Shrinkage and Selection Operator**) (L1 Regularization)** is similar to Ridge Regression but can lead to sparse models with fewer coefficients; some can become precisely zero. |
| **L2 (Ridge)** | Shrinks weights smoothly; discourages large values but doesn't zero them out. |
| **Elastic Net** | Combines L1 and L2 regularization. |

## 🧠 **Purpose of Regularization**

- Prevents **overfitting** by penalizing complexity.
- Helps in **feature selection** (L1).
- Improves **generalization** on unseen data.
- Stabilizes model training.

## References

- [Norm](../mathematical/norm.md)
- [Regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics))
- https://en.wikipedia.org/wiki/Lasso_(statistics)
- https://en.wikipedia.org/wiki/Ridge_regression
