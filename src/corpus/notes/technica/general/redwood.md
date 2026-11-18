---
tags: [note, workload-automation, saas, redwood, work-execution]
---

# Redwood

> **Redwood** — now **Redwood RunMyJobs** — is workload automation delivered as a service: the same job-net model as [Control-M](/view.html?p=notes/technica/general/control-m.md) — jobs, dependencies, calendars, SLAs — but hosted, with a web console and connectors into SAP, Oracle, databases, file transfer and cloud services, rather than an agent estate the customer installs and runs.

> Its place in the market is the SaaS answer to the same problem: an enterprise has a nightly and periodic batch estate that must run in order, on time, with an audit trail, and it does not want to operate the scheduler itself. Redwood sells the service and the connectors; the customer keeps the jobs and the calendars.

## The model

| Concept | What it is |
| --- | --- |
| **Job** | The unit of work: a script, a SAP job, a database task, a file transfer, a cloud action |
| **Job chain / flow** | The dependency graph, with success, failure and conditional links |
| **Calendar** | The business calendar and the run windows |
| **SLA** | The expected completion time, monitored by the service |
| **Connector** | The integration to a target system — SAP, Oracle, Salesforce, cloud, file transfer |
| **Console** | The web operations surface: the plan, the run history, the alerts |

## The properties that matter

| Property | Consequence |
| --- | --- |
| **SaaS delivery** | No scheduler infrastructure to operate; the vendor runs the engines |
| **Connector catalogue** | The integration is pre-built per target system |
| **SAP depth** | The product's traditional centre of gravity |
| **SLA monitoring** | The service tracks whether the plan is on time, not just whether it ran |
| **Coexistence** | Usually runs beside an on-premises automation tool while the estate migrates |

## Where it sits

> Redwood is **workload automation** in the work-execution taxonomy, the cloud-delivered member of the family. The distinction from a background-job system is the same one Control-M draws: the unit is the enterprise job net, not an application job. The distinction from Redwood's competitors is delivery, not function.

## References

- [Redwood RunMyJobs](https://www.redwood.com/)
- [Work Execution System](/view.html?p=notes/technica/computation/enterprise-information-system-eis/work-execution-system.md) — the family this tool belongs to
- [Control-M](/view.html?p=notes/technica/general/control-m.md) — the on-premises counterpart
- [Temporal](/view.html?p=notes/technica/general/temporal.md) · [Camunda](/view.html?p=notes/technica/general/camunda.md) — the workflow engines, for the contrast between process orchestration and batch automation
