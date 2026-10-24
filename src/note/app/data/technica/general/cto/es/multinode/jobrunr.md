# JobRunr

> JobRunr is an embeddable JVM library for durable, distributed background jobs — fire-and-forget, delayed, and recurring — written with plain Java methods.
>

> It is the complement of the request path: the web request returns fast while the `Job` persists as JSON in the application's existing database, is claimed and executed by a `BackgroundJobServer`, retried on failure, and observed in a built-in dashboard.
>

> This note characterizes JobRunr as a full ensemble — jobs, states, scheduler API, server cluster, storage providers, dashboard, filters, framework integrations, and practices (OSS plus a marked Pro sketch) — following the schema in [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md).

## Formulation

### What technical element type does this technical instance belong to?

**JobRunr belongs to the `Constitutive Technical Object` technical element type, readable as a `Technical Element Set`.**

More specifically:

```text
Constitutive Technical Object
└── JobRunr (embeddable background-processing library)
    readable as Technical Element Set (jobs + states + scheduler + server + storage + dashboard + filters + practices)
```

JobRunr is constitutive because it is built to be embedded in an existing application, constituting that application's background-processing subsystem — like a `database schema` or `bearing` in the taxonomy, it is a component of a larger technical object, not a standalone system. A host application *embeds* JobRunr; the scheduler *persists* jobs; a server *claims* and *realizes* them. The deployed ensemble (application + JobRunr + database + dashboard) can additionally be read as a `Production Technical System`. As a coherent body of objects + techniques + knowledge + institutions organized around one capability — durable background work on the JVM — it is also a `Technical Element Set`.

### What is this technical instance?

> JobRunr is a versioned, embeddable JVM library instance (Java 8+, Kotlin; OSS LGPL 3.0 plus commercial Pro) that turns plain Java methods — referenced via lambdas through `BackgroundJob`/`JobScheduler`, or via `JobRequest`/`JobRequestHandler` commands — into persisted, atomically claimed, automatically retried, dashboard-observable background jobs executed by a `BackgroundJobServer` cluster backed by the application's existing SQL or NoSQL database.

Lineage: Ronald Dehuysser, `jobrunr/jobrunr` on GitHub; Java alternative to HangFire (.NET), Sidekiq/Resque/delayed_job (Ruby), Celery (Python); persistent and distributed successor to Quartz and Spring Task Scheduler. Exemplar version in this note: 8.8.1 (`org.jobrunr:jobrunr`).

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one JobRunr-embedded application instance (library v8.x, one database, one server cluster, one dashboard); deployment-specific values appear only in rows marked exemplar.
>
> Stopping rule: a row is terminal when it names a concrete class, annotation, method, job state, database table, endpoint, config attribute, or named actor.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a host application *embeds* JobRunr; the scheduler *persists* a job; a server *claims* and *executes* it; Pro rows are marked `(Pro)`.

| Instance Tree Path | Description |
| --- | --- |
| `Constitutive Technical Object` → JobRunr | Embeddable background-processing library instance plus its server, storage, dashboard, and practices. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` | Grouping: Technical Architecture elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → Coherence (one persisted job, many realizations) | Organizing structure: a single persisted `(root) > Technical Element Set > Technical Architecture` record drives scheduling, claiming, execution, retry, and observation. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → JobRequest pattern | Command/handler separation: `(root) > Technical Element Set > Technical Architecture` carries data, `JobRequestHandler` performs the work. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → JobRequest pattern → `Technical Interface` | Grouping: Technical Interface elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → JobRequest pattern → `Technical Interface` → JobRequest | Interface carrying job data plus `getJobRequestHandler()`. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → JobRequest pattern → `Technical Interface` → BackgroundJobRequest | Static facade offering the same API for `JobRequest`s. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → JobRequest pattern → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → JobRequest pattern → `Technical Mechanism` → JobRequestHandler | `run(request)` implementation performing the work. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → JobRequest pattern → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Architecture` → JobRequest pattern → `Constitutive Technical Object` → JobRequestScheduler | Injectable scheduler for `JobRequest`s. |
| `Constitutive Technical Object` → JobRunr → `Technical Capability` | Grouping: Technical Capability elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Capability` → Realized capability | Capability realized: durable, distributed background work on the JVM with no extra infrastructure. |
| `Constitutive Technical Object` → JobRunr → `Technical Institution` | Grouping: Technical Institution elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Institution` → Governance (author + licenses) | Ronald Dehuysser authorship; `(root) > Technical Element Set > Technical Institution` on GitHub; LGPL 3.0 OSS plus commercial Pro tier. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Distribution (Maven Central) | Versioned artifact `(root) > Technical Element Set > Production Technical System > Production Technical Object > Constitutive Technical Object` consumed via Maven or Gradle (exemplar 8.8.1). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job | Unit of work performed outside the current execution context, with name, signature, details, and state history. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Specification` | Grouping: Technical Specification elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Specification` → JobDetails | Type, method to execute, and arguments extracted from the lambda via ASM and serialized to JSON. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Parameter` → Job name | Human-readable name: `(root) > Technical Element Set > Technical Parameter` value, `JobBuilder` value, or derived default. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Feedback` | Grouping: Technical Feedback elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Feedback` → Job history | Ordered record of all states the job has passed through. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Feedback` → ENQUEUED state | Job waiting to be claimed by a server (`(root) > Technical Element Set > Technical Feedback`). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Feedback` → SCHEDULED state | Job waiting for its due moment (`(root) > Technical Element Set > Technical Feedback` with instant + reason). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Feedback` → PROCESSING state | Job currently claimed and executed by a server (`(root) > Technical Element Set > Technical Feedback` with server identity). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Feedback` → SUCCEEDED state | Job completed, with latency and process durations recorded (`(root) > Technical Element Set > Technical Feedback`). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Failure` | Grouping: Technical Failure elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Failure` → FAILED state | Job exhausted all retries; stays visible in the dashboard, never silently dropped. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Job → `Technical Mechanism` → Orphaned-job detection | Server updates a processing job every poll interval (default 15 s); stale PROCESSING jobs are reclaimed after crash. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → RecurringJob | A `(root) > Technical Element Set > Production Technical System > Production Technical Object > Constitutive Technical Object` template with a cron expression or fixed interval attached; the master node schedules due instances each poll cycle. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → RecurringJob → `Technical Parameter` | Grouping: Technical Parameter elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → RecurringJob → `Technical Parameter` → Cron expression | Schedule definition (plain cron; advanced CRON is Pro). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → RecurringJob → `Technical Constraint` | Grouping: Technical Constraint elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → RecurringJob → `Technical Constraint` → OSS recurring limit | Up to 100 recurring jobs in OSS (5000 in Pro) — exemplar quota. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → BackgroundJob |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → BackgroundJob → `General Technique` | Grouping: General Technique elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → BackgroundJob → `General Technique` → enqueue | Fire-and-forget: `BackgroundJob.enqueue(() -> service.work(arg))` runs once, almost immediately. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → BackgroundJob → `General Technique` → schedule | Delayed: `BackgroundJob.schedule(Instant.now().plus(5, DAYS), () -> …)` runs once at a due moment, surviving restarts. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → BackgroundJob → `General Technique` → scheduleRecurrently | Recurring: `scheduleRecurrently("daily-report", Cron.daily(), () -> …)` runs on a fixed schedule. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → JobScheduler | Injectable scheduler behind the static facade; preferable for testability. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → JobScheduler → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → JobScheduler → `Technical Mechanism` → Idempotent creation | Creating a job with an already-existing id does not save it again. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Framework integration |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Framework integration → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Framework integration → `Constitutive Technical Object` → Spring Boot starter | Auto-configured scheduler, server, activator, and `(root) > Technical Element Set > Production Technical System > Production Technical Object > Constitutive Technical Object` support for Spring Boot. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Framework integration → `Constitutive Technical Object` → Quarkus extension | Same integration surface for Quarkus. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Framework integration → `Constitutive Technical Object` → Micronaut integration | Same integration surface for Micronaut. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Framework integration → `Technical Interface` | Grouping: Technical Interface elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Framework integration → `Technical Interface` → Fluent API | Plain-Java `(root) > Technical Element Set > Technical Interface` setup without a framework. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider | Abstraction persisting all job information as JSON; no job data kept in process memory. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Constitutive Technical Object` → RDBMS shape | Four tables and a view in relational backends. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` | Grouping: Technical Dependency elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → PostgreSQL | Supported relational backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → MySQL | Supported relational backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → MariaDB | Supported relational backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → Oracle | Supported relational backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → SQL Server | Supported relational backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → IBM Db2 | Supported relational backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → H2 | Supported embedded backend (dev/test). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → SQLite | Supported embedded backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → CockroachDB | Supported distributed-SQL backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → MongoDB | Supported NoSQL backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → Amazon DocumentDB | Supported NoSQL backend. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Dependency` → In-memory | Non-durable backend for tests. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Interface` | Grouping: Technical Interface elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → StorageProvider → `Technical Interface` → Custom StorageProvider | Extension point for own backends. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Serialization |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Serialization → `Technical Dependency` | Grouping: Technical Dependency elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Serialization → `Technical Dependency` → Jackson | Supported JSON library (2 and 3). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Serialization → `Technical Dependency` → Gson | Supported JSON library. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Serialization → `Technical Dependency` → JSON-B | Supported JSON library. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Serialization → `Technical Dependency` → Kotlin Serialization | Supported JSON library for Kotlin. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard | Built-in real-time web UI for monitoring jobs, servers, and failures. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Interface` | Grouping: Technical Interface elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Interface` → JobRunrDashboardWebServer | Embedded server exposing the UI at `http://localhost:8000` by default (exemplar). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Feedback` | Grouping: Technical Feedback elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Feedback` → State inspection | Per-job view: history, arguments, stack traces on failure. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Interface & Actuation` | Grouping: Technical Interface & Actuation elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Interface & Actuation` → Manual requeue/delete | One-click operator intervention on listed jobs. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Security` | Grouping: Technical Security elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Security` → Pro search and auth (Pro) | Advanced search, authentication, SSO, custom context path, framework-embedded serving. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Element Set` | Grouping: Technical Element Set elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Dashboard → `Technical Element Set` → Multi-cluster view (Pro) | Central view across clusters. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Workflows |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Workflows → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Workflows → `Technical Mechanism` → continueWith (Pro) | Job chaining: continuation runs once the enclosing job or batch finishes. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Workflows → `Technical Element Set` | Grouping: Technical Element Set elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Workflows → `Technical Element Set` → Batches (Pro) | Parent job aggregating child jobs with a single continuation. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Workflows → `Technical Interaction` | Grouping: Technical Interaction elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Workflows → `Technical Interaction` → External jobs (Pro) | Tracking work finishing outside the JVM (GPU inference, human approval), signalled done from anywhere. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Queues |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Queues → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Queues → `Technical Mechanism` → Priority queues (Pro) | Ordered execution by job priority. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Queues → `Technical Mechanism` → Dynamic queues (Pro) | Runtime-defined queue routing. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Queues → `Technical Configuration` | Grouping: Technical Configuration elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Queues → `Technical Configuration` → Server tags (Pro) | Routing jobs to tagged servers (e.g. GPU nodes). |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Throttles |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Throttles → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Throttles → `Technical Mechanism` → Rate limiters (Pro) | Bounded execution rate against downstream systems. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Throttles → `Technical Mechanism` → Mutexes (Pro) | Mutual exclusion across distributed jobs. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Throttles → `Technical Constraint` | Grouping: Technical Constraint elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Throttles → `Technical Constraint` → Job time-outs (Pro) | Bounded job execution duration. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Results |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Results → `Technical Feedback` | Grouping: Technical Feedback elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Results → `Technical Feedback` → Job result (Pro) | Return-value capture and retrieval for completed jobs. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Results → `General Technique` | Grouping: General Technique elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Results → `General Technique` → Replacing jobs (Pro) | Superseding a pending job with a newer definition. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Transactions |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Transactions → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Transactions → `Technical Mechanism` → Transaction plugin (Pro) | Enqueueing jobs atomically inside the application's transaction. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Scheduling |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Scheduling → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Scheduling → `Technical Mechanism` → Instant processing (Pro) | Bypassing poll latency for immediate execution. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Scheduling → `Technical Mechanism` → Real-time scheduling (Pro) | Sub-poll-cycle schedule/enqueue responsiveness. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Scheduling → `Technical Maintenance` | Grouping: Technical Maintenance elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Scheduling → `Technical Maintenance` → Custom delete policy (Pro) | Retention rules for finished-job records. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Resilience |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Resilience → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Resilience → `Technical Mechanism` → Database fault tolerance (Pro) | Continued operation across database outages. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Evolution |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Evolution → `Technical Evolution` | Grouping: Technical Evolution elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Evolution → `Technical Evolution` → CI/CD and job migrations (Pro) | Renamed-method migration support across deploys. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Evolution → `Technical Evolution` → Database migrations (Pro) | Schema migration support for the job store. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Observability |  |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Observability → `Technical Feedback` | Grouping: Technical Feedback elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Observability → `Technical Feedback` → Metrics (Pro) | Micrometer-style processing metrics export. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Observability → `Technical Interaction` | Grouping: Technical Interaction elements. |
| `Constitutive Technical Object` → JobRunr → `Constitutive Technical Object` → Observability → `Technical Interaction` → Issue-tracking integration (Pro) | Failed-job escalation into trackers. |
| `Constitutive Technical Object` → JobRunr → `Technical Dependency` | Grouping: Technical Dependency elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Dependency` → Minimal dependencies | ASM (lambda inspection), slf4j, plus one JSON library. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` | Grouping: Technical Interface elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → BackgroundJob facade | Static helpers (`(root) > Technical Element Set > Technical Interface`, `schedule`, `scheduleRecurrently`) delegating to the `JobScheduler`. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobContext | Execution context handed to job methods for progress, logging, and durable steps. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobContext → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobContext → `Technical Mechanism` → runStepOnce | Idempotent durable step, e.g. `runStepOnce("order-confirmation", () -> …)`; re-runs skip finished steps. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobActivator | IoC bridge resolving job-method instances from Spring, Micronaut, Quarkus, or other containers. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobFilter hooks | Extension points at every lifecycle stage for auditing, notifications, and custom logic. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobFilter hooks → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobFilter hooks → `Technical Mechanism` → JobClientFilter | Before/after job creation hooks. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobFilter hooks → `Technical Mechanism` → JobServerFilter | Before/after job processing hooks. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobFilter hooks → `Technical Mechanism` → ElectStateFilter | Hooks on state-transition election. |
| `Constitutive Technical Object` → JobRunr → `Technical Interface` → JobFilter hooks → `Technical Mechanism` → ApplyStateFilter | Hooks on state-transition application. |
| `Constitutive Technical Object` → JobRunr → `Technical Specification` | Grouping: Technical Specification elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Specification` → @Job annotation | Method-level configuration: name, retries, labels. |
| `Constitutive Technical Object` → JobRunr → `Technical Specification` → @Job annotation → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Specification` → @Job annotation → `Technical Mechanism` → %0 substitution | Positional argument interpolation in job names, e.g. `"Send welcome email to %0"`. |
| `Constitutive Technical Object` → JobRunr → `Technical Specification` → @Recurring annotation | Declarative recurring-job registration on startup (Spring, Micronaut, Quarkus). |
| `Constitutive Technical Object` → JobRunr → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Mechanism` → JobBuilder | Fluent builder for computed names and retry counts around a lambda or `JobRequest`. |
| `Constitutive Technical Object` → JobRunr → `Technical Mechanism` → RetryFilter | Built-in rescheduling with exponential back-off: 10 attempts by default. |
| `Constitutive Technical Object` → JobRunr → `Technical Mechanism` → RetryFilter → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Mechanism` → RetryFilter → `Technical Mechanism` → Custom RetryFilter | Application-provided retry behavior override. |
| `Constitutive Technical Object` → JobRunr → `Technical Mechanism` → RetryFilter → `Technical Mechanism` → RetryPolicy (Pro) | Declarative retry policies in the Pro tier. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` | Grouping: Production Technical System elements. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer | In-process server polling storage, atomically claiming jobs, and invoking target methods. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Configuration` | Grouping: Technical Configuration elements. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Configuration` → Disabled by default | Server and dashboard must be explicitly enabled. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Constraint` | Grouping: Technical Constraint elements. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Constraint` → One per JVM | Never start more than one `(root) > Technical Element Set > Technical Constraint` in the same JVM instance. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Constitutive Technical Object` | Grouping: Constitutive Technical Object elements. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Constitutive Technical Object` → Worker pool | Dedicated worker-pool threads executing claimed jobs. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Mechanism` | Grouping: Technical Mechanism elements. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Mechanism` → Virtual threads | Loom virtual-thread execution support. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Mechanism` → Atomic claim | Claimed jobs are never processed twice across the cluster. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Mechanism` → Master election | Longest-running server becomes master and runs housekeeping: enqueueing scheduled jobs, scheduling recurring jobs, deleting jobs. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Interaction` | Grouping: Technical Interaction elements. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Interaction` → Horizontal scale-out | More application instances each join the cluster and share load automatically. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Strategy` | Grouping: Technical Strategy elements. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Technical Strategy` → Carbon-aware processing | Scheduling strategy biased toward low-carbon grid windows. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Production Technical System` | Grouping: Production Technical System elements. |
| `Constitutive Technical Object` → JobRunr → `Production Technical System` → BackgroundJobServer → `Production Technical System` → Microservice deployment | Alternative topology: JobRunr runs as its own deployable instead of embedded. |
| `Constitutive Technical Object` → JobRunr → `Technical Practice` | Grouping: Technical Practice elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Practice` → REST-offload practice | Repeatable pattern: return the HTTP response immediately, run the long work as an enqueued job. |
| `Constitutive Technical Object` → JobRunr → `Technical Practice` → Newsletter practice | Repeatable pattern: mass notifications as fire-and-forget jobs. |
| `Constitutive Technical Object` → JobRunr → `Technical Practice` → Batch-import practice | Repeatable pattern: XML/CSV/JSON imports as background batches. |
| `Constitutive Technical Object` → JobRunr → `Technical Practice` → Recurring-report practice | Repeatable pattern: automated reports as recurring jobs. |
| `Constitutive Technical Object` → JobRunr → `Technical Practice` → Command-handler practice | Repeatable pattern: `(root) > Technical Element Set > Technical Practice`/`JobRequestHandler` separation of job data and logic. |
| `Constitutive Technical Object` → JobRunr → `Technical Evolution` | Grouping: Technical Evolution elements. |
| `Constitutive Technical Object` → JobRunr → `Technical Evolution` → Evolution Quartz-to-JobRunr | Historical line: Quartz/Spring Task Scheduler (in-memory, single-node) → JobRunr (persisted, distributed) → Pro tier. |

## Usage

> Three calls cover most needs; all persist a `Job` and return immediately.

```java
// Fire-and-forget: runs once, almost immediately
BackgroundJob.enqueue(() -> emailService.sendWelcomeEmail(userEmail));

// Delayed: runs once, 5 days from now — survives restarts
BackgroundJob.schedule(Instant.now().plus(5, ChronoUnit.DAYS), () -> emailService.sendFollowUp(userEmail));

// Recurring: runs on a cron schedule
BackgroundJob.scheduleRecurrently("daily-report", Cron.daily(), () -> reportService.sendDailyReport());
```

```java
// Configured: name with argument substitution + retry budget
@Job(name = "Send welcome email to %0", retries = 3)
public void sendWelcomeEmail(String userEmail) { ... }
```

```java
// Durable multi-step method: finished steps are skipped on retry
public void processOrder(UUID orderId, JobContext context) {
    context.runStepOnce("order-confirmation", () -> orderService.sendConfirmation(orderId));
    context.runStepOnce("warehouse-notification", () -> orderService.notifyWarehouse(orderId));
}
```

## References

- [JobRunr — Distributed Java Background Job Scheduler](https://www.jobrunr.io/)
- [JobRunr Documentation — Introduction](https://www.jobrunr.io/en/documentation/)
- [jobrunr/jobrunr on GitHub](https://github.com/jobrunr/jobrunr)
- [JobRunr compared (alternatives)](https://www.jobrunr.io/en/documentation/alternatives/)
- [Spring Boot](note.html?n=technica/cto/es/multinode/spring-boot.md)
- [Sidekiq](note.html?n=technica/cto/es/multinode/sidekiq.md)
- [Philosophia Artium Technicarum et Operis](https://raw.githubusercontent.com/csiglab/Naturgnosis/refs/heads/main/app/note/data/meta/philosophia-artium-technicarum-et-operis.md)
