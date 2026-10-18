---
tags: [learning-system, trainable-computational-system]
---

# Decision Tree

 : Random Forest (Random%20Forest%2008e4703f17bc43b6a7530a2c25d5106b.md)

> In this note, we explore the decision tree class of systems.
> 

> **Note:** This is a discriminative system—it does not learn the deep ontology or underlying dynamics of the domain. Instead, it implements a simple input–output mapping, capturing no latent or dynamical structure.
> 

## Introduction

> What is a decision tree?  A decision tree is a class of *trainable computational systems* that implement piecewise-constant (or piecewise-linear, in some variants) decision functions by recursively partitioning an input feature space using conditional tests.
> 

### How does a decision tree differ from a LLM?

> LLM do tries to represent - and simulate the domain - but the  `Decision Tree` is a much more simpler system …
> 

> An LLM tries to construct a high-dimensional, distributed representation that can approximate the **generative structure of a domain** and support complex state evolution, while a decision tree merely implements a fixed set of hierarchical decision rules that map inputs to outputs without any notion of domain simulation.
> 

> LLMs rely on **rich internal state representations** and learned transition dynamics; decision trees rely on explicit, shallow symbolic structure with no internal dynamics beyond rule traversal.
> 

### Technique Space Structure

> **Which techniques constitute the practical ecosystem of decision trees?**
> 

| **Technique Type** | **Description** | **Instance(s)** |
| --- | --- | --- |
| Tree Induction Algorithm | Core procedure for constructing the tree via recursive partitioning of the feature space. | ID3, C4.5, CART |
| Split Criterion | Objective function used to select feature thresholds at each node. | Information Gain, Gain Ratio, Gini Impurity, Chi-square |
| Feature Thresholding | Methods for handling continuous and categorical variables during splits. | Binary thresholding, Multiway splits |
| Pruning Strategy | Techniques to control overfitting by simplifying tree structure post- or pre-training. | Cost-Complexity Pruning, Reduced Error Pruning, Early Stopping |
| Handling Missing Values | Mechanisms for robustness to incomplete data during training and inference. | Surrogate Splits, Probabilistic Routing |
| Tree Variant | Structural modifications that alter representational capacity or inductive bias. | Oblique Trees, Soft Decision Trees |
| Ensemble Construction | Techniques that combine multiple trees to improve generalization. | Random Forest, Bagging, Extremely Randomized Trees |
| Boosting Framework | Sequential reweighting strategies that turn weak trees into strong predictors. | AdaBoost, Gradient Boosting, XGBoost |
| Regularization Technique | Constraints imposed on tree growth to manage complexity. | Max Depth, Min Samples per Leaf, Min Impurity Decrease |
| Interpretability Method | Techniques for extracting human-understandable explanations from trained trees. | Rule Extraction, Feature Importance |
| Probabilistic Output Calibration | Methods to convert leaf statistics into calibrated probability estimates. | Laplace Smoothing, Platt Scaling |
| Deployment Optimization | Techniques for efficient inference and production use. | Tree Compilation, SIMD Inference, Model Compression |

## Theoretical Foundation

> In this section, we examine the formal principles that underlie decision tree models, including their representational capacity, statistical foundations, and limitations. We focus on how tree structure, split criteria, and training strategies relate to predictive performance, generalization, and function approximation.
> 

### **Bias–Variance Tradeoff**

- How does the bias–variance decomposition inform the design, training, and evaluation of decision trees?
- How do tree depth, pruning, and ensemble methods affect bias and variance?

### **Overfitting and Generalization**

- How can overfitting in decision trees be formally measured?
- Which structural or statistical indicators (e.g., tree depth, leaf purity, validation error) quantify overfitting risk?

### **Function Approximation Capacity**

- To what extent can decision trees approximate arbitrary functions?
- Under what conditions (depth, width, feature discretization) do decision trees approach **universal approximation**?
- How does the number of partitions in the input space relate to approximation accuracy for highly nonlinear functions?

### **Statistical and Information-Theoretic Principles**

- How do split criteria (e.g., Gini, entropy, variance reduction) relate to minimizing prediction error?
- Can these criteria be interpreted in terms of expected risk or information gain?

### **Representational Limitations**

- What are the theoretical limits of decision trees in capturing interactions among features?
- How do axis-aligned versus oblique splits affect the tree’s expressive power?

## Training

> This section covers the system’s representation and the procedures used to train it.
> 

### System Representation

> What is the appropriate representation of the system, and into which primitive structures can a decision tree be reduced?
> 

> A decision tree is fundamentally a **hierarchical decomposition of the input space**, implemented as a tree structure but reducible to simpler, interpretable primitives like rules, Boolean circuits, or functional mappings. Its representational capacity is **explicit and shallow**, unlike generative systems (LLMs) which encode rich latent states and dynamics. Training data encoding, problem complexity, and feature dimensionality directly influence its depth, structure, and ultimately its expressivity.
> 

> A decision tree can be represented at multiple levels, depending on whether we emphasize computation, logic, or data structure:
> 

| Representation Type | Description |
| --- | --- |
| **Tree Data Structure** | The canonical representation: nodes encode feature tests, edges encode outcomes of tests, leaves encode outputs (class labels, regression values, or probability distributions). |
| **Rule Set** | Each root-to-leaf path can be interpreted as an **if–then rule**, providing an explicit logical mapping from input features to output. |
| **Boolean Circuit** | For binary classification, the tree can be reduced to a Boolean circuit, where internal nodes are AND/OR/NOT gates corresponding to splits. |
| **Lookup Table** | For discrete or small feature spaces, the tree’s mapping can be flattened into a table mapping input combinations to output labels. |
| **Functional Representation** | The decision tree can be viewed as a piecewise-constant or piecewise-linear function over the input feature space. Each leaf defines a region of the feature space and the corresponding output. |
| **Linear Constraint with Indicator Variables** | In optimization contexts, each path can be encoded as a set of linear inequalities with binary indicators specifying which leaf is active for a given input. |
| **Probabilistic Representation** | Leaves can store class probabilities, enabling soft outputs or uncertainty estimates. This is especially relevant for ensembles or probabilistic calibration. |

How to represent the training data?

- **Feature encoding**: Continuous variables are often kept as-is (or normalized); categorical variables are typically one-hot encoded or mapped to integers.
- **Labels**: Encoded as discrete categories (classification) or continuous values (regression).
- **Missing values**: Can be represented with a special “NA” marker or imputed; decision trees can handle them via surrogate splits or probabilistic routing.

### Dataset

> How to prepare the dataset? How to prepare the validation dataset?
> 

> Preparing the dataset is a critical step in training decision trees. Unlike generative systems, decision trees rely entirely on **explicit input–output mappings**, so data quality, representation, and partitioning directly determine model performance.
> 

**Which are the preparation techniques or steps?**

| **Phase** | **Step** | **Description** |
| --- | --- | --- |
| Feature Encoding | Continuous features | Retain numeric values; optionally normalize or standardize if feature scales vary significantly. |
|  | Categorical features | Convert to integers, one-hot vectors, or ordinal codes depending on tree implementation requirements. |
|  | Mixed feature types | Most tree algorithms (CART, C4.5) handle mixed types natively, but explicit encoding can improve performance. |
| Label Representation | Classification | Encode discrete target classes (e.g., integers, one-hot vectors for multi-class trees). |
|  | Regression | Use raw numeric values; optionally scale for numeric stability. |
| Handling Missing Values | Placeholder assignment | Assign a marker (e.g., `NA` or `null`) for missing entries. |
|  | Surrogate splits | Use alternate features when primary split feature is missing during training or inference. |
|  | Probabilistic routing | Route missing values based on observed distributions in training data. |
| Data Partitioning | Training set | Used to construct the tree (learn splits and assign leaf outputs). |
|  | Validation set | Optional; used for pre-pruning or hyperparameter tuning to prevent overfitting. |
|  | Test set | Held out for final evaluation to measure generalization performance. |

**How to evaluate the dataset?**

| **Criterion** | **Description** |
| --- | --- |
| **Completeness** | Measures whether the dataset has all necessary features and target labels for training; checks for missing values or incomplete samples. |
| **Consistency** | Checks for contradictory entries, duplicates, or logically inconsistent data points that could mislead tree splits. |
| **Representativeness** | Ensures the dataset adequately covers the input space and target variability; avoids sampling bias or underrepresented regions. |
| **Balance / Class Distribution** | Evaluates the proportion of classes in classification tasks; highly imbalanced datasets may require resampling or weighting. |
| **Feature Relevance** | Measures how informative each feature is for predicting the target, e.g., via correlation, mutual information, or impurity reduction. |
| **Redundancy / Multicollinearity** | Identifies highly correlated or duplicate features that may not add information and could lead to unnecessarily complex trees. |
| **Noise / Outliers** | Detects anomalous or extreme values that can cause overfitting in unpruned trees. |
| **Scalability / Size** | Evaluates whether the dataset size is sufficient to train a tree with desired depth and partitioning resolution. |
| **Distributional Properties** | Checks for skewed or non-uniform distributions in features or target variables that may affect split quality. |
| **Data Quality Metrics** | Includes missing value rates, error rates, or data entry reliability scores to assess the overall reliability of the dataset. |
| **Validation / Generalization Check** | Uses cross-validation or holdout sets to ensure the dataset enables robust estimation of predictive performance. |

**Which are the advanced strategies?**

| **Strategy** | **Description** | **Use** |
| --- | --- | --- |
| Cross-Validation | Split dataset into *k* folds; train on *k-1* folds and validate on the remaining fold; repeat for all folds. | Reduces variance in performance estimates, ensures robust evaluation, mitigates overfitting on small datasets. |
| Stratified Sampling | Maintain class proportions in training, validation, and test sets. | Ensures balanced representation of all classes, especially important for imbalanced classification tasks. |
| Bootstrapping | Sample data with replacement to create multiple training sets. | Used in ensemble methods (e.g., Random Forests) to reduce variance and improve generalization. |
| Feature Engineering | Create new features via transformations (polynomial terms, logarithms, interactions). | Allows trees to capture complex or nonlinear relationships with fewer splits. |
| Feature Selection | Identify and retain only the most informative features based on impurity reduction, correlation, or statistical tests. | Reduces overfitting risk, decreases tree complexity, improves interpretability. |
| Data Augmentation | Generate synthetic samples or perturb existing data to expand dataset. | Improves generalization when dataset is small; commonly used for regression or imbalanced datasets. |
| Pre-Pruning (Early Stopping) | Halt tree growth based on criteria like max depth, min samples per leaf, or minimum impurity decrease. | Controls overfitting during training, reduces tree complexity. |
| Post-Pruning | Grow a full tree and then remove branches that minimally improve validation performance. | Improves generalization, simplifies tree structure, reduces sensitivity to noise. |
| Ensemble Techniques | Combine multiple trees via bagging, boosting, or random feature selection. | Increases predictive performance, reduces variance, stabilizes predictions. |
| Probabilistic Calibration | Adjust leaf probabilities using methods like Laplace smoothing or Platt scaling. | Produces well-calibrated probability estimates for classification tasks. |
| Hyperparameter Optimization | Systematically search for optimal tree parameters (e.g., depth, min samples, split criterion) using grid search, random search, or Bayesian optimization. | Maximizes predictive performance and generalization. |
| Out-of-Bag Evaluation | Evaluate bagged trees using samples not included in bootstrap. | Provides an internal estimate of generalization error without a separate validation set. |

### Evolution (Optimization)

**How  to train (evolve the system)? Which are the algorithms?**

A decision tree evolves by recursively partitioning the input space to reduce uncertainty in the output variable. The system does **not learn domain dynamics or latent representations**, but optimizes a **local decision criterion** at each node to produce a mapping that approximates the target function.

- **Classification trees:** Minimize impurity measures at each split (e.g., Gini Impurity, Entropy/Information Gain).
- **Regression trees:** Minimize variance or squared error within each leaf.

The optimization is **greedy and local**: each node chooses the split that maximally reduces the objective, without global foresight.

**Which is the core training algorithm?**

The training process typically involves the following steps:

1. **Start at the root:** Consider all training data.
2. **Select best split:** Evaluate candidate splits across features using a split criterion.
3. **Partition data:** Divide the dataset according to the chosen split.
4. **Recursion:** Repeat steps 2–3 on each child node until a stopping condition is met.
5. **Leaf assignment:** Assign outputs (class labels, regression values, probabilities) to leaf nodes.
6. **Stopping conditions** (prevent overgrowth and overfitting):
    - Maximum tree depth reached.
    - Minimum number of samples per leaf.
    - Minimum reduction in impurity achieved.
    - All samples at a node have the same output.

**Which are the post-training improvements?**

- **Pre-pruning:** Halt growth early using stopping conditions to reduce complexity.
- **Post-pruning:** Grow a full tree first and then remove branches that contribute minimal improvement on validation data.
    - **Cost-Complexity Pruning (CART):** Remove branches that minimally reduce classification/regression error relative to a complexity penalty.
    - **Reduced Error Pruning:** Remove nodes if validation error does not increase.

Pruning improves generalization and reduces sensitivity to noise, maintaining a balance between bias and variance.

**Which are the specific training algorithms?**

| **Algorithm** | **Description** | **Assessment** |
| --- | --- | --- |
| **ID3 (Iterative Dichotomiser 3)** | Constructs a tree using a top-down, greedy approach. Uses **Information Gain** as the split criterion. Handles categorical features naturally. | Pros: Simple, interpretable, fast on small datasets. Cons: Prone to overfitting, does not handle continuous features natively, biased toward features with many categories. |
| **C4.5** | Extension of ID3. Supports **continuous features**, missing values, and uses **Gain Ratio** to normalize splits. Can perform **post-pruning**. | Pros: More robust than ID3, handles mixed data types, supports pruning. Cons: Slightly more complex, can still overfit on noisy data. |
| **CART (Classification and Regression Trees)** | Constructs **binary trees** for both classification and regression. Uses **Gini Impurity** for classification and **variance reduction** for regression. Supports **cost-complexity pruning**. | Pros: Handles both tasks, widely used, supports pruning and regression. Cons: Binary splits may produce deeper trees, may be sensitive to outliers. |
| **CHAID (Chi-squared Automatic Interaction Detection)** | Uses **Chi-square statistics** for categorical splits. Can produce multi-way splits. Focuses on finding significant associations between features and the target. | Pros: Produces statistically robust splits, multiway branching reduces depth. Cons: Limited to categorical targets or discretized features; less common in modern ML pipelines. |
| **Oblique Decision Trees** | Splits are **linear combinations of features**, not axis-aligned. Can capture complex decision boundaries with fewer nodes. | Pros: Can model non-axis-aligned boundaries efficiently. Cons: More computationally intensive, less interpretable. |
| **Random Forest Training (Bagged Trees)** | Trains multiple trees on **bootstrapped samples** with random feature selection at each split. Predictions are aggregated by majority vote or averaging. | Pros: Reduces variance, robust to overfitting, handles large feature spaces. Cons: Individual trees lose interpretability; larger memory footprint. |
| **Gradient Boosted Trees (e.g., XGBoost, LightGBM)** | Trains trees sequentially, each tree corrects residuals of the previous ensemble. Optimizes differentiable loss functions. | Pros: High predictive performance, handles missing data and heterogeneous features, widely used in competitions. Cons: Sensitive to hyperparameters, longer training times, less interpretable. |
| **Extremely Randomized Trees (ExtraTrees)** | Randomized splitting thresholds and feature selection. Trees trained on full dataset without bootstrapping. | Pros: Fast training, reduced variance, robust to overfitting. Cons: May be less accurate than carefully tuned ensembles; randomness can increase bias. |

**How to monitor the training of the system?**

Decision tree evolution can be monitored using metrics and diagnostics:

- **Training vs validation error:** Tracks overfitting and underfitting.
- **Tree depth and size:** Measures model complexity.
- **Split statistics:** Observe impurity reduction at each split to identify informative features.
- **Leaf statistics:** Check class distribution or regression variance in leaves.
- **Feature importance:** Derived from cumulative reduction in impurity across splits involving each feature.

**Which are the computational complexity of training?**

- Training is **O(n log n)** for axis-aligned splits on continuous features, with n = number of samples.
- Memory usage grows with depth and number of nodes.
- Efficient implementations use **sorted feature arrays** and **precomputed statistics** for fast split evaluation.

### Evaluation

> How to evaluate the system? Decision trees are evaluated both in terms of **predictive performance** and **structural properties**, depending on the task (classification or regression) and the intended use (standalone tree vs. ensemble).
> 

**Which are the performance metrics?**

| **Category** | **Metric** | **Description** | **Note** |
| --- | --- | --- | --- |
| **Classification** | Accuracy | Fraction of correctly predicted labels over all samples. | Simple, intuitive; may be misleading with imbalanced classes. |
|  | Precision | Proportion of true positives among predicted positives: TP / (TP + FP). | Important when false positives are costly. |
|  | Recall (Sensitivity) | Proportion of true positives among actual positives: TP / (TP + FN). | Important when false negatives are costly. |
|  | F1-Score | Harmonic mean of precision and recall: 2 × (Precision × Recall) / (Precision + Recall). | Balances precision and recall; useful for imbalanced datasets. |
|  | ROC-AUC | Area under the Receiver Operating Characteristic curve; measures class separability. | Threshold-independent; useful for probabilistic outputs. |
|  | Log-Loss / Cross-Entropy | Penalizes confident but incorrect predictions; measures quality of probability estimates. | Lower values indicate better calibrated probability predictions. |
|  | Matthews Correlation Coefficient (MCC) | Correlation between observed and predicted classifications. | Robust for imbalanced datasets. |
| **Regression** | Mean Squared Error (MSE) | Average squared difference between predicted and true values. | Sensitive to outliers; common in training objective. |
|  | Root Mean Squared Error (RMSE) | Square root of MSE; same units as the target variable. | Easier to interpret than MSE; highlights large errors. |
|  | Mean Absolute Error (MAE) | Average absolute difference between predicted and true values. | Less sensitive to outliers than MSE; robust metric. |
|  | R² (Coefficient of Determination) | Fraction of variance explained by the model: 1 − (SS_res / SS_tot). | Indicates goodness-of-fit; 1 = perfect prediction, 0 = mean prediction. |
|  | Adjusted R² | R² adjusted for number of predictors; penalizes overly complex models. | Useful when comparing models with different numbers of features. |
|  | Mean Absolute Percentage Error (MAPE) | Average absolute percentage error between predictions and true values. | Normalized metric; sensitive to zero targets. |
| **Probabilistic (Calibration)** | Brier Score | Mean squared error between predicted probabilities and true outcomes. | Measures calibration of probabilistic predictions; lower is better. |
|  | Expected Calibration Error (ECE) | Quantifies difference between predicted probabilities and actual outcomes in bins. | Evaluates how well probabi |

Which are the others evaluation criteria?

| **Category** | **Criteria** | **Description** | **Note** |
| --- | --- | --- | --- |
| **Structural Evaluation** | Tree Depth | Measures how many levels the tree has from root to deepest leaf. | Deeper trees may overfit; shallower trees may underfit. |
|  | Number of Nodes / Leaves | Counts the total nodes or terminal leaves in the tree. | Too many nodes indicate high complexity and potential overfitting. |
|  | Feature Importance Distribution | Distribution of how much each feature contributes to splits. | Helps identify which features the model relies on most. |
|  | Leaf Purity / Variance | Homogeneity of the target values within leaves. | Low impurity indicates effective splits; high variance may signal poor partitioning. |
| **Cross-Validation** | K-Fold Cross-Validation | Split data into k subsets; train on k-1 folds and validate on the remaining fold. | Reduces variance in performance estimates. |
|  | Leave-One-Out / Stratified Sampling | Each sample (or stratified group) is used as a validation set once. | Useful for small datasets or imbalanced classes. |
| **Overfitting & Generalization** | Training vs. Validation Performance | Compare model performance on training and validation/test sets. | Large discrepancy → overfitting; poor performance on both → underfitting. |
|  | Pruning & Ensemble Techniques | Apply post-pruning or train ensembles to improve generalization. | Helps reduce variance, control tree complexity, and improve stability. |
| **Ensemble-Specific Evaluation** | Aggregated Metrics | Combine predictions from all trees via majority vote (classification) or averaging (regression). | Provides overall ensemble performance. |
|  | Out-of-Bag (OOB) Error | Evaluate bagged trees using samples not included in the bootstrap. | Avoids need for separate validation set; estimates generalization error. |
|  | Gain in Impurity / Feature Importance | Sum of impurity reduction contributed by each feature or tree. | Measures contribution of features and splits to predictive power. |
| **Interpretability Assessment** | Rule Extraction / Leaf Inspection | Examine paths from root to leaf as human-readable rules. | Assesses whether model reasoning is understandable. |
|  | Consistency with Domain Knowledge | Check if splits and decision paths align with expected patterns. | Validates model behavior against expert knowledge. |

## Inference

> In this section, we examine the system’s representational capacity and its practical usage.
> 

### Which task can the system do?

- Decision trees are **predictive systems**: they map input features to output labels or values.
- They can perform:
    - **Classification** (discrete outputs, e.g., spam/not spam, disease/no disease).
    - **Regression** (continuous outputs, e.g., house prices, temperature predictions).
    - **Probability estimation** (by counting outcomes in leaves and optionally calibrating).
- They **cannot simulate dynamics** or generate novel trajectories beyond learned input–output patterns.

### What does the system can represent?

- A decision tree represents the domain as a **hierarchical partitioning of the input space**, where each region corresponds to a leaf output.
- Internally, the system does **not create abstract latent representations**: each node only stores the split criterion, and each leaf stores the output or a probability distribution.
- Representational capacity is **shallow and explicit**:
    - Simple rules for discrete decisions.
    - Piecewise-constant or piecewise-linear mappings for regression tasks.
- Complex input–output relationships require **deep or wide trees**, leading to many partitions of the input space.

### How does the system represents the domain?

- The domain is captured **implicitly**, through observed correlations between input features and outputs, rather than via an explicit model of causality or system dynamics.
- Intermediate nodes represent **conditional decisions**—partial knowledge about the domain conditioned on previous splits.
- No global, generative, or hierarchical latent structure is learned: the tree’s “knowledge” is **purely local** to paths from root to leaves.

### Does the system created initial - and intermediary representations?

> There is not internal representation - and even output representation the leaft is just -  a tag - or value computed - not a derived representation - or evolved one.
> 
- **Initial representation**: Raw features from the training data, possibly preprocessed (normalized, one-hot encoded).
- **Intermediate representation**: Internal nodes encode the partitioning logic (feature + threshold).
- **Final representation**: Leaves encode output labels, values, or probabilities.
- These representations are **explicit, interpretable, and discrete**, unlike the distributed embeddings of generative models.
- The system **does not evolve internal states or latent variables** beyond the structural encoding of splits and leaf outputs.

## Evaluation

> In this section, we address the evaluation of the decision tree class of systems as a whole.
> 

### Which are the application of the system?

| **Category** | **Use** | **Description** |
| --- | --- | --- |
| **Classification** | Binary/Multiclass Prediction | Assign samples to discrete classes, e.g., spam detection, disease diagnosis, customer segmentation. |
| **Regression** | Continuous Output Prediction | Predict numerical values, e.g., house prices, sales forecasting, sensor measurements. |
| **Probability Estimation** | Risk/Probability Modeling | Estimate likelihoods of outcomes using leaf statistics and optional calibration (Laplace, Platt scaling). |
| **Feature Selection / Importance** | Explainability & Insights | Identify which features contribute most to predictions via impurity reduction or split frequency. |
| **Decision Support Systems** | Business / Operational Rules | Provide interpretable “if–then” decision rules for operational guidance in finance, medicine, or logistics. |
| **Ensemble Learning** | Enhanced Predictive Performance | Used as base learners in Random Forests, Gradient Boosted Trees, ExtraTrees to improve accuracy and robustness. |
| **Anomaly / Outlier Detection** | Identify Rare Events | Leaves with very few samples or unusual outcomes can indicate anomalies. |

### Which are the limits of the system?

| **Category** | **Limit** | **Description** |
| --- | --- | --- |
| **Representational Capacity** | Poor at capturing complex patterns | Struggle with highly nonlinear or high-dimensional relationships without deep/wide trees. |
| **Overfitting** | Sensitive to noise | Trees can perfectly memorize training data if unpruned, leading to poor generalization. |
| **Instability** | High variance | Small changes in training data can produce very different trees; mitigated with ensembles. |
| **Lack of Generativity** | Cannot simulate domain | Decision trees are purely discriminative; they do not model underlying dynamics or latent structures. |
| **Limited Extrapolation** | Cannot predict beyond training range | Leaf outputs correspond only to observed or partitioned feature ranges; no interpolation beyond regions. |
| **Interpretability vs Depth** | Deep trees lose clarity | Very large trees become harder to interpret, reducing usefulness for decision support. |
| **Bias Toward Certain Features** | Split criterion bias | Criteria like Information Gain can favor features with more categories, potentially skewing model. |
| **Handling Complex Feature Interactions** | Limited without oblique splits | Axis-aligned trees struggle to represent oblique or highly correlated feature interactions efficiently. |

## Related Method(s)

> What are the related methods or extensions?
> 

| **Method** | **Description** | **Relation to Decision Trees** |
| --- | --- | --- |
| **Random Forests** | Ensemble of decision trees trained on bootstrapped samples with random feature selection. Predictions are aggregated (majority vote for classification, averaging for regression). | Reduces variance of individual trees; maintains local partitioning structure but introduces ensemble-level stability and robustness. |
| **Gradient Boosted Trees (GBTs)** | Sequentially trained trees where each tree corrects the residual errors of the previous ensemble. Optimizes a differentiable loss function. | Extends trees into a stage-wise additive model; increases predictive accuracy and allows more complex function approximation while still using hierarchical partitioning at each stage. |
| **Extra Trees (Extremely Randomized Trees)** | Trees built with randomized splits and thresholds, often without bootstrapping. | Variation of tree construction to reduce variance and increase computational efficiency; emphasizes stochasticity in split selection. |
| **Oblique Decision Trees** | Trees that split along **linear combinations of features** rather than axis-aligned splits. | Increases expressive power to capture correlated or oblique feature interactions; requires optimization at each node for hyperplane splits. |
| **Soft Decision Trees / Probabilistic Trees** | Nodes use probabilistic routing (soft splits) instead of hard binary splits. | Introduces smoothness in the mapping; allows differentiable training and integration with gradient-based methods. |
| **Model Trees (e.g., M5)** | Regression trees with linear models or other parametric functions at leaves instead of constants. | Enhances local function approximation capacity; merges tree-based partitioning with parametric modeling. |
| **Rule Extraction / Rule Sets** | Convert decision trees (or ensembles) into explicit rules for interpretability. | Preserves decision logic but flattens hierarchical structure; useful for explainable AI applications. |
| **Boosted Oblique Trees** | Combination of gradient boosting and oblique splits. | Integrates high expressivity (oblique splits) with additive residual correction (boosting); more powerful function approximator than standard trees. |
| **Hybrid Models (Tree + Neural Network)** | Trees used for feature partitioning, neural networks used for local function approximation within leaves. | Combines hierarchical partitioning of input space with generative or latent-state modeling; bridges discriminative and latent representations. |
| **Extensible Decision Trees for Time Series / Sequential Data** | Trees adapted to sequential or temporal features using lagged inputs or recurrent splits. | Extends standard trees to approximate dynamical input-output mappings; still lacks full generative simulation capability. |

## QA

- Do decision trees constitute a foundational computational primitive of intelligence, or are they emergent algorithmic structures tailored to specific decision problems?
- Can a decision tree be collapsed into a single level?
- What is the relationship between the structure of the problem and the depth of the tree?
- How many partitions of the input space (i.e., decision branches) does a decision tree need in order to accurately learn a highly nonlinear function?
- How to visualize a decision tree?

## References

- https://en.wikipedia.org/wiki/Decision_tree
- https://mljar.com/supertree/
- https://mljar.com/blog/visualize-sklearn-tree/
- https://news.ycombinator.com/item?id=16932077
- https://news.ycombinator.com/item?id=18079479
- https://news.ycombinator.com/item?id=7957801
- https://mlu-explain.github.io/decision-tree/
- Quinlan, J. Ross. "Induction of decision trees." Machine learning 1.1 (1986): 81-106.
- Leo Breiman, Jerome H. Friedman, Richard A. Olshen, and Charles J. Stone — Classification and Regression Trees (CART) (1984)
- J. R. Quinlan — Induction of Decision Trees (ID3), Machine Learning 1(1):81–106 (1986)
- J. R. Quinlan — C4.5: Programs for Machine Learning (1993)
- Loh, Wei‐Yin. "Fifty years of classification and regression trees." *International Statistical Review* 82.3 (2014): 329-348.
- https://arxiv.org/abs/2210.05189
- https://github.com/dbremont/algorithms/tree/main/om
- [A Set of Mental Models about ML](https://app.notion.com/p/A-Set-of-Mental-Models-about-ML-2e9c0f5171ec8038ab1de2619cfe37fd?pvs=21)
- https://www.kaggle.com/datasets?tags=13417-Decision+Tree
- https://github.com/dbremont/algorithms/tree/main/om/ds
