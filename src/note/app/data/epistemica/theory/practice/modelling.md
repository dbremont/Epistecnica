---
tags: [epistemology, representation, modelling, identifiability]
qa:
  - What is the modelling instance — the map $f_\theta: X \to Y$, the model artifact, the practice, or the identification problem that binds them?
  - Why is $Y$ a datum in inverse problems and the unknown in forward problems, and what stays invariant across the problem types?
  - What epistemic element type does modelling belong to, and why is `Aggregate` primary over `Epistemic Operation`, `Epistemic Construction`, and `Epistemic Evaluation`?
  - What is the relation between a connector $C$ and the schema $X \to Y$ — realization, morphism, pullback, or physical measurement channel?
  - When are several $X$ contexts or several models observationally equivalent, and what does the fibre $B^{-1}(y)$ leave unidentified?
  - What separates structural from practical identifiability, and which one can a finite, noisy dataset ever establish?
  - Is Hadamard well-posedness — existence, uniqueness, stability — the same as identifiability, or a precondition for it?
  - What does equifinality share with observational equivalence, and where do the two come apart?
  - What does a gauge orbit hide, and when is gauge-fixing a discovery rather than a convention?
  - When is a model right for the wrong reasons, and which tests — intervention, out-of-distribution prediction, structural stability — can expose it?
  - Can predictive success justify structural claims, or does it only admit a model into the fibre?
  - Where does the functional-map framing stop working — stochastic kernels, causal graphs, partial observability, or open systems?
  - What does the *Modelado* master contribute — the modelling pipeline, well-posedness, the domain index — that the identification diagram alone does not?
  - Which parts of the note are read as inquiry and which as parsed reality?
  - What would count as evidence against the identification framing itself?
---

# Modelling

Related: [Model](note.html?n=epistemica/theory/practice/model.md), [Epistemic Artifact](note.html?n=epistemica/theory/practice/epistemic-artifact.md), [Representation](note.html?n=epistemica/theory/practice/general/representation.md), [Affirmation Space](note.html?n=epistemica/theory/practice/affirmation-space.md), [Variable](note.html?n=epistemica/theory/practice/variable.md), [State](note.html?n=epistemica/theory/practice/state.md), [Activity](note.html?n=epistemica/theory/practice/activity.md), [Reality](note.html?n=epistemica/theory/ontology/reality.md), [Quasi-Open Interaction Field](note.html?n=epistemica/theory/ontology/quasi-open-interaction-field.md)

> Let’s model modelling, a note on the theory modelling (that is the praxis of epistemology).
> 

> Note: This is a highly - abstraction framework - not  a guide -in research practice - there is feedback loop, and strategy (what, how, when?) are streamly relevant - for any practice project advances.
> 

> **Note:** A model of reality is, fundamentally, an **affirmation about reality** — often a **composite affirmation** built from more basic, fundamental affirmations. However, this is not always strictly the case: in **effective models**, some components of the model may **not correspond directly to affirmations about reality**, but serve as computational or conceptual tools. Still, in general, the **model as a whole represents an affirmation about reality**.
> 

> Note: The nature of models will be determine by the - **segment of reality type**. A great weakness of this note - is that is not - segment of reality type  aware.
> 

> Modelling is the practice of issuing a map $f_\theta : X \to Y$ as an answer to a question, under an explicit specification of what is known and what is unknown; identification is the recovery of that map, its inputs, or its parameters from what the map produces.

> A model is not the target. It is a representation whose adequacy is judged by what the observation can and cannot distinguish — a model can reproduce every observation and still be the wrong model.

> **Modelling:**  [Piece of Reality  → Data (Observations)] → Formal Representations (Data, Process, etc.) → Testing Explanatory or Predictive Power.
> 

> What we observe is not nature itself, but nature exposed to our method of questioning. - Werner Heisenberg, German physicist
> 

> **Scientific insight** is the profound understanding or discovery that reveals underlying principles or patterns in natural phenomena, often leading to significant advancements in **knowledge** or **technology**.
> 

> An [**organizing principle**](https://en.wikipedia.org/wiki/Organizing_principle) is a core assumption from which everything else by proximity can derive a classification or a value. It is like a central reference point that allows all other objects to be located, often used in a [conceptual framework](https://en.wikipedia.org/wiki/Conceptual_framework).
> 

> **Universal Abstraction for Modelling:** The goal of modelling, in this formulation, is to construct an **intelligent actor** — an entity with an explicit internal architecture capable of receiving inputs, maintaining state, and adapting through training to achieve specified behavioral outcomes.
> 

> 

## Formulation

### What is this epistemic instance?

> The instance is also the *Modelado* master note — the modelling domain of the epistemic corpus.

> How to decomposed scientific modelling? What do we mean by a decomposition? How to evaluate such decomposition?
> 

> Note: This  does not imply ordering.
> 

> One can also think of the following as  Reality → Representation, Query, Evaluation triad.
> 

> Note: The **Observer**—or *epistemic operator*—requires differentiated treatment in more articulated scientific frameworks (i.e., models of modelling). Its role, structure, and effects (e.g., how it interacts with or perturbs reality) must be explicitly specified rather than implicitly assumed.
> 

> A simple formulation will be  $\mathcal{R}
\xrightarrow{\Phi_{\mathcal{O}}}
\Sigma
\xrightarrow{\mathcal{H}}
\text{Structured Representation}
\xrightarrow{\mathcal{Q}, \mathcal{E}}
\text{Epistemic Judgement}$.
> 

![Ontic state should be understood as a snapshot.](../assets/note/philosophia-naturalis/modelling/ontic-representation-observed-state.png)

Ontic state should be understood as a snapshot.

We define **scientific modelling** as a structured system: $\mathcal{M} = \langle \mathcal{R}, \mathcal{O}, \Phi, \Sigma, \mathcal{Q}, \mathcal{E}, \models \rangle$

Where:

- **$\mathcal{R}$ — Ontic Reality**: The part of the world being studied; the actual system or phenomenon.
- **$\mathcal{O}$ — Epistemic Observer**: The agent or system that observes, measures, and constructs the model.
- **$\Phi$ — Observation (Measurement Operator)**: The process that converts reality into recorded data (snapshots or states). Note. In practice we also attach the context that affect the system time, environment, etc.
- **$\Sigma$ — State Space (Representation)**: The set of all possible recorded states; the formal space where data lives, relation between elements of states,  state transition etc.
- **$\mathcal{Q}$ — Query Space**: The set of questions we ask about the system (e.g., predict, explain, control).
- **$\mathcal{E}$ — Evaluation Functional**: The criteria used to judge how good the model is (e.g., accuracy, fit, usefulness).
- **$\models$ — Satisfaction Relation**
A rule that determines whether the model adequately explains or fits the observed data.

> The **modelling instance** is the organized practice of constructing, evaluating, and inverting a representation of a target. Its minimal form is a map
>
> $$f_\theta : X \to Y,$$
>
> where $X$ is the input, state, predictor, or context space; $Y$ is the observable, output, or response space; $\theta$ collects parameters; and $f$ is the functional form. A **model instance** — a *connector* $C = (X, f_\theta)$ — binds a context to a map and produces an observation $y = f_\theta(x)$.
>
> The roles are not fixed kinds. $X$ may be a system state in one problem and a controllable input in another; $Y$ may be a measured response or a computed output. What fixes the roles is the **problem specification**, i.e. which of $f$, $\theta$, $x$, and $y$ are given and which are sought:

| Problem type | Known | Unknown | Objective |
| --- | --- | --- | --- |
| **Forward problem** | $f, \theta, x$ | $y$ | Compute the output. |
| **Inverse problem** | $f, \theta, y$ | $x$ | Infer the input from the output. |
| **Parameter estimation** | $f, x, y$ | $\theta$ | Estimate the model parameters. |
| **System identification** | input–output observations | $f$, model structure, or $\theta$ | Identify a model of the system. |
| **Inverse modelling** | observations $y$ and assumptions | model structure, parameters, inputs, or their combination | Construct a model consistent with the observations. |
| **Predictive modelling** | training data | a predictive function | Learn to predict outputs for new inputs. |
| **Inverse design** | model and desired output | input or design configuration | Find a configuration that produces the desired output. |

> $Y$ is a datum only in the inverse, estimation, identification, and design problems. In the forward problem it is the unknown to be computed. The invariant is not "the output is always known"; it is **the observation is always the constraint**, whichever role the problem assigns to $Y$.

> The practice is organized by one diagram. Let $\mathcal{H}$ be the hypothesis space (inputs, maps, parameters, structures) and $\mathcal{Y}$ the observation space. The **behaviour map**
>
> $$B : \mathcal{H} \to \mathcal{Y}, \qquad B(C) = y$$
>
> sends a model instance to what it predicts or produces. Then:
>
> - the **fibre** $B^{-1}(y) = \{C \in \mathcal{H} : B(C) = y\}$ is the set of models consistent with the datum;
> - the **kernel** $C_1 \sim C_2 \iff B(C_1) = B(C_2)$ is the relation of observational indistinguishability;
> - the **quotient** $\mathcal{H}/\!\sim$ is what the observations actually identify.
>
> A model is **structurally identifiable** when its fibre is a single gauge orbit in the ideal, noise-free case; it is **practically identifiable** when the fibre is small enough under the available data and noise. Identifiability is therefore not a property of $f$ alone: it is a property of the triple (map, admissible hypothesis class, observation regime).

### What epistemic element type does this epistemic instance belong to?

> Primary type: `Aggregate` — the **Modelling Practice Set**: the organized inquiry that binds an orientation (the question and its purpose), a target (segment, observable, target element), an access regime (interface, record), a representation (the map and its elements), operations (evaluation, inference, estimation), evaluations (identifiability, equivalence, validation, error), a context (noise and conditions), and an infrastructure (tools, repositories) into one coherent epistemic whole. The root type is declared once, and the branches are read as elements of inquiry.

> `readable as` an `Epistemic Operation` when attention falls on the practice (evaluating, inverting, estimating, identifying); `readable as` an `Epistemic Construction` when attention falls on the model as an artifact; and `readable as` an `Epistemic Evaluation` when attention falls on identifiability, equivalence, and validation. `Aggregate` is primary because the practice is not exhausted by any one of these readings: the map without the operation is inert, and the operation without the evaluation cannot say what was identified.

> The target segment itself is read in the **Ontic Order** — it is a piece of observer-independent reality. The modelling practice that describes it is epistemic; the note must not confuse the two orders.

### Is the type of this `epistemic element instance` ambiguous?

> Yes, at the level of the map alone. The same $f : X \to Y$ can be read as a **representation** (the map as an encoding), a **construction** (the model as an artifact), an **operation** (inference from data), or an **evaluation** (the judgment of identifiability). The ambiguity is not a defect to be removed by picking one reading; it is resolved by declaring `Aggregate` primary and keeping the other readings as branches or as `readable as` prose. Collapsing them into one type would lose either the artifact, the practice, or the criterion.

> `C` carries a second ambiguity: it can name a model instance $(X, f_\theta)$, a connector between two maps, or a physical measurement channel. The decomposition distinguishes them — the model instance sits under `Epistemic Representation`, the connector is a morphism between representations, and the channel sits under `Epistemic Infrastructure`. A note that uses "connector" without saying which of the three it means is under-specified.

> The roles of $X$ and $Y$ are a third ambiguity, and the sharpest one: calling both "variables" hides that one may be an ontic state and the other an observation record. The problem specification fixes the roles; the decomposition types them separately.

### What is the recursive instance decomposition of this epistemic instance?

> The practice is decomposed as an aggregate because its constituents belong to different epistemic types and only an aggregate can hold them together. The tree at the end of this answer is the structural answer; the representational anatomy and the relation tables in between are the conceptual content that the evaluation branches judge.

#### Piece of Realty

> A very **abstract notion** of the set of elements of reality to study, system, ecosystem, field, etc.
> 

##### Recording

> What is a snapshot of reality?
> 

> How do we record a snapshot of reality in order to study its dynamics?
> 

> The  snapshot of reality is the **freezing of a system at a specific point in time**, enabling the construction and **definition** of a **state representation as an approximation to the** snapshot. Since the freezing can’t be done - this represent an ideal.
> 

> The nature of these recordings constrains the form of the resulting model (e.g., superficial vs. structural). Such representations typically do not recover the underlying generative dynamics (whether deterministic or stochastic). Instead, they specify statistical relationships among components of the observed state, without identifying the mechanisms that produce them.
> 

> **Note:** Observational recording is foundational, as it constitutes the empirical substrate from which the representation is constructed. Our decision - of selecting the form of relations between variables it’s the key part - in which the value of the representation is deposited, it has a role in the epistemic used, and also in our posterior validations against reality.
> 

##### Variable Reality Aspect Type

> How to we select the aspects that we pay attention?
> 

> How do we track the threads—types of changes—in a piece of reality?
> 

> This abstraction serves as a bridge to notions such as *variables* and *observables*. It attempts to define the **Platonic ideal of a “type of aspect of reality”**—that is, a principled way of carving reality into analyzable dimensions along which states can vary and changes can be tracked.
> 

##### Variable Reality Aspect Type Abstraction

> It is an abstraction of a **“Variable–Reality Aspect Type”**—that is, a formally defined dimension along which a system can vary.
> 

> It captures a class of distinguishable aspects of reality that can be **identified, measured, and tracked across snapshots**, enabling their incorporation into a state representation.
> 

> In this sense, *properties*, *variables*, *features*, and *observables* are different epistemic roles or instantiations of this underlying abstraction, depending on the modeling context and formalism.
> 

> Which are the **abstractions that** approximate the **‘Variable Reality Aspect Type’**?
> 

| **Abstraction** | **Description** |
| --- | --- |
| **Property** | A qualitative or quantitative attribute that can be ascribed to a system or entity; it defines what can, in principle, be true of the system. |
| **Variable** | A symbolic placeholder that ranges over the possible values of a property, enabling its formal representation and manipulation. |
| **Feature** | A constructed or selected representation derived from one or more variables, tailored for a specific task or modeling objective. |
| **Observable** | A measurable instantiation of a property, defined through a measurement procedure that connects the model to empirical reality. |
| **Signal** | A time- or space-indexed sequence of observable values, representing the dynamic realization of a property as it evolves or is recorded. |

##### State

> What is an state?
> 

> What can be the nature of the state?
> 

> A state is a formalism that represents and captures a snapshot of a piece of reality.
> 

> In practice, we construct models of the ontic substrate **through the mediation of a chosen formalism for  a snapshot (observation at a particular point in time)**, the so called **state (the encoding at a particular point in time of the ontic substrate)**.
> 

> See more in [State](note.html?n=epistemica/theory/practice/state.md).
> 

#### Representation: State Evolution, State-Context Relation,  Intra-State Relation

> See more in [Context-State Relation](note.html?n=epistemica/theory/practice/context-state-relation.md).
> 

> How can we **encode the changes** and relationships within a **piece of reality**?
> 

> How is reality encoded?
> 

> What kinds of descriptions - and representations of the {State Set} can we build?
> 

> How to think  about this descriptions?
> 

> A representation is not just a description of states, but a **formalization of relations over the state space**—within states, across states, and between states and context.
> 

| Representation Type | Description |
| --- | --- |
| **State Representation** | A mapping of a snapshot of reality into a structured state $s \in \Sigma$, composed of variables. |
| **State Evolution** | A rule or mapping that describes how states change over time: $s_t \rightarrow s_{t+1}$. |
| **State–Context Relation** | A mapping that relates states to external variables or conditions (e.g., time, environment, parameters). |
| **Intra-State Relation** | Structural relationships between variables within a single state (e.g., constraints, dependencies, correlations). |
| **State Distribution** | A probabilistic description over the state space, capturing uncertainty or variability. |
| **Trajectory Representation** | A sequence or path of states over time: ${s_t}_{t \in T}$. |
| **Generative Representation** | A mechanism that produces states or trajectories (e.g., simulations, stochastic processes). |
| **Constraint Representation** | A set of rules that restrict admissible states or transitions. |

##### How to think  about this descriptions?

- **Abstraction - Compression** → loss of information is inevitable
- **Granularity** → resolution of description (discrete vs continuous)
- **Coordinate Dependence** → choice of parameterization
- **Equivalence Classes** → multiple representations of the same reality

#### Affirmation Space

> What can be said about the represented system?
> 

> What statements are **expressible**, **distinguishable**, and **meaningful** under (R)?
> 

The affirmation space can be conceived as:

$\Phi(R) = \text{Closure}(\mathcal{L}(R))$

- $\mathcal{L}(R)$: language induced by the representation
- Closure: all well-formed statements under logical/mathematical operations

##### What are the classes of statements that can be made?

In a very compact way:

- **What exists** → State Space, Structure
- **What happens** → Dynamical, Stochastic
- **What is observed** → Statistical, Phenomenological
- **What causes what** → Causal
- **How good the model is** → Meta-level

| **Statement** | Description | Instance(s) |
| --- | --- | --- |
| **Structural** | Asserts properties of the state space or representation independent of time or data. | Linearity, Continuity, Topology, Geometry, etc. |
| **Dynamical** | Specifies rules governing how states change across an index (e.g., time). | Evolution laws, transition Rules, etc. |
| **Statistical** | Describes variability, uncertainty, and relationships using probabilistic structure. | Distributions, Correlations,Variation, etc. |
| **Causal** | Encodes intervention-based relationships and counterfactual dependencies. | interventions, counterfactuals, etc. |
| **Event Stream Regularity** | States empirical regularities observed in data without specifying underlying mechanisms. |  |
| **State Space** | Defines the set of all possible states the system can occupy. |  |
| **State Structure** | Specifies relations and constraints within a single state. |  |
| **State at time ( t )** | Describes a specific snapshot of the system at index ( t ). |  |
| **Stochastic** | Specifies randomness in state evolution or observation via probabilistic mechanisms. |  |
| **Meta** | Evaluates properties of the model itself rather than the system directly. | identifiable, stable, computable |

#### Affirmation Evaluation

> aka. Query Evaluation.
> 

The query evaluation can be conceived as:
$\models_{\mathcal{E}} ; \subseteq ; \mathcal{S} \times \Phi$

This defines when a statement is:

- satisfied
- supported
- useful
- actionable

Evaluation is parameterized by a regime:

- **Empirical** → agreement with data
- **Predictive** → out-of-sample performance
- **Explanatory** → structural coherence
- **Causal** → validity under intervention
- **Computational** → tractability
- **Robustness** → stability under perturbations

#### Guiding Principle Set

##### **Principle of Representational of Anti-Reification**

> aka **Principle of Representational Conservatism**
> 

> aka. **Anti-Reification Mandate**
> 

> See more in https://www.youtube.com/watch?v=XcY3ZtgYis0, Aforismo.
> 

> Note: Linguistic representations suffer from low precision, high ambiguity, and reductive labeling, making them prone to misuse in reasoning. Unlike formal systems (e.g., mathematics), language relies on metaphors, contextual vagueness, and discrete categories that often misalign with reality.
> 

> Never treat a formal model as the ground of reality. Always verify when extrapolating from formalism to the physical or social world.
> 

> Formal representations are instruments for understanding aspects of reality; they must not be mistaken for reality itself. Extrapolations from formal models must be critically evaluated before being applied to the real world.
> 

> *Formal representations (models, theories, symbols) must not be  conflated with reality itself. While such representations can  approximate or describe aspects of reality, they are not ontologically  equivalent to it. Extrapolating the consequences of a formal system onto  reality without empirical validation constitutes an epistemic  error—imposing abstraction onto the concrete.*
> 

> **Hypostatization Fallacy:** Treating abstractions (e.g., "the market," "IQ," "neural representations") as concrete entities.
> 

**Corollaries:**

1. **Anti-Overreach**: Formal systems are tools, not truths. Their validity is constrained by their assumptions and domain of applicability.
2. **Empirical Anchoring**: The consequences of a formal representation must be tested against reality, not assumed to mirror it.
3. **Abstraction Awareness**: Recognize when a representation is being treated as reality itself (a form of *reification* or *hypostatization*).
4. Formalisms are tools, not universal ontologies. Their misuse arises when their domain of applicability is ignored.

Aphorisms:

- A model is a map, not the territory. Confusing them is a cardinal error.
- Formalism describes; it does not decree reality.
- A representation is a lens, not a law.
- Mistaking the model for the world is the beginning of delusion.
- Formalisms serve reality; reality does not serve formalisms.
- The model is an instrument, not an oracle.
- Extrapolation is not revelation.
- A formalism is a scaffold for thought, not a substitute for the world.
- To impose the consequences of a model onto reality is to abandon truth for convenience.

##### ⚠️  The Social Systems Modeling Paradox: Visibility vs. Intelligibility

> Also known as: "Emergence Beyond the Obvious"
> 
> 
> When the visibility of social systems is mistaken for their intelligibility or transparency.
> 

> **Visibility** is not intelligibility. The transparency of surface interactions conceals the opacity of system-level behavior.
> 

> Although **social systems** are directly observable—unlike molecular or quantum systems—their visibility often creates an illusion of understanding. We see people interacting, institutions functioning, and decisions being made, and assume that we comprehend the system. But this is a profound epistemic trap.
> 

> At this **level of organization**, social systems are among the most complex entities in nature. They are shaped by adaptive agents, strategic behavior, recursive feedback loops, and emergent properties that are irreducible to individual components. The visible patterns are often deceptive—what appears to be simple or self-evident may mask deep structural dynamics.
> 

#### Modeling Tools

> A **modeling template**, also known as a model template, is a pre-defined structure or framework that provides a standardized format for creating models in a specific domain or context. It serves as a starting point or guide for developing models by providing a consistent structure, variables, relationships, and assumptions that are commonly used within that domain.
> 

> **Mathematics** is the art of clear thinking.
> 

> **Computer Science** is the art of modelling processes.
> 

> **Statistics** is the art of describing phenomena without delving into their underlying mechanisms.
> 

![Untitled](../assets/note/epistemica/modelado/untitled.png)

#### Systems

> The goal is to create a **universal framework** for **modeling systems**, including **listing natural systems**, developing classifications, and creating tools to facilitate their modeling.
> 

#### Model Theory

> Try to develop a theory of modelling.
> 

#### Problem

> Let’s say we have a specification of a problem: does it have a solution? If so, is it unique, are there many solutions, or none at all? - For this used the terminology of **Well-Posed Problem**.
> 

> **Determinacy** refers to the property of a system where its **future state is uniquely determined by its initial state and the governing rules/laws**.
> 

> **Characterization of Solutions:** This is a broader goal that includes determining existence, uniqueness, *and* describing the *set* of all solutions (e.g., parameterizing the solution space if there are infinitely many).
> 

> **Well-Posed Problem (Hadamard)**: A problem is well-posed if it satisfies three conditions: (1) a **solution exists (Existence)**, (2) the **solution is unique (Uniqueness),** and (3) the solution's behavior changes continuously with the initial data (**stabilit**y). Existence and uniqueness are the first two pillars of **well-posedness**.
> 

#### Modelling Domains

[Causality](note.html?n=epistemica/causality.md)
[Simulation](note.html?n=epistemica/simulation.md)
[Optimization](note.html?n=epistemica/optimization.md)
[Mathematical](index.html?dir=epistemica/mathematical)
[Observational](note.html?n=epistemica/observational.md)
[Decision Making](note.html?n=epistemica/observational/decision/decision-making.md)
[Signal Processing](note.html?n=epistemica/signal-processing.md)
[Natural Computing](note.html?n=epistemica/natural-computing.md)
[Complexity Science](note.html?n=epistemica/complexity-science.md)
[**Statistical Mechanics**](note.html?n=epistemica/construction/statistical-mechanics.md)
[Dynamical Intelligence](note.html?n=epistemica/dynamical-intelligence.md)
[Computational Science](note.html?n=epistemica/computational-science.md)
[Formal Concept Analysis (FCA)](note.html?n=epistemica/formal-concept-analysis-fca.md)
[**System of Units of Measurement**](note.html?n=epistemica/system-of-units-of-measurement.md)
[Exploratory Data Analysis (EDA)](note.html?n=epistemica/exploratory-data-analysis-eda.md)

#### Relations among connectors

> The question "what is the relation between $C$ and $X \to Y$?" has four precise answers, and they must not be merged:

| Situation | Formal object | Relation | Epistemic name |
| --- | --- | --- | --- |
| A model instance realizes the schema | $C$ is an object of the slice category $\mathcal{C}/Y$ over the map $f$ | instance-of / realization | model instantiation |
| Several $X$ contexts produce the same $y$ | pullback $X_1 \times_Y X_2 = \{(x_1,x_2) : f_1(x_1)=f_2(x_2)\}$ | fibre product | observational indistinguishability of inputs |
| Several models produce the same $y$ | kernel pair $\ker B = \{(C_1,C_2) : B(C_1)=B(C_2)\}$ | equivalence relation | observational equivalence; identifiability class |
| A connector $u$ links two maps without changing behaviour | commuting triangle $f_2 \circ u = f_1$ | isomorphism in $\mathcal{C}/Y$ | reparameterization / gauge equivalence |
| Different structure, same behaviour | $C_1 \sim C_2$ but $C_1 \not\cong C_2$ | equivalence without isomorphism | right for the wrong reasons |
| Different trajectories, same final state | non-injective flow map | many-to-one | equifinality |
| Same conditional distribution, different causal graph | Markov equivalence class | distributional equivalence | causal underdetermination |
| Same response distribution up to an affine transform | group action on the parameter space | gauge orbit | linking / equating (IRT) |

> The dual pair **kernel / coequalizer** is the formal core: the kernel pair names what cannot be distinguished, and its coequalizer — the quotient $\mathcal{H}/\!\sim$ — is the object the observation identifies. Non-injective $f$ therefore does not make the model wrong; it makes only the class $[x]$ identifiable.

> A connector $C$ in the narrow sense is a **morphism of the modelling diagram**, not a fourth kind of entity. If $C$ is a channel that carries $X$ to $Y$, it is `Epistemic Infrastructure`; if $C$ is a reparameterization between two representations, it is a morphism in the slice; if $C$ is a shared latent parameter linking two maps, the two maps form a span over the latent space. The relation type follows from which of these the connector is.

#### Identifiability, equivalence, and the "right for the wrong reasons" failure

> **Identifiability** is the injectivity of the behaviour map on the admissible hypothesis class, modulo gauge. It is *structural* when it holds for ideal data and *practical* when the fibre is small relative to noise and sample size. It is *global* or *local*, and it applies to parameters, inputs, or model structure.

> **Equifinality** is the special case of a non-injective input-to-output map over trajectories: different initial states or paths reach the same final observation. It is a property of open, dissipative, or regulated systems, not a failure of the observer.

> **Functional equivalence** is the same schema on a different hypothesis space: different organizational structures producing the same function. The organizational case and the dynamical case are instances of one relation, not two theories.

> **Gauge equivalence** is the case in which a group acts on the representation while leaving every observation invariant. Only the orbit is identified; a gauge-fixing convention — a scale, a reference level, a normalization — is what turns an orbit into a point. Linking and equating in item-response models is exactly this: the parameters are identified only up to an affine transformation.

> **Right for the wrong reasons** names the failure in which $C \sim C^\*$ (the model reproduces the observations) while $C \not\cong C^\*$ (the model does not reproduce the structure). Predictive success is behavioural equivalence, not structural identification. The diagnostic is not more fit but a different test: intervene on the target, evaluate out of distribution, test parameter and structural stability, and run an identifiability analysis before treating a validated model as the model. Underdetermination by data is the general form; a validated model in a non-trivial fibre has not been identified, only admitted.

> The five literatures behind this note are five instances of the same schema: structural identifiability of parametric models, equivalence problems in model structure, equifinality in open systems, functional equivalence in organization design, and scale linking in psychometrics. They differ in what $\mathcal{H}$ contains and in what the equivalence relation preserves — parameters, structures, trajectories, functions, or scales — not in the identification diagram.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Modelling Practice Set | The organized practice of issuing a map from a target segment to an observation, with the operations and evaluations that make the map answerable. |
| `Aggregate` → Modelling Practice Set → `Epistemic Orientation` | Grouping: the question the model answers and the purpose it serves. |
| `Aggregate` → Modelling Practice Set → `Epistemic Orientation` → `Epistemic Purpose` | Grouping: purposes of modelling. |
| `Aggregate` → Modelling Practice Set → `Epistemic Orientation` → `Epistemic Purpose` → Compression Purpose | Minimize description length while preserving explanation, prediction, or intervention. |
| `Aggregate` → Modelling Practice Set → `Epistemic Orientation` → `Epistemic Question` | Grouping: the question that fixes the known/unknown partition. |
| `Aggregate` → Modelling Practice Set → `Epistemic Orientation` → `Epistemic Question` → Forward Or Inverse Question | Whether to compute the output from the map or to recover the map, its inputs, or its parameters from the output. |
| `Aggregate` → Modelling Practice Set → `Epistemic Target` | Grouping: what the model is about. |
| `Aggregate` → Modelling Practice Set → `Epistemic Target` → `Target Segment` | Grouping: the bounded portion of reality under description. |
| `Aggregate` → Modelling Practice Set → `Epistemic Target` → `Target Segment` → Modelled Segment | The selected piece of observer-independent reality, at a declared level of organization. |
| `Aggregate` → Modelling Practice Set → `Epistemic Target` → `Observable` | Grouping: the features of the target that the model addresses. |
| `Aggregate` → Modelling Practice Set → `Epistemic Target` → `Observable` → Observed Response | The registered output $y$ against which the model is checked. |
| `Aggregate` → Modelling Practice Set → `Epistemic Target` → `Target Element` | Grouping: the constituent objects or states of the target. |
| `Aggregate` → Modelling Practice Set → `Epistemic Target` → `Target Element` → System State | The configuration $x$ of the target at the resolution relevant to the problem. |
| `Aggregate` → Modelling Practice Set → `Epistemic Access` | Grouping: how the target becomes registrable. |
| `Aggregate` → Modelling Practice Set → `Epistemic Access` → `Observation Interface` | Grouping: the boundary mechanism coupling target and observer. |
| `Aggregate` → Modelling Practice Set → `Epistemic Access` → `Observation Interface` → Measurement Channel | The instrument, sensor, or protocol that produces the observation. |
| `Aggregate` → Modelling Practice Set → `Epistemic Access` → `Observation Record` | Grouping: what is retained from the observation. |
| `Aggregate` → Modelling Practice Set → `Epistemic Access` → `Observation Record` → Observation Record Set | The dataset of registered observations, including its noise and sampling conditions. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` | Grouping: the map and its constituents. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` | Grouping: the sign system in which the model is expressed. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` → Model Map | The map $f_\theta : X \to Y$ together with its parameters and admissible domain. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` | Grouping: the combinable constituents of the map. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` → Input Variable | The $X$ role: state, predictor, input, or context. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` → Output Variable | The $Y$ role: observable, response, or computed output. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Representation Element` → Model Parameter | The $\theta$ role: the quantities estimated or identified. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Constitutive Substrate` | Grouping: the rules that constitute the map. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Constitutive Substrate` → Functional Form | The equations, rules, or architecture relating $X$ to $Y$. |
| `Aggregate` → Modelling Practice Set → `Epistemic Representation` → `Representational System` → Model Map → `Constitutive Substrate` → Identification Constraint | The gauge, scale, or normalization convention that turns an orbit into a point. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` | Grouping: what is done with the representation. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Action` | Grouping: direct transformations of epistemic content. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Action` → Forward Evaluation | Compute $y$ from the map, its parameters, and an input. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Action` → `Inference` | Grouping: derivations from observations back to the model. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Action` → `Inference` → Inverse Inference | Recover an input, state, or structure consistent with the observation. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Action` → `Inference` → Parameter Estimation | Estimate the parameter vector from input–output data. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Organization` | Grouping: reproducible organizations of the operations. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Organization` → `Method` | Grouping: generalized ways of modelling. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Organization` → `Method` → Identification Method | The organized procedure that selects a model class and estimates it, a priori or a posteriori. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Organization` → `Procedure` | Grouping: ordered routines within a method. |
| `Aggregate` → Modelling Practice Set → `Epistemic Operation` → `Organization` → `Procedure` → Model Selection Procedure | The routine that compares candidate structures under an identifiability and validation criterion. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` | Grouping: how the model and the inference are judged. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: standards of judgment. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` → `Epistemic Standard` → Identifiability Standard | Structural or practical uniqueness of the identified object modulo gauge. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` → `Epistemic Criterion` | Grouping: evaluated properties. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` → `Epistemic Criterion` → Observational Equivalence Criterion | Whether two model instances lie in the same fibre of the behaviour map. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` → `Validation` | Grouping: checks against observation. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` → `Validation` → Behavioural Validation | Prediction error, replication, and intervention tests of the map's behaviour. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` → `Error` | Grouping: deviations and failures. |
| `Aggregate` → Modelling Practice Set → `Epistemic Evaluation` → `Error` → Structural Error | Behavioural equivalence with structural inadequacy: right for the wrong reasons. |
| `Aggregate` → Modelling Practice Set → `Epistemic Context` | Grouping: the conditions under which the practice occurs. |
| `Aggregate` → Modelling Practice Set → `Epistemic Context` → `Epistemic Condition` | Grouping: surrounding conditions. |
| `Aggregate` → Modelling Practice Set → `Epistemic Context` → `Epistemic Condition` → Noise Condition | The noise, sampling, and disturbance regime that governs practical identifiability. |
| `Aggregate` → Modelling Practice Set → `Epistemic Infrastructure` | Grouping: what supports the practice. |
| `Aggregate` → Modelling Practice Set → `Epistemic Infrastructure` → `Epistemic Tool` | Grouping: instruments of modelling. |
| `Aggregate` → Modelling Practice Set → `Epistemic Infrastructure` → `Epistemic Tool` → Estimator | The estimator, solver, or optimizer that performs the inference. |
| `Aggregate` → Modelling Practice Set → `Epistemic Infrastructure` → `Information Repository` | Grouping: stored observations and models. |
| `Aggregate` → Modelling Practice Set → `Epistemic Infrastructure` → `Information Repository` → Observation Dataset | The retained observations, metadata, and provenance used by the practice. |

### What is a critical conceptual evaluation of this `epistemic element instance`?

> **Verdicts.** The instance is conceptually well identified: pass. Its definition is clear enough to use but leaves "connector" under-specified: partial. Its determinacy is carried by the fibre/quotient construction: pass. It is internally consistent once the role of $Y$ is indexed by problem type: pass. Its representational adequacy covers deterministic forward, inverse, estimation, and identification problems and needs extension for stochastic and causal cases: partial. Its purpose adequacy — supporting identifiability analysis, model discrimination, and the diagnosis of right-for-the-wrong-reasons — is high: pass.

| Criterion | Verdict | Diagnostic |
| --- | --- | --- |
| **Conceptual Identification** | Pass | The instance is the modelling practice, not the target; the behaviour map names what is identified and the fibre names what is not. |
| **Definitional Clarity** | Partial | $X$ and $Y$ are role names, not kinds; the note fixes them by the problem specification. "Connector" is locally defined as model instance, morphism, or channel, but the term invites conflation. |
| **Conceptual Determinacy** | Pass | "What is identified?" has a determinate answer: the quotient of the hypothesis space by observational equivalence, modulo gauge. |
| **Internal Consistency** | Pass | The apparent conflict between "$Y$ is known" and the forward problem is resolved by indexing $Y$'s role to the problem type. |
| **Representational Adequacy** | Partial | The functional map covers forward, inverse, estimation, and identification; stochastic kernels, causal equivalence classes, and partial observability require the kernel/Markov-equivalence extensions stated in the relation table. |
| **Purpose Adequacy** | Pass | The schema supports identifiability analysis, equivalence testing, model selection, and the separation of predictive success from structural adequacy. |

#### On Feasible of Modelling

> ¿Can system x be model? ¿What’s the nature of such model?
> 

> What **factors impact the feasible modeling** task for a particular problem?
> 

> See this in Philosophia Naturalis.
> 

#### Evolution of Modelling

> Theories of modelling !!!
> 

> **Metamodeling** is the process of creating abstract models (metamodels) that define the structure, semantics, and rules of other models within a specific domain, enabling consistency, interoperability, and analysis across different modeling systems.
> 

> Studying the history of **scientific modeling dogmas** unveils the evolution of human understanding, reveals the diverse perspectives that shaped scientific inquiry, and sheds light on the dynamic interplay between theories, paradigms, and the advancement of knowledge.
> 

> “Res cogitans” “thinking thing” it refers to the mind or consciousness as a distinct entity capable of thought and awareness.
> 

> Res Extensa refers to the “extended thing” or physical matter.
> 

> “The likelihood of a theory being true decreases as the number of sentences it comprises increases.”
> 

> **Intelligible Form**: An intelligible form refers to an abstract, conceptual essence or pattern that can be understood through rational thought rather than sensed through physical perception.
> 

> **Newton Meta-Model**: It is commonly believed that Newton showed that the world is a machine, following mechanical principles, and that we can therefore dismiss “the ghost in the machine,” the mind, with appropriate ridicule. The facts are the opposite: Newton exorcised the machine, leaving the ghost intact. The mind-body problem in its scientific form did indeed vanish as unformulable, because one of its terms, body, does not exist in any intelligible form. Newton knew this very well, and so did his great contemporaries.
> 

- Simplex Linear Systems /  Mechanical Systems
- Complex Systems

- **Pre-Scientific Era**: No specific dogma existed, as scientific methods still needed to be formalized.
- **Mechanical Philosophy (17th century)**: The belief that the world operates as if constructed by a skilled artisan, leading to the idea that understanding the world entails creating a mechanical model. This model was used by Galileo, Descartes …
    - **Mechanical Philosophy** - Everything in the universe can be understood in mechanical terms [which are intuitive to human beings; e.g., babies assume a hidden point of contact when shown a cause and effect at a distance]. In mechanical philosophy, the nature of the universe is intelligible to us through direct observation.
    - **Exorcising the Ghost In the Machine** - Understanding nature in direct mechanical terms.
    - **Newton**, to his dismay (and ridicule by his contemporaries), showed that the Mechanical Philosophy was incoherent because the “action at a distance” posited in his theory of gravity could not be explained in purely mechanical terms.
    - **Descartes** was interested in phenomena that could not be modeled using mechanical devices alone, such as mental phenomena.
- **Vitalism (18th century)**: Living organisms possess a unique life force or vital principle that cannot be explained solely by mechanical principles.
- **Positivism (19th century)**: Knowledge should be based on empirical observation, and scientific models should focus on observable facts and verifiable data.
- **Reductionism (20th century)**: Complex phenomena can be understood by reducing them to their fundamental constituent parts, as various scientific disciplines advocate.
- **Systems Theory (mid-20th century)**: Emphasizes the interconnectedness and interdependencies of elements within a system, considering holistic perspectives.
- **Computational Modeling (late 20th century)**: Utilizing computational methods and simulations to model and understand complex phenomena, such as weather patterns or biological processes.
- **Complexity Theory (late 20th century)**: Examines how complex systems exhibit emergent properties that the properties of their components cannot fully explain.
- **Integrative and Multidisciplinary Approaches (present)**: Recognizes the need for interdisciplinary collaboration and integrating different scientific models and perspectives to tackle complex real-world problems.
- [AI Guided Models](https://news.ycombinator.com/item?id=40298927)

## QA

### What is the nature of the ‘Variable Reality Aspect Type Abstraction’ as an epistemic element? What is its history?

> This appears to be one of the greatest breakthroughs in human thought—especially the development of numerical variables.
> 

## References

- [Philosophy](note.html?n=epistemica/theory/philosophy.md)
- [Epistemic Artifact](note.html?n=epistemica/theory/practice/epistemic-artifact.md)
- A General Guide to Representation & Estimation

- **Model Theory**
- [Epistemology](note.html?n=epistemica/theory/practice/general/epistemology.md)
- (**Church–Turing Thesis**) Computationalism
- Dynamical Intelligence
- https://en.wikipedia.org/wiki/Metamodeling
- [Science, Mind, and Limits of Understanding](https://chomsky.info/201401__/)
- [Intelligible Form](https://en.wikipedia.org/wiki/Intelligible_form)
- [The machine, the ghost, and the limits of understanding: Newton’s contributions to the study of mind](https://www.reddit.com/r/philosophy/comments/28a9bj/noam_chomsky_the_machine_the_ghost_and_the_limits/)
- [Chomsky – The Machine, the Ghost and the Limits of Understanding](https://news.ycombinator.com/item?id=26448901)
- [The Mysteries of Nature: How Deeply Hidden?](https://web.ics.purdue.edu/~drkelly/ChomskyMysteriesNatureHidden2009.pdf)
- [Corpuscularianism](https://en.wikipedia.org/wiki/Corpuscularianism)
- https://www.nature.com/articles/s41586-022-05543-x
- Peer review is an honor-based system ([lemire.me](http://lemire.me/))
[https://news.ycombinator.com/item?id=38982912](https://news.ycombinator.com/item?id=38982912)
- [Ontology](note.html?n=epistemica/theory/practice/general/ontology.md)
- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Philosophia Conceptuum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-conceptuum-et-operis.md)
- Anstett-Collin, F., Denis-Vidal, L., & Millérioux, L. (2020). A priori identifiability: An overview on definitions and approaches. *Annual Reviews in Control*, 50, 139–149.
- Bekey, G. A., & Hadaegh, F. Y. (1982). Equivalence problems in structural identifiability. *Mathematics and Computers in Simulation*, 24(6), 460–465.
- von Bertalanffy, L. (1950). The theory of open systems in physics and biology. *Science*, 111(2872), 23–29.
- Gresov, C., & Drazin, R. (1997). Equifinality: Functional equivalence in organization design. *Academy of Management Review*, 22(3), 403–428.
- van der Linden, W. J., & Barrett, M. D. (2016). Linking item response model parameters. *Psychometrika*, 81(3), 650–673. https://doi.org/10.1007/s11336-015-9469-6
- Quine, W. V. O. (1951). Two dogmas of empiricism. *The Philosophical Review*, 60(1), 20–43.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
