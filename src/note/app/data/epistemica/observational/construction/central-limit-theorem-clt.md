---
tags: [probability, technique]
---

# Central Limit Theorem (CLT)

 : Random Variable (Random%20Variable%20255c0f5171ec80dc95a8d63345182df0.md)

> **Central Limit Theorem** states that, given a sufficiently large number of independent and identically distributed samples from a random variable, the sampling distribution of a suitable estimator (such as the sample mean) will converge to a **normal distribution**, regardless of the original distribution of the random variable.
> 

> **Note:** This concerns the **distribution of the estimator** (e.g., the sample mean), **not** the distribution of the random variable itself.
> 

> **Note**: …
> 

## Formulation

Let $X_1, X_2, \dots, X_n$ be a sequence of independent and identically distributed (i.i.d.) random variables with:

- Mean $\mu = \mathbb{E}[X_i]$
- Finite variance $\sigma^2 = \text{Var}(X_i) < \infty$

Define the **sample mean**:  $\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$   Then, as $n \to \infty$,  the standardized sum $Z_n = \frac{\sqrt{n} (\bar{X}_n - \mu)}{\sigma}$  converges in distribution to a standard normal distribution: $Z_n \xrightarrow{d} N(0,1)$

## **Requirement**

> Which are the requirements (assumptions) in which the theorem is based?
> 
1. **Independence**: The random variables must be independent (or weakly dependent under some generalizations).
2. **Identically distributed**: Classical CLT **assumes same distribution**, but there are generalized versions (Lindeberg–Feller) for non-identical distributions.
3. **Finite variance**: Infinite variance distributions (like Cauchy) do not satisfy the classical CLT.
4. **Implication**: No matter the original distribution of $X_i$, the sum (or average) becomes approximately normal for large $n$.

## Consequence

- Justifies why the normal distribution appears so frequently in statistics and nature.
- Enables **confidence intervals** and **hypothesis testing** even when the underlying distribution is unknown.

## Proof

> 
- [ ]  [Two Proofs of the Central Limit Theorem](https://www.cs.toronto.edu/~yuvalf/CLT.pdf)
- [ ]  https://www.youtube.com/watch?v=nWadI0_u6QU
- [ ]  https://math.stackexchange.com/questions/1800852/prerequisites-to-prove-central-limit-theorem

## References

- https://en.wikipedia.org/wiki/Central_limit_theorem
- https://en.wikipedia.org/wiki/Illustration_of_the_central_limit_theorem
- https://www.youtube.com/watch?v=zeJD6dqJ5lo
