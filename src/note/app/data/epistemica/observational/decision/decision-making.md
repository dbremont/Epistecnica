# Decision Making

> In this note, we will analyze the **cognitive-psychological process** of — **decision making** and its **related ontic elements**, along with frameworks to improve the outcomes of such a process.
> 

> **Decision-making** is the cognitive process of selecting a course of action from multiple alternatives to achieve a goal, often involving the evaluation of risks, benefits, and uncertainties.
> 

> **Note:** Decision-making is an almost daily task for agents. This note should be viewed in tandem with related work on  [Problem](https://app.notion.com/p/Problem-1e8c0f5171ec80e59848c3449661c09f?pvs=21) and [Agency](https://app.notion.com/p/Agency-eebe9b5a15d84a3db7a1a1273fc29a2c?pvs=21).
> 

> See [Decision Theory](note.html?n=epistemica/observational/decision/theory.md) for the field-level entry: branches, methods, and links.

## Glossary

| Term | Definition |
| --- | --- |
| **Action Space** | The set of feasible and distinguishable actions available to a decision-maker at the time of choice. |
| **Agent–Environment Coupling** | The dynamic interface through which an agent’s actions transform the environment and environmental feedback updates the agent’s cognitive state. |
| **Bayesian Decision Theory** | A normative framework in which decisions are made by updating beliefs via Bayes’ rule and selecting actions that maximize expected utility with respect to posterior beliefs. |
| **Bounded Rationality** | A descriptive model of decision-making under cognitive, informational, and temporal limitations, where agents satisfice (seek “good enough” solutions) rather than optimize. |
| **Commitment** | A post-choice property representing the persistence of a selected action as an intention or control constraint, binding the agent to a trajectory. |
| **Decision Event** | A point-like occurrence marking the collapse of competing alternatives into a single committed trajectory; the moment of selection. |
| **Decision Pathology** | A recurrent distortion, limitation, or breakdown in the processes of framing, evaluating, selecting, committing to, or revising a decision, resulting in degraded decision quality or misalignment between action and objective. |
| **Decision Problem** | A formalized task requiring selection of an action under uncertainty, defined by a tuple of world states, actions, transition dynamics, evaluation metrics, and a decision rule. |
| **Decision Rule** | The selection mechanism that maps beliefs, evaluations, and constraints onto an action (e.g., argmax expected utility, satisficing threshold, heuristic policy). |
| **Decision-Making** | The cognitive process (or task) of selecting a course of action from multiple alternatives to achieve a goal, involving evaluation of risks, benefits, and uncertainties. When viewed ontologically, it is a stratified processual system encompassing process, mapping, capacity, and event. |
| **Deliberation** | An iterative integrative process that coordinates inference, valuation, and simulation to compare alternatives and resolve uncertainty into a provisional judgment. |
| **Dual Process Theory** | A framework proposing that decision-making emerges from the interaction between intuitive/automatic (System 1) and reflective/deliberative (System 2) cognitive processes. |
| **Expected Utility Theory** | A normative theory in which a rational agent chooses the option that maximizes the sum of utilities weighted by their probabilities (expected utility). |
| **Heuristic** | A rule-of-thumb decision strategy that reduces cognitive cost, often fast and practical but potentially prone to systematic bias. |
| **Loss Aversion** | A cognitive bias where potential losses are weighted more heavily than equivalent gains; a core component of Prospect Theory. |
| **Markov Decision Process (MDP)** | A mathematical framework for sequential decision-making under stochastic transitions, defined by states, actions, transition probabilities, and reward functions. |
| **Model Misspecification** | An informational pathology in which the internal representation of a decision problem is structurally incorrect relative to the true environment. |
| **Multi-Criteria Decision Analysis (MCDA)** | A family of methods that evaluate alternatives against multiple criteria, typically by assigning weights and scores to produce a ranked order. |
| **Naturalistic Decision Making** | A research framework studying how experts make decisions in uncertain, time-constrained, real-world environments, often using recognition-primed judgment. |
| **Ontic** | Pertaining to the actual, real-world entities, structures, and relations that exist independently of a particular theory or model. In this note, “ontic elements” refer to the components of decision-making as they exist in cognitive and environmental reality. |
| **Option Generation** | The process by which possible alternatives emerge, are imagined, discovered, or proposed as candidate actions. |
| **Preference Ordering** | A comparative relation over alternatives (e.g., A ≻ B, indifference) that reflects the decision-maker’s values or utility structure. |
| **Prospect Theory** | A descriptive theory of decision under risk where outcomes are evaluated relative to a reference point, with asymmetric weighting of gains and losses (loss aversion) and probability distortion. |
| **Rationality** | A property of a decision or decision-maker indicating degree of internal coherence and norm-conformity (e.g., consistency with expected utility maximization or logical constraints). |
| **Reversibility** | A property representing the cost or difficulty of undoing or revising a decision after commitment. |
| **Satisficing** | A decision strategy in which an agent selects the first option that meets an acceptability threshold, rather than searching for the optimal option. |
| **Simulation / Prediction Process** | A cognitive process that generates possible future or hypothetical outcomes from candidate actions, enabling counterfactual reasoning and anticipation. |
| **Task (decision-making)** | A structured requirement to reduce uncertainty over a set of alternatives by coordinating multiple cognitive processes (perception, inference, valuation, prediction) into a single committed selection under constraints. |
| **Trade-off Relation** | A structural constraint in which improving one valued dimension (e.g., speed) necessarily worsens another (e.g., accuracy). |
| **Trigger Event** | A point-like occurrence that initiates decision dynamics, such as a deadline, external question, surprise, or internal demand for action. |
| **Uncertainty** | A property of the epistemic state representing the degree of unknown or probabilistic indeterminacy in beliefs about the world, outcomes, or causal structure. |

## Formulation

> How to ground a  technical  on **decision making**?
> 

### What type of element is **decision making**?

> Decision making is ontologically best characterized as a **stratified processual system** rather than a single type of entity: at the base level it is a temporally extended **process** that transforms informational and motivational states into action-selection outcomes under constraints; at the functional level it is a **mapping mechanism** that implements a policy from epistemic and value states to actions; at the dispositional level it is a **capacity of an agentive system** to resolve uncertainty into commitments; and at the phenomenological or event level it is manifested as a discrete **selection event** marking the collapse of alternative action branches into a committed trajectory.
> 

> Decision making is a **composite cognitive task** that enacts and coordinates multiple cognitive processes—such as perception, inference, valuation, and simulation—in order to transform an uncertain epistemic state and a set of preferences into a committed action under constraints.  It’s not a process itself - by a type of task.
> 

> A decision-making task is characterized by a **structured requirement to reduce uncertainty over a set of alternatives by coordinating multiple cognitive processes (perception, inference, valuation, and prediction) into a single committed selection under constraints**, where the output is not merely a computed result but an **action-binding commitment that resolves a space of possible trajectories into one executable course of action.**
> 

### What is the grammar (or map) useful for parsing the elements related to decision-making?

> See more in [Ontology Template](https://app.notion.com/p/Ontology-Template-2f7c0f5171ec80eea496cb2437779712?pvs=21).
> 

> Note: Some of this elements are non ontic -like a task - which is a synontic element - the section shuold probably be called
> 

| Type | Element | Description |
| --- | --- | --- |
| **Structure (normative-relational)** | Task | Constraint-goal specification over an agent–environment system defining success criteria and admissible actions. |
| **System (Agentive Substrate)** | Cognitive Agent | Persistent system (biological, artificial, institutional) that hosts and coordinates cognition and decision processes. |
| **State (epistemic)** | Belief State | Structured representation of uncertainty about the world, outcomes, and causal structure. |
| **State (evaluative)** | Preference (Utility State) | Representation of value ordering over outcomes, trajectories, or states of affairs. |
| **State (environmental)** | World State (Outcome Space) | The external configuration of the environment, including all possible states affected by actions. |
| **State (situational phase)** | Initial State | Pre-decision condition: problem recognition and activation of need for action. |
| **State (situational phase)** | Deliberative State | Active comparison, simulation, and evaluation of alternatives under uncertainty. |
| **State (situational phase)** | Terminal State | Post-decision condition where commitment is made and action trajectory is fixed. |
| **Process (perceptual)** | Perception Process | Acquisition and transformation of environmental signals into internal representations. |
| **Process (cognitive-inferential)** | Inference Process | Updating of belief state via probabilistic, logical, or heuristic transformations. |
| **Process (cognitive-evaluative)** | Valuation Process | Assignment or updating of utility, preference weights, or normative rankings. |
| **Process (counterfactual)** | Simulation / Prediction Process | Generation of possible future or hypothetical outcomes from candidate actions. |
| **Process (integrative reasoning)** | Deliberation | Iterative coordination of inference, valuation, and simulation to compare alternatives. |
| **Process (selection mechanism)** | Action-Selection Process | Mapping of integrated epistemic + evaluative state to a candidate action set. |
| **Process (commitment execution)** | Implementation | Translation of selected option into real-world action. |
| **Process (system coordination)** | Decision-Making Architecture | Higher-order control structure coordinating all subprocesses into a unified decision regime. |
| **Event (initiating)** | Trigger Event | Point-like occurrence initiating decision dynamics (deadline, question, surprise, demand). |
| **Event (selection)** | Decision Event | Collapse of competing alternatives into a single committed trajectory. |
| **Event (execution)** | Action Event | Observable execution of chosen behavior in the environment. |
| **Event (communication)** | Declaration Event | External articulation or signaling of the chosen option. |
| **Process/Event (sub-event)** | Selection Event (Neural/Computational) | Internal threshold-crossing event where one option becomes dominant. |
| **Entity (option space)** | Options / Alternatives | Candidate courses of action available to the agent (mentally represented or externally given). |
| **Entity (normative axis)** | Criteria / Values | Standards used to evaluate alternatives (cost, ethics, utility, safety, etc.). |
| **Relation (comparative)** | Preference Ordering | Ordering relation over alternatives (A ≻ B, indifference, etc.). |
| **Relation (causal)** | Causal Link | Mapping from action → outcome in the environment. |
| **Relation (teleological)** | Means–End Relation | Structural relation where an action is a method for achieving a goal. |
| **Relation (trade structure)** | Trade-off Relation | Constraint where increasing one valued dimension decreases another. |
| **Relation (system coupling)** | Agent–Environment Coupling | Dynamic interface through which actions transform environment and feedback updates cognition. |
| **Disposition (agent property)** | Decisiveness | Tendency to commit quickly and robustly to an option. |
| **Disposition (agent property)** | Risk Aversion | Preference bias toward lower-uncertainty outcomes. |
| **Disposition (agent property)** | Computational Capacity | Cognitive/physical resource bounds for processing, simulation, and inference. |
| **Property (normative)** | Rationality | Degree of internal coherence and norm-conformity (e.g., expected utility consistency). |
| **Property (epistemic)** | Uncertainty | Degree of unknown or probabilistic indeterminacy in belief state. |
| **Property (structural tension)** | Conflict | Incompatibility among values, goals, or options. |
| **Property (post-choice state)** | Commitment | Persistence of selected action as intention or control constraint. |
| **Property (control cost)** | Reversibility | Cost/difficulty of undoing or revising a decision. |
| **Intentional Object** | Representation of Non-Actual | Mental representation of counterfactuals, future outcomes, or imagined alternatives with causal efficacy in deliberation. |

## **Description**

> ***How does** it work? **How to even describe** the decision type of task? Which are the mechanisms? What **pathologies or failure** modes arise? Which **explanatory frameworks or theories** account for it?*
> 

### Ontic Map

> See more in [What is the grammar (or map) useful for parsing the elements related to decision-making?](decision-making.md).
> 

### *What **pathologies or failure** modes arise?*

> A **decision pathology** is a recurrent distortion, limitation, or breakdown in the processes of framing, evaluating, selecting, committing to, or revising a decision, resulting in degraded decision quality or misalignment between action and objective.
> 

| **Category** | **Pathology** | **Description** |
| --- | --- | --- |
| **Cognitive** | Bounded Rationality | Decision-maker cannot fully evaluate all options because cognition, time, or information-processing capacity is limited. |
| **Cognitive** | Overconfidence | Confidence in judgment exceeds actual predictive or evaluative accuracy. |
| **Cognitive** | Confirmation Bias | Evidence supporting prior beliefs is privileged while disconfirming evidence is discounted. |
| **Cognitive** | Anchoring | Initial information disproportionately influences subsequent judgment. |
| **Cognitive** | Availability Bias | Easily recalled examples dominate reasoning regardless of true relevance or frequency. |
| **Cognitive** | Loss Aversion | Potential losses are weighted more heavily than equivalent gains. |
| **Cognitive** | Sunk-Cost Continuation | Prior investment causes continued commitment to an unfavorable option. |
| **Cognitive** | Motivated Reasoning | Reasoning becomes shaped by desired conclusions rather than evidence. |
| **Cognitive** | Indecision / Paralysis | Inability to select among alternatives due to uncertainty, fear, or overload. |
| **Cognitive** | Impulsive Choice | Premature decision made without sufficient analysis or evaluation. |
| **Informational** | Incomplete Information | Decision occurs without access to necessary relevant information. |
| **Informational** | Noisy Information | Signal is obscured by irrelevant, conflicting, or low-quality inputs. |
| **Informational** | Misinformation | Decision is shaped by false or inaccurate information. |
| **Informational** | Outdated Models | Mental or formal models no longer reflect current conditions. |
| **Informational** | Poor Signal Extraction | Failure to identify what information is actually relevant to the decision. |
| **Informational** | Hidden Variables | Important causal factors remain unseen or unaccounted for. |
| **Informational** | Model Misspecification | The internal representation of the problem is structurally incorrect. |
| **Informational** | Inability to Estimate Consequences | Failure to forecast likely outcomes or downstream effects. |
| **Structural · Procedural** | Badly Framed Decision Problem | The decision is incorrectly formulated from the outset. |
| **Structural · Procedural** | False Alternatives | The option space is artificially narrowed or incorrectly represented. |
| **Structural · Procedural** | Criteria Mismatch | Evaluation criteria do not align with the real objective. |
| **Structural · Procedural** | Premature Closure | Decision process terminates before sufficient exploration or analysis. |
| **Structural · Procedural** | Wrong-Objective Optimization | Optimization occurs against a proxy or incorrect target rather than the actual goal. |
| **Structural · Procedural** | Poor Scenario Exploration | Insufficient exploration of possible outcomes or futures. |
| **Structural · Procedural** | Weak Feedback Loops | Decision outcomes are not adequately monitored for correction or learning. |
| **Structural · Procedural** | Failure to Revisit Assumptions | Initial assumptions remain unchallenged despite new evidence. |
| **Organizational · Social** | Groupthink | Desire for consensus suppresses critique, dissent, or alternative views. |
| **Organizational · Social** | Incentive Misalignment | Participants are rewarded according to objectives different from the intended decision goal. |
| **Organizational · Social** | Political Distortion | Decision quality is altered by power struggles or internal politics. |
| **Organizational · Social** | Diffusion of Responsibility | Accountability becomes diluted across multiple actors. |
| **Organizational · Social** | Authority Capture | Hierarchical influence overrides evidence-based evaluation. |
| **Organizational · Social** | Coordination Failure | Multiple actors fail to synchronize decisions or action effectively. |
| **Organizational · Social** | Information Silos | Relevant information remains fragmented across groups and does not circulate. |
| **Temporal** | Acting Too Early | Decision is made before enough information or analysis exists. |
| **Temporal** | Acting Too Late | Delay reduces available options or worsens outcomes. |
| **Temporal** | Excessive Delay | Decision stalls beyond a useful operational timescale. |
| **Temporal** | Inability to Commit | Selection occurs but cannot be translated into stable action. |
| **Temporal** | Inability to Adapt After Commitment | Decision remains fixed despite changing evidence or context. |
| **Temporal** | Path Dependence Lock-In | Previous choices constrain future options excessively, reducing adaptability. |

### **What phenomenology—that is, which dynamics and related elements—must a theory account for? What are we even explaining?**

> A theory of **decision-making** must explain **decision as a real unfolding process**—not merely the final act of choosing.
> 

> The **explanandum** is therefore broader than *choice*. It includes the cognitive, temporal, informational, and social dynamics through which a possible action becomes perceived, evaluated, selected, enacted, and later revised.
> 

> A **theory of decision-making** must explain how agents move from perceived situation → possible alternatives → evaluation → commitment → action → consequence → adaptation.
> 

| **Phenomenon** | **Description** |
| --- | --- |
| **Problem Recognition** | How a situation becomes perceived as requiring a decision at all—why a condition is interpreted as a problem, opportunity, threat, or decision point. |
| **Decision Framing** | How the decision is defined: its boundaries, scope, stakes, assumptions, and what counts as the relevant question. |
| **Option Generation** | How possible alternatives emerge, are imagined, discovered, or proposed. |
| **Preference Formation** | How desires, priorities, goals, and value hierarchies are formed, weighted, and stabilized. |
| **Criteria Formation** | How evaluation criteria are selected and how “better,” “worse,” success, or failure become operationally defined. |
| **Information Acquisition** | How evidence is gathered, filtered, interpreted, and incorporated into the decision process. |
| **Uncertainty Representation** | How uncertainty, ambiguity, probability, and incomplete knowledge are modeled or perceived. |
| **Evaluation of Alternatives** | How options are assessed against goals, criteria, expected outcomes, and constraints. |
| **Trade-off Navigation** | How competing objectives are balanced against one another, such as speed vs quality or cost vs performance. |
| **Prediction  · Anticipation** | How future consequences are forecasted, simulated, imagined, or estimated before action. |
| **Judgment Formation** | How a provisional judgment emerges regarding which option appears preferable. |
| **Selection · Choice** | How one alternative becomes selected over competing possibilities. |
| **Commitment Formation** | How evaluation turns into commitment—how a tentative preference becomes a decided course of action. |
| **Decision Execution** | How a decision is translated into actual behavior, implementation, or intervention in the world. |
| **Feedback Perception** | How outcomes are observed, interpreted, and made available for reflection after action. |
| **Learning · Updating** | How beliefs, models, strategies, or future decisions are updated based on outcomes. |
| **Revision · Reversal** | How decisions are reconsidered, modified, abandoned, or reversed after commitment. |
| **Temporal Dynamics** | How decision unfolds over time, including urgency, hesitation, iteration, deadlines, momentum, and closure. |
| **Emotional Dynamics** | How emotions—fear, anxiety, desire, confidence, regret, anticipation, stress—shape decision behavior. |
| **Social Dynamics** | How interaction with others influences decision through persuasion, conflict, negotiation, cooperation, authority, or incentives. |
| **Collective Decision Formation** | How decisions emerge when multiple actors participate rather than a single individual. |
| **Error Production** | How poor decisions arise, including the generation of distortions, mistakes, or failures. |
| **Post-decision Rationalization** | How decisions are later justified, narrated, defended, or reinterpreted after they are made. |

### Can a theory explain all of the related ontology, dynamics, and phenomena involved in decision-making? It almost seems to require a model of the decider, the environment, and the surrounding social interactions. Is something this broad even tractable?

> A single theory probably cannot *fully* explain all of decision-making if by “theory” we mean one compact model with one set of primitives. Decision-making is too ontologically heterogeneous for that. It spans cognition, action, environment, time, and social interaction simultaneously.
> 

> **(Clarification of the Term Tractability)** A phenomenon is tractable when it can be systematically studied through manageable abstractions that yield explanatory and predictive leverage, even without exhaustively representing every detail.
> 

#### **Why not? Why it’s is difficult?**

Decision-making appears deceptively simple because we often reduce it to “choosing between options.”

But the actual phenomenon is much broader.

To explain a real decision, a theory must often account for:

- **The decider** — Who or what is deciding? A person, team, institution, or algorithm.
- **Internal cognition** — Beliefs, memory, perception, attention, inference, valuation, emotion.
- **Option space** — How alternatives become visible or imaginable.
- **Goals and values** — What the system is optimizing for.
- **The environment** — Constraints, causal structure, risks, uncertainty.
- **Time** — Deadlines, sequential adaptation, delayed consequences.
- **Action** — Translation from evaluation into implementation.
- **Feedback** — Observation of consequences after acting.
- **Learning** — Updating beliefs and future strategy.
- **Social context** — Influence, coordination, incentives, institutions, conflict.

#### What it is tractable?

> Which can be account it for?
> 

### *Which **explanatory frameworks or theories** account for it?*

> Note: Some of this ‘theories’ are actually - practical methods - to solved or think about decision making.
> 

| **Category (Theory · Framework · Method)** | **Element** | **Core Description** | **Primary Explanandum** | **What It Explains (Account)?** | **Limitation Set** |
| --- | --- | --- | --- | --- | --- |
| Theory | Expected Utility Theory | Normative account in which agents choose the option with maximal expected utility under uncertainty. | Rational choice under risk | Preference-consistent choice, trade-offs between outcomes, optimization under uncertainty. | Assumes stable preferences and high rational coherence; weak on emotion and real cognition. |
| Framework | Bounded Rationality | Decision-making under cognitive, informational, and temporal limits; agents satisfice rather than optimize. | Limited decision capacity | Heuristic reasoning, search behavior, procedural rationality, “good enough” decisions. | Less formally predictive; less suited to optimization analysis. |
| Theory | Prospect Theory | Decisions are evaluated relative to a reference point, with asymmetric weighting of gains and losses. | Decision under risk with cognitive bias | Loss aversion, framing effects, probability distortion, risk asymmetry. | Strong descriptively, but less comprehensive institutionally or temporally. |
| Theory / Framework | Bayesian Decision Theory | Decision as belief updating under uncertainty combined with choice. | Choice under uncertainty | Evidence integration, belief revision, probabilistic reasoning, adaptive inference. | Requires explicit priors and structured probabilities; descriptive realism varies. |
| Method | Decision Analysis | Structured practical method for evaluating alternatives, probabilities, consequences, and values. | Practical decision structuring | Clarifies choices, compares options, improves explicit reasoning under uncertainty. | Dependent on framing quality and quality of inputs. |
| Theory / Framework | Game Theory | Studies decision-making where outcomes depend on the choices of multiple interacting agents. | Strategic interaction | Cooperation, competition, bargaining, negotiation, incentive structures. | Often assumes strategic rationality and simplified actors. |
| Theory | Behavioral Decision Theory | Empirical study of how people actually make judgments and decisions. | Real-world human judgment | Biases, heuristics, context dependence, departures from rational choice. | Often descriptive rather than normative. |
| Framework | Dual Process Theory | Decision emerges through interaction between intuitive/automatic and reflective/deliberative cognition. | Cognitive mechanism of judgment | Intuition, impulse, deliberation, conflict between fast and slow reasoning. | Two-system distinction may oversimplify cognition. |
| Framework | System Dynamics | Understands decisions within larger systems shaped by feedback loops and delayed consequences. | Decision in complex systems | Feedback effects, unintended consequences, long-term policy behavior. | Less precise about individual cognition. |
| Framework | Naturalistic Decision Making | Examines how experts make decisions in uncertain, time-constrained, real-world environments. | Decisions under pressure | Recognition-based judgment, expertise, situational awareness, rapid operational choice. | Highly context-specific; less generalizable formally. |
| Theory | Discrete Choice Theory | Models decision-making as selection among a finite set of mutually exclusive alternatives, where each option carries an associated utility to the decision-maker. Choice probability is typically represented as a function of observed and latent preferences. | Choice among alternatives | Individual selection behavior across options (e.g. buy/not buy, A vs B vs C), preference heterogeneity, substitution effects, demand patterns, response to incentives or attributes. | Often assumes stable preferences and utility comparability; can underrepresent dynamic learning, social influence, emotion, and changing context over time. |

### Which are the affirmations that can be assign to a decision problem?

| **Category** | **Affirmation** | **Description** |
| --- | --- | --- |
| Ontic | A decision problem exists | There is a well-defined situation requiring selection among alternatives under constraints. |
| Ontic | A decision-maker is present | An agent (individual, collective, or system) is capable of selecting an action. |
| Ontic | A set of alternatives is defined | At least two distinct, mutually distinguishable actions or policies are available. |
| Ontic | A state of the world is relevant | Outcomes depend on external conditions that are not fully controlled by the decision-maker. |
| Epistemic | The decision-maker has incomplete information | The full state of the world and/or consequences of actions are not fully known. |
| Epistemic | Uncertainty over outcomes exists | Actions map to outcomes probabilistically or indeterminately. |
| Epistemic | Beliefs over states or outcomes are representable | The agent can, explicitly or implicitly, assign credences, expectations, or subjective probabilities. |
| Evaluative | Preferences or values are defined | The decision-maker has a criterion (utility, objective, goal structure) for ranking outcomes. |
| Evaluative | Trade-offs exist among outcomes | Improving one dimension of value typically worsens another. |
| Evaluative | Outcomes are comparable under a valuation scheme | There exists a coherent way (explicit or implicit) to compare consequences. |
| Structural | Actions have consequences | Each alternative induces a mapping from current state to future state(s). |
| Structural | The mapping from action to outcome is non-trivial | Outcomes are not identical across actions; the decision is meaningful. |
| Structural | Constraints restrict feasible actions | Not all logically imaginable actions are available or executable. |
| Temporal | The decision is time-indexed | The decision occurs at a specific time and may affect future states. |
| Temporal | Irreversibility or path-dependence may hold | Some actions cannot be undone or alter future option sets. |
| Strategic (optional) | Other agents may influence outcomes | The environment may include other decision-makers with interacting choices. |
| Behavioral | The decision-maker has a procedure for selection | Some rule, heuristic, or algorithm (explicit or implicit) is used to choose. |
| Normative (optional) | A notion of correctness or optimality exists | The decision can be evaluated against a standard (rationality, efficiency, welfare). |
| Diagnostic | The decision problem may be mis-specified | The framing of alternatives, values, or constraints may be incorrect or incomplete. |

## **Practice**

> *How to frame the task of decision making? How can decision-making be performed effectively? How can it be improved and evaluated? Which practical frameworks guide it?*
> 

> Note: For the pitfalls see the [*What **pathologies or failure** modes arise?*](decision-making.md).
> 

### *How to frame the task of decision making?*

> Let’s formulate the decision-making task in the most principled way possible.
> 

> **Note:** In practice, the decision problem is typically framed as a multi-objective optimization problem.
> 

#### Component Set

| **Component** | **What it captures?** | **Formalization** |
| --- | --- | --- |
| **Decision Maker** | Agent that perceives, evaluates, and acts | Defined by action capability, internal state, and metric set |
| **World State** | Current configuration of external reality at time ($t$) | State space $(\mathcal{S})$ |
| **World Dynamics** | Rules governing how the world changes through time; causal evolution of states | Transition structure $(T : \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S})$ **or** $(T : \mathcal{S} \rightarrow \mathcal{S})$ without intervention |
| **Action Space** | Set of actions available to the decision maker | $(\mathcal{A})$ |
| **Decision Problem** | Task of selecting an action under state, dynamics, and evaluation constraints | Formal tuple $(\mathcal{S}, \mathcal{A}, T, \mathcal{M}, \phi)$ |
| **Evaluation Metric Set ($\mathcal M$)** | *What matters?  (profit, survival, speed, safety, fairness)* | Utility Function Set $(\mathcal M)$
 |
| **Decision Evaluation  Model** | Mechanism by which candidate actions or future states are assessed according to the metric set -   How are the  `Evaluation Metric Set` *are operationalized?* | Evaluation function ($E : \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}^n$) or utility map $U(s')$                                        |
| **Decision Rule** |  |  |

#### Instance

> **Should I take an umbrella today?**
> 

This can be formalized as: $\mathcal D = (\mathcal S, \mathcal A, T, \mathcal M, \phi)$  where:

- $\mathcal S$: current world state - $s_t = (\text{probability of rain},; \text{time outside},; \text{weather conditions})$
- $\mathcal A$: available actions -  $\mathcal A = {\text{take umbrella},; \text{do not take umbrella}}$
- $T$: world dynamics - transition from current weather state to future weather outcome $T(s_t, a) \rightarrow s_{t+1}$
- $\mathcal M$: evaluation metric set
e.g.
    - avoiding getting wet
    - minimizing inconvenience of carrying the umbrella
    - maximizing comfort
- Decision **Evaluation Model**: function that scores each action under the evaluation metric set $E : \mathcal S \times \mathcal A \rightarrow \mathbb{R}$ - for our problem  one possible evaluation model is:  $E(a)= w_1(\text{stay dry})  w_2(\text{carrying inconvenience}) + w_3(\text{comfort})$.
- $(\phi)$: **decision rule** - selects the action that maximizes expected value under ($\mathcal M$) - for our case - $E(\text{take umbrella}) > E(\text{do not take umbrella})$.

#### How can “Should I take an umbrella today?” be framed in an elementary way for a simple decision maker?

For a simple decision maker, this process can be read informally as:

- **What is happening right now?** → *Looks cloudy; rain may happen.*
- **What can I do?** → *Take the umbrella or leave it.*
- **What is likely to happen next?** → *If it rains and I do not take it, I may get wet; if I take it and it does not rain, I carry it unnecessarily.*
- **What matters to me?** → *Staying dry, avoiding inconvenience, and remaining comfortable.*
- **Which option scores better overall?** → *Compare both actions under those criteria.*
- **Choose the better action.** → *Take the umbrella if its expected benefit exceeds its inconvenience.*

### *How can an execution of a decision making task can be evaluated?*

> By assessing the quality of the **process**, the **choice produced**, and the **outcome generated** relative to the decision maker’s objectives and the information available at the time of decision.
> 

### How to improve the execution of a decision-making task?

> By improving the quality of the state representation, option generation, prediction, evaluation, and action selection performed during the decision process.
> 

See:

- **Improve state representation** — build a more accurate understanding of the current world state.
- **Improve option generation** — generate better or broader candidate actions.
- **Improve forecasting** — better predict how actions propagate through world dynamics.
- **Improve evaluation** — refine the metric set and scoring model used to compare outcomes.
- **Improve selection** — choose more coherently under uncertainty, trade-offs, and constraints.
- **Improve feedback and learning** — compare expected vs realized outcomes and update future decision models accordingly.

### *Which practical elements (tool, framework, heuristic, etc)  guide it?*

> Note: All of this have to be grounded in the theory - but the theoretical explanation is not a practical element - it’s the guide at beast on how to design practical element to guide decision making.
> 

> See for the theory [*Which **explanatory frameworks or theories** account for it?*](decision-making.md).
> 

> **Note: Decision elements partition into two fundamental classes: *heuristic* or formal** depending on whether they primarily reduce cognitive cost or optimize expected value under an explicit model.
> 

| **Category** | **Element** | **Description** | **Operationalization** | **Evaluation (Scope · Limitation)** |
| --- | --- | --- | --- | --- |
| Practical Framework | Decision Tree | Tree-structured representation of sequential decisions and outcomes. | Define decision nodes → enumerate actions → map outcomes → compare branches. | Strong for structured sequential problems; scales poorly with combinatorial complexity. |
| Practical Framework | OODA Loop | Iterative decision cycle: Observe–Orient–Decide–Act. | Continuous environmental sensing → interpretation → action → feedback loop. | Effective in dynamic environments; can underemphasize deep deliberation. |
| Practical Framework | SWOT Analysis | Strategic diagnostic of internal/external factors. | Identify strengths, weaknesses, opportunities, threats. | Useful for framing; weak for precise decision selection. |
| Practical Framework | Scenario Planning | Multi-future planning under uncertainty. | Construct plausible futures → evaluate decisions across scenarios. | Robust for long-term uncertainty; non-predictive. |
| Theoretical Model | Markov Decision Process (MDP) | Sequential decision model under stochastic transitions. | Define states, actions, transitions, rewards → compute optimal policy. | Powerful for control/optimization; requires strong modeling assumptions. |
| Method | Monte Carlo Simulation | Stochastic sampling for outcome estimation. | Simulate random samples → estimate distribution of outcomes. | Effective under uncertainty; computationally intensive. |
| Method | Stochastic Optimization | Optimization under probabilistic uncertainty. | Define objective → incorporate randomness → solve expected/robust solution. | Strong for uncertain systems; model sensitivity can be high. |
| Method | Cost–Benefit Analysis (CBA) | Quantifies net value of alternatives. | Estimate costs/benefits → compute net utility → compare options. | Effective for quantifiable outcomes; weak for intangible factors. |
| Method | Multi-Criteria Decision Analysis (MCDA) | Multi-factor evaluation of alternatives. | Define criteria → assign weights → score alternatives → rank. | Flexible but sensitive to subjective weighting. |
| Method | Prioritization Matrix | Ranking framework for execution ordering. | Define axes (impact/effort/etc.) → score → prioritize. | Useful operationally; oversimplifies dependencies. |
| Method | Pre-Mortem Analysis | Failure simulation before execution. | Assume failure → identify causes → adjust plan. | Reduces blind spots; depends on cognitive diversity. |
| Method | Post-Mortem / Retrospective | Outcome evaluation after execution. | Compare outcomes vs expectations → extract lessons. | Improves learning; affected by hindsight bias. |
| Tool | Decision Matrix | Tabular comparison of alternatives vs criteria. | Build matrix → score → aggregate → select option. | Transparent but can induce false precision. |
| Tool | Checklist | Procedural verification tool. | Follow predefined step/condition list. | High reliability for routine tasks; weak for novel problems. |
| Tool | Risk Matrix | Probability–impact risk mapping tool. | Identify risks → estimate likelihood/impact → classify. | Useful for governance; coarse granularity. |
| Theoretical Model | Bayesian Decision Theory | Decision-making under uncertainty using Bayes rule + utility. | Update beliefs → compute expected utility → choose optimal action. | Normatively strong; requires probabilistic specification. |
| Theoretical Model | Expected Utility Theory | Utility-maximizing decision under risk. | Assign utilities → compute expected value → maximize. | Foundational but descriptively limited. |
| Method | Risk Analysis Frameworks | Structured risk identification and evaluation. | Identify risks → assess exposure → prioritize mitigation. | Broad applicability; often qualitative. |
| Method | Value-at-Risk (VaR) | Quantile-based downside risk measure. | Estimate loss distribution → compute percentile loss threshold. | Widely used in finance; ignores tail risk beyond cutoff. |
| Optimization Method | Robust Optimization | Optimization under worst-case uncertainty. | Define uncertainty set → optimize worst-case objective. | Strong guarantees; can be overly conservative. |
| Optimization Method | Chance-Constrained Optimization | Probabilistic constraint satisfaction. | Define constraints → enforce probability thresholds. | Balances feasibility and risk; hard to calibrate probabilities. |
| Method | Real Options Analysis | Valuation of decision flexibility over time. | Model options embedded in decisions → evaluate strategic flexibility. | Captures adaptability; model complexity high. |
| Behavioral Theory | Satisficing | Choice of satisfactory rather than optimal solutions. | Define threshold → select first acceptable option. | Realistic under bounded rationality; not optimal. |
| Behavioral Theory | Heuristics | Rule-of-thumb decision strategies. | Apply simplified cognitive rules. | Fast and practical; prone to systematic bias. |
| Behavioral Theory | Prospect Theory | Descriptive model of decision under risk. | Model reference dependence + loss aversion. | Empirically strong; normatively inconsistent. |
| Method | Sensitivity Analysis | Impact of parameter variation on outcomes. | Vary inputs → observe output changes. | Useful for robustness; limited structural insight. |
| Game Theory | Nash Equilibrium | Stable strategy profile in multi-agent systems. | Define payoff functions → solve fixed-point equilibrium. | Central concept; may yield multiple or non-intuitive equilibria. |
| Game Theory | Bayesian Games | Game theory under incomplete information. | Define beliefs + strategies → compute Bayesian equilibrium. | Powerful but computationally complex. |
| Game Theory | Mechanism Design | Design of systems to elicit desired behaviors. | Define incentives → design rules → analyze equilibria. | Strong normative power; sensitive to assumptions. |
| Behavioral Theory | Behavioral Decision Theory | Empirical study of real decision behavior. | Observe deviations from rational models. | Descriptive richness; limited predictive structure. |
| Behavioral Theory | Bounded Rationality | Decision-making under cognitive/resource limits. | Model constrained optimization or heuristics. | Realistic; less precise mathematically. |
| Learning Model | Reinforcement Learning | Learning optimal policy via reward feedback. | Define environment → learn policy via reward signals. | Powerful for adaptive systems; data intensive. |
| Probabilistic Model | Bayesian Networks | Graphical probabilistic dependency modeling. | Define DAG structure → assign conditional probabilities → infer. | Interpretable; structure specification is difficult. |
| ML Method | Deep Learning for Uncertainty Quantification | Neural estimation of predictive uncertainty. | Train models → estimate probabilistic outputs. | High performance; interpretability issues. |
| Method | AHP (Analytic Hierarchy Process) | Pairwise comparison decision method. | Decompose hierarchy → pairwise comparisons → aggregate weights. | Structured but consistency-sensitive. |
| Method | TOPSIS | Distance-to-ideal ranking method. | Compute ideal solution → rank by closeness. | Simple and effective; depends on normalization. |
| Method | PROMETHEE | Outranking-based multicriteria decision method. | Compare alternatives pairwise → compute preference flows. | Rich preference modeling; computational overhead. |
| Systems Model | System Dynamics | Feedback-loop modeling of complex systems. | Define stocks/flows → simulate dynamics over time. | Strong for macro behavior; coarse granularity. |
| Systems Method | Soft Systems Methodology | Qualitative systems problem structuring. | Model stakeholders → define perspectives → iterate understanding. | Good for ambiguity; weak formal precision. |
| Principle | Precautionary Principle | Avoid action under severe uncertainty risk. | Identify potential harm → prioritize avoidance. | Conservative; may inhibit innovation. |
| Ethical Theory | Utilitarianism | Maximize aggregate utility. | Evaluate total consequences → choose maximum welfare option. | Normative baseline; aggregation issues. |
| Ethical Theory | Deontological Ethics | Rule-based decision constraints. | Apply moral rules independent of outcomes. | Strong constraints; may ignore consequences. |
| Systems Method | Adaptive Management | Iterative policy learning system. | Implement → monitor → adjust policies. | Good for ecological systems; slow convergence. |
| Method | Dynamic Decision-Making | Decisions evolving over time under feedback. | Update actions based on system evolution. | Realistic; analytically complex. |
| Finance Model | Kelly Criterion | Optimal bet sizing for growth maximization. | Maximize log wealth growth → compute optimal fraction. | Theoretically optimal; risk-sensitive. |
| Finance Model | Modern Portfolio Theory (MPT) | Portfolio optimization under risk-return tradeoff. | Optimize expected return vs variance. | Foundational; relies on distribution assumptions. |
| Finance Model | Black–Scholes Model | Option pricing under stochastic dynamics. | Model asset diffusion → price derivative analytically. | Widely used; assumes idealized markets. |
| Engineering Model | Reliability Engineering | System failure modeling and prediction. | Model failure rates → compute reliability metrics. | Strong for systems design; data dependent. |
| Engineering Model | Robust Design | Design insensitive to variability. | Optimize performance under parameter variation. | Improves stability; may reduce optimal performance. |
| Method | Policy Robustness Analysis | Evaluation of policy stability under uncertainty. | Stress-test policies across scenarios. | Useful for governance; scenario-dependent. |
| Decision Rule | Maximin (Wald Criterion) | Choose worst-case maximizing option. | Evaluate minimum payoff → select best worst-case. | Conservative; ignores upside. |
| Decision Rule | Maximax | Optimistic decision rule. | Select option with maximum possible payoff. | Risk-seeking; unstable under uncertainty. |
| Decision Rule | Hurwicz Criterion | Weighted optimism-pessimism rule. | Combine best/worst outcomes via parameter α. | Flexible but subjective α choice. |
| Decision Rule | Minimax Regret | Minimize worst-case regret. | Compute regret matrix → minimize maximum regret. | Balanced but computationally heavier. |
| Method | Cost-Benefit Analysis (CBA) | Net value comparison of alternatives. | Quantify costs/benefits → compute net payof | Works for measurable outcomes; weak for intangibles. |

### Which are the practical heuristics useful for guiding the practice in decision making?

| **Category** | **Heuristic** | **Description** | **Evaluation** |
| --- | --- | --- | --- |
| **Framing & Scoping** | **10-10-10 Rule (Welch)** | Evaluate a decision by asking: *How will I feel about this choice in 10 minutes? 10 months? 10 years?* | Forces emotional distancing and time-horizon perspective. Effective for impulsive or short-termist choices; may oversimplify deeply complex trade-offs where long-term consequences are unknowable. |
|  | **Inversion / Pre-Mortem** | Instead of asking “How can we succeed?”, ask “If this project failed catastrophically, what would have caused it?” Then design preventive measures. | Systematically uncovers blind spots and collective overconfidence. Requires psychological safety to voice fears; can become ritualistic if not linked to concrete plan changes. |
|  | **Problem Reframing (“What is the real question?”)** | Before solving, explicitly iterate on the problem statement: *Are we solving the right problem? What is the core need?* | Prevents solving symptoms rather than causes. Time-consuming initially; may stall action if used excessively, but high leverage for ill-defined strategic choices. |
| **Option Generation** | **Analogical Reasoning (Case-Based)** | Search memory for similar past situations or exemplars: *How did we/others handle something like this before?* | Fast pattern recognition; leverages collective experience. Risk of surface-level analogies and ignoring novel features; works best when supplemented with structural mapping. |
|  | **Vanishing Options Test** | For each option in turn, assume it is impossible and force yourself to find an alternative. Then compare the expanded set. | Counters premature narrowing and false dilemmas. May generate low-quality alternatives if constraints are relaxed too far; a creativity-enhancing safeguard rather than a selection rule. |
| **Evaluation & Selection** | **Satisficing (Simon)** | Set an aspiration level for each key criterion. Select the *first* option that meets all thresholds, rather than searching for the optimal one. | Efficient under bounded rationality; avoids analysis paralysis. Outcome quality depends entirely on threshold calibration; risks “good enough” being lower than what was truly attainable if thresholds are set too low. |
|  | **Take-the-Best (Gigerenzer)** | Identify the single most valid cue that discriminates between options. Decide solely based on that cue; if it is ambiguous, move to the next most valid cue and stop when one option is clearly favored. | Extremely frugal and often surprisingly accurate in real environments (less-is-more effect). Fragile when cue validities change rapidly; assumes a structured set of known cues. |
|  | **Elimination by Aspects (Tversky)** | Define acceptable cutoffs on attributes in order of importance. Eliminate any option that fails a cutoff; continue until one option remains. | Transparent and easy to justify; mimics natural non-compensatory decision making. Ignores trade-offs where an exceptional performance on one attribute could outweigh a minor deficit on another. |
|  | **Pro/Con List with Weighting** | List pluses and minuses for each option. Optionally assign rough weights (+1 to +5, -1 to -5) to reflect importance, then sum. | Simple, familiar, and externalizes working memory. Prone to confirmation bias in item generation; weights are subjective and can be manipulated post-hoc. Best as a discussion tool, not a final arbiter. |
| **Uncertainty Management** | **Minimax Regret Heuristic** | For each option, identify the worst “regret” (gap between outcome and best possible outcome in that scenario). Choose the option whose maximum regret across scenarios is smallest. | Protects against extreme downside regret without needing probabilities. Sensitive to scenario specification; may lead to overly conservative choices if high-regret scenarios are improbable. |
|  | **Robust Action / Hedging** | Prefer actions that keep future options open or work reasonably well across many plausible scenarios (e.g., “no-regret moves”). | Resilient under deep uncertainty; avoids lock-in. Can dilute resources and prevent bold, high-return bets when confidence is warranted; may be outperformed by focused strategies if the world is stable. |
|  | **Safety Margin / Factor of Safety** | In engineering or resource decisions, intentionally overestimate loads, timelines, or costs by a fixed multiplier to absorb surprises. | Simple, effective buffer against variability and ignorance. Cumulative safety factors can compound into waste; requires calibration to avoid gross over-engineering. |
| **Commitment & Execution** | **Two-Way Door Rule (Bezos)** | Classify decisions as Type 1 (irreversible, “one-way door”) or Type 2 (reversible, “two-way door”). For Type 2, decide quickly and delegate; for Type 1, proceed slowly with deep analysis. | Focuses analytical effort on high-stakes, irreversible choices; prevents over-analysis of low-risk decisions. Misclassification risk: some apparently reversible decisions create path dependencies that are hard to undo in practice. |
|  | **Minimum Viable Decision (MVD)** | Identify the smallest, cheapest action that tests a key assumption of your preferred option. Decide to run that test, then review. | Transforms a big binary commitment into a learning loop; reduces risk of large sunk costs. Only applies when decision can be decomposed into testable hypotheses; may delay necessary commitment in time-critical situations. |
|  | **Set a Decision Deadline (Timeboxing)** | Explicitly assign a time limit for deliberation, after which you must choose based on the best available information at that moment. | Counters excessive delay and analysis paralysis. Creates artificial pressure that may reduce information quality if deadline is too tight; the heuristic is the deadline itself, not the choice rule used at expiry. |
| **Social & Group Setting** | **Devil’s Advocate Protocol** | Formally assign one person (or subgroup) the role of challenging the majority-favored option, regardless of personal belief. | Reduces groupthink and surfaces hidden assumptions. Can be performed perfunctorily; works best when the role rotates and the critique is genuinely considered, not just tolerated. |
|  | **Anonymous Voting / Delphi Method** | In initial rounds, gather independent, anonymous judgments or forecasts. Aggregate, share anonymized reasons, and re-poll. | Diminishes authority capture and social conformity; leverages collective wisdom. Slower than open discussion; may miss the nuance of live debate. Best for estimation and criteria weighting, not for generating novel options. |

## **Case Study**

| **Case Study** | **Scenario (World State)** | **Decision Maker(s) {Constraints, Uncertainty Structure, Objective, Capabilities}** | **Decision Problem** | **Action Space** | **Context** | **Decision Evaluation Model** | **Decision Rule** | **Postmortem Analysis** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Pandemic Policy Response (COVID-19 Early Phase)** | Emergence of a novel infectious disease with exponential spread and high uncertainty about transmission and mortality. | Government + public health agencies; constraints: ICU capacity, economic tolerance; uncertainty: epidemiological parameters; objective: minimize deaths + system collapse. | Select intervention strategy under high uncertainty. | Lockdown, partial restrictions, travel bans, testing/contact tracing, no intervention. | Globalized economy, political pressure, behavioral compliance variability. | Multi-objective loss function (health outcomes + economic cost). | Threshold-based containment strategies (e.g., reduce Rₜ < 1). | Early interventions reduced spread but caused economic disruption; errors from delayed data, model uncertainty, and compliance heterogeneity. |
| **Corporate Product Launch (Tech Platform)** | Competitive tech market with uncertain demand and rapid innovation cycles. | Executive team; constraints: budget, engineering capacity, time-to-market; uncertainty: adoption and competition; objective: maximize growth and revenue. | Decide whether and how to launch a product/feature. | Launch, staged rollout, pivot, delay, cancel. | Market competition, investor expectations, network effects. | Forecast-based revenue + growth models (LTV/CAC, adoption curves). | Expected value maximization with managerial adjustment. | Failures often due to overestimated demand or underestimated competition response. |
| **Autonomous Vehicle Navigation** | Real-time dynamic road environment with uncertainty in agent behavior and sensor noise. | Autonomous system; constraints: safety rules, physical limits; uncertainty: environment and agent intent; objective: safe + efficient motion. | Choose immediate control action at each timestep. | Accelerate, brake, lane change, turn, maintain trajectory. | Traffic laws, road geometry, weather, sensor quality. | Cost function combining safety, time, comfort, legality. | Model predictive control / RL policy optimization. | Failures from rare edge cases, perception errors, and distribution shift. |
| **Monetary Policy Interest Rate Decision** | Economy with inflation pressure, unemployment variation, and uncertain macro dynamics. | Central bank; constraints: policy lag, mandate; uncertainty: inflation/output gap; objective: price stability + employment. | Set optimal interest rate policy. | Raise, lower, hold, forward guidance adjustments. | Global capital flows, fiscal policy, expectations dynamics. | Macroeconomic forecasting models (DSGE, Phillips curve variants). | Taylor-rule-style heuristic with judgment adjustments. | Forecast errors due to structural shifts and model misspecification. |
| **University Admissions Selection** | Large applicant pool with limited seats and noisy signals of future performance. | Admissions committee; constraints: capacity, legal/equity rules; uncertainty: applicant quality signals; objective: maximize cohort quality + institutional goals. | Select subset of applicants for admission. | Admit, reject, waitlist, conditional admit. | Rankings pressure, diversity requirements, reputational incentives. | Multi-criteria scoring (academic + extracurricular + predicted success). | Ranking + threshold cutoffs + categorical constraints. | Biases from proxy variables; calibration errors in predicting performance. |

## QA

### How to frame the case studies?

> A case study is framed as a **bounded decision episode embedded in a specific environment**, reconstructed through its actors, constraints, information structure, and outcome trajectory, in order to explain the causal mechanism linking context → choice → consequence.
> 

| **Element** | **Description** |
| --- | --- |
| Scenario (World State) | The relevant configuration of the external world at decision time, including all variables that may influence outcomes (physical, economic, social, institutional state). |
| Decision Maker(s) {Constraints, Uncertainty Structure, Objective, Capabilities} | The agent or set of agents performing the decision, characterized by their limitations (resources, time, cognition), epistemic state (beliefs, information access), preference structure (objectives/utility), and action capabilities. |
| Decision Problem | The induced formalized task: selection of an action under uncertainty given a world state, objective, and constraints. It is the *problem representation*, not the world itself. |
| Action Space | The set of feasible and distinguishable actions available to the decision-maker at the time of choice, including structural constraints and prohibitions. |
| Context | The surrounding structural conditions that shape the decision but are not directly part of the state-action mapping (institutional rules, cultural norms, market conditions, temporal urgency). |
| Decision Evaluation Model | The internal or external mapping used to assign value to outcomes (utility function, loss function, reward model, multi-criteria scoring system, normative benchmark). |
| Decision Rule | The selection mechanism that maps (beliefs, evaluations, constraints) → action (e.g., argmax expected utility, satisficing threshold, heuristic policy, learned policy, equilibrium strategy). |
| Postmortem Analysis | The retrospective evaluation of the decision episode after outcomes are realized, reconstructing the relationship between expected vs actual outcomes, identifying deviations between predicted and realized consequences, and diagnosing causal factors (e.g., informational errors, model misspecification, constraint misjudgment, decision rule failure, or contextual shifts). It also includes counterfactual analysis (what would have happened under alternative actions or better information) and yields explanatory judgments about performance, robustness, and failure modes. |

### Which are the related epistemic areas?

| **Epistemic Area** | **Description** | **Relation with Decision Theory** |
| --- | --- | --- |
| Probability Theory | Formal calculus of uncertainty and random variables. | Provides the foundational language for representing uncertainty in states, outcomes, and transitions (core to Bayesian decision theory, MDPs, risk models). |
| Statistics (Inference Theory) | Methods for estimating parameters and learning from data. | Supplies belief-updating mechanisms and empirical grounding for decision models under uncertainty. |
| Bayesian Epistemology | Normative theory of belief updating via Bayes’ rule. | Direct epistemic foundation of Bayesian decision theory; governs belief formation used in expected utility computation. |
| Utility Theory | Formal representation of preferences over outcomes. | Defines the value structure required to evaluate and compare actions in rational decision models. |
| Optimization Theory | Mathematical study of selecting best elements under constraints. | Encodes the computational core of decision-making as maximization/minimization problems. |
| Game Theory | Analysis of strategic interaction among rational agents. | Extends decision theory to multi-agent environments where outcomes depend on others’ decisions. |
| Economics (Microeconomic Theory) | Study of choice, incentives, and market behavior. | Provides formal models of rational agents, equilibrium behavior, and constrained choice environments. |
| Information Theory | Quantification of information, entropy, and information flow. | Shapes decision-making under information constraints; foundational for active inference, RL exploration, and uncertainty reduction. |
| Control Theory | Regulation of dynamic systems via feedback control. | Formalizes sequential decision-making in continuous time systems; strongly related to MDPs and RL. |
| Cognitive Science | Study of human cognition, perception, and reasoning. | Provides descriptive constraints (bounded rationality, heuristics) on how real decision-making deviates from normative models. |
| Psychology (Judgment & Decision-Making) | Empirical study of human choice behavior. | Introduces systematic deviations from rational models (biases, heuristics, prospect theory). |
| Behavioral Economics | Integration of psychology with economic decision models. | Modifies classical decision theory to account for observed non-rational behaviors. |
| Machine Learning | Data-driven modeling of patterns and predictions. | Provides predictive models and learned policies used in modern decision systems (RL, uncertainty quantification). |
| Reinforcement Learning Theory | Learning optimal policies via reward signals. | Operationalizes sequential decision theory under unknown environments (approximate MDP solving). |
| Systems Theory | Study of complex interacting systems and feedback loops. | Provides structural frameworks for modeling multi-component decision environments. |
| Complexity Theory | Study of computational hardness and tractability. | Determines which decision problems are solvable or approximable within resource constraints. |
| Logic (Formal & Modal Logic) | Study of valid inference and structured reasoning. | Underlies formal representations of belief, knowledge, and decision rules. |
| Ethics (Normative Philosophy) | Study of what agents ought to do. | Defines normative constraints on allowable decision outcomes (utilitarianism, deontology, etc.). |
| Epistemology (General) | Study of knowledge, justification, and belief. | Provides foundational constraints on what counts as rational belief in decision processes. |
| Network Theory | Study of graph-structured interactions. | Models dependencies between agents, states, and information flows in decision systems. |
| Dynamical Systems Theory | Study of time-evolving systems governed by rules. | Formalizes temporal evolution of states in sequential decision problems. |

## References

- [Ontology](https://app.notion.com/p/Ontology-138eea37a34f43ed87c16d1818629723?pvs=21)
- [Decision Theory](https://en.wikipedia.org/wiki/Decision_theory)
- [Philosophia Naturalis](https://app.notion.com/p/Philosophia-Naturalis-32ac0f5171ec807b9388c870ab664abf?pvs=21)
- https://en.wikipedia.org/wiki/Rationality
- https://en.wikipedia.org/wiki/Control_theory
- https://en.wikipedia.org/wiki/Decision_theory
- https://www.bremontix.xyz/toolbox/epistemica/graph.html
- https://en.wikipedia.org/wiki/Discrete_choice
- [Decision Theory - Plato Stanford](https://plato.stanford.edu/entries/decision-theory/)
- [The “Just One More” Paradox – Kelly Criterion](https://news.ycombinator.com/item?id=37996991)
- https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis
- North, D. Warner. "A tutorial introduction to decision theory." *IEEE transactions on systems science and cybernetics* 4.3 (1968): 200-210.
- **von Neumann, J., & Morgenstern, O. (1944).** *Theory of games and economic behavior*. Princeton University Press.
- **Savage, L. J. (1954).** *The foundations of statistics*. John Wiley & Sons.
- **Raiffa, H. (1968).** *Decision analysis: Introductory lectures on choices under uncertainty*. Addison-Wesley.
- **Luce, R. D., & Raiffa, H. (1957).** *Games and decisions: Introduction and critical survey*. John Wiley & Sons. [Internet Archive](https://ia802909.us.archive.org/6/items/in.ernet.dli.2015.132625/2015.132625.Games-And-Decisions-Introduction-And-Critical-Survey.pdf)
- **Berger, J. O. (1985).** *Statistical decision theory and Bayesian analysis* (2nd ed.). Springer.
- **Robert, C. P. (2001).** *The Bayesian choice: From decision-theoretic foundations to computational implementation*. Springer. (Winner of the 2004 DeGroot Prize)
- **Simon, H. A. (1982).** *Models of bounded rationality* (Vols. 1–3). MIT Press.
- **Tversky, A., & Kahneman, D. (1974).** Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124–1131.
- **Kahneman, D., Slovic, P., & Tversky, A. (Eds.). (1982).** *Judgment under uncertainty: Heuristics and biases*. Cambridge University Press.
- **Kahneman, D., & Tversky, A. (1979).** Prospect theory: An analysis of decision under risk. *Econometrica, 47*(2), 263–292.
- **Kahneman, D., & Tversky, A. (1984).** Choices, values, and frames. *American Psychologist, 39*(4), 341–350.
- **Kahneman, D. (2011).** *Thinking, fast and slow*. Farrar, Straus and Giroux.
- **Evans, J. S. B. T., & Stanovich, K. E. (2013).** Dual-process theories of higher cognition: Advancing the debate. *Perspectives on Psychological Science, 8*(3), 223–241.
- **Stanovich, K. E. (2011).** *Rationality and the reflective mind*. Oxford University Press.
- **Klein, G. A. (1998).** *Sources of power: How people make decisions*. MIT Press.
- **Klein, G. A., Orasanu, J., Calderwood, R., & Zsambok, C. E. (Eds.). (1993).** *Decision making in action: Models and methods*. Ablex Publishing.
- **Hammond, J. S., Keeney, R. L., & Raiffa, H. (1999).** *Smart choices: A practical guide to making better decisions*. Harvard Business School Press.
- **von Winterfeldt, D., & Edwards, W. (1986).** *Decision analysis and behavioral research*. Cambridge University Press.
- **Goodwin, P., & Wright, G. (2014).** *Decision analysis for management judgment* (5th ed.). John Wiley & Sons.
- **Belton, V., & Stewart, T. J. (2002).** *Multiple criteria decision analysis: An integrated approach*. Kluwer Academic Publishers.
- **Saaty, T. L. (1980).** *The analytic hierarchy process: Planning, priority setting, resource allocation*. McGraw-Hill.
- **Janis, I. L. (1982).** *Groupthink: Psychological studies of policy decisions and fiascoes* (2nd ed.). Houghton Mifflin.
- **Whyte, G. (1991).** The escalation of commitment to a course of action: A review and integration. *Academy of Management Review, 16*(2), 398–421.
- **Arkes, H. R., & Blumer, C. (1985).** The psychology of sunk cost. *Organizational Behavior and Human Decision Processes, 35*(1), 124–140.
- **Bazerman, M. H., & Moore, D. A. (2012).** *Judgment in managerial decision making* (8th ed.). John Wiley & Sons.
- **Kahneman, D., & Tversky, A. (1979).** Prospect theory: An analysis of decision under risk. *Econometrica, 47*(2), 263–292.
- **Gadomski, A. M. (1993).** *TOGA: A methodological and conceptual framework for knowledge-based systems*. ENEA Technical Report.
- **Dignum, F., & Greaves, M. (Eds.). (2017).** *Issues in agent communication*. Springer.
- **Putnam, H. (1967).** The nature of mental states. In W. H. Capitan & D. D. Merrill (Eds.), *Art, mind, and religion* (pp. 37–48). University of Pittsburgh Press.
- **Sutton, R. S., & Barto, A. G. (2018).** *Reinforcement learning: An introduction* (2nd ed.). MIT Press.
- **Baron, J. (2007).** *Thinking and deciding* (4th ed.). Cambridge University Press.
- **Peterson, M. (2017).** *An introduction to decision theory* (2nd ed.). Cambridge University Press.
- [Control Theory](dynamical-intelligence/control-theory.md)
- [Simulation](simulation.md)
- [Causality](causality.md)
- [Observational](observational.md)
- [Dynamical Intelligence](dynamical-intelligence.md)
- https://www.edx.org/learn/discrete-mathematics/ecole-polytechnique-federale-de-lausanne-introduction-to-discrete-choice-models
- Ben-Akiva, Moshe and Steven R. Lerman (1985) Discrete Choice Analysis: Theory and Application to Travel Demand. Cambridge, Mass.: MIT Press.
- https://bactra.org/notebooks/political-decision-making.html
- https://bactra.org/notebooks/sequential-decisions.html
- https://bactra.org/notebooks/judgment.html
- https://bactra.org/notebooks/decision-theory.html
- [Prediction Market](https://app.notion.com/p/Prediction-Market-286c0f5171ec80ccb3bce24ee14fc060?pvs=21)
- https://www.youtube.com/playlist?list=PL7xZX_sYV5vEfMxkb5SUuGkZcizIhGzhx
