---
tags: [probability, stochastic-process]
---

# Martingale

 : Expected Value (Expected%20Value%20a126776d511e4492b643fb5075e68ef2.md), Stochastic Process (Stochastic%20Process%200fecab268ff946668713151fbce73638.md)

> A **Martingale** is a stochastic process where the expected value of the **next observation**, given all past observations, is equal to the **current observation**, implying **no predictable trend** or bias over time.
> 

## QA:

- How does the idea of a **`Martingale` allows us to define ‘fairness’ in a Rigorous way?**
- How to think deeply about **`Martingale`?**
- What does having expert Knowledge about  **`Martingale` looks like?**
- What is the meaning of the expected feature?

## Formulation

> A martingale is a stochastic process (a sequence of random variables) that models a "fair game," where the expected future value, given all past information, is equal to the current value.
> 

> Let $(\Omega, \mathcal{F}, P)$ be a probability space, and $\{\mathcal{F}n\}{n \geq 0}$  be a filtration (an increasing sequence of σ-algebras representing information up to time $n$.
> 

A stochastic process $\{X_n\}_{n \geq 0}$ is a **martingale** with respect to $\{\mathcal{F}_n\}$ if:

1. **Integrability**: $\mathbb{E}[|X_n|] < \infty$ for all $n$.
2. **Adaptedness**:  $X_n$ is $\mathcal{F}_n$-measurable (i.e.,  $X_n$ depends only on information up to time $n$.
3. **Martingale Property**:  $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n \quad \text{(a.s.)}$ 
(The conditional expectation of the next value, given past information, is the current value.)

## Taxonomy

- **Submartingale**: $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] \geq X_n$ (a favorable game, expected value increases).
- **Supermartingale**: $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] \leq X_n$ (an unfavorable game, expected value decreases).

## Uses

- Modeling Fair Games: Martingales are used to model fair games where the expected future value, given the current information, equals the present value.
- Signal Processing: Martingales are used in the analysis and filtering of stochastic signals, such as in Kalman filtering.
- **Finance**: Modeling stock prices under the risk-neutral measure (where discounted asset prices are martingales).
- **Gambling Theory**: Analyzing betting strategies (e.g., the classic "double after loss" strategy).
- **Statistics**: Sequential hypothesis testing and estimation.

## **Limitations**

- The martingale property assumes no bias (fair game), which rarely holds in real-world scenarios (e.g., casinos have an edge).
- In finance, strict martingales require idealized assumptions (e.g., no arbitrage, frictionless markets).

## Case Studies

### **Symmetric Random Walk**

Let $\{Z_n\}$ be i.i.d. random variables with $P(Z_n = +1) = P(Z_n = -1) = \frac{1}{2}$.

Define $S_n = \sum_{i=1}^n Z_i$ (a symmetric random walk). 

Then $\{S_n\}$ is a martingale because: $\mathbb{E}[S_{n+1} \mid \mathcal{F}n] = S_n + \mathbb{E}[Z{n+1}] = S_n + 0 = S_n$.

### **Gambler’s Fortune in a Fair Bet**

A gambler bets on fair coin flips, winning  $+1$ on heads and losing $-1$ on tails.

Their fortune  $\{X_n\}$ is a martingale since the expected future fortune equals the current fortune.

### Fair Coin Toss

> Let Xₙ be your cumulative gain. Then {Xₙ} is a martingale.
> 

### **Product of Independent Mean-1 Random Variables**

Let $Y_1, Y_2, \dots$ be independent with $\mathbb{E}[Y_i] = 1$.

Define$M_n = \prod_{i=1}^n Y_i$. Then  $\{M_n\}$ is a martingale because:
$\mathbb{E}[M_{n+1} \mid \mathcal{F}n] = M_n \cdot \mathbb{E}[Y{n+1}] = M_n \cdot 1 = M_n.$

## QA

### What is the meaning of the expected feature?

## References

- https://en.wikipedia.org/wiki/Martingale_(probability_theory)
