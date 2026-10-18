---
tags: [probability]
---

# Moment-Generating Function (MGF)


> The **moment-generating function** of a random variable (X) is a function $M_X(t)$ that **encodes all the moments of (X)**.
> 

## Formulation

It is defined as: $M_X(t) = \mathbb{E}[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} , dF_X(x)$

where:

- $t \in \mathbb{R}$ (or a subset where the expectation exists),
- $F_X(x)$ is the cumulative distribution function of (X),
- $\mathbb{E}[\cdot]$ denotes expectation.

## Property

> Note: I Need to Proof This.
> 
1. **Existence at $t=0$** : $M_X(0) = 1$ The MGF is always defined at $t = 0$.
2. **Uniqueness** If two random variables have the same MGF (in an open interval around 0), they have the **same distribution**.
3. **MGF of sums of independent variables** If $X$ and $Y$ are independent: $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$
4. **Scaling and shifts** If $a$ and $b$ are constants: $M_{aX + b}(t) = e^{bt} M_X(at)$
5. **Non-negative** $M_X(t) \ge 0 \quad \text{for real } t$
6. **Connection to cumulants** The logarithm of the MGF is the **cumulant generating function**: $K_X(t) = \log M_X(t)$
7. **Moment extraction:** The (n)-th moment of (X) is obtained by differentiating $M_X(t)$ (n) times at ($t = 0$): $\mathbb{E}[X^n] = M_X^{(n)}(0)$
8. **Sum of independent variables:** For independent (X) and (Y),  $M_{X+Y}(t) = M_X(t) M_Y(t)$, which simplifies analysis of sums.

## Use

| **Use** | **Description** |
| --- | --- |
| **Generate moments** | Obtain mean, variance, higher moments by differentiation |
| **Characterize distribution** | Two RVs with same MGF have the same distribution |
| **Sum of independents** | MGF of sum = product of MGFs of independent variables |
| **Limit theorems** | Useful in proofs of CLT and convergence results |
| **Probability calculations** | Simplifies complex expectation calculations |
| **Cumulant analysis** | Log MGF generates cumulants for advanced modeling |

## References

- https://en.wikipedia.org/wiki/Moment-generating_function
