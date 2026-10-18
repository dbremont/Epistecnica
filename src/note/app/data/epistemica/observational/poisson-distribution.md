---
tags: [continous]
---

# Poisson Distribution


> Models the number of events occurring in a fixed interval of time or space.
> 

## Formulation

The **Poisson distribution** is a **discrete probability distribution** that describes the number of times an event occurs in a fixed interval of time, space, or volume — **given that**:

1. Events occur **independently**.
2. The **average rate** (λ, lambda) of occurrence is **constant**.
3. Two events **cannot** occur at exactly the same instant (events are **singular**).

## **Probability Mass Function (PMF)**

For a Poisson random variable $X \sim \text{Poisson}(\lambda)$: $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \qquad k = 0, 1, 2, \dots$

- $\lambda > 0$ is the **expected number of events** in the interval.
- $k$ is the **observed count** of events.

## Operator

- **Mean:** $\mathbb{E}[X] = \lambda$
- **Variance:** $\text{Var}(X) = \lambda$
- **Standard deviation:** $\sqrt{\lambda}$

## **Use**

- Number of calls at a call center per hour.
- Number of emails received per day.
- Number of decay events from a radioactive source in a given time.
- Number of misprints per page in a book.

## **Relation**

**Relation to Other Distributions:**

- **Binomial approximation:** $\text{Binomial}(n,p) \approx \text{Poisson}(\lambda = np)$
when $n$ is large and $p$ is small.
- **Exponential connection:** The **inter-arrival times** between Poisson events follow the **Exponential distribution** with rate parameter $\lambda$.

## References

- https://en.wikipedia.org/wiki/Poisson_distribution
- [‣](https://app.notion.com/p/1255314a56398062bf9dd9049fb1c396?pvs=21)
