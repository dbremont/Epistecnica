---
tags: [fixed-structure-parametric-model, learning-system]
---

# Autoregressive Integrated Moving Average (ARIMA) Model


> ARIMA (*Autoregressive Integrated Moving Average*) models a time series by combining **autoregression (AR)**, **differencing (I)**, and **moving averages (MA)**. Below is its formal decomposition, optimization, and connection to stochastic processes.
> 

## **1. Core Components**

An ARIMA model is defined by three parameters:

- **\(p\)**: Order of autoregression (AR).
- **\(d\)**: Degree of differencing (I).
- **\(q\)**: Order of moving average (MA).

Denoted as **ARIMA(\(p, d, q\))**.

---

## **2. Model Equation**

For a time series \(\{y_t\}\), the ARIMA(\(p, d, q\)) model is:

\[
(1 - \sum_{i=1}^p \phi_i L^i) (1 - L)^d y_t = c + (1 + \sum_{j=1}^q \theta_j L^j) \epsilon_t
\]

**Where:**

- \(L\) = Lag operator (\(L y_t = y_{t-1}\)).
- \(\phi_i\) = Autoregressive coefficients (AR).
- \(\theta_j\) = Moving average coefficients (MA).
- \(c\) = Constant (drift term).
- \(\epsilon_t \sim \mathcal{N}(0, \sigma^2)\) = White noise error.

---

### **2.1 Expanded Form**

Applying the operators:

1. **Differencing (I)**:
    
    \[
    \Delta^d y_t = (1 - L)^d y_t \quad \text{(makes series stationary)}
    \]
    
2. **Autoregressive (AR)**:
    
    \[
    y_t = c + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + \epsilon_t
    \]
    
3. **Moving Average (MA)**:
    
    \[
    y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q}
    \]
    

---

## **3. Stationarity Requirement**

- ARIMA assumes **weak stationarity** after differencing:
    - Mean, variance, autocorrelation constant over time.
- **Unit root tests** (e.g., ADF, KPSS) verify stationarity.

---

## **4. Parameter Estimation**

### **Maximum Likelihood Estimation (MLE)**

Minimize the conditional sum of squared errors:

\[
\hat{\phi}, \hat{\theta} = \arg \min_{\phi, \theta} \sum_{t=1}^T \epsilon_t^2
\]

### **Box-Jenkins Method**

1. **Model Identification**:
    - Use ACF/PACF plots to guess \((p, q)\).
2. **Estimation**:
    - Fit \(\phi_i, \theta_j\) via MLE.
3. **Diagnostics**:
    - Check residuals (Ljung-Box test for whiteness).

---

## **5. Special Cases**

| Model | Formula | Use Case |
| --- | --- | --- |
| **AR(\(p\))** | \(y_t = c + \sum_{i=1}^p \phi_i y_{t-i} + \epsilon_t\) | Pure autoregression |
| **MA(\(q\))** | \(y_t = \mu + \epsilon_t + \sum_{j=1}^q \theta_j \epsilon_{t-j}\) | Pure moving average |
| **ARMA(\(p,q\))** | Combines AR(\(p\)) + MA(\(q\)) | Stationary series |
| **Random Walk** | ARIMA(0,1,0): \(\Delta y_t = \epsilon_t\) | Nonstationary trends |

---

## **6. Example: ARIMA(1,1,1)**

\[
(1 - \phi_1 L)(1 - L) y_t = c + (1 + \theta_1 L) \epsilon_t
\]

Expanded:

\[
y_t = c + (1 + \phi_1) y_{t-1} - \phi_1 y_{t-2} + \epsilon_t + \theta_1 \epsilon_{t-1}
\]

---

## **7. Limitations**

- **Linear only**: Cannot capture nonlinear dynamics (e.g., volatility clustering).
- **Fixed structure**: \((p, d, q)\) chosen manually or via grid search.
- **Sensitive to outliers**: Assumes Gaussian noise (\(\epsilon_t \sim \mathcal{N}(0, \sigma^2)\)).

---

## **8. Extensions**

- **SARIMA**: Adds seasonal terms (e.g., ARIMA\((p, d, q)(P, D, Q)_s\)).
- **ARIMAX**: Includes exogenous variables.
- **Fractional ARIMA (FARIMA)**: Allows fractional \(d\) for long memory.

---

### **Summary**

ARIMA is a **parametric, equation-based** model—not a learning system—but its parameter optimization shares similarities with ML. It excels at linear trends/seasonality but lacks the flexibility of modern ML (e.g., LSTMs, GPs).

**Key Reference**:

Box, G. E. P., & Jenkins, G. M. (1970). *Time Series Analysis: Forecasting and Control*.

Would you like a Python implementation walkthrough?

## References

- [Autoregressive Integrated Moving Average (ARIMA) models](https://www.wikiwand.com/en/Autoregressive_integrated_moving_average)
- Box, G. E. P., & Jenkins, G. M. (1970). *Time Series Analysis: Forecasting and Control*.
