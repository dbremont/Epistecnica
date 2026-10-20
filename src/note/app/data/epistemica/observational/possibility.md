---
tags: [foundation]
---

# Possibility

> In this section, we explore the notion of possibility, its related concepts, and their implications for sophisticated epistemic formalisms.

> A state of affairs is possible when the constraints in force do not rule it out; possibility is the space of alternatives over which probability, information, and entropy are defined.

> Possibility is the most permissive of the modal notions: it says what *could* be, without saying how likely or how valuable it is. Probability weights the alternatives, information shrinks them, and entropy measures how many remain — but all three presuppose a possibility space. This note fixes that concept and separates it from the neighbouring notions it is routinely confused with: variation, uncertainty, contingency, and indeterminacy.

## Formulation

### What is this epistemic instance?

Possibility is a modal status: a state of affairs $s$ is possible relative to a set of constraints $C$ when $C$ does not exclude $s$,

$$\mathrm{Poss}_C(s) \;\Longleftrightarrow\; \neg\,\Box_C\,\neg s,$$

where $\Box_C$ is necessity under the same constraints. The constraints determine a **possibility space**

$$\Omega_C = \{\, s \;:\; C \text{ does not rule out } s \,\},$$

which is the domain over which any later probability distribution, information measure, or entropy is defined.

Possibility is always **relative** to a constraint set, and the constraint set fixes which modality is meant:

- **Logical possibility** — the constraint is non-contradiction; the widest space.
- **Nomological possibility** — the constraint is compatibility with the laws of the relevant science.
- **Epistemic possibility** — the constraint is compatibility with what an agent knows or believes; it is possibility *for* an inquirer.
- **Technical possibility** — the constraint is feasibility given available means; it is possibility *for* an intervention.

Beyond the binary reading, possibility admits **degrees**. A possibility measure $\Pi$ on $\Omega$ is maxitive rather than additive:

$$\Pi(\varnothing)=0,\qquad \Pi(\Omega)=1,\qquad \Pi(A\cup B)=\max\bigl(\Pi(A),\Pi(B)\bigr),$$

with dual necessity $N(A)=1-\Pi(\neg A)$. This is the precise sense in which possibility is weaker than probability: it records what is not excluded and how strongly, without committing to a full additive weighting.

### What epistemic element type does this epistemic instance belong to?

An **`Aggregate`** — the organized concept-system of possibility: its questions, target, contexts, representation, constructions, operations, evaluation, and infrastructure. Within that aggregate, the concept **Possibility** is an **Epistemic Construction** (a concept), and its formalizations are models and theories. The decomposition is read under the **Epistemic Order**.

### Is the type of this `epistemic element instance` unambiguous?

The primary reading is unambiguous: the note documents the concept-system of possibility as an **`Aggregate`**, with the concept itself an **Epistemic Construction**. A legitimate secondary reading is **ontic modality** — the modal status belongs to states of affairs in a segment of reality, and the concept is how that status is represented; that reading is kept as `readable as …` prose, not as a second tree. What is *not* licensed is collapsing possibility into its neighbours: probability is a measure *over* a possibility space, uncertainty is the epistemic gap *about* which possibility obtains, and variation is a pattern of differences *among realized states*. Treating any of these as synonyms is a category error, not a refinement.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: this table decomposes one epistemic instance — the concept-system of possibility — into the aspects that later formalizations attach to: orientation, target, context, representation, construction, operation, evaluation, and infrastructure.
>
> Stopping rule: a row is terminal when it names a concrete construction, operation, standard, tool, or context; the aspects are not decomposed further here.
>
> Identity: Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique.
>
> Typing: the decomposition is read under the Epistemic Order; the root type is `Aggregate`, and the concept `Possibility` is an `Epistemic Construction` within it.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Possibility | The organized concept-system of possibility: the questions, target, contexts, representation, constructions, operations, evaluation, and infrastructure that make the concept usable. |
| `Aggregate` → Possibility → `Epistemic Orientation` | Grouping: the questions and purposes that possibility answers. |
| `Aggregate` → Possibility → `Epistemic Orientation` → `Epistemic Question` | Grouping: questions directing the formalization of possibility. |
| `Aggregate` → Possibility → `Epistemic Orientation` → `Epistemic Question` → Possibility Question | The question "what is not excluded by the constraints in force?" |
| `Aggregate` → Possibility → `Epistemic Orientation` → `Epistemic Purpose` | Grouping: purposes of the formalization. |
| `Aggregate` → Possibility → `Epistemic Orientation` → `Epistemic Purpose` → Formalization Purpose | The purpose of giving possibility a calculus that later formal systems can implement. |
| `Aggregate` → Possibility → `Epistemic Target` | Grouping: what possibility ranges over. |
| `Aggregate` → Possibility → `Epistemic Target` → `Target Segment` | Grouping: the delimited domain of alternatives. |
| `Aggregate` → Possibility → `Epistemic Target` → `Target Segment` → Possibility Space | The set of alternatives the constraints leave open. |
| `Aggregate` → Possibility → `Epistemic Target` → `Observable` | Grouping: registrable features of the target. |
| `Aggregate` → Possibility → `Epistemic Target` → `Observable` → Constraint | The condition that rules an alternative in or out. |
| `Aggregate` → Possibility → `Epistemic Target` → `Observable` → Accessibility Relation | The relation selecting which alternatives are reachable from the actual state. |
| `Aggregate` → Possibility → `Epistemic Target` → `Target Element` | Grouping: constituted elements of the modal domain. |
| `Aggregate` → Possibility → `Epistemic Target` → `Target Element` → Modal Status | The status of an alternative: possible, impossible, necessary, or contingent. |
| `Aggregate` → Possibility → `Epistemic Context` | Grouping: the constraint regime that fixes which possibility is meant. |
| `Aggregate` → Possibility → `Epistemic Context` → Logical Context | Non-contradiction; the widest possibility space. |
| `Aggregate` → Possibility → `Epistemic Context` → Nomological Context | Compatibility with the laws of the relevant science. |
| `Aggregate` → Possibility → `Epistemic Context` → Epistemic Possibility Context | Compatibility with what an agent knows or believes. |
| `Aggregate` → Possibility → `Epistemic Context` → Technical Context | Feasibility given the means available to an intervention. |
| `Aggregate` → Possibility → `Epistemic Representation` | Grouping: the modal representation of alternatives. |
| `Aggregate` → Possibility → `Epistemic Representation` → `Representational System` | Grouping: the formal language of possibility. |
| `Aggregate` → Possibility → `Epistemic Representation` → `Representational System` → Modal System | The system of operators, worlds, frames, and valuations in which possibility is expressed. |
| `Aggregate` → Possibility → `Epistemic Representation` → `Representational System` → Modal System → `Representation Element` | Grouping: combinable constituents of the modal system. |
| `Aggregate` → Possibility → `Epistemic Representation` → `Representational System` → Modal System → `Representation Element` → Modal Operator | The operators □ and ◇ expressing necessity and possibility. |
| `Aggregate` → Possibility → `Epistemic Representation` → `Representational System` → Modal System → `Representation Element` → Possible World | A complete alternative state of affairs. |
| `Aggregate` → Possibility → `Epistemic Representation` → `Representational System` → Modal System → `Constitutive Substrate` | Grouping: the rules and structures constituting the modal system. |
| `Aggregate` → Possibility → `Epistemic Representation` → `Representational System` → Modal System → `Constitutive Substrate` → Possibility Frame | The set of worlds together with the accessibility relation. |
| `Aggregate` → Possibility → `Epistemic Representation` → `Representational System` → Modal System → `Constitutive Substrate` → Valuation | The assignment of propositions to worlds. |
| `Aggregate` → Possibility → `Epistemic Construction` | Grouping: the concepts, models, measures, and theories of possibility. |
| `Aggregate` → Possibility → `Epistemic Construction` → Possibility Definition | The definition: a state of affairs is possible under a constraint set when the set does not exclude it. |
| `Aggregate` → Possibility → `Epistemic Construction` → Possibility Measure | The graded model: a maxitive measure with dual necessity. |
| `Aggregate` → Possibility → `Epistemic Construction` → Possibility Theory | The formal theory of graded possibility. |
| `Aggregate` → Possibility → `Epistemic Construction` → Modal Logic Theory | The theory of the modal operators over frames. |
| `Aggregate` → Possibility → `Epistemic Operation` | Grouping: procedures that compute or explore possibility. |
| `Aggregate` → Possibility → `Epistemic Operation` → `Action` | Grouping: direct operations on the modal domain. |
| `Aggregate` → Possibility → `Epistemic Operation` → `Action` → Constraint Satisfaction | Finding assignments that satisfy the stated constraints. |
| `Aggregate` → Possibility → `Epistemic Operation` → `Action` → Reachability Analysis | Finding states reachable from the actual one under the dynamics. |
| `Aggregate` → Possibility → `Epistemic Operation` → `Action` → Scenario Enumeration | Listing coherent bundles of alternatives for planning. |
| `Aggregate` → Possibility → `Epistemic Operation` → `Action` → Feasibility Analysis | Filtering alternatives by practical and resource constraints. |
| `Aggregate` → Possibility → `Epistemic Evaluation` | Grouping: how a possibility claim is judged. |
| `Aggregate` → Possibility → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: standards judging possibility claims. |
| `Aggregate` → Possibility → `Epistemic Evaluation` → `Epistemic Standard` → Consistency Standard | The modal system must be consistent. |
| `Aggregate` → Possibility → `Epistemic Evaluation` → `Epistemic Standard` → Non-Emptiness Standard | The possibility space must contain at least one alternative. |
| `Aggregate` → Possibility → `Epistemic Evaluation` → `Epistemic Criterion` | Grouping: evaluated properties of possibility claims. |
| `Aggregate` → Possibility → `Epistemic Evaluation` → `Epistemic Criterion` → Constraint Satisfaction Criterion | The claimed alternative must satisfy the stated constraints. |
| `Aggregate` → Possibility → `Epistemic Evaluation` → `Validation` | Grouping: checks discharging doubt about a possibility claim. |
| `Aggregate` → Possibility → `Epistemic Evaluation` → `Validation` → Model Check | The claim is checked against the model. |
| `Aggregate` → Possibility → `Epistemic Infrastructure` | Grouping: tools that support possibility reasoning. |
| `Aggregate` → Possibility → `Epistemic Infrastructure` → `Epistemic Tool` | Grouping: instruments of possibility reasoning. |
| `Aggregate` → Possibility → `Epistemic Infrastructure` → `Epistemic Tool` → Constraint Solver | A solver for constraint satisfaction. |
| `Aggregate` → Possibility → `Epistemic Infrastructure` → `Epistemic Tool` → Model Checker | A tool that checks modal claims over frames. |

### What Is a critical conceptual evaluation of this `epistemic element instance`?

The concept's strength is its minimal commitment. It says only what cannot be ruled out, so it remains available before a probability model exists and survives when no such model can be justified — in scenario planning, in robust design, and in modal logic. It also makes the dependency order explicit: probability, information, and entropy are all constructions *over* a possibility space, not competitors to it.

Its limits are equally real. A purely qualitative possibility treats every non-excluded alternative alike, which is too weak for decisions that must weigh consequences. Gradation helps but is non-unique: possibility, plausibility, and probability are different calculi, and choosing one is a modelling decision, not a theorem. The constraint set is context-dependent, so "possible" without a stated constraint is incomplete. And the possible-worlds formalisation, while exact, is representation-heavy and can invite the illusion that every combinatorial alternative is a genuine possibility. The concept earns its keep only when the constraints and the purpose of the inquiry are stated alongside it.

## Which Formal Systems Formalize the Intuitive Notion of Possibility?

> Each formal system below targets one or more of the aspects named in the decomposition — the space, the constraints, the accessibility relation, the modal operators, the measure, or the operations.

> **Note:** A formalization need not address possibility directly; it may instead formalize one of its aspects, such as uncertainty, variability, or the structure of possible outcomes.

| Epistemic Element | Description | Role | Relevance to the Epistemic Element |
|---|---|---|---|
| Modal Logic | Formalizes possibility and necessity through modal operators and their logical relations. | **Logical characterization:** establishes the logical relations between possibility, necessity, and impossibility. | **Direct:** possibility is an explicit, fundamental notion formalized by the system. |
| Possible-World Semantics | Represents possibility through alternative possible worlds and an accessibility relation between them. | **Semantic interpretation:** interprets modal statements in terms of alternative worlds and their relations. | **Direct:** interprets possibility in terms of alternative worlds in which a proposition holds. |
| Set-Theoretic Possibility Space | Represents possibility as a set of alternatives not excluded by specified constraints. | **Alternative specification:** defines the alternatives under consideration, providing a domain for further formal operations. | **Direct:** explicitly represents the set of alternatives considered possible under specified conditions. |
| State Space | Represents the possible states or configurations of a system. | **State characterization:** specifies the states a system may occupy, independently of their probabilities or dynamic reachability. | **Direct:** defines the range of states represented by a system, although membership does not necessarily imply dynamic reachability. |
| Combinatorics | Formalizes the enumeration and combination of alternatives and configurations. | **Alternative enumeration:** determines the number of configurations satisfying specified structural conditions. | **Quantitative:** quantifies the number of alternatives within a specified combinatorial domain. |
| Constraint Satisfaction Problem (CSP) | Represents alternatives through variables, domains, and constraints. | **Constraint-based determination:** identifies assignments that satisfy specified constraints. | **Direct:** determines which assignments are admissible under specified constraints. |
| Satisfiability Theory | Formalizes whether a logical specification admits at least one satisfying assignment. | **Logical existence determination:** establishes whether a specification is satisfiable or unsatisfiable. | **Direct:** determines whether at least one assignment satisfies a specified logical description. |
| Possibility Theory | Formalizes graded possibility using possibility distributions and possibility measures. | **Graded possibility assessment:** represents and compares degrees of possibility without requiring an additive probability distribution. | **Direct:** explicitly formalizes possibility as a graded quantity. |
| Fuzzy Set Theory | Formalizes graded membership in sets through membership functions. | **Graded membership representation:** provides mathematical machinery for representing degrees of membership, including those used in possibility distributions. | **Indirect:** supports formalizations of graded possibility, although membership degree is not itself necessarily a measure of possibility. |
| Probability Theory | Formalizes the assignment of probabilities to events within a sample space. | **Probabilistic quantification:** quantifies event probabilities according to the axioms of probability. | **Related:** formalizes probabilistic uncertainty over alternatives. Probability and possibility are distinct concepts. |
| Imprecise Probability | Represents probabilistic uncertainty through sets or intervals of probability distributions. | **Probabilistic uncertainty representation:** accommodates incomplete probabilistic knowledge by allowing multiple admissible probability distributions. | **Indirect:** formalizes uncertainty about probability assignments rather than possibility itself. |
| Information Theory | Formalizes information associated with outcomes and probability distributions. | **Information quantification:** quantifies information content, uncertainty in probability distributions, and informational relationships between variables. | **Indirect:** formalizes aspects of uncertainty and outcome variation through information measures without directly formalizing possibility as such. |
| Counterfactual Semantics | Formalizes hypothetical alternatives by evaluating what would hold under counterfactual conditions. | **Counterfactual evaluation:** determines what would hold under hypothetical conditions that differ from the actual situation or an assumed scenario. | **Direct:** formalizes hypothetical alternatives and their consequences, including situations contrary to fact. |
| Reachability Theory | Formalizes which states a system can reach from an initial state under specified dynamics and constraints. | **Dynamical accessibility determination:** identifies states reachable from specified initial conditions. | **Direct:** distinguishes dynamically reachable states from those unreachable under the specified dynamics. |
| Feasibility Analysis | Identifies alternatives that satisfy specified practical, technical, or resource constraints. | **Practical admissibility determination:** identifies alternatives that can be implemented under specified conditions. | **Direct:** formalizes practical possibility within a defined context, distinguishing feasibility from logical or abstract possibility. |
| Scenario Analysis | Constructs and examines alternative situations under different assumptions or conditions. | **Scenario construction and exploration:** enables systematic examination of alternative situations and comparison of their potential consequences. | **Applied:** operationalizes the exploration of possible situations, particularly potential futures and their consequences. |

## QA

### Which Intuitive Notions Are Related?

The draft's term list, sorted into what belongs to possibility, what is a neighbouring concept, and what is a different kind of thing altogether.

| Term | Definition | Relation to Possibility |
|---|---|---|
| Necessity | A state of affairs holding in every accessible alternative. | Dual: $\text{Necessity}(A)=\neg\text{Possibility}(\neg A)$. |
| Contingency | A possibility that is not necessity; its negation is also possible. | A modal notion distinguishing what could be otherwise from what must be. |
| Uncertainty | The epistemic gap concerning which possibility obtains. | An epistemic state, not the modal space itself. |
| Indeterminacy | A possibility left unsettled by the description. | A feature of a description or system that leaves alternatives unresolved. |
| Variation | Differences across states or instances of a system. | An ontic pattern of differences, not possibility itself. |
| Variability | A system's disposition to vary. | A dispositional aspect of variation. |
| Diversity | Multiplicity of distinct types in a population. | A property of realized variety, not of the space of alternatives itself. |
| Rarity | Low frequency or low probability of an outcome. | A probability-related notion concerning how infrequently an outcome occurs. |
| Probability | A measure assigning weights to outcomes or events in a possibility space. | Presupposes a space of possibilities and differentiates them by likelihood. |
| Shannon Quantity | Information content or entropy associated with a probability distribution. | Quantifies information or uncertainty through the distribution of probabilities over possible outcomes. |
| Entropy | A measure of uncertainty in a probability distribution or, in certain settings, the logarithm of the number of possible states. | Quantifies the distribution or multiplicity of possibilities under a specified model. |
| Alternative | One element of a possibility space. | An individual option or possible state within the space. |
| Possible Worlds | Complete alternative states as represented in modal semantics. | A formal semantic representation of possibilities. |
| Scenario | A coherent description of a possible set of circumstances. | An applied representation of a possible situation, often used in planning and analysis. |

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- Aristotle. *Metaphysics*, Book Θ (on potentiality and actuality).
- Leibniz, G. W. (1710). *Essais de Théodicée* (possible worlds).
- Kripke, S. A. (1980). *Naming and Necessity*.
- Kolmogorov, A. N. (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung*.
- Zadeh, L. A. (1978). Fuzzy sets as a basis for a theory of possibility. *Fuzzy Sets and Systems*, 1, 3–28.
- Dubois, D. & Prade, H. (1988). *Possibility Theory: An Approach to Computerized Processing of Uncertainty*.
- [Probability](note.html?n=epistemica/observational/probability.md) — a probability space is a possibility space equipped with an additive measure; possibility is logically prior.
- [Theory of Probability](note.html?n=epistemica/observational/theory-of-probability.md) and [Imprecise Probability](note.html?n=epistemica/observational/imprecise-probability.md) — the measure-theoretic and interval-valued treatments of the weighting layer.
- [Information](note.html?n=epistemica/observational/information.md) and [Shannon Information Theory](note.html?n=epistemica/observational/shannon-information-theory.md) — information is the reduction of a possibility space.
- [Shannon Information Content](note.html?n=epistemica/observational/it/shannon-information-content.md) and the [Information Theory Atlas](data/epistemica/observational/it/atlas.html) — the single-outcome atom and the operational quantities built on it.
- [Entropy](note.html?n=epistemica/observational/entropy.md) — the expected uncertainty of the space, and its many realisations.
- [Random Variable](note.html?n=epistemica/observational/random-variable.md) and [Variance](note.html?n=epistemica/observational/variance.md) — the quantitative treatment of variation once a measure is fixed.
- [Extreme Event](note.html?n=epistemica/complexity-science/extreme-event.md) and [Rare Events Modelling](note.html?n=epistemica/observational/rare-events-modelling.md) — applied possibility at the tails of a distribution.
- [Aleatorio](https://etimologias.dechile.net/?aleatorio)
