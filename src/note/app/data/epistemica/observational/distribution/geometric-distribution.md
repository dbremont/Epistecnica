# Geometric Distribution

   : Bernoulli Distribution (Bernoulli%20Distribution%200d4be944e3a24f4eb5b530120fcf125a.md), Binomial Distribution (Binomial%20Distribution%2093d6cef12f104d769af0627f2a04c139.md), Negative Binomial Distribution (Negative%20Binomial%20Distribution%20d9d392b312aa4766bdccde4c07ccfd70.md)

> The **Geometric Distribution** models the **number of trials needed to get** the **first success** in a sequence of independent Bernoulli trials, where each trial has the same probability of success $p$.
> 

Formally, if $X$ is a random variable representing the trial number of the first success: $X \sim \text{Geometric}(p)$

- $p$ = probability of success on a single trial
- $X = 1, 2, 3, \dots$

## Probability Mass Function (PMF)

> The probability that the first success occurs on the *k*-th trial:   $P(X = k) = (1-p)^{\,k-1}\,p,\qquad k = 1,2,3,\dots$
> 
- $(1-p)^{k-1}$ — probability of $k-1$ consecutive failures
- $p$ — probability of success on trial $k$

## Cumulative Distribution Function (CDF)

The probability that the first success occurs **on or before** the *k*-th trial: $P(X \le k) = 1 - (1-p)^{\,k},\qquad k = 1,2,3,\dots$

## Relation

| **Distribution** | **Relation to Geometric** | **Description** | **Typical Use Cases** |
| --- | --- | --- | --- |
| **Bernoulli** | Basis of Geometric (Geometric is a sequence of Bernoulli trials) | Models a single trial with success ($p$) or failure $(1-p)$. | Coin flips, success/failure experiments. |
| **Binomial** | Related via CDF: $P(X \le n) = P(\text{Binomial}(n,p) \ge 1)$ | Counts number of successes in a fixed number of trials. | Quality control, polling, genetics. |
| **Negative Binomial** | Generalization: Geometric is the case $r=1$. | Counts trials until the r-th success. | Reliability testing, epidemiology, accident modeling. |
| **Exponential** | Continuous analogue (both are memoryless). | Models waiting time until first event in continuous time. | Queueing systems, survival analysis, Poisson processes. |
| **Pascal** | Synonym for Negative Binomial. | Same as above. | Same as above. |

## Case Study

| **Case Study** | **Description** |
| --- | --- |
| **Customer Support Complaints** | Number of calls until the first complaint about a product is received. |
| **Basketball Free Throws** | Number of attempts until a player makes the first successful free throw. |
| **Manufacturing Defects** | Number of items inspected until the first defective item is found. |
| **Drug Trial Success** | Number of patients treated until the first one shows a positive response to a new drug. |
| **Hiring Process** | Number of interviews until the first candidate meets all requirements. |
| **Network Transmission** | Number of packet transmissions until the first one is successfully delivered without error. |
| **Gambling (Coin Toss)** | Number of coin tosses until the first heads appears. |
| **Cybersecurity Intrusion Detection** | Number of login attempts until the first detected breach occurs. |

## References

- [Serie](../mathematical/serie.md)
- [Sequence](../mathematical/sequence.md)
- https://en.wikipedia.org/wiki/Geometric_distribution
