---
tags: [probability, technique]
---

# Sampling

 : Resampling (Resampling%20dcf270ecaea949f3a7d44524e6e3f2df.md)

> In probability and statistics, **sampling** refers to the process of selecting a subset of elements from a larger **population** or **universe** in order to make inferences about the whole population. The main idea is that it is usually impractical or impossible to observe every member of a population, so we observe a sample and use it to estimate population properties.
> 

> A **sample** can be seemed as a representation of the population; we can abuse the concept of model and called it that.
> 

## Criteria

> What criteria ensure that a sample reliably reflects the population? How do we know that we have a good sample? What a good sample mean? How large should the sample be?
> 

> The key in this process is that a well-chosen sample **retains the essential properties of the population**, allowing any procedure applied to the sample to be meaningfully **generalized to the population**.
> 

## Method

> How do we choose the sample?
> 

| **Sampling Method** | **Description** |
| --- | --- |
| **Simple Random Sampling** | Every member of the population has an equal chance of being selected. |
| **Systematic Sampling** | Selects every nth member from a list or sequence, starting from a random point. |
| **Stratified Sampling** | Divides the population into distinct subgroups (strata) and samples from each subgroup. |
| **Cluster Sampling** | Divides the population into clusters, randomly selects some clusters, and samples all members within those clusters. |
| **Convenience Sampling** | Selects samples based on their easy availability or accessibility. |
| **Judgmental (Purposive) Sampling** | Selects samples based on the judgment of the researcher, targeting specific individuals. |
| **Snowball Sampling** | Initial participants recruit additional participants from their acquaintances, forming a network. |
| **Quota Sampling** | Ensures representation of specific subgroups by selecting samples to meet predefined quotas. |
| **Multi-Stage Sampling** | Combines multiple sampling methods, such as clustering followed by stratified sampling. |
| **Bootstrap Sampling** | Uses resampling with replacement from the original sample to create multiple simulated samples. |
| **Simple Random Sampling Without Replacement** | Each member is selected once and not replaced, ensuring a unique sample without repetition. |
| **Simple Random Sampling With Replacement** | Members can be selected more than once, allowing repetitions in the sample. |
| **Gibbs Sampling** | A Markov Chain Monte Carlo (MCMC) method that generates samples from a multivariate probability distribution by sequentially sampling each variable conditional on the others. |
| **Rejection Sampling** | A method to generate samples from a target distribution by sampling from a proposal distribution and accepting or rejecting points based on a criterion. |
| **Importance Sampling** | Generates weighted samples from a proposal distribution to estimate properties of a target distribution, correcting for the difference between the two distributions. |

### Resampling

> **Resampling** works on an existing sample to infer variability or stability.
> 

### Computational Sampling Technique

> **Computational sampling techniques** generate samples from a model or distribution when direct sampling is difficult.
> 

## Checklist

- [ ]  Ensure the sample is **randomly selected** (or follows a well-defined sampling scheme).
- [ ]  Verify that the sample size is **adequate** for reliable inference.
- [ ]  Check that the sample **captures the variability** of the population.
- [ ]  Confirm that the sampling method aligns with the **study objectives** and assumptions.

## Pitfall

- [ ]  **Ignoring non-stationarity**: Population characteristics may change over time, invalidating inferences.
- [ ]  **Non-representative selection**: Missing subgroups or important patterns.
- [ ]  **Insufficient sample size**: Leads to unreliable or highly variable estimates.
- [ ]  **Bias**: Sample systematically over- or under-represents parts of the population.

## References

- [Sampling (statistics)](https://en.wikipedia.org/wiki/Sampling_(statistics))
