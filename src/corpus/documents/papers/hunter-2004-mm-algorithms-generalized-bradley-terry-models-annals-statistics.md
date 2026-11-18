---
tags: [document, statistics, paired-comparisons, optimization, ranking]
---

# Hunter, D. R. (2004). MM Algorithms for Generalized Bradley–Terry Models. The Annals of Statistics, 32(1), 384–406. https://doi.org/10.1214/aos/1079120141

```python
@article{hunter2004mm,
  title = {MM algorithms for generalized Bradley--Terry models},
  author = {Hunter, David R.},
  journal = {The Annals of Statistics},
  volume = {32},
  number = {1},
  pages = {384--406},
  year = {2004},
  doi = {10.1214/aos/1079120141},
  jstor = {3448514},
}
```

## Notes

The Bradley–Terry model turns paired comparisons into a probability: if object $i$ has strength $\pi_i > 0$, then
$$\Pr(i \text{ beats } j) = \frac{\pi_i}{\pi_i + \pi_j},$$
and the strengths are estimated from the observed wins. It is the standard latent-strength model behind sports rankings, preference data and any experiment in which subjects are compared two at a time. The estimation problem is a likelihood maximisation, and the classical solution is Zermelo's iterative scaling — a fixed-point algorithm that is easy to state and, in the original presentation, not obviously convergent.

**What the paper does.** Hunter's contribution is to show that Zermelo's algorithm is a special case of a general and provably convergent scheme — the **MM algorithm** (minorization–maximization, also called majorization–minimization in the optimisation literature). The construction is the standard one: at the current estimate, build a surrogate function that lies below the log-likelihood and touches it at the current point, maximise the surrogate, and repeat. Because the surrogate is chosen to be easy to maximise and to touch the objective, each step cannot decrease the likelihood, so the sequence is monotone; under the usual regularity conditions it converges to the maximum-likelihood estimate.

**The generalization is the point.** The basic Bradley–Terry model handles two objects and no ties. Hunter derives MM algorithms for the extensions that applied work actually needs:

- **ties**, through Davidson's model, in which the probability of a draw is a third outcome with its own parameter;
- **home-field advantage**, where one side of every comparison carries an extra parameter;
- **comparisons among more than two objects**, where the outcome is an ordering rather than a winner.

For each, the MM algorithm is written explicitly, the surrogate is exhibited, and the monotone convergence follows from the same argument rather than from a case-by-case proof.

**Why it matters.** The paper made a classical algorithm trustworthy and general. Before it, the iterative scaling for Bradley–Terry was folklore with an uncertain convergence proof; after it, the fitting method for paired-comparison models is a short, monotone, easily implemented loop — one that remains the default in ranking software and in the applied literature on preference and sports models. The MM template also generalises: the same construction is now used for mixture models, multidimensional scaling and other latent-variable likelihoods where the direct maximisation is intractable.

**The boundary worth keeping.** The paper is about *fitting* a model that is already chosen; it does not argue that Bradley–Terry is the right model for a given comparison design. That choice — and the questions of transitivity, identifiability of the strengths up to a multiplicative constant, and the handling of sparse comparison graphs — belongs to the modelling decision around it.

## References

- https://doi.org/10.1214/aos/1079120141
- [JSTOR 3448514](https://www.jstor.org/stable/3448514)
- [CiteSeerX 10.1.1.110.7878](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.110.7878)
- [Ranking](/view.html?p=notes/epistemica/mathematical/relation/ranking.md) — the ordering the model estimates
- [Ordering](/view.html?p=notes/epistemica/quantification/ordering.md) — the ordinal scale a pairing produces
- [Matching](/view.html?p=notes/epistemica/singular/matching.md) — the assignment problem the comparison data often comes from
- [Generalized Linear Models](/view.html?p=notes/epistemica/observational/computational/generalized-linear-models-glm.md) — the likelihood family Bradley–Terry belongs to
- [Statistics](/view.html?p=notes/miscellanea/discipline/statistics.md) — the discipline
