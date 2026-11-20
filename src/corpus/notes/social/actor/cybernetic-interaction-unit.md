---
tags: [note, social, actor, social-element, interaction-unit, cybernetics, artificial-agent]
---

# Cybernetic Interaction Unit

> A **Cybernetic Interaction Unit** is a bounded artificial system capable of interaction: it measures its environment, decides on a course, and acts on it. Its agency is designed and delegated, not grown.

It is the artificial kind of [Interaction Unit](/view.html?p=notes/social/actor/interaction-unit.md) — the counterpart of the [Human](/view.html?p=notes/social/actor/human.md) in the actor typology. The unit is a *control loop* made into an actor: a sensor reads a state, a controller compares it to a reference and selects an action, an actuator changes the world, and the change feeds back into the next reading. What makes it one unit is the closed loop, not the parts.

## The loop

| Element | Function | What fails without it |
| --- | --- | --- |
| **Sensor** | Registers the environment or the unit's own state | The unit is blind: it acts without knowing the result |
| **Controller** | Compares the reading to a reference and selects the action | The unit has a signal but no decision |
| **Actuator** | Acts on the world | The decision never leaves the unit |
| **Reference** | The state or objective the unit is set to pursue | There is no error, so nothing to correct |
| **Feedback** | The consequence, returned as the next reading | The loop is open: errors accumulate uncorrected |
| **Boundary** | What is inside the unit and what it acts upon | The unit dissolves into its environment |

The technical detail of the loop is the [Control System](/view.html?p=notes/technica/cybernetics/control-system.md); the machine-intelligence version — a model that infers, predicts, acts and updates — is the [Active Inference System](/view.html?p=notes/technica/cybernetics/ais.md).

## Kinds

- **Software agent** — a process that perceives its information environment, decides, and acts through interfaces; the [Agent](/view.html?p=notes/epistemica/singular/agent.md) of the simulation and multi-agent literature.
- **Robot** — a physical unit with sensors, actuators and a body, acting in a shared space.
- **Control system** — an embedded unit regulating a plant: thermostats, autopilots, industrial controllers.
- **Machine-intelligence system** — a unit whose controller is a trained model, with inference, memory, planning and tool use wrapped around it.

## Agency and accountability

A cybernetic unit has **delegated agency**: the intention it pursues is set by whoever designs, configures or instructs it, and its autonomy is a matter of degree — from a thermostat's fixed rule to a system that selects its own subgoals. That delegation is what makes it socially legible: the unit acts, but the *accountability* for the action runs back along the delegation chain to a person or an organization.

The social question is therefore not whether the unit is conscious but whether it is **recognized as an actor**: who deployed it, who can stop it, and who answers when it acts. A unit with no answerable principal is not an actor but an accident waiting to be attributed.

## Decomposition

> Boundary: one generic cybernetic unit — the loop, its parts, and its kinds. The technologies that realize it are linked, not decomposed here.
>
> Stopping rule: a row is terminal when it names a part, a kind, or an agency element.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit | Bounded artificial system capable of sensing, deciding and acting. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Part)` Sensor | Interface registering the environment or the unit's state. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Part)` Controller | Decision element comparing the reading to a reference. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Part)` Actuator | Element that acts on the world. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Part)` Feedback Loop | The return of the consequence as the next reading. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Part)` Boundary | The interface separating the unit from what it acts upon. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Kind)` Software Agent | Process acting through information interfaces. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Kind)` Robot | Embodied unit acting in a shared physical space. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Kind)` Control System | Embedded unit regulating a plant. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Kind)` Machine-Intelligence System | Unit whose controller is a trained model. |
| `Interaction Unit` `(→ Part)` Cybernetic Interaction Unit `(→ Part)` Delegated Agency | The designed intention the unit pursues, set by its principal. |

## Read it with

- [Actor](/view.html?p=notes/social/actor/actor.md) — the typology the unit joins.
- [Interaction Unit](/view.html?p=notes/social/actor/interaction-unit.md) — the grammar root.
- [Human](/view.html?p=notes/social/actor/human.md) — the biological counterpart.
- [Control System](/view.html?p=notes/technica/cybernetics/control-system.md) — the technical loop.
- [Active Inference System](/view.html?p=notes/technica/cybernetics/ais.md) — the machine-intelligence realization.
- [Agent](/view.html?p=notes/epistemica/singular/agent.md) — the simulation and multi-agent reading.

## References

- Wiener, N. (1948). *Cybernetics: Or control and communication in the animal and the machine*. MIT Press.
- Ashby, W. R. (1956). *An introduction to cybernetics*. Chapman & Hall.
- Simon, H. A. (1969). *The sciences of the artificial*. MIT Press.
- Beer, S. (1972). *Brain of the firm*. Allen Lane.
- von Foerster, H. (1981). *Observing systems*. Intersystems Publications.
- Russell, S., & Norvig, P. (2020). *Artificial intelligence: A modern approach* (4th ed.). Pearson.
- Wooldridge, M. (2009). *An introduction to multiagent systems* (2nd ed.). Wiley.
- Floridi, L., & Sanders, J. W. (2004). On the morality of artificial agents. *Minds and Machines*, 14(3), 349–379.
