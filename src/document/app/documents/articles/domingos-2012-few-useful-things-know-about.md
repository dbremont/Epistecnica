---
tags: [ml, physical]
---

# Domingos, P. (2012). A few useful things to know about machine learning. Communications of the ACM, 55(10), 78–87.


```jsx
@article{domingos2012few,
  title={A few useful things to know about machine learning},
  author={Domingos, Pedro},
  journal={Communications of the ACM},
  volume={55},
  number={10},
  pages={78--87},
  year={2012},
  publisher={ACM New York, NY, USA}
}
```

## Notes

---

> Note: Great document.
> 

> **Common Wisdom** needed to excel in machine learning.
> 

> **Learning Efficiency:** Turns small input knowledge into a large amount of output knowledge.
> 

> A key criterion for **choosing a representation** is which kinds of knowledge can be easily expressed in it.
> 

> **Inductive Bias**: …
> 

> All **learning works** basically by **grouping** similar data in the **same class**.
> 

> Representation Theory: …
> 

> Learnable Theory: …
> 

## Index

## Abstract

> **ML Systems** automatically “learn”  “programs” from data. **ML** has been used in web search, spam filters, recommender systems, ad placement, credit scoring,  fraud detection, stock trading,  drug design, and many more.
> 

## Machine Learning Family Model

> …
> 

| **Model Family** | **Instances** | **Idea** | **Notes** |
| --- | --- | --- | --- |
| **Probabilistic Models** | Naive Bayes, Logistic Regression | Predict probability distributions over classes. | Assumes feature independence (NB) |
| **Geometric Models** | Support Vector Machines (SVM), Perceptron | Learn decision boundaries in the input space. | Margin maximization (SVM) |
| **Tree-based Models** | Decision Trees, Random Forests, Gradient Boosted Trees (XGBoost) | Make decisions by asking a series of yes/no questions. | Handle categorical and numerical features |
| **Neural Network Models** | Feedforward Neural Networks, CNNs, Transformers | Deep layered representations of data. | Highly flexible, can approximate any function |
| **Instance-based Models** | k-Nearest Neighbors (k-NN) | Store all training data and classify based on similarity. | Memory intensive; lazy learning |
| **Ensemble Models** | Bagging, Boosting, Stacking (e.g., Random Forest, AdaBoost) | Combine multiple models to improve accuracy. | Reduces bias and/or variance |
| **Bayesian Models** | Bayesian Networks, Gaussian Processes | Model uncertainty explicitly with full distributions. | Requires heavy computation for large data |
| **Graph-based Models** | Graph Neural Networks (GNNs), Label Propagation | Model data with graph structure. | Useful for network-structured data |
| **Rule-based Models** | RuleFit, RIPPER, Decision Lists | Learn interpretable "if-then" rules. | Often more interpretable |
| **Evolutionary Models** | Genetic Algorithms, Genetic Programming | Use natural selection concepts to evolve classifiers. | Good for optimization and feature discovery |
| **Symbolic Models** | Inductive Logic Programming (ILP) | Learn logical programs or symbolic relationships. | Good for structured reasoning |

## Machine Learning Strategy

> …
> 

| **Learning Strategy** | **Description** |
| --- | --- |
| **Supervised Learning** | Trained on fully labeled data. |
| **Semi-supervised Learning** | Trained on a small labeled set + large unlabeled set. |
| **Self-supervised Learning** | Learns to generate labels from raw data; no human labeling needed. |
| **Unsupervised Learning** | No labels at all; find structure in data (e.g., clustering, density estimation). |
| **Few-shot Learning** | Learns from very few examples per class. |
| **Zero-shot Learning** | Learns to generalize to unseen classes without any labeled example. |
| **One-shot Learning** | Learns to recognize a new class from exactly one example. |
| **Active Learning** | The model can *ask* for labels on the most informative examples to optimize learning. |
| **Online Learning** | Learns continuously as new data arrives (rather than all at once). |
| **Reinforcement Learning (RL)** | Learns by interacting with an environment and receiving rewards or penalties. |
| **Curriculum Learning** | Data is presented in a meaningful order (easy → hard) to improve training efficiency. |
| **Meta-learning ("Learning to Learn")** | Learns how to quickly adapt to new tasks or datasets. |

## Machine Learning System

> Learning  = Representation + Evaluation + Optimization.
> 

> Representation here refers to the system - learning.
> 

### Classifier

> A **classifier** is a function $\mathcal{X} \rightarrow \mathcal{Y}$ that maps input instances from a feature space $\mathcal{X} \subseteq \mathbb{R}^d$  to a discrete label space $\mathcal{Y} = \{y_1, y_2, \dots, y_k\}$, typically learned from a labeled dataset  $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^n$ via a training procedure that minimizes a loss function $\mathcal{L}(f(x), y)$ subject to regularization constraints and capacity bounds of the hypothesis class $\mathcal{H} \ni f$.
> 

### **Representation**

- **Hypothesis:** A **Classifier** must be represented in some formal language that a computer can handle.
- **Hypothesis Space: Choosing the classifier representation** also determines the hypothesis space of learnable classifiers, since classifiers are parameterized models.

### **Evaluation**

- An objective function, or scoring function, quantitatively evaluates classifier performance (usefulness - correction) and guides the selection among competing models based on predefined optimization criteria.

### **Optimization**

- A **method** to search and move in the **Hypothesis Space**.

## Generalization

> It’s **generalization** that counts.
> 

> The goal of **ML** is that models generalized that it performs well outside the training or testing datasets.
> 

> **Note:** This implies that a local optimum in the loss-parameter space may perform better than the global optimum.
> 

Techniques:

- Cross-validation
- Test-training split

## Data

> Data Alone is Not Enough.
> 

> Note: Remember, our goal is to somehow model the data generation process.
> 

> Deep Formulations Problems:  How to know which are the classes?
> 

> Every learner must embody some knowledge or assumptions beyond the data it is given in order to generalize beyond it. This notion was formalized in the “free launch theorems”.
> 

## Overfitting

> Overfitting has many faces.
> 

> **Note:** Overfitting is essentially memorizing the data—encoding everything—which is not the goal of learning. The goal is to compress and encode a process with the minimal amount of effort.
> 

> Is the data that we have **sufficient** to learn a **classifier**?
> 

One way to understand overfitting is by **decomposing generalization** into bias and variance:

- **Bias**: Always learn the same wrong things.
- **Variance**: Learn different wrong things.

Techniques:

- Regularization,
- …

## Dimensionality

> Intuition Fails in High Dimensions
> 

> **Original Formulation**:  Bellman - Algorithms that works well in low dimensions becomes intractable in higher dimensions.
> 

> **ML Formulation:** Generalizing correctly becomes exponentially harder as the number of dimensions (features) increases; the training set will only cover a tiny fraction of the input space.
> 

> **Note:** This is the reason why ML is needed;  not formal reasoning can handle this.
> 

> Image: We have two variables that correctly determine the output, but we add 98 random variables as noise. Will a learner be able to correctly identify and remove the irrelevant ones? **Many Optimization Algorithms** will fail.
> 

## Theoretical Guarantee

> **Theoretical Guarantees** Are **Not What They Seem**.
> 

> One of the **major developments** of recent decades has been the realization that we can have guarantees on the results of **inductive**, particularly if we are willing to settle for **probabilistic guarantees**.
> 

| **Type of Guarantee** | **Description** | **Key Tools / Concepts** |
| --- | --- | --- |
| **Generalization** | How well a model trained on finite data performs on unseen data | PAC Learning ; VC Dimension; Rademacher Complexity; Uniform Convergence |
| **Convergence** | How fast and reliably the optimization reaches a solution | Gradient Descent;  Convexity & Strong Convexity; Non-convex Analysis; NTK |
| **Consistency** | Whether the algorithm converges to the optimal predictor as data grows | Bayes Consistency;  Universal Consistency (e.g., for k-NN) |
| **No Free Lunch (NFL)** | Without assumptions, no method is universally better than random guessing | NFL Theorems;  Emphasis on Inductive Bias and Domain Assumptions |
| **Robustness** | Sensitivity of the model to input perturbations or adversarial attacks | Lipschitz Bounds; Adversarial Training; Certified Defenses (e.g., Smoothing) |
| **Information-Theoretic** | Bonds based on data complexity and mutual information | Information Bottleneck; MDL Principle; Generalization via Mutual Information |

## Feature

> Feature Engineering is the key !!!
> 

> Note: This seems wrong;  seen, a  learner can learn itself a feature representation.
> 

> Note:  A Lot of time is spent working with the
> 

## Data > Algorithm

> More Data Beats a Clever Algorithm.
> 

Constraints:

- Time, data, algorithms

Learner:

> The word parametric here is rather confusing; the semantics of the words parametric;  did not match the used (denotation).
> 

> Variable size learners can in principle learn any function given sufficient data,  but in practice they may not (the algorithm;  stock in a local optimum); or computational cost.
> 
- Fixed **representation** size (Fixed set of parameters to learn) →  Parametric.
- Variable **representation** size (Variable set of parameters to learn) → Non-Parametric.

## Many Models > One Model

> **Learn** Many Models,  Not Just One.
> 

> **Learn** a set of `models` ; and combine use a method to combine their answer to produce a result; based on their **collective knowledge (aka wisdom of the crowd)**.
> 

| **Category** | **Technique Name** | **Description** |
| --- | --- | --- |
| **Classical Ensembles** | **Bagging** | Train on bootstrapped datasets; reduce variance. |
|  | **Boosting** | Train models sequentially to correct errors. |
|  | **Stacking** | Use a meta-learner to combine base models. |
|  | **Blending** | Similar to stacking, but uses a validation holdout. |
|  | **Hard Voting** | Majority vote from classifiers. |
|  | **Soft Voting** | Average predicted probabilities. |
|  | **Weighted Averaging** | Combine models using performance-based weights. |
| **Bayesian & Probabilistic** | **Bayesian Model Averaging** | Combine models using posterior probabilities. |
|  | **Bayesian Committee Machine** | Bayesian fusion of submodels trained on partitions. |
|  | **Hierarchical Bayesian Ensembles** | Use Bayesian hierarchy over models. |
|  | **Product of Experts** | Combine distributions by multiplication. |
|  | **Mixture of Experts** | Gating model selects the most relevant expert. |
|  | **Gaussian Process Ensembles** | Combine GPs or kernels across models. |
| **Neural Methods** | **Snapshot Ensembles** | Save and ensemble from checkpoints. |
|  | **Deep Ensembles** | Independent training of neural networks. |
|  | **Ensemble Distillation** | Train a student model on the ensemble’s output. |
|  | **MC Dropout** | Approximate ensemble via dropout at inference. |
|  | **Test-Time Augmentation** | Aggregate predictions from augmented inputs. |
| **Rule-Based & Decision Aggregation** | **Majority Voting** | Most common class wins. |
|  | **Weighted Majority Algorithm** | Online weighting of experts. |
|  | **Rule-Based Fusion** | Use logic or thresholds to combine models. |
| **Meta/Online Learning** | **Meta-Ensembles** | Ensemble of ensembles. |
|  | **Online Ensemble Learning** | Update weights/models in real-time. |
|  | **Boosting with Expert Advice** | Sequential training with adversarial feedback. |
| **Geometric/Manifold Approaches** | **Convex Combination on Manifolds** | Combine parameters in geometric space. |
|  | **Wasserstein Barycenters** | Combine distributions via optimal transport. |
| **Cluster/Evolutionary Methods** | **Clustered Ensembles** | Group similar models and ensemble within clusters. |
|  | **Genetic Algorithm-based Selection** | Evolve ensembles via genetic optimization. |
|  | **Evolutionary Ensemble Optimization** | Evolve structure + weights of ensembles. |
| **Sampling/Diversity-based** | **Negative Correlation Learning** | Encourage error diversity during training. |
|  | **Random Subspace Method** | Use subsets of features for each model. |
|  | **Bag of Models/Features** | Ensemble based on varied data views or transformations. |
| **Hybrid/Advanced** | **Neural Architecture Ensembles** | Combine different NN architectures. |
|  | **Heterogeneous Model Fusion** | Mix fundamentally different model types. |
|  | **Self-Ensembling (Consistency Training)** | Encourage consistency under perturbations. |
|  | **Entropy-Regularized Ensemble** | Regularize diversity via entropy. |
| **Theoretical/Decision Theory** | **Game-Theoretic Combination** | Use equilibrium strategies to combine models. |
|  | **Decision-Theoretic Fusion** | Optimize for expected decision loss. |
|  | **PAC-Bayesian Ensembles** | Ensemble with generalization guarantees. |
|  | **Information-Theoretic Fusion** | Fuse models using KL-divergence or MI. |

## Simplicity vs Accuracy

> **Simplicity** does not imply accuracy.
> 

> **Occam’s** razor entities should not be **multiply without necessity**. Choose **simplicity** over **complexity**. This means it's easy to overfit when the model has more parameters. Is the **ensemble a counterexample** to this?
> 

> **Occam’s** razor is a **heuristic** for the **selection of models** and **explanations**;  can we find a better one.
> 

> …
> 

## Representable vs. Learnable

> Representable Does Not Imply Learnable.
> 

> Learnable means; that the algorithm will be the parameter set in the parameter space; sometimes this is not possible because the function has many local optima; and the algorithm is unable to move in the space; to find the global optima.
> 

- Can it be **represented**?
    - What is the data needed to infer a phenomena?
    - …
- Can it be **learnable**?

## Correlation vs Causation

> Correlation does not imply causation.
> 

> Observational Data.
> 

> Experimental Data.
> 

## QA

- What is the **false-discovery** rate?
- What makes a **function learnable**?
- Why do all instances look alike in **higher** dimensions?
    - **Curse of Dimensionality**: As the number of dimensions increases, the volume of space increases exponentially, making it increasingly unlikely that randomly chosen points will be far apart. In practical terms, this means that most points in high-dimensional spaces are nearly equidistant from each other, making differences less noticeable.
    - **Geometric Properties**: In higher dimensions, the geometry of shapes becomes more uniform. For example, spheres and cubes in high dimensions exhibit more symmetry, and the distinction between different points or instances becomes harder to discern due to their uniformity in distances and angles.
    - …
- What is the **manifold hypothesis**?
- Conceptual Understanding
    - How to use the **generalization capacity**, characterized by variance and bias, to choose a representation and optimization method?
    - What is the "No Free Lunch" theorem, and how does it constrain what we can expect from machine learning algorithms?
    - How does the bias-variance tradeoff manifest in practice, and why is it fundamental to model selection?
    - What is meant by "data alone is not enough"? Why is prior knowledge crucial in learning?
    - What role does feature engineering play in model performance, and why is it often more important than the choice of algorithm?
    - What are the implications of overfitting and underfitting in terms of hypothesis space complexity?
- Practical Implications
    - How does regularization help prevent overfitting, and what does it imply about your assumptions?
    - Why is cross-validation a better measure of generalization than training accuracy?
    - Why does “more data usually beats a cleverer algorithm,” and when might that not be true?
    - How does the use of ensembles (e.g., bagging, boosting) reflect a practical workaround to theoretical limitations?
    - What does the paper suggest about debugging a learning algorithm when it doesn’t perform well?
- Meta-Level Thinking
    - Why is it misleading to believe there is a universally best learning algorithm? How does this idea influence experimentation?
    - How can learning be seen as “searching” through hypothesis space, and what are the consequences of this view?
    - What is the paper's stance on the relationship between interpretability and performance in models?
    - How does the concept of "representation" permeate all aspects of machine learning?
    - What are the hidden dangers of automating ML pipelines, as implied by the discussions on overfitting and hyperparameter tuning?
- Philosophical/Reflective
    - If machine learning is all about generalization, what does that imply about the scientific method itself?
    - How should a practitioner balance theoretical understanding with empirical tinkering?
    - What lessons from this paper are most commonly violated in real-world ML projects? Why?
    - How does this paper reframe your understanding of what it means to “learn” from data?
    - Which of the "useful things" discussed changed the way you think about machine learning the most—and why?

## Conclusion

> …
>
