---
tags: [development]
---

# UI/UX

- [User Research](note.html?n=technica/computation/system/interface/ui/conceptual-model-computing-system-interface/user-research.md)

> UX: A multidimensional system property representing the dynamic, contextual, and affective interaction between a user and a system, emergent from the coalescence of cognitive load, usability metrics, interaction feedback loops, perceptual-motor efficiency, and system affordances within a defined task environment.
> 

> **After market  Market Research identifies a problem then  UX/UI do**:  Now that we've identified a real user problem, let's design, test, and refine experiences that solve it meaningfully and intuitively.
> 

## Formulation

**UX** is **not a static attribute** of an interface but a **complex function** `UX(u, s, t, e)` where:

- `u` = user profile (cognitive model, perceptual thresholds, prior experience)
- `s` = system architecture (interaction design, affordance model, feedback mechanisms)
- `t` = task complexity and goal structure
- `e` = environment and device constraints (latency, display, input method)

## Parts

| Component | Description |
| --- | --- |
| **Cognitive Load (CL)** | Measured in bits/sec or using frameworks like NASA-TLX; relates to short-term memory and decision complexity during interaction. |
| **System Affordances** | Perceived actionable properties derived from interface design, mapped to user schema. |
| **Interaction Latency (IL)** | Time between user action and system feedback (measured in ms); directly affects perceived system responsiveness. |
| **Perceptual Feedback Loop** | The sensory feedback mechanism (visual, haptic, auditory) that closes the action-perception-action cycle. |
| **Error Rate (ER)** | Frequency of unintended user actions due to ambiguous affordances or misaligned mental models. |
| **Efficiency** | Time to complete task / optimal time, often represented via Fitts’s Law or Hick’s Law modeling. |
| **Satisfaction** | Quantified via standardized psychometric scales (e.g., SUS, UEQ, AttrakDiff), reflecting hedonic and pragmatic quality dimensions. |

## Formalization in HCI Theory

UX can be situated within **Human-Computer Interaction (HCI)** as a property of **system-user interactions** evaluated along three axes:

1. **Effectiveness (E):** Task completion rate
2. **Efficiency (η):** Time, effort, and cognitive resources expended
3. **Satisfaction (Σ):** Subjective utility and emotional response

Thus:

```
UX = f(E, η, Σ, ER, IL, CL, ENV, CONTEXT)

```

Where:

- `ENV` = execution environment (network, device, screen)
- `CONTEXT` = social, temporal, and operational usage context

## UX Research

> Goal: Design a UI
> 

> 🔹 Tasks: Understand user needs, business goals, and system constraints.
> 

## UX Conceptual Design

> Goal: Define the structural backbone of the system.
> 
- Use Cases
- Task Analysis & User Journey Mapping

## **Interaction Design (IxD)**

> Goal: Define dynamic behavior and affordances.
> 

## Visual Design (UI Design)

> Goal: Create a perceptually clear, aesthetic interface.
> 

## **Prototyping**

> Goal: Test flows and interactions before development.
> 

## Evaluation

> Goal: Evaluate usability and emotional response.
> 

## Specification for Development

> Goal: Ensure correct handoff and implementability.
> 

## References

- https://en.wikipedia.org/wiki/User_experience
- https://en.wikipedia.org/wiki/User_experience_evaluation