---
tags: [probability]
---

# Expectation–Maximization (EM) Algorithm


> The [Expectation–Maximization Algorithm](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm#cite_note-Dempster1977-1) is an iterative optimization method used to estimate parameters for statistical models when there are missing or unobserved data.
> 

The EM algorithm involves two steps in each iteration:

1. The E-step: In this step, the expected value of the unobserved or missing data is calculated given the current estimates of the model parameters.
2. The M-step: In this step, the model parameters are updated to maximize the likelihood of the observed data using the expected values of the missing data from the E-step.

These two steps are repeated until convergence is achieved, at which point the estimates of the model parameters are assumed to be the maximum likelihood estimates. EM algorithm is a powerful tool for estimating parameters of complex models with latent variables, such as mixture models or hidden Markov models.

## References

- Dempster, Arthur P., Nan M. Laird, and Donald B. Rubin. “Maximum likelihood from incomplete data via the EM algorithm.” Journal of the royal statistical society: series B (methodological) 39.1 (1977): 1-22.
- Kamal Nigam, et al.: Text Classification from Labeled and Unlabeled Documents using EM. Machine Learning, 1999.
- Samdani, Chang, and Roth. Unified Expectation Maximization. NAACL 2012.
