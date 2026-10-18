---
tags: [framework]
---

# Theory of Probability

 : Probability (Probability%204210c322839242cd8cc944b9b1e7c27f.md), Statistics (Statistics%20c9d6a53f36a8494eae934a1a14f969da.md)

> aka. Thinking About The Theory.
> 

> Core mathematical instruments used to **develop the fundamental tools that provide support   probability theory toolbox.**
> 

## Meta Toolbox

- **Set Theory & Measure Theory** – Formal foundation for probability spaces, σ-algebras, and measurable functions.
- **Combinatorial & Analytic Methods** – Counting techniques, generating functions, and asymptotic analysis of sums and sequences.
- **Bounds & Inequalities** – Markov, Chebyshev, Jensen, Hoeffding, Chernoff; control of tail probabilities.
- **Transforms** – Probability generating functions, moment-generating functions, characteristic functions.
- **Convergence Concepts** – Almost sure, in probability, in distribution, in Lᵖ; Law of Large Numbers (LLN).
- **Limit Theorems** – Central Limit Theorem (CLT), Poisson limit theorem, large deviations.
- **Simulation & Approximation Tools** – Monte Carlo methods, coupling arguments, concentration inequalities.
- **Asymptotic Behavior** – Analysis of distributions and statistics as sample size grows; asymptotic normality.
    - **Large Deviations:** How do probabilities of rare events decay exponentially?
    - **Extreme Value Theory:** How do maxima/minima of sequences of random variables behave asymptotically?
- Functional & Operator Methods:
    - **Markov Operators & Transition Kernels** – Study stochastic processes.
    - **Martingales** – Model fair games and controlled growth.
    - **Spectral Methods** – Analyze convergence and stability in stochastic systems.

## **Asymptotic Behavior**

> Core results describing limits and fluctuations of sequences of random variables.
> 

> See [Law of Large Number](law-of-large-number.md), [**Central Limit Theorem (CLT)**](central-limit-theorem-clt.md), ….
> 

| **Result** | **Description** |
| --- | --- |
| **Law of Large Numbers (Weak & Strong)** | Sample averages converge to expected value under appropriate conditions. |
| **Central Limit Theorem (CLT)** | Normal approximation for sums of independent random variables. |
| **Law of the Iterated Logarithm** | Fine-scale fluctuations around the mean for sums of i.i.d. variables. |
| **Glivenko–Cantelli Theorem** | Empirical distribution functions converge uniformly to the true distribution. |

## **Inequalities & Bounds**

| **Inequality** | Description |
| --- | --- |
| **Markov’s Inequality** | Bounds probability that a non-negative random variable exceeds a threshold. |
| **Chebyshev’s Inequality** | Controls deviation from the mean using variance. |
| **Chernoff Bounds** | Exponential bounds for sums of independent random variables. |
| **Hoeffding’s Inequality** | Tail bounds for bounded independent variables. |
| **Jensen’s Inequality** | Relates convex functions of expectations to expectations of convex functions. |

## Miscellanea Result

> Important theorems and tools not classified under the core meta-theory.
> 

| **Result** | **Description** | **Tags** |
| --- | --- | --- |
| **De Moivre–Laplace Theorem** | Early normal approximation to the binomial distribution. | Approximation |
| **Slutsky’s Theorem** | Convergent sequences of random variables preserve convergence under arithmetic operations. | Convergence |
| **Continuous Mapping Theorem** | Convergence of random variables extends under continuous transformations. | Convergence |
| **Skorokhod Representation Theorem** | Provides almost sure representations for weakly convergent sequences. | Convergence |
| **Poisson Approximation (Law of Rare Events)** | Binomial with small pp and large nn approximates Poisson. | Approximation |
| **Wald’s Equation** | Relates expected sums of random variables to expectations under stopping times. | Stopping Times |
| **Optional Stopping Theorem** | Conditions under which stopping a martingale preserves expected value. | Martingales |

## References

- [Inequality](../mathematical/inequality.md)
- [**AM-GM Inequality**](../mathematical/am-gm-inequality.md)
- [**Jensen's Inequality**](../mathematical/jensen-s-inequality.md)
- [Chebyshev's Inequality](../mathematical/chebyshev-s-inequality.md)
- [Cauchy-Schwarz Inequality](../mathematical/cauchy-schwarz-inequality.md)
- https://en.wikipedia.org/wiki/Slutsky%27s_theorem
- https://en.wikipedia.org/wiki/Markov%27s_inequality
- https://en.wikipedia.org/wiki/De_Moivre%E2%80%93Laplace_theorem
- https://en.wikipedia.org/wiki/Convergence_of_random_variables
- [A Guide to Mathematical Problem-Solving](https://app.notion.com/p/A-Guide-to-Mathematical-Problem-Solving-256c0f5171ec803e9629f496098e5d97?pvs=21)
- https://www.youtube.com/@AProbabilitySpace
