# Source Code

- [GIT (Global Information Tracker)](note.html?n=technica/computation/system/operation/operation-conceptual-model/git-global-information-tracker.md)

> ….
> 

## Annotation System

> What does problem  does an annotation system solves? An **annotation system augments** source code with structured metadata that communicates intent, status, constraints, risks, and maintenance information to both humans and automated tools.
> 

> What kind of technical element is an annotation system? `Technical Standard` and `Technical Practice`.
> 

| **Category** | **Annotation** | **Meaning** |
| --- | --- | --- |
| **Work Management** | `@TODO` | Work still needs to be done. |
|  | `@FIXME` | Known bug or incorrect behavior that should be corrected. |
|  | `@BUG` | Documents an existing bug or defect. |
|  | `@LATER` | Planned enhancement that is intentionally postponed. |
|  | `@REVIEW` | Requires manual review or peer inspection. |
|  | `@QUESTION` | Documents an unresolved question. |
|  | `@VERIFY` | Indicates an assumption or behavior that must be verified. |
|  | `@IDEA` | Records a possible future improvement or design idea. |
| **Code Evolution** | `@REFACTOR` | Code should be restructured without changing behavior. |
|  | `@SIMPLIFY` | Logic can be simplified. |
|  | `@OPTIMIZE` | Opportunity for performance or efficiency optimization. |
|  | `@TECH-DEBT` | Intentional technical debt. |
|  | `@HACK` | Temporary implementation that should eventually be replaced. |
|  | `@WORKAROUND` | Temporary solution for an external limitation or bug. |
|  | `@DEPRECATED` | Feature or code should no longer be used. |
|  | `@EXPERIMENTAL` | Feature is experimental and may change. |
|  | `@LEGACY` | Legacy implementation retained for compatibility. |
|  | `@STABLE` | Mature and stable implementation. |
|  | `@MIGRATION` | Documents migration work or compatibility transition. |
|  | `@SINCE` | Indicates the version or release in which the code was introduced. |
| **Correctness & Contracts** | `@PRECONDITION` | Conditions that must hold before execution. |
|  | `@POSTCONDITION` | Conditions guaranteed after execution. |
|  | `@INVARIANT` | Property that must always remain true. |
|  | `@ASSUMPTION` | Important assumption made by the implementation. |
|  | `@SIDE-EFFECT` | Describes observable side effects. |
|  | `@THREAD-SAFE` | Code is safe for concurrent execution. |
|  | `@NOT-THREAD-SAFE` | Code is not safe for concurrent use. |
| **Quality Attributes** | `@SECURITY` | Security-related concern or implementation. |
|  | `@PERFORMANCE` | Performance-sensitive code. |
|  | `@MEMORY` | Memory usage consideration. |
|  | `@CONCURRENCY` | Threading or synchronization concern. |
|  | `@COMPATIBILITY` | Cross-version or cross-platform compatibility concern. |
|  | `@SCALABILITY` | Scalability consideration. |
|  | `@RELIABILITY` | Reliability concern. |
|  | `@AVAILABILITY` | Availability or fault-tolerance consideration. |
|  | `@PORTABILITY` | Platform portability concern. |
|  | `@USABILITY` | User experience or usability consideration. |
| **Architecture & Design** | `@API` | Documents an important API contract. |
|  | `@COMPONENT` | Identifies the architectural component. |
|  | `@MODULE` | Indicates the logical module. |
|  | `@LAYER` | Specifies the architectural layer. |
|  | `@BOUNDARY` | Marks a system or subsystem boundary. |
|  | `@RESPONSIBILITY` | Explains the responsibility of the code. |
|  | `@DEPENDENCY` | Documents an important dependency. |
|  | `@EXTENSION-POINT` | Intended extension point for future implementations. |
|  | `@PATTERN` | Indicates the design pattern being implemented. |
| **Requirements & Traceability** | `@SPEC` | References a technical specification. |
|  | `@REQUIREMENT` | References a functional or non-functional requirement. |
|  | `@TRACE` | Links the code to requirements, tickets, or issues. |
|  | `@DECISION` | Documents an architectural or design decision. |
|  | `@RATIONALE` | Explains why the implementation exists. |
| **Testing** | `@TEST` | Notes testing considerations. |
|  | `@TEST-CASE` | References a related test case. |
|  | `@TESTED` | Indicates the code has been validated. |
|  | `@MOCK` | Intended for testing or mocking. |
|  | `@COVERAGE` | Notes expected or missing test coverage. |
| **Configuration & Deployment** | `@CONFIG` | Depends on configuration values. |
|  | `@ENVIRONMENT` | Environment-specific behavior. |
|  | `@FEATURE-FLAG` | Controlled by a feature flag. |
|  | `@DEFAULT` | Documents default behavior or values. |
| **Observability** | `@LOGGING` | Important logging behavior. |
|  | `@METRICS` | Emits or relies on metrics. |
|  | `@TRACING` | Distributed tracing concern. |
|  | `@AUDIT` | Audit trail or audit logging. |
| **Data & Persistence** | `@CACHE` | Caching behavior. |
|  | `@PERSISTENCE` | Persistence concern. |
|  | `@TRANSACTION` | Transactional behavior. |
|  | `@SERIALIZATION` | Serialization or deserialization concern. |
|  | `@INDEX` | Database indexing consideration. |
| **Reliability & Resilience** | `@RETRY` | Retry mechanism. |
|  | `@TIMEOUT` | Timeout behavior. |
|  | `@FALLBACK` | Fallback strategy. |
|  | `@CIRCUIT-BREAKER` | Circuit breaker implementation. |
|  | `@IDEMPOTENT` | Operation is idempotent. |
|  | `@RECOVERY` | Recovery strategy after failures. |
| **Compliance & Governance** | `@LICENSE` | Licensing information. |
|  | `@PRIVACY` | Privacy-related concern. |
|  | `@GDPR` | GDPR compliance note. |
|  | `@PCI` | PCI compliance consideration. |
|  | `@HIPAA` | HIPAA compliance consideration. |
| **Ownership & Maintenance** | `@OWNER` | Code owner. |
|  | `@TEAM` | Responsible team. |
|  | `@CONTACT` | Technical contact. |
|  | `@MAINTAINER` | Primary maintainer. |
| **Documentation** | `@NOTE` | General explanatory note. |
|  | `@WARNING` | Important caution for maintainers. |
|  | `@EXAMPLE` | Example of expected usage or behavior. |
|  | `@REFERENCE` | References external documentation or resources. |
|  | `@SEE` | Points to related code or documentation. |
|  | `@DOMAIN` | Explains a business or domain concept. |
|  | `@BUSINESS-RULE` | Documents an important business rule implemented by the code. |
|  | `@GLOSSARY` | Defines important domain terminology. |

### Which annotations are commit-blocking?

| Annotation | Requires Immediate Action? | Blocks Commit? |
| --- | --- | --- |
| `@FIXME` | Yes | Yes |
| `@QUESTION` | Yes | Yes |
| `@VERIFY` | Yes | Yes |
| `@REVIEW` | Yes | Yes |
| `@TODO` | Usually | Depends on policy |

## References

- https://en.wikipedia.org/wiki/Source_code
- Monorepo - How Large enterprises manage a body of related body of Software; Imagine an Operative System; etc multiple repos or a single one? [https://blog.swgillespie.me/posts/monorepo-ingredients/](https://blog.swgillespie.me/posts/monorepo-ingredients/)
- https://github.com/dbremont/configs