---
tags: [inference, regression]
---

# Simple Linear Regression

 : Regression (Regression%20175c0f5171ec80ba9eb2d67dd7339800.md)

> **Linear regression** is a **statistical modeling technique** that estimates the linear relationship between a dependent variable and one or more independent variables by minimizing the squared differences between observed and predicted values.
> 

> **Gauss** and **Legendre’s** invention of the method of least squares—long before vectors, matrices, or modern statistics—was a visionary leap that laid the foundation for regression, inference, and much of modern data science.
> 

> **Modelling Note:** These are purely empirical, linear-regression models of a given phenomenon; they do not attempt to explain its inner structure, mechanisms, or causal chain. They merely describe superficial state changes, and the state representation itself is often highly aggregated and abstract.
> 

QA (see more in https://github.com/dbremont/desirable-difficulties/blob/main/modelado/Linear-Regression.md):

- **How to think about linear regression?** What kinds of **processes can it represent**? How can we evaluate if a process is suitable to be modeled using **linear regression**? What are the limitations of **linear regression**?
- How to think about linear regression? What are the limits of **linear regression**?
- Is the loss calculated over the entire dataset (global), over local neighborhoods of data points, or in some other way?

## 📘 Breviarium: Linear Regression

### Formulation

> Linear Regression is a **parametric-supervised learning method** that models the conditional expectation $\mathbb{E}[Y \mid X]$ of a scalar response variable $Y \in \mathbb{R}$ as a **linear combination** of explanatory variables $X = (X_1, X_2, \dots, X_p)^T \in \mathbb{R}^p$.
> 

The **model assumes** the form: $Y = X^T \beta + \varepsilon$ where:

- $p\beta \in \mathbb{R}^p$ is the vector of unknown regression coefficients,
- $\varepsilon \sim \mathcal{N}(0, \sigma^2)$ is an i.i.d. stochastic error term with zero mean and constant variance (homoskedasticity), and
- $X^T \beta$ defines a **hyperplane** in $\mathbb{R}^p$.

### Core Components

- **Representation**: Linear regression models the dependent variable as a linear combination of input features plus an error term: $y = \mathbf{x}^\top \boldsymbol{\beta} + \varepsilon$ where $\boldsymbol{\beta}$ contains the coefficients to be estimated, and $\varepsilon$ is assumed to be a zero-mean, homoscedastic, and independent error.
- **Optimization**: The model parameters $\boldsymbol{\beta}$ are estimated by minimizing the **residual sum of squares (RSS)**: $\hat{\boldsymbol{\beta}} = \arg\min_{\boldsymbol{\beta}} \| \mathbf{y} - \mathbf{X} \boldsymbol{\beta} \|^2$ This is a convex problem with a closed-form solution if $\mathbf{X}^\top \mathbf{X}$ is invertible.
- **Evaluation**: The model is typically evaluated using metrics such as **Mean Squared Error (MSE)**, **$R^2$** (coefficient of determination), and **adjusted $R^2$**. Residual analysis and inference on $\boldsymbol{\beta}$ (e.g., t-tests, confidence intervals) are used to assess model fit and variable significance.

### Representation Capacity

> See more here [](https://app.notion.com/p/248c0f5171ec80618455e4de9574f748?pvs=21).
> 

| **Characteristic** | **Description** |
| --- | --- |
| **Linearity** | The expected value of the outcome is a linear function of inputs. |
| **Additivity** | Each input contributes additively (not multiplicatively or interactively unless transformed). |
| **Homogeneity of variance** | The variance of errors does not depend on input values (homoscedasticity). |
| **Independence** | Observations are independent of each other. |
| **Gaussian noise (optional)** | For inference (e.g., confidence intervals), we often assume normally distributed errors. |

## Representation

| **Representation** | **Description** | **Form** |
| --- | --- | --- |
| **Scalar Form** | Expresses the model and prediction in terms of individual variables. | $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p + \varepsilon$ |
| **Vector Form** | Represents features and coefficients as vectors; useful for compact notation. | $y = \mathbf{x}^\top \boldsymbol{\beta} + \varepsilon$ |
| **Matrix Form** | Represents multiple samples using matrices; enables batch computation. | $\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\varepsilon}$ |
| **Optimization Problem (MSE)** | Objective is to minimize squared error loss over dataset. | $\min_{\boldsymbol{\beta}} \ \frac{1}{n} \| \mathbf{y} - \mathbf{X} \boldsymbol{\beta} \|^2$ |
| **Normal Equation** | Closed-form solution derived by setting gradient to zero. | $\boldsymbol{\hat{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}$ |
| **Probabilistic Form** | Interprets outputs as noisy observations from a normal distribution. | $y_i \sim \mathcal{N}(\mathbf{x}_i^\top \boldsymbol{\beta}, \sigma^2)$ |
| **Bayesian Form** | Places prior over parameters; results in posterior distributions. | $p(\boldsymbol{\beta} \mid \mathbf{X}, \mathbf{y}) \propto p(\mathbf{y} \mid \mathbf{X}, \boldsymbol{\beta}) \, p(\boldsymbol{\beta})$ |
| **Geometric Interpretation** | Views solution as orthogonal projection onto column space of $\mathbf{X}$. | $\mathbf{\hat{y}} = \mathbf{X} \boldsymbol{\hat{\beta}}$ is projection of $\mathbf{y}$ onto $\text{col}(\mathbf{X})$ |
| **Dual Form** | Expresses solution in terms of dot products; useful in kernel methods. | $\boldsymbol{\hat{\beta}} = \mathbf{X}^\top \boldsymbol{\alpha}$ where ${\alpha} = (\mathbf{X} \mathbf{X}^\top)^{-1} \mathbf{y}$ |
| **Regularized Form** | Adds penalty to control model complexity (e.g., Ridge, Lasso). | Ridge: $\min_{\boldsymbol{\beta}} \ \| \mathbf{y} - \mathbf{X} \boldsymbol{\beta} \|^2 + \lambda \| \boldsymbol{\beta} \|^2$                       Lasso:  $\min_{\boldsymbol{\beta}} \ \| \mathbf{y} - \mathbf{X} \boldsymbol{\beta} \|^2 + \lambda \| \boldsymbol{\beta} \|_1$ |

## **Optimization**

### Estimator Assumption

> What properties must a system satisfy in order to apply simple linear regression?
> 

> Do these preconditions change depending on the estimators used? Yes, but they are a combinations of this.
> 

> [](https://app.notion.com/p/248c0f5171ec80618455e4de9574f748?pvs=21),[(Statistic) Estimator](statistic-estimator.md),[Homoscedasticity](homoscedasticity.md)
> 

| **Property** | **Description** |
| --- | --- |
| **Linearity** | The relationship between the independent variable $x$ and dependent variable $y$ is linear. |
| **Independence** | Observations are independent; residuals/errors are uncorrelated across data points. |
| **Homoscedasticity** | Constant variance of residuals across all values of $x$; no systematic pattern in error spread. |
| **Normality of Errors** | Residuals (differences between observed and predicted values) are approximately normally distributed. |
| **No Influential Outliers** | Absence of extreme values that disproportionately affect the regression fit. |

### Estimator

> aka **Learner - Optimizer**.
> 

> Note: What assumptions does the estimator make about the data? Alternatively, what properties must the data satisfy for the estimator to be valid or applicable?
> 

| **Name** | **Description** | **Formula** | **Assumptions** |
| --- | --- | --- | --- |
| **Ordinary Least Squares (OLS)** | Analytical solution that minimizes the MSE; closed-form for linear regression. | $\boldsymbol{\hat{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}$ | Linearity, independence, homoscedasticity, no multicollinearity, normal errors (for inference), etc. |
| **Gradient Descent (GD)** | Iterative optimization method using full dataset gradients to minimize loss. | $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \eta \nabla_\theta \mathcal{L}$ | Differentiability of loss, convexity (for global optimum), fixed learning rate, etc. |
| **Stochastic Gradient Descent (SGD)** | Uses one sample at a time for updates; faster per step, more variance. | $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \eta \nabla_\theta \mathcal{L}^{(i)}$ | Same as GD, but also assumes random sampling and small enough learning rate for convergence, etc. |
| **Mini-batch Gradient Descent** | Trades off between GD and SGD by using small batches of data. | $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \eta \nabla_\theta \mathcal{L}^{(B)}$ | Same as GD/SGD; assumes batch size balances variance and convergence speed |
| **Momentum** | Accelerates convergence by accumulating a velocity vector in gradient direction. | $v_t = \gamma v_{t-1} + \eta \nabla_\theta \mathcal{L},  \boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - v_t$ | Same as GD; assumes consistent gradient direction; $\gamma ∈ [0,1)$, etc. |
| **Nesterov Accelerated Gradient (NAG)** | Improves momentum by looking ahead before computing gradient. | $v_t = \gamma v_{t-1} + \eta \nabla_\theta \mathcal{L}(\boldsymbol{\theta} - \gamma v_{t-1}),  \boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - v_t$ | Same as Momentum; assumes smooth loss surface, etc. |
| **Adagrad** | Adapts learning rate for each parameter using sum of historical gradients. | … | Assumes sparse features; learning rate becomes very small over time, etc. |
| **RMSProp** | Variant of Adagrad with exponential decay of gradient history. | … | Assumes non-stationary objectives; suitable for online and non-convex problems, etc. |
| **Adam** | Combines Momentum and RMSProp; popular adaptive optimizer. | … | Assumes differentiability; robust to noisy gradients; performs well in practice under wide conditions, etc. |

## Evaluation

> See more in [Loss Function](../optimization/loss-function.md).
> 

| **Name** | **Description** | **Formula** |
| --- | --- | --- |
| **Mean Squared Error (MSE)** | Penalizes large errors more due to squaring; most common for OLS. | $\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$ |
| **Mean Absolute Error (MAE)** | More robust to outliers; linear penalty. | … |
| **Huber Loss** | Quadratic for small errors, linear for large errors; balances MSE and MAE. | … |
| **Log-Cosh Loss** | Smooth approximation to MAE; less sensitive to outliers than MSE. | $\sum_{i=1}^{n} \log(\cosh(y_i - \hat{y}_i))$ |
| **Quantile Loss** | Used in quantile regression; asymmetric penalty for over- and under-prediction. | $\sum_{i=1}^{n} \rho_\tau(y_i - \hat{y}_i), \quad \rho_\tau(e) = e(\tau - \mathbb{I}\{e < 0\})$ |
| **Squared Log Error (MSLE)** | Penalizes underestimates more than overestimates; useful when values span orders of magnitude. | $\frac{1}{n} \sum_{i=1}^{n} \left( \log(1 + y_i) - \log(1 + \hat{y}_i) \right)^2$ |
| **Tukey’s Biweight Loss** | Redescending M-estimator; ignores very large outliers. | … |
| **Welsch Loss** | Strongly penalizes medium errors; diminishes large ones. | $L(e) = 1 - \exp\left( -\left(\frac{e}{c}\right)^2 \right)$ |
| **Fair Loss** | Similar to Huber but smoother; balances bias and robustness. | … |
| **Cauchy Loss** | Heavy-tailed distribution penalty; robust to outliers. | $L(e) = \frac{1}{2} c^2 \log\left(1 + \left( \frac{e}{c} \right)^2 \right)$ |

## Regularization

> Regularization is a technique used to **prevent overfitting** by adding a penalty term to the loss function during model training. This penalty discourages overly complex models by constraining or shrinking coefficient estimates, improving generalization on unseen data.
> 

> See more in [**Regularization**](regularization.md).
> 

### Common Regularization Method

| **Method** | **Description** | **Penalty Term** |
| --- | --- | --- |
| **Ridge (L2)** | Adds the sum of squared coefficients as a penalty to the loss function. |  |
| **Lasso (L1)** | Adds the sum of absolute coefficients, promoting sparsity (feature selection). |  |
| **Elastic Net** | Combines L1 and L2 penalties to balance between Ridge and Lasso effects. |  |

### How Regularization Work

- The parameter λ\lambda (regularization strength) controls the amount of shrinkage:
    - $\lambda = 0$ → No regularization (equivalent to ordinary least squares).
    - Larger $\lambda$ → More shrinkage, coefficients move closer to zero.
- Regularization helps improve **model stability** and **prediction accuracy**, especially when dealing with noisy or high-dimensional data.

## 🌱 Genesis

> **Gauss** minimized the sum of squared errors explicitly by **taking partial derivatives** with respect to each parameter.
> 

> **Vectors** were formalized in physics (Gibbs, 1880s) and then abstracted in mathematics.
> 

| Year | Contributor | Contribution |
| --- | --- | --- |
| 1795 | **Gauss** (claimed) | Used least squares for planetary orbits |
| 1805 | **Legendre** | First published method of least squares |
| 1809 | **Gauss** | Theoretical foundation in celestial mechanics |
| 1821 | **Gauss-Markov** | Formalized properties (BLUE) |
| 1920s | **Fisher** | Linked to maximum likelihood and inference |

## ⚠️ Limits of Linear Regression

> 

| **Limitation** | **Description** | **Implication** | **Remedy** |
| --- | --- | --- | --- |
| **Linearity Assumption** | Assumes output is a linear function of inputs. | Fails to capture nonlinear relationships. | Use **polynomial regression**, **interaction terms**, or **nonlinear models** (e.g., trees, kernels). |
| **Outlier Sensitivity** | Squared error loss gives high weight to outliers. | Model can be distorted by anomalous points. | Use **robust regression** (e.g., Huber, RANSAC), or **outlier removal**. |
| **Multicollinearity** | Predictors are highly correlated. | Estimates become unstable and hard to interpret. | Apply **Ridge regression**, **PCA**, or **drop/recombine correlated features**. |
| **Homoscedasticity** | Assumes constant variance in residuals. | Inefficient estimates, invalid inference. | Use **weighted least squares** or **heteroscedasticity-consistent errors** (e.g., White's correction). |
| **Independence of Errors** | Assumes residuals are uncorrelated. | Biased standard errors and incorrect inference. | Use **time series models** (e.g., ARIMA), **clustered standard errors**, or **GLS**. |
| **Gaussian Errors (for inference)** | Errors should be normal for valid p-values and confidence intervals. | Inference becomes unreliable. | Use **bootstrapping**, **robust standard errors**, or **nonparametric methods**. |
| **Limited Expressiveness** | Single linear model over all data. | Can't model complex or localized patterns. | Use **decision trees**, **splines**, **kernel methods**, or **neural networks**. |
| **No Feature Selection** | Includes all predictors by default. | Reduces interpretability and may degrade accuracy. | Use **Lasso**, **Elastic Net**, or **feature selection algorithms**. |
| **Overfitting in High Dimensions** | When number of features is close to or exceeds number of samples. | Poor generalization to new data. | Use **regularization** (Lasso/Ridge), **dimensionality reduction**, or **cross-validation**. |
| **Global Model Behavior** | Coefficients apply uniformly across input space. | Can't adapt to heterogeneous data regions. | Use **local regression (e.g., LOESS)** or **model ensembles** with regional specialization. |

## References

- https://en.wikipedia.org/wiki/Linear_regression
- https://en.wikipedia.org/wiki/Simple_linear_regression
- [Hyperplane](../mathematical/hyperplane.md)
- https://github.com/dbremont/algorithms/tree/main/om
- https://en.wikipedia.org/wiki/Least_squares
- https://stats.stackexchange.com/questions/46151/how-to-derive-the-least-square-estimator-for-multiple-linear-regression
- https://economictheoryblog.com/2015/02/19/ols_estimator/
- https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem
- [(Statistic) Estimator](statistic-estimator.md)
- https://archive.org/details/bub_gb_ORUOAAAAQAAJs conicis solem ambientium
- https://archive.org/details/nouvellesmthode00legegoog
- https://arxiv.org/abs/2203.01425
- https://news.ycombinator.com/item?id=43895890
- https://lindeloev.github.io/tests-as-linear/
- https://news.ycombinator.com/item?id=12254098
- https://en.wikipedia.org/wiki/Frisch%E2%80%93Waugh%E2%80%93Lovell_theorem
- https://news.ycombinator.com/item?id=12254098
- [Covariance](covariance.md)
- [Covariance Matrix](../mathematical/covariance-matrix.md)
- 
- [Backpropagation](../optimization/backpropagation.md)
- [Gradient Descent (GD)](../optimization/gradient-descent-gd.md)
- [**Stochastic Gradient Descent (SGD)**](../optimization/stochastic-gradient-descent-sgd.md)
- [(Statistic) Estimator](statistic-estimator.md)
- [Exploratory Data Analysis (EDA)](../exploratory-data-analysis-eda.md)
