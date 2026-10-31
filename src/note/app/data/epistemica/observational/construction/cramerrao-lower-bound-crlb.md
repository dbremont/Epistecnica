---
tags: [theorem]
---

# Cramér–Rao Lower Bound (CRLB)

 : Fisher Information (Fisher%20Information%204cefa509a9c94f7b912cfbdc477adbec.md), Theory of Statistics (Theory%20of%20Statistics%20272c0f5171ec80ce988eebaba3a61964.md), Relative Efficiency (Relative%20Efficiency%20272c0f5171ec80f39b6dc6ed72cd8f62.md)

> The **Cramér–Rao Lower Bound (CRLB)** is a fundamental result in estimation theory that tells you **how good an unbiased estimator can possibly be**.
> 

### **Definition**

For an unbiased estimator $\hat{\theta}$ of a parameter $\theta$, its variance satisfies: 

$\mathrm{Var}(\hat{\theta}) \geq \frac{1}{\mathcal{I}(\theta)}$ where $\mathcal{I}(\theta)$ is the **Fisher Information**:  $\mathcal{I}(\theta) = \mathbb{E}\!\left[\left(\frac{\partial}{\partial \theta} \ln f(X;\theta)\right)^2\right]$

- $f(X;\theta)$ is the likelihood (or probability density) of the data.
- The right-hand side is the **minimum possible variance** of any unbiased estimator of $\theta$.

## **General Cramér–Rao Lower Bound (CRLB)**

Let:

- $X_1, X_2, \dots, X_n$ be a sample with likelihood $L(\theta; x_1, \dots, x_n)$ or density $f(x; \theta)$, where $\theta \in \Theta \subseteq \mathbb{R}$ is an unknown parameter.
- $g(\theta)$ be a **function of the parameter** $\theta$ that we want to estimate.
- $\hat{g}(X_1, \dots, X_n)$ be an **unbiased estimator** of $g(\theta)$: $\mathbb{E}_\theta[\hat{g}] = g(\theta)$.

If $\hat{g}$ is unbiased for $g(\theta)$,

then its variance satisfies:  $\operatorname{Var}(\hat{g}) \ge \frac{(g'(\theta))^2}{I(\theta)}$

 where $g'(\theta) = \frac{d}{d\theta} g(\theta)$.

## References

- https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93Rao_bound
