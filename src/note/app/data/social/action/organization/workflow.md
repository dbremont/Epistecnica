---
tags: [workflow, organization, action, social-element]
---

# Workflow

> **Workflow** is the defined sequence of steps routing work among actors and roles — the organization form that turns a repeated doing into a repeatable route: who does what next, on which trigger, under which rule, into which state.

## Formulation

### What social element type does this social instance belong to?

**Workflow belongs to the `Workflow` social element type (Action category, `Action Organization` branch, Synontic layer)** — a defined route existing through the shared recognition of its actors. It is distinct from `Process / Event` (a temporally extended transformation), from `Plan` (a one-off arrangement it may repeat), and from `Interaction Pattern` (a recurring sequence it may formalize).

### What is this social instance?

> The routed doing: a trigger starting it, steps ordered, actors and roles named, a routing rule deciding each next move, and states marking progress. Workflows decompose into their kinds and their anatomy; the route is the instance, the repeatability the form.

### What is the recursive instance decomposition of this social instance?

> Boundary: one organization family, decomposed at middle depth — kinds and anatomy only.
>
> Stopping rule: a row is terminal when it names a workflow kind or an anatomy element.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| Workflow `(→ Part)` Workflow | Defined sequence of steps routing work among actors and roles. |
| Workflow `(→ Part)` Workflow `(→ Kind)` Approval Workflow | Route moving a request through authorizations to decision. |
| Workflow `(→ Part)` Workflow `(→ Kind)` Clinical Workflow | Route moving a patient through assessment, treatment, and follow-up. |
| Workflow `(→ Part)` Workflow `(→ Kind)` Manufacturing Workflow | Route moving material through transformation to finished good. |
| Workflow `(→ Part)` Workflow `(→ Kind)` Software Workflow | Route moving code through review, test, and release. |
| Workflow `(→ Part)` Workflow `(→ Part)` Process / Event | Grouping: the start of the route. |
| Workflow `(→ Part)` Workflow `(→ Part)` Process / Event `(→ Part)` Workflow Trigger | Occurrence starting a run of the route. |
| Workflow `(→ Part)` Workflow `(→ Part)` `Social Action` | Grouping: the doings the route orders. |
| Workflow `(→ Part)` Workflow `(→ Part)` `Social Action` `(→ Part)` Workflow Step | Causally efficacious event placed at one station of the route. |
| Workflow `(→ Part)` Workflow `(→ Component)` Social Role | Grouping: the stations of the route. |
| Workflow `(→ Part)` Workflow `(→ Component)` Social Role `(→ Component)` Step Actor | Expectation that a named role performs its station's step. |
| Workflow `(→ Part)` Workflow `(→ Component)` Norm / Regulation | Grouping: the decisions the route makes. |
| Workflow `(→ Part)` Workflow `(→ Component)` Norm / Regulation `(→ Component)` Routing Rule | Shared protocol deciding each next station from the current state. |
| Workflow `(→ Part)` Workflow `(→ Part)` State | Grouping: the progress the route marks. |
| Workflow `(→ Part)` Workflow `(→ Part)` State `(→ Kind)` Workflow State | Snapshot of a run at one station of the route. |

## References

- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [Plan](note.html?n=social/action/organization/plan.md) (the arrangement a workflow repeats)
- [Project](note.html?n=social/action/organization/project.md) (the effort a workflow may serve)
