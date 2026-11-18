---
tags: [note, workflow-engine, durable-execution, temporal, work-execution]
---

# Temporal

> **Temporal** is a durable-execution platform: a workflow is ordinary code, its state is an event-sourced history the server records, and when a worker crashes the workflow is replayed from that history and continues where it stopped. It is the workflow-engine family's answer to the problem of long-running, stateful work that must survive failure.

> The design choice that defines it is **code as the process definition** — no BPMN diagram, no XML graph — with the constraint that the workflow code must be **deterministic**, because the engine reconstructs the state by re-running it against the recorded events. Everything else follows from that constraint: activities isolate the non-deterministic calls, versioning exists to keep the replay consistent across deployments, and the history is the source of truth.

## The model

| Concept | What it is |
| --- | --- |
| **Workflow** | A deterministic function; its state is the history of the events it has seen |
| **Activity** | A non-deterministic unit of work — an API call, a database write, a file transfer — executed by a worker and recorded |
| **Worker** | A process running the SDK, polling a task queue, executing workflows and activities |
| **Task queue** | The routing name that binds a worker to the work it can execute |
| **History** | The event log the server persists: the workflow's durable state |
| **Timer, signal, query** | First-class primitives for waiting, for external input and for inspection |

## The server

| Service | Job |
| --- | --- |
| **Frontend** | The API gateway for the SDKs and the workers |
| **History** | The event-sourced state store and the workflow's orchestration |
| **Matching** | Dispatches tasks to the workers polling a task queue |
| **Worker service** | Runs the internal system workflows |
| **Persistence** | The database (Cassandra, PostgreSQL, MySQL) that holds the history and the visibility records |

## The properties that matter

| Property | Consequence |
| --- | --- |
| **Durable execution** | A workflow survives process, node and cluster failure without a checkpoint written by the developer |
| **Determinism** | Replay reconstructs state — and forbids random, clock, I/O and unordered iteration in workflow code |
| **Activities** | The side effects are isolated, retried and recorded, so a failure is a retry, not a lost step |
| **Timers and signals** | Long waits and external events are part of the workflow, not a polling job |
| **Versioning** | Code changes must keep old histories replayable — the platform's real operational discipline |

## Where it sits

> Temporal is a **workflow engine**: the unit is the process instance, the state is the history, and the coordination is the point. It is not a task queue (the queue is inside it) and not a background-job system (a job is a single activity). The nearest neighbours are [Camunda](/view.html?p=notes/technica/general/camunda.md), which executes BPMN instead of code, and the scheduling and queueing tools that Temporal replaces rather than composes with.

## References

- [Temporal](https://github.com/temporalio/temporal) — the server repository
- [Temporal documentation](https://docs.temporal.io/)
- [Work Execution System](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md) — the family this tool belongs to
- [Camunda](/view.html?p=notes/technica/general/camunda.md) — the BPMN-based workflow engine
- [Process-Oriented Representation](/view.html?p=notes/technica/computation/representation/process-oriented-representation.md) — what a workflow is a representation of
- [Business Process Engine](/view.html?p=notes/technica/computation/enterprise-information-system-eis/business-process-engine.md) — the engine read as an EIS component
