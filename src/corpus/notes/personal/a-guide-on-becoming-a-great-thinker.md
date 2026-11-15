---
tags: [note, guia]
---

# A Guide on Becoming a Great Thinker

**Contains:** [A Guide to Action](/view.html?p=notes/personal/a-guide-to-action.md), [A Guide to Study](/view.html?p=notes/personal/a-guide-to-study.md), [A Guide to Debug Others People's Minds](/view.html?p=notes/personal/a-guide-to-debug-others-people-s-minds.md), [A Guide on Intellectuals Dialogs](/view.html?p=notes/personal/a-guide-on-intellectuals-dialogs.md)

> **A guide to improving your thinking—designed to help you become more critical, reflective, intellectually curious, and clear in your reasoning—so you can better understand complex issues, challenge assumptions, and make well-informed decisions across all areas of life.**
> 

> In essence, this guide shows you how to effectively **parse and predict reality**, equipping you with the tools to navigate complexity and uncertainty with insight and confidence.
> 

> <u>**The effectiveness of our mental tools correlates with the time and effort we invest in improving them.**</u>
> 

> **Nota:** Sinónimos de “bad thinker”: “pensador superficial”, “expositor de obviedades”.
> 

> Nota: Sinónimos de “good thinker”: “pensador sistemático”, “analista fino”.
> 

## Index

## Breviarium

- **Cultivate Curiosity**
    - **Ask "Why?" Constantly** – Challenge assumptions and dig deeper into the root of ideas.
    - **Explore Diverse Fields** – Read widely across science, philosophy, history, and art to make unexpected connections.
    - **Stay Open-Minded** – Be willing to question your own beliefs and consider opposing  viewpoints.
- Master Several Frameworks of Thinking
- Master the Art of Learning
- Communicate Clearly
- Build Mental Discipline
- Study the Great Thinkers
    - **Socrates** – Question everything.
    - **Einstein** – Thought experiments and imagination.
    - **Marie Curie** – Rigorous experimentation and persistence.
    - **Nassim Taleb** – Antifragility and skepticism of predictions.
- Apply Thinking to Real Problems
- Stay Humble & Keep Improving

## What makes  a bad thinker?

> A "bad thinker" exhibits systematic failures in cognitive processes, characterized by deviations from normative standards of rationality, epistemology, and logic.
> 

> A bad thinker systematically misallocates model capacity, either by overfitting surface regularities or underfitting latent structure, thereby failing to construct minimal sufficient representations that maximize explanatory and predictive power per unit of description length under realistic uncertainty and feedback constraints.
> 

> See [Explanation](https://app.notion.com/p/Explanation-11dc0f5171ec80b8b8bcf08793bc64a8?pvs=21).
> 

### **Epistemological Failures**

- **Poor Evidence Calibration**: Inability to weight evidence according to Bayesian principles (e.g., ignoring base rates, misjudging likelihood ratios).
- **Doxastic Irresponsibility**: Forming/maintaining beliefs without sufficient justificatory evidence or despite counterevidence.
- **Non-Updating of Beliefs**: Resisting belief revision in light of new data (belief perseverance), violating the *principle of total evidence*.
- Preferring instantial evidence (case studies) over statistical evidence (meta-analyses) violates the Principle of Induction.

### **Cognitive Biases & Heuristics (System 1 Dominance)**

- **Confirmation Bias**: Selectively seeking/recalling information that confirms pre-existing beliefs while ignoring disconfirming evidence.
- **Affect Heuristic**: Allowing emotional responses to override probabilistic reasoning (e.g., "This feels dangerous, therefore it *is* dangerous").
- **Availability Heuristic**: Overestimating the probability of events based on ease of recall (e.g., vivid media coverage distorting risk assessment).
- **Sunk Cost Fallacy**: Continuing futile endeavors due to prior investment (irrational resource allocation).

### **Metacognitive Deficits**

- **Illusory Superiority (Dunning-Kruger Effect)**: Lack of competence prevents self-assessment accuracy, leading to overconfidence.
- **Failure of Debiasing**: Inability to recognize or correct for known biases (e.g., not adjusting for anchoring effects).
- **Cognitive Miserliness**: Defaulting to low-effort processing (Type 1 thinking) when analytical reasoning (Type 2) is required.

### **Logical & Argumentative Failures**

- **Formal Fallacies**:
    - Affirming the consequent (*If P, then Q; Q, therefore P*).
    - Denying the antecedent (*If P, then Q; Not P, therefore not Q*).
- **Informal Fallacies**:
    - *Ad hominem* (attacking the person, not the argument).
    - *Straw man* (misrepresenting an opponent's position).
    - *False dilemma* (oversimplifying options).

### **Dispositional & Motivational Factors**

- **Motivated Reasoning**: Subconsciously tailoring reasoning to arrive at desired conclusions (driven by identity/ideology).
- **Epistemic Closed-Mindedness**: Rejecting disconfirming evidence to protect worldview (e.g., backfire effect).
- **Intellectual Laziness**: Avoidance of cognitive effort, reliance on intuition in complex domains.

### **Probabilistic & Statistical Illiteracy**

- **Misunderstanding Conditional Probability**: Failing to grasp *P(A|B)* vs. *P(B|A)* (e.g., prosecutor's fallacy).
- **Neglect of Sample Size**: Drawing conclusions from statistically underpowered data.
- **Conjunction Fallacy**: Believing specific outcomes are more probable than general ones (e.g., Linda Problem).

### **Failure to Abstract (Overfitting to Instances)**

> **Loss of Predictive Power**: Instance-bound thinking fails in novel contexts (no transfer learning).
> 

> **Fragility**: Laws generalize; anecdotes break under slight perturbations.
> 

A bad thinker often exhibits:

- **Case-Based Reasoning**: Over-reliance on anecdotal or singular examples (*"I know someone who smoked and lived to 100, so smoking isn’t harmful"*).
    - Violates **statistical generalization** (ignoring distributions for outliers).
    - Reflects **inductive laziness**—failure to derive principles from data.
- **Neglect of Causal Mechanisms**: Describing *what* happened without modeling *why* (surface-level analysis).
    - Contrasts with deep thinkers who use **abductive reasoning** (inferring best explanations) or **computational modeling** (simulating underlying laws).

### Cognitive Basin of Attraction

> A **cognitive basin of attraction** is a mental “default mode” for interpreting a situation or choosing a solution. Once thought patterns settle into this basin, alternative ways of thinking become less likely to be considered.
> 

Case:

Suppose $X$ is the spike count of a neuron:

- **Default focus (attractor)**: Model $X$ with a probability distribution, e.g., Poisson($\lambda$), to capture the likelihood of seeing a given spike count.
- **Alternative representations ignored**:
    1. **Derived random variables**: $Y = X^2$, $Z = \mathbb{1}_{X>5}$ (indicator of high activity), or inter-spike intervals $T$.
    2. **Joint distributions**: $(X, X_{t-1})$ to capture temporal correlation.
    3. **Functional transformations**: $f(X)$ that may encode energy, synchrony, or other network-level properties.

Take a case of a random:

- The default attractor is: *“To understand $X$, just look at its probability distribution $P(X)$”*.
- This mental attractor makes it easy to ignore **derived random variables** or **transformations of $X$** that could reveal other aspects of the system.

The cognitive attractor “traps” reasoning into thinking that **only P(X) matters**, even though these derived variables can encode biologically or experimentally relevant information.

### **Neurocognitive Underpinnings**

- **Prefrontal Cortex (PFC) Dysfunction**: Poor executive control impairs error detection, planning, and inhibition of intuitive responses.
- **Amygdala Hijacking**: Emotional arousal overrides cortical reasoning pathways.
- **Dopaminergic Reward Systems**: Reinforce motivated reasoning (seeking "pleasurable" conclusions over truth).

### **Remediation Framework**

Improving thinking requires:

1. **Deliberate Practice**: Training in logic, probabilistic reasoning, and scientific methodology.
2. **Metacognitive Scaffolding**: Checklists (e.g., CONSORT for evidence), pre-mortems, and adversarial collaboration.
3. **Cognitive Forcing Functions**: Algorithms (e.g., Bayesian calculators) to bypass biased intuition.
4. Teach Scientific Reductionism: Isolate variables, test boundary conditions.
5. Train in Counterfactuals: "Would this instance falsify the general rule?”
6. Use Formal Systems: Probability theory, dynamical systems (e.g., "This case is a sample from what distribution?").

## What makes a great thinker?

- A great thinker can **compress** complex ideas into simpler representations `(Kolmogorov complexity)`.
- Their mental models allow for efficient **pattern recognition, abstraction, and generalization** across domains.
- They exhibit **algorithmic efficiency** in problem-solving, minimizing unnecessary steps while maximizing insight.
- **Epistemic Rigor (Information Processing and Justification)**
    - They systematically **verify claims using falsification, Bayesian reasoning, or formal logic**.
    - They distinguish between **empirical, rational, and heuristic** forms of knowledge, avoiding category errors.
    - Furthermore, they construct **coherent and non-trivial axiomatic systems** in their reasoning.
- **Multi-Scale Cognition (Macro and Micro-Level Thinking)**
    - A great thinker can analyze both **low-level implementation details** and **high-level system architecture** of a concept.
    - They demonstrate **recursive depth in their reasoning**, where conclusions feed back into meta-level refinements.
    - Their ability to **zoom in and out** of a problem space suggests a highly adaptable cognitive framework.
- They introduce **high-information-density insights**, meaning their ideas significantly reduce entropy (uncertainty) in a given field.
- They are able to **debug their own cognitive biases**, implementing **epistemic hygiene protocols** (e.g., steelmanning opposing views).
- **Network Effects and Knowledge Graph Centrality**
    - Their ideas serve as **high-connectivity nodes** in conceptual and technological knowledge graphs.
    - They act as **bridge vertices**, connecting previously disjoint intellectual domains.
    - Their influence is measurable via metrics like **citation centrality, cross-disciplinary adoption, and memetic survival over time**.
- **Novelty vs. Optimization Balance**
    - They demonstrate a **Pareto-efficient mix of exploitation (refining existing knowledge) and exploration (pioneering new ideas)**.
    - They navigate **high-dimensional thought spaces**, balancing between local optimization and global paradigm shifts.
    - Furthermore, they effectively generate **counterfactual models**, exploring alternative theoretical frameworks.
- …

## Thinking Framework

> How to solve problems? How to **parse reality**? How to compute answers?
> 

| **Framework** | **Purpose** |
| --- | --- |
| **Critical Thinking** | Analyze arguments logically |
| **Design Thinking** | Human-centered innovation |
| **Systems Thinking** | Understand complex systems holistically |
| **Lateral Thinking** | Generate unconventional ideas |
| **First Principles** | Break problems into fundamental truths |
| **Six Thinking Hats** | Parallel thinking (team collaboration) |
| **Socratic Questioning** | Deepen understanding via questions |
| **5 Whys** | Root-cause analysis |
| **SWOT Analysis** | Strategic planning |
| **PDCA (Plan-Do-Check-Act)** | Continuous improvement |
| **Logical** |  |
| **Probabilistic** |  |
| **Dynamical** |  |
| **Adaptative** |  |
| **Metacognitive** |  |
| **Mathematical** |  |
| **Complexity** |  |
| **Optimization** |  |

## How to improve my thinking?

> Or  Metacognition.
> 

### Reflective Practice

> Observe your own cognition from an external perspective: its capacities, strengths, and limitations. Compare it against other cognitions and observers, and actively seek ways to improve it.
> 

### Continuous Improvement

> All of our thinking tools—representations, operations, and conceptual frameworks—are approximations of ideal forms; they are inherently imperfect.
> 

> As humans, we have certain built-in cognitive capacities. <u>**The effectiveness of our mental tools correlates with the time and effort we invest in improving them.**</u> This applies to mental representations, operational strategies, definitions, and all aspects of thought.
> 

> Ask yourself: how much time have I dedicated to improving this?
> 

> Definitions capture either the mental concepts of the observer or aspects of the world itself. Crafting strong definitions requires intentionality. Definitions act as key thinking tokens, essential for structuring thought. Therefore, we must continuously re-evaluate our concepts and definitions to refine our understanding.
> 

### **Recursive Corruption Errors**

- **🕳️** **The Invisible Bootstrapping Problem**: Assuming your current tools for detecting biases are themselves unbiased *(e.g., "I used logic to confirm that logic is reliable")*
- **♟️** **The Chessmaster’s Trap**: Believing you’ve escaped a cognitive flaw while still being governed by its higher-order version *(e.g., "I’m not biased—I’ve learned about biases!" while failing to notice deeper biases in your anti-bias framework)*
- **🌀** **The Anti-Heuristic Heuristic**: Over-optimizing against one class of errors while silently amplifying others *(e.g., avoiding confirmation bias so aggressively that you reject all consensus knowledge)*

### **Epistemic Self-Sabotage**

- **📉** **The Metacognition Paradox**: The more you introspect about your thinking, the more you alter (and often distort) the original process *(like a quantum observer effect for cognition)*
- **⚡** **The Lightning-Proof Lamppost**: Only checking for errors where your current tools can see them *(e.g., statisticians finding only statistically detectable flaws while missing structural ones)*
- **🌐** **The Framework Prison**: Your flaw-detection system is blind to flaws that would require dismantling the system itself *(e.g., scientific method struggles to detect paradigm-induced blindness)*

### **Anti-Insight Mechanisms**

- **💀** **The Dead Man’s Switch of Beliefs**: Your mind automatically generates defenses against threats to your core error-detection frameworks *(e.g., dismissing critiques of rationality as "postmodern nonsense")*
- **🎭** **The Masked Ball Problem**: Every layer of meta-cognition adds new disguises for old flaws *(e.g., "I’m aware of motivated reasoning" becoming a new motivation to dismiss challenges)*
- **📜** **The Infinite Regress of Doubt**: Applying skepticism to your skepticism tools until all cognition paralyzes *(e.g., "How do I know my anti-bias techniques aren’t biased?")*

### **Systemic Blindness Generators**

- **🌪️** **The Self-Immunizing Fallacy**: Flaws that evolve to resist detection *(e.g., conspiracy theories interpreting counter-evidence as proof of their truth)*
- **⚖️** **The Gravity of the Discarded**: The more flaws you fix, the heavier the remaining distortions become *(like error concentration in scientific fields after "easy" problems are solved)*
- **🧩** **The Mosaic Illusion**: Correctly identifying many small flaws while missing the emergent large flaw they compose *(e.g., spotting logical fallacies in an argument but missing its fundamental ontological error)*

### **Meta-Meta Traps**

- **🎯** **The Ouroboros Standard**: Judging your error-correction methods by the very thinking they’re meant to correct *(e.g., "My intuition confirms my intuition-checking method works")*
- **🚪** **The Hofstadter-Turing Threshold**: Beyond a certain complexity, your flaw-detection system cannot model its own flaws without contradiction *(like Gödel’s incompleteness for cognition)*
- **🌑** **The Black Hole Bias**: Some flaws distort your perception so fundamentally that their existence becomes unfalsifiable within your framework *(e.g., a fish cannot discover "water")*

### Mental Pass, Formal Pass

> Start by visualizing the solution in your mind. Since working memory is limited, this forces you to simplify the problem and focus on its core elements. Then, formalize and externalize your thoughts—write them down or express them clearly—to check their validity and progressively refine their structure and precision.
> 

### **Analogical Reasoning**

> Applying insights from one domain to another (e.g., comparing electrical circuits to water flow).
> 

### **Schema Construction**

> Building mental frameworks to organize related concepts (e.g., in physics or math).
> 

### Mental Model

> …
> 

### **Externalization**

> Drawing, writing, or speaking thoughts to reduce cognitive load.
> 

### **Problem Decomposition**

> Break a complex problem into smaller, manageable parts.
> 

### **Chunking**

> Group individual elements into meaningful units (great for memory and learning).
> 

### **Layered Abstraction**

> Think at multiple levels of abstraction—zoom in and out.
> 

## Layered Model-Based Diagnosis

> *Layered Model-Based Diagnosis* is a systematic approach to identifying, analyzing, and resolving problems within complex systems by leveraging structured models that represent the system at multiple hierarchical or functional layers. Each layer encapsulates specific aspects—such as physical components, processes, organizational roles, or strategic decisions—allowing targeted diagnosis through the interaction and dependencies across these layers.
> 

## References

- [Formal System](https://app.notion.com/p/Formal-System-41d02881d0544314b0e7ad3e6ada608a?pvs=21)
- [Cognitive Bias](https://app.notion.com/p/Cognitive-Bias-d73ded9c25094efd90bac7529abf6f2a?pvs=21)
- [Reason](https://app.notion.com/p/Reason-1ccc0f5171ec80d2a7f0f5653e9ba297?pvs=21)
- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Thinking](https://app.notion.com/p/Thinking-0a566bbc19ce415ebbc2a38d4b50428b?pvs=21)
- 
- [System](https://app.notion.com/p/System-1dac0f5171ec80c38c08f74d095235a9?pvs=21)
- https://es.wikipedia.org/wiki/Sofista
- [A Guide to Study](/view.html?p=notes/personal/a-guide-to-study.md)
- 
- [A Guide to Language and Cognition](/view.html?p=notes/personal/a-guide-to-language-and-cognition.md)
- [A Guide to Building Knowledge Forest](/view.html?p=notes/personal/a-guide-to-building-knowledge-forest.md)
- [A Guide to Mathematical Problem-Solving](/view.html?p=notes/personal/a-guide-to-mathematical-problem-solving.md)
- https://www.johndcook.com/blog/2020/10/04/why-a-little-knowledge-is-a-dangerous-thing/
- [**A Guide to Improving Computational Systems in a Principled Way**](/view.html?p=notes/personal/a-guide-to-improving-computational-systems-in-a-pr.md)
