---
tags: [decision-making]
---

# Decision Theory

> Decision theory is the study of choice among alternatives under uncertainty: given a set of options, a set of possible states, the consequences of each option in each state, and the agent's beliefs and preferences, it asks which option should be chosen — or explains which one is.

It has three readings that are often run together. **Normative** decision theory says how a rational agent ought to choose; **descriptive** decision theory says how agents actually choose; **prescriptive** decision theory says how to improve choice in practice. This note is the field-level entry: it fixes the vocabulary, decomposes the field into its branches, and links the corpus notes that develop each branch.

## Formulation

### What is this epistemic instance?

Decision theory is the organized theory of choice under uncertainty. Its canonical elements are the decision problem's alternatives, the states of the world, the outcome of each alternative in each state, the agent's belief over states, the agent's preference over outcomes, and the decision rule that maps beliefs and preferences to an action.

Following [Decision Making](note.html?n=epistemica/decision-making.md), a decision problem can be written as

$$\mathcal{D} = (\mathcal{S}, \mathcal{A}, T, \mathcal{M}, \phi),$$

where $\mathcal{S}$ is the state space, $\mathcal{A}$ the action space, $T$ the transition structure, $\mathcal{M}$ the evaluation metric set, and $\phi$ the decision rule. The special case of a single choice is the [Decision Problem](note.html?n=epistemica/observational/decision-problem.md); the sequential case adds dynamics and becomes a Markov decision process or an optimal-control problem.

The field's centre of gravity is the pair (belief, preference): a probability distribution over states and a utility over outcomes. Expected utility combines them; Bayesian decision theory updates the belief before combining; prospect theory replaces the utility with a reference-dependent value function; bounded rationality replaces maximization with satisficing. Each is a different answer to the same structure.

### What epistemic element type does this epistemic instance belong to?

An **`Aggregate`** — the organized field of decision theory: its questions, target, representation, constructions, operations, evaluation, and infrastructure. Within that aggregate, the core theory (expected utility) is an **Epistemic Construction** (a theory), and the individual methods are constructions and operations. The decomposition is read under the **Epistemic Order**.

### Is the type of this `epistemic element instance` ambiguous?

The primary reading is unambiguous: the note documents the organized field, an `Aggregate`, with the core theory an `Epistemic Construction`. A secondary reading splits the field by stance — normative, descriptive, or prescriptive — and that split is kept as prose, not as three separate trees. What is *not* licensed is collapsing decision theory into its neighbouring fields: optimization studies the search for a best element under a fixed objective, game theory studies choice when outcomes depend on other agents' choices, and control theory studies the regulation of a dynamical system over time. Each is a neighbour with its own grammar, not a synonym.

### What is the recursive instance decomposition of this epistemic instance?

> Boundary: this table decomposes one epistemic instance — the organized field of decision theory — into the aspects that its theories and methods attach to: orientation, target, representation, construction, operation, evaluation, and infrastructure.
>
> Stopping rule: a row is terminal when it names a concrete theory, method, standard, tool, or constituent of the decision problem; the aspects are not decomposed further here.
>
> Identity: Instance Tree Path holds instances only — never epistemic element types; every path in this table is unique.
>
> Typing: the decomposition is read under the Epistemic Order; the root type is `Aggregate`, and the core theory is an `Epistemic Construction` within it.

| Instance Tree Path | Description |
| --- | --- |
| `Aggregate` → Decision Theory | The organized field of choice under uncertainty: its questions, decision problem, representation, theories, methods, evaluation, and tools. |
| `Aggregate` → Decision Theory → `Epistemic Orientation` | Grouping: the questions and purposes that decision theory answers. |
| `Aggregate` → Decision Theory → `Epistemic Orientation` → `Epistemic Question` | Grouping: questions directing the theory of choice. |
| `Aggregate` → Decision Theory → `Epistemic Orientation` → `Epistemic Question` → Normative Question | What ought a rational agent choose, given its beliefs and preferences? |
| `Aggregate` → Decision Theory → `Epistemic Orientation` → `Epistemic Question` → Descriptive Question | What do agents actually choose, and how do they deviate from the normative answer? |
| `Aggregate` → Decision Theory → `Epistemic Orientation` → `Epistemic Question` → Prescriptive Question | How can a decision process be structured to improve its outcome? |
| `Aggregate` → Decision Theory → `Epistemic Orientation` → `Epistemic Purpose` | Grouping: purposes of the field. |
| `Aggregate` → Decision Theory → `Epistemic Orientation` → `Epistemic Purpose` → Rational Choice Purpose | To render choice coherent, comparable, and defensible under uncertainty. |
| `Aggregate` → Decision Theory → `Epistemic Target` | Grouping: what decision theory ranges over. |
| `Aggregate` → Decision Theory → `Epistemic Target` → `Target Segment` | Grouping: the delimited decision situation. |
| `Aggregate` → Decision Theory → `Epistemic Target` → `Target Segment` → Decision Problem | The bounded task of selecting an action under states, outcomes, and constraints. |
| `Aggregate` → Decision Theory → `Epistemic Target` → `Observable` | Grouping: registrable features of the decision problem. |
| `Aggregate` → Decision Theory → `Epistemic Target` → `Observable` → Alternative Set | The options available to the decision-maker. |
| `Aggregate` → Decision Theory → `Epistemic Target` → `Observable` → State Set | The states of the world on which outcomes depend. |
| `Aggregate` → Decision Theory → `Epistemic Target` → `Observable` → Outcome Set | The consequences of each action in each state. |
| `Aggregate` → Decision Theory → `Epistemic Target` → `Target Element` | Grouping: constituted elements of the decision problem. |
| `Aggregate` → Decision Theory → `Epistemic Target` → `Target Element` → Decision Rule | The mapping from beliefs and preferences to a selected action. |
| `Aggregate` → Decision Theory → `Epistemic Representation` | Grouping: how beliefs, preferences, and the decision problem are represented. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` | Grouping: the formal systems of decision theory. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Preference System | The representation of value over outcomes. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Preference System → `Representation Element` | Grouping: combinable constituents of the preference representation. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Preference System → `Representation Element` → Utility Function | The map from outcomes to a scalar value. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Preference System → `Constitutive Substrate` | Grouping: the structure constituting the preference representation. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Preference System → `Constitutive Substrate` → Preference Ordering | The comparative relation over outcomes that the utility represents. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Belief System | The representation of uncertainty over states. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Belief System → `Representation Element` | Grouping: combinable constituents of the belief representation. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Belief System → `Representation Element` → Probability Distribution | The assignment of probabilities to states or outcomes. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Belief System → `Constitutive Substrate` | Grouping: the structure constituting the belief representation. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Belief System → `Constitutive Substrate` → Prior | The initial belief from which updating proceeds. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Decision Model | The representation of the decision problem as a structured object. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Decision Model → `Representation Element` | Grouping: combinable constituents of the decision model. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Decision Model → `Representation Element` → Decision-Analysis Tree | The sequential decision and chance nodes unfolded as a tree. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Decision Model → `Constitutive Substrate` | Grouping: the structure constituting the decision model. |
| `Aggregate` → Decision Theory → `Epistemic Representation` → `Representational System` → Decision Model → `Constitutive Substrate` → Transition Model | The dynamics mapping states and actions to next states. |
| `Aggregate` → Decision Theory → `Epistemic Construction` | Grouping: the theories and models of decision theory. |
| `Aggregate` → Decision Theory → `Epistemic Construction` → Expected Utility Theory | The normative theory: choose the action maximizing probability-weighted utility. |
| `Aggregate` → Decision Theory → `Epistemic Construction` → Bayesian Decision Theory | Expected utility with beliefs updated by Bayes' rule. |
| `Aggregate` → Decision Theory → `Epistemic Construction` → Prospect Theory | The descriptive theory: reference-dependent value with loss aversion and probability distortion. |
| `Aggregate` → Decision Theory → `Epistemic Construction` → Bounded Rationality Model | The descriptive model: satisficing under cognitive, informational, and temporal limits. |
| `Aggregate` → Decision Theory → `Epistemic Construction` → Game Theory | The strategic theory: choice when outcomes depend on other agents' choices. |
| `Aggregate` → Decision Theory → `Epistemic Construction` → Markov Decision Process | The sequential theory: states, actions, transitions, and rewards over time. |
| `Aggregate` → Decision Theory → `Epistemic Operation` | Grouping: procedures that structure or solve a decision. |
| `Aggregate` → Decision Theory → `Epistemic Operation` → `Action` | Grouping: direct operations on a decision problem. |
| `Aggregate` → Decision Theory → `Epistemic Operation` → `Action` → Decision Analysis | Structuring alternatives, probabilities, consequences, and values into a comparable form. |
| `Aggregate` → Decision Theory → `Epistemic Operation` → `Action` → Multi-Criteria Decision Analysis | Evaluating alternatives against several conflicting criteria. |
| `Aggregate` → Decision Theory → `Epistemic Operation` → `Action` → Robust Decision-Making | Selecting strategies that perform acceptably across a wide range of plausible futures. |
| `Aggregate` → Decision Theory → `Epistemic Operation` → `Action` → Scenario Planning | Constructing coherent alternative futures and evaluating choices across them. |
| `Aggregate` → Decision Theory → `Epistemic Operation` → `Action` → Dynamic Programming | Solving sequential decisions by decomposing them into overlapping subproblems. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` | Grouping: how a decision or a decision procedure is judged. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` → `Epistemic Standard` | Grouping: standards judging decisions. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` → `Epistemic Standard` → Rationality Standard | The decision coheres with the agent's beliefs and preferences. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` → `Epistemic Standard` → Coherence Standard | The belief and preference relations are internally consistent. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` → `Epistemic Criterion` | Grouping: evaluated properties of a decision. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` → `Epistemic Criterion` → Regret Criterion | The decision minimizes the worst-case shortfall against the best alternative. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` → `Epistemic Criterion` → Robustness Criterion | The decision remains acceptable under a range of models or futures. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` → `Validation` | Grouping: checks discharging doubt about a decision. |
| `Aggregate` → Decision Theory → `Epistemic Evaluation` → `Validation` → Outcome Validation | Comparing the realized outcome with the decision's predicted consequences. |
| `Aggregate` → Decision Theory → `Epistemic Infrastructure` | Grouping: tools that support decision-making. |
| `Aggregate` → Decision Theory → `Epistemic Infrastructure` → `Epistemic Tool` | Grouping: instruments of decision support. |
| `Aggregate` → Decision Theory → `Epistemic Infrastructure` → `Epistemic Tool` → Decision Support System | A system that structures inputs and ranks alternatives for a decision-maker. |
| `Aggregate` → Decision Theory → `Epistemic Infrastructure` → `Epistemic Tool` → Optimization Solver | A solver that returns an optimal or near-optimal action under a stated objective. |
| `Aggregate` → Decision Theory → `Epistemic Infrastructure` → `Epistemic Tool` → Simulation Engine | A tool that samples outcomes or futures to estimate consequences. |

### What Is a critical conceptual evaluation of this `epistemic element instance`?

The field's strength is unification: one structure — alternatives, states, outcomes, beliefs, preferences, a decision rule — covers betting, portfolio choice, medical triage, policy under uncertainty, and sequential control. Expected utility gives a sharp normative baseline; Bayesian decision theory adds belief updating; MDPs extend the same structure over time. Methods such as MCDA, RDM, and scenario planning make the structure usable when a single utility is unavailable or contested.

Its limits are equally sharp. Expected utility assumes stable, complete preferences and a well-specified probability model; bounded rationality and prospect theory show that actual agents violate both. The normative-descriptive gap is not a defect to be patched but a standing research problem. Model misspecification propagates into every downstream recommendation, and the choice of decision rule (maximin, minimax regret, expected utility) can reverse the ranking of alternatives. The field earns its keep only when the decision rule, the belief model, and the preference model are stated alongside the recommendation.

## Entry Map

Each branch of the decomposition is developed in the corpus by the notes below.

| Branch | Note | What it covers |
| --- | --- | --- |
| Decision making | [Decision Making](note.html?n=epistemica/decision-making.md) | The cognitive process, glossary, pathologies, and practical frameworks. |
| Decision problem | [Decision Problem](note.html?n=epistemica/observational/decision-problem.md) | The formal $(S, E)$ structure: solution space and evaluation model. |
| Expected value | [Expected Value](note.html?n=epistemica/observational/expected-value.md) | The probability-weighted average underlying expected utility. |
| Trade-offs | [Trade-Off](note.html?n=epistemica/optimization/trade-off.md) | Competing criteria and the compromises between them. |
| Uncertainty | [Probability](note.html?n=epistemica/observational/probability.md), [Possibility](note.html?n=epistemica/observational/possibility.md) | The belief-side foundations: graded uncertainty and the space of alternatives. |
| Belief updating | [Bayes' Theorem](note.html?n=epistemica/observational/bayes-theorem.md), [Bayes Estimator](note.html?n=epistemica/observational/bayes-estimator.md) | How evidence revises the belief that feeds a decision. |
| Coherence | [Dutch Book](note.html?n=epistemica/observational/dutch-book.md), [Betting](note.html?n=epistemica/observational/betting.md) | Coherent probability as the avoidance of sure loss. |
| Bet sizing | [Kelly Criterion](note.html?n=epistemica/observational/kelly-criterion.md) | Growth-optimal sizing of a repeated bet. |
| Multi-criteria | [Multiple-Criteria Decision-Making (MCDM)](note.html?n=epistemica/optimization/multiple-criteria-decision-making-mcdm.md) | Ranking alternatives against several conflicting criteria. |
| Robustness | [Robust Decision-Making (RDM)](note.html?n=epistemica/optimization/robust-decision-making-rdm.md) | Strategies that perform acceptably across plausible futures. |
| Sequential decisions | [Markov Decision Processes (MDP)](note.html?n=epistemica/dynamical-intelligence/markov-decision-processes-mdp.md) | States, actions, transitions, and rewards over time. |
| Control | [Control Theory](note.html?n=epistemica/dynamical-intelligence/control-theory.md), [Optimal Control Theory](note.html?n=epistemica/dynamical-intelligence/optimal-control-theory.md), [Model Predictive Control (MPC)](note.html?n=epistemica/dynamical-intelligence/model-predictive-control-mpc.md) | Regulating a dynamical system, with and without an explicit objective. |
| Computational decisions | [Combinatorial Optimization](note.html?n=epistemica/optimization/combinatorial-optimization.md), [Dynamic Programming](note.html?n=epistemica/optimization/dynamic-programming.md), [Knapsack Problem](note.html?n=epistemica/optimization/knapsack-problem.md) | Decision problems in the computer-science sense. |
| Decision trees | [Decision Tree](note.html?n=technica/ais/learning-method/decision-tree.md) | The trainable ML model — distinct from the decision-analysis tree. |
| Information value | [Shannon Information Content](note.html?n=epistemica/observational/it/shannon-information-content.md) | The surprisal that information reduces; the atom of value-of-information reasoning. |

## QA

### What Is the Value Added by Decision Theory When Solution Generation, Discovery, and Development Are Often the Most Relevant Aspects?

> It is worth noting that, in many cases, solution development, discovery, and related activities are the most relevant aspects of decision-making. If we understand decision-making within the broader process of problem-solving, decisions are made to solve problems or achieve underlying objectives. From this perspective, defining the set of choices and selecting the most appropriate option may not be the most significant part of the process. The real challenge may lie in discovering, generating, and developing the possible solutions in the first place.

> This seems to reflect an important limitation of decision theory: it is an abstract framework for organizing and analyzing choice activities, but it does not guarantee solutions to the underlying problems. Moreover, decision-making is not a self-contained, general activity that can be performed independently of its context. It is always a situated, concrete activity embedded in a particular problem domain, with its own characteristics, constraints, and requirements. That is, there is no **universally effective decision-maker** who can be transferred from one context to another and remain equally effective.

## References

- [Philosophia Artium Epistemicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-epistemicarum-et-operis.md)
- [Decision Making](note.html?n=epistemica/decision-making.md)
- [Decision Problem](note.html?n=epistemica/observational/decision-problem.md)
- von Neumann, J. & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*.
- Savage, L. J. (1954). *The Foundations of Statistics*.
- Simon, H. A. (1955). A Behavioral Model of Rational Choice. *Quarterly Journal of Economics*.
- Bellman, R. (1957). *Dynamic Programming*.
- Luce, R. D. & Raiffa, H. (1957). *Games and Decisions: Introduction and Critical Survey*. Wiley. [Internet Archive](https://ia802909.us.archive.org/6/items/in.ernet.dli.2015.132625/2015.132625.Games-And-Decisions-Introduction-And-Critical-Survey.pdf)
- Keeney, R. L. & Raiffa, H. (1976). *Decisions with Multiple Objectives*.
- Kahneman, D. & Tversky, A. (1979). Prospect Theory. *Econometrica*.
- Puterman, M. L. (1994). *Markov Decision Processes*.
- [Decision Theory](https://bactra.org/notebooks/decision-theory.html)
