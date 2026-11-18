---
tags: [note, scheduling, jvm, quartz, work-execution]
---

# Quartz

> **Quartz** is a job scheduler for the JVM: a `Job` is a unit of work, a `Trigger` says when it fires, and a `Scheduler` binds the two and executes the job on a thread pool. It is the pure case of the scheduler family — it fires work and does not try to run a process.

> Its place in the stack is the clock. An application that needs "run this every night at 02:00" or "fire once at a date" embeds Quartz; a background-job system such as [JobRunr](/view.html?p=notes/technica/general/jobrunr.md) or [Hangfire](/view.html?p=notes/technica/general/hangfire.md) usually embeds a scheduler of the same kind to handle its recurring jobs.

## The model

| Object | What it is |
| --- | --- |
| **Job** | The unit of work — a class implementing `execute`, stateless in itself |
| **JobDetail** | The instance definition: the job class, its identity, its data |
| **Trigger** | When to fire: a `SimpleTrigger` (interval) or a `CronTrigger` (calendar expression) |
| **Scheduler** | The registry that binds jobs to triggers and dispatches them |
| **JobStore** | Where the schedule lives — in memory (`RAMJobStore`) or in a database (`JobStoreTX`) |

## The properties that matter

| Property | Consequence |
| --- | --- |
| **Cron triggers** | Full calendar expressions, including day-of-week and day-of-month |
| **Persistent job store** | The schedule survives a restart; the database becomes the source of truth |
| **Clustering** | Several instances share the store and coordinate firing, so a job fires once, not once per node |
| **Misfire policy** | What to do when the scheduler was down at the fire time — fire now, fire once, skip |
| **Thread pool** | The execution capacity; the scheduler does not own the workload |

## What it does not do

> Quartz does not retry a failed job, does not keep a durable record of the attempts, does not expose a dashboard, and does not chain jobs into a process. Those are the responsibilities of the background-job systems and the workflow engines above it. Using Quartz for a long-running process is the classic category error: the schedule is fine, the execution semantics are missing.

## References

- [Quartz Scheduler](https://www.quartz-scheduler.org/)
- [Quartz on GitHub](https://github.com/quartz-scheduler/quartz)
- [Work Execution System](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md) — the family this tool belongs to
- [Hangfire](/view.html?p=notes/technica/general/hangfire.md) · [JobRunr](/view.html?p=notes/technica/general/jobrunr.md) — the background-job systems that embed a scheduler
