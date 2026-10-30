---
tags: [framework]
---

# State Estimation


> Etymologically, a "filter" is something you pass a fluid through, especially to purify it. In signal processing, a filter became a device or operation you pass a signal through, especially to remove what is (for your purposes) noise or irrelevancies, thereby purifying it. Its meaning (in this sense) thus diverged: one the one hand, to general transformations of signals, such as preserving their high-frequency ("high-pass") or low-frequency ("low-pass") components; on the other hand, to trying to estimating some underlying true value or state, corrupted by distortion and noise.
> 

> Estimate the actual state of a system based on noisy or incomplete observations using techniques like Kalman filters or particle filters.
> 

> **State estimation** is the process of determining the internal state of a dynamic system based on observed measurements, often in the presence of noise and uncertainty.
> 

## State Estimation Techniques

> 

| Method | **Description** | **System Type** | **Key Features** | **Use Cases** |
| --- | --- | --- | --- | --- |
| **Kalman Filter** | Linear filter that provides optimal estimates of system states given Gaussian noise. | Linear, Time-varying | Recursive, real-time state estimation, minimal computational cost | Tracking, navigation, control systems, finance |
| **Extended Kalman Filter (EKF)** | Generalization of the Kalman Filter to nonlinear systems using first-order linearization. | Nonlinear | Linearizes around current estimate, applies Kalman filter | Robotics, autonomous vehicles, nonlinear systems |
| **Unscented Kalman Filter (UKF)** | Nonlinear filter that approximates mean and covariance more accurately than EKF using sigma points. | Nonlinear | Uses unscented transform to better handle nonlinearity | Aerospace, nonlinear dynamics, satellite tracking |
| **Particle Filter** | Nonlinear, non-Gaussian filter using Monte Carlo simulations to represent the state distribution. | Nonlinear, Non-Gaussian | Uses particles (samples) to represent probability distribution | Object tracking, AI, complex nonlinear models |
| **Information Filter** | Kalman filter variant that operates in information form (inverse covariance) instead of covariance. | Linear, Time-varying | Efficient for sparse matrices, works well in distributed systems | Large-scale sensor networks, decentralized filtering |
| **Rauch-Tung-Striebel Smoother** | Smoothing algorithm based on the Kalman filter, designed to estimate past states more accurately. | Linear, Time-varying | Backward pass through data to refine estimates | Post-processing data, smoothing noisy measurements |
| **Moving Horizon Estimation (MHE)** | Optimization-based method that estimates current states by minimizing a cost function over a time window. | Nonlinear, Constrained systems | Incorporates constraints, robust against model mismatch | Model predictive control, chemical processes |
| **H∞ Filter** | Robust filter designed to minimize the worst-case estimation error under uncertain noise conditions. | Linear, Nonlinear | Robust to model uncertainties, focuses on worst-case performance | Control systems, robust state estimation in noisy environments |
| **Kalman-Bucy Filter** | Continuous-time version of the Kalman filter used for linear continuous-time systems. | Continuous-time linear systems | Continuous state update, ideal for analog or time-continuous systems | Electrical circuits, continuous processes |
| **Interacting Multiple Model (IMM) Filter** | Combines multiple Kalman filters for systems with different modes of operation. | Switching systems, Multi-modal systems | Switches between models based on likelihood of operation mode | Hybrid systems, target tracking with mode switching |
| **Finite Impulse Response (FIR) Filter** | State estimator that does not rely on the recursive nature of the Kalman filter, using a sliding window. | Linear, Time-invariant | No dependency on noise covariance, robust in time-varying noise | Time-series prediction, systems with unknown noise properties |
| **Ensemble Kalman Filter (EnKF)** | Ensemble-based approximation of the Kalman filter, often used in high-dimensional systems. | Nonlinear | Uses ensemble of system states to approximate distribution | Weather forecasting, large-scale environmental modeling |
| **Square Root Kalman Filter** | A variant of the Kalman filter that maintains numerical stability by computing square roots of covariance matrices. | Linear, Time-varying | Improves numerical stability in systems with poor conditioning | Systems with high numerical precision requirements |
| **Wiener Filter** | A filter designed for linear systems that minimizes the mean square error between the estimated and true state. | Linear, Time-invariant | Optimal for signal processing in stationary environments | Signal processing, audio and image noise reduction |
| **Covariance Intersection Filter** | A method for fusing information from different sensors without requiring cross-correlation knowledge. | Linear, Nonlinear | Safe fusion of uncertain data, robust to unknown correlations | Sensor fusion, multi-sensor state estimation |
| Maximum a Posteriori (MAP) |  |  |  |  |
| Covariance Intersection (CI) |  |  |  |  |
| Moving Horizon Estimation (MHE) |  |  |  |  |
| Ensemble Kalman Filter (EnKF) |  |  |  |  |
| Moving Average Filter |  |  |  |  |
| Luenberger Observer |  |  |  |  |

## References

- https://www.nature.com/articles/s41586-023-06574-8
- https://www.nature.com/articles/s42005-024-01606-9?fromPaywallRec=false
- https://www.nature.com/articles/s43588-022-00281-6?fromPaywallRec=false
- https://www.nature.com/articles/s42256-022-00575-4?fromPaywallRec=true
- https://en.wikipedia.org/wiki/Filtering_problem_(stochastic_processes)
- https://en.wikipedia.org/wiki/Zakai_equation

[**Kalman Filter**](../observational/kalman-filter.md)

[**Wiener Filter**](../observational/wiener-filter.md)

[**Particle Filter**](../observational/particle-filter.md)

[Dynamical Intelligence](../dynamical-intelligence.md) 

[**System Identification**](system-identification.md) 

[Smoothing](smoothing.md)
