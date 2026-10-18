---
tags: [framework, state-estimation]
---

# State Estimation

 : Filtration (Filtration%2015fc0f5171ec8000a310e17a381d06de.md), Filter (Filter%203acc0f5171ec80c5abc8e5e734d3791f.md)

> In this note we will explore the general concept of **“State Estimation”**, a unifying concept that appears across diverse fields such as control theory, signal processing, statistics, robotics, and artificial intelligence. At its core, state estimation concerns the problem of **inferring the underlying condition or configuration of a system**—its “state”—based on **observations, measurements, and prior knowledge**, which may be noisy, incomplete, or indirect.
> 

> **Note:** State Estimation is not a field itself, but rather a **task or problem statement** that arises in many disciplines. It refers to the **objective of inferring the hidden or internal state of a system from available observations**, often under uncertainty, noise, or partial information.
> 

> **Filtering** is the **task** of estimating an unobserved variable (often called the "state") using only **available observations up to the current time**.
> 

> Given a system with **latent (hidden) states** evolving over **time** and **observations** that are noisy functions of these states, the **Filter Problem** is to estimate the current state of the system using all past and present observations.
> 

## 🗂️ Index

## Formulation

> **Goal:** Given a system with hidden or latent states $x_t$ and observable outputs $y_t$, estimate $x_t$ as accurately as possible using **available observations**, possibly prior knowledge, and a **model of system dynamics**.
> 

> The **state estimation problem** is essentially the **inverse problem of reconstructing hidden states from observable data** while accounting for **system dynamics and uncertainty**. It unifies filters, observers, Bayesian inference, and modern machine learning approaches under a single conceptual framework.
> 

### **System Dynamics (State Evolution)**

> $x_{t+1} = f(x_t, u_t, w_t)$
> 
- $x_t$ – system state at time $t$
- $u_t$ – control input or exogenous input
- $w_t$ – process noise or uncertainty
- $f(\cdot)$ – state transition function (may be linear or nonlinear)

### **Observation Model (Measurements)**

> $y_t = h(x_t, v_t)$
> 
- $y_t$ – observable output
- $v_t$ – measurement noise
- $h(\cdot)$ – measurement function

### **Estimation Objective**

> Compute an estimate $\hat{x}t$ *of $x_t$ given observations $y{1:t}$* (all data up to time $t$), optionally inputs $u_{1:t}$, by minimizing some notion of **error or uncertainty**:
> 
- **Deterministic formulation:** $\hat{x}t = \arg\min_x \|y{1:t} - h(x)\|$
- **Probabilistic formulation:** $\hat{x}t = \mathbb{E}[x_t \mid y{1:t}]$ or $\hat{x}t = \arg\max{x_t} p(x_t \mid y_{1:t})$

### **Assumptions**

- The system may be **linear or nonlinear**, **time-invariant or time-varying**.
- Noise may be **Gaussian, non-Gaussian, or unknown**.
- Observations may be **complete or partial**, **continuous or discrete**.

## Technique

> A **State Estimation technique** is a **systematic method or algorithm designed to infer the internal state of a system from observed data, measurements, or signals, often in the presence of uncertainty, noise, or incomplete information**.
> 

> It provides a **mapping from observations and prior knowledge to an internal representation** of the system, enabling prediction, tracking, control, or decision-making. Depending on the context, state estimation techniques may be **deterministic or probabilistic**, **linear or nonlinear**, and can range from classical filters like the **Kalman filter** to more general frameworks like **particle filters, Bayesian inference, or energy-based models**.
> 

| **Technique** | **Description** | **Model Representation** | **Model Evaluation** | **Optimization** |
| --- | --- | --- | --- | --- |
| **Kalman Filter** | Optimal linear estimator for systems with Gaussian noise; recursively estimates state using prediction and update steps | Linear dynamical system: $x_{t+1} = A x_t + B u_t + w_t$, $y_t = C x_t + v_t$ | Prediction error covariance, RMSE between estimated and true states | Model parameters (A, B, C, noise covariances) are often given or estimated from data |
| **Extended Kalman Filter (EKF)** | Nonlinear extension of Kalman filter using first-order Taylor expansion | Nonlinear dynamics: $x_{t+1} = f(x_t,u_t)+w_t$, $y_t = h(x_t)+v_t$ | Linearization error, estimation error metrics | Requires Jacobians of f and h; parameters tuned or learned from data |
| **Unscented Kalman Filter (UKF)** | Uses deterministic sampling (sigma points) to handle nonlinearities more accurately than EKF | Same as EKF but uses unscented transform | State estimation error, covariance consistency | Parameters and process/noise covariances tuned via data or EM-like methods |
| **Particle Filter** | Sequential Monte Carlo method representing posterior distribution with weighted samples |  |  | Effective sample size, estimation variance |
| **Bayesian Filtering / Recursive Bayes** | General probabilistic framework for updating belief about state |  |  | KL divergence, likelihood of observations |
| **Energy-Based Models (EBM) for State Estimation** | Models state as minimizer of an energy function encoding observations and dynamics | Energy function $E(x; y)$, posterior proportional to $e^{-E(x;y)}$ | Loss on reconstructed state, likelihood under energy model | Gradient-based optimization, contrastive divergence, or variational approaches |
| **Observer Design (Control Theory)** | Constructs a dynamical system that asymptotically tracks true state | Luenberger observer: $\dot{\hat{x}} = A \hat{x} + Bu + L(y - C \hat{x})$ | Convergence rate, estimation error | Observer gain L designed via pole placement or optimization |

## Use

| Domain | Use Case | Typical Filters |
| --- | --- | --- |
| 🔧 **Control** | Estimate position, velocity, etc. from noisy sensors; used in SLAM and navigation | Kalman Filter, EKF, UKF |
| 🎧 **Signal Processing** | Denoising, signal reconstruction, extract true signal from noise | Kalman Filter, Wiener Filter |
| 🧬 **Computational Biology** | Infer gene regulatory states, model DNA/protein sequences | Hidden Markov Models (HMMs), Particle Filters |
| 🧠 **Neuroscience** | Decode neural activity, estimate cognitive states from EEG/fMRI | Kalman Filter, Particle Filters |
| 📈 **Finance (Econometrics)** | Infer latent volatility from price data, track economic indicators | Stochastic Volatility Models, Dynamic Factor Models |
| 🤖 **Machine Learning** | Learn dynamics from data, model time series, approximate filtering | RNNs, LSTMs, KVAE, Deep State-Space Models |

## References

- [Latent Model](latent-model.md)
- [**Mixture Model**](mixture-model.md)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [General Topic Note Template](https://app.notion.com/p/General-Topic-Note-Template-1cec0f5171ec801e86e6c894702cfe23?pvs=21)
- https://en.wikipedia.org/wiki/State_observer
- https://en.wikipedia.org/wiki/Filter_(signal_processing)
- https://en.wikipedia.org/wiki/Filtering_problem_(stochastic_processes)
