# Exponential Distribution


> The exponential distribution is a continuous probability distribution that describes the time between events in a **Poisson process** — a process in which events occur continuously and independently at a constant average rate.
> 

## Characterization

### **Probability Density Function (PDF)**

$f(x; \lambda) =
\begin{cases} 
\lambda e^{-\lambda x}, & x \ge 0, \\
0, & x < 0
\end{cases}$

- $\lambda > 0$ is the **rate parameter** (average number of events per unit time).
- $x$ is the random variable (time between events).

### **Cumulative Distribution Function (CDF)**

$F(x; \lambda) = P(X \le x) = 1 - e^{-\lambda x}, \quad x \ge 0$

## **Property**

1. **Mean (Expected Value):**  $E[X] = \frac{1}{\lambda}$
2. **Variance:**  $Var(X) = \frac{1}{\lambda^2}$
3. **Memoryless Property:**  $P(X > s + t \mid X > s) = P(X > t)$

## Use

- Time until a radioactive particle decays.
- Time between arrivals in a queue (e.g., customers at a store, calls at a call center).
- Lifetime of electronic components or machinery.

## Case Study

> A call center wants to model the **time between incoming customer calls** to better staff operators. Historical data suggests that calls arrive **randomly and independently**, at an average rate of **12 calls per hour**.
> 

> 

## Relation

| **Distribution** | **Relationship with Exponential** |
| --- | --- |
| **Poisson** | Time between events in a Poisson process is exponential |
| **Gamma** | Exponential is Gamma with shape $\alpha = 1$ |
| **Erlang** | Exponential is Erlang with $k = 1$ |
| **Weibull** | Exponential is Weibull with shape $k = 1$ |
| **Geometric** | Discrete analogue |
| **Uniform** | Exponential as a transformation of Uniform |
| **Minimum of i.i.d exponentials** | Minimum is exponential |
| **Beta** | Via order statistics |

## References

- https://en.wikipedia.org/wiki/Exponential_distribution
