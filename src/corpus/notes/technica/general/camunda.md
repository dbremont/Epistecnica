---
tags: [note, workflow-engine, bpmn, camunda, work-execution]
---

# Camunda

> **Camunda** is a workflow and decision engine built on **BPMN 2.0**: the process is a diagram — tasks, gateways, events, lanes — and the engine executes it, keeping the state of each process instance, the variables it carries, and the history of what happened. It is the graphical, standards-based counterpart to [Temporal](/view.html?p=notes/technica/general/temporal.md)'s code-as-workflow.

> The representation is the product. A BPMN model is readable by the business and executable by the engine, which is why the workflow-engine family in the enterprise is usually a BPMN engine: the diagram is the contract between the people who define the process and the system that runs it.

## The model

| Element | What it is |
| --- | --- |
| **Process definition** | The deployed BPMN model, versioned per deployment |
| **Process instance** | One execution of the definition, with its own state |
| **Task** | A unit of work — service, user, script, business rule, or manual |
| **Gateway** | The branching and merging — exclusive, inclusive, parallel, event-based |
| **Event** | The start, end, timer, message, signal or error boundary |
| **Variable** | The process data carried by the instance, visible to the tasks |
| **External task** | A task the engine hands to an external worker to complete |

## The properties that matter

| Property | Consequence |
| --- | --- |
| **BPMN 2.0** | A standard notation, tool support and a model a non-programmer can read |
| **DMN** | Decision tables as a first-class artefact beside the process |
| **Human tasks** | A task list UI for the steps a person must perform |
| **External tasks** | The engine orchestrates workers without embedding their code |
| **History** | The audit record of every instance, activity and variable change |
| **Camunda 8 / Zeebe** | The distributed, scalable engine; the process is still BPMN |

## Where it sits

> Camunda is a **workflow engine** in the work-execution taxonomy: the unit is the process instance and the state is the engine's. Compared with Temporal it trades determinism-by-code for a standard diagram: BPMN is easier to govern and harder to express arbitrary logic in; Temporal is the reverse. Compared with a background-job system it adds the graph — the order, the gateways, the human steps and the long waits.

## References

- [Camunda](https://camunda.com/)
- [Camunda documentation](https://docs.camunda.io/)
- [BPMN 2.0 specification](https://www.omg.org/spec/BPMN/)
- [Work Execution System](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md) — the family this tool belongs to
- [Temporal](/view.html?p=notes/technica/general/temporal.md) — the code-first workflow engine
- [Business Process Engine](/view.html?p=notes/technica/computation/enterprise-information-system-eis/business-process-engine.md) — the engine read as an EIS component
- [Process-Oriented Representation](/view.html?p=notes/technica/computation/representation/process-oriented-representation.md) — the representation BPMN is one notation for
