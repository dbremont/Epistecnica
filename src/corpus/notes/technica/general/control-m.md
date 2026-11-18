---
tags: [note, workload-automation, batch, control-m, work-execution]
---

# Control-M

> **Control-M** is BMC's enterprise workload-automation platform: the scheduler of the batch estate. It runs the nightly cycle across mainframe, Unix, Windows, SAP, databases and cloud services — thousands of jobs with calendars, dependencies, resource requirements and an operations console that shows the state of the whole plan.

> Its unit is not the job but the **job net**: the dependency graph of the night's work, with the conditions that must hold before each job runs. That is the difference between a scheduler and workload automation — the scheduler knows the time, the automation platform knows the *order and the conditions* of an estate.

## The model

| Concept | What it is |
| --- | --- |
| **Job** | A unit of work — a script, a program, a database task, an SAP job, a file transfer |
| **Job net / flow** | The dependency graph: which jobs must complete, and under which conditions |
| **Calendar** | The business calendar that decides which days the plan applies to |
| **Condition** | The prerequisite or outcome that gates a job — a file, a job's completion, a resource |
| **Resource** | The capacity a job needs — a tape drive, a server, a licence, an agent |
| **Agent** | The process on each machine that executes the job and reports back |
| **Active Environment** | The operations console: the plan, the jobs, the alerts, the reruns |

## The properties that matter

| Property | Consequence |
| --- | --- |
| **Cross-platform** | One plan spanning z/OS, Unix, Windows, SAP and cloud |
| **Condition-based dependencies** | The graph is data, not code — operations can change it |
| **Calendars** | Business-day logic: month-end, holidays, staggered cycles |
| **Restart and rerun** | A failed job is rerun, and the downstream jobs wait |
| **Audit and SLA** | The run history is an operational and regulatory record |

## Where it sits

> Control-M is **workload automation**: the enterprise-scale orchestration of batch work. It is not a background-job system (it does not live inside an application), not a task queue (it does not transport messages) and not a BPMN engine (it does not model human workflows). It is the operations layer that the whole batch estate reports to, and it coexists with the application-level tools rather than replacing them.

## References

- [Control-M](https://www.bmc.com/it-solutions/control-m.html)
- [Control-M documentation](https://documents.bmc.com/supportu/controlm/)
- [Work Execution System](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md) — the family this tool belongs to
- [Redwood](/view.html?p=notes/technica/general/redwood.md) — the SaaS counterpart in the same family
- [Quartz](/view.html?p=notes/technica/general/quartz.md) — the single-application scheduler, for contrast
