---
tags: [learning-system, technique]
---

# Ensemble Learning

> Aka.  Ensemble Method
> 

> An **ensemble method** in machine learning and statistical learning theory refers to a class of **meta-algorithms** that **construct and combine multiple base models** (also called **learners** or **estimators**), typically of the same or different types, in order to produce a **composite model** whose **predictive performance surpasses that of any individual base model**.
> 

> Ensemble methods exploit the principle that **a group of weak learners**, if sufficiently diverse and properly aggregated, can form a **strong learner**, as formalized in **PAC-learning theory** and **bias-variance decomposition** frameworks.
> 

> Combining multiple models to enhance overall predictive performance and robustness.
> 

## Goals

- Improve predictive accuracy and robustness.
- Stabilize model predictions under small perturbations of the data.
- Achieve better bias-variance trade-off.
- Leverage model diversity and complementary errors.

## Taxonomy

| **Category (with Tags)** | **Method** | **Description** |
| --- | --- | --- |
| **Averaging-Based 🔁🧮 (Variance Reduction)** | **Bagging** | Trains multiple models on bootstrap samples and averages predictions to reduce variance. |
|  | **Random Forest** | Ensemble of decision trees using bagging and random feature selection to decorrelate models. |
|  | **Extra Trees** | Uses extreme randomization in node splitting for faster and more diverse trees. |
| **Boosting-Based 🔁📈 (Bias Reduction, Sequential Learning)** | **AdaBoost** | Sequentially focuses on misclassified instances by adjusting weights. |
|  | **Gradient Boosting** | Builds additive models to minimize a loss function using residuals. |
|  | **LogitBoost** | Boosting adapted to logistic regression; good for classification. |
| **Stacking-Based 🧠🔀 (Stability, Meta-Learning)** | **Stacking** | Combines base models by training a meta-model on their outputs. |
|  | **Blending** | Variant of stacking using a hold-out validation set instead of full cross-validation. |
| **Voting-Based 🗳️🧮 (Stability, Simple Aggregation)** | **Hard Voting** | Predicts the most common class label across models. |
|  | **Soft Voting** | Averages predicted probabilities and selects the most probable class. |
| **Bayesian Methods 🧠📊 (Uncertainty, Probabilistic)** | **Bayesian Model Averaging** | Weights model predictions by posterior probabilities to account for model uncertainty. |
| **Hybrid Methods 🧬⚙️ (Advanced Combinations)** | **Bootstrap + Boosting** | Mixes resampling and sequential learning for robust ensembles. |
|  | **Bayesian Boosting** | Introduces Bayesian priors and uncertainty modeling into boosting frameworks. |

## References

- [Ensemble (mathematical physics)](https://en.wikipedia.org/wiki/Ensemble_(mathematical_physics))
- https://en.wikipedia.org/wiki/Ensemble_learning
