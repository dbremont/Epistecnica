---
tags: [framework]
---

# Computational Learning

 : World-Model (World-Model%202e9c0f5171ec808e9e62c30c4ac05491.md)

> In this note, we will explore Computational Learning - Machine Learning , in essence, the **Theory of Everything (TOE)** of Computation 😊: how to synthesize computational systems—either from data or experience, which is commonly called **Machine Learning**. Here, however, we will refer to it as **Computational System Training**.
> 

> A **trained computational system** is the result of a learning process, where a parameterized structure is synthesized through iterative training guided by an objective (loss) function. Once trained, the model no longer updates and serves solely for inference.
> 

Key Questions

- What is the representation capacity of a **learning model** $L_m$?  How does this model represent problem? Which problems can it represents?
- What kinds of ‘questions’ can the **learning model** $L_m$ answer? How does it **answer** it them?
- What are the practical limitations or constraints of Learning Model $L_m$ in real-world applications?
- What is the structure of the system being taught?
    - What is being taught? What is the skill? What can it do with it?
    - How is it taught?
    - How is it evaluated?
- Which are the main type of Learners?
    - **Discriminative Learners:** Learn direct input–output mappings without modeling underlying dynamics.
    - **Generative Learners:** Learn both the structure and dynamics of the domain, enabling generation and simulation.
    - **World-Model Learners:** Construct internal models of the environment, capturing states, dynamics, and causal relationships to support prediction, planning, and reasoning.
    - **Reinforcement Learners:** Learn policies to maximize cumulative reward through interaction with an environment; can be model-free (direct policy/value learning) or model-based (using a world model for planning).
    - **Meta-Learners (Learning to Learn):** Learn strategies for quickly adapting to new tasks, leveraging prior knowledge for efficient transfer and few-shot learning.
    - **Self-Supervised Learners:** Learn representations from raw, unlabeled data by exploiting inherent structure, enabling robust feature extraction and pretraining for downstream tasks.

![image.png](../assets/note/epistemica/observational/computational-learning/image.png)

![image.png](../assets/note/epistemica/observational/computational-learning/image-1.png)

![image.png](../assets/note/epistemica/observational/computational-learning/image-2.png)

## Meta

> Evaluation Framework.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | ⭐⭐⭐⭐: Strong note. Well-structured, relevant, and insightful, though with minor room for improvement. |
| **Completeness** | ⭐⭐⭐ |
| **Coherence & Structure** | ⭐⭐⭐⭐: Logical framework (TCSEE) and paradigm tree provide good organization, though some transitions could be smoother. |
| **Epistemic Self-Assessment** | ⭐⭐ - Strong theoretical understanding but lacks practical fluency in implementation and real-world applications. |
| **Should I Reorganize This -in My Content Forest?** | Keep as core conceptual framework. Consider creating companion notes for specific sub-topics (optimization, representation learning) to enhance depth. |
| **What’s my study Strategy? Should I Change It?** | Current strategy balances theory and framework well. Consider adding more practical implementation examples and case studies to bridge theoretical concepts with application. |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | ML is the computational approach to automatically learn patterns and make predictions or decisions from data without being explicitly programmed. At its core, it’s about **generalization from examples**. |
| **Evidentia (Evidence) 📊** | Evidence comes from empirical performance on datasets, benchmarks, and tasks. Verification occurs via evaluation metrics (accuracy, F1 score, RMSE), reproducible experiments, ablation studies, and statistical validation. |
| **Telos (Intent) 🎯** | ML aims to create systems that can **adapt, predict, classify, or generate** based on input data. Tools include models, training algorithms, and evaluation frameworks. Outcomes include automation, insights from data, and enhanced decision-making. |
| **Gnosis (Understanding) 🧠** | Mental models of ML should capture **data, model, optimization, and evaluation** as interconnected components. Representations include hierarchical abstraction (from features → model → task), procedural knowledge (training pipelines, hyperparameter tuning), and meta-awareness (bias, overfitting, generalization). Prerequisites: linear algebra, probability, statistics, and computational thinking. |
| **Epignosis (Application) 🛠️** | ML is applied in **vision, language, robotics, medicine, finance, recommendation systems, anomaly detection**, and more. Mastery enables designing novel models, deploying systems at scale, and interpreting results for strategic decisions. |
| **Relatio (Connections) 🔗** | Connects to **statistics, optimization, computer science, neuroscience, cognitive science, control theory, operations research**, and domain-specific knowledge. Interdisciplinary connections include AI ethics, human-computer interaction, and scientific modeling. |
| **Idoneitas (Suitability) 📐** | Effectiveness is measured by task-specific metrics, computational efficiency, generalization capability, robustness, and ability to handle real-world variability. Benchmarks and leaderboards provide comparative suitability. |
| **Limites (Limits) ⛔** | ML struggles with **small data, distribution shifts, interpretability, fairness, and causality**. Performance depends on quality of data, assumptions in models, and appropriateness of tasks. |
| **Contextus (Context) 🌍** | Emerged from statistics and AI research; historical context includes perceptrons, neural networks, kernel methods, and deep learning breakthroughs. Cultural context includes data-driven decision-making, AI adoption in industry, and societal debates on automation. |
| **Dynamis (Evolution) 🌱** | ML evolves toward **self-supervised learning, foundation models, multimodal learning, and reinforcement learning at scale**. Emerging influences: hardware accelerators, massive datasets, algorithmic innovations, and ethical/regulatory frameworks. |
| **Critica (Critique) 🔍** | Criticisms include **opacity (“black box”), bias, overfitting, energy consumption, and ethical risks**. Debates focus on explainability, robustness, and responsible AI practices. |
| **Verbum Usus (Language Use) 🗣️** | “Machine learning” is widely used in technical, business, and popular discourse. Semantic patterns include learning from data, prediction, adaptation; connotations vary between technical rigor and hype. Stylistic use often overlaps with AI and data science narratives. |

### Formulation

- **[**Training**] TCSEE** (**Trainable** **Computational System** → **Evolution** ←→  **Evaluation**): **Random Untrained Template** → Train System.
    - ML = **Representation** (Model) + Evaluation + **Optimization** (Learning Algorithm).
- **[**`Trainable Computational System`  Selection & Training**] MT-CSEE** (`Meta-Trainable Computational System` ←→   Trainable Computational System ←→  Evolution ←→  Evaluation)

### 💡Terminology

> In **this section**, we aim to **untangle** the terminology used in **CL, see the [Re-Designation Mandate](https://app.notion.com/p/Re-Designation-Mandate-261c0f5171ec80378715eb3e81e889cc?pvs=21).**
> 

- **Computational Learning Systems:** Any system (algorithm + representation + update rule) that can learn from data.
- **Machine Learning Models:** Parametric (e.g., neural nets) or non-parametric (e.g., k-NN).
- Parameter: Fixed Parameter (Parametrid); Non Fixed Parameter (Non Parameter).
    - **Parametric Model**: A parametric model is a mathematical model that contains a fixed set of parameters, which are numerical values that determine the model's behavior. These parameters are usually learned from data through a process called parameter estimation. Once the parameters are determined, the model can make predictions or generate new data.
    - **Non-Parametric Model**: Decision trees, k-nearest neighbors, and support vector machines, …
- Model: …
- Model Architecture: …
- Teaching - Learning Strategy: …
- Representation:  Input Representation | Trainable Computational System | Representation Tool
    - **Represent the data** → *Learn a model that captures correlations, patterns, summaries of observed samples.*
    - **Represent the process** → *Learn the underlyingw causal, generative, or mechanistic structure that produced the data.*
    - **Both** → *Understand both the structure of the data and the dynamics that give rise to it.*
- **Bias:**  Bias is the error introduced by approximating a real-world problem, which may be complex, by a simplified model. High bias means the model makes strong assumptions about the data and can underfit, failing to capture the underlying patterns.
- **Variance:**  Variance is the error introduced by the model’s sensitivity to small fluctuations or noise in the training data.  High variance means the model fits the training data very closely but may fail to generalize well to unseen data (overfitting).
- **Discriminative modeling** refers to a class of statistical and machine learning models that **directly model the decision boundary or the conditional probability of the output given the input**.
- **Generative modeling** is a subfield of machine learning focused on **learning the underlying probability distribution of data** to **generate new samples** that resemble the training data. It contrasts with **discriminative modeling** (which learns boundaries between classes) and **representation learning** (which extracts useful features).

### 📜 History

| **Time Period** | **Development** |
| --- | --- |
| **4th Century BCE** | **Aristotle's Syllogism**: Aristotle developed formal logic and the syllogism, laying the groundwork for deductive reasoning, which is fundamental to later computational logic and algorithms. |
| **17th Century** | **Leibniz's Binary System (1679)**: Gottfried Wilhelm Leibniz developed the binary numeral system, foundational for computing. |
| **18th Century** | **Bayes' Theorem (1763)**: Thomas Bayes introduced Bayes' Theorem, which became a cornerstone for probabilistic reasoning and machine learning algorithms. |
| **19th Century** | **Charles Babbage and Ada Lovelace (1830s-1840s)**: Babbage conceptualized the Analytical Engine, and Lovelace wrote the first algorithm, considering the machine’s capability beyond mere calculation. |
| **1950** | **Turing Test**: Alan Turing proposed the Turing Test in his paper "Computing Machinery and Intelligence," which questioned whether machines can think, laying a philosophical foundation for AI. |
| **1956** | **Dartmouth Workshop**: John McCarthy and others coined the term "Artificial Intelligence" during the Dartmouth Conference, marking the birth of AI as a field, closely related to ML. |
| **1957** | **Perceptron Model**: Frank Rosenblatt developed the Perceptron, an early neural network model, marking a significant step toward modern deep learning. |
| **1960s-1970s** | **Early AI and ML Models**: Development of algorithms like decision trees, clustering methods, and basic reinforcement learning models. |
| **1980s** | **Backpropagation Algorithm**: The resurgence of neural networks, particularly the development of the backpropagation algorithm by Geoffrey Hinton and others, enabling training of deep neural networks. |
| **1990s** | **Support Vector Machines (SVM)**: Introduction of SVM, a powerful supervised learning algorithm for classification and regression tasks. |
| **2000s** | **Rise of Big Data and Ensemble Methods**: With the increase in computational power, big data became more accessible, leading to the development of ensemble methods like Random Forest and boosting algorithms. |
| **2010s** | **Deep Learning Revolution**: Deep learning, particularly using deep neural networks and techniques like convolutional neural networks (CNNs) and recurrent neural networks (RNNs), achieved state-of-the-art performance in many domains like image and speech recognition. |
| **2020s** | **AI/ML Integration and Ethical Concerns**: Machine learning becomes integral to various industries, with growing attention on ethical concerns, bias, and the interpretability of AI systems. Transformer models, like GPT and BERT, revolutionize natural language processing. |

### 🧠 Mental Representation

> How should we think about x?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

## Paradigm

> **Paradigm of Computational System Construction**, in the realm of **Computational Learning**.
> 

```bash
🔵 Computational System (How to Build a Computational System?)
├── 🟢 Programming (Manual System Creation)
│
└── 🟡 Computational Learning (CL) (System Synthesis)
    ├── 🔴 Supervised Learning
    ├── 🟠 Unsupervised Learning
    └── 🟤 Evolutionary Learning
    ├── 🟣 Reinforcement Learning    
    ├── ⚫ Self-Supervised Learning

 ⚫ Neuromorphic
 🟠 Probabilistic
 🟡 Neuro-Symbolic System
```

| Paradigm | Description |
| --- | --- |
| **Meta Learning** | Learning to learn: the system improves its own learning process across tasks or environments. |
| **Supervised Learning** | Learning from labeled data, where the system maps inputs to known outputs. |
| **Unsupervised Learning** | Learning patterns or structure from unlabeled data, such as clustering or dimensionality reduction. |
| **Reinforcement Learning** | Learning by interacting with an environment, using rewards and penalties to guide behavior. |
| **Self-Supervised Learning** | Learning representations from unlabeled data by generating surrogate labels from the data itself. |
| **Evolutionary Learning** | Learning through population-based search and adaptation, inspired by biological evolution (e.g., genetic algorithms). |
| **Representation Learning** | Learn useful feature representations directly from data, often through optimization-based approaches like deep learning. |

### Representation Learning

> **Representation learning** is a branch of machine learning focused on automatically discovering compact, meaningful representations of data that make downstream tasks—like classification, regression, and clustering—easier and more effective.
> 

> **Representation learning** is a subfield of machine learning and artificial intelligence concerned with **automatically discovering and constructing effective feature representations from raw data**, typically through hierarchical or nonlinear transformations. The goal is to **learn representations that disentangle and expose the underlying explanatory factors of variation** in the data, making subsequent tasks (e.g., classification, regression, clustering) more tractable.
> 

> A **Sparse Distributed Representation** is a way of encoding information as a high-dimensional binary or real-valued vector where:
> 
> - Only a small percentage of the components (bits or neurons) are active (non-zero) at any time (sparsity).
> - The information is distributed across many components rather than localized in one.

> **Representation learning** is a type of machine learning that enables models to automatically discover and learn useful features or representations from raw data, facilitating the performance of various tasks such as classification, regression, and clustering.
> 

![](https://miro.medium.com/v2/resize:fit:1400/1*Xnqhv2iGK9J6KYcFtklqoQ@2x.jpeg)

Key Questions:

- How to represent recursive structures? Tensor Product Representations (TPR), Recursive Autoassociative Memories (RAAM), Holographic Reduced Representations (HRR, Hierarchical Sequence Models, Recursive Neural Networks.
- …

### Reinforcement Learning

> **Reinforcement Learning (RL)** is a type of machine learning where an *agent* learns to make decisions by interacting with an *environment*, receiving *rewards* for good actions and adjusting its strategy over time to maximize long-term success.
> 

> See more in [Dynamical Intelligence](../dynamical-intelligence.md).
> 

## Problem Encoding

> How to represent the input? How to encode the input?
> 

> See more in [Input Representation](input-representation.md).
> 

## Trainable Computational System Space

> **TCSEE** (**Trainable** **Computational System** → **Evolution** ←→  **Evaluation**): **Random Untrained Template** → Train System.
> 

> Note: In **Computational Learning**, the **synthesized computational systems** are pure; they do not have side effects. However, they can be connected to actuators to interact with the  **environment**.
> 

### Capacity

> Which are the tasks or capacities that a hypothetical 'Trainable Computational System' can perform?
> 

| **Capacity** | **Related Capacity** | **Description** |
| --- | --- | --- |
| Recall | Memory, Retrieval, Knowledge Base Lookup | Ability to store and retrieve information from memory when needed. |
| Planning | Sequential Decision-Making, Task Scheduling, Policy Optimization | Ability to organize actions or steps to achieve a goal. |
| Prediction | Classification(Tags) , Regression, Sequence Modeling, Forecasting | Ability to anticipate future states, events, or outcomes based on past and present information. |
| Adaptation | Transfer Learning, Online Learning, Meta-Learning | Ability to adjust behavior or strategy in response to changes in the environment. |
| Exploration | Bandit Algorithms, Reinforcement Learning Exploration, Curiosity-Driven Learning | Ability to seek out new possibilities, strategies, or environments. |
| Understanding | Representation Learning, Semantic Parsing, Knowledge Extraction | Ability to extract meaning and relations from information and experiences. |
| Self-Regulation | Regularization, Optimization Control, AutoML, Hyperparameter Tuning | Ability to monitor, evaluate, and adjust its own processes or behaviors. |
| World Modelling | Generative Models, Simulation Learning, Model-Based RL | Ability to build internal models of the environment and its dynamics. |
| Goal-Directed Behavior | Reinforcement Learning, Control, Policy Learning | Ability to pursue defined objectives through coherent action. |
| Perception & Representation | Computer Vision, Speech Recognition, Embedding Learning, Encoding  | Ability to sense, interpret, and represent external or internal states. |

### Space

> Note: Distinguish between the model’s capacity **(what it can do)**, the mechanisms that implement it (how it works), and the teaching strategy, including optimization and training procedures **(how it is taught)**.
> 

> **Note:** *Representation* may designate either the **structural state of a trainable system** or the **representational capacity and encoding scheme through which the system models its domain**. These notions must be distinguished explicitly to avoid conceptual conflation.
> 

| **Category** | **Trainable Computational System** | **Description** | **Representation (How the System Is Represented?)** | **Evaluation** | **Optimization (Evolution)** |
| --- | --- | --- | --- | --- | --- |
| Linear Models | Linear Regression | Models linear relationship between features and continuous target. | Weight vector, bias term | MSE, R² | Normal equation, Gradient Descent |
|  | Ridge Regression | Linear regression with L2 regularization. | Weights with penalty term | RMSE, MAE | Gradient Descent |
|  | Lasso Regression | Linear regression with L1 regularization. | Sparse weights | RMSE, MAE | Coordinate Descent |
|  | Elastic Net | Combination of L1 and L2 regularization. | Weighted mix of L1/L2 penalties | MAE, R² | Coordinate Descent |
|  | Polynomial Regression | Fits non-linear data using polynomial terms. | Polynomial feature expansion | R², MSE | Least squares, GD |
| Classification | Logistic Regression | Models probability of binary outcomes. | Sigmoid on linear weights | Log-loss, AUC | Gradient Descent, L-BFGS |
|  | Softmax Classifier | Multiclass generalization of logistic regression. | Softmax weights | Cross-entropy | SGD, Adam |
|  | Perceptron | Binary classifier updated sequentially. | Weight vector | Misclassification error | Online weight updates |
|  | Passive-Aggressive (PA) | Online large-margin classifier. | Weight vector | Hinge loss | Online convex optimization |
| Decision Trees | CART | Tree with Gini or MSE splits. | Tree structure | Gini, Accuracy | Greedy splitting |
|  | ID3 | Tree using information gain (entropy). | Tree nodes and branches | Entropy reduction | Greedy splitting |
| Ensemble Methods | Random Forest | Bagging of decision trees. | Forest of trees | OOB error, Accuracy | Random sampling + tree learning |
|  | AdaBoost | Sequentially weighted tree boosting. | Weighted tree ensemble | Accuracy, AUC | Weighted error minimization |
|  | XGBoost | Gradient boosting with regularization. | Additive tree model | Log-loss, Accuracy | Gradient descent + shrinkage |
|  | LightGBM | Leaf-wise gradient boosting. | Histogram bins + leaves | AUC, RMSE | Histogram-based greedy |
|  | CatBoost | Handles categorical variables automatically. | Oblivious trees | Log-loss | Ordered boosting |
| Kernel Methods | SVM (Linear/RBF) | Finds separating hyperplane in feature space. | Support vectors, kernels | Margin, AUC | Quadratic Programming |
|  | Kernel Ridge Regression | Combines ridge regression with kernel trick. | Kernel matrix | MSE | Dual optimization |
| Instance-Based | k-NN | Predicts by nearest neighbors. | Stored examples | Accuracy, Top-k | Lazy (no training) |
|  | LVQ | Learns representative prototypes for each class. | Prototypes in feature space | Classification error | Gradient descent on prototypes |
| Neural Networks | MLP | Fully connected feedforward network. | Weight matrices | Cross-entropy, MSE | Backpropagation, SGD |
|  | CNN | Convolutions for spatial data. | Filters, feature maps | Accuracy, IOU | SGD, Adam |
|  | RNN | Models sequential data. | Recurrent hidden states | Perplexity, Accuracy | BPTT |
|  | LSTM | RNN with gates for long-term memory. | Cell states, gates | Accuracy, BLEU | Adam, RMSProp |
|  | Transformer | Attention-based architecture. | Attention weights, embeddings | Perplexity, BLEU | Adam, Learning rate schedule |
|  | RNN with Hebbian Plasticity | Recurrent network with activity-dependent weight updates. | Recurrent weights | Prediction error, stability | Hebbian learning rules |
| Probabilistic Models | Naive Bayes | Assumes conditional independence. | Likelihood tables | Log-loss, Accuracy | Closed-form, MLE |
|  | Gaussian NB | Uses Gaussian for continuous features. | Mean/variance per class | Accuracy, Log-loss | MLE |
|  | GMM | Mixture of Gaussians for clustering/density. | Means, covariances | Log-likelihood, BIC | EM algorithm |
| PGMs | Bayesian Networks | Directed acyclic graph with CPDs. | Nodes and CPTs | Inference accuracy | EM, Variational Inference |
|  | CRFs | Undirected models for structured prediction. | Graphical structure | Label accuracy | Maximum likelihood, SGD |
| Clustering | K-Means | Assigns points to k centroids. | Centroids | Silhouette, Inertia | Lloyd's algorithm |
|  | DBSCAN | Density-based clustering. | Core points and neighborhoods | ARI, Purity | Parameter-based detection |
|  | Mean Shift | Shifts points toward mode of density. | Density peaks | Cluster quality | Mode seeking algorithm |
|  | Spectral Clustering | Uses eigenvectors of similarity matrix. | Laplacian eigenvectors | NMI, ARI | Eigen decomposition |
| Dimensionality Reduction | PCA | Projects data to maximize variance. | Principal components | Explained variance | SVD |
|  | ICA | Maximizes statistical independence. | Independent components | Reconstruction error | Gradient descent |
|  | t-SNE | Preserves local structure in low-dim space. | Pairwise similarities | KL divergence | Gradient descent |
|  | UMAP | Preserves local & global structure. | Topological embedding | Trustworthiness, NMI | Graph layout optimization |
| Autoencoder Models | Autoencoder | Neural network that reconstructs input. | Bottleneck layer | MSE, Reconstruction error | Backpropagation |
| RL Models | Q-Learning | Tabular value iteration. | Q-table | Reward sum | Bellman update |
|  | DQN | Deep Q-value approximator. | Neural network Q-function | Episode reward | Replay buffer + gradient descent |
|  | Policy Gradient | Directly optimizes policy. | Stochastic policy | Expected reward | REINFORCE, Adam |
|  | PPO | Stable policy optimization. | Actor-Critic architecture | Total return | Clipped objective function |
| Graph Models | GCN | Convolution over graphs. | Node features + adjacency | Node classification acc. | Backpropagation |
|  | GAT | Attention-based GCN variant. | Attention weights | Accuracy, F1 | Adam |
| Symbolic Models | ILP | Learns logic rules from examples. | Logic programs | Rule accuracy | Search over hypotheses |
| Evolutionary Models | Genetic Algorithms | Population-based optimization. | Chromosomes | Fitness score | Mutation, crossover |
|  | NEAT | Evolve neural network topology. | Evolving graphs | Task-specific | Neuroevolution |
| Energy-Based Models | RBM | Energy-based model with hidden units. | Energy function | Free energy | Contrastive divergence |
|  | DBM | Stacked RBMs. | Multiple energy layers | Log-likelihood | Layer-wise training |
|  | Hopfield Net | Associative memory network. | Energy surface | Stability, Recall rate | Hebbian rule |
| Mixture Models | DPMM | Infinite mixture model. | Stick-breaking process | Log-likelihood | Gibbs sampling |
| Survival Models | Cox Model | Models hazard rate over time. | Hazard function | Concordance index | Partial likelihood |
| Generative Models | GAN | Generator vs discriminator. | Two NNs | FID, Inception Score | Alternating GD |
|  | Diffusion Model | Reverse-time denoising process. | Noise schedule | FID, Log-likelihood | Score matching, Langevin |
| Feature Selection | Recursive Feature Elimination | Iteratively removes least useful features. | Subsets of features | Accuracy, AUC | Greedy elimination |
| Anomaly Detection | One-Class SVM | Separates normal data from origin. | Hyperplane in feature space | Precision, Recall | QP solver |
|  | Isolation Forest | Uses random splits to isolate anomalies. | Isolation trees | Anomaly score | Random partitioning |
| Association Learning | Apriori | Finds frequent itemsets. | Itemset lattice | Support, Confidence | Bottom-up search |
|  | FP-Growth | Frequent itemset mining using prefix trees. | FP-tree | Lift, Support | Tree-based mining |
| Statistical Models | Kalman Filter | Recursive Bayesian estimation. | State transition + measurement | Prediction error | Linear Gaussian updates |
|  | HMM | Hidden state sequence model. | Transition + emission matrix | Log-likelihood | EM (Baum-Welch) |
|  | Gaussian Process | Non-parametric regression/classification. | Covariance function | Log-marginal likelihood | Matrix inversion, Gradient Descent |
| Adaptive Filters | LMS Filter | Linear adaptive filter minimizing MSE. | Filter weights | MSE, SNR improvement | Stochastic gradient descent |
|  | RLS Filter | Recursive least squares adaptive filter. | Filter weights + covariance matrix | MSE, Convergence speed | Recursive updates |
|  | Kalman Filter Adaptive | Combines adaptive filtering with state estimation. | State + covariance | Prediction error | Kalman gain updates |
| Signal Processing Models | FIR Filter Design | Trains filter coefficients to match frequency response. | Coefficient vector | Frequency response error | Least squares, windowing |
|  | IIR Filter Design | Feedback filter with trainable poles/zeros. | Coefficients of numerator/denominator | Magnitude response error | Nonlinear optimization |
| Reservoir Computing | Echo State Network (ESN) | RNN with fixed reservoir; only output weights trained. | Reservoir states + output weights | MSE, prediction accuracy | Linear regression on output weights |
|  | Liquid State Machine (LSM) | Spiking neuron reservoir network for temporal tasks. | Reservoir spikes + readout weights | Classification accuracy | Gradient-free or Hebbian learning |
| Signal Reconstruction | Wiener Filter | Optimal linear filter minimizing output MSE given signal + noise statistics. | Filter coefficients | MSE, SNR | Closed-form solution |
|  | Blind Source Separation (ICA) | Separates mixed signals without knowing sources. | Unmixing matrix | Signal-to-interference ratio | Gradient descent or FastICA |
| Neuromorphic Models | Spiking Neural Network (SNN) | Neurons emit spikes; temporal coding. | Spike trains + synaptic weights | Accuracy, spike-timing error | STDP, gradient surrogate |
| Filtering & Estimation | Particle Filter | Nonlinear Bayesian state estimation. | Set of weighted particles | RMSE, likelihood | Resampling + weight update |
| Quantum-Inspired Models | Quantum Boltzmann Machine | Probabilistic model using quantum states. | Qubits + energy function | Log-likelihood | Quantum annealing or gradient-based |
| Control Systems | Adaptive PID Controller | PID gains updated based on performance. | Kp, Ki, Kd | Tracking error, overshoot | Gradient descent, recursive tuning |
| Graph Signal Processing | Graph Adaptive Filter | Filter on graph signals; weights trained to minimize error. | Graph adjacency + filter coefficients | MSE on nodes | Gradient-based optimization |

## Trainable Computational System Aspect Set

> A Trainable Computational System is a representational tool that can learn from data or experience to perform tasks through training.
> 

> Which are the aspects that **characterizes this systems**?
> 

| **Aspect** | **Description** |
| --- | --- |
| **Input Representation** | The way raw data is encoded before processing (e.g., feature vectors, embeddings, tokens, graphs, images). |
| **Teaching Strategy** | A general concept that can refere to the teaching paradigm, certain input representation (masking  - prediction),  basically; how can we teach this capacity; to this system. |
| **Regularization** | Mechanisms to prevent overfitting and enforce generalization (e.g., dropout, weight decay, early stopping, constraints). |
| **Optimization (Evolution)** | The algorithmic process for adjusting parameters to minimize/maximize an objective (e.g., gradient descent, evolutionary strategies). |
| **Evaluation** | Methods to assess performance against objectives, including metrics (accuracy, loss, reward) and validation schemes. |
| **Hyperparameter** | Externally set variables controlling training dynamics (e.g., learning rate, batch size, architecture depth). |
| **Capacity** | Fundamental abilities of the system (e.g., prediction, planning, recall, adaptation, exploration, understanding). |
| **Property** | System-level characteristics emerging from design and training (e.g., robustness, scalability, interpretability, efficiency). |
| **Inference Strategy** |  |
| **Output Representation** | The form in which results are expressed (e.g., class labels, probability distributions, sequences, generated content). |
| **Inductive Bias** | … |

### Hyperparameter

> Externally set variables controlling training dynamics (e.g., learning rate, batch size, architecture depth).
> 

### Parameter Space

> The **parameter space** of a **model is the mathematical** domain—typically a high-dimensional **Euclidean space**—comprising all possible configurations of its learnable parameters. Formally, for a parameter vector $\theta \in \mathbb{R}^n$, the parameter space is $\Theta \subseteq \mathbb{R}^n$, where each point $\theta \in \Theta$ corresponds to a distinct instantiation of the model.
> 

Properties:

- **Dimensionality**: Equal to the number of independent parameters in the model.
- **Topology**: In most practical machine learning models, $\Theta$ is endowed with the standard topology of  $\mathbb{R}^n$, allowing notions like continuity and differentiability to apply to functions defined over it (e.g., the loss function $\mathcal{L}(\theta)$).
- **Optimization Landscape**: The parameter space is the domain over which optimization (e.g., via gradient descent) is performed to minimize a cost function.
- **Search Space**: In Bayesian or evolutionary methods, the parameter space defines the domain of probabilistic or combinatorial search.

### Inductive Bias

> **Inductive bias** refers to the set of assumptions that a learning algorithm uses to generalize beyond the training data. In machine learning, since it's impossible to learn anything useful from data alone without making any assumptions (as per the *No Free Lunch Theorems*), every model has to impose some bias to make learning feasible.
> 

| **Bias Type** | **Example** | **Effect** |
| --- | --- | --- |
| **Preference Bias** | Linear models prefer straight-line solutions. | Reduces overfitting, enables generalization. |
| **Restriction Bias** | Decision trees split on features; k-NN assumes local similarity. | Limits hypothesis space to manageable regions. |
| **Language Bias** | Logic programs may restrict to Horn clauses. | Determines what kinds of functions or rules can be expressed. |
| **Regularization Bias** | L2 regularization prefers small weights. | Penalizes complex models to prefer simpler ones. |

### **Teaching Strategy**

> Which concrete teaching strategies should we employ to train our systems? How to show the system data that induces learning?
> 

> **Teaching Strategy:** The method or procedure used to organize how a model is exposed to data and learning signals, guiding it toward the acquisition of desired capacities. This includes the design of input-output examples, feedback mechanisms, curricula, and other instructional techniques that induce learning. However, here, we focus on the **overall organization of learning**, rather than the specific mechanics of parameter updates, optimization algorithms, or low-level training procedures.
> 

| **Strategy** | **Description** | **How Does It Teaches?** | **Capacity Taught** |
| --- | --- | --- | --- |
| **Masked Token (Patch Prediction)** | Hide part of the input (tokens in text, patches in images) and predict them. | Forces the model to infer missing information from surrounding context. | Contextual understanding, feature extraction. |
| **Next-Step (Sequence Prediction)** | Predict the next item in a sequence (next word, next frame, next action). | Learning signal comes from predicting what comes next, capturing temporal and causal dependencies. | Temporal reasoning, sequence modeling. |
| **Denoising (Corruption Recovery)fv** | Add noise or distort input and train the system to reconstruct the original. | Teaches the system to focus on underlying structure rather than surface noise. | Robust representation, feature extraction. |
| **Permutation (Shuffling Prediction)** | Shuffle parts of the input and train the model to recover original order. | Forces the model to encode relational structure between components. | Structural understanding, reasoning about order. |
| **Contrastive Pairing** | Show positive and negative pairs and teach the system which are similar or related. | Pulls similar representations together and pushes dissimilar ones apart in embedding space. | Discriminative embeddings, cross-modal understanding. |
| **Hint (Guided Prediction)** | Provide partial hints or scaffolds for the output and train the system to complete. | Gradually reduces guidance to increase autonomy while retaining correctness. | Complex reasoning, compositional understanding. |
| **Multi-Task Signal Mixing** | Train on multiple related tasks simultaneously with shared representation. | Learning is reinforced across tasks, helping capture shared structures. | Generalization, compositionality. |
| **Self-Consistency (Chain-of-Thought)** | Generate multiple reasoning paths and enforce consistency. | Rewards outputs that agree across reasoning chains, improving stability and robustness. | Logical reasoning, problem-solving. |
| **Reward Shaping** | Provide detailed intermediate feedback rather than only final outcomes. | Guides learning by breaking down complex objectives into manageable, reinforced steps. | Complex decision-making, planning. |
| **Curriculum (Difficulty Scheduling)** | Start with simpler examples and progressively increase difficulty. | Gradually increases challenge, allowing incremental acquisition and stabilization of skills. | Robust mastery of capacities, hierarchical learning. |
| **Co-training** | Train multiple models (or views) on complementary subsets of data and allow them to teach each other. | Models share predictions or confidence to reinforce each other’s learning. | Robust generalization, semi-supervised learning, multi-view integration. |
| **Adversarial Training** | Train the system with inputs that are intentionally perturbed or challenging (adversarial examples). | Forces the model to learn more robust and generalizable features by resisting misleading or tricky inputs. | Robustness, security-aware reasoning, resilience to noise. |
| Knowledge Distillation | Use a large, trained “teacher” model to guide a smaller “student” model. | Student model learns to mimic teacher outputs, capturing complex patterns efficiently. | Efficient representation, transfer of expertise. |
| Imitation Learning | Train the system to mimic expert demonstrations (actions, decisions, or outputs). | Provides a direct mapping from input to desired behavior, reducing exploration complexity. | Behavioral replication, decision-making, policy learning. |
| Contrastive Predictive Coding (CPC) | Learn representations by predicting future latent states in an embedding space. | Encourages the model to encode information useful for predicting future structure without direct supervision. | Sequential representation, feature extraction, temporal dependencies. |
|  |  |  |  |

### Inference Strategy

> How can we guide or augment a model’s reasoning and behavior at inference time to improve its performance?
> 

> An **inference strategy** is a method used to guide, structure, or augment a model’s behavior *at inference time* (when it is generating outputs, not being trained).
> 

> See more in [Chain-of-thought (CoT)](chain-of-thought-cot.md).
> 

| **Strategy** | **Description** |
| --- | --- |
| **Chain-of-Thought (CoT)** | Model generates intermediate reasoning steps in natural language before producing the final answer, improving multi-step reasoning. |
| **Self-Consistency** | Sample multiple CoT reasoning paths and select the most consistent answer across them, reducing errors from single-path reasoning. |
| **Tree-of-Thought (ToT)** | Organize reasoning as a branching search tree, exploring alternative solution paths before selecting the best one. |
| **ReAct (Reason + Act)** | Interleaves reasoning steps with external actions (e.g., querying tools or APIs) to solve more complex problems. |
| **Reflection (Self-Reflection)** | Model reviews and critiques its own output to identify and correct errors. |
| **Debate (Multi-Agent Reasoning)** | Multiple model instances argue different positions, and a final judgment aggregates their reasoning. |
| **Prompt Chaining** | Breaks a complex task into a sequence of smaller inference steps, passing the output of one as the input to the next. |

### **Training Optimization**

> 
- **Batch Training**
- ….

### Evolution (Optimization)  (Training)

> **Credit Assignment** refers to the problem of determining **which parts of a model or which actions in a sequence are responsible for a particular outcome** (e.g., success or failure, reward or loss). It’s a central challenge in **learning systems**, especially in **reinforcement learning** and **deep learning**.
> 

Training - Evolution :  The general process involves:

1. Starting with an **unrefined (initial) learning model**.
2. **Adjusting (training) the model using data**, so it can identify patterns or relationships.
3. **Refining the model until it can accurately reproduce (or generalize) the underlying data-generating process**.

| **Method** | **Description** | **Use** |
| --- | --- | --- |
| **Gradient Descent (GD)** | Iteratively updates parameters in the direction of the negative gradient of the loss function. | General-purpose optimization for training neural networks and regression models. |
| **Stochastic Gradient Descent (SGD)** | Uses a randomly sampled mini-batch of data to compute approximate gradients. | Efficient large-scale training, faster convergence on big datasets. |
| **Momentum** | Extends SGD by adding a fraction of the previous update to the current step. | Accelerates convergence, helps escape shallow local minima. |
| **Nesterov Accelerated Gradient (NAG)** | A variant of momentum that anticipates the next position for gradient calculation. | Faster convergence and better stability than standard momentum. |
| **Adagrad** | Adapts learning rates individually for each parameter based on past gradients. | Good for sparse data and features; adapts learning rates automatically. |
| **RMSProp** | Divides the learning rate by a moving average of recent squared gradients. | Handles non-stationary objectives, common in RNN training. |
| **Adam** | Combines momentum and RMSProp; maintains moving averages of gradients and squared gradients. | Default optimizer for most deep learning tasks; robust and efficient. |
| **AdamW** | Variant of Adam with decoupled weight decay regularization. | Prevents overfitting, standard in modern deep learning architectures. |
| **Adadelta** | Extension of Adagrad that restricts the window of accumulated past gradients. | Adaptive learning rates without manual tuning, stable for deep networks. |
| **LBFGS** | Quasi-Newton method approximating the Hessian matrix for faster convergence. | Effective for smaller datasets and convex problems, often in classical ML. |
| **SGD with Learning Rate Scheduling** | Adjusts the learning rate during training according to a schedule. | Improves convergence and helps escape plateaus or sharp minima. |
| **Evolutionary / Genetic Algorithms** | Population-based search optimizing parameters using mutation, crossover, and selection. | Non-differentiable objectives, black-box optimization, hyperparameter search. |
| **Bayesian Optimization** | Probabilistic model guides the search for optimal hyperparameters. | Hyperparameter tuning, expensive function optimization. |

### **Regularization**

| Technique | Description |
| --- | --- |
| **Early Stopping** | Stop training when validation performance degrades |
| **Dropout** | Randomly deactivate neurons during training |
| **L1 / L2 Regularization** | Penalize large weights in the loss function |
| **Data Augmentation** | Randomly transform input data to increase diversity |
| **Mixup / CutMix** | Blend inputs/labels to smooth decision boundaries |

### Evaluation

> Methods to assess performance against objectives, including metrics (accuracy, loss, reward) and validation schemes.
> 

| **Name** | **Description** |
| --- | --- |
| **Accuracy** | Fraction of correct predictions over total predictions; measures overall correctness. |
| **Precision** | Fraction of true positives among all predicted positives; measures correctness of positive predictions. |
| **Recall (Sensitivity)** | Fraction of true positives among all actual positives; measures completeness of positive predictions. |
| **F1 Score** | Harmonic mean of precision and recall; balances correctness and completeness. |
| **Mean Squared Error (MSE)** | Average squared difference between predicted and actual values; penalizes large errors. |
| **Root Mean Squared Error (RMSE)** | Square root of MSE; same units as target variable, easier interpretation. |
| **Mean Absolute Error (MAE)** | Average absolute difference between predicted and actual values; less sensitive to outliers than MSE. |
| **R² (Coefficient of Determination)** | Fraction of variance explained by the model; measures goodness-of-fit for regression. |
| **Log-Loss / Cross-Entropy** | Measures probability distance between predicted and true labels; used in classification. |
| **Area Under ROC Curve (AUC-ROC)** | Measures trade-off between true positive rate and false positive rate; evaluates classifier ranking. |
| **Confusion Matrix** | Tabular summary of predicted vs. actual class labels; useful for detailed classification analysis. |
| **Perplexity** | Exponential of average negative log-likelihood; used for evaluating probabilistic language models. |
| **BLEU / ROUGE** | Measures overlap between generated text and reference text; used in NLP tasks like translation or summarization. |

### Validation

> See more in [Model Validation](model-validation.md).
> 

### Post-training Technique

| Technique | Description | Use Cases |
| --- | --- | --- |
| **Model Quantization** | Reduce precision of weights (e.g., float32 → int8) to save space | Mobile, embedded systems |
| **Pruning** | Remove redundant neurons or connections | Model compression |
| **Knowledge Distillation** | Train smaller "student" model to mimic a larger "teacher" | Fast inference, model compression |
| **Retraining (Fine-Tuning) (Adaptation)** | Further train model on specialized domain or dataset | Domain adaptation |
| **Calibration** | Adjust predicted probabilities to reflect real confidence | Medical AI, classification |
| **Bias Correction** | Adjust outputs to mitigate known bias or fairness issues | Ethical ML, hiring models |
| **Adversarial Training** | Retrain with adversarial examples to improve robustness | Security-critical applications |
| **Post-Hoc Explainability** | Analyze and interpret model decisions after training | SHAP, LIME, fairness audits |
| **Ensembling** | Combine predictions of multiple models (e.g., voting, averaging) | Competitions, robustness |
| **Embedding Extraction** | Use trained model as a feature extractor (e.g., BERT, CLIP) | Downstream tasks, transfer learning |

### Assumption

| **Assumption** | **Implication** |
| --- | --- |
| IID (Independent and Identically Distributed Data) | Training and test data come from the same distribution. |
| Stationarity | The data-generating process doesn't change over time. |
| Sufficient Features | The inputs contain enough information to predict outputs. |
| Learnability | There exists a hypothesis in the model class that performs well. |

### Property

> System-level characteristics emerging from design and training (e.g., robustness, scalability, interpretability, efficiency).
> 
- Scale-Invariant (Stable Under Certain Input Perturbation)
- …

## **Ensemble Trainable Computational System**

> Let’s bring together a lot of **Trainable Computational System to build a Larger System.**
> 

## Relation

> Which are the related areas to ML?
> 

| Area | Description | AI Relation |
| --- | --- | --- |
| **Statistical Learning Theory** | Framework for understanding ML algorithms through statistics and probability, focusing on inference and model performance. | Provides the theoretical foundation for designing, analyzing, and evaluating ML models. |
| **Pattern Recognition** | Identifying and classifying patterns in data using algorithms and statistical techniques. | Core to applications like image, speech, and handwriting recognition. |
| **Computational Statistics** | Application of computational techniques to perform statistical analysis, including algorithm development and simulations. | Enables efficient model training, resampling, and simulation-based inference. |
| **Statistics** | Study of data collection, analysis, interpretation, and presentation. | Essential for hypothesis testing, feature selection, and evaluating model performance. |
| **Probability** | Study of randomness, uncertainty, and likelihood of events. | Underpins probabilistic models, Bayesian methods, and uncertainty estimation. |
| **Optimization** | Techniques to find the best parameters for a model under constraints. | Central to training ML models via gradient descent, convex/non-convex optimization. |
| **Linear Algebra** | Study of vectors, matrices, and linear transformations. | Fundamental for representing data, neural networks, and matrix operations in ML. |
| **Calculus** | Study of change, derivatives, and integrals. | Required for gradient computation and backpropagation in neural networks. |
| **Information Theory** | Study of quantifying, storing, and communicating information. | Provides metrics like entropy, KL divergence, and mutual information used in ML models. |
| **Signal Processing** | Analysis, transformation, and interpretation of signals. | Important for feature extraction in audio, image, and time-series data. |
| **Graph Theory** | Study of nodes and edges and their relationships. | Underpins graph neural networks, knowledge graphs, and relational data modeling. |
| **Computational Complexity** | Study of algorithmic efficiency and resource usage. | Guides design of scalable ML algorithms and understanding training/inference limits. |
| **Numerical Methods** | Algorithms for approximating mathematical operations. | Used for efficient computation in ML, e.g., solving linear systems and eigenproblems. |
| **Data Mining** | Extracting patterns from large datasets. | Provides algorithms for clustering, association rules, and anomaly detection. |
| **Database Systems** | Organizing, storing, and querying structured data. | ML relies on efficient access to large-scale datasets for training and evaluation. |
| **Reinforcement Learning** | Study of agents learning from interactions with an environment via rewards. | Core paradigm for AI in robotics, games, and decision-making systems. |
| **Control Theory** | Study of regulating dynamic systems to achieve desired behavior. | Forms the basis for RL and AI-driven robotics control systems. |
| **Cognitive Science** | Interdisciplinary study of mind, perception, and learning. | Inspires neural architectures, learning algorithms, and AI modeling of cognition. |
| **Neuroscience** | Study of brain structure and function. | Provides inspiration for neural networks and biologically plausible learning rules. |
| **Computer Vision** | Automatic analysis of images and videos. | Core application of ML for object recognition, segmentation, and tracking. |
| **Natural Language Processing (NLP)** | Processing and understanding human language. | Uses ML to perform translation, sentiment analysis, summarization, and chatbots. |
| **Robotics** | Design, control, and autonomous operation of robots. | ML is applied for perception, planning, and control in robotic systems. |
| **Simulation & Modeling** | Creating computational models of real-world systems. | ML uses simulations to generate synthetic data and optimize systems. |
| **Operations Research** | Mathematical modeling for decision-making and optimization. | Helps design AI systems for logistics, scheduling, and resource allocation. |
| **Econometrics** | Statistical methods applied to economic data. | Supports predictive modeling, causal inference, and AI-driven economic simulations. |
| **Bayesian Statistics** | Probabilistic framework for inference with prior knowledge. | Widely used in probabilistic ML, Bayesian networks, and uncertainty quantification. |
| **Time Series Analysis** | Analysis of sequential data points over time. | Core for forecasting, anomaly detection, and sequential decision-making in AI. |
| **Complex Systems Theory** | Study of emergent behavior in interacting systems. | Informs AI modeling of networks, multi-agent systems, and adaptive behavior. |
| **Fuzzy Logic** | Reasoning with uncertain or imprecise information. | Used in rule-based AI, control systems, and approximate reasoning. |
| **Topology** | Study of geometric properties preserved under deformation. | Emerging use in topological data analysis for feature extraction and ML. |
| **Game Theory** | Study of strategic interactions among rational agents. | Used in multi-agent RL, adversarial ML, and economic AI models. |
| **Evolutionary Computation** | Optimization inspired by biological evolution. | Includes genetic algorithms and evolutionary strategies for AI model search. |
| **Human-Computer Interaction (HCI)** | Study of how humans interact with computers. | Guides design of AI systems for usability, interpretability, and collaboration. |

## Formalism

> Formalisms for Artificial General Intelligence (AGI) aim to provide theoretical frameworks and models that can describe or guide the development of systems with general intelligence comparable to or surpassing human intelligence.
> 

| **Theory** | Description |
| --- | --- |
| **AIXI** | Mathematical ideal of general intelligence; combines Solomonoff induction + reinforcement learning. |
| **Predictive Coding** | Brain-inspired: minimizes prediction error via hierarchical Bayesian inference. |
| **Free Energy Principle** | Extension of predictive coding; systems act to minimize "surprise" (free energy). |
| **Solomonoff Induction** | Theoretical optimal Bayesian inference for sequence prediction. |
| **Causal Learning** | Learning cause-effect relationships (vs. correlations). |
| **Developmental AI** | Embodied learning through stages (e.g., infant-like curiosity). |
| **Integrated Information Theory (IIT)** | Measures consciousness (Φ) as integrated information. |
| **Federated Learning** | Decentralized learning across devices while preserving privacy. |
| **Neural Darwinism** | Neural networks evolve via selection (e.g., synaptic pruning). |
| **Rational Agent Model** | An agent chooses actions that maximize its expected utility based on beliefs about the world. Standard in AI. |
| **Adaptive Control Theory** | Intelligence as the ability to control a system optimally in an uncertain environment. |
| Turing Machines | Intelligence as the ability to compute functions. Led to ideas like the Church-Turing thesis for intelligence. |
| Bayesian Brain Hypothesis | The brain (or an intelligent agent) *updates beliefs* using Bayes' rule. Intelligence = optimal inference under uncertainty. |
| **Predictive Coding** | The brain constantly predicts sensory inputs and corrects errors; learning = minimizing prediction error. |
| Connectionist | Intelligence emerges from many simple processing units (neurons) interacting. Deep learning is a modern version. |
| Evolutionary Computation | Intelligence can evolve through variation and selection, like biological evolution (e.g., genetic algorithms). |
| Embodied Cognition | Intelligence is deeply tied to the body's interactions with the world — not just brain-in-a-vat computation. |
| Minimum Description Length Principle | Intelligence prefers simpler, more compressible models of the world (compression = understanding). |
| Symbolic Reasoning (GOFAI) | Early AI: Intelligence is manipulating symbols according to formal rules (e.g., logic, theorem proving). |

## Challenge

- [ ]  https://en.wikipedia.org/wiki/Winograd_schema_challenge

## ❓ QA

- Why not called how machines learn? but how do we teach them?
- What’s the **teaching / learning** duality?
- What do we mean by representation learning?
- What does a given learning system represent? How does that learning system represent a given representation target (RepTarget)? What are common types of **RepTargets**?
- Is asking whether the same learning system can represent many things a sensible question?

### Is ML Linear Algebra?

> Note: ML is not linear algebra. In fact, the algebraic part is rarely used directly; linear algebra mainly provides data structures for representing information, while the real work comes from calculus, optimization, and other nonlinear methods.
> 

### Is ‘Generative AI’ a misnomer?

> Generative AI; fundamental is also Input → Output;  all AI is Generative. Even if you say - It  Generates new content; it’s a composition of the building blocks.
> 

### How does the quality of data affect machine learning model quality?

> 

### Does all data need to be converted into numerical form to perform machine learning?

Basically Yes,  most machine learning algorithms rely on:

- **Algebraic operations** (like dot products, matrix multiplication),
- **Optimization techniques** (like gradient descent), and
- **Distance metrics** (like Euclidean or cosine distance).

These operations **require numeric input** (real numbers, vectors, tensors).

| **Original Data Type** | **Numerical Representation** | **Technique** |
| --- | --- | --- |
| Text | Word embeddings, one-hot vectors | TF-IDF, Word2Vec, BERT |
| Categories | One-hot, label encoding | Scikit-learn encoders |
| Images | Pixel intensity values | Numpy arrays or tensors |
| Audio | Spectrograms, MFCCs | Signal processing tools |
| Graphs | Adjacency matrices, node embeddings | GNNs, DeepWalk |
| Time series | Sequences of values | Sliding windows, feature extraction |

### When we talk about a learning system that correctly represents a decision boundary, do we judge this based on the model’s behavior—its ability to classify points correctly—or based on the model’s internal architecture?

![image.png](../assets/note/epistemica/observational/computational-learning/image-3.png)

> When we talk about a learning system that correctly learns or represents a decision boundary—like a complex frontier between countries—and you want to determine which country a given point belongs to, there are two main ways to interpret this:
> 

**Inference from Model Behavior (Output-based Interpretation):**

- Here, the model acts like a black box.
- You input the point coordinates, and the model outputs the predicted country (label).
- The decision boundary is implicit, derived from how the model classifies points.
- This is the common approach in many ML systems where the internal workings aren’t directly interpreted.
- You don't explicitly see which part of the model corresponds to which sub-region; you only see the final classification result.

 **Inference from Internal Architecture (Interpretability or Explainability):**

> Map the **behavior** to the **internal structures** responsible for it.
> 
- This approach tries to *open the black box* and understand which parts of the model correspond to which sub-regions.
- For example, in some neural networks, specific neurons or subnetworks might specialize in recognizing features or regions.
- In classical decision trees, branches explicitly represent sub-regions.
- In complex neural networks or deep learning, it is much harder but sometimes possible with interpretability techniques (like layer-wise relevance propagation, feature attribution, or attention maps) to assign parts of the network to certain decision regions.
- You might identify subnetworks or clusters of neurons responsible for particular spatial regions (e.g., islands or overlaps).

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [](https://app.notion.com/p/245c0f5171ec80749daec722e73b8a81?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- [Functional](../mathematical/functional.md)
- [Decision Boundary](https://en.wikipedia.org/wiki/Decision_boundary)
- [Decision boundary](https://en.wikipedia.org/wiki/Decision_boundary)
- [Pattern Recognition](https://en.wikipedia.org/wiki/Pattern_recognition)
- [Representer theorem](https://en.wikipedia.org/wiki/Representer_theorem)
- [Statistical classification](https://en.wikipedia.org/wiki/Statistical_classification)
- [Computational Statistics](https://en.wikipedia.org/wiki/Computational_statistics)
- [Statistical learning theory](https://en.wikipedia.org/wiki/Statistical_learning_theory)
- https://en.wikipedia.org/wiki/Machine_learning
- https://en.wikipedia.org/wiki/Artificial_intelligence
- https://paperswithcode.com/task/representation-learning
- Hutter, Marcus. "Universal algorithmic intelligence: A mathematical top→ down approach." Artificial general intelligence. Berlin, Heidelberg: Springer Berlin Heidelberg, 2007. 227-290.
- [ ]  https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/
- https://chizkidd.github.io//2025/05/30/machine-learning-key-math-eqns/#gradient-descent
- [‣](https://app.notion.com/p/25d598edb7908029ac2dce7687abe850?pvs=21)
- [Algorithm](https://app.notion.com/p/Algorithm-617ee00b46ea444799ea7a4945d72921?pvs=21)
- https://en.wikipedia.org/wiki/Mixture_of_experts
- https://categoricaldeeplearning.com/
- [**Statistical Mechanics**](note.html?n=epistemica/construction/statistical-mechanics.md)
- Akyürek, Ekin, et al. "The surprising effectiveness of test-time training for abstract reasoning." *arXiv preprint arXiv:2411.07279* (2024).
- https://medium.com/@rachittayal7/a-gentle-introduction-to-distributed-training-of-ml-models-81295a7057de
- https://arxiv.org/abs/2407.07852
- https://plato.stanford.edu/entries/fine-tuning/
- https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)
- https://d2l.ai/chapter_computer-vision/fine-tuning.html
- https://stats.stackexchange.com/questions/421741/what-is-the-credit-assignment-problem-in-machine-learning-and-deep-learning
- https://arxiv.org/abs/2312.01072
- https://en.wikipedia.org/wiki/Parameter_space
- https://lilianweng.github.io/posts/2025-05-01-thinking/
- https://en.wikipedia.org/wiki/Adaptive_filter
- https://atcold.github.io/2024/08/05/SN.html
- https://karpathy.github.io/2022/03/14/lecun1989/
