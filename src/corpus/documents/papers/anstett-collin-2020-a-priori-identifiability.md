---
tags: [document, paper, identifiability, control-theory, modelling]
---

# Anstett-Collin, F., Denis-Vidal, L., & Millérioux, L. (2020). A priori identifiability: An overview on definitions and approaches. *Annual Reviews in Control*, 50, 139–149.

```python
@article{anstettcollin2020priori,
  title = {A priori identifiability: An overview on definitions and approaches},
  author = {Anstett-Collin, F. and Denis-Vidal, L. and Mill{\'e}rioux, L.},
  journal = {Annual Reviews in Control},
  volume = {50},
  pages = {139--149},
  year = {2020},
}
```

## Notes

> **A priori identifiability** is a property of the **model structure alone**: given ideal, noise-free observations of the outputs, can the parameters be recovered uniquely? The question is asked *before* an experiment is designed, and it does not depend on the data — which is what separates it from practical identifiability, where noise, excitation and sample size decide what can actually be estimated.

**The overview's useful work is terminological.** The literature uses "identifiable" for at least four different properties, and the paper separates them: **global** identifiability (a unique parameter vector for the whole admissible set) against **local** (unique in a neighbourhood); **structural** against **practical**; and identifiability of the parameters against identifiability of functions of them. A model can be locally but not globally identifiable, and a parameter can be non-identifiable while a function of it — a ratio, a product, a steady-state gain — is perfectly recoverable.

**The approaches are mapped to the model class.** Differential algebra for rational nonlinear systems, the generating-series method, linearisation around an operating point for the linear case, and the numerical/algebraic tests that decide the question for a given structure. The paper's value is that it states which method applies to which class rather than presenting one method as general.

> The consequence for practice is the one the corpus already leans on: where a model is not identifiable, the parameters lie in **fibres** — the sets of parameter values that produce the same output — and any calibrated value is a representative of a set, not a measurement. Gauge-fixing (a normalisation, a reference level, a prior) is what makes the number reportable, which is why reporting a calibrated parameter without the gauge convention is under-specified.

## References

- [Calibration](/view.html?p=notes/epistemica/validation/calibration.md) — the practical side: the calibration trap and what a fibre does to a calibrated value
- [Identification](/view.html?p=notes/epistemica/meta/theory/identification.md) — system identification, whose solvability this theory conditions
- [Modelling](/view.html?p=notes/epistemica/meta/theory/modelling.md) — the epistemic frame the model structure belongs to
- [Underdetermination](/view.html?p=notes/epistemica/meta/theory/underdetermination.md) — the epistemic version of the same failure
