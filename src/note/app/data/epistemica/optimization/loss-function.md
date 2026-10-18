# Loss Function


> A **loss function** is a mathematical function that **quantifies the cost of prediction errors** made by a model. It maps the discrepancy between predicted values ($\hat{y}$) and true values ($y$) to a **real number** that the learning algorithm tries to **minimize**.
> 

$\mathcal{L}(y, \hat{y}) \in \mathbb{R}_{\ge 0}$

## Terminology

| Term | Scope |
| --- | --- |
| **Loss function** | Error on **one sample** |
| **Cost function** | **Aggregate loss** (e.g. sum or mean over samples) |
| **Objective function** | Loss + regularization or constraints |

## 🧱 **Formal Definition**

Let:

- $y$ be the true value
- $\hat{y} = f(x; \theta)$ be the predicted value from the model
- $\mathcal{L}(y, \hat{y})$ be the loss function

Then training seeks to minimize: $\min_{\theta} \sum_{i=1}^n \mathcal{L}(y_i, \hat{y}_i)$

or, in expectation form:  $\min_{\theta} \mathbb{E}_{(x, y) \sim \mathcal{D}}[\mathcal{L}(y, f(x; \theta))]$

## 🧠 **Purpose of a Loss Function**

- Guides the learning algorithm.
- Measures model performance during training.
- Drives gradient-based optimization (e.g., backpropagation).
- Can encode asymmetries, penalties, or domain-specific priorities.

## 📋 **Loss Functions Table**

> 

### 📋 Loss Functions Table

| **Category** | **Loss Function** | **Description** |
| --- | --- | --- |
| **Regression** | Mean Squared Error (MSE) | Penalizes squared differences between actual and predicted values. |
|  | Mean Absolute Error (MAE) | Penalizes absolute differences; more robust to outliers than MSE. |
|  | Huber Loss | Quadratic for small errors, linear for large ones; combines MSE & MAE. |
|  | Log-Cosh Loss | Smooth version of MAE using logarithm of hyperbolic cosine. |
|  | Quantile Loss | Asymmetric loss for quantile regression; penalizes over- or underestimation. |
|  | Tukey’s Biweight Loss | Further limits the influence of outliers by bounding large errors. |
| **Classification** | Binary Cross-Entropy | Measures performance of a binary classifier using log loss. |
|  | Categorical Cross-Entropy | Generalization of BCE for multi-class problems with one-hot targets. |
|  | Sparse Categorical Cross-Entropy | Like above but assumes integer class labels. |
|  | Hinge Loss | Used in SVMs; penalizes predictions that fall inside the margin. |
|  | Squared Hinge Loss | Variant of hinge loss with squared penalty. |
|  | Focal Loss | Down-weights easy examples, focuses training on hard-to-classify cases. |
|  | Kullback–Leibler Divergence | Measures difference between predicted and target probability distributions. |
| **Ranking / Structured** | Pairwise Ranking Loss | Penalizes incorrect ordering between pairs of items (e.g., in recommendations). |
|  | Triplet Loss | Encourages distance between anchor-positive and anchor-negative to be maximized. |
|  | Contrastive Loss | Encourages similar examples to be close, dissimilar ones far apart. |
| **Reconstruction / Unsupervised** | Mean Squared Error (Autoencoders) | Measures how well an autoencoder reconstructs input data. |
|  | Negative Log Likelihood (NLL) | Often used in probabilistic generative models (e.g., VAEs, language models). |
| **Reinforcement Learning** | Temporal Difference Loss | Difference between predicted and actual returns in TD learning. |
|  | Policy Gradient Loss | Optimizes parameters of a stochastic policy to increase expected return. |
|  | Actor-Critic Loss | Combines policy loss and value loss in actor-critic algorithms. |

## Common Alternative Names

| Term | Context |
| --- | --- |
| **Cost Function** | General optimization or engineering |
| **Error Function** | Emphasis on prediction error |
| **Objective Function** | General optimization, especially constrained |
| **Risk Function** | Statistical decision theory |
| **Energy Function** | Physics-inspired models (e.g. Hopfield networks) |
| **Penalty Function** | When highlighting constraints or regularization |
| **Score Function** | In some ML and statistical settings |
| **Fitness Function** | Evolutionary algorithms / genetic programming |
| **Utility Loss** | Economics / decision theory (negative utility) |
| **Divergence Measure** | Information theory (e.g., KL divergence) |

## References

- https://en.wikipedia.org/wiki/Loss_function
