---
tags: [description-artifact]
---

# Computation Description Artifact

- [Program](note.html?n=technica/computation/language-system/conceptual-model-language-system/program.md)

> **Computation Description Artifact** — an artifact whose primary purpose is to **describe, specify, compose,  or otherwise represent a computation**, independently of or prior to its execution.
> 

## Which descriptive artifacts are used to specify computations?

| **Type** | **Description** | **Where does it live? (Source File, Runtime)** | **Usage** | **Concrete Instantiation(s)** |
| --- | --- | --- | --- | --- |
| **Program** | Describes an executable computation in a programming language | Source File / Runtime | General-purpose computation | `.java`, `.c`, `.cpp`, `.py`, executable |
| **Query** | Declaratively describes a computation over data | Source File / Runtime | Data retrieval and transformation | SQL query, SPARQL query, GraphQL query |
| **Workflow** | Describes a computation as a composition of activities and their control/data dependencies | Source File / Runtime | Process and computation orchestration | Airflow DAG, Argo Workflow, GitHub Actions workflow |
| **Pipeline** | Describes a computation as a sequence or graph of processing stages and transformations | Source File / Runtime | CI/CD, ETL, ML, data processing | ETL pipeline, ML pipeline, CI/CD pipeline |
| **DAG** | Describes a computation through computational nodes and their dependency relationships | Source File / Runtime | Dependency-driven computation | Airflow DAG, Spark DAG, Maven execution graph |
| **Build Specification** | Describes a software-build computation, including dependencies, plugins, lifecycle, goals, and configuration | Source File / Runtime | Build automation | `pom.xml`, `build.gradle` |
| **Build Script** | Describes a build computation through explicitly specified computational steps | Source File / Runtime | Imperative build automation | `Makefile`, shell script, Gradle build script |
| **Job Specification** | Describes a unit of computation, including its inputs, parameters, resources, and execution requirements | Source File / Runtime | Batch and distributed computing | Kubernetes Job, SLURM job script |
| **Task Specification** | Describes an individual computational activity and its execution configuration | Source File / Runtime | Workflow and job systems | Airflow task, Kubernetes task, Maven Mojo executio |

## References

- https://en.wikipedia.org/wiki/Source_code
- https://en.wikipedia.org/wiki/SQL