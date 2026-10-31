---
tags: [discrete, sequence, specific]
---

# Binomial Coefficient

 : Combinatorics (Combinatorics%20231c0f5171ec8005bd62f206032ece34.md), Combination (Combination%20277c0f5171ec803dafbfe10d1761e4a6.md), Recurrence Equation (Recurrence%20Equation%20122c0f5171ec8029b62aebd9ef062806.md)

> The **binomial coefficient** $\binom{n}{k}$ counts the number of ways to choose $k$ elements from a set of $n$ elements, without regard to order.
> 

## Formulation

> $\binom{n}{k} = \text{number of subsets of size } k \text{ from an } n\text{-element set.}$
> 

> $\binom{n}{k} = \frac{n!}{k!(n-k)!}, \quad \text{for } 0 \leq k \leq n$ and $\binom{n}{k} = 0$ otherwise.
> 

## Pascal Triangle

> Pascal’s Triangle arranges the coefficients $\binom{n}{k}$ in triangular form:
> 

```
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
         ...
```

- Each entry is the sum of the two entries directly above it.
- The $n$-th row corresponds to the coefficients of $(a+b)^n$.

## Relation

| Concept | Role of Binomial Coefficient |
| --- | --- |
| **Binomial Theorem** | Expansion coefficients in $(a+b)^n = \sum\_{k=0}^n \binom{n}{k} a^{n-k} b^k$. |
| **Combination** | $\binom{n}{k}$ counts the number of $k$-element subsets of an $n$-element set. |
| **Branching Process** | Governs probabilities in binomial offspring distributions: $P(X=k)=\binom{n}{k} p^k (1-p)^{n-k}$. |
| **Generating Function** | Coefficients in $(1+x)^n = \sum\_{k=0}^n \binom{n}{k}x^k$; generalizes to $(1+x)^\alpha$. |
| **Convolution** | Identities like $\sum_{k=0}^n \binom{r}{k}\binom{s}{n-k}=\binom{r+s}{n}$ express combinatorial addition laws. |

## References

- https://en.wikipedia.org/wiki/Pascal%27s_triangle
- https://en.wikipedia.org/wiki/Binomial_coefficient
