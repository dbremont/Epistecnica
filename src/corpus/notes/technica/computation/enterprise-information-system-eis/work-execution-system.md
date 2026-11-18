---
tags: [note, integration, work-execution, job-management, scheduling, workflow]
---

# Work Execution System

> A **work execution system** — the **Job Management System (JMS)** in the operational vocabulary — is the technical set that runs work that is not a user request: it decides *when* a unit of work runs, *where* it runs, *what happens* when it fails, and *how* the units are chained into a process. It is the layer between the application and the clock.

> The five families below are not a ladder of sophistication; they answer different questions. A scheduler answers **when**; a background-job system answers **how a unit of work outlives the request that created it**; a task queue answers **how the work reaches a worker**; a workflow engine answers **what the order of the steps is**; and workload automation answers **how the enterprise's batch estate is orchestrated across platforms**. Most real systems combine three or four of them.

## The Families

| Family | The question it answers | Trigger model | State it holds | Examples |
| --- | --- | --- | --- | --- |
| **Job Scheduler** | When does this job fire? | Calendar, cron, fixed interval | The next fire time; the job definition | Quartz, Hangfire (recurring), Control-M (as part of a plan) |
| **Background Job Processing** | How does work outlive the request? | Enqueue from the application | The job record and its attempts | Hangfire, Sidekiq, Celery, JobRunr |
| **Task Queue** | How does the work reach a worker? | Producer puts a message on a broker | The message, its acknowledgement, its visibility timeout | RabbitMQ, Celery, SQS-style brokers |
| **Workflow Engine** | In what order do the steps run, and what happens on failure? | Process start, message, timer, signal | The process instance and its history | Camunda, Temporal |
| **Workload Automation** | How is the enterprise batch estate orchestrated? | Calendar and dependency nets | The job net, the daily plan, the run history | Control-M, Redwood RunMyJobs |

## Where the boundaries are

> The families overlap in the small and separate in the large.
>
> - A **scheduler** fires a job and forgets it; it does not know whether the job succeeded, and it usually has no retry policy. Quartz is the pure case.
> - A **background-job system** adds the job's durable record, its retries, its dashboard and its worker pool — the unit of work is a method call that survives a restart. Sidekiq, Celery, Hangfire and JobRunr are here, and they usually embed a scheduler for recurring work.
> - A **task queue** is the transport underneath: a broker with acknowledgement and delivery semantics. It is the substrate a background-job system or a workflow engine may use, not a system that decides anything about the work.
> - A **workflow engine** executes a *process definition* — a graph of activities, gateways and events — and keeps the instance state so that a long-running sequence survives crashes, waits and human tasks. Its unit is the process instance, not the job.
> - **Workload automation** is the enterprise-scale case: thousands of jobs across mainframe, Unix, Windows, SAP and cloud, with calendars, dependencies and an operations console. Control-M and Redwood are the products; a scheduler with a database is the toy version.

## The process axis

> The workflow engine and the workload-automation product both execute *processes*, and a process is a representation before it is an execution: the graph of activities, their order, their conditions and their state. That representation is decomposed in [Process-Oriented Representation](/view.html?p=notes/technica/computation/representation/process-oriented-representation.md), and the engine is the thing that interprets it.

## In the integration architecture

> The work execution system is the temporal complement of the [information-systems integration](/view.html?p=notes/technica/computation/enterprise-information-system-eis/information-systems-integration.md) layer: the integration moves data between systems, the execution system moves *work* through time. A nightly export is a scheduled job; a settlement chain is a workflow; a reconciliation sweep across a hundred systems is workload automation.

## References

- [Quartz](/view.html?p=notes/technica/general/quartz.md) · [Hangfire](/view.html?p=notes/technica/general/hangfire.md) · [Temporal](/view.html?p=notes/technica/general/temporal.md) · [Camunda](/view.html?p=notes/technica/general/camunda.md) · [Control-M](/view.html?p=notes/technica/general/control-m.md) · [Redwood](/view.html?p=notes/technica/general/redwood.md) — the tools of the five families
- [JobRunr](/view.html?p=notes/technica/general/jobrunr.md) · [Celery](/view.html?p=notes/technica/general/lib/celery.md) · [Sidekiq](/view.html?p=notes/technica/general/sidekiq.md) · [RabbitMQ](/view.html?p=notes/technica/general/rabbitmq.md) · [Apache Airflow](/view.html?p=notes/technica/general/apache-airflow.md) · [n8n](/view.html?p=notes/technica/general/n8n.md) — the neighbouring tools
- [Business Process Engine](/view.html?p=notes/technica/computation/enterprise-information-system-eis/business-process-engine.md) — the engine read as an EIS component
- [Process-Oriented Representation](/view.html?p=notes/technica/computation/representation/process-oriented-representation.md) — the representation the engines execute
- [Information Systems Integration](/view.html?p=notes/technica/computation/enterprise-information-system-eis/information-systems-integration.md) — the data-side counterpart
