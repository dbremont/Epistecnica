---
tags: [note, epistemology]
---

# Variable

Related: [Modelling](/view.html?p=notes/epistemica/meta/theory/modelling.md), [Variable–Reality Aspect Type (VRAT)](/view.html?p=notes/epistemica/meta/theory/variable-reality-aspect-type-vrat.md), [State Descriptor](/view.html?p=notes/epistemica/meta/theory/state-descriptor.md)

> A variable is an abstraction mechanism, technique  that formalized the platonic notion of **`Variable–Reality Aspect Type`**   - a identifiable dimension (aspect) in which a  piece of realty can vary.
> 

> A **`Variable–Reality Aspect Type (VRAT)`** is a *class of admissible variation modes* that can be consistently abstracted from a system.
> 

> **Note:** The notions of *dimension* (or *aspect*) are treated as primitives and left undefined. Their intended meaning is conveyed through canonical examples of aspects of reality, such as temperature, velocity, and position.
> 

Guiding questions:

- What is the nature of a variable (ontic, epistemic, mixed)?
- How to characterize a variable? What is the affirmation space about a variable?

## Formulation

> What is the nature of a variable (ontic, epistemic, mixed)?
> 

> A variable is an epistemic abstraction that formalizes a **Variable–Reality Aspect Type**—a stabilized and identifiable dimension of variation in a system—by embedding it into a structured formal object with a domain, interpretation, and admissible transformations.
> 

### What is the nature of a variable (ontic, epistemic, mixed)?

> A variable is an **epistemic operator that encodes a stabilized dimension of variation of a system into a formal object with a domain, interpretation, and admissible transformations**.
> 

> A variable does not exist as such in the ontic substrate; reality does not contain variables, symbols, or domains. Instead, reality exhibits **structured variation**—differences, regularities, and invariances.
> 

A variable arises when a modeler:

1. **Selects** a dimension of variation in a system
2. **Stabilizes** it as an identifiable aspect
3. **Formalizes** it within a symbolic and mathematical framework

In this sense:

- **Epistemic** → A variable is a representational and formal device used for modeling, reasoning, and computation
- **Ontic anchoring** → Its validity and usefulness depend on real, reproducible structures in the underlying system

### How a variables comes to being?

> Variables are not *given* — they are **constructed under constraints**.
> 

This construction involves:

- **Selection** (what varies)
- **Stabilization** (making it identifiable across contexts)
- **Formalization** (embedding into mathematics or symbolic systems)

## Characterization

> Note: The characterization can be extracted from the affirmation space, but for simplicity and used let’s specify the main aspects here.
> 

> A variable $X$ can be characterized as: $X := ( \mathcal{D}, \mathcal{I}, \mathcal{M}, \mathcal{C} )$.
> 

| **Component** | **Meaning** |
| --- | --- |
| **$\mathcal{D}$ (Domain)** | Set of admissible values |
| **$\mathcal{I}$ (Interpretation)** | What aspect of reality it refers to |
| **$\mathcal{M}$ (Measurement map)** | How values are obtained |
| **$\mathcal{C}$ (Constraints)** | Laws, invariants, admissibility conditions |

## Affirmation Space

> The **affirmation space** of a variable is the set of all *well-formed, truth-evaluable statements* that can be made about it.
> 

> Note: Variables will captures the properties of **`Variable–Reality Aspect Type (VRAT)`**  like  ****{Intensive,  Extensive, etc.} - for this see
> 

| **Category** | **Affirmation (Form)** | **Description** |
| --- | --- | --- |
| **Structural** | $X \in \mathcal{D}$, $X$ is continuous/discrete/bounded | Asserts intrinsic properties of the variable’s domain and mathematical structure |
| **State-Level** | $X = x$, $X \in A \subseteq \mathcal{D}$ | Assigns or constrains the value of the variable |
| **Relational** | $X > Y$, $X = f(Y)$ | Defines relationships between variables |
| **Dynamical** | $\frac{dX}{dt} = f(X,t)), (X_{t+1} = g(X_t))$ | Specifies how the variable evolves across an index (e.g., time) |
| **Statistical** | $X \sim P$, $\mathbb{E}[X] = \mu$, $\mathrm{Var}(X) = \sigma^2$ | Describes uncertainty, variability, or probabilistic structure |
| **Constraint-Based** | $g(X) = 0$, $h(X) \leq 0$ | Imposes admissibility conditions or invariants |
| **Measurement** | $x = M(s)$, $X = x \pm \epsilon$ | Relates the variable to an operational measurement process and error |
| **Epistemic** | $X$ is observable/latent/estimated | Characterizes the epistemic status of the variable within the model |
| **Interpretation** | X ≡ “temperature”, $X$ represents thermal intensity | Links the variable to a specific aspect of reality (semantic grounding) |
| **Measurment** | $M: S \rightarrow \mathcal{D}$, protocol $P_M$ defines measurement procedure | Specifies the concrete procedure, instrumentation, and conditions under which values are obtained |

## Taxonomy

> 

| **Type of Variable** | **Description** |
| --- | --- |
| **Independent Variable (IV)** | This variable is manipulated or controlled in an experiment or study to determine its effect on the dependent variable. It is often denoted as “X” in equations. |
| **Dependent Variable (DV)** | This variable is measured or observed to assess the effect of changes in the independent variable. It is often denoted as “Y” in equations. |
| **Categorical Variables** | Variables representing categories or groups, typically with labels or names, such as gender (male, female) or color (red, blue, green). |
| **Numerical Variables** | Variables that represent numerical values, which can be further categorized into: |
| **Continuous Variables** | These can take any value within a range and are often measured with precision, such as height or weight. |
| **Discrete Variables** | These can only take specific, distinct values and are often counted, such as the number of students in a classroom. |
| **Ordinal Variables** | Categorical variables with a specific order or ranking, where the exact numerical difference between categories may not be meaningful, like educational levels. |

## Variable Interaction

> Two variables can be related in several **forms**, and the choice of form is a modelling claim about the two aspects of reality, not a notation. Additive says the aspects contribute independently; multiplicative says they are jointly constitutive; an interaction says the effect of one depends on the level of the other. The same data can be described under any of them — and the descriptions make different claims about the world.

| Relationship | Form | Meaning |
| --- | --- | --- |
| **Additive** | $X+Z$ | Independent contributions |
| **Multiplicative** | $XZ$ | Joint/product effect |
| **Interaction in regression** | $\beta_3 XZ$ | Effect of $X$ depends on $Z$ |
| **Exponential** | $e^{\beta X}$ | Percentage/proportional effect |
| **Cobb–Douglas** | $A X^\alpha Z^\beta$ | Inputs combine multiplicatively |

> Read the table as a ladder of stronger commitments. The additive form asserts **separability**: the effect of $X$ is the same at every level of $Z$, so the two aspects can be studied one at a time. The multiplicative form asserts **jointness**: the effect of $X$ scales with $Z$, and neither term is interpretable alone. The interaction term $\beta_3 XZ$ is the regression form that **tests** the claim rather than assuming it, which is why it belongs to the estimation vocabulary and not to the algebra of the model.

> Two rows are the same relation in different coordinates. $e^{\beta X}$ is the multiplicative form written on the log scale, which is why a coefficient in a log-linear model reads as a **percentage** effect rather than a unit effect. And $A X^\alpha Z^\beta$ is the canonical Cobb–Douglas case, where the exponents are output elasticities and $\alpha+\beta$ tests the returns to scale — a multiplicative relation whose parameters carry the economic interpretation. See [Production Function](/view.html?p=notes/epistemica/singular/production-function.md) and [Regression](/view.html?p=notes/epistemica/observational/computational/regression.md) for the estimation side.

> **The caution the fourth row invites.** With an interaction term present, the coefficient on $X$ is no longer the effect of $X$ in general; it is the effect of $X$ at $Z = 0$, which may be a point outside the data. The general effect is a function of $Z$, and centred predictors are the usual remedy because they move the reference point to the mean. A model with an uncentred interaction whose "main effect" is read as an average effect is the most common misreading in applied work.

## References

- https://en.wikipedia.org/wiki/Variable_(mathematics)
