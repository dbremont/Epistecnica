---
tags: [epistemology, tooling]
---

# Explanation

Related: [Truth](note.html?n=epistemica/theory/practice/truth.md), [Reason](note.html?n=epistemica/theory/practice/general/reason.md), [Evolutionary Explanation](note.html?n=epistemica/theory/practice/evolutionary-explanation.md), [Causality](note.html?n=epistemica/theory/ontology/causality.md)

> In this note we will explain **explanations**—one of the most useful, if not the most useful, **epistemic praxis**.
> 

> **Explanation** is the practice of **(extracting)** identifying regularities in the connection between **observable effects** (phenomena) and the **underlying ontology** (states, structures, and dynamics), making these **connections** explicit, clear, and intelligible, thereby enabling answers to why things are the way they are and not otherwise. Another way to see it is - **removing the magic** from the underlying ontology → by compressing it - reducing it to the core - to what’s matter.
> 

> An **explanation** is a structured mapping that connects a phenomenon or entity (**`explanandum`**) to an intelligible conceptual, formal, or mechanistic structure (**`explanans`**), which renders the phenomenon understandable, predictable, or actionable. It serves the function answering why questions - and grounding the answers that we give about a given **`explanandum`.**
> 

> An **explanation** is a set of statements that represents **these connections**.
> 

> **Note:** By this account, explanations are not about particular (singular) cases; they concern the relationship between effects and classes of cases. Explanations require testing, and singular cases generally cannot be tested because their conditions often cannot be recreated.
> 
> 
> When analysis focuses on singular cases, it often drifts into deterministic narratives or speculative accounts. The only reliable way to avoid this is to analyze classes of cases, where regularities can be identified and tested.
> 
> This is also the only way to strip away the apparent “magic” of the ontology: singular cases can often be grounded in many different underlying ontological accounts, making them insufficient for establishing explanatory validity.
> 
> **Note:** The term *explanation* is often applied to singular cases (e.g., *a fire → smoke*). However, in such instances what occurs is not the construction of a new explanation but the **instantiation or application of a general explanatory relation** to a particular case. The explanatory work is performed at the level of the **general class of events**, while the singular case merely **recasts that general explanation under specific conditions**.
> 

> An explanation is a rule or principle derived from observed regularities, which helps to **assemble coherent accounts of individual observed events**. The stronger the regularity linking a class of phenomena to its underlying substrate, the more concise and unified these accounts can be.
> 

> **What remains in this note is the task of explaining** how to do this and how to evaluate our explanations.
> 

> **Note:** The term **‘Explanation’** is often used loosely to refer both to the connection between a phenomenon and its underlying ontic structure, and to the observation that emerges from this connection. It is also used to denote the application of this understanding to particular cases. However, there is no true explanation of singular cases—only applications of the general principle.
> 

Guiding Questions:

- What kinds of statements constitute an explanation?
- What makes an explanation good?
- What do we mean by “Why?”
- Are all forms of **explanation ultimately contrastive**—answering why things are this way rather than some relevant alternative?
- How to evaluate explanations - of the past? We only know one realization - not the different future that were not realized?
- Which are the limits of evolutionary explanation in the light of stochasticlity?
- What is the role of counterfactuals in explanations?

## Term

> What are the semantics of the term *explanation*?
> 

> La palabra **explicar** viene del latín *explicare* (“desplegar, desenrollar”), formado por *ex-* (“afuera”) y *plicare* (“doblar”), con el sentido original de “desdoblar algo para hacerlo claro”.
> 

| Area | Description |
| --- | --- |
| **Cognitive** | A mental model or representation that makes a phenomenon intelligible. |
| **Communicative / Linguistic** | A statement, narrative, or discourse that conveys understanding from one agent to another. |
| **Philosophical / Epistemic** | Justification or account that connects facts, causes, or principles to the phenomenon, supporting knowledge claims. |
| **Scientific / Mechanistic** | The description of mechanisms, processes, or laws that generate the phenomenon. |
| **Statistical / Probabilistic** | An account that expresses the likelihood or regularity of a phenomenon rather than deterministic causation. |
| **Functional / Teleological** | Explains the purpose, role, or function of a phenomenon within a system. |
| **Pragmatic / Action-Oriented** | Serves to guide decisions or actions, showing consequences or reasons for a phenomenon in context. |
| **Mathematical / Formal** | A derivation or proof showing how a result logically follows from axioms or rules. |
| **Psychological / Human-Behavioral** | Understanding a person’s actions or decisions in terms of motives, beliefs, or intentions. |
| **Legal** | A structured reasoning or argument that justifies a decision, ruling, or interpretation of law based on evidence, precedent, and legal principles. |

## Formulation

> An **explanation** is a set of statements that **uncover or clarify the underlying factors** behind a phenomenon. Statements that constitute explanations are not merely descriptive; they **connect phenomena to causes, mechanisms, principles, probabilities, or functions** in a way that makes the phenomenon intelligible.
> 

> An explanation unrolls the phenomenon in terms of an explanatory basis, rendering it comprehensible, testable, etc.
> 

> Explanation is a human cognitive construct and operational process. Its forms and rigor are historically contingent, evolving with knowledge and context. It is dynamic rather than purely statistical, embodying the active structuring of understanding.
> 

### Formal Schema

An explanation can be modeled as a tuple: $\mathcal{E} = \langle P, B, R, C \rangle$

where:

- $(P):$ **Explanandum** (*the phenomenon to be explained*): the target event, regularity, or proposition.
- $(B)$: **Explanans** (*the explanatory basis*): a set of statements, facts, or principles.
- $(R)$: explanatory relation (logical, probabilistic, causal, structural).
- $(C)$: context (background knowledge, pragmatic interests, audience).

Such that:

1. $R(B, P)$ holds (dependence condition).
2. $(B)$ is factually adequate.
3. $(R)$ is contextually relevant (answers the explanatory demand).
4. $(\mathcal{E})$ enhances intelligibility of $(P)$.

### Explanatory Relation

Different explanatory frameworks instantiate the $(B \Rightarrow P)$ relation differently:

- **Deductive-Nomological (Hempel–Oppenheim model):** $(B = {L, C})$, where $(L)$ are laws and $(C)$ conditions. Then $L \wedge C \vdash P$
- **Inductive-Statistical:** (B) makes (P) highly probable: $Pr(P|B) \approx 1$
- **Causal-Mechanistic:** (B) describes causal processes/mechanisms such that $Cause(B) \to Effect(P)$
- **Structural-Functional (systems):** (B) specifies the role or function of (P) within a system (S).

### Validity

> An explanation $\mathcal{E}(B, P)$, where $(B)$ is the basis and $(F)$ the phenomenon, must satisfy:
> 
1. **Dependence**: (F) must depend on (B) in a way relevant to the explanatory context.
    - Logical dependence (deduction, probability).
    - Causal dependence (event caused by mechanism).
    - Structural dependence (part–whole, functional, systemic).
2. **Correctness**: (B) must be factually adequate (true, approximately true, or empirically well-supported).
3. **Relevance**: The relation $(B \Rightarrow F)$ must single out factors that answer a why/how-question about (P).
4. **Cognitive Function**: (B) must increase understanding of (F) for a cognitive agent (answering a request for explanation).

## Technique Space

> How to explain ‘things’?
> 

| Category | Technique | Description | Usage Guide |
| --- | --- | --- | --- |
| **Causal Analysis** | **Mechanism Decomposition** | Break the phenomenon into the chain of causal processes that generate it. | Identify entities, activities, and interactions that produce the outcome. |
|  | **Causal Graph Modeling** | Represent causal dependencies using directed graphs (DAGs). | Useful for disentangling confounders, mediators, and causal pathways. |
|  | **Process Tracing** | Reconstruct the sequence of events that produced the phenomenon. | Common in history, political science, and case analysis. |
|  | **Intervention Analysis** | Evaluate what happens when variables are manipulated. | Core method in experimental sciences. |
| **Counterfactual Reasoning** | **Counterfactual Testing** | Ask whether the phenomenon would occur if a factor were absent. | Identifies causal necessity and sufficiency. |
| **Counterfactual Reasoning** | **Contrastive Analysis** | Explain why outcome A occurred rather than outcome B. | Central in historical and social explanations. |
| **Statistical Methods** | **Regression Analysis** | Identify statistical relationships between variables. | Used when causal mechanisms are partially unknown. |
| **Statistical Methods** | **Statistical Relevance Analysis** | Determine which factors change the probability of the phenomenon. | Focuses on probabilistic dependence. |
| **Comparative Methods** | **Controlled Comparison** | Compare similar systems differing in one variable. | Classic method in comparative politics and sociology. |
| **Comparative Methods** | **Natural Experiments** | Exploit exogenous variation to infer causal relationships. | Used in economics and social sciences. |
| **Mechanistic Methods** | **Mechanistic Modeling** | Construct models of interacting components generating the phenomenon. | Used in biology, engineering, and complex systems. |
| **Mechanistic Methods** | **Simulation Modeling** | Simulate system dynamics computationally. | Useful when analytical solutions are impossible. |
| **Formal Methods** | **Mathematical Derivation** | Show that a phenomenon logically follows from axioms or equations. | Typical in physics and mathematics. |
| **Formal Methods** | **Proof by Model Construction** | Build a model demonstrating how the phenomenon emerges. | Used in theoretical science. |
| **Systems Analysis** | **Structural Analysis** | Explain phenomena in terms of system architecture and relationships. | Useful for institutions and complex networks. |
| **Systems Analysis** | **Functional Decomposition** | Explain phenomena in terms of the roles components play in a system. | Common in biology and engineering. |
| **Historical Methods** | **Path Dependence Analysis** | Explain outcomes as consequences of historical sequences. | Important in institutional and technological evolution. |
| **Historical Methods** | **Genealogical Reconstruction** | Trace the origin and evolution of structures or practices. | Used in anthropology and historical sociology. |
| **Cognitive / Behavioral** | **Intentional Reconstruction** | Explain actions in terms of beliefs, desires, and rational choices. | Standard in economics and decision theory. |
| **Cognitive / Behavioral** | **Behavioral Mechanism Analysis** | Explain actions through cognitive biases or psychological mechanisms. | Used in behavioral sciences. |
| **Complex Systems** | **Emergence Analysis** | Explain macro phenomena arising from micro-level interactions. | Useful in markets, traffic, ecosystems. |
| **Complex Systems** | **Agent-Based Modeling** | Simulate agents interacting under rules to reproduce observed patterns. | Used in economics, sociology, ecology. |
| **Unification Methods** | **Theory Unification** | Show that multiple phenomena follow from the same underlying theory. | Classic explanatory strategy in physics. |
| **Heuristic Methods** | **Abductive Inference** | Infer the best explanation among competing hypotheses. | Used when mechanisms are uncertain. |

## Evaluation

> What are the criteria to evaluate an explanation?
> 

> A good explanation must account for why things work this way and why they don’t work that way.
> 

| **Criterion** | **Description** | **Case** |
| --- | --- | --- |
| **Causal (Mechanistic Adequacy)** | It identifies the causes or mechanisms responsible. | Plant phototropism occurs due to auxin redistribution, causing differential cell elongation. |
| **Scope (Generality)** | Applies beyond a single instance; reveals broader patterns or laws. | Newton’s law of gravity explains both falling apples and planetary orbits. |
|  |  |  |
| **Precision (Specificity)** | Provides sufficient detail to distinguish the phenomenon. | Traffic jams result from high-density lane changes, not merely “human behavior.” |
| **Consistency (Coherence)** | Does not contradict established knowledge or internal logic. | A biological explanation should align with known cellular and molecular processes. |
| **Simplicity (Parsimony)** | Avoids unnecessary assumptions; prefers simpler explanations. | Newtonian gravity is simpler and more testable than invoking mysterious forces. |
| **Falsifiability (Testability)** | Can, in principle, be tested and potentially refuted. | A scientific hypothesis about disease transmission must allow predictions that could be experimentally verified. |
| **Hard-to-Vary (Deutsch Criterion)** | The explanation (that is **`explanans`**) cannot be **easily changed or adjusted without losing** essential explanatory power. | Evolution by natural selection is hard to vary: alternative explanations either fail to explain observed adaptation patterns or require ad hoc assumptions. |
| **Veracity** | The explanation is true or approximately true, corresponding to reality. | The germ theory of disease accurately identifies microbes as the cause of specific illnesses. |
| **Empirical Adequacy** | It **accounts for what is observed.** | Plate tectonics explains continental drift, seismic activity, and mountain formation. |

### **Hard-to-Vary (Deutsch Criterion)**

> An explanation is an account of a set of observations. If that account can be reused to explain many different phenomena because it lacks constraints, then it is easy to vary.
> 

Case:

- Good Explanation:  **Planets follow trajectories** determined by inverse-square **gravitational attraction and conservation laws**.
- Bad Explanation:  **Planets move** the way they do because that is how the **heavens arrange them**.

## Theory

> Which are the different model of explanation? How to explain explanations?
> 

### Taxonomy

| **Type of Explanation** | **Description** |
| --- | --- |
| **Causal** | Cites the event or mechanism that brings about (or sustains) the phenomenon being explained. |
| **Teleological** | Explains by giving the purpose or function of the phenomenon. |
| **Formal** | Cites the shape, structure, or form of the phenomenon as an explanation. |
| **Material** | Cites the material components that make up the phenomenon. |

### Model

> A **model of explanation** is a structured framework that specifies the relation between what needs to be explained (**explanandum**) and what does the explaining (**explanans**), defining the conditions under which an explanation counts as adequate (e.g., causal, deductive-nomological, statistical, mechanistic, or functional).
> 

> There is not a universal model of explanation;  it seems very domain specific.
> 

> See more here [Explanatory Relation](note.html?n=epistemica/theory/practice/explanation.md).
> 

| **Model** | **Description** | **Evaluation (Scope and Limits)** | **Tags(s)** |
| --- | --- | --- | --- |
| **Deductive-Nomological (D-N) Model** | Uses general laws and initial conditions to logically deduce an event ("covering law" model). | Strong in explaining deterministic phenomena where laws are known. Limited for probabilistic or context-dependent events; cannot handle singular or complex social events well. | Logical, Scientific, Deterministic |
| **Inductive-Statistical (I-S) Model** | Explains events with probabilistic laws, applicable when phenomena have statistical patterns. | Useful for populations or repeated events; limited for individual cases or events without clear statistical regularity. | Probabilistic, Statistical, Scientific |
| **Causal Explanation Model** | Identifies and explains causes to understand why events occur. | Broad applicability; can struggle with complex, multi-factorial, or emergent phenomena where causality is non-linear or distributed. | Causal, Mechanistic, Scientific |
| **Functional Explanation Model** | Explains events by their function or role within a system. | Effective in systems biology or social systems; limited when function is unclear or when explaining origins rather than current role. | Functional, Systemic, Teleonomic |
| **Teleological Explanation Model** | Uses purpose or goals to explain events, common in philosophy and biology. | Useful for goal-directed systems; limited in purely mechanistic contexts or where intentions are unknown or non-existent. | Teleological, Goal-Oriented, Normative |
| **Mechanistic Explanation Model** | Details mechanisms and processes that produce phenomena. | Very precise for well-understood systems; limited when mechanisms are unknown or highly complex. | Mechanistic, Process-Oriented, Scientific |
| **Narrative Explanation Model** | Explains events through a coherent storyline connecting them. | Strong in historical or social contexts; may lack predictive power and can be subjective. | Narrative, Historical, Interpretive |
| **Pragmatic or Contextual Explanation Model** | Tailors explanations to the context and needs of the audience. | Flexible and audience-focused; may sacrifice generalizability or rigor for applicability. | Pragmatic, Contextual, Applied |
| **Intentional or Rational Explanation Model** | Examines actions based on the intentions, beliefs, or desires behind them. | Effective for human behavior and decision-making; limited when intentions are hidden, irrational, or non-agent-based. | Intentional, Rational, Agent-Centered |
| **Unificationist Model** | Unifies disparate phenomena under a single coherent framework. | Provides overarching insight and theoretical elegance; limited when phenomena resist simplification or unification. | Unification, Theoretical, Scientific |
| **Statistical-Relevance Model** | Shows which statistical factors are relevant to an event, emphasizing relevance over causation. | Useful for identifying key variables; limited in explaining causal mechanisms or deeper system dynamics. | Statistical, Probabilistic, Analytical |
| **Evolutionary Explanation Model** | Explains phenomena as products of evolutionary processes, adaptation, or natural selection. | Powerful in biology and adaptive systems; limited for explaining non-evolutionary phenomena or rapid social/cultural changes. | Evolutionary, Biological, Functional |

### **The Symmetry Problem**

> **Let’s consider `The Flagpole Problem`** in which   **flagpole of height (H)** standing vertically on the ground. When sunlight hits the pole at an angle ($\theta$), it casts a **shadow of length (L)**. Using basic geometry:   $L = \frac{H}{\tan(\theta)}$,  we can de we can **deduce** the length of the shadow (L) - based on  the **height of the flagpole** H and the **angle of the sun** $\theta$.
> 

> This seems like a perfectly good **scientific explanation**: The shadow has length (L) **because** the pole has height (H) and the sun is at angle ($\theta$).
> 

> The **Symmetry** Problem:  However, the same equation can be rearranged:  $H = L \tan(\theta)$,  So if we know: the **shadow length** (L) and  the **sun angle** (\theta) we can deduce the **height of the flagpole** (H).
> 

> Logically, this deduction is **just as valid**.  But it sounds wrong to say: The flagpole has height (H) **because** its shadow is length (L). The **shadow does not explain the height**.
> 

> This is actually a **problem of language rather than of explanation itself**. In explanation, we typically ground our account in the **underlying ontology**—the states, structures, and dynamics that generate the observed phenomena.
> 
> 
> However, once the connection between ontology and observable effects is established, we can often **rearrange the relation** and infer aspects of the underlying ontology from the observations. In that sense, the relation can be used in both directions: from ontology → observation (explanation) and from observation → ontology (inference or reconstruction).
> 
> It is called a **connection** for a reason. In simple systems—like the flagpole and its shadow—this reversal is straightforward because the mapping between variables is simple and well-defined.
> 
> In more complex systems, however, the situation changes. The observable results are usually **much simpler than the underlying ontology that produces them**. As a consequence, many different ontological configurations may produce the same observable outcome. This makes the reverse mapping—from observations back to the underlying substrate—much harder and often underdetermined.
> 

## Limitation

> What are the limits of explaining this **`*explanandum*`**?  Each class of **`explanandum`** calls for a specific explanatory mode, yet complex social phenomena systematically challenge the adequacy and closure of all such modes.
> 

> Can every observation be ‘explain’? Can we connect every observation with underlying mechanisms - even if they are probabilistic? A Kind of Scientific Maximalism.
> 

| **Limit** | **Description** | **Instance** |
| --- | --- | --- |
| **Observational Complexity** | Some phenomena are too complex or entangled for complete causal explanation; interactions may be nonlinear, stochastic, or context-dependent. | Explaining why a specific neighborhood experiences sudden social unrest despite multiple socioeconomic interventions. |
| **Singular/Unique Events** | Unique events may not have generalizable causes, limiting explanatory power to analogies or narratives rather than law-like accounts. | A one-time catastrophic failure of a new technological system that has no historical precedent. |
| **Incomplete Knowledge** | Limits in empirical access or measurement prevent fully grounded explanations; unknown variables can disrupt causal accounts. | Early climate modeling before greenhouse gas dynamics were understood. |
| **Emergent Phenomena** | Macro-level patterns arise from micro-level interactions in ways that cannot be fully deduced from the parts. | Traffic jams forming spontaneously without a clear triggering incident. |
| **Temporal/Contextual Dependence** | Causal factors may only operate under specific temporal or situational conditions, making universal explanations impossible. | A policy that works in one country but fails in another due to institutional differences. |
| Inherit Stochasticity | Some phenomena involve irreducible randomness or probabilistic processes that defy deterministic causal explanation; outcomes can be described only in statistical terms. | … |
| True Lack of Underlying Mechanisms (Non Characteriable  Stochasticity) | (Knightian Uncertainty) (Uncertainty of the Uncertainty Itself) Certain phenomena exhibit no discernible pattern, structure, or causal mechanism, appearing as pure noise or fundamental indeterminacy that resists any explanatory model. | The precise outbreak time of a rare, spontaneous riot in a city with no prior tensions or identifiable trigger, where all known factors show no correlation. |

## Case

> See details case study here.
> 

| **Phenomenon** | **Explanation** | **Evaluation Criteria** |
| --- | --- | --- |
| Water boils at 100°C at standard pressure | Boiling occurs because molecular kinetic energy overcomes intermolecular forces at this temperature | ✅ Accuracy, ✅ Causal/Mechanistic Adequacy, ✅ Precision, ✅ Consistency, ✅ Testability |
| Plants grow toward light (phototropism) | Auxin hormones redistribute to shaded side, causing differential cell elongation | ✅ Causal/Mechanistic Adequacy, ✅ Precision, ✅ Explanatory Power, ✅ Coherence |
| Traffic jams form spontaneously on highways | High-density lane changes create wave-like slowdowns | ✅ Mechanistic Adequacy, ✅ Scope, ✅ Precision, ✅ Explanatory Power |
| Apple falls from a tree | Newton’s law of universal gravitation pulls the apple toward Earth | ✅ Accuracy, ✅ Scope/Generality, ✅ Simplicity, ✅ Explanatory Power, ✅ Testability |
| Heart pumps blood | The heart circulates oxygen and nutrients to sustain the body | ✅ Functional Adequacy, ✅ Causal/Mechanistic Adequacy, ✅ Explanatory Power, ✅ Coherence |
| Water boils at 100°C | Because it wants to | ❌ Lacks Causal/Mechanistic Adequacy, ❌ Accuracy, ❌ Precision, ❌ Explanatory Power |
| Plants grow toward light | Because light is good | ❌ Lacks Causal/Mechanistic Adequacy, ❌ Precision, ❌ Testability |
| Traffic jams form | Because people are careless | ❌ Too vague, ❌ Lacks Mechanistic Adequacy, ❌ Explanatory Power |
| Apple falls | Because the apple is lazy | ❌ Nonsensical, ❌ Lacks Causal/Mechanistic Adequacy, ❌ Accuracy |
| Heart pumps blood | Because life is nice | ❌ Lacks Functional Adequacy, ❌ Causal/Mechanistic Adequacy, ❌ Explanatory Power |

## QA

### What type of activity is an explanation?

> An **explanation** is a **cognitive-epistemic activity**. More precisely, it is an activity aimed at **making sense of a phenomenon by revealing its causes, mechanisms, conditions, or rules**. It is about **understanding**, not just describing.
> 

### Can we have explanation for singular events?

> No, explanations by definition are general; they explain a **class of events**. A single instance can only be described.
> 

> A mistaken explanation confuses description with explanation. For example: *“We lost the war because the good is not without”* attempts to ‘explain’ the outcome of a single war. While it may suggest a broader framework—that the presence of ‘good’ influences war outcomes—it fails as a proper explanation for that one instance.
> 

> Take the case of ‘Explain the Chernobyl Failure’:  Explanations are derived from knowledge extracted from **classes of events**, and when we explain a singular event we are **applying that prior knowledge to a specific configuration**, not creating a new explanation. More than an explanation - this is just applications - of explanations - to account for an instance - than anything else.
> 

> We may need better terminology to distinguish **general explanatory grounding** (explanation) from its **application to particular scenarios** (an account).
> 

### What do we mean by ‘regularity’ and connection?

> **Regularity** refers to the invariant patterns—whether deterministic, stochastic, or structural—that persist across a class of phenomena. It does not imply a single, forced outcome (determinism), but rather a constrained "behavioral space" (e.g., a probability distribution or an attracter in a complex system).
> 

> **Connection** is the epistemic  link from  observations  to the  underlying **ontological substrate ground in the regularities.** An explanation uses the regularity as a filter to **"strip away" the magic and incidental noise**, reducing the substrate to its functional core—the essential states and dynamics that make the phenomenon intelligible.
> 

> Let’s apply this framework to analyze **path-dependent evolutions**. We still need to connect events to the **underlying substrate**. The current state of the substrate depends on past states and is explained by reference to those earlier states. Even if we observe only a single trajectory and lack multiple comparable cases, this does not prevent us from extracting general observations. Each **state transition** can be treated as an observation. Moreover, we can decompose a trajectory into segments, allowing us to derive **partial observations** from different parts of the process.
> 

> (Key Point) That is a **path-dependent phenomena is not an ‘observation’ it itself a class of observations** - and that allow us to extract patterns - and regularity - that inform the connections between the observed and underlying substrate.
> 

### What is the relation between explanation and causation?

> Causation is usually considered the ultimate form of explanation, but many phenomena—such as statistical associations, emergent behaviors, or cases where a causal model is not possible—require other ways of explaining. In such cases, the goal of explanation is to make the phenomenon intelligible, understandable, and conceptually manageable, even if a direct causal account cannot be provided.
> 

### Which are the targets of explanation?

> What are the objects of explanation? What are the limits of the explanations we can construct? How does the nature of the `explanandum`—e.g., deterministic, stochastic, chaotic, or unobservable—constrain and delimit admissible forms of explanation?
> 

### How should outcomes that depend on **human agency and intentionality be explained**?

> 

### What are the usual conflations in theories of explanation?

> A common conflation is the **confusion of explanatory techniques** (such as counterfactual reasoning) with the **core of explanation itself**—namely, the revelation of the connection between what we observe (phenomena) and the underlying substrate.
> 

> Another conflation occurs when explanations are treated as applying to **individual instances**, rather than to **classes of phenomena**.
> 

> This is similar to confusing the **abstract concept of number** with a **particular representation of numbers**, such as Indo-Arabic numerals.
> 

## References

- [Epistemology](note.html?n=epistemica/theory/practice/general/epistemology.md)
- https://plato.stanford.edu/entries/scientific-explanation/
- https://en.wikipedia.org/wiki/Explanation
- https://en.wikipedia.org/wiki/Georg_Henrik_von_Wright
- https://www.readthesequences.com/A-Technical-Explanation-Of-Technical-Explanation
- https://www.youtube.com/watch?v=3eEffbjzNwE
- O'Hear, Anthony. *Beyond evolution: Human nature and the limits of evolutionary explanation*. Clarendon Press, 1997.
- https://plato.stanford.edu/entries/evolution/
- Henrich, Natalie, and Joseph Patrick Henrich. *Why humans cooperate: A cultural and evolutionary explanation*. Oxford University Press, 2007.
- An Essay on Pattern, Prediction, Randomness and Explanation
- Causality
- https://www.lesswrong.com/posts/jcTsbaQ8hNc7qxwaQ/explanations-as-hard-to-vary-assertions
- [Pattern](note.html?n=epistemica/theory/practice/general/pattern.md)
