---
tags: [estimator, probability]
---

# Maximum Likelihood Estimation (MLE)

 : James–Stein Estimator (James%E2%80%93Stein%20Estimator%20b73b540853f0462391dc223b38dff1e3.md)

> **Maximum Likelihood Estimation (MLE)** is a method of estimating the parameters of a statistical model by maximizing the **likelihood function**, which measures the probability of observing the given data as a function of the parameters, yielding parameter values that make the observed data most probable under the assumed model.
> 

MLE is a **methodological framework** (or **general estimation scheme**) for finding the parameters of a statistical model that make the observed data most probable.

- It’s **not a specific algorithm** — it’s a principle.
- You can use many different optimization techniques (calculus, gradient descent, numerical solvers) to actually compute the MLE, depending on the complexity of the model.

## Meta

> Evaluation Framework.
> 

> **The understanding of a concept is proportional** to the time invested in deep reflection, deliberate practice, and repeated engagement with its nuances. If a Concept has been learned soft of by osmosis - then is not well understood.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | ⭐⭐⭐⭐ (Strong). Well-structured, relevant, and insightful, though with minor room for improvement. |
| **Completeness** | … |
| **Coherence & Structure** | … |
| **Epistemic Self-Assessment** | ⭐⭐ (Basic). Partial understanding; can handle simple situations but lacks depth, integration, or flexibility. -  Weakness –  Multiple Parameters - **MLE**. |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** | See more here [**What’s my study Strategy?**](maximum-likelihood-estimation-mle.md). |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | **MLE is a principle of parameter estimation**: choose the parameter values that maximize the probability (likelihood) of observing the data you actually saw. Its essence is aligning model parameters with observed reality by maximizing plausibility under the model. |
| **Evidentia (Evidence) 📊** | The justification for MLE lies in probability theory: maximizing the likelihood is equivalent to finding the most probable explanation for the data under the model. MLE has desirable asymptotic properties — it is **consistent**, **asymptotically unbiased**, and **efficient** under mild regularity conditions. Its performance can be empirically verified via simulation (bias, variance) or through goodness-of-fit tests. |
| **Telos (Intent) 🎯** | The aim is to produce parameter estimates that make the chosen model describe the data as well as possible. It provides a universal, mathematically grounded procedure to connect theory (model) and observation (data). The outcome is a single "best-fitting" parameter vector. |
| **Gnosis (Understanding) 🧠** | To build a mental representation: understand (1) probability models, (2) likelihood as a function of parameters, (3) calculus-based optimization, and (4) log-likelihood simplifications. Developing intuition involves seeing likelihood surfaces, comparing different parameter values, and practicing with examples (Bernoulli, Normal, regression). A solid foundation in probability and optimization is required to make this representation meaningful and usable. |
| **Epignosis (Application) 🛠️** | Applied in almost every statistical model: linear regression, logistic regression, survival models, mixture models, hidden Markov models, deep learning (cross-entropy loss = negative log-likelihood). Mastery enables building custom likelihoods for complex models and using numerical optimization methods (Newton-Raphson, gradient ascent, EM algorithm). |
| **Relatio (Connections) 🔗** | Connects deeply to: **Bayesian inference** (MLE is a special case with a uniform prior), **information theory** (KL-divergence minimization), **machine learning** (loss functions often are negative log-likelihoods), and **decision theory** (frequentist estimation framework). |
| **Idoneitas (Suitability) 📐** | MLE performs well when the model is well-specified and the sample size is large. Metrics of suitability include bias, mean squared error, asymptotic efficiency, and goodness-of-fit diagnostics. |
| **Limites (Limits) ⛔** | If the model is mis-specified, MLE can produce misleading results. It may have multiple local maxima, be numerically unstable, or fail when data are sparse. Small samples can produce biased or high-variance estimates. |
| **Contextus (Context) 🌍** | Developed by Ronald A. Fisher in the 1920s as part of the foundation of modern statistics. MLE became a unifying principle in parametric statistics, bridging theoretical probability and practical data analysis. |
| **Dynamis (Evolution) 🌱** | Modern evolutions include penalized MLE (regularization, e.g., Lasso), generalized likelihood methods, likelihood-free inference (ABC), and integration into machine learning frameworks where it appears as loss minimization. |
| **Critica (Critique) 🔍** | Criticized for sensitivity to model mis-specification and for ignoring prior knowledge (purely frequentist). Can be computationally expensive in high dimensions. These critiques led to Bayesian methods, robust likelihoods, and alternative estimators (e.g., method of moments, M-estimators). |
| **Verbum Usus (Language Use) 🗣️** | The term “maximum likelihood” is standard in statistics, econometrics, and machine learning. Often shortened to "MLE." In practice, it’s used to mean either the **principle** (“fit the model via MLE”) or the **result** (“the MLE of θ is …”). Its use carries connotations of rigor, optimality, and generality. |

### 🧠 Mental Representation

> How should we think about MLE?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 
- **Core Idea:** MLE finds the parameter values that make the observed data most probable under the chosen model.
- **Visualize Likelihood Surfaces:** Imagine a “landscape” where the height represents the likelihood for different parameter values. The MLE is at the peak.
- **Log-Likelihood Intuition:** Maximizing log-likelihood is like stretching or smoothing the surface to simplify calculations without changing the peak location.
- **Connection to Data & Model:** MLE aligns model assumptions with observed data; think of it as tuning the model until it best “explains” what you see.

### 📜 History

> Timeline of key developments and milestones related to MLE.
> 

| Period | Milestone |
| --- | --- |
| 1920s | Ronald A. Fisher develops the Maximum Likelihood Estimation principle. |
| 1930s–1950s | Formalization of MLE in parametric statistics; widespread adoption in theoretical statistics. |
| 1960s–1970s | Development of numerical optimization methods for MLE (e.g., Newton-Raphson). |
| 1980s–1990s | Application in econometrics, generalized linear models, survival analysis. |
| 2000s–Present | Integration into machine learning frameworks; penalized likelihood, EM algorithm, likelihood-free inference (ABC). |

## **Likelihood Principle**

> Is the “**Likelihood Principle” a  principle of just a Heuristic in - the MLE Scheme?**
> 

> **Likelihood Principle** – The estimate depends only on the likelihood function (not on other aspects of the data collection).
> 

> The maximum likelihood principle is used because it selects the parameter that makes the observed data **most probable**, and this approach has strong **theoretical guarantees** (consistency, efficiency, asymptotic normality) and is **intuitively appealing**.
> 

### Intuition

> Imagine you toss a coin $n$ times and see $k$ heads. You don’t know the probability of heads $p$. MLE chooses $p$ that **makes your actual outcome most likely**.
> 

> If you saw 7 heads in 10 tosses, MLE says $\hat{p} = 0.7$  because that value makes the observed data most probable.
> 

> So it’s a **natural principle**: pick the parameter that best “explains” the data you actually observed.
> 

### **Limitations**

- Can be biased for small samples.
- May not exist or be unique for some models.
- Sensitive to model misspecification.

## Procedure

> In statistics, we already have a well-established set of models and their corresponding likelihood functions. If the data reasonably fits a known model (and vice versa), there is usually no need to invent a completely new model or likelihood function. Instead, we just choose the appropriate model from this existing set and perform estimation.
> 

> Note: The challenging part of MLE is often **selecting the right model for the data**. This step is as much an art as it is a science, requiring experience, domain knowledge, and sometimes experimentation to ensure that the chosen model **appropriately captures** the underlying data-generating process - or **characterizes** the data.
> 

> Note: A probabilistic model (Statistical Model) defines the **model class** (e.g., Normal distribution, logistic regression).
> 

> Note: The results of the process is called - Maximum Likelihood Estimator.
> 

> MLE is a **principle** that says: “Choose the parameters that maximize the likelihood.”
> 

> The actual maximization can be done with calculus (simple cases) or numerical optimization (complex cases).
> 

Steps for performing Maximum Likelihood Estimation (MLE):

1. **Specify the Model and Parameters**
    - Define a model $M$ with parameters $\theta$.
    - The model can be as simple as a probability distribution (e.g., Normal with mean and variance) or a more complex relationship between features and outcomes.
2. **Construct the Likelihood Function**
    - Build the **likelihood function** $L(\theta)$, which measures how likely the observed data is given the parameters $\theta$: $L(\theta) = P(\text{data} \mid \theta)$
    - This function quantifies how well the model with parameters $\theta$ explains the data.
3. **Optimize the Likelihood Function**
    - Use mathematical optimization to find the parameter values $\hat{\theta}$ that **maximize** $L(\theta)$.
    - In practice, we usually maximize the **log-likelihood** because it simplifies calculations:$\ell(\theta) = \log L(\theta)$
    - The MLE solution is found by solving for the parameters where the gradient is zero:
    $\frac{\partial \ell(\theta)}{\partial \theta} = 0$

## **Likelihood Function**

> Likelihood is **non-negative**, but log-likelihood can be negative.
> 

> If your **likelihood $L(\theta)$ itself** is negative, that is **impossible**. It usually indicates a **calculation or formula error** (e.g., missing squares in a normal pdf, wrong constants, or a mistaken sign).
> 

> $L(\theta; x_1, \dots, x_n) = \prod_{i=1}^n f(x_i; \theta)$, we take one parameter;
> 

## Property

> Which are the fundamental properties of MLE Scheme?
> 

> How do we proof this properties?
> 

| **Property** | **Description** |
| --- | --- |
| **Consistency** | The MLE converges in probability to the true parameter value as the sample size grows: $\hat{\theta}_{MLE} \xrightarrow{p} \theta$. |
| **Asymptotic Unbiasedness** | Although the MLE may be biased for finite samples, $\lim_{n \to \infty} \mathbb{E}[\hat{\theta}_{MLE}] = \theta$. |
| **Asymptotic Normality** | For large $n$, the MLE is approximately normally distributed: $\sqrt{n}(\hat{\theta}_{MLE} - \theta) \xrightarrow{d} \mathcal{N}(0, I(\theta)^{-1})$, where $I(\theta)$ is the Fisher information. |
| **Asymptotic Efficiency** | Among all consistent estimators, the MLE achieves the minimum asymptotic variance (Cramér–Rao lower bound). |
| **Invariance Property** | If $\hat{\theta}$ is the MLE of $\theta$, then $g(\hat{\theta})$ is the MLE of $g(\theta)$ for any function $g$. |
| **Equivariance under Reparameterization** | MLE results are consistent under smooth transformations of parameters. |
| **Sufficiency** | If sufficient statistics exist, the MLE is typically a function of them, using all information in the sample. |
| **Asymptotic Optimality** | MLE minimizes asymptotic mean squared error among regular estimators. |
| **Large-Sample Approximation to Bayesian Posterior Mode** | For large $n$, the MLE coincides with the mode of the posterior under a uniform prior. |
| **Relation to Information Theory** | MLE asymptotically minimizes Kullback–Leibler divergence between the true distribution and the model. |
| **Potential Bias in Small Samples** | In finite samples, MLE can be biased or unstable; bias corrections or alternative estimators may be preferred. |
| **Sensitivity to Model Mis-specification** | If the assumed model is wrong, MLE may be inconsistent or misleading. |
| **Computational Considerations** | Finding MLE may require iterative numerical optimization for complex models; multiple local maxima are possible. |
| **Robustness Limitations** | MLE is sensitive to outliers and extreme observations; robust variants (M-estimators) exist. |

### **Asymptotic Unbiasedness**

> An estimator $\hat{\theta}_n$ is asymptotically unbiased for a parameter $\theta$ if its bias approaches zero as the sample size grows: $\lim_{n \to \infty} \text{Bias}(\hat{\theta}n)
= \lim{n \to \infty} \bigl(\mathbb{E}[\hat{\theta}_n] - \theta\bigr) = 0.$
> 

> Maximum Likelihood Estimators (MLEs) are generally not exactly unbiased for finite $n$, but under standard regularity conditions, they become **asymptotically unbiased**, meaning that for sufficiently large $n$, their expected value gets arbitrarily close to the true parameter. This property is a key reason MLEs perform well in large-sample settings.
> 

### **Invariance Property**

> The MLE of a transformation of a parameter is simply the transformation of the MLE.
> 

> The **invariance property of MLEs** is **not just a re-representation** — it actually **gives you a valid estimator for a new parameter**.
> 

Let:

- $X_1, X_2, \ldots, X_n$ be your observed data.
- $L(\theta) = f(x_1, x_2, \ldots, x_n ; \theta)$ be the likelihood function.
- $\hat{\theta} = \arg\max_{\theta} L(\theta)$ be the MLE of $\theta$.
- Define a parameter of interest $\phi = g(\theta)$ where $g$ is a one-to-one, differentiable function.
- Then: $\hat{\phi}_{\text{MLE}} = g(\hat{\theta})$ is the MLE of $\phi$.

Benefit:

- **Without the property**, you would have to rederive the likelihood in terms of $\theta = \text{depends on } \phi$, maximize it, and solve for $\phi$.
- **With the property**, you can skip that entire process and just transform your existing MLE.

## Alternative

> What other estimation schemes (methods) exist for estimating model parameters that best fit the data?
> 

| **Scheme** | **Description** |
| --- | --- |
| **Method of Moments (MoM)** | Estimates parameters by equating sample moments (mean, variance, etc.) with theoretical moments of the model. Often simpler than MLE but may be less efficient. |
| **Bayesian Estimation** | Uses Bayes’ theorem to compute a full posterior distribution for parameters. Produces a probability distribution over possible parameter values, not just a single point estimate. |
| **Least Squares (LS)** | Minimizes the sum of squared residuals. A special case of MLE under Gaussian noise assumptions. Widely used in regression problems. |
| **Generalized Method of Moments (GMM)** | Extends MoM by using multiple moment conditions and weighting them optimally. Popular in econometrics. |
| **Robust Estimation (M-Estimators)** | Modifies the likelihood or loss function to reduce sensitivity to outliers or model mis-specification. Examples include Huber loss. |
| **Maximum A Posteriori (MAP)** | Similar to MLE but incorporates a prior distribution over parameters. Finds the mode of the posterior distribution. |
| **Quantile Regression / Median-Unbiased Estimation** | Estimates parameters by matching conditional quantiles (like the median) rather than the mean, making it robust to skewed distributions. |
| **Minimum Distance Estimation** | Chooses parameters that minimize a distance (e.g., KL-divergence, Wasserstein) between empirical and theoretical distributions. |

## Limits

> What are the limits or constraints that apply to the MLE scheme?
> 

| **Limit  (Constraint)** | **Description** |
| --- | --- |
| **Finite-Sample Bias** ⚠️ | MLE can be biased in small samples, especially for complex models or models with many parameters. |
| **Model Mis-specification** ❌ | If the assumed model does not reflect the true data-generating process, MLE can be inconsistent and produce misleading estimates. |
| **Non-Regular Likelihoods** ⚡ | Some likelihood functions are irregular (non-differentiable, multimodal), making MLE undefined or difficult to compute. |
| **Computational Challenges** 🖥️ | Complex models may require iterative numerical optimization, which can be slow or get trapped in local maxima. |
| **Sensitivity to Outliers** 🔒 | MLE is highly sensitive to extreme values or outliers, which can distort parameter estimates. |
| **Sample Size Dependence** 📏 | Many desirable properties of MLE (unbiasedness, efficiency, normality) are asymptotic; small samples may violate these. |
| **Identifiability Requirements** 🔑 | Parameters must be identifiable; if multiple parameter values produce the same likelihood, MLE is not unique. |
| **Assumption Dependence** 📐 | MLE relies on correct assumptions about data distribution (independence, identical distribution, etc.). |

## Case Study

### Uniform Distribution

> Suppose we have $X_1, X_2, \dots, X_n \sim \text{Uniform}(0, \theta)$, where $\theta > 0$ is unknown, here $\text{Uniform}(0, \theta)$ is our model.
> 

> The **goal**: find the Maximum Likelihood Estimator (MLE) for $\theta$.
> 

Likelihood Function: 

$L(\theta; x_1, \dots, x_n) = \prod_{i=1}^{n} f(x_i; \theta) = \prod_{i=1}^{n} \frac{1}{\theta} \mathbf{1}{\{0 \le x_i \le \theta\}}
= \frac{1}{\theta^n} \mathbf{1}{\{\theta \ge \max(x_1, \dots, x_n)\}}$, where $\mathbf{1}_{\{\cdot\}}$ is the indicator function.

Log-Likelihood Transformation:

$\ell(\theta) = \log L(\theta) = -n \log \theta + \log \mathbf{1}{\{\theta \ge X{(n)}\}}$ where $X_{(n)} = \max(x_1, \dots, x_n)$, Notice that the log-likelihood is **monotonically decreasing in $\theta$** for $\theta \ge X_{(n)}$.

Maximization:

- Because $L(\theta) = 0$ for $\theta < X_{(n)}$, the likelihood is **only positive when $\theta \ge X_{(n)}$**.
- Among all $\theta \ge X_{(n)}$, the likelihood decreases as $\theta$ increases.
- Therefore, the **maximum occurs at the smallest feasible $\theta$**: $\hat{\theta}{MLE} = X{(n)} = \max(x_1, \dots, x_n)$

### Bernoulli Estimation

> Suppose we have $X_1, X_2, \dots, X_n \sim \text{Bernoulli}(p)$, where $p \in [0,1]$ is the unknown probability of “success.”
> 

Likelihood Function:

> Assuming that observations are independent,  $L(p; x_1, \dots, x_n) = \prod_{i=1}^{n} p^{x_i} (1-p)^{1-x_i} = p^{\sum x_i} (1-p)^{n - \sum x_i}$
> 

> Let $S = \sum_{i=1}^{n} X_i$ be the total number of successes. Then: $L(p) = p^S (1-p)^{n-S}$
> 

Log-Likelihood Transformation:

> $\ell(p) = \log L(p) = S \log p + (n-S) \log (1-p)$
> 

Maximization:

- Take the derivative w.r.t $p$ and set it to 0:  $\frac{d\ell(p)}{dp} = \frac{S}{p} - \frac{n-S}{1-p} = 0$
- Solve for $p$: $\frac{S}{p} = \frac{n-S}{1-p} \quad \Rightarrow \quad S(1-p) = (n-S)p$
- $S - S p = n p - S p \quad \Rightarrow \quad S = n p$
- $\hat{p}{MLE} = \frac{S}{n} = \frac{1}{n} \sum{i=1}^{n} X_i$

### Regression

Suppose we have $n$ observations $(x_i, y_i)$ and we assume the **linear model**: $Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \text{ i.i.d.}$

- Parameters to estimate: $\theta = (\beta_0, \beta_1, \sigma^2)$
- Goal: find the MLEs $\hat{\beta}_0, \hat{\beta}_1, \hat{\sigma}^2$

**Likelihood Function:**

The conditional PDF of $Y_i$ given $x_i$ is:
$f(y_i \mid x_i; \beta_0, \beta_1, \sigma^2) = \frac{1}{\sqrt{2 \pi \sigma^2}} \exp \Bigg[ - \frac{(y_i - \beta_0 - \beta_1 x_i)^2}{2\sigma^2} \Bigg]$

Assuming independent errors, the likelihood function is:
$L(\beta_0, \beta_1, \sigma^2) = \prod_{i=1}^n \frac{1}{\sqrt{2 \pi \sigma^2}} \exp \Bigg[ - \frac{(y_i - \beta_0 - \beta_1 x_i)^2}{2\sigma^2} \Bigg]$

**Log-Likelihood Transformation:**

> $\ell(\beta_0, \beta_1, \sigma^2) = -\frac{n}{2} \log(2\pi) - \frac{n}{2} \log \sigma^2 - \frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$
> 

**Maximization:**

(a) MLE of $\beta_0, \beta_1$

> Maximizing $\ell$ w\.r.t $\beta_0, \beta_1$ is equivalent to **minimizing the sum of squared residuals**:  $\text{RSS}(\beta_0, \beta_1) = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$
> 

Solve the normal equations:
$\frac{\partial \text{RSS}}{\partial \beta_0} = 0, \quad \frac{\partial \text{RSS}}{\partial \beta_1} = 0$

The solutions are:
$\hat{\beta}1 = \frac{\sum{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}, \quad
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$

(b) MLE of $\sigma^2$

Plug $\hat{\beta}_0, \hat{\beta}_1$ into the log-likelihood and maximize w\.r.t $\sigma^2$:  $\frac{\partial \ell}{\partial \sigma^2} = - \frac{n}{2\sigma^2} + \frac{\text{RSS}(\hat{\beta}_0, \hat{\beta}_1)}{2 (\sigma^2)^2} = 0$

Solve for $\sigma^2$: $\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2$

## ❓ QA

> How to adapt the **MLE Scheme** for non I.I.D data?
> 

> Prove the **consistency** of the MLE under regularity conditions. Which regularity conditions are essential?
> 

> Derive the **asymptotic normality** of the MLE and explain the role of the Fisher information.
> 

> Explain the **Cramér–Rao lower bound** and demonstrate how the MLE achieves asymptotic efficiency.
> 

> Discuss **bias and variance** trade-offs for MLE in finite samples. Can you construct examples where MLE is biased?
> 

> How do **reparameterizations** affect the MLE? Can you formally prove equivariance?
> 

> Derive the **relationship between MLE and Kullback–Leibler divergence**. Why does MLE minimize KL divergence asymptotically?
> 

> How do you deal with **multiple local maxima** in the likelihood function? Provide algorithmic strategies.
> 

> Discuss the **computational complexity** of MLE in high-dimensional or structured models (e.g., hierarchical models).
> 

> Explain **penalized likelihoods** (Lasso, Ridge) and how they modify the classical MLE principle.
> 

> How does **numerical optimization** (Newton-Raphson, EM algorithm, gradient ascent) converge to the MLE? What assumptions are needed?
> 

> How do you assess **convergence and stability** of an iterative MLE algorithm in practice?
> 

> How sensitive is MLE to **outliers** or extreme observations? How can influence functions be used to quantify this?
> 

> How does MLE connect to **Bayesian estimation**? How does a uniform prior make MAP equivalent to MLE?
> 

> Explain the connection between MLE and **information theory**, particularly KL divergence and cross-entropy loss.
> 

> Discuss MLE in the context of **latent variable models** (e.g., mixture models, HMMs) and the use of the EM algorithm.
> 

> How can MLE be generalized in **likelihood-free inference** (Approximate Bayesian Computation)?
> 

> Compare MLE to **minimum distance estimation** or **generalized method of moments** in terms of efficiency and robustness.
> 

> Can MLE fail to exist? Provide explicit examples (e.g., non-regular likelihoods, boundary parameters).
> 

> Is there any relation with LDA (Linear Discriminant Analysis) and MLE?
> 

> How to proof the **Invariance Property of MLE Scheme?**
> 

### **What’s my study Strategy?**

> Mastering MLE at a PhD level requires years of iterative study, rigorous mathematical derivation, computational experimentation, and critical reflection to internalize its theoretical foundations, asymptotic properties, practical implementation, and connections to broader statistical and probabilistic frameworks.
> 

> My strategy progresses from basic conceptual understanding of the subject to meta-level comprehension, combining practical examples with technical reflection to master the appropriate application of the scheme.
> 

**Build Strong Foundations**

- **Probability & Statistics:** Ensure mastery of probability distributions, expected values, variance, joint/marginal distributions, independence, conditional probability.
- **Mathematical Tools:** Be fluent in multivariate calculus, linear algebra, real analysis, and measure-theoretic probability for rigorous derivations.
- **Conceptual Clarity:** Understand what likelihood is, why it is **not a probability of parameters**, and the philosophical principles behind MLE (Likelihood Principle, invariance, consistency).

**Systematic Theoretical Study**

- **Properties of MLE:** Study consistency, asymptotic normality, efficiency, sufficiency, and equivariance.
- **Advanced Theory:** Learn the Cramér–Rao lower bound, Fisher information, likelihood ratio tests, and connections to information theory.
- **Edge Cases & Limits:** Study non-iid data, boundary parameters, small-sample bias, and model mis-specification.

**Computational & Applied Mastery**

- **Implementation Skills:** Write likelihood and log-likelihood functions in Python, R, or Julia.
- **Numerical Optimization:** Practice Newton-Raphson, gradient ascent, EM algorithm for latent-variable models, and handling convergence issues.
- **Visualization:** Plot likelihood surfaces and log-likelihoods to develop intuition about parameter behavior.

**Integration & Reflection**

- **Compare with Other Methods:** Understand method of moments, Bayesian estimation (MAP), M-estimators, and generalized method of moments (GMM).
- **Critical Reflection:** Examine where MLE succeeds and fails, think about sensitivity to model mis-specification, sample size, and outliers.
- **Meta-Learning:** Reflect on your understanding, connect MLE to decision theory, machine learning, and statistical inference at a broader level.

**Iterative Deepening**

- **Simulate & Experiment:** Create synthetic datasets to test MLE properties under controlled conditions.
- **Teach & Explain:** Try explaining MLE and its subtleties to peers or in writing; this exposes gaps in understanding.
- **Research Applications:** Apply MLE to real, messy data; confront practical issues like non-convergence, missing data, or model selection.

### What is the meaning of **`likelihood` in `likelihood function`?**

> **Note:** This is **not a probability**. It is simply an **evaluation of how well the model parameters explain the observed data**—a measure of the model’s explanatory capacity for the data.
> 

> The **likelihood** is a measure of **how plausible a set of parameters is given the observed data**.
> 

> The word **“likelihood”** emphasizes that this is an **evaluation of the plausibility of parameters**, not a probability of the parameters themselves.
> 

### What Is a Model in This Setting?

> In this context, a **model** is a mathematical or probabilistic representation of the process that generates the observed data. It defines a **family of probability distributions** (or functions) characterized by certain parameters, which describe how data behaves under the assumptions of the model.
> 

### What Is a Parameter in This Setting?

> A **parameter** is a numerical characteristic or quantity within the model that determines the specific behavior of the distribution. Examples include the mean and variance of a Normal distribution, the probability of success in a Bernoulli trial, or regression coefficients in a linear model. Parameters are **unknown values** that MLE aims to estimate from the observed data.
> 

### Does f(D | $\theta$); means conditional Probability?

> This is a common source of confusion caused by ambiguous notation. For this reason, the likelihood is often written as $f(D; \theta)$ instead of $f(D \mid \theta)$. It is **not a conditional probability**: the data $D$ is fixed and not a random event, so the likelihood is a function of the parameters $\theta$, not of the data.
> 

> This means the likelihood measures **how plausible the observed data is given a specific choice of parameters**. In other words, it evaluates **how well a particular parameterization of the model explains or fits the observed data**. The likelihood function treats the data as fixed and varies the parameters to find the values that make the data most probable.
> 

### In Maximum Likelihood Estimation, why is the likelihood function defined as the product of the probabilities (or densities) of the observed data points?

> Multiplying the probabilities is equivalent to asking:  - What is the probability of seeing **all these observations exactly as they occurred**, assuming the model parameters $\theta$ are true? - Each observation contributes independently to the total likelihood, which is why we multiply.
> 

> If the observations are also **identically distributed** (i.i.d.), each term comes from the same distribution $f(x; \theta)$. Then the likelihood becomes:  $L(\theta) = \prod_{i=1}^{n} f(x_i; \theta)$
> 

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- 
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [Plato’s Dialectic Method](https://app.notion.com/p/Plato-s-Dialectic-Method-268c0f5171ec805cbb91d16158ae579e?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- [](https://app.notion.com/p/24ac0f5171ec8020aec7f11bae9eb632?pvs=21)
- https://en.wikipedia.org/wiki/Maximum_likelihood_estimation
- 
- https://en.wikipedia.org/wiki/Likelihood_principle
- https://stats.stackexchange.com/questions/70972/why-we-always-put-log-before-the-joint-pdf-when-we-use-mlemaximum-likelihood
- https://intro.quantecon.org/mle.html
- Lehmann, E. L., & Casella, G. (1998). *Theory of point estimation* (2nd ed.). Springer.
- Rao, C. R. (1973). Linear statistical inference and its applications (2nd ed.). Wiley.
- Ferguson, T. S. (1996). *A course in large sample theory*. Chapman & Hall.
- Casella, G., & Berger, R. L. (2002). Statistical inference (2nd ed.). Cengage Learning.
- Le Cam, Lucien. "Maximum likelihood: an introduction." *International Statistical Review/Revue Internationale de Statistique* (1990): 153-171.
- Olive, David (2004). "Does the MLE maximize the likelihood?" (PDF). Southern Illinois University.
- Zacks, Shelemyahu (1971). The Theory of Statistical Inference. New York: John Wiley & Sons. p. 223.
- Hald, Anders (1999). "On the History of Maximum Likelihood in Relation to Inverse Probability and Least Squares". Statistical Science. 14 (2): 214–222. doi:10.1214/ss/1009212248.
- Wilks, Samuel S. (1962). *Mathematical Statistics*. New York, NY: John Wiley & Sons.
- Stigler, Stephen M. (1986). The history of statistics: the measurement of uncertainty before 1900. Harvard University Press.
- Stigler, Stephen M. (1999). Statistics on the table: the history of statistical concepts and methods. Harvard University Press.
- Hald, Anders (1998). A history of mathematical statistics from 1750 to 1930. New York, NY: Wiley.
- Aldrich, John (1997). ["R.A. Fisher and the making of maximum likelihood 1912–1922"](https://doi.org/10.1214%2Fss%2F1030037906)
- https://en.wikipedia.org/wiki/Invariant_estimator
- https://stats.stackexchange.com/questions/390741/invariance-property
