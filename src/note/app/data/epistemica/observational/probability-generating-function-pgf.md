---
tags: [probability]
---

# Probability-Generating Function (PGF)


> The PGF is a **power series representation of a discrete probability distribution**, particularly useful for non-negative integer-valued random variables like counts or number of events. It simplifies **computing probabilities, moments, and studying sums of independent variables**.
> 

## Formulation

> The **probability-generating function** of a discrete random variable (X) taking non-negative integer values is a function $G_X(s)$ defined as: $G_X(s) = \mathbb{E}[s^X] = \sum_{k=0}^{\infty} P(X = k) , s^k$
> 

where:

- (s) is a real or complex variable, typically $|s| \le 1)$,
- $P(X = k)$ is the probability that (X) takes the value (k),
- $\mathbb{E}[\cdot]$ denotes expectation.

## Property

1. **Moment extraction:** The derivatives of $G_X(s)$ at (s=1) yield the moments of (X), e.g., $\mathbb{E}[X] = G_X'(1), \quad \text{Var}(X) = G_X''(1) + G_X'(1) - [G_X'(1)]^2$
2. **Sum of independent variables:** For independent discrete random variables (X) and (Y), $G_{X+Y}(s) = G_X(s) , G_Y(s)$
3. **Compact representation:** Encodes the full probability mass function in a single analytic function.

## References

- https://en.wikipedia.org/wiki/Probability-generating_function
