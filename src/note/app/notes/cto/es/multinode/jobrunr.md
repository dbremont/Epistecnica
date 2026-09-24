# JobRunr

> JobRunr is an embeddable JVM library for durable, distributed background jobs — fire-and-forget, delayed, and recurring — written with plain Java methods.
>

> It is the complement of the request path: the web request returns fast while the `Job` persists as JSON in the application's existing database, is claimed and executed by a `BackgroundJobServer`, retried on failure, and observed in a built-in dashboard.
>

> This note characterizes JobRunr as a full ensemble — jobs, states, scheduler API, server cluster, storage providers, dashboard, filters, framework integrations, and practices (OSS plus a marked Pro sketch) — following the schema in [Philosophia Artium Technicarum et Operis](note.html?n=general/philosophia-artium-technicarum-et-operis.md).

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

| Instance Tree Path | Description | Technical Category | Technical Element Type Tree Path |
|---|---|---|---|
| **JobRunr** | Embeddable background-processing library instance plus its server, storage, dashboard, and practices. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > Coherence (one persisted job, many realizations) | Organizing structure: a single persisted `Job` record drives scheduling, claiming, execution, retry, and observation. | System Structure | `(root) > Technical Architecture` |
| JobRunr > Realized capability | Capability realized: durable, distributed background work on the JVM with no extra infrastructure. | Mechanism & Capability | `(root) > Technical Capability` |
| JobRunr > Governance (author + licenses) | Ronald Dehuysser authorship; `jobrunr/jobrunr` on GitHub; LGPL 3.0 OSS plus commercial Pro tier. | Knowledge & Methodology | `(root) > Technical Element Set > Knowledge & Methodology > Technical Institution` |
| JobRunr > Distribution (Maven Central) | Versioned artifact `org.jobrunr:jobrunr` consumed via Maven or Gradle (exemplar 8.8.1). | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > Minimal dependencies | ASM (lambda inspection), slf4j, plus one JSON library. | System Relations | `(root) > Technical Dependency` |
| JobRunr > Job | Unit of work performed outside the current execution context, with name, signature, details, and state history. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > Job > JobDetails | Type, method to execute, and arguments extracted from the lambda via ASM and serialized to JSON. | Requirements & Definition | `(root) > Technical Specification` |
| JobRunr > Job > Job name | Human-readable name: `@Job` value, `JobBuilder` value, or derived default. | Requirements & Definition | `(root) > Technical Parameter` |
| JobRunr > Job > Job history | Ordered record of all states the job has passed through. | Technical Control | `(root) > Technical Control > Technical Feedback` |
| JobRunr > Job > ENQUEUED state | Job waiting to be claimed by a server (`EnqueuedState`). | Technical Control | `(root) > Technical Control > Technical Feedback` |
| JobRunr > Job > SCHEDULED state | Job waiting for its due moment (`ScheduledState` with instant + reason). | Technical Control | `(root) > Technical Control > Technical Feedback` |
| JobRunr > Job > PROCESSING state | Job currently claimed and executed by a server (`ProcessingState` with server identity). | Technical Control | `(root) > Technical Control > Technical Feedback` |
| JobRunr > Job > SUCCEEDED state | Job completed, with latency and process durations recorded (`SucceededState`). | Technical Control | `(root) > Technical Control > Technical Feedback` |
| JobRunr > Job > FAILED state | Job exhausted all retries; stays visible in the dashboard, never silently dropped. | Technical Control | `(root) > Technical Control > Technical Failure` |
| JobRunr > Job > Orphaned-job detection | Server updates a processing job every poll interval (default 15 s); stale PROCESSING jobs are reclaimed after crash. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > RecurringJob | A `Job` template with a cron expression or fixed interval attached; the master node schedules due instances each poll cycle. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > RecurringJob > Cron expression | Schedule definition (plain cron; advanced CRON is Pro). | Requirements & Definition | `(root) > Technical Parameter` |
| JobRunr > RecurringJob > OSS recurring limit | Up to 100 recurring jobs in OSS (5000 in Pro) — exemplar quota. | Technical Context | `(root) > Technical Constraint` |
| JobRunr > BackgroundJob facade | Static helpers (`enqueue`, `schedule`, `scheduleRecurrently`) delegating to the `JobScheduler`. | System Structure | `(root) > Technical Interface` |
| JobRunr > BackgroundJob > `enqueue` | Fire-and-forget: `BackgroundJob.enqueue(() -> service.work(arg))` runs once, almost immediately. | Technique | `(root) > General Technique Type` |
| JobRunr > BackgroundJob > `schedule` | Delayed: `BackgroundJob.schedule(Instant.now().plus(5, DAYS), () -> …)` runs once at a due moment, surviving restarts. | Technique | `(root) > General Technique Type` |
| JobRunr > BackgroundJob > `scheduleRecurrently` | Recurring: `scheduleRecurrently("daily-report", Cron.daily(), () -> …)` runs on a fixed schedule. | Technique | `(root) > General Technique Type` |
| JobRunr > JobScheduler | Injectable scheduler behind the static facade; preferable for testability. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > JobScheduler > Idempotent creation | Creating a job with an already-existing id does not save it again. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > JobRequest pattern | Command/handler separation: `JobRequest` carries data, `JobRequestHandler` performs the work. | System Structure | `(root) > Technical Architecture` |
| JobRunr > JobRequest pattern > `JobRequest` | Interface carrying job data plus `getJobRequestHandler()`. | System Structure | `(root) > Technical Interface` |
| JobRunr > JobRequest pattern > `JobRequestHandler` | `run(request)` implementation performing the work. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > JobRequest pattern > `BackgroundJobRequest` | Static facade offering the same API for `JobRequest`s. | System Structure | `(root) > Technical Interface` |
| JobRunr > JobRequest pattern > `JobRequestScheduler` | Injectable scheduler for `JobRequest`s. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > `@Job` annotation | Method-level configuration: name, retries, labels. | Requirements & Definition | `(root) > Technical Specification` |
| JobRunr > `@Job` annotation > `%0` substitution | Positional argument interpolation in job names, e.g. `"Send welcome email to %0"`. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > `JobBuilder` | Fluent builder for computed names and retry counts around a lambda or `JobRequest`. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > `@Recurring` annotation | Declarative recurring-job registration on startup (Spring, Micronaut, Quarkus). | Requirements & Definition | `(root) > Technical Specification` |
| JobRunr > `JobContext` | Execution context handed to job methods for progress, logging, and durable steps. | System Structure | `(root) > Technical Interface` |
| JobRunr > `JobContext` > `runStepOnce` | Idempotent durable step, e.g. `runStepOnce("order-confirmation", () -> …)`; re-runs skip finished steps. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > BackgroundJobServer | In-process server polling storage, atomically claiming jobs, and invoking target methods. | System Structure | `(root) > Production Technical System` |
| JobRunr > BackgroundJobServer > Disabled by default | Server and dashboard must be explicitly enabled. | Requirements & Definition | `(root) > Technical Configuration` |
| JobRunr > BackgroundJobServer > One per JVM | Never start more than one `BackgroundJobServer` in the same JVM instance. | Technical Context | `(root) > Technical Constraint` |
| JobRunr > BackgroundJobServer > Worker pool | Dedicated worker-pool threads executing claimed jobs. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > BackgroundJobServer > Virtual threads | Loom virtual-thread execution support. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > BackgroundJobServer > Atomic claim | Claimed jobs are never processed twice across the cluster. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > BackgroundJobServer > Master election | Longest-running server becomes master and runs housekeeping: enqueueing scheduled jobs, scheduling recurring jobs, deleting jobs. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > BackgroundJobServer > Horizontal scale-out | More application instances each join the cluster and share load automatically. | System Relations | `(root) > Technical Interaction` |
| JobRunr > BackgroundJobServer > Carbon-aware processing | Scheduling biased toward low carbon-intensity grid windows. | Technique | `(root) > General Technique Type` |
| JobRunr > BackgroundJobServer > Microservice deployment | Alternative topology: JobRunr runs as its own deployable instead of embedded. | System Structure | `(root) > Production Technical System` |
| JobRunr > JobActivator | IoC bridge resolving job-method instances from Spring, Micronaut, Quarkus, or other containers. | System Structure | `(root) > Technical Interface` |
| JobRunr > Framework integration > Spring Boot starter | Auto-configured scheduler, server, activator, and `@Recurring` support for Spring Boot. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > Framework integration > Quarkus extension | Same integration surface for Quarkus. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > Framework integration > Micronaut integration | Same integration surface for Micronaut. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > Framework integration > Fluent API | Plain-Java `JobRunr.configure()` setup without a framework. | System Structure | `(root) > Technical Interface` |
| JobRunr > RetryFilter | Built-in rescheduling with exponential back-off: 10 attempts by default. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > RetryFilter > Custom RetryFilter | Application-provided retry behavior override. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > RetryFilter > RetryPolicy (Pro) | Declarative retry policies in the Pro tier. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > JobFilter hooks | Extension points at every lifecycle stage for auditing, notifications, and custom logic. | System Structure | `(root) > Technical Interface` |
| JobRunr > JobFilter hooks > JobClientFilter | Before/after job creation hooks. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > JobFilter hooks > JobServerFilter | Before/after job processing hooks. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > JobFilter hooks > ElectStateFilter | Hooks on state-transition election. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > JobFilter hooks > ApplyStateFilter | Hooks on state-transition application. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > StorageProvider | Abstraction persisting all job information as JSON; no job data kept in process memory. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > StorageProvider > RDBMS shape | Four tables and a view in relational backends. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > StorageProvider > PostgreSQL | Supported relational backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > MySQL | Supported relational backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > MariaDB | Supported relational backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > Oracle | Supported relational backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > SQL Server | Supported relational backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > IBM Db2 | Supported relational backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > H2 | Supported embedded backend (dev/test). | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > SQLite | Supported embedded backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > CockroachDB | Supported distributed-SQL backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > MongoDB | Supported NoSQL backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > Amazon DocumentDB | Supported NoSQL backend. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > In-memory | Non-durable backend for tests. | System Relations | `(root) > Technical Dependency` |
| JobRunr > StorageProvider > Custom StorageProvider | Extension point for own backends. | System Structure | `(root) > Technical Interface` |
| JobRunr > Serialization > Jackson | Supported JSON library (2 and 3). | System Relations | `(root) > Technical Dependency` |
| JobRunr > Serialization > Gson | Supported JSON library. | System Relations | `(root) > Technical Dependency` |
| JobRunr > Serialization > JSON-B | Supported JSON library. | System Relations | `(root) > Technical Dependency` |
| JobRunr > Serialization > Kotlin Serialization | Supported JSON library for Kotlin. | System Relations | `(root) > Technical Dependency` |
| JobRunr > Dashboard | Built-in real-time web UI for monitoring jobs, servers, and failures. | System Structure | `(root) > Constitutive Technical Object` |
| JobRunr > Dashboard > `JobRunrDashboardWebServer` | Embedded server exposing the UI at `http://localhost:8000` by default (exemplar). | System Structure | `(root) > Technical Interface` |
| JobRunr > Dashboard > State inspection | Per-job view: history, arguments, stack traces on failure. | Technical Control | `(root) > Technical Control > Technical Feedback` |
| JobRunr > Dashboard > Manual requeue/delete | One-click operator intervention on listed jobs. | Technique | `(root) > Technical Interface & Actuation` |
| JobRunr > Dashboard > Pro search and auth (Pro) | Advanced search, authentication, SSO, custom context path, framework-embedded serving. | Technical Control | `(root) > Technical Security` |
| JobRunr > Dashboard > Multi-cluster view (Pro) | Central view across clusters. | System Structure | `(root) > Technical Element Set` |
| JobRunr > Workflows > `continueWith` (Pro) | Job chaining: continuation runs once the enclosing job or batch finishes. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Workflows > Batches (Pro) | Parent job aggregating child jobs with a single continuation. | System Structure | `(root) > Technical Element Set` |
| JobRunr > Workflows > External jobs (Pro) | Tracking work finishing outside the JVM (GPU inference, human approval), signalled done from anywhere. | System Relations | `(root) > Technical Interaction` |
| JobRunr > Queues > Priority queues (Pro) | Ordered execution by job priority. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Queues > Dynamic queues (Pro) | Runtime-defined queue routing. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Queues > Server tags (Pro) | Routing jobs to tagged servers (e.g. GPU nodes). | Requirements & Definition | `(root) > Technical Configuration` |
| JobRunr > Throttles > Rate limiters (Pro) | Bounded execution rate against downstream systems. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Throttles > Mutexes (Pro) | Mutual exclusion across distributed jobs. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Throttles > Job time-outs (Pro) | Bounded job execution duration. | Technical Context | `(root) > Technical Constraint` |
| JobRunr > Results > Job result (Pro) | Return-value capture and retrieval for completed jobs. | Technical Control | `(root) > Technical Control > Technical Feedback` |
| JobRunr > Results > Replacing jobs (Pro) | Superseding a pending job with a newer definition. | Technique | `(root) > General Technique Type` |
| JobRunr > Transactions > Transaction plugin (Pro) | Enqueueing jobs atomically inside the application's transaction. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Scheduling > Instant processing (Pro) | Bypassing poll latency for immediate execution. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Scheduling > Real-time scheduling (Pro) | Sub-poll-cycle schedule/enqueue responsiveness. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Scheduling > Custom delete policy (Pro) | Retention rules for finished-job records. | Lifecycle & Continuity | `(root) > Technical Maintenance` |
| JobRunr > Resilience > Database fault tolerance (Pro) | Continued operation across database outages. | Mechanism & Capability | `(root) > Technical Mechanism` |
| JobRunr > Evolution > CI/CD and job migrations (Pro) | Renamed-method migration support across deploys. | Lifecycle & Continuity | `(root) > Technical Evolution` |
| JobRunr > Evolution > Database migrations (Pro) | Schema migration support for the job store. | Lifecycle & Continuity | `(root) > Technical Evolution` |
| JobRunr > Observability > Metrics (Pro) | Micrometer-style processing metrics export. | Technical Control | `(root) > Technical Control > Technical Feedback` |
| JobRunr > Observability > Issue-tracking integration (Pro) | Failed-job escalation into trackers. | System Relations | `(root) > Technical Interaction` |
| JobRunr > REST-offload practice | Repeatable pattern: return the HTTP response immediately, run the long work as an enqueued job. | Technique | `(root) > Technical Practice` |
| JobRunr > Newsletter practice | Repeatable pattern: mass notifications as fire-and-forget jobs. | Technique | `(root) > Technical Practice` |
| JobRunr > Batch-import practice | Repeatable pattern: XML/CSV/JSON imports as background batches. | Technique | `(root) > Technical Practice` |
| JobRunr > Recurring-report practice | Repeatable pattern: automated reports as recurring jobs. | Technique | `(root) > Technical Practice` |
| JobRunr > Command-handler practice | Repeatable pattern: `JobRequest`/`JobRequestHandler` separation of job data and logic. | Technique | `(root) > Technical Practice` |
| JobRunr > Evolution Quartz-to-JobRunr | Historical line: Quartz/Spring Task Scheduler (in-memory, single-node) → JobRunr (persisted, distributed) → Pro tier. | Lifecycle & Continuity | `(root) > Technical Evolution` |

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
- [Spring Boot](note.html?n=cto/es/multinode/spring-boot.md)
- [Sidekiq](note.html?n=cto/es/multinode/sidekiq.md)
- [Philosophia Artium Technicarum et Operis](note.html?n=general/philosophia-artium-technicarum-et-operis.md)
