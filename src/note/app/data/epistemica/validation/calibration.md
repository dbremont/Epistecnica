---
tags: [calibration, identifiability, validation, estimation]
---

# Calibration

> Calibration is the practice of fixing the free elements of a representation — its parameters, its scale, or its probability assignment — against a trusted reference, so that the representation reproduces what is taken as the standard.

> A calibrated model is not thereby a validated model: calibration constrains behaviour to a reference, validation judges whether that behaviour extends beyond it.

## Formulation

### What is this epistemic instance?

> The **calibration instance** is the organized practice of bringing a representation into agreement with a reference. In its parametric form it selects the free parameters $\theta$ of a map $f_\theta : X \to Y$ by minimizing a discrepancy against data:
>
> $$\theta^\* = \arg\min_{\theta \in \Theta} \; d\big(B(C_\theta),\, r\big),$$
>
> where $B(C_\theta)$ is the behaviour of the model instance, $r$ is the reference (observations, a measurement standard, or a target frequency), and $d$ is the discrepancy or loss. The result is a calibrated instance $C_{\theta^\*}$, not a validated one.

> The word covers three practices that must not be conflated:

| Sense | Reference $r$ | What is fixed | Criterion |
| --- | --- | --- | --- |
| **Parameter / model calibration** | data from the target | parameters $\theta$, sometimes structure | discrepancy, likelihood, posterior |
| **Probabilistic / forecast calibration** | observed frequencies | the probability assignment $P(Y \mid X)$ | reliability; predicted probabilities match frequencies |
| **Measurement / instrument calibration** | a measurement standard | the scale, zero, or response function | traceability, bias, uncertainty |

> The three share one schema — representation, reference, discrepancy, adjustment — and differ in what is adjusted and what the reference is. A probability calibration curve is not a parameter fit; a measurement calibration is not a model calibration; treating them as one operation hides the failure modes specific to each.

> Calibration must also be distinguished from its neighbours. **Identification** asks whether the free elements are recoverable from the reference at all; calibration *produces* an estimate even when the answer is no, in which case it selects an arbitrary representative of a gauge orbit. **Validation** judges adequacy on data not used for calibration; calibration alone can always be made to fit. **Estimation** is the inference step; calibration is the practice that fixes the target of that inference and certifies the fit.

> For probabilistic models, calibration is a property of the forecast, not of the parameters: among all events assigned probability $p$, the observed frequency should be $p$. A model can be sharp and calibrated, sharp and miscalibrated, or calibrated and useless; calibration is necessary for reliability, not sufficient for skill.

### What epistemic element type does this epistemic instance belong to?

> Primary type: `Aggregate` — the **Calibration Practice Set**: the organized inquiry that binds an orientation (which free elements, against which reference), a target (segment, observable, reference record), a representation (map, parameters, scale), operations (fitting, estimation, adjustment), evaluations (discrepancy, reliability, traceability, independent validation), a context (noise and data regime), and an infrastructure (algorithms, reference data) into one coherent epistemic whole. The root type is declared once, and the branches are read as elements of inquiry.

> `readable as` an `Epistemic Operation` when attention falls on the act of fitting or adjusting; `readable as` an `Epistemic Evaluation` when attention falls on the criterion that decides when the fit is acceptable; and `readable as` an `Epistemic Construction` when attention falls on the calibrated artifact. `Aggregate` is primary because calibration is not exhausted by the operation: the criterion and the artifact are constitutive of the practice.

> The calibrated segment and the standard are read in the **Ontic Order**; the calibration practice that brings a representation into agreement with them is epistemic.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, in three ways that the decomposition keeps apart. First, **sense**: parameter calibration, probabilistic calibration, and measurement calibration are different practices with different references and criteria. Second, **aspect**: calibration names the act, the resulting state ("the model is calibrated"), and the warrant ("the calibration is acceptable"); only the first is an operation, and the third is an evaluation. Third, **object**: what is calibrated may be a parameter vector, a probability assignment, or a measurement scale.

> The ambiguity is resolved by declaring `Aggregate` primary and typing the branches separately — parameter calibration under `Epistemic Representation` and `Epistemic Operation`, probabilistic calibration under `Epistemic Evaluation` (reliability), measurement calibration under `Epistemic Access` and `Epistemic Representation` (scale). Collapsing the three into one type would make "calibrated" equivocal.

### What is the recursive instance decomposition of this epistemic instance?

> Calibration is decomposed as an aggregate because its constituents belong to different epistemic types. The tree is the structural answer; the prose before it fixes the relations that the evaluation branches judge.

#### Calibration and its neighbours

> Calibration sits between modelling and validation: it takes a representation produced by modelling and prepares it for validation by fixing its free elements against a reference. It does not establish that the representation is true, only that it reproduces the reference under the chosen discrepancy and domain.

> The **calibration trap** is the failure in which the free elements absorb the data: the fit improves while predictive power and structural adequacy degrade. It is the parametric form of overfitting and a close relative of "right for the wrong reasons". Its diagnosis is not a better fit but an independent test — held-out data, intervention, out-of-distribution prediction, and an identifiability analysis before the calibrated values are read as properties of the target.

> When the free elements are not identifiable, calibration still returns a value: the optimizer lands somewhere in the fibre $B^{-1}(r)$. The number is a representative, not a measurement; gauge-fixing (a normalization, a reference level, a prior) is what makes it reportable. Reporting a calibrated parameter without the gauge convention is under-specified.

> Measurement calibration is the limiting case in which the reference is a standard rather than the target: the operation fixes the instrument's response, and traceability — an unbroken chain of comparisons to the standard — is the criterion. Probabilistic calibration is the limiting case in which the reference is a frequency: the operation fixes the forecast's reliability, and proper scoring rules plus reliability diagrams are the criteria.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Calibration Practice Set | The organized practice of bringing a representation into agreement with a reference, with the operations and evaluations that make the agreement reportable. |
| `Aggregate` → Calibration Practice Set → `Epistemic Orientation` | Grouping: what is calibrated against what, and why. |
| `Aggregate` → Calibration Practice Set → `Epistemic Orientation` → `Epistemic Purpose` | Grouping: purposes of calibration. |
| `Aggregate` → Calibration Practice Set → `Epistemic Orientation` → `Epistemic Purpose` → Reproduction Purpose | Reproduce the reference closely enough for prediction, explanation, or intervention. |
| `Aggregate` → Calibration Practice Set → `Epistemic Orientation` → `Epistemic Question` | Grouping: the question that fixes the free elements and the reference. |
| `Aggregate` → Calibration Practice Set → `Epistemic Orientation` → `Epistemic Question` → Free Element Question | Which parameters, scale, or probability assignment are free, and which reference fixes them? |
| `Aggregate` → Calibration Practice Set → `Epistemic Target` | Grouping: what the calibration is about. |
| `Aggregate` → Calibration Practice Set → `Epistemic Target` → `Target Segment` | Grouping: the bounded portion of reality under calibration. |
| `Aggregate` → Calibration Practice Set → `Epistemic Target` → `Target Segment` → Calibrated Segment | The selected piece of observer-independent reality whose behaviour the reference constrains. |
| `Aggregate` → Calibration Practice Set → `Epistemic Target` → `Observable` | Grouping: the features of the target that the reference records. |
| `Aggregate` → Calibration Practice Set → `Epistemic Target` → `Observable` → Reference Observation | The registered output $r$ against which the representation is calibrated. |
| `Aggregate` → Calibration Practice Set → `Epistemic Target` → `Target Element` | Grouping: the constituent states of the target. |
| `Aggregate` → Calibration Practice Set → `Epistemic Target` → `Target Element` → Calibrated State | The configuration whose behaviour the calibrated representation must reproduce. |
| `Aggregate` → Calibration Practice Set → `Epistemic Access` | Grouping: how the reference becomes registrable. |
| `Aggregate` → Calibration Practice Set → `Epistemic Access` → `Observation Interface` | Grouping: the boundary mechanism coupling target and observer. |
| `Aggregate` → Calibration Practice Set → `Epistemic Access` → `Observation Interface` → Measurement Channel | The instrument, sensor, or protocol that produces the reference. |
| `Aggregate` → Calibration Practice Set → `Epistemic Access` → `Observation Record` | Grouping: what is retained from the reference. |
| `Aggregate` → Calibration Practice Set → `Epistemic Access` → `Observation Record` → Calibration Dataset | The reference data, including its noise, sampling, and provenance. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` | Grouping: the representation whose free elements are fixed. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` | Grouping: the sign system in which the representation is expressed. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → Model Map | The map $f_\theta : X \to Y$ with its free and fixed elements. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` | Grouping: the combinable constituents of the map. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` → Free Parameter | The $\theta$ role: the quantity calibration adjusts. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` → Fixed Parameter | The quantity held fixed by prior knowledge or convention. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` → Input Variable | The $X$ role: state, predictor, or context. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` → Output Variable | The $Y$ role: the observable or response. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Constitutive Substrate` | Grouping: the rules that constitute the map. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Constitutive Substrate` → Parameter Domain | The admissible set $\Theta$ and the gauge conventions that make a point reportable. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → `Measurement Scale` | The scale, zero, and unit fixed in measurement calibration. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → `Measurement Scale` → `Representation Element` | Grouping: the constituents of the scale. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → `Measurement Scale` → `Representation Element` → Scale Zero | The reference point from which the instrument's readings are measured. |
| `Aggregate` → Calibration Practice Set → `Epistemic Representation` → `Representational System` → `Measurement Scale` → `Representation Element` → Scale Unit | The unit in which the calibrated readings are expressed. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` | Grouping: what is done to bring the representation into agreement. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Action` | Grouping: direct transformations of the representation. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Action` → Calibration Fit | Adjust the free elements until the discrepancy is minimized or the criterion is met. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Action` → `Inference` | Grouping: derivations of the free elements from the reference. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Action` → `Inference` → Parameter Estimation | Infer $\theta$ from the reference data. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Action` → `Inference` → Posterior Updating | Update a probability assignment over the free elements from data and priors. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Organization` | Grouping: reproducible organizations of the operation. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Organization` → `Method` | Grouping: generalized ways of calibrating. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Organization` → `Method` → Calibration Method | The organized choice of reference, loss, and optimizer (least squares, likelihood, Bayesian updating, curve matching). |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Organization` → `Procedure` | Grouping: ordered routines within a method. |
| `Aggregate` → Calibration Practice Set → `Epistemic Operation` → `Organization` → `Procedure` → Calibration Procedure | The routine that splits data, fits the free elements, and reports the calibrated values with their gauge conventions. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` | Grouping: how the calibration is judged. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: standards of judgment. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Epistemic Standard` → Calibration Criterion | The threshold or loss below which the representation counts as calibrated. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Epistemic Criterion` | Grouping: evaluated properties. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Epistemic Criterion` → Discrepancy Criterion | How far the representation's behaviour is from the reference. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Epistemic Criterion` → Reliability Criterion | Whether predicted probabilities match observed frequencies. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Epistemic Criterion` → Traceability Criterion | Whether the measurement scale is linked by an unbroken chain to the standard. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Validation` | Grouping: checks beyond the calibration reference. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Validation` → Independent Validation | Held-out data, replication, and intervention tests of the calibrated representation. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Error` | Grouping: deviations and failures. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Error` → Calibration Error | The residual discrepancy between the calibrated behaviour and the reference. |
| `Aggregate` → Calibration Practice Set → `Epistemic Evaluation` → `Error` → Extrapolation Error | Failure of the calibrated representation outside the reference's domain. |
| `Aggregate` → Calibration Practice Set → `Epistemic Context` | Grouping: the conditions under which calibration occurs. |
| `Aggregate` → Calibration Practice Set → `Epistemic Context` → `Epistemic Condition` | Grouping: surrounding conditions. |
| `Aggregate` → Calibration Practice Set → `Epistemic Context` → `Epistemic Condition` → Noise Condition | The noise and sampling regime that bounds what can be calibrated. |
| `Aggregate` → Calibration Practice Set → `Epistemic Context` → `Epistemic Condition` → Data Regime | The amount, coverage, and provenance of the reference data. |
| `Aggregate` → Calibration Practice Set → `Epistemic Infrastructure` | Grouping: what supports the practice. |
| `Aggregate` → Calibration Practice Set → `Epistemic Infrastructure` → `Epistemic Tool` | Grouping: instruments of calibration. |
| `Aggregate` → Calibration Practice Set → `Epistemic Infrastructure` → `Epistemic Tool` → Calibration Algorithm | The optimizer, solver, or estimator that performs the fit. |
| `Aggregate` → Calibration Practice Set → `Epistemic Infrastructure` → `Information Repository` | Grouping: stored references and calibrated models. |
| `Aggregate` → Calibration Practice Set → `Epistemic Infrastructure` → `Information Repository` → Reference Dataset | The retained reference data, metadata, and provenance. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdicts.** The instance is conceptually well identified once the three senses are separated: pass. Its definition is clear but the word is systematically equivocal in use: partial. Its determinacy is carried by the declared reference and criterion; without them "calibrated" is indeterminate: partial. It is internally consistent once parameter, probabilistic, and measurement calibration are typed as branches: pass. Its representational adequacy covers parametric and measurement calibration, and probabilistic calibration through reliability criteria: pass. Its purpose adequacy — supporting fitting, reporting, and the separation of calibration from validation — is high: pass.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The instance is the calibration practice, not the fit alone; the reference and the discrepancy are named. |
| **Definitional Clarity** | Partial | "Calibration" names parameter fitting, probability reliability, and instrument scaling; the note separates them, but ordinary use does not. |
| **Conceptual Determinacy** | Partial | What counts as calibrated depends on the declared reference, loss, and domain; the note makes that dependence explicit rather than removing it. |
| **Internal Consistency** | Pass | The three senses share one schema and are kept distinct; calibration is not silently equated with validation or identification. |
| **Representational Adequacy** | Pass | Parametric and measurement calibration are covered directly; probabilistic calibration is covered by reliability and proper scoring. |
| **Purpose Adequacy** | Pass | Supports calibration reporting, identifiability checks, independent validation, and the diagnosis of the calibration trap. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- [Validation](note.html?n=epistemica/validation/validation.md)
- [Model Validation](note.html?n=epistemica/validation/validation.md)
- [Probability Model Validation](note.html?n=epistemica/validation/probability-model-validation.md)
- [Identification](note.html?n=epistemica/theory/practice/identification.md)
- [Modelling](note.html?n=epistemica/theory/practice/modelling.md)
- [Simulation](note.html?n=epistemica/simulation.md)
- [Measurement Theory](note.html?n=epistemica/measurement/measurement-theory.md)
- Anstett-Collin, F., Denis-Vidal, L., & Millérioux, L. (2020). A priori identifiability: An overview on definitions and approaches. *Annual Reviews in Control*, 50, 139–149.
- Gneiting, T., & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association*, 102(477), 359–378.
- Murphy, A. H. (1973). A new vector partition of the probability score. *Journal of Applied Meteorology*, 12(4), 595–600.
- Dawid, A. P. (1982). The well-calibrated Bayesian. *Journal of the American Statistical Association*, 77(379), 605–610.
- JCGM (2012). *International Vocabulary of Metrology — Basic and General Concepts and Associated Terms (VIM)* (3rd ed.). Joint Committee for Guides in Metrology.
- DeGroot, M. H., & Fienberg, S. E. (1983). The comparison and evaluation of forecasters. *The Statistician*, 32(1/2), 12–22.
- Murphy, A. H., & Winkler, R. L. (1977). Reliability of subjective probability forecasts of precipitation and temperature. *Journal of the Royal Statistical Society: Series C (Applied Statistics)*, 26(1), 41–47.
- Murphy, A. H., & Winkler, R. L. (1987). A general framework for forecast verification. *Monthly Weather Review*, 115(7), 1330–1338.
- Murphy, A. H., & Winkler, R. L. (1992). Diagnostic verification of probability forecasts. *International Journal of Forecasting*, 7(4), 435–455.
- Foster, D. P., & Vohra, R. V. (1998). Asymptotic calibration. *Biometrika*, 85(2), 379–390.
- Gneiting, T., Balabdaoui, F., & Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, 69(2), 243–268.
- Berg, J. E., Nelson, F. D., & Rietz, T. A. (2008). Prediction market accuracy in the long run. *International Journal of Forecasting*, 24(2), 285–300. https://www.sciencedirect.com/science/article/abs/pii/S0169207008000320
- Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review*, 78(1), 1–3.
- Bröcker, J. (2009). Reliability, sufficiency, and the decomposition of proper scores. *Quarterly Journal of the Royal Meteorological Society*, 135(643), 1512–1519.
- Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. In *Proceedings of the 34th International Conference on Machine Learning* (pp. 1321–1330).
- Kuleshov, V., Fenner, N., & Ermon, S. (2018). Accurate uncertainties for deep learning using calibrated regression. In *Proceedings of the 35th International Conference on Machine Learning* (pp. 2796–2804).
- Naeini, M. P., Cooper, G. F., & Hauskrecht, M. (2015). Obtaining well calibrated probabilities using Bayesian binning. In *Proceedings of the AAAI Conference on Artificial Intelligence*, 29(1), 2901–2907.
- Kumar, A., Liang, P., & Ma, T. (2019). Verified uncertainty calibration. In *Advances in Neural Information Processing Systems*, 32.
- Platt, J. (1999). Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods. In A. J. Smola, P. L. Bartlett, B. Schölkopf, & D. Schuurmans (Eds.), *Advances in large margin classifiers* (pp. 61–74). MIT Press.
- Zadrozny, B., & Elkan, C. (2002). Transforming classifier scores into accurate multiclass probability estimates. In *Proceedings of the Eighth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (pp. 694–699).
- Niculescu-Mizil, A., & Caruana, R. (2005). Predicting good probabilities with supervised learning. In *Proceedings of the 22nd International Conference on Machine Learning* (pp. 625–632).
- Raftery, A. E., Gneiting, T., Balabdaoui, F., & Polakowski, M. (2005). Using Bayesian model averaging to calibrate forecast ensembles. *Monthly Weather Review*, 133(5), 1155–1174.
- Jolliffe, I. T., & Stephenson, D. B. (Eds.). (2012). *Forecast verification: A practitioner's guide in atmospheric science* (2nd ed.). Wiley.
- Gneiting, T., & Katzfuss, M. (2014). Probabilistic forecasting. *Annual Review of Statistics and Its Application*, 1, 125–151.
