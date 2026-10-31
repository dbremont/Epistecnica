---
tags: [probability]
---

# Diffusion Process

 : Diffusion Model (Diffusion%20Model%2019e73600d6d34e968766695794161eeb.md)

> ..
> 

QA:

- Why the name diffusion?
- How to simulate the diffusion of particle using the **Fokker-Planck Equation? [How to simulate the diffusion of particles using the Fokker-Planck Equation?](https://app.notion.com/p/How-to-simulate-the-diffusion-of-particles-using-the-Fokker-Planck-Equation-1bcc0f5171ec80de8ad6d8bd447aeb4f?pvs=21)**

## Mathematical Representation

> Note: This is a general  form that can model many diffusion processes; but diffusion proceses are a  class of stochastic proceses; with many equations that models them.
> 

> The **mathematical representation** of a **diffusion process** is typically given by a **stochastic differential equation (SDE)**. Here is the general form:  $dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t$
> 

### **Explanation of Terms**

1. **$X_t$:** The state of the process at time $t$. This could represent a particle's position, a financial asset's price, or any other quantity evolving over time.
2. **$\mu(X_t, t)$:** The **drift term**, which represents the deterministic part of the process. It describes the expected or average rate of change of $X_t$ over time.
3. **$\sigma(X_t, t)$:** The **diffusion term** (or volatility term), which represents the random fluctuations in the process. It scales the randomness introduced by Brownian motion.
4. **$dW_t$:**
    - The increment of a **Brownian motion** (or Wiener process), which models the random noise. Brownian motion has the following properties:
        - $W_t$ is continuous almost surely.
        - $W_t$ has independent increments.
        - $W_t \sim \mathcal{N}(0, t)$, meaning it is normally distributed with mean 0 and variance $t$.
5. **$dt$:** An infinitesimal time increment.

### **Integral Form**

> The SDE can also be written in its integral form: 
$X_t = X_0 + \int_0^t \mu(X_s, s) \, ds + \int_0^t \sigma(X_s, s) \, dW_s$
> 
- **$X_0$:** The initial value of the process at time \( t = 0 \).
- **$\int_0^t \mu(X_s, s) \, ds$:** The cumulative effect of the drift over time.
- **$\int_0^t \sigma(X_s, s) \, dW_s$:** The cumulative effect of the random fluctuations (stochastic integral with respect to Brownian motion).

## Uses

### **Geometric Brownian Motion (GBM)**

- **Description:** Models exponential growth or decay with random fluctuations (e.g., stock prices).
- **SDE:**  $dX_t = \mu X_t \, dt + \sigma X_t \, dW_t$
- **Applications:** Financial modeling, population dynamics.

### **Ornstein-Uhlenbeck Process**

- **Description:** Models mean-reverting processes (e.g., particle motion under friction, interest rates).
- **SDE:**  $dX_t = \theta (\mu - X_t) \, dt + \sigma \, dW_t$
- **Applications:** Physics, finance, biology.

### **Vasicek Model**

- **Description:** A specific type of Ornstein-Uhlenbeck process used to model interest rates.
- **SDE:** $dX_t = a(b - X_t) \, dt + \sigma \, dW_t$
- **Applications:** Financial mathematics.

### **Cox-Ingersoll-Ross (CIR) Model**

- **Description:** Models interest rates with a square-root diffusion term to ensure non-negativity.
- **SDE:** $dX_t = a(b - X_t) \, dt + \sigma \sqrt{X_t} \, dW_t$
- **Applications:** Financial mathematics.

### **Brownian Motion with Drift**

- **Description:** Models linear growth or decay with random fluctuations.
- **SDE:** $dX_t = \mu \, dt + \sigma \, dW_t$
- **Applications:** Physics, finance.

### **Stochastic Logistic Growth**

- **Description:** Models population growth with a carrying capacity and random fluctuations.
- **SDE:** $dX_t = r X_t \left(1 - \frac{X_t}{K}\right) \, dt + \sigma X_t \, dW_t$
- **Applications:** Ecology, biology.

### **Black-Scholes Model**

- **Description:** Models the price of financial derivatives.
- **SDE:** $dX_t = \mu X_t \, dt + \sigma X_t \, dW_t$
- **Applications:** Financial mathematics.

### **Stochastic Heat Equation**

- **Description:** Models heat diffusion with random fluctuations.
- **SDE:** $dX_t = \alpha \nabla^2 X_t \, dt + \sigma \, dW_t$
- **Applications:** Physics, engineering.

### **Stochastic FitzHugh-Nagumo Model**

- **Description:** Models neuron activity with random fluctuations.
- **SDE:**
    - $dX_t = \left(X_t - \frac{X_t^3}{3} - Y_t\right) \, dt + \sigma \, dW_t$
    - $dY_t = \epsilon (X_t + a - b Y_t) \, dt + \sigma \, dW_t$
- **Applications:** Neuroscience.

### **Stochastic Chemical Kinetics**

- **Description:** Models chemical reactions with random fluctuations.
- **SDE:**  $dX_t = \mu(X_t) \, dt + \sigma(X_t) \, dW_t$
- **Applications:** Chemistry, biochemistry.

### **Stochastic Volatility Models**

- **Description:** Models financial asset prices with random volatility.
- **SDE:**
    - $dX_t = \mu X_t \, dt + \sigma_t X_t \, dW_t$
    - $d\sigma_t = \kappa (\theta - \sigma_t) \, dt + \xi \sigma_t \, dW_t^\sigma$
- **Applications:** Financial mathematics.

## Why the name diffusion?

> In physics, diffusion describes how particles (e.g., molecules) spread  out from regions of high concentration to regions of low concentration 
due to random motion. This random motion is mathematically modeled by **Brownian motion** (or Wiener process), which is a continuous-time stochastic process with continuous but highly irregular trajectories.
> 

> A **diffusion process** in probability theory generalizes  this idea. It describes how a quantity (e.g., the position of a 
particle) evolves over time in a way that is continuous but subject to  random fluctuations, much like physical diffusion.
> 

> The process describes the **spreading of probability distributions** over time, much like how particles spread in physical diffusion.
> 

## References

- https://en.wikipedia.org/wiki/Diffusion_process
- [Lecture 12: Diffusion processes](http://www.stat.t.u-tokyo.ac.jp/~sei/lec/170706note.pdf)
- https://encyclopediaofmath.org/wiki/Diffusion_process
-
