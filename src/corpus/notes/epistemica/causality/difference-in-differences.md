---
tags: [note, causality, econometrics, quasi-experiment, statistics]
qa:
 - Parallel trends is an assumption about a counterfactual that is never observed. What evidence would make it credible rather than merely convenient?
 - With staggered adoption, the two-way fixed-effects estimator is a weighted average of many 2×2 comparisons — some of them using already-treated units as controls. When is that weighting defensible?
 - Does a pre-trend test have power to detect the violations that matter, or does it mostly test the violations that are large enough to be visible?
---

# Difference in Differences

> **Difference in differences** (DiD) estimates a causal effect by comparing the change in an outcome for a treated group with the change for an untreated group over the same period. It removes the treated group's time-invariant differences and the common time shock in one subtraction, and the identifying assumption is that, absent treatment, the two groups would have moved in parallel. The design is the workhorse of policy evaluation where randomisation is impossible: a minimum wage, a Medicaid expansion, a tariff, a training programme.

> The estimator is simple; the assumption is not. "Parallel trends" is a claim about a counterfactual path that is never observed, and the whole methodological literature since the 2000s is about what happens when the claim is approximate, when treatment arrives at different times, and when the comparison group is contaminated by the treatment itself.

## The 2×2 case

Two groups ($T$ treated, $C$ control) and two periods (before, after). The DiD estimate is

$$\hat{\tau} = \big(\bar{Y}_{T,\text{after}} - \bar{Y}_{T,\text{before}}\big) - \big(\bar{Y}_{C,\text{after}} - \bar{Y}_{C,\text{before}}\big).$$

The first difference removes the group's fixed level; the second removes the common time effect. What remains is the treatment effect, provided that the treated group's change would have equalled the control group's change without the treatment.

| | Before | After | Change |
| --- | --- | --- | --- |
| **Treated** | $\bar{Y}_{T,b}$ | $\bar{Y}_{T,a}$ | $\Delta_T$ |
| **Control** | $\bar{Y}_{C,b}$ | $\bar{Y}_{C,a}$ | $\Delta_C$ |
| **Difference** | — | — | $\hat{\tau} = \Delta_T - \Delta_C$ |

Equivalently, in regression form with a treatment dummy $D_i$, a post-period dummy $P_t$, and their interaction:

$$Y_{it} = \alpha + \beta D_i + \gamma P_t + \tau\,(D_i \cdot P_t) + \varepsilon_{it},$$

where $\tau$ is the DiD estimate. With multiple groups and periods, the same logic is written as a two-way fixed-effects regression:

$$Y_{it} = \alpha_i + \lambda_t + \tau D_{it} + \varepsilon_{it},$$

with unit fixed effects $\alpha_i$ absorbing the group level and time fixed effects $\lambda_t$ absorbing the common shock.

## The identifying assumption

**Parallel trends**: in the absence of treatment, the average outcome in the treated group would have followed the same path as the control group. This is weaker than "the groups are alike" — they may differ in level, as long as they trend together — and stronger than "the pre-period looks similar", because it constrains a counterfactual that continues after treatment begins.

The assumption is not testable, but it can be probed:

- **Pre-trends.** Estimate the event-study version — interactions of treatment with each period — and check that the pre-treatment coefficients are flat. Flat pre-trends are consistent with parallel trends, not proof of them: a violation that begins at treatment is invisible.
- **Placebo outcomes and placebo groups.** An outcome the treatment cannot plausibly affect, or a group it cannot plausibly reach, should show no effect.
- **Composition.** If treatment changes who is in the sample — entry, exit, migration — the group means change for a reason unrelated to the outcome.
- **Anticipation and spillovers.** If agents adjust before the policy starts, or the control group is affected by the treatment (a neighbouring state's minimum wage, a competitor's price), the comparison group is contaminated.

## Staggered adoption and the modern critique

When units adopt treatment at different times, the two-way fixed-effects estimator is not a single 2×2 comparison. Goodman-Bacon (2021) showed that it equals a weighted average of all the 2×2 DiDs the data admit — including comparisons that use **already-treated units as controls**. Those comparisons are biased when treatment effects grow over time, because the "control" group is still changing under the treatment it received earlier. The weights can even be negative, so the estimate can have the wrong sign.

The remedies are estimators that make the comparison explicit:

- **Callaway and Sant'Anna (2021)** — estimate group-time average treatment effects using only never-treated or not-yet-treated units as controls, then aggregate with chosen weights.
- **Sun and Abraham (2021)** — interact relative-time indicators with cohort indicators, so that already-treated cohorts never serve as controls.
- **Borusyak, Jaravel and Spiess (2024)** — imputation: fit the untreated outcome model on untreated observations, then compare observed outcomes with the imputed counterfactual.
- **Synthetic control** — construct the counterfactual as a weighted combination of untreated units, for the single-treated-unit case.

The practical rule: with staggered timing, do not report a plain two-way fixed-effects coefficient as *the* effect. Report the group-time estimates and the aggregation rule.

## Inference

DiD estimates are usually serially correlated within units, and naive standard errors are too small. Cluster at the level of treatment assignment — the state, the region, the firm — not the individual. With few clusters, the cluster-robust asymptotics fail and the usual correction is a wild cluster bootstrap (Cameron, Gelbach and Miller, 2008). Bertrand, Duflo and Mullainathan (2004) is the paper that made the point unavoidable: ignoring serial correlation in DiD can overstate significance by an order of magnitude.

## In the corpus

The [Causal Reasoning](/view.html?p=notes/epistemica/causality/causality.md) note uses DiD as the instrument for questions like whether tariffs helped an industry reach minimum efficient scale — a policy that arrives at a date, in a set of sectors, with no randomisation. The design's demands are exactly the ones that note's questions impose: name the treated and control groups, show the pre-trend, and do not let the comparison group be a sector that received the same policy earlier.

## References

- Ashenfelter, O., & Card, D. (1985). Using the longitudinal structure of earnings to estimate the effect of training programs. *The Review of Economics and Statistics*, 67(4), 648–660. — the paper that made the pre-treatment dip a named threat.
- Card, D., & Krueger, A. B. (1994). Minimum wages and employment: A case study of the fast-food industry in New Jersey and Pennsylvania. *The American Economic Review*, 84(4), 772–793. — the canonical 2×2 policy application.
- Bertrand, M., Duflo, E., & Mullainathan, S. (2004). How much should we trust differences-in-differences estimates? *The Quarterly Journal of Economics*, 119(1), 249–275. — serial correlation and the inference problem.
- Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. *Journal of Econometrics*, 225(2), 254–277. — the decomposition of two-way fixed effects into 2×2 comparisons.
- Callaway, B., & Sant'Anna, P. H. C. (2021). Difference-in-differences with multiple time periods. *Journal of Econometrics*, 225(2), 200–230. — the group-time estimator for staggered adoption.
- Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics*, 225(2), 175–199. — the interaction-weighted event study.
- Borusyak, K., Jaravel, X., & Spiess, J. (2024). Revisiting event-study designs: Robust and efficient estimation. *The Review of Economic Studies*, 91(6), 3253–3285. — the imputation estimator.
- Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *The Review of Economics and Statistics*, 90(3), 414–427. — the wild cluster bootstrap for few clusters.
- [Difference in differences — Wikipedia](https://en.wikipedia.org/wiki/Difference_in_differences)
