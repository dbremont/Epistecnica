---
tags: [note, representation, process, workflow, bpmn]
---

# Process-Oriented Representation

> A **process-oriented representation** represents work as a **process**: a set of activities, the transitions that order them, the state the execution carries, and the events and conditions that gate the next step. Where a data representation answers *what is this value*, a process representation answers *what happens next, and under what condition*.

> The representation is the part the engine does not invent. A workflow engine — BPMN in [Camunda](/view.html?p=notes/technica/general/camunda.md), code in [Temporal](/view.html?p=notes/technica/general/temporal.md), a job net in [Control-M](/view.html?p=notes/technica/general/control-m.md) — is an interpreter for a representation somebody else wrote. Choosing the notation is choosing what the process can say.

## What the representation contains

| Element | What it represents | In BPMN | In code-as-workflow |
| --- | --- | --- | --- |
| **Activity** | A unit of work | Task, sub-process, call activity | A function call, an activity invocation |
| **Transition** | The order | Sequence flow | The next statement |
| **Gateway** | A branch or a merge | Exclusive, inclusive, parallel, event-based | `if`, `switch`, parallel branches |
| **Event** | A trigger or a signal | Start, end, timer, message, signal, error | A signal, a timer, an exception |
| **State** | What the execution carries | Process variables | Local variables in the history |
| **Actor** | Who performs the step | Lane, user task | A worker, a human task queue |

## The notations

| Notation | Shape | What it is good at | What it costs |
| --- | --- | --- | --- |
| **BPMN 2.0** | A diagram of activities, gateways and events | Readable by business and executable by the engine; a governance artefact | The model is the source of truth, so model and code drift apart if the engine is embedded |
| **Workflow-as-code** | The program itself | Arbitrary logic, tests, the developer's tools | Determinism constraints, and the process is only readable by programmers |
| **State machine** | States and transitions | Explicit state, simple reasoning about legal transitions | The state space explodes for concurrent work |
| **DAG / job net** | A dependency graph | Batch scheduling across an estate; the graph is data | No human steps, no long-lived state beyond the run |
| **Petri net** | Places, transitions, tokens | Formal analysis of concurrency and soundness | Rarely the operational notation |

## Why the representation matters

> Three consequences follow from taking the representation seriously.
>
> **The engine's capability is the notation's capability.** A BPMN engine cannot express what the notation cannot draw; a code-first engine can express anything, at the cost of a process that is not readable as a diagram. This is the real difference between [Camunda](/view.html?p=notes/technica/general/camunda.md) and [Temporal](/view.html?p=notes/technica/general/temporal.md), not the runtime.
>
> **The representation is the audit record.** The instance history — which activity ran, when, with which variables — is a process representation frozen in time. That is why the workflow engine is also a compliance artefact.
>
> **Versioning is representational.** Changing a process while instances are running means keeping the old representation interpretable. Every engine solves this differently, and it is the hardest operational problem in the family.

## Where it sits

> The process representation is the *what* of the [work execution system](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md), whose engines are the *how*. It is the dynamic counterpart of the data representations in this shelf: the same shelf answers how values are stored, this note answers how work is ordered. [Business Process Engine](/view.html?p=notes/technica/computation/enterprise-information-system-eis/business-process-engine.md) reads the same object as an EIS component.

## References

- [BPMN 2.0 specification](https://www.omg.org/spec/BPMN/)
- [Workflow patterns](http://www.workflowpatterns.com/) — the catalogue of what a process notation can express
- [Work Execution System](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md) — the engines that execute the representation
- [Business Process Engine](/view.html?p=notes/technica/computation/enterprise-information-system-eis/business-process-engine.md) — the engine as an EIS component
- [Workflow](/view.html?p=notes/technica/computation/language-system/workflow.md) — the unit-of-computation reading
- [Camunda](/view.html?p=notes/technica/general/camunda.md) · [Temporal](/view.html?p=notes/technica/general/temporal.md) · [Control-M](/view.html?p=notes/technica/general/control-m.md) — three interpreters of three notations
