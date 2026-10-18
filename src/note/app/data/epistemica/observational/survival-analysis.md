---
tags: [technique]
---

# Survival Analysis


> Survival analysis is a statistical method used to analyze and model the time until an event occurs, such as failure, death, or other specified events.
> 

> **Survival Analysis Techniques:** Approaches for analyzing time-to-event data, including Kaplan-Meier survival curves and Cox proportional hazards regression.
> 

## Breviarum

- A **time-to-event** modelling framework.
- Focuses on:
    - The **hazard function** → instantaneous risk of event at time *t*.
    - The **survival function** → probability of surviving beyond *t*.
- Can be parametric (Weibull, exponential), semi-parametric (Cox model), or non-parametric (Kaplan–Meier).
- Not about latent factor extraction — instead, it’s about estimating **risk over time** given covariates, often with censoring.

## Model

> Note: Model here is meant to designate a modelling template.
> 

| **Model** | **Description** | **Typical Use Case** | **Notes** |
| --- | --- | --- | --- |
| **Kaplan–Meier Estimator** | Non-parametric estimate of survival function using product-limit method. | Descriptive survival curves for dropout, churn, patient survival. | No covariates; visualizes time-to-event; handles right-censoring well. |
| **Nelson–Aalen Estimator** | Non-parametric cumulative hazard estimator. | Estimating and comparing hazard rates over time. | Often paired with KM for hazard/survival comparison. |
| **Cox Proportional Hazards (PH) Model** | Semi-parametric; estimates effect of covariates on hazard, assumes proportional hazards. | Academic dropout modelling with socio-economic & performance covariates. | Baseline hazard unspecified; interpretable hazard ratios; PH assumption must hold. |
| **Stratified Cox Model** | Cox model with strata that have different baseline hazards. | Dropout analysis stratified by school or department. | Keeps PH assumption within strata; no hazard ratio for stratification variable. |
| **Extended Cox Model** | Allows time-varying covariates or non-proportional hazards. | Modelling dropout risk where GPA changes each semester. | Flexible but more complex; careful data structuring needed. |
| **Exponential Model** | Parametric model with constant hazard over time. | Simple baseline for dropout when risk is assumed constant. | Unrealistic for most real-world cases; easy to interpret. |
| **Weibull Model** | Parametric model with monotonic hazard (increasing or decreasing). | Dropout risk that consistently rises or falls over time. | Can be PH or AFT; more flexible than exponential. |
| **Log-normal Model** | Parametric AFT model; log of survival times follows a normal distribution. | Events that have a “peak time” risk then decrease (e.g., burnout dropouts). | Not proportional hazards; interprets covariates in time-multiplication terms. |
| **Log-logistic Model** | Parametric AFT; can model non-monotonic hazards (rise then fall). | Student dropout risk peaking mid-degree. | Can handle long tails better than log-normal. |
| **Gompertz Model** | Parametric PH with exponentially changing hazard. | Age-related risks in retirement dropout or health studies. | Common in demography and reliability. |
| **Aalen’s Additive Hazards Model** | Models hazard as additive function of covariates. | Dropout studies where effects of factors are additive rather than multiplicative. | No proportionality assumption; less common than Cox. |
| **Fine–Gray Competing Risks Model** | Models subdistribution hazards for competing risks. | Dropout vs. transfer to another institution. | Estimates cumulative incidence for each event type. |
| **Cause-specific Hazard Model** | Models hazards for each competing risk separately. | Separate models for dropout vs. graduation vs. transfer. | PH assumption within each cause. |
| **Andersen–Gill Model** | Extension of Cox for recurrent events. | Students re-enrolling and then dropping out multiple times. | Requires careful handling of dependence between events. |
| **Prentice–Williams–Peterson Models** | Recurrent event models with ordered event structure. | Dropout after successive academic warnings. | Handles event order explicitly. |
| **Random Survival Forest (RSF)** | Ensemble ML method for censored data. | Predict dropout timing with complex nonlinear interactions. | No PH assumption; variable importance measures; less interpretable. |
| **Gradient Boosted Survival Models** | Boosted trees adapted for censored survival data. | High-dimensional dropout prediction with complex covariates. | More predictive but less transparent. |
| **DeepSurv** | Neural network generalization of Cox PH. | Dropout prediction from rich student behavioral data (e.g., clickstream). | Needs large datasets; interprets via hazard ratio-like outputs. |
| **Bayesian Survival Models** | Priors on hazard/survival parameters; Bayesian inference. | Dropout prediction with small data and domain-informed priors. | Flexible; credible intervals replace confidence intervals. |
| **Joint Models (Longitudinal + Survival)** | Links longitudinal measurement model with survival model. | Modelling GPA trajectories and dropout jointly. | Handles measurement error; more computationally demanding. |

## Case Studies

| **Problem** | **Description** | **Why Survival Analysis Fits** |
| --- | --- | --- |
| **Student dropout** | Predict when students will leave before completing their degree, given academic, socio-economic, and behavioral data. | Explicitly models **time-to-event**, accounts for **censoring** (students still enrolled), and quantifies **risk over time**. |
| **Employee turnover** | Model the time until an employee resigns or is terminated. | Handles **right-censored** data (employees still at company) and allows hazard ratio interpretation for HR policy decisions. |
| **Customer churn** | Predict how long a customer will remain subscribed to a service. | Captures **tenure effects**, seasonal risk changes, and supports **time-varying covariates** (e.g., usage patterns). |
| **Machine/component failure** | Estimate the remaining useful life of equipment under different operating conditions. | Developed in reliability engineering; naturally models **failure times** with possible **left truncation** and censoring. |
| **Disease progression** | Time from diagnosis to a health event (e.g., relapse, death). | Handles **competing risks** (different event types) and partial follow-up periods. |
| **Loan default** | Predict when borrowers will default, if at all. | Captures temporal risk dynamics and accommodates loans still active at observation end. |
| **Time to software defect** | Estimate how long until a software module experiences a critical bug after deployment. | Allows for time-based risk modelling while incorporating operational metrics. |
| **Adoption of innovation** | Time until a person or organization adopts a technology or policy. | Models adoption curves while accounting for non-adopters in the dataset. |
| **Recidivism risk** | Estimate how long after release an individual may re-offend. | Incorporates censoring for individuals who have not re-offended during study period. |
| **Time to promotion** | How long until an employee is promoted to a certain level. | Captures career progression timing while adjusting for different individual paths. |

## References

- https://en.wikipedia.org/wiki/Survival_analysis
