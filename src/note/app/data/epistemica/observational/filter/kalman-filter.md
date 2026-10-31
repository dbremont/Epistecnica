---
tags: [learning-system, state-estimation]
---

# Kalman Filter

 : Filter (Filter%203acc0f5171ec80c5abc8e5e734d3791f.md)

> This note is about the **Kalman filter** — a method for **estimating the state of a system**. It was introduced by Rudolf E. Kalman in his 1960 paper "A New Approach to Linear Filtering and Prediction Problems." The filter is designed for **linear systems with Gaussian noise** and gives the best estimate by **minimizing the average error**.
> 

## 🗂️ Index

## ❓ QA

- …

## **✅ Note Quality Evaluation**

> (**⭐⭐⭐⭐⭐**)  → Does this note adhere to the prototype structure? If it is incomplete, in what way? See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21).
> 

## 📘 Breviarium

> A comprehensive exploration of the topic.
> 

> **Nucleus (🧬)** → Deepest Essence (What is the deepest essence?)
> 

> **Telos (🎯)** → Intent (What is it for? Toward what end is it directed?)
> 

> **Techne (🛠️)** → Function / Used (By what craft or process is it made to work?)
> 

> **Idoneitas (📏)** → Suitability (How well is it fitted for its purpose?)
> 

> **Limites** (🚧) → Limits (What are its boundaries? What constraints define its operation?)
> 

> **Contextus (🌐)** → Context (What is the historical, cultural, or situational context in which this study occurs?)
> 

## 🧠 Autovaluatio

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

## 📝 Formulation

| **Formulation** | **Domain** | **Key Characteristics** | **Typical Applications** |
| --- | --- | --- | --- |
| **Linear Kalman Filter (LKF)** | Linear / Gaussian | Assumes linear system and Gaussian noise; exact closed-form solution | Navigation, control systems |
| **Extended Kalman Filter (EKF)** | Nonlinear (approximate) | First-order linearization via Taylor expansion | Robotics, aerospace, GPS |
| **Unscented Kalman Filter (UKF)** | Nonlinear (approximate) | Uses sigma points for better approximation of mean and covariance | Nonlinear estimation, target tracking |
| **Information Filter (IF)** | Linear / Sparse systems | Uses inverse covariance (information form); better for sparse/large systems | Sensor networks, SLAM |
| **Distributed Kalman Filter** | Multi-agent / Decentralized | Each node runs a filter and exchanges estimates | Sensor networks, collaborative robotics |
| **Ensemble Kalman Filter (EnKF)** | Large-scale / Stochastic | Uses Monte Carlo sample ensemble to estimate state and covariance | Weather modeling, fluid dynamics |
| **Square Root Kalman Filter** | Linear / Numerical | Propagates square roots of covariance (e.g., Cholesky factor) | Precision-critical systems, numerical computing |
| **Time-Varying Kalman Filter** | Time-dependent systems | Allows dynamics and noise models to change over time | Adaptive signal processing |
| **Adaptive Kalman Filter** | Learning / Online | Learns or updates noise covariances QQ and RR from data | Time-varying or uncertain environments |
| **H-infinity Filter ($\mathcal{H}_\infty$)** | Robust / Worst-case | Minimizes worst-case estimation error, not assuming noise is Gaussian | Robust control, uncertain environments |
| **Robust Kalman Filter** | Robust / Non-Gaussian | Handles outliers or non-Gaussian noise; may include uncertainty bounds | Finance, autonomous vehicles |
| **Continuous-time Kalman Filter (Kalman–Bucy)** | Linear / Continuous | Continuous-time version of LKF; used in differential systems | Theoretical control, physics simulations |

## 🧾 Linear Kalman Filter (LKF)

> aka. Original Formulation.
> 

### 📝 Formulation

The system is described by the following **discrete-time linear stochastic model**:

**State Transition Equation**: $\mathbf{x}_k = \mathbf{A}_{k-1} \mathbf{x}_{k-1} + \mathbf{B}_{k-1} \mathbf{u}_{k-1} + \mathbf{w}_{k-1}$

- $\mathbf{x}_k$: state vector at time step $k$
- $\mathbf{A}_{k-1}$: state transition matrix
- $\mathbf{B}_{k-1}$: control input matrix
- $\mathbf{u}_{k-1}$: control vector
- $\mathbf{w}_{k-1}$: process noise (zero-mean Gaussian with covariance $\mathbf{Q}_{k-1})$

**Observation Equation**:  $\mathbf{z}_k = \mathbf{H}_k \mathbf{x}_k + \mathbf{v}_k$

- $\mathbf{z}_k$: measurement vector at time step $k$
- $\mathbf{H}_k$: observation matrix
- $\mathbf{v}_k$: measurement noise (zero-mean Gaussian with covariance $\mathbf{R}_k)$

### 🔁 **Kalman Filter Recursion**

> Each time step consists of a **predict** and an **update** phase.
> 

**Prediction (Time Update)**

- **Predicted State Estimate**: $\hat{\mathbf{x}}_{k|k-1} = \mathbf{A}_{k-1} \hat{\mathbf{x}}_{k-1|k-1} + \mathbf{B}_{k-1} \mathbf{u}_{k-1}$
- **Predicted Covariance**: $\mathbf{P}_{k|k-1} = \mathbf{A}_{k-1} \mathbf{P}_{k-1|k-1} \mathbf{A}_{k-1}^\top + \mathbf{Q}_{k-1}$

**Update (Measurement Update)**

- **Innovation (Residual)**: $\mathbf{y}_k = \mathbf{z}_k - \mathbf{H}_k \hat{\mathbf{x}}_{k|k-1}$
- **Innovation Covariance**: $\mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^\top + \mathbf{R}_k$
- **Kalman Gain**: $\mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}_k^\top \mathbf{S}_k^{-1}$
- **Updated State Estimate**: $\hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k \mathbf{y}_k$
- **Updated Covariance**: $\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \mathbf{P}_{k|k-1}$

### State Covariance Matrix (P)

> It tracks the uncertainty in the estimated state.
> 

> 

### **Process Noise Covariance (Q)**

> Models uncertainty in the **system dynamics** or model itself.
> 

### **Measurement Noise Covariance (R)**

> Models uncertainty in the **sensor or measurement system**.
> 

## 📚 References

- [General Topic Note Template](https://app.notion.com/p/General-Topic-Note-Template-1cec0f5171ec801e86e6c894702cfe23?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- …
- https://en.wikipedia.org/wiki/Kalman_filter
- [Covariance Matrix](../mathematical/covariance-matrix.md)
- https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/
- https://news.ycombinator.com/item?id=39343746
- https://python.quantecon.org/kalman.html
- [‣](https://app.notion.com/p/1cf598edb79080efb4dbfcaa61ac8436?pvs=21)
- [‣](https://app.notion.com/p/1cf598edb79080b18a9dc28f1afe831b?pvs=21)
- [‣](https://app.notion.com/p/1cf598edb79080d2a0fbd2415e79da4b?pvs=21)
- [https://ntrs.nasa.gov/api/citations/19860003843/downloads/19860003843.pdf](https://ntrs.nasa.gov/api/citations/19860003843/downloads/19860003843.pdf)
