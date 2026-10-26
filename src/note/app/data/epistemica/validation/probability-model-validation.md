# Probability Model Validation

Related: [Model Validation](note.html?n=epistemica/validation/model-validation.md)

> **Probability model validation** is the process of assessing whether a probabilistic model **adequately represents the system or phenomenon it is intended to describe**, capturing both the **structural dependencies** and the **stochastic behavior** of the variables of interest. The goal is to ensure that predictions, inferences, or decisions based on the model are **reliable** and **consistent with observed data**.
> 

> **Continue:** We need to enter, study, and evaluate the methods of evaluation themselves.
> 

## What makes a good probability representation?

| Criteria | Description |
| --- | --- |
| **Expressiveness** | Able to capture the full range of uncertainty, dependencies, and conditional relationships in the system. |
| **Clarity / Interpretability** | Probabilities, dependencies, and structure are understandable and interpretable by humans or other systems. |
| **Coherence** | Probabilities obey the axioms of probability (e.g., non-negative, sum to 1 where required, consistent conditional probabilities). |
| **Compactness / Parsimony** | Avoids unnecessary complexity; represents the essential stochastic structure without overfitting. |
| **Computational Tractability** | Supports efficient computation for inference, prediction, or simulation. |
| **Robustness** | Small changes in assumptions or inputs do not produce implausible results. |
| **Flexibility / Extensibility** | Can be updated with new data or extended to incorporate additional variables or dependencies. |
| **Validation-Friendly** | Allows easy evaluation against observed data using calibration, goodness-of-fit, or predictive performance checks. |

## How  do we validate our probabilistic model?

Validation involves several complementary checks:

1. **Predictive Accuracy:**
    - Compare model predictions with observed outcomes.
    - Evaluate whether the probabilities assigned to events reflect actual frequencies (calibration).
2. **Structural Consistency:**
    - Assess if the assumed **joint or conditional dependencies** among variables match observed relationships.
    - Check for independence assumptions or correlations embedded in the model.
3. **Sensitivity Analysis:**
    - Test how changes in inputs or assumptions affect outputs.
    - Identify parameters or assumptions that significantly influence model behavior.
4. **Out-of-Sample Testing / Cross-Validation:**
    - Validate model on data not used for parameter estimation to check generalization.
5. **Plausibility and Coherence:**
    - Ensure probabilities are coherent (no negative probabilities, sum to 1 where required).
    - Verify that the model does not violate domain knowledge or known constraints.

## Which are the principles?

| Principle | Description |
| --- | --- |
| Consistency | The model should consistently reproduce patterns observed in data and respect known theoretical relationships. |
| Calibration | Predicted probabilities should match empirical frequencies; e.g., events predicted at 70% probability occur roughly 70% of the time. |
| Robustness | The model’s outputs should remain informative under minor changes to inputs or assumptions. |
| Transparency | Assumptions, dependencies, and conditional structures should be explicit and reproducible. |

### Which are the methods?

| Category | Method | Description |
| --- | --- | --- |
| Goodness-of-Fit | Chi-square test, KS test, Anderson-Darling test | Compare empirical distribution of data to model-predicted distribution. |
| Likelihood-Based | Log-likelihood, AIC, BIC | Evaluate how well the model explains data while penalizing complexity. |
| Bayesian Checks | Posterior predictive checks | Simulate data from posterior predictive distribution and compare to observations. |
| Cross-Validation | k-fold, train/test split | Assess predictive performance on data not used in model fitting. |
| Residual Analysis | Residual plots, standardized residuals | Identify systematic discrepancies between predictions and observations. |
| Sensitivity Analysis | Scenario testing, parameter perturbation | Evaluate how changes in assumptions or inputs affect model outputs. |
| Information-Theoretic | KL divergence, entropy metrics | Measure divergence between predicted and empirical distributions. |

## Which are the tips?

| Tip | Description |
| --- | --- |
| Validate Early | Begin validation while building the model, not just at the end. |
| Use Multiple Metrics | Combine calibration, predictive performance, and structural checks for a holistic view. |
| Check Assumptions Explicitly | Ensure independence, conditionality, or distributional assumptions are realistic. |
| Visualize Predictions | Graphical comparisons can reveal mis-specifications not visible numerically. |
| Document Everything | Record validation steps, data splits, and assumptions for reproducibility. |

## Which are the pitfalls?

| Pitfall | Description |
| --- | --- |
| Overfitting | Model fits the training data too closely and fails to generalize. |
| Ignoring Dependencies | Treating variables as independent when they are not leads to misleading results. |
| Miscalibration | Predicted probabilities systematically over- or under-estimate actual frequencies. |
| Confirmation Bias | Selecting validation metrics or data subsets that favor the model. |
| Neglecting Out-of-Sample Testing | Failing to validate on unseen data hides poor generalization. |
| Complexity Without Justification | Adding unnecessary parameters that do not improve explanatory power. |

## QA

### How do we detect model incompleteness—that is, when there is unaccounted context affecting the probability outcomes?

> A probabilistic model is rarely complete. Detection focuses on identifying **patterns of misfit**—systematic discrepancies, unexplained correlations, or context-dependent mispredictions—that indicate missing structure or unmodeled dependencies.
> 

> **Note:** Incredible enough — to complete the matter — a context-based true phenomenon can sometimes be represented by a non-context-aware distribution under the KL test, **because the marginal probabilities of outcomes average out to match the model**, even though the hidden context influences individual events.
> 

| Approach | Signals of Incompleteness |
| --- | --- |
| **Residual Analysis** | Examine residuals (difference between observed and predicted outcomes). Systematic patterns, clusters, or correlations in residuals indicate missing variables or contextual factors. |
| **Calibration Checks** | If predicted probabilities consistently over- or under-estimate observed frequencies across subsets of data, it may indicate unmodeled context affecting outcomes. |
| **Out-of-Sample / Cross-Validation Performance** | Large drops in performance on new data suggest that the model does not capture all relevant factors or interactions. |
| **Conditional Performance Analysis** | Evaluate predictions conditional on known subgroups or covariates. Discrepancies reveal context-specific effects not included in the model. |
| **Sensitivity Analysis / Scenario Testing** | Perturb inputs or environmental variables and observe output changes. Unexpected sensitivity may indicate missing dependencies. |
| **Information-Theoretic Metrics** | Measures like **KL divergence** between predicted and empirical distributions can highlight gaps where the model fails to capture real variation. |
| **Expert or Domain Knowledge Review** | Comparing model assumptions to domain knowledge can uncover omitted variables or context dependencies. |
| **Latent Variable Modeling / Residual Correlations** | Strong correlations among residuals may suggest the influence of unobserved latent variables affecting multiple outcomes. |

## References

- Tohme, Tony. The Bayesian validation metric: a framework for probabilistic model calibration and validation. Diss. Massachusetts Institute of Technology, 2020.
- https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
