---
tags: [epistemology, statistics, discipline, framework]
---

# Statistics

> In this set of notes, Statistics is treated as a **discipline** — an **Epistemic Aggregate**: the organized inquiry into variation, uncertainty, and inference from data — how warranted claims are extracted from observations that differ across samples and populations.

> **Statistics** is the discipline dedicated to the **design of data production**, the **quantification of uncertainty**, and the **inference** from samples to populations. It encodes the regularity of **variation** — the fact that observations differ, that measurement errs, and that outcomes are not deterministic — into formal systems of probability, estimation, and hypothesis testing, thereby providing rigorous grounds for prediction, comparison, and decision under uncertainty. Data inspires our models, and through those models we describe, predict, and act on an uncertain world.

Statistics is mathematics turned on the world's irreducible variation: where
mathematics deduces within a fixed formal system, statistics **infers beyond
the observed** — from sample to population, from present to future, from
signal to noise. Its product is a *warranted claim under uncertainty*; its
warrant is calibration, not proof.

This note is the discipline-level Aggregate; its evaluative sibling
**validation** (checking a model against reality) lives in the
[`validation/`](index.html?dir=epistemica/validation) folder, and the schema it
instantiates is owned by the canonical
[Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md).

: Probability (Probability%204210c322839242cd8cc944b9b1e7c27f.md), Theory of Probability (Theory%20of%20Probability%20272c0f5171ec80c1bcafcd23a25b4f50.md), Theory of Statistics (Theory%20of%20Statistics%20272c0f5171ec80ce988eebaba3a61964.md), Comparison (Comparison%20275c0f5171ec800590bfc9a57e022fc9.md)

> Statistics (Datomatica), aka. The Logic of Data.
> 

> Statistics is a toolbox—including representation, inference, and description—that operates on the ontic traces of a piece of reality to produce elements encoding aspects of the affirmation space of that reality.
> 

> **Statistics** is a set of **`tools`** **(formal representations)** + **(techniques)** used to **`extract`** **meaningful insights**(description - aka **statistic**, and underlying process capturing) from a dataset.  M**eaningful insights means capturing part of the affirmation space about the generator.**
> 

> **Statistics is the discipline that provides systematic methods** to describe, summarize, and visualize data, as well as to model the underlying processes that generate the data and quantify the uncertainty inherent in those processes.
> 

> Statistics represents a  **human epistemic phase** transition represents a shift from **case-instance-based reasoning** to the **formal study of a collection of data points** about a phenomenon or system.
> 

> “Statistics is a huge misnomer; if it were named accurately for its modern purpose, it should be called **datomatica**—the systematic study of data.”
> 

> Note: A superficial understanding of statistics can be more misleading than having no knowledge at all.
> 

![modelling.jpeg](../assets/note/epistemica/discipline/statistics/modelling.jpeg)

[https://pbs.twimg.com/media/GPFHPSCWwAAvrXq?format=jpg&name=large](https://pbs.twimg.com/media/GPFHPSCWwAAvrXq?format=jpg&name=large)

![Untitled](../assets/note/epistemica/discipline/statistics/untitled.png)

## Formulation

### What is this epistemic instance?

> Statistics is the organized inquiry system into variation and uncertainty: it designs how data are produced, quantifies how much a claim is exposed to chance, and infers from finite samples to the populations and futures they were drawn from. Its product is a calibrated statement of support, uncertainty, and generalization; its warrant is that the procedure behaves as advertised over repeated use.

### What epistemic element type does this epistemic instance belong to?

> An **`Aggregate`** — the organized inquiry system of statistics: one coherent body scoping orientation, target, representations, operations, evaluations, communication, and infrastructure around the quantification of uncertainty and inference from data.

### Is the type of this `epistemic element instance` ambiguous?

> No at the root: statistics is a structured collection of epistemic elements organized as one coherent epistemic whole, so `Aggregate` is its primary type. Two boundaries are worth stating. Against **mathematics**: probability theory is the mathematical scaffold statistics uses, but statistics adds what pure mathematics does not supply — a *data-producing design* and a *repeated-sampling warrant*. Against **epistemic evaluation / validation**: a p-value or a calibrated model is a statistical *construction*, while validating a scientific model against reality is the *evaluation* branch; the two are adjacent but not identical, and calibration is a distinct practice, not a synonym for validation (see [`validation/calibration.md`](note.html?n=epistemica/validation/calibration.md)).

### What is the recursive instance decomposition of this epistemic instance?

> The table below decomposes statistics as an organized inquiry system, grown along the branches of inquiry. A deep core (orientation, target, access, representation, operation, evaluation) is developed to levels 4–5; the rest is carried to level 3–4. Each leaf resolves to a concrete instance.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Statistics | The organized inquiry into variation, uncertainty, and inference from data: one body of statistical knowledge with its orientation, target, representations, operations, evaluations, and infrastructure. |
| `Aggregate` → Statistics → `Epistemic Orientation` | Grouping: the directing structure of the inquiry. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Purpose` | Grouping: purposes of the inquiry. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Purpose` → Uncertainty Quantification Purpose | Telos: state how much of a claim is exposed to chance, in a calibrated scale. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Purpose` → Generalization Purpose | Telos: warrant a claim about a population or future from a finite sample. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Purpose` → Comparison Purpose | Telos: determine whether an observed difference exceeds what chance alone produces. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Question` | Grouping: questions directing the inquiry. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Question` → Significance Question | Formulated question: is this observed effect distinguishable from sampling noise? |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Question` → Estimation Question | Formulated question: what is the value of this population quantity, and with what precision? |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Question` → Design Question | Formulated question: how should data be produced so the inference it supports is valid? |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Goal` | Grouping: desired outcomes. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Goal` → Calibrated Claim Goal | Desired outcome: a claim whose stated uncertainty matches its long-run frequency of error. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Gap` | Grouping: gaps motivating the inquiry. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Gap` → Unquantified Uncertainty Gap | Deficiency: an observed difference whose chance component has not yet been bounded. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Role` | Grouping: roles performed within the inquiry. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Role` → Statistician | Principal inquirer: designing studies, fitting models, and judging uncertainty. |
| `Aggregate` → Statistics → `Epistemic Orientation` → `Epistemic Role` → Data Subject | The entity whose observations are registered — the human, cell, or market the sample is drawn from. |
| `Aggregate` → Statistics → `Epistemic Agency` | Grouping: entities and organized activities performing the discipline's work. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Agent` | Grouping: agents performing statistical operations. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Agent` → Statistician | Entity designing, estimating, and testing; analysts and software realize this agent. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Act` | Grouping: primitive acts of the statistician. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Act` → Sampling Act | Primitive act selecting a subset of the population to observe. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Act` → Measuring Act | Primitive act registering a value of a variable on a unit. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Act` → Estimating Act | Primitive act computing a statistic as a point or interval for a parameter. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Act` → Testing Act | Primitive act computing how extreme the observed data are under a null model. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Activity` | Grouping: organized sequences of acts. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Activity` → Designing | Fixing the sampling frame, randomization, and sample size before data are seen. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Activity` → Exploring | Summarizing and visualizing data to find structure before formal testing. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Activity` → Modeling | Fitting a probability model to the data-generating process. |
| `Aggregate` → Statistics → `Epistemic Agency` → `Epistemic Activity` → Testing | Quantifying the evidence against a stated null hypothesis. |
| `Aggregate` → Statistics → `Epistemic Target` | Grouping: the addressed domain of inquiry. |
| `Aggregate` → Statistics → `Epistemic Target` → `Target Domain` | Grouping: domains addressed. |
| `Aggregate` → Statistics → `Epistemic Target` → `Target Domain` → Population | Bounded domain: the full set of units the claim generalizes to. |
| `Aggregate` → Statistics → `Epistemic Target` → `Target Segment` | Grouping: segments selected for study. |
| `Aggregate` → Statistics → `Epistemic Target` → `Target Segment` → Sample | The observed subset drawn from the population by the sampling design. |
| `Aggregate` → Statistics → `Epistemic Target` → `Observable` | Grouping: registrable features of the target. |
| `Aggregate` → Statistics → `Epistemic Target` → `Observable` → Variable | Registrable feature: a measurable property taking values across units. |
| `Aggregate` → Statistics → `Epistemic Target` → `Observable` → Parameter | The fixed but unknown population quantity the sample estimates. |
| `Aggregate` → Statistics → `Epistemic Target` → `Observable` → Effect Size | Registrable feature: the magnitude of a difference or association, not merely its presence. |
| `Aggregate` → Statistics → `Epistemic Access` | Grouping: means by which the target becomes registrable. |
| `Aggregate` → Statistics → `Epistemic Access` → `Observation Interface` | Grouping: interfaces coupling the population to a record. |
| `Aggregate` → Statistics → `Epistemic Access` → `Observation Interface` → Randomized Trial | Interface assigning units to conditions by chance, breaking confounding by design. |
| `Aggregate` → Statistics → `Epistemic Access` → `Observation Interface` → Survey Instrument | Interface eliciting responses from a sampled set of subjects. |
| `Aggregate` → Statistics → `Epistemic Access` → `Observation Record` | Grouping: registered representations of observations. |
| `Aggregate` → Statistics → `Epistemic Access` → `Observation Record` → Data Table | Registered rows of units and columns of measured variables. |
| `Aggregate` → Statistics → `Epistemic Representation` | Grouping: structures through which content is encoded and manipulated. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` | Grouping: sign systems of the discipline. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` → Probability Distribution | Function assigning likelihoods to the outcomes of a random variable. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` → Probability Distribution → Normal Distribution | Exemplar distribution realizing the type: the bell curve governing sums of many small effects. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` → Probability Distribution → Binomial Distribution | Exemplar distribution realizing the type: counts of successes in fixed independent trials. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` → Likelihood Function | Mapping from parameter values to the plausibility of the observed data. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` → Sampling Distribution | Distribution of a statistic over repeated samples — the bridge from data to uncertainty. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` → `Constitutive Substrate` | Grouping: rules constituting the representations. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` → `Constitutive Substrate` → Probability Axiom | The non-negativity, unit-mass, and additivity rules every distribution satisfies. |
| `Aggregate` → Statistics → `Epistemic Representation` → `Representational System` → `Constitutive Substrate` → Estimand Convention | What exactly is being estimated — the target quantity the procedure aims at. |
| `Aggregate` → Statistics → `Epistemic Operation` | Grouping: operations transforming data into inference. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Action` | Grouping: direct transformations of the data. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Action` → Summary Statistic | Compressing a sample to a mean, variance, or quantile. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Action` → Interval Estimation | Producing a confidence or credible interval for a parameter. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Action` → Hypothesis Test | Computing the extremeness of the data under a null model to a p-value. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` | Grouping: coordinated routines and generalized ways. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` → `Method` | Grouping: generalized methods of inference. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` → `Method` → Maximum Likelihood | Choosing the parameter value that makes the observed data most probable. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` → `Method` → Regression | Estimating the conditional relationship of a response to explanatory variables. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` → `Method` → Resampling | Estimating a sampling distribution by repeatedly drawing from the observed data. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` → `Method` → Resampling → Bootstrap | Exemplar resampling method: sampling with replacement to approximate uncertainty. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` → `Principle` | Grouping: rules guiding the operations. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` → `Principle` → Randomization Principle | Chance assignment, not adjustment, is what breaks confounding in a trial. |
| `Aggregate` → Statistics → `Epistemic Operation` → `Organization` → `Principle` → Sufficient Statistic Principle | A statistic is sufficient when it captures all the sample carries about the parameter. |
| `Aggregate` → Statistics → `Epistemic Evaluation` | Grouping: assessments of the discipline's outputs. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: standards judging results. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Epistemic Standard` → Calibration Standard | A stated uncertainty stands only if, over repeated use, the claimed coverage matches. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Epistemic Standard` → Error-Rate Standard | A test stands only if its false-positive rate is held at the declared level. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Epistemic Criterion` | Grouping: evaluated properties. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Epistemic Criterion` → Bias-Variance Criterion | An estimator is judged by the trade-off between systematic and sampling error. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Epistemic Criterion` → Power Criterion | A test is judged by its ability to detect an effect of stated size. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Validation` | Grouping: checks discharging doubt. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Validation` → Model Check | Comparing the fitted model's implications against the observed data. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Validation` → Replication | Re-running the study to see whether the inference reproduces. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Error` | Grouping: deviations from the true state. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Error` → Type I Error | Rejecting a true null hypothesis — a false positive. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Error` → Type II Error | Failing to reject a false null hypothesis — a false negative. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Feedback` | Grouping: evaluations returned to the design. |
| `Aggregate` → Statistics → `Epistemic Evaluation` → `Feedback` → Sample-Size Revision | Enlarging the sample after a power analysis exposes low detection. |
| `Aggregate` → Statistics → `Epistemic Communication` | Grouping: transmission of statistical content. |
| `Aggregate` → Statistics → `Epistemic Communication` → `Epistemic Inscription` | Grouping: persistent renderings. |
| `Aggregate` → Statistics → `Epistemic Communication` → `Epistemic Inscription` → Reported Estimate | A point estimate with its interval and stated uncertainty, recorded for scrutiny. |
| `Aggregate` → Statistics → `Epistemic Communication` → `Epistemic Publication` | Grouping: published expositions. |
| `Aggregate` → Statistics → `Epistemic Communication` → `Epistemic Publication` → Statistical Report | Sustained account of a study's design, analysis, and uncertainty. |
| `Aggregate` → Statistics → `Epistemic Infrastructure` | Grouping: structures enabling the inquiry. |
| `Aggregate` → Statistics → `Epistemic Infrastructure` → `Epistemic Tool` | Grouping: tools performing the statistics. |
| `Aggregate` → Statistics → `Epistemic Infrastructure` → `Epistemic Tool` → Statistical Software | Software fitting models, computing intervals, and running tests. |
| `Aggregate` → Statistics → `Epistemic Infrastructure` → `Epistemic Tool` → Statistical Software → R | Exemplar tool realizing the type: the language and runtime of applied statistics. |
| `Aggregate` → Statistics → `Epistemic Infrastructure` → `Information Repository` | Grouping: stored data and reference. |
| `Aggregate` → Statistics → `Epistemic Infrastructure` → `Information Repository` → Dataset | Stored table of units and variables consulted instead of re-collected. |
| `Aggregate` → Statistics → `Epistemic Infrastructure` → `Epistemic Institution` | Grouping: bodies sustaining the discipline. |
| `Aggregate` → Statistics → `Epistemic Infrastructure` → `Epistemic Institution` → Pre-Registration Registry | Institution fixing the analysis plan before data are seen, curbing selective reporting. |
| `Aggregate` → Statistics → `Epistemic Context` | Grouping: conditions surrounding the inquiry. |
| `Aggregate` → Statistics → `Epistemic Context` → `Epistemic Condition` | Grouping: conditions under which results are interpreted. |
| `Aggregate` → Statistics → `Epistemic Context` → `Epistemic Condition` → i.i.d. Condition | Results conditional on units being independent and identically distributed. |
| `Aggregate` → Statistics → `Epistemic Context` → `Epistemic Condition` → Observational Condition | Results from non-randomized data are conditional on all confounders being measured. |

### What Is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdict.** Statistics is conceptually strong where it matters most — its boundary rule (a claim is statistical iff its warrant is a repeated-sampling or posterior calibration) is determinate, and its purpose-adequacy is proven by its role as the discipline of warranted inference under uncertainty. Its principal risk is *misuse*: a formally correct procedure is routinely read as bearing more warrant than its design supports, so misuse-resistance is the criterion where the discipline is weakest.

| Criterion | Verdict | Diagnostic Focus |
| --- | --- | --- |
| Conceptual Identification | Strong | Distinguished from probability theory (its mathematical scaffold) by the added data-design and repeated-sampling warrant; distinguished from validation by calibrating claims, not adjudicating a model against reality. |
| Definitional Clarity | Strong | Estimand, sampling design, and calibration are stated conditions; the note separates the p-value (an extremeness measure) from effect size (a magnitude), avoiding the common conflation. |
| Conceptual Determinacy | Strong | Borderline cases (Bayesian posteriors vs frequentist intervals) are handled by declaring the warrant type, not by excluding a school. |
| Internal Consistency | Strong | Error rates, power, and calibration are mutually compatible; Type I / Type II are defined against a fixed null. |
| Representational Adequacy | Strong | The `Aggregate` reading captures the discipline; the sampling distribution is correctly placed as the bridge from data to uncertainty, not as a property of the world. |
| Purpose Adequacy | Strong | Uncertainty quantification, generalization, and comparison are all served; the note never claims the procedure proves a causal mechanism on its own. |
| Misuse Resistance | **Weak–Moderate** | The p-value is habitually misread as the probability the null is true; statistical significance is conflated with practical importance. The discipline's notation invites this, and only design literacy (randomization, pre-registration) check it. |

Its limits follow from the same source as its strength. The i.i.d. assumption
and the observational condition are load-bearing and usually unverifiable from
the data themselves: a calibrated procedure over repeated use says nothing
guaranteeing *this* instance, and an observational study inherits whatever
confounding its design did not break. The discipline is also silent about what
its models do not encode — a fitted distribution is a compression, and the
world's tail behavior routinely exceeds it. Overall the instance is mature and
heavily validated; what its warrant is conditional on is the honesty of the
design and the honesty of the reader.

## Meta

> Evaluation Framework.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | ⭐⭐⭐: Moderately useful. Covers essential ideas but may lack depth, cohesion, or polish. |
| **Completeness** | ⭐⭐⭐⭐: Very comprehensive coverage of most statistical concepts, with good depth in core areas but some gaps in specialized or emerging topics. |
| **Coherence & Structure** | ⭐⭐⭐: Well-organized with clear sections, but could benefit from better integration of related concepts and reduced redundancy between sections. |
| **Epistemic Self-Assessment** | ⭐⭐ Basic - Partial understanding; can handle simple situations but lacks depth, integration, or flexibility. |
| **Should I Reorganize This -in My Content Forest?** | Consider creating a more logical progression from basic to advanced concepts, better integrating theoretical foundations with practical applications, and making connections between different statistical methods more explicit. |
| **What's my study Strategy? Should I Change It?** | Start with foundational concepts (probability, descriptive statistics), build to inference methods and hypothesis testing, then explore different statistical models. Include practical exercises and real-world case studies, incorporate computational tools, and regularly connect concepts to solve actual problems rather than just theoretical understanding. |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

> **Statistics: Toolbox** `×` **{Problem,  Representation} →  {Representation,  Inference}.**
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | **Statistics** is the science of learning from data, transforming raw information into knowledge through systematic methods of collection, analysis, interpretation, and presentation. At its core, it represents a human epistemic phase transition from case-instance-based reasoning to the formal study of collections of data points about phenomena or systems. |
| **Evidentia (Evidence) 📊** | Statistical evidence includes data patterns, probability distributions, test statistics, confidence intervals, and Bayesian posteriors. Claims are verified through hypothesis testing, cross-validation, replication studies, and sensitivity analyses. The strength of statistical evidence is quantified through p-values, effect sizes, and confidence levels. |
| **Telos (Intent) 🎯** | Statistics aims to extract meaningful insights from data, quantify uncertainty, make predictions, test hypotheses, identify causal relationships, and support decision-making. It provides tools for describing data, modeling underlying processes, and generalizing findings from samples to populations. |
| **Gnosis (Understanding) 🧠** | Develop a mental representation that integrates descriptive statistics, probability theory, inference methods, and modeling techniques. Build hierarchical understanding from basic concepts (mean, variance) to advanced methods (Bayesian networks, causal inference). Connect statistical thinking to real-world problem-solving through practical applications and case studies. |
| **Epignosis (Application) 🛠️** | Apply statistical methods to experimental design, data analysis, model building, and interpretation. Master techniques for handling real-world data challenges like missing values, outliers, and confounding variables. Develop skills in statistical programming, visualization, and communication of results to diverse audiences. |
| **Relatio (Connections) 🔗** | Statistics intersects with mathematics (probability, calculus), computer science (algorithms, machine learning), domain-specific sciences (biology, economics, social sciences), and philosophy (epistemology, scientific method). It provides the foundation for data science, artificial intelligence, and evidence-based decision-making across disciplines. |
| **Idoneitas (Suitability) 📐** | Statistics is effective when methods match the data structure and research questions. Its value is measured by predictive accuracy, explanatory power, practical significance, and reproducibility. Good statistics balances rigor with relevance, complexity with interpretability, and theoretical soundness with practical applicability. |
| **Limites (Limits) ⛔** | Statistics cannot prove causation without experimental design, overcome small sample sizes, eliminate all uncertainty, or handle highly complex systems with computational irreducibility. It has limitations in handling high-dimensional data, ensuring representativeness, and addressing ethical concerns in data collection and interpretation. |
| **Contextus (Context) 🌍** | Statistics evolved from early demographic studies to modern data science, shaped by computational advances and big data challenges. Cultural context influences statistical practices, from p-value controversies to Bayesian vs. frequentist debates. Applications vary across domains, from clinical trials to social sciences, requiring contextual interpretation. |
| **Dynamis (Evolution) 🌱** | Statistics is evolving with computational advances, machine learning integration, and causal inference methods. Emerging trends include high-dimensional statistics, network analysis, and real-time data processing. The field adapts to new data types (unstructured, streaming) and ethical considerations (algorithmic fairness, privacy). |
| **Critica (Critique) 🔍** | Criticisms include p-value misuse, overemphasis on significance testing, publication bias, and replication crises. Debates surround Bayesian vs. frequentist approaches, statistical vs. practical significance, and the balance between model complexity and interpretability. Ethical concerns address data privacy, algorithmic bias, and responsible communication of results. |
| **Verbum Usus (Language Use) 🗣️** | Statistical language ranges from technical (p-value, confidence interval, ANOVA) to accessible (significant, correlation, average). Misuse of terms like "proof" and "significance" in popular discourse creates confusion. The field's terminology continues evolving, with recent emphasis on concepts like "reproducibility" and "causal inference" gaining prominence. |

### 🏷️ Terminology

| **Term** | **Definition** |
| --- | --- |
| **Population** | An abstract concept that captures the entire set of individuals or observations of interest in a study. |
| **Parameter** | A numerical characteristic of a population (e.g., mean, variance, regression coefficient, …). |
| **Sample** | A subset of the population used to make inferences about the whole. |
| **Statistic** | A numerical characteristic calculated from a sample. |
| **Estimator** | A rule or formula for calculating an estimate of a population parameter from sample data. |
| **Random Variable** | A variable whose value is subject to randomness or uncertainty. |
| **Probability Distribution** | A function describing the likelihood of each possible outcome of a random variable. |
| **Mean (Expected Value)** | The average or central value of a random variable. |
| **Variance** | A measure of the spread or dispersion of a set of values. |
| **Standard Deviation** | The square root of variance, indicating the typical distance from the mean. |
| **Correlation** | A measure of the linear relationship between two variables. |
| **Regression** | A method to model the relationship between a dependent variable and one or more independent variables. |
| **Hypothesis** | A statement or claim about a population parameter that can be tested statistically. |
| **p-value** | The probability of observing results at least as extreme as those measured, assuming the null hypothesis is true. |
| **Confidence Interval** | A range of values within which a population parameter is estimated to lie with a certain probability. |
| **Bayesian Statistics** | A statistical approach that incorporates prior beliefs and updates probabilities as new data is observed. |

### 🕰️ History

> History of Statistical Thinking.
> 

| **Period** | **Place** | **Development** |
| --- | --- | --- |
| 1600s | Europe (England, Netherlands) | Early collection of demographic data; John Graunt analyzes London mortality records (“Bills of Mortality”) to study population patterns. |
| 1700s | Europe (France, Germany) | Development of probability theory by Jakob Bernoulli, Abraham de Moivre; emergence of actuarial science and life insurance mathematics. |
| 1800s | Europe (France, UK) | Formalization of statistical methods for social and economic data; Adolphe Quetelet introduces “social physics” and the concept of the average man. |
| 1850s–1900s | Europe (UK, Germany) | Development of correlation and regression (Francis Galton, Karl Pearson); rise of biometrics and statistical inference foundations. |
| 1920s–1930s | Europe & USA | R.A. Fisher develops modern statistical inference, maximum likelihood, ANOVA, and experimental design. |
| 1940s–1950s | USA | Application of statistics to industrial quality control (Shewhart, Deming) and social sciences; beginnings of multivariate analysis. |
| 1960s–1980s | Global | Expansion of computational statistics; development of Bayesian methods, non-parametric statistics, and stochastic processes. |
| 1990s–present | Global | Growth of data science, machine learning, and big data analytics; widespread use of computational and simulation-based statistical methods. |

### 🎋 Field

| **Category** | **Field** | **Description** |
| --- | --- | --- |
| **Foundations** | **Theoretical Statistics** | Mathematical foundations of statistical inference (estimation theory, hypothesis testing, asymptotics, information theory). |
|  | **Probability Theory (Statistical Basis)** | Underlying probabilistic framework for statistical reasoning (measure theory, random variables, limit theorems). |
|  | **Decision Theory** | Principles for optimal decision-making under uncertainty using loss/utility functions. |
|  | **Asymptotic Statistics** | Behavior of estimators and tests as sample size grows (consistency, CLT, efficiency, limit distributions). |
| **Core Methods** | **Descriptive Statistics** | Summarization of data with measures (mean, variance, skewness) and visualization. |
|  | **Inferential Statistics** | Drawing conclusions about populations from samples (confidence intervals, hypothesis tests). |
|  | **Frequentist Statistics** | Inference based on long-run frequency properties (p-values, maximum likelihood, ANOVA). |
|  | **Bayesian Statistics** | Inference via Bayes’ theorem, combining prior beliefs with data evidence. |
|  | **Nonparametric Statistics** | Methods that do not assume a fixed parametric distribution (rank tests, kernel methods). |
|  | **Semi-parametric Statistics** | Models with both parametric and nonparametric components (Cox proportional hazards, partially linear models). |
|  | **Robust Statistics** | Methods resistant to violations of model assumptions and outliers. |
| **Data Structures & Models** | **Regression Analysis** | Relationship modeling between variables (linear, generalized linear, nonlinear regression). |
|  | **Multivariate Statistics** | Analysis of multiple dependent variables (PCA, factor analysis, MANOVA). |
|  | **Categorical Data Analysis** | Methods for qualitative/categorical outcomes (logistic regression, contingency tables). |
|  | **Survival Analysis** | Analysis of time-to-event data, handling censoring and hazard functions. |
|  | **Longitudinal Data Analysis** | Models for repeated measures over time on the same subjects. |
|  | **Mixed Models / Hierarchical Models** | Models with both fixed and random effects, handling clustered data. |
| **Data Collection & Experimentation** | **Experimental Design** | Planning experiments to ensure valid inference (randomization, blocking, factorial design). |
|  | **Survey Sampling** | Methods for drawing representative samples and estimating population parameters. |
|  | **Sampling Theory** | Mathematical study of properties of sampling procedures. |
| **Dependence & Dynamics** | **Time Series Analysis** | Modeling temporal dependence in data (ARIMA, state-space models, forecasting). |
|  | **Spatial Statistics** | Analyzing spatial/geographical data (kriging, point processes). |
|  | **Stochastic Processes in Statistics** | Use of random processes to model evolving data. |
| **Computation & Algorithms** | **Computational Statistics** | Algorithmic/statistical computing (Monte Carlo, bootstrap, EM algorithm). |
|  | **Simulation-Based Inference** | Using resampling or simulation methods (MCMC, importance sampling). |
|  | **Statistical Learning / Machine Learning** | Prediction and pattern discovery (regularization, ensembles, neural networks). |
| **Applications (Domain-Specific)** | **Biostatistics** | Application in biology, health, and medicine (clinical trials, epidemiology). |
|  | **Econometrics** | Statistical methods applied to economics and finance. |
|  | **Psychometrics** | Statistical models for psychological measurement and latent traits. |
|  | **Educational Statistics** | Methods for assessing learning outcomes and tests. |
|  | **Industrial Statistics / Quality Control** | Process control, reliability, Six Sigma, manufacturing optimization. |
|  | **Environmental Statistics** | Analysis of climate, ecology, and environmental risk data. |
|  | **Social Statistics** | Application to sociology, political science, and demographics. |
| **Frontiers** | **High-Dimensional Statistics** | Inference when number of variables is large relative to sample size. |
|  | **Causal Inference** | Statistical methods for identifying and estimating causal relationships. |
|  | **Information-Theoretic Statistics** | Using entropy and divergence to evaluate models and inference. |
|  | **Computationally Intensive Methods** | Large-scale, big data, and distributed statistical computing. |
|  | **Bayesian Nonparametrics** | Infinite-dimensional Bayesian models (Dirichlet processes, Gaussian processes). |

## Guide

- What is the representation capacity of a **statistical model** $L_m$?
- What kinds of ‘questions’ can the **Statistical Model** $L_m$ answer? How does it **answer** it them?
- What are the practical limitations or constraints of **Statistical Model** $L_m$ in real-world applications?
- How do we know that our dataset (sample) is representative?

## Data Collection

> What data do we need? How much? How accurate and precise?
> 

> How do I choose an appropriate sample size, and how should I assess the quality of my statistical procedure based on that sample size?
> 

## Modelling

> Statistical modeling is an art. Every method and technique makes many assumptions, so be careful and mindful of them. Always check clearly whether your problem meets the specifications of the tools you are using.
> 

> **Statistics provides the principles and tools** for drawing valid conclusions from data, just as **logic** provides the principles for valid reasoning.
> 

> Statistical tools are usually developed to solve practical problems and are validated to ensure reliability and accuracy. The theoretical validity of many statistical methods is often justified using convergence results and asymptotic probability arguments, such as the law of large numbers or the central limit theorem.
> 

> Every statistical analysis is a long process of transforming complex data step by step—like navigating a tree—using statistical tools to generate meaningful conclusions or results. Unfortunately, the outcomes are not as clean or certain as deductions in formal logic.
> 

### Problem Space

| **Category (Question)** | **Key Question** | **Procedures** |
| --- | --- | --- |
| **Description (What is happening?)** | What is happening in the data? | Mean, median, mode, variance, standard deviation, histograms, box plots, scatter plots |
| **Inference (Why?)** | What underlying truths can we infer from the data? | Hypothesis testing, p-values, confidence intervals, Bayesian inference |
| **Prediction (What can we conclude?)** | What will happen next or for a new observation? | Regression, classification, forecasting, neural networks |
| **Causation (Why because?)** | What causes what? | Randomized controlled trials, instrumental variables, Granger causality, structural equation modeling |
| **Interaction Effect (How jointly?)** | How do variables jointly influence an outcome? | Two-way ANOVA, regression with interaction terms, moderation analysis |
| **Optimization (How best?)** | What is the best decision under constraints? | Linear programming, convex optimization, gradient descent, dynamic programming |
| **Comparison (How do groups differ?)** | Are there differences between groups? | t-tests, ANOVA, Mann-Whitney U test, Kruskal-Wallis test |
| **Associative (Are variables related?)** | Are variables related? | Correlation, chi-square test, mutual information, association rules |
| **Exploration (What lies beyond?)** | What patterns or structures emerge without predefined hypotheses? | Clustering, PCA, EDA, t-SNE, UMAP |
| **Grouping (How to group?)** | How can we group similar observations? | k-means, hierarchical clustering, DBSCAN, Gaussian mixture models |
| **Anomaly Detection (What deviates?)** | What deviates from the norm? | Z-scores, Isolation Forest, One-Class SVM, Local Outlier Factor |
| **Validation (Is it true?)** | How well does the model reflect reality? | Cross-validation, out-of-sample testing, bootstrap, holdout validation |
| **Simulation (What could happen?)** | What could happen under different scenarios? | Monte Carlo simulation, agent-based modeling, stochastic simulation |
| **Uncertainty Quantification (How confident?)** | How confident are we in estimates or predictions? | Confidence intervals, credible intervals, Bayesian posterior analysis |
| **Classification (What category?)** | What category does this belong to? | Logistic regression, decision trees, SVM, random forests, k-NN |
| **Dimensionality Reduction (How to simplify?)** | How can we reduce data complexity while preserving structure? | PCA, ICA, LLE, autoencoders |
| **Time Dependence (How over time?)** | How does the variable evolve over time? | ARIMA, time series decomposition, exponential smoothing, state-space models |
| **Decision Optimization (How to decide?)** | What actions maximize expected outcomes? | Expected utility maximization, reinforcement learning, Markov decision processes |
| **Regularization (How to avoid overfitting?)** | How can we prevent overfitting? | Ridge, Lasso, Elastic Net, dropout (in neural nets) |
| **Trend Analysis (What are long-term movements?)** | What are the long-term movements in the data? | Moving averages, time series regression, seasonal decomposition |
| **Reliability (How consistent?)** | How consistent and repeatable are the measurements? | Cronbach’s alpha, test-retest reliability, Intraclass Correlation Coefficient (ICC) |
| **Sensitivity Analysis (How sensitive?)** | How do changes in input affect outputs? | One-way sensitivity analysis, tornado diagrams, scenario analysis |
| **Effect Size Measurement (How large?)** | How large and meaningful are observed effects? | Cohen’s d, odds ratio, relative risk, eta-squared |
| **Survival Analysis (How long until event?)** | How long until an event occurs? | Kaplan-Meier estimator, Cox proportional hazards model, life tables |
| **Multilevel Modeling (How to handle nested data?)** | How to model hierarchical or nested data? | Mixed-effects models, hierarchical linear models, random intercept/slope models |
| **(Robustness) How to make inferences that are not unduly affected by outliers or violations of assumptions?** | How to make inferences that are not unduly affected by outliers or violations of assumptions? | M-estimators, median-based estimators, trimmed means, robust regression |
| **(Nonparametric) (Non Distribution Family Assumption) How to analyze data without assuming a specific distribution?** | How to analyze data without assuming a specific distribution? | Rank-based tests, kernel density estimation, permutation tests, Spearman correlation |
| **(Model Evaluation) Which model best describes the data?** | Which model best describes the data? | AIC, BIC, likelihood ratio tests, cross-validated performance, information criteria |
| **(Data Collection) What data?** | What data do we need? How much? How accurate and precise? | Experimental design, sampling strategies, power analysis, measurement error assessment, calibration, missing data handling, imputation, data cleaning, quality control |
| **Resampling (How to assess reliability?)** | How can we assess reliability using the sample? | Bootstrap, jackknife, permutation tests |

### Representation Target

| **Target** | **Description** |
| --- | --- |
| **Population** | The complete set of individuals or units you want to study or talk about. |
| **Sample** | The manageable subset of the population you actually study. |
| **Variable** | Any characteristic that can differ between subjects (height, eye color, yes/no answers). |
| **Outlier** | A data point that looks like it wandered into the wrong neighborhood — unusually different. |
| **Missing Data** | Empty spots or unavailable values in your dataset. |
| **Random Variable** | A placeholder representing uncertain future outcomes governed by chance. |
| **Experiment** | A process where you actively manipulate factors to observe effects. |
| **Observation** | Passive data collection without interference. |
| **Randomisation** | Using chance to assign treatments or groups, reducing bias. |
| **System** | The real-world entity or mechanism under study. |
| **Process** | A sequence of events or operations unfolding over time within the system. |
| **Hidden Variable** | A factor affecting outcomes but not directly observed or measured. |

### Representation Toolbox

> See ([Trainable Computational System Space](note.html?n=epistemica/observational/computational-learning.md) ) for Cl and ([**Representation Toolbox**](note.html?n=epistemica/observational/probability.md)) for Probabilistic ones.
> 

> **Note:** A statistical model is basically a **trainable computational system, but here we will only cover the more traditional ones.**
> 

> Statistical formal representations, often called statistical models, are mathematical or probabilistic descriptions of relationships between variables and data-generating processes.
> 

> Statistical Models = Specification + Evaluation + Optimization.
> 

| **Model** | **Specification** | **Evaluation** | **Optimization (Training)** | **Typical Uses** |
| --- | --- | --- | --- | --- |
| **Linear Regression** | $Y = X\beta + \epsilon, \ \epsilon \sim \mathcal{N}(0, \sigma^2)$ | MSE, $R^2$, AIC | OLS, MLE | Prediction, causal inference |
| **Logistic Regression** | $\text{logit}(p) = X\beta$ | Cross-entropy, AUC, log-loss | MLE, gradient descent | Binary classification |
| **Poisson Regression** | $\log(\mu) = X\beta,\ Y \sim \text{Poisson}(\mu)$ | Deviance, log-likelihood | IRLS, MLE | Count data modeling (insurance, epidemiology) |
| **Probit Regression** | $P(Y=1|X) = \Phi(X\beta)$ | Log-likelihood, ROC | MLE |  |
| **Bayesian Linear Regression** | Prior + likelihood → posterior | Posterior predictive checks | Bayes rule, MCMC | Small data, uncertainty quantification |
| **Gaussian Mixture Model (GMM)** | $p(x) = \sum_k \pi_k \mathcal{N}(\mu_k, \Sigma_k)$ | Log-likelihood, BIC | EM algorithm | Clustering, density estimation |
| **Naive Bayes** | Assumes conditional independence | Accuracy, log-loss | Closed-form MLE | Text classification |
| **Hidden Markov Model (HMM)** | Markov latent states + emission | Likelihood, accuracy | EM (Baum-Welch), Viterbi | Speech, genomics, POS tagging |
| **Principal Component Analysis (PCA)** | Maximize variance of projections | Explained variance | Eigen decomposition | Visualization, compression |
| **Factor Analysis** | Linear latent structure + noise | Likelihood | MLE, EM | Psychology, economics |
| **k-Means** | Partitions data into $k$ centroids | Within-cluster SSE (inertia) | Lloyd’s algorithm | Market segmentation |
| **Hierarchical Clustering** | Nested partitions via linkage | Dendrogram, silhouette score | Greedy tree building | Taxonomies, bioinformatics |
| **Kernel Density Estimation (KDE)** | Smooth PDF estimate | Likelihood, CV | Bandwidth selection | Exploratory analysis |
| **Kernel Smoother** | $\hat{f}(x_0) = \frac{\sum_{i=1}^n K\left(\frac{x_i - x_0}{h}\right) y_i}{\sum_{i=1}^n K\left(\frac{x_i - x_0}{h}\right)}$, with kernel $K$ and bandwidth $h$ | MSE, cross-validation (CV) | Bandwidth selection (CV, plug-in methods) | Nonparametric regression, smoothing noisy data, exploratory analysis |
| **Support Vector Machine (SVM)** | Max-margin hyperplane, kernel trick | Hinge loss, accuracy | Quadratic programming | Image recognition, text |
| **Random Forests** | Voting ensemble of trees | OOB error, accuracy, MSE | Bootstrap + tree splitting | Tabular data, feature importance |
| **Gradient Boosted Trees** | Boosting over weak learners | Log-loss, RMSE | Greedy additive training | Forecasting, competitions |
| **Neural Networks (MLP)** | Layered nonlinear functions | MSE, cross-entropy | Backprop, SGD, Adam | Pattern recognition |
| **Convolutional Neural Networks (CNNs)** | Spatial filters + pooling | Accuracy, F1 | SGD, Adam | Image classification |
| **Recurrent Neural Networks (RNNs)** | Temporal recurrence over input | Perplexity, loss | BPTT, SGD | Language modeling, time series |
| **Naïve Model** | $\hat{y}_{t+1} = y_t$ | RMSE, MAE | None | Benchmark forecast |
| **Mean Model** | $\hat{y}_t = \bar{y}$ | RMSE, MAE | None | Baseline forecast |
| **Seasonal Naïve** | $\hat{y}{t+h} = y{t+h-m}$ | RMSE, MAPE | None | Seasonal benchmark |
| **AR (Autoregressive)** | $y_t = \phi_1 y_{t-1} + \cdots + \phi_p y_{t-p} + \epsilon_t$ | AIC, BIC, RMSE | Yule-Walker, MLE | Time series with autocorrelation |
| **MA (Moving Average)** | $y_t = \epsilon_t + \theta_1 \epsilon_{t-1} + \cdots + \theta_q \epsilon_{t-q}$ | AIC, BIC, RMSE | MLE | Noise modeling |
| **ARMA** | $AR(p) + MA(q)$ | AIC, BIC, RMSE | MLE | Stationary time series |
| **ARIMA** | ARMA + differencing | AIC, BIC, RMSE | MLE | Non-stationary series |
| **SARIMA** | ARIMA + seasonal terms | AIC, BIC, RMSE | MLE | Seasonal time series |
| **ARIMAX** | ARIMA + exogenous regressors | AIC, BIC, RMSE | MLE | Time series with covariates |
| **VAR (Vector AR)** | $Y_t = A_1 Y_{t-1} + \cdots + A_p Y_{t-p} + \epsilon_t$ | AIC, BIC, RMSE | OLS, MLE | Multivariate time series |
| **VARMA** | Vector ARMA model | AIC, BIC, RMSE | MLE | Multivariate stationary series |
| **SES (Simple Exp. Smoothing)** | $y_t = \alpha y_{t-1} + (1-\alpha)\hat{y}_{t-1}$ | RMSE, MAPE | Gradient-based | Short-term forecasts |
| **Holt’s Linear** | SES + trend | RMSE, MAPE | Gradient-based | Trending series |
| **Holt-Winters** | Trend + seasonality | RMSE, MAPE | Gradient-based | Seasonal data |
| **Kalman Filter** | State-space recursion | Likelihood, RMSE | Recursive updates | Tracking, control, DLMs |
| **Dynamic Linear Models (DLM)** | Bayesian state-space | Posterior predictive checks | Kalman filter, MCMC | Forecasting with uncertainty |
| **Structural Time Series** | Decompose into trend, seasonal, irregular | Likelihood, RMSE | Kalman filter, MLE | Decomposition-based forecasting |
| **ARFIMA** | ARIMA + fractional differencing | AIC, BIC, RMSE | MLE | Long memory processes |
| **ARCH** | $\sigma_t^2 = \alpha_0 + \alpha_1 \epsilon_{t-1}^2 + \cdots$ | Likelihood, volatility metrics | MLE | Volatility modeling |
| **EGARCH** | Log variance model | Likelihood, volatility metrics | MLE | Financial volatility |
| **Support Vector Regression (SVR)** | $\min \|w\|^2$ s.t. $|y_i - w^Tx_i| < \epsilon$ | $\epsilon$-insensitive loss, RMSE | Quadratic programming | Regression, time series |
| **Temporal Convolutional Networks (TCN)** | 1D dilated causal convolutions | RMSE, MAE | SGD, Adam | Sequential data |
| **Prophet** | $y(t) = g(t) + s(t) + h(t) + \epsilon_t$ | RMSE, MAPE | MAP estimation | Business forecasting |
| **Cox Proportional Hazards** | $h(t|X) = h_0(t)\exp(X\beta)$ | Concordance, log-rank | Concordance, log-rank | Partial likelihood |
| **Multilevel (Mixed) Models** | Random + fixed effects structure | REML likelihood, ICC | MLE, Bayesian inference | Grouped data, education, health |
| **Dirichlet Process Mixture Models (DPMM)** | Infinite mixture model prior | Posterior metrics | MCMC, variational Bayes | Flexible clustering |
| Generalized Additive Models (GAMs) | $Y = beta0 + sum_j f_j(X_j) + \epsilon$, with smooth functions $f_j$ | MSE, deviance, AIC, cross-validation | Backfitting algorithm, penalized likelihood | Flexible regression, non-linear effects, interpretable smoothing |
| Regularized Regression |  |  |  |  |
| Generalized Estimating Equations (GEE) | Extension of GLM for correlated/clustered data: $g(mu_ij) = X_ij * \beta$ | Quasi-likelihood, robust standard errors | Iteratively reweighted least squares (IRLS) | Longitudinal data, repeated measures, clustered data |
| Quantile Regression | Minimizes $\sum_i \rho_au(y_i - X_i*\beta)$, with check function $\rho_\tau$ | Check loss, MAE, coverage of quantiles | Linear programming, interior point methods | Modeling medians or other quantiles, robust regression |
| Ordinal Regression |  |  | Likelihood, AIC, accuracy | MLE, gradient-based |
| Copula Models | Joint distribution via copula: $F_{X,Y}(x,y) = C(F_X(x)$, $F_Y(y); \theta)$ | Log-likelihood, AIC, tail dependence measures | MLE, inference functions for margins (IFM) | Modeling dependencies, finance, insurance, risk aggregation |
| Functional Data Analysis | Observations are functions $Y_i(t)$; e.g., $Y_i(t) = \beta 0(t) + \sum_j X_ij * \beta_j(t) + \epsilon_i(t)$ | MSE, integrated squared error, functional cross-validation | Basis expansion (splines, Fourier), penalized least squares | Longitudinal curves, growth curves, EEG/ECG signals, time series as functions |
| **Energy Based Model** | … | … | .. | .. |

### Inference Toolbox

> What inferences can we make from a statistical representation or from raw pieces of reality? What are the tools used to make these inferences?
> 

> See [Problem Space](note.html?n=epistemica/discipline/statistics.md), [Statistical Function](note.html?n=epistemica/observational/statistical-function.md),  [(Statistic) Estimator](note.html?n=epistemica/observational/statistic-estimator.md), …
> 

| **Category** | **Inference** | **Description** |
| --- | --- | --- |
| **Point Estimation** | Estimate Parameters | Infer single-value estimates of population parameters (e.g., mean, variance) from sample data. |
| **Interval Estimation** | Confidence Intervals | Provide a range of plausible values for population parameters, with a given confidence level. |
| **Hypothesis Testing** | Significance Tests | Assess whether observed data provides enough evidence to reject a null hypothesis. |
| **Regression & Association** | Relationships Between Variables | Infer dependencies, correlations, or causal links between variables using regression models or association metrics. |
| **Prediction / Forecasting** | Future Values | Use statistical models to predict unseen outcomes based on current or historical data. |
| **Classification & Clustering** | Grouping & Labeling | Assign observations to categories or identify latent group structures in data. |
| **Bayesian Inference** | Posterior Updating | Update beliefs about parameters or hypotheses based on observed data and prior knowledge. |
| **Anomaly Detection** | Outlier Identification | Detect unusual or rare events that deviate significantly from expected patterns. |
| **Causal Inference** | Cause-Effect Relationships | Identify causal links using experimental design, counterfactuals, or structural models. |
| **Dimensionality Reduction** | Feature Extraction | Infer the underlying structure of data by reducing complexity while preserving important patterns (e.g., PCA). |

### Description

> See more in [(Statistic) Estimator](note.html?n=epistemica/observational/statistic-estimator.md) and [Statistical Function](note.html?n=epistemica/observational/statistical-function.md).
> 

### Principle

> Survivorship Bias
> 

> However, some fundamental principles guide statistical analysis, including:
> 

| **Principle** | **Description** |
| --- | --- |
| **Principle of Randomness** | Emphasizes the importance of randomness in data collection and analysis, highlighting the need for random sampling and randomization to reduce bias in experiments. |
| **Principle of Inference** | It involves drawing conclusions or making predictions about a population based on a sample of data, using underlying techniques like hypothesis testing and confidence intervals. |
| **Principle of Uncertainty** | Acknowledges the inherent uncertainty in statistical analysis, with results often expressed using measures like p-values or confidence intervals. |
| **Principle of Data Distribution** | It assumes that data follow specific probability distributions (e.g., a normal distribution), which can impact the choice of statistical tests and models. |
| **Principle of Reproducibility** | Stresses the need for statistical analysis to be conducted in a way that allows others to independently replicate and verify results. |
| **Principle of Non-Bias** | Focuses on minimizing bias in data collection and analysis, ensuring that findings are objective and unbiased. |

### Pitfall

> **Statistical Analysis**, while a powerful tool, is prone to several common pitfalls that can affect the validity and reliability of results.
> 

| **Pitfall** | **Description** |
| --- | --- |
| **Selection Bias (Survivorship Bias)** | Systematically excluding or including specific groups or data, leading to skewed results. |
| **Confounding Variables** | Failing to account for variables that distort relationships between the variables of interest. |
| **Non-Independence** | You violate the independence assumption, particularly in time series or spatial data. |
| **Misinterpretation of Correlation** | Assuming correlation implies causation when it does not. |
| **Overfitting** | Creating overly complex models that fit noise rather than meaningful patterns. |
| **Multiple Comparisons** | Conducting many tests without adjusting increases the risk of false positives. |
| **P-Hacking** | Manipulating analysis or testing until significant results are achieved. |
| **Publication Bias** | Selectively publishing studies with significant results while neglecting non-significant findings. |
| **Missing Data** | Inappropriately handling missing data leads to biased or inefficient results. |
| **Small Sample Sizes** | Conducting statistical tests with small samples needs more power to detect meaningful effects. |
| **Outliers** | Ignoring or mishandling outliers in data analysis affects the results. |
| **Inappropriate Model Assumptions** | Applying methods that rely on assumptions that do not hold in the data. |
| **Cherry-Picking Data** | Selectively presenting data that supports a particular argument while omitting contradicting evidence. |
| **Misleading Visualizations** | Creating graphs or charts distorts the data or does not accurately convey the results. |
| **Ignoring Effect Size** | I am focusing solely on statistical significance without considering practical or clinical relevance. |
| **Failure to Validate Models** | Not validating models on independent data leads to over-optimistic performance estimates. |
| **Ethical Concerns** | Ignoring ethical implications related to data privacy, consent, or potential biases. |
| **Assuming Normality** | Applying parametric tests without verifying that the data follows a normal distribution. |
| **Post-Hoc Hypotheses** | Formulating hypotheses after data analysis may lead to spurious findings. |
| **Inadequate Reporting** | Failing to disclose methods, data, and results fully hinders replication and assessment. |
| **Misusing p-Values** | Misinterpreting or misusing p-values without considering their limitations and context. |
| **Texas Sharpshooter Fallacy** | Focusing on data clusters that appear significant without accounting for randomness, creating an illusion of meaning. |
| **Confirmation Bias** | Seeking or interpreting data in a way that confirms preconceived beliefs while disregarding conflicting evidence. |
| **Hasty Generalization** | Drawing broad conclusions from a small or unrepresentative sample of data. |
| **Post Hoc Fallacy** | Assuming that because one event followed another, the first caused the second without sufficient evidence. |
| **Correlation Implies Causation** | Mistakenly inferring a causal relationship based solely on correlation. |
| **Regression to the Mean** | Misinterpreting the tendency of extreme data points to move closer to the mean in subsequent measurements. |
| **Ecological Fallacy** | Making inferences about individuals based on group-level data, potentially leading to incorrect conclusions. |
| **Anecdotal Evidence** | Relying on isolated anecdotes or personal experiences to support a broader claim without considering the overall context. |
| **Simpson’s Paradox** | A situation where aggregated data shows one trend, but the opposite trend emerges when data is disaggregated. |
| **Gambler’s Fallacy** | Believing that past outcomes in random events influence future outcomes as if a balance were to be maintained. |
| **Base Rate Fallacy** | Ignoring the prior probability of an event when considering new evidence. |
| **False Cause Fallacy** | Attributing a cause-and-effect relationship between two events without adequate evidence. |
| **Overconfidence Bias** | Overestimating the accuracy and certainty of one’s predictions or judgments. |
| **Causation vs. Correlation** | Correlation does not imply causation; further experimental evidence is needed to prove causation. |
| **Model Selection** | Choosing the appropriate model is challenging; incorrect selection can lead to inaccurate results. |
| **Limited Predictive Power** | Some models may have limited predictive power for highly complex or chaotic systems. |
| **Sensitivity to Outliers** | Extreme values can disproportionately affect results in some methods. |
| **Data Quality** | Results depend on data accuracy and completeness; poor data quality can lead to unreliable results. |

## Model

### Model Evaluation

> **Statistical hypothesis testing** is a method used to determine whether there is enough evidence in a sample of data to infer that a certain condition or effect exists in the population from which the sample was drawn.
> 

> **Statistical hypothesis testing** is a method used to assess whether inferences or models derived from sample data can be generalized to the entire population.
> 

> **Accuracy:** How closely the model’s predictions or outputs match the actual or observed data.
> 

> Data Requirements: The quantity and quality of data needed to build and validate the model.
> 

> Validation: The degree to which the model has been tested against real-world scenarios or independent datasets.
> 

> Robustness: The model can handle variability in data without significant loss of performance.
> 

> Generalizability: The model’s ability to perform well on unseen data, not just the data it was trained on.
> 

> Flexibility: The model’s adaptability to changes in assumptions, parameters, or conditions.
> 

> Consistency: The model's ability to produce stable and repeatable results under similar conditions.
> 

> Interpretability: How easily can the model's results be understood and interpreted by humans?
> 

| **Strategy** | **Description** |
| --- | --- |
| **Cross-Validation** | A technique where the dataset is divided into multiple subsets to validate model performance on different data partitions. |
| **Train-Test Split** | A method where the data is divided into a training set to build the model and a test set to evaluate its performance. |
| **Bootstrap Methods** | Techniques that involve resampling the dataset with replacement to assess the stability and accuracy of the model. |
| **Holdout Validation** | A form of validation where a portion of the dataset is held out and not used during training to test the model's performance. |
| **AIC (Akaike Information Criterion)** | A criterion used to select the best model among a set of models, balancing goodness-of-fit with model complexity. |
| **BIC (Bayesian Information Criterion)** | Similar to AIC, but with a stronger penalty for model complexity, used to prevent overfitting. |
| **ROC Curve (Receiver Operating Characteristic Curve)** | A graphical plot that shows the diagnostic ability of a binary classifier system as its discrimination threshold is varied. |
| **Confusion Matrix** | A table that describes the performance of a classification model by comparing predicted and actual classifications. |
| **Precision and Recall** | Metrics used to evaluate the performance of a classification model, focusing on the accuracy of positive predictions. |
| **F1 Score** | The harmonic mean of precision and recall, providing a single metric that balances both aspects of model performance. |
| **R-squared** | A measure of how well the model explains the variability of the dependent variable, used in regression analysis. |
| **Mean Absolute Error (MAE)** | A metric for regression models that measures the average magnitude of errors in predictions, without considering their direction. |
| **Mean Squared Error (MSE)** | A metric for regression models that measures the average squared difference between predicted and actual values. |
| **Root Mean Squared Error (RMSE)** | The square root of MSE, providing a measure of prediction accuracy in the same units as the response variable. |
| **Residual Analysis** | Examining residuals (the differences between observed and predicted values) to assess the fit and identify patterns not captured by the model. |
| **Lift and Gain Charts** | Tools used to evaluate the performance of classification models by showing the improvement of the model over random guessing. |
| **Calibration Plots** | Graphical representations that compare predicted probabilities to actual outcomes, assessing the model's accuracy in probability estimates. |
| **Model Stability** | Evaluating how the model’s predictions change with different subsets of data or with small variations in input features. |

### Model Validation

> See [Model Validation](note.html?n=epistemica/validation/validation.md) & [Statistical Hypothesis Testing](note.html?n=epistemica/validation/statistical-hypothesis-testing.md).
> 

### **Predictive Power**

> Models should possess predictive power, enabling them to make successful predictions about physical systems beyond the data used to construct them. Accurate predictions strengthen confidence in the model’s validity.
> 

> La palabra "predicación" viene **del latín praedicatio y significa "acción y efecto de anunciar algo públicamente"**.  Sus componentes léxicos son: el prefijo pre- (antes, delante), dicare  (destinar, consagrar), más el sufijo -ción (acción y efecto).
> 

> Predictability is the extent to which future events or behaviors can be forecasted accurately based on current knowledge or patterns.
> 

> A **forecast (**pronóstico**)** is a prediction or estimation of a future event or trend based on current and historical data, analysis, and modeling techniques, often used in contexts like weather, economics, and business planning.
> 

### **Simplicity**

> The complexity of the model in terms of the number of parameters, assumptions, and computational effort required.
> 

> Is the model overly complicated for the task?
> 

## Sampling

> Se more in [Sampling](note.html?n=epistemica/observational/sampling.md) and  [**Resampling**](note.html?n=epistemica/observational/resampling.md).
> 

> In probability and statistics, **sampling** refers to the process of selecting a subset of elements from a larger **population** or **universe** in order to make inferences about the whole population. The main idea is that it is usually impractical or impossible to observe every member of a population, so we observe a sample and use it to estimate population properties.
> 

> This is a key procedure in **estimation** and **data selection**. We usually cannot operate on the entire dataset, because the data is generated according to an underlying probabilistic process (at least we assume this), which may itself change over time in **non-stationary** settings.
> 

> **Sampling** is the process of selecting a subset of individuals or observations from a larger population to make inferences about that population.
> 

> **Resampling** is a statistical technique where repeated samples are drawn from the observed data (the sample itself) rather than the population.
> 

> The key in this process is that a well-chosen sample **retains the essential properties of the population**, allowing any procedure applied to the sample to be meaningfully **generalized to the population**.
> 

## Comparison

> In statistics, a **population** is the entire set of individuals, items, or measurements that we want to study. Populations can be finite or infinite, and can be characterized by parameters such as the **mean (μ)**, **variance (σ²)**, **proportions**, or the **overall distribution**.
> 

> **Population Comparison:**  Comparing populations involves analyzing differences or relationships between two or more populations. This can be done with respect to **means**, **variances**, **distributions**, or **proportions**.
> 

> See more in [Comparison](note.html?n=epistemica/observational/comparison.md).
> 

## Foundation

> Aka. A Meta Theory of Statistics
> 

> What is the theoretical grounding of statistics? When should a **statistical procedure** be used?
> 

> See more in [Theory of Statistics](note.html?n=epistemica/observational/theory-of-statistics.md) and [Theory of Probability](note.html?n=epistemica/observational/theory-of-probability.md).
> 

### Induction

> **The Problem of Induction** refers to the philosophical challenge of justifying the inference of general principles from specific observations. In other words, it questions how we can logically conclude that future events will resemble past events based solely on past experience.
> 

> For example, seeing the sun rise every day in the past does not logically guarantee it will rise tomorrow, yet we expect it to do so. This uncertainty arises because inductive reasoning assumes patterns hold beyond observed cases without absolute proof.
> 

> Philosophers like David Hume famously highlighted this problem, emphasizing that induction lacks a rational foundation, making it a fundamental issue in the philosophy of science and knowledge.
> 

### Probability

> Statistically, we usually deal with stochastic systems (at least from the observer’s point of view). The **framework that models** these **systems is called probability**, which can be interpreted as follows:
> 
1. *physical*, namely the frequency or propensity of the occurrence of a state of affairs, often referred to as the chance, or else as
2. *epistemic*, namely the degree of belief in the occurrence of the state of affairs, the willingness to act on its assumption, a degree of support or confirmation, or similar.

## Limitation

> **Steven Wolfram criticizes traditional statistics** for being overly focused on fitting data to preconceived models rather than exploring and understanding the underlying complexity of the data.
> 

## Relation

| **Area** | **Brief Description** | **Typical Interactions with Statistics** |
| --- | --- | --- |
| **Decision Theory** | Formal study of how to choose optimal actions under uncertainty. | Loss functions, risk, Bayes rules, utility theory, optimal stopping. |
| **Machine Learning** | Algorithms that learn patterns from data for prediction or control. | Cross-validation, regularization, model selection, PAC-Bayes bounds. |
| **Econometrics** | Statistical methods tailored to economic data and theory. | Instrumental variables, panel data models, time-series econometrics. |
| **Biostatistics** | Statistics applied to biology, medicine, and public health. | Survival analysis, clinical-trial design, epidemiological models. |
| **Psychometrics** | Measurement of psychological attributes and educational testing. | Factor analysis, IRT (Item Response Theory), reliability/validity. |
| **Operations Research** | Mathematical models for optimal decision-making in complex systems. | Stochastic optimization, queueing models, simulation, Markov decision processes. |
| **Information Theory** | Quantification of information, entropy, and coding efficiency. | Model comparison via AIC/BIC, minimum description length (MDL), mutual information. |
| **Actuarial Science** | Risk assessment in insurance and finance. | Survival models, credibility theory, extreme-value statistics. |
| **Bayesian Data Analysis** | Treats parameters as random variables; updates beliefs with data. | Prior selection, posterior inference, Bayesian experimental design. |
| **Spatial & Spatio-temporal Statistics** | Models for data indexed in space and time. | Kriging, Gaussian random fields, point processes. |
| **Causal Inference** | Methods to estimate cause–effect relationships from data. | Randomized experiments, instrumental variables, DAGs, potential outcomes framework. |
| **Data Visualization** | Graphical representation of data to support analysis and communication. | Grammar of graphics, interactive dashboards, exploratory data analysis (EDA). |
| **Survey Methodology** | Design and analysis of sample surveys. | Sampling frames, weighting, non-response adjustments, variance estimation. |

## Case Study

> See
> 
- [‣](https://app.notion.com/p/249598edb790800e99d0f999e0f006e7?pvs=21)
- …

| **Case Study** | **Problem** | **Statistical Analysis** | **Description** |
| --- | --- | --- | --- |
| Student Dropout Prediction | Predict which students are likely to drop out of school early. | Survival Analysis | Models the time until dropout occurs, handling censored data and estimating dropout probabilities over time. |
| Customer Churn in Telecom | Identify factors causing customers to leave the service. | Cox Proportional Hazards Model | A regression model for time-to-event data, estimating the effect of covariates on the hazard (risk) of churn. |
| Clinical Trial Drug Effectiveness | Determine if a new drug improves patient recovery rates. | Randomized Controlled Trial (RCT) with ANOVA and t-tests | Compares treatment and control groups to detect statistically significant differences in outcomes. |
| Manufacturing Defect Rate | Analyze causes of defects in a production line. | Control Charts & Regression | Control charts monitor process stability; regression identifies relationships between variables and defect rates. |
| Marketing Campaign Effectiveness | Measure impact of a campaign on sales over time. | Time Series Analysis | Analyzes sales data over time to detect trends, seasonal effects, and impact of interventions like campaigns. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md) (schema owner)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md) (evaluation criteria)
- [Validation](note.html?n=epistemica/validation/validation.md) — the evaluative sibling of statistics
- [Calibration](note.html?n=epistemica/validation/calibration.md) — a distinct practice, not a synonym for validation
- [Statistical Hypothesis Testing](note.html?n=epistemica/validation/statistical-hypothesis-testing.md)
- [p-value](note.html?n=epistemica/validation/p-value.md) · [e-value](note.html?n=epistemica/validation/e-value.md)
- [Exploratory Data Analysis](note.html?n=epistemica/exploratory-data-analysis-eda.md)
- [Mathematics](note.html?n=epistemica/discipline/mathematics.md) — the parent formal discipline
- [REES](note.html?n=epistemica/rees.md) — the inventory this discipline is indexed in
- [Statistics](https://en.wikipedia.org/wiki/Statistics)
- [Statistical model](https://en.wikipedia.org/wiki/Statistical_model)
- http://bactra.org/notebooks/statistics.html
- http://bactra.org/notebooks/computational-statistics.html
- [The Problem of Induction](https://app.notion.com/p/The-Problem-of-Induction-1fdc0f5171ec8031a27ef5c52d2c549e?pvs=21)
- https://en.m.wikipedia.org/wiki/Statistical_theory
- https://en.wikipedia.org/wiki/Robust_statistics
- https://en.wikipedia.org/wiki/Free_probability
- https://en.m.wikipedia.org/wiki/History_of_statistics
- https://en.m.wikipedia.org/wiki/Multivariate_statistics
- https://en.wikipedia.org/wiki/James–Stein_estimator
- [ ]  https://plato.stanford.edu/entries/learning-formal/
- https://en.wikipedia.org/wiki/Statistical_model_specification
- [Ten Statistical Ideas that Changed the World](https://www.youtube.com/playlist?list=PLt_pNkbycxqahVksaNnjz3M6759xHIZ-r)
- https://plato.stanford.edu/entries/statistics/
- http://bactra.org/notebooks/properties-vs-principles-for-statistics.html
- https://norvig.com/chomsky.html
- https://honglangwang.wordpress.com/2014/12/30/machine-learning-books-suggested-by-michael-i-jordan-from-berkeley/
- [ ]  [‣](https://app.notion.com/p/249598edb79080589c6ef26fabdcd9c8?pvs=21)
- [ ]  [‣](https://app.notion.com/p/10e598edb7908119b002f33cd08e6287?pvs=21)
- [‣](https://app.notion.com/p/249598edb790800e99d0f999e0f006e7?pvs=21)
- [ ]  [‣](https://app.notion.com/p/10e598edb7908150baafc6e551b6e578?pvs=21)
- [ ]  https://en.wikipedia.org/wiki/Smoothing_spline
- https://en.wikipedia.org/wiki/P-value
- https://en.wikipedia.org/wiki/Statistical_hypothesis_test
- [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
- [Statistical model validation](https://en.wikipedia.org/wiki/Statistical_model_validation)
- [Properties versus Principles in Defining "Good Statistics"](http://bactra.org/notebooks/properties-vs-principles-for-statistics.html)
- The World is Unpredictable
[https://www.edge.org/response-detail/10171](https://www.edge.org/response-detail/10171)
- Computational Irreducibility
[https://en.wikipedia.org/wiki/Computational_irreducibility](https://en.wikipedia.org/wiki/Computational_irreducibility)
- Bialek, William, Ilya Nemenman, and Naftali Tishby. "Predictability, complexity, and learning." Neural computation 13.11 (2001): 2409-2463.
- Lorenz, Edward N. "Predictability: A problem partly solved." Proc. Seminar on predictability. Vol. 1. No. 1. 1996.
- Menzly, Lior, Tano Santos, and Pietro Veronesi. "Understanding predictability." Journal of Political Economy 112.1 (2004): 1-47.
- Boffetta, Guido, et al. "Predictability: a way to characterize complexity." Physics reports 356.6 (2002): 367-474.
- Schneider, Tapio, and Stephen M. Griffies. "A conceptual framework for predictability studies." Journal of climate 12.10 (1999): 3133-3155.
- Lau, William KM, Duane E. Waliser, and Duane Waliser. Predictability and forecasting. Springer Berlin Heidelberg, 2005.
- Lorenz, Edward N. "Predictability: A problem partly solved." Proc. Seminar on predictability. Vol. 1. No. 1. 1996.
- Webster, Peter J., et al. "Monsoons: Processes, predictability, and the prospects for prediction." Journal of Geophysical Research: Oceans 103.C7 (1998): 14451-14510.
- DelSole, Timothy, and Michael K. Tippett. "Predictability: Recent insights from information theory." Reviews of Geophysics 45.4 (2007).
- Bandi, Federico M., et al. "The scale of predictability." Journal of Econometrics 208.1 (2019): 120-140.
- Ang, Andrew, and Geert Bekaert. "Stock return predictability: Is it there?." The Review of Financial Studies 20.3 (2007): 651-707.
- Ehrenberg, Andrew SC, and John A. Bound. "Predictability and prediction." Journal of the Royal Statistical Society Series A: Statistics in Society 156.2 (1993): 167-194.
- Farmer, Leland E., Lawrence Schmidt, and Allan Timmermann. "Pockets of predictability." The Journal of Finance 78.3 (2023): 1279-1341.
- Bacchetta, Philippe, Elmar Mertens, and Eric Van Wincoop. "Predictability in financial markets: What do survey expectations tell us?." Journal of International Money and Finance 28.3 (2009): 406-426.
- Niklaus Wirth, or the Importance of Being Simple ([acm.org](http://acm.org/))
[https://news.ycombinator.com/item?id=39004526](https://news.ycombinator.com/item?id=39004526)
- Forster, Malcolm R., et al. "The new science of simplicity." *Simplicity, inference and modelling: keeping it sophisticatedly simple* (2001): 83-119.
- Baker, Alan. "Simplicity." (2004).
- A. Zellner, H. A. Keuzenkamp, and M. McAleer (eds.) (2001): Simplicity, Inference
and Modelling, Cambridge University Press, pp. 83-119.
- [‣](https://app.notion.com/p/25e598edb790808bb988d1e56089405a?pvs=21)
- [‣](https://app.notion.com/p/25e598edb790803890a2e56a34456f39?pvs=21)
- [Seasonal Autoregressive Integrated Moving Average](https://machinelearningmastery.com/sarima-for-time-series-forecasting-in-python)
- [Time Series](https://www.wikiwand.com/en/Time_series)
- [Time Series with Konrad](https://www.youtube.com/playlist?list=PL98nY_tJQXZmT9ZB59T0lsx0ZzzLrYdX4)
- [Time Series Analysis](https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/)
- [Practical Time Series Analysis](https://www.coursera.org/learn/practical-time-series-analysis)
- [Time Series Forecasting](https://www.udacity.com/course/time-series-forecasting--ud980)
- Facebook Prophet
- MAPE forecasting metric
- [Dynamical System](note.html?n=epistemica/mathematical/ds/dynamical-system.md)
- https://en.wikipedia.org/wiki/Gompertz_function
- [‣](https://app.notion.com/p/273598edb790800ebe9efdc968b59009?pvs=21)
- https://archive.org/details/practicaldataana0000brya
- https://www.youtube.com/watch?v=QKplGhhF1E4
- https://en.wikipedia.org/wiki/Dummy_variable_(statistics)
