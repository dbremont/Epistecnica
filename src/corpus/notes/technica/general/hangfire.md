---
tags: [note, background-jobs, dotnet, hangfire, work-execution]
---

# Hangfire

> **Hangfire** is a background-job framework for .NET: a method call is enqueued as a job, persisted in a database (SQL Server, PostgreSQL, Redis, and others), and executed later by a worker — reliably, with retries, and with a dashboard that shows what is queued, running, succeeded and failed.

> It is the .NET answer to the same problem [JobRunr](/view.html?p=notes/technica/general/jobrunr.md) solves on the JVM: the web request returns fast, the work continues, and the state of the work is a durable record rather than an in-memory task. Where Hangfire differs is the tight ASP.NET integration and the batteries-included dashboard.

## The job types

| Type | What it does |
| --- | --- |
| **Fire-and-forget** | Enqueue once and execute as soon as a worker is free |
| **Delayed** | Execute at a specified future time |
| **Recurring** | Execute on a cron schedule — the embedded scheduler |
| **Continuation** | Execute after a parent job succeeds or fails |

## The properties that matter

| Property | Consequence |
| --- | --- |
| **Persistent storage** | A job survives a process restart; the database is the source of truth |
| **Automatic retries** | A failed job is retried with a backoff, and the attempts are visible |
| **Dashboard** | The operational surface: queues, running jobs, history, manual retry |
| **Distributed workers** | Several servers process the same store, so throughput scales horizontally |
| **Filters** | Cross-cutting hooks for logging, metrics, tenant context and authorisation |

## Where it sits

> Hangfire is a **background-job processing** system with a scheduler inside it. It is not a workflow engine: chaining is limited to continuations, and a long-running, stateful process with human tasks and gateways belongs to [Camunda](/view.html?p=notes/technica/general/camunda.md) or [Temporal](/view.html?p=notes/technica/general/temporal.md). The distinction is the one the [work execution system](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md) note draws between a job and a process instance.

## References

- [Hangfire](https://www.hangfire.io/)
- [Hangfire on GitHub](https://github.com/HangfireIO/Hangfire)
- [Work Execution System](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md) — the family this tool belongs to
- [Quartz](/view.html?p=notes/technica/general/quartz.md) — the scheduler-only alternative on the JVM side
- [JobRunr](/view.html?p=notes/technica/general/jobrunr.md) — the JVM counterpart
