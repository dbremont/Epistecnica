---
tags: [abstract-framework, probability]
---

# Probability Representation Regime

 : Probability (Probability%204210c322839242cd8cc944b9b1e7c27f.md)

> In this note we introduce the notion of a **Probability Representation Regime**—a conceptual analysis of the different ways in which the abstract ontic–epistemic notion of **stochastic variation and possibility** is operationalized.
> 

> There **is no single universal theory of probability** in practice. Instead, each representation regime typically comes with its own mathematical formalism, modeling assumptions, and inferential practices.
> 

## Regime Space

> Note: This is an intent  of factorizing all notions and uses of probably - but some probably epistemic artifact will fall under several of this regimes.
> 

| **Regime** | **Description** | **Type System (Formal Object)** | **Category Theory Formulation** | **Assignment Mechanism** | **Validation** | **Intuition** |
| --- | --- | --- | --- | --- | --- | --- |
| **Static Regime** | Probability as a fixed measure over an outcome space. | $(\Omega, \mathcal{F}, P)$, $P \in \Delta(\Omega)$ | Objects in **Meas / Prob** category; morphisms are measure-preserving or measurable maps. | Empirical estimation or prior specification. | KS test, likelihood, entropy fit. | “Probability is a thing.” |
| **Kernel Regime** | Probability as a conditional mapping between spaces. | Stochastic kernel $K: X \to \Delta(Y)$ | **Kleisli category of Giry monad**; morphisms are kernels, composition via integration. | Conditional probabilistic models, learned transitions. | Predictive accuracy, generalization, stability. | “Probability is a relation/function.” |
| Process (Path) Regime | …. |  |  |  |  |  |
| **Operator (Pushforward) Regime** | Probability induced via transformations of latent randomness. | (P_X = G_# P_Z), measurable $(G: Z \to X)$ | Functorial pushforward on measure spaces; morphisms induce measure transport. | Latent-variable models, deterministic/stochastic generators, kernel composition. | KL/FID/Wasserstein, sample quality, reconstruction. | “Probability is constructed by transformation.” |

## QA

- Is this an orthogonal characterization of all conceptions and operationalizations of probability?
- Why do we need the definition of a kernel regime? Why not just use the static framework with conditional and joint distributions, etc.?
- What are the epistemic and ontological views on probability?
    - Probability as ground truth
    - Probability as upgraded partial knowledge
    - Imprecise probability
    - ...
- What are the implementation forms across these regimes?
    - Analytical (closed-form)
    - Numerical (MCMC-based)
    - Neural (GAN / diffusion / VAE-based)
- Can all regimes be formulated in terms of the static regime?
- Where does generative machine learning fit within this regime space?
- Which should be the question ask to select a the right regime - for the segment of of reality to represent at hand?
    - …

## References

- https://en.wikipedia.org/wiki/Giry_monad
- https://en.wikipedia.org/wiki/Cylinder_set
- https://en.wikipedia.org/wiki/Wiener_process
- https://en.wikipedia.org/wiki/Generative_model
- https://en.wikipedia.org/wiki/Imprecise_probability
- https://en.wikipedia.org/wiki/Pushforward_measure
- https://en.wikipedia.org/wiki/Fr%C3%A9chet_inception_distance
- https://en.wikipedia.org/wiki/Flow-based_generative_model
- https://en.wikipedia.org/wiki/Kolmogorov_extension_theorem
- https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space
- https://en.wikipedia.org/wiki/Girsanov_theorem
- https://en.wikipedia.org/wiki/Point_process_operation
- https://en.wikipedia.org/wiki/Random_measure
- https://en.wikipedia.org/wiki/Finite-dimensional_distribution
- https://en.wikipedia.org/wiki/C%C3%A0dl%C3%A0g
