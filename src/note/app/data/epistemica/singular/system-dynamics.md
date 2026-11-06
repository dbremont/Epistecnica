# System Dynamics


> In this note we will explore **‘System Dynamics’** - as in epistemic not as an ontic aspect.
> 

> **Note:** This should not be confused with the ontological aspect — **dynamics of systems or change in systems**. This is just one epistemic approach model that aspect.
> 

> **System Dynamics**" is arguably an **unfortunate name,** as it invites ambiguity: does it refer to the actual dynamics of systems, or to the epistemic framework developed by **Jay Forrester**?
> 

TODO:

- Create some simulations: https://chat.z.ai/s/cb890f12-77ab-44d5-8dbf-18782eb0f05f - here https://github.com/dbremont/algorithms

## What kind of epistemic element(s) best capture System Dynamics?

| **Epistemic Element** | **Does System Dynamics fit?** | **Why** |
| --- | --- | --- |
| **Epistemic Framework** | **★★★★★ Primary** | It is a conceptual and formal framework for understanding systems through feedback loops, stocks, flows, delays, and nonlinear dynamics. It structures inquiry. |
| **Epistemic Strategy** | ★★★★☆ | It recommends a way of investigating problems: model the whole system, identify feedback, simulate behavior over time, test interventions. |
| **Epistemic Principle** | ★★★☆☆ | It embodies principles like "structure drives behavior", "feedback matters", "behavior emerges from interactions", "dynamic complexity over event thinking". |
| **Epistemic Representation Form** | ★★★☆☆ | It introduces abstract representational forms such as stock-and-flow diagrams and causal loop diagrams. |
| **Epistemic Operator** | ★★★☆☆ | Simulation, sensitivity analysis, parameter estimation, policy testing are operators used within System Dynamics. |
| **Epistemic Process** | ★★★☆☆ | Practitioners follow an iterative modeling process: conceptualize → formulate → calibrate → validate → simulate → revise. |

## How should I make sense of *System Dynamics*? How should I conceptualize it and bring it into an intelligible form?

> System Dynamics should be conceived as an epistemic framework for representing, reasoning about, and experimenting with the dynamic behavior of systems. Rather than focusing on isolated events, it seeks to explain how the underlying structure of a system generates patterns of behavior over time through feedback loops, accumulations (stocks), flows, delays, and nonlinear interactions.
> 

### What is the role of `System Dynamics`?

> The role of System Dynamics is to provide an epistemic framework for understanding, explaining, predicting, and experimenting with the dynamic behavior of systems. It makes the causal mechanisms that generate patterns of behavior over time explicit by representing systems in terms of stocks, flows, feedback loops, delays, and nonlinear interactions.
> 

| Epistemic Function | Role of System Dynamics |
| --- | --- |
| **Representation** | Represents the causal structure of dynamic systems. |
| **Explanation** | Explains how system structure generates observed behavior over time. |
| **Prediction** | Anticipates the consequences of structural changes and policies through simulation. |
| **Experimentation** | Enables safe "what-if" experiments without modifying the real system. |
| **Policy Design** | Helps identify interventions that improve long-term system behavior. |
| **Communication** | Provides a common language for discussing dynamic complexity among stakeholders. |

### What is the structure of the framework?

> A good way to organize this is to distinguish the **structural primitives** (what the framework is built from) from the **procedural steps** (how it is applied). Since you're asking for the *structure of the framework*, focus on the former.
> 

| **Category** | **Element** | **Description** | **Role** |
| --- | --- | --- | --- |
| **Structural Primitive** | Stocks | Quantities that accumulate over time. | Represent the system's state. |
| **Structural Primitive** | Flows | Rates that increase or decrease stocks. | Produce change over time. |
| **Structural Primitive** | Feedback Loops | Circular causal relationships. | Generate dynamic behavior. |
| **Structural Primitive** | Delays | Time lags between cause and effect. | Introduce inertia and oscillation. |
| **Structural Primitive** | Auxiliary Variables | Intermediate computational variables. | Express supporting causal relationships. |
| **Structural Primitive** | Parameters | Fixed constants defining the model. | Configure assumptions and behavior. |
| **Structural Primitive** | Decision Rules | Equations or policies governing flows. | Specify how the system responds. |
| **Structural Primitive** | Nonlinear Relationships | Non-proportional causal relationships. | Capture complex dynamics. |
| **Representation** | Causal Loop Diagrams | Qualitative causal diagrams. | Communicate and reason about feedback structure. |
| **Representation** | Stock-and-Flow Diagrams | Formal structural diagrams. | Specify the simulation model. |
| **Computational Artifact** | Simulation Model | Executable mathematical model. | Compute system behavior over time. |
| **Analytical Procedure** | Simulation | Execute the model through time. | Explore system behavior. |
| **Analytical Procedure** | Sensitivity Analysis | Vary parameters systematically. | Assess robustness and uncertainty. |
| **Analytical Procedure** | Policy Analysis | Compare alternative interventions. | Evaluate candidate policies. |

## Which are the limits of `System Dynamics`?

> System Dynamics **is not a general theory of all dynamic phenomena**. It is an epistemic framework that is particularly well suited for systems whose behavior is driven by accumulations, feedback loops, delays, and continuous change. Outside this domain, its explanatory power decreases.
> 

| Limitation | Explanation |
| --- | --- |
| **Aggregate representation** | System Dynamics typically models populations, resources, or aggregate quantities rather than individual entities. It abstracts away heterogeneous actors. |
| **Weak representation of autonomous agents** | It has limited ability to represent agents with distinct beliefs, goals, learning processes, and adaptive behaviors. Agent-Based Modeling is often better suited for such systems. |
| **Limited treatment of discrete events** | Although discrete events can sometimes be approximated, frameworks such as Discrete-Event Simulation represent event-driven systems more naturally. |
| **Model-dependent** | The quality of conclusions depends entirely on the quality of the causal model. Missing variables, incorrect feedback loops, or unrealistic assumptions can produce misleading results. |
| **Difficult parameter estimation** | Many parameters are difficult to observe or estimate empirically, making calibration challenging. |
| **Structural uncertainty** | Multiple plausible causal structures may explain the same observed behavior, making model selection difficult. |
| **High abstraction** | Important local mechanisms or individual-level interactions may disappear when aggregated into stocks and flows. |
| **Not a discovery mechanism** | System Dynamics does not automatically discover causal structure; the modeler must hypothesize and construct it. |
| **Computational, not empirical** | Simulation explores the consequences of assumptions but does not itself establish that those assumptions are true. Experimental or observational evidence is still required. |

## Which other epistemic elements compete with `System Dynamics`?

> Which other epistemic frameworks compete with or complement System Dynamics for understanding dynamic systems?
> 

> Note:  This frameworks - can be combined with **‘System Dynamics’**.
> 

| Framework | Primary focus |
| --- | --- |
| Control Theory | Regulation, stability, and feedback control of dynamic systems. |
| Dynamical Systems Theory | Mathematical analysis of continuous and discrete dynamical systems. |
| Agent-Based Modeling (ABM) | Emergent system behavior arising from interactions among autonomous agents. |
| Discrete-Event Simulation | Systems whose state changes at discrete events in time. |
| Network Science | Dynamic behavior emerging from network topology and interactions. |
| Operations Research | Optimization and decision-making under constraints. |
| Cybernetics | Communication, regulation, control, and adaptation in systems. |
| Viable System Model (VSM) | Organizational viability through recursive management and regulation. |
| State-Space Modeling | Representing system dynamics using state variables and differential or difference equations. |
| Markov Models | Systems characterized by probabilistic state transitions. |
| Petri Nets | Concurrency, synchronization, and event-driven dynamics. |

## How to used the framework?

### Does the framework is more for simulation? Or for analytical (symbolic) representations?

> System Dynamics is fundamentally a simulation-oriented framework, but it uses symbolic representations as an intermediate step.
> 

### How the workflow looks like?

```jsx
Real Dynamic System
          │
          ▼
Conceptual Model
          │
          ▼
Causal Loop Diagram (symbolic)
          │
          ▼
Stock-and-Flow Diagram (symbolic)
          │
          ▼
Mathematical Model (differential/difference equations)
          │
          ▼
Simulation
          │
          ▼
Behavior over Time
          │
          ▼
Analysis & Policy Design
```

## **Which have been some of the successful applications of the framework?**

> System Dynamics has been successfully applied to problems characterized by feedback, accumulation, delays, and long-term policy effects. Some of its most influential applications include:
> 

| **Domain** | **Application** | **Contribution** |
| --- | --- | --- |
| **Industrial Management** | Production, inventory, and supply chain management | Helped explain production oscillations, inventory instability, and the effects of feedback delays. |
| **Business Strategy** | Organizational growth and competitive dynamics | Supported strategic planning by modeling market growth, resource constraints, and competitive feedback. |
| **Urban Planning** | Urban development and infrastructure | Analyzed long-term interactions among housing, transportation, employment, and population growth. |
| **Public Policy** | Healthcare, education, taxation, and regulation | Evaluated the long-term consequences of alternative public policies before implementation. |
| **Environmental Systems** | Resource management and sustainability | Modeled interactions among population, natural resources, pollution, and economic development. |
| **Climate Change** | Carbon cycles and mitigation policies | Explored the long-term effects of emissions, feedback mechanisms, and climate interventions. |
| **Healthcare Systems** | Disease dynamics and hospital capacity | Assisted in planning healthcare resources and understanding systemic effects of policy decisions. |
| **Project Management** | Large engineering and software projects | Modeled schedule pressure, workforce dynamics, productivity, and rework cycles. |
| **Economics** | Macroeconomic and regional economic systems | Investigated economic growth, investment, employment, and business cycles through feedback structures. |
| **Defense and Security** | Logistics and strategic planning | Supported analysis of resource allocation, logistics, and long-term operational planning. |

## References

- [Philosophia Naturalis](https://app.notion.com/p/Philosophia-Naturalis-32ac0f5171ec807b9388c870ab664abf?pvs=21)
- https://en.wikipedia.org/wiki/System_dynamics
- https://en.wikipedia.org/wiki/Dynamic_simulation
- https://www.youtube.com/watch?v=XL_lOoomRTA&t=1348s
- https://www.youtube.com/watch?v=G1mVnqdlpvo
- https://www.youtube.com/watch?v=ddmygPTRjc0
