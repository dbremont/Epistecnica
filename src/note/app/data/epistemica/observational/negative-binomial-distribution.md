---
tags: [discrete]
---

# Negative Binomial Distribution

   : Bernoulli Distribution (Bernoulli%20Distribution%200d4be944e3a24f4eb5b530120fcf125a.md), Geometric Distribution (Geometric%20Distribution%205b08dc3f91464f80a3f9aacd5ad797cd.md), Binomial Distribution (Binomial%20Distribution%2093d6cef12f104d769af0627f2a04c139.md)

> The **Negative Binomial Distribution** models the number of **trials** needed to achieve the r-th success in a sequence of **independent Bernoulli trials**, each with probability of success $p$.
> 

## Formulation

Formally, if $X$ is the random variable representing the total number of trials until the r-th success:

$X \sim \text{NegBin}(r, p)$

- $r \in \mathbb{N}$ = number of required successes (fixed, positive integer)
- $p \in (0,1)$ = probability of success on each trial
- $X = r, r+1, r+2, \dots$

## **Probability Mass Function (PMF)**

$P(X = k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}, \quad k = r, r+1, r+2, \dots$

- $\binom{k-1}{r-1}$ = ways to arrange the first $r-1$ successes among the first $k-1$ trials
- $p^r$ = probability of $r$ successes
- $(1-p)^{k-r}$ = probability of $k-r$ failures

## **Cumulative Distribution Function (CDF)**

> The CDF can be written in terms of the **regularized incomplete beta function**: $P(X \le k) = I_p(r, k-r+1)$
> 

## Relation

| **Distribution** | **Relation to Negative Binomial** | **Description** | **Typical Use Cases** |
| --- | --- | --- | --- |
| **Bernoulli** | Building block (trials are Bernoulli experiments). | Single success/failure trial with probability pp. | Coin flips, pass/fail experiments. |
| **Binomial** | Binomial fixes number of trials $n$ and counts successes; Negative Binomial fixes number of successes $r$ and counts trials. | Two “dual” ways to model repeated Bernoulli trials. | Quality testing, survey experiments. |
| **Geometric** | Special case: $\text{NegBin}(r=1, p) = \text{Geom}(p)$. | Trials until the **first** success. | Waiting times, reliability. |
| **Pascal** | Synonym for Negative Binomial. | Alternate naming convention. | Same as Negative Binomial. |
| **Poisson** | Negative Binomial generalizes Poisson as an **overdispersed count model**. | Poisson: mean = variance; NegBin: variance > mean. | Count data in epidemiology, ecology, insurance claims. |
| **Exponential (Gamma)** | Continuous analogues: Gamma is the waiting time for rr events in a Poisson process; NegBin is the discrete counterpart. | Both model “time until r events,” one discrete, one continuous. | Queueing theory, survival analysis. |

## Case Study

| **Case Study** | **Description** |
| --- | --- |
| **Medical Trials** | Number of patients tested until 5 show a positive response to a new treatment. |
| **Quality Control in Manufacturing** | Number of items inspected until 3 defective items are found. |
| **Basketball Shooting** | Number of shots taken until a player makes 10 successful free throws. |
| **Customer Service Complaints** | Number of calls until the call center receives 4 complaints about a product. |
| **Network Packet Transmission** | Number of packets sent until 2 are successfully transmitted without error. |
| **Epidemiology (Disease Spread)** | Number of people exposed until 6 become infected. |
| **Insurance Claims** | Number of policies observed until 3 claims are filed. |
| **Reliability Testing** | Number of devices tested until 5 pass quality standards. |

## References

- https://en.wikipedia.org/wiki/Negative_binomial_distribution
