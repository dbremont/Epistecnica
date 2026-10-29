---
tags: [discrete]
---

# Binomial Distribution

   : Bernoulli Distribution (Bernoulli%20Distribution%200d4be944e3a24f4eb5b530120fcf125a.md), Geometric Distribution (Geometric%20Distribution%205b08dc3f91464f80a3f9aacd5ad797cd.md), Negative Binomial Distribution (Negative%20Binomial%20Distribution%20d9d392b312aa4766bdccde4c07ccfd70.md)

> The **Binomial distribution** is a **discrete probability** **distribution** that models the number of **successes** in a fixed number of independent **Bernoulli trials** (experiments with exactly two possible outcomes: success or failure), each with the same probability of success.
> 

> **Interpretation:** If we flip a fair coin 10 times, what is the probability of getting exactly 6 heads?.
> 

> **Note:** This is a derivative distribution;  or a distribution derivative model of a stochastic piece of reality.
> 

## Formulation

- **Parameters:**
    - $n$ = number of trials
    - $p$ = probability of success in a single trial
- **Random Variable:**  $X$ = number of successes in $n$ trials
- **Support:** $X \in \{0, 1, 2, \dots, n\}$
- **Probability Mass Function (PMF):**  $P(X = k) = \binom{n}{k} p^{k}(1 - p)^{\,n - k}, \quad k = 0,1,2,\dots,n$  where $\displaystyle\binom{n}{k} = \frac{n!}{k!\,(n - k)!}$  is the binomial coefficient.
- **Mean:** $\mu = np$
- **Variance:** $\sigma^{2} = np(1 - p)$

## Relation

| Distribution | Relationship with Binomial | Notes |
| --- | --- | --- |
| **Bernoulli** | A Binomial$(n,p)$ is the **sum of $n$ independent Bernoulli($p$) trials**. | Each single trial of a Binomial is Bernoulli. |
| **Negative Binomial** | Models the **number of trials until a fixed number of successes**; Binomial models **number of successes in a fixed number of trials**. | Complementary view: “success-first” vs “trial-fixed.” |
| **Geometric** | Special case of Negative Binomial with **1 success**. | Number of trials until first success. |
| **Poisson** | Binomial$(n,p)$ ≈ Poisson($\lambda = n p$) for **large $n$, small $p$**. | Useful for rare events in large populations. |
| **Hypergeometric** | Similar to Binomial but **without replacement** from a finite population. | Binomial assumes independent trials with replacement (or infinite population). |
| **Normal** | Binomial($n,p$) ≈ Normal($\mu = np, \sigma^2 = np(1-p)$) for **large $n$**. | Central Limit Theorem approximation. |

## Case Study

| Case Study | Description | Trials ($n$) | Success Probability (pp) | Random Variable ($X$) |
| --- | --- | --- | --- | --- |
| **Coin Flips** | Counting number of heads in 10 fair coin flips | 10 | 0.5 | Number of heads |
| **Kidney Compatibility** | Counting number of compatible donors out of 5 candidates | 5 | 0.3 (assumed) | Number of compatible donors |
| **Quality Control** | Number of defective items in a batch of 20 products | 20 | 0.05 | Number of defective items |
| **Customer Purchases** | Number of customers making a purchase out of 50 visitors | 50 | 0.2 | Number of purchases |
| **Sports Success** | Number of successful free throws out of 15 attempts | 15 | 0.8 | Number of successes |
| **Vaccine Effectiveness** | Number of people showing immunity in a sample of 30 vaccinated | 30 | 0.9 | Number of immune individuals |

## QA

### How to derive the ‘Binomial Distribution’?

> `<<TODO>>`
> 

## References

- https://en.wikipedia.org/wiki/Binomial_distribution
