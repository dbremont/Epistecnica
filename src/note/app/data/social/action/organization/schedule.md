---
tags: [schedule, organization, action, social-element]
---

# Schedule

> **Schedule** is the temporal allocation sequencing actions, agents, and resources — the organization form that binds a doing to time: which entry runs in which slot, with what means, toward which milestone, and along which critical path.

## Formulation

### What social element type does this social instance belong to?

**Schedule belongs to the `Schedule` social element type (Action category, `Action Organization` branch, Synontic layer)** — a temporal allocation existing through the shared commitment of its actors to the same time. It is distinct from `Plan` (the arrangement it times), from `State` (a snapshot it may fix), and from `Process / Event` (the run it orders).

### What is this social instance?

> The timed doing: entries listed, slots assigned, resources allocated, milestones fixed, and the critical path declaring which entries govern the whole. Schedules decompose into their kinds and their anatomy; the allocation is the instance, the shared time the form.

### What is the recursive instance decomposition of this social instance?

> Boundary: one organization family, decomposed at middle depth — kinds and anatomy only.
>
> Stopping rule: a row is terminal when it names a schedule kind or an anatomy element.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path is unique.

| Instance Tree Path | Description |
| --- | --- |
| Schedule `(→ Part)` Schedule | Temporal allocation sequencing actions, agents, and resources. |
| Schedule `(→ Part)` Schedule `(→ Kind)` Production Schedule | Allocation sequencing manufacture to capacity and demand. |
| Schedule `(→ Part)` Schedule `(→ Kind)` Project Schedule | Allocation sequencing a bounded effort's work to its deadline. |
| Schedule `(→ Part)` Schedule `(→ Kind)` Transport Schedule | Allocation sequencing carriage to routes and slots. |
| Schedule `(→ Part)` Schedule `(→ Part)` Class Timetable | Allocation sequencing teaching to rooms, teachers, and hours. |
| Schedule `(→ Part)` Schedule `(→ Part)` `Activity` | Grouping: the doings the allocation times. |
| Schedule `(→ Part)` Schedule `(→ Part)` `Activity` `(→ Part)` Scheduled Entry | Coarse bundle of actions placed at one position of the allocation. |
| Schedule `(→ Part)` Schedule `(→ Part)` State | Grouping: the positions the allocation fixes. |
| Schedule `(→ Part)` Schedule `(→ Part)` State `(→ Part)` Time Slot | Bounded interval assigned to an entry. |
| Schedule `(→ Part)` Schedule `(→ Part)` State `(→ Part)` Schedule Milestone | Snapshot at which the timed doing is judged against the allocation. |
| Schedule `(→ Part)` Schedule `(→ Part)` Resource | Grouping: the means the allocation commits. |
| Schedule `(→ Part)` Schedule `(→ Part)` Resource `(→ Part)` Slot Resource Allocation | Assignment of scarce means to an entry in its slot. |
| Schedule `(→ Part)` Schedule `(→ Part)` Process / Event | Grouping: the dependencies the allocation orders. |
| Schedule `(→ Part)` Schedule `(→ Part)` Process / Event `(→ Part)` Critical Path | Succession of entries whose delay delays the whole. |

## References

- [Philosophia Socialium et Operis](note.html?n=meta/philosophia-socialium-et-operis.md)
- [Plan](note.html?n=social/action/organization/plan.md) (the arrangement a schedule times)
- [Project](note.html?n=social/action/organization/project.md) (the effort a project schedule bounds)
