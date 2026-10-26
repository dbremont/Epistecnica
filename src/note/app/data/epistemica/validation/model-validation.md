---
tags: [learning-system, probability, statistic]
---

# Model Validation

Related: [Statistical Hypothesis Testing](note.html?n=epistemica/validation/statistical-hypothesis-testing.md), [Probability Model Validation](note.html?n=epistemica/validation/probability-model-validation.md)

> The process of quantitatively and qualitatively assessing the performance, reliability, and generalizability of a mathematical, statistical, or computational model by comparing its outputs against independent datasets, theoretical expectations, or known system behaviors, to determine whether the model accurately represents the underlying system or phenomenon within a specified domain of applicability.
> 

- Problems
- Techniques
- Related Tools

### 1. **Model Verification**

- Ensures the model is implemented correctly.
- Topics: code correctness, numerical stability, algorithm verification, software testing.

### 2. **Model Calibration / Parameter Estimation**

- Fitting model parameters to data before validation.
- Topics: maximum likelihood estimation, Bayesian inference, optimization methods, regularization.

### 3. **Cross-Validation Techniques**

- Methods to assess generalization performance.
- Topics: k-fold, leave-one-out, stratified sampling, nested cross-validation.

### 4. **Uncertainty Quantification (UQ)**

- Assessing confidence in model predictions.
- Topics: Monte Carlo simulation, bootstrapping, propagation of input uncertainties, confidence intervals.

### 5. **Sensitivity Analysis**

- Determining which inputs most affect outputs.
- Topics: local vs global sensitivity, Sobol indices, variance-based methods.

### 6. **Error Analysis and Residual Diagnostics**

- Evaluating model discrepancies.
- Topics: residual plots, heteroscedasticity, bias-variance decomposition, goodness-of-fit metrics.

### 7. **Hypothesis Testing**

- Statistical tests comparing model predictions to observations.
- Topics: chi-square tests, Kolmogorov-Smirnov test, likelihood ratio tests.

### 8. **Probabilistic Modeling & Calibration**

- Using probability distributions for predictions and validation.
- Topics: Bayesian model checking, predictive posterior checks, calibration curves.

### 9. **Overfitting / Underfitting Analysis**

- Ensuring the model generalizes to unseen data.
- Topics: complexity control, regularization, parsimony principles, learning curves.

### 10. **Domain of Applicability**

- Defining the input space where the model is valid.
- Topics: extrapolation limits, operational envelopes, boundary conditions, scenario analysis.

### 11. **Benchmarking and Comparative Studies**

- Comparing multiple models against the same dataset or system.
- Topics: model intercomparison, ensemble modeling, performance ranking.

### 12. **Verification-Validation-Accreditation (VV&A)**

- Formal framework in computational science, engineering, and defense applications.
- Topics: standard protocols, documentation, independent assessment.

---

If you want, I can make a **visual concept map linking model validation to all these related topics** showing dependencies and workflows—it’s very useful for technical overviews. Do you want me to do that?

## References

- https://en.wikipedia.org/wiki/Statistical_model_validation
- https://tjfisher19.github.io/introStatModeling/model-validation.html
- https://www.kaggle.com/code/dansbecker/model-validation
