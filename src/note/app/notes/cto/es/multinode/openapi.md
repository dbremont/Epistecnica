# OpenAPI Specification (OAS)

> OpenAPI is a language-agnostic standard for describing HTTP APIs as machine-readable contracts, consumable by humans and tooling alike.
>

> It is the complement of an implementation: the OpenAPI document states the intended interface (paths, operations, schemas, security) while servers, clients, and gateways realize it.
>

> This note treats OpenAPI as a full ecosystem — the versioned specification plus its documents, annotations, generators, validators, renderers, and practices — following the schema in [Philosophia Artium Technicarum et Operis](note.html?n=general/philosophia-artium-technicarum-et-operis.md).

## Formulation

### What technical element type does this technical instance belong to?

**OpenAPI belongs to the `Technical Standard` technical element type — a set of versioned specs — readable as a `Technical Element Set`.**

More specifically:

```text
Technical Standard
└── OpenAPI (umbrella standard — OAS 2.0 / 3.0 / 3.1)
    readable as Technical Element Set (spec + documents + tooling + practices)
```

OpenAPI is a standard because it is a normative specification governing the form, function, interoperability, and behavior of API description documents. It is itself a set: versioned spec documents (Swagger 2.0, OAS 3.0, OAS 3.1) grouped under one umbrella. A tool (validator, generator, renderer) *implements* the spec; a running server, gateway, or generated client *realizes* a described interface. As a coherent body of standard + blueprint documents + objects + techniques + institutions organized around one capability — specify, produce, validate, document, and consume API interfaces — it can also be read as a `Technical Element Set`.

### What is this technical instance?

> OpenAPI is a versioned, serialization-independent standard instance for machine-readable HTTP API contracts — describing paths, operations, parameters, request/response bodies, schemas, and security in JSON or YAML — together with the document format, tooling, and contract-first/code-first practices that generate code, validation, documentation, and gateway enforcement from a single source.

Lineage: Swagger 2.0 (Wordnik/SmartBear) donated to the OpenAPI Initiative (Linux Foundation, 2015) → OAS 3.0 (2017) → OAS 3.1 (2021, full JSON Schema alignment).

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one OAS 3.x ecosystem instance (standard, document format, spec objects, tooling, practices, control, governance); deployment-specific values appear only in rows marked exemplar.
>
> Stopping rule: a row is terminal when it names a concrete spec version, a named OAS object field, a file, a named tool, a config attribute, or a named actor.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a tool *implements* the standard; a server, gateway, or generated client *realizes* a described interface.

| Instance Tree Path | Description | Technical Category | Technical Element Type Tree Path |
|---|---|---|---|
| **OpenAPI** | Umbrella standard plus its document format, tooling, and practices for API contracts. | Requirements & Definition | `(root) > Technical Standard` |
| OpenAPI > Coherence (one contract, many artifacts) | Organizing structure: a single machine-readable contract drives code, docs, validation, mocks, and gateway policy. | System Structure | `(root) > Technical Architecture` |
| OpenAPI > Realized capability | Capability realized: specify, produce, validate, document, and consume HTTP API interfaces from one source. | Mechanism & Capability | `(root) > Technical Capability` |
| OpenAPI > Governance (OpenAPI Initiative) | Linux Foundation stewardship of the spec set; versioning and conformance process. | Knowledge & Methodology | `(root) > Technical Element Set > Knowledge & Methodology > Technical Institution` |
| OpenAPI > Specification | The versioned spec set: Swagger 2.0, OAS 3.0, OAS 3.1 documents. | Requirements & Definition | `(root) > Technical Standard` |
| OpenAPI > Specification > OAS 3.1 document | Current spec version, aligned with JSON Schema (2021). | Requirements & Definition | `(root) > Technical Standard` |
| OpenAPI > Specification > OAS 3.0 document | Prior spec version still widely deployed. | Requirements & Definition | `(root) > Technical Standard` |
| OpenAPI > Specification > Swagger 2.0 document | Donated predecessor format (2015 heritage). | Requirements & Definition | `(root) > Technical Standard` |
| OpenAPI > OpenAPI Document | A concrete API contract file (`openapi.json` / `openapi.yaml`) conforming to the spec. | System Structure | `(root) > Technical Blueprint` |
| OpenAPI > OpenAPI Document > Info | Title, version, description of the described API. | Requirements & Definition | `(root) > Technical Specification` |
| OpenAPI > OpenAPI Document > Servers | Base URLs and variables where the described API is realized (exemplar values per deployment). | System Structure | `(root) > Technical Configuration` |
| OpenAPI > OpenAPI Document > Paths | Route table mapping URL templates to operations. | System Structure | `(root) > Technical Interface` |
| OpenAPI > OpenAPI Document > Paths > Operation | One HTTP method + path entry: parameters, bodies, responses, security. | System Structure | `(root) > Technical Interface` |
| OpenAPI > OpenAPI Document > Paths > Operation > `operationId` | Stable identifier linking an operation to generated code and tooling. | Requirements & Definition | `(root) > Technical Parameter` |
| OpenAPI > OpenAPI Document > Paths > Operation > Tags | Grouping label organizing operations in renderers. | Requirements & Definition | `(root) > Technical Specification` |
| OpenAPI > OpenAPI Document > Parameter | Typed input bound from query, path, header, or cookie. | Requirements & Definition | `(root) > Technical Parameter` |
| OpenAPI > OpenAPI Document > RequestBody | Declared request payload shape and media types. | Requirements & Definition | `(root) > Technical Specification` |
| OpenAPI > OpenAPI Document > Responses | Declared response shapes per status code. | Requirements & Definition | `(root) > Technical Specification` |
| OpenAPI > OpenAPI Document > Components | Reusable section: schemas, security schemes, headers, examples. | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > OpenAPI Document > Components > Schema | Data-model definition (OAS 3.1: plain JSON Schema). | Requirements & Definition | `(root) > Technical Specification` |
| OpenAPI > OpenAPI Document > Components > SecurityScheme | Declared auth mechanism (HTTP, apiKey, OAuth2, OpenID Connect). | Technical Control | `(root) > Technical Security` |
| OpenAPI > OpenAPI Document > Security Requirement | Which security schemes guard an operation or the whole API. | Technical Control | `(root) > Technical Security` |
| OpenAPI > OpenAPI Document > ExternalDocs | Pointer to out-of-band documentation. | Knowledge & Methodology | `(root) > Technical Knowledge` |
| OpenAPI > Annotation libraries | Code annotations that emit OpenAPI documents (e.g. Swashbuckle attributes in ASP.NET — see Documentation below). | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Editors | Authoring tools producing and previewing OpenAPI documents (e.g. Swagger Editor). | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Validators | Tools checking a document against the spec schema (spec conformance). | Technical Control | `(root) > Verification` |
| OpenAPI > Contract testing | Tools checking an implementation against its document (interface conformance). | Technical Control | `(root) > Validation` |
| OpenAPI > Renderers | Documentation UIs realizing a document for humans (e.g. Swagger UI, ReDoc — see Configuration below). | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Generators | Family of build-time tools *implementing* the standard in two directions: docs-from-code (emit the document from annotated code) and code-from-docs (emit code from the document). | Mechanism & Capability | `(root) > Technical Mechanism` |
| OpenAPI > Generators > Generator direction (docs-from-code vs code-from-docs) | Typology: docs-from-code scans code and emits `openapi.yaml/json`; code-from-docs reads the document and emits clients, servers, and stubs. | Mechanism & Capability | `(root) > Technical Capability` |
| OpenAPI > Generators > Document generators (docs-from-code) | Tools that scan annotated code and emit the OpenAPI document; the code-first practice path. | Mechanism & Capability | `(root) > Technical Mechanism` |
| OpenAPI > Generators > Document generators > `swagger-maven-plugin` (`io.swagger.core.v3`) | Maven plugin *implementing* OAS resolution from JAX-RS code (javax and `-jakarta` artifacts); scans annotations and writes the document at build time. | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Generators > Document generators > `swagger-maven-plugin` > `resolve` goal | Build goal resolving the OpenAPI model from code, bound by default to the `compile` phase. | Technique | `(root) > Technical Act` |
| OpenAPI > Generators > Document generators > `swagger-maven-plugin` > `resourcePackages` / `resourceClasses` | Scan scope: which JAX-RS packages or classes are introspected for paths and operations. | Requirements & Definition | `(root) > Technical Parameter` |
| OpenAPI > Generators > Document generators > `swagger-maven-plugin` > `outputFileName` / `outputPath` / `outputFormat` | Emission coordinates: base file name, target directory, and format (`JSON`, `YAML`, `JSONANDYAML`). | Requirements & Definition | `(root) > Technical Parameter` |
| OpenAPI > Generators > Document generators > `swagger-maven-plugin` > `prettyPrint` / `sortOutput` | Serialization flags controlling human-readable output and deterministic key ordering. | Requirements & Definition | `(root) > Technical Parameter` |
| OpenAPI > Generators > Document generators > `swagger-maven-plugin` > `configurationFilePath` / `openAPI` Info input | Optional seed: YAML config file and/or `openAPI` Info block (title, version, description, license) merged with the scanned model. | Requirements & Definition | `(root) > Technical Specification` |
| OpenAPI > Generators > Document generators > `swagger-maven-plugin` > Annotation inputs | JAX-RS plus `swagger-annotations` / `swagger-jaxrs2` markers (`@OpenAPIDefinition`, `@Operation`, `@Parameter`, `@Schema`) consumed by the scan. | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Generators > Document generators > `swagger-maven-plugin` > Emitted `openapi.yaml` / `openapi.json` | Build output: the resolved OpenAPI document file (one OAS 3.x contract instance). | Requirements & Definition | `(root) > Technical Specification` |
| OpenAPI > Generators > Document generators > `springdoc-openapi-maven-plugin` (`org.springdoc`) | Spring Boot sibling: `generate` goal fetching the live `v3/api-docs` from a test-phase Boot app (with `spring-boot-maven-plugin` start/stop) and saving it (`apiDocsUrl`, `outputDir`, `outputFileName`). | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Generators > Document generators > `smallrye-openapi-maven-plugin` (MicroProfile) | MicroProfile/Jakarta EE sibling emitting the document from SmallRye OpenAPI annotations at build time. | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Generators > Code generators (code-from-docs) | Tools that read one OpenAPI document and emit clients, server stubs, and config; the contract-first practice path. | Mechanism & Capability | `(root) > Technical Mechanism` |
| OpenAPI > Generators > Code generators > `openapi-generator-maven-plugin` (`org.openapitools`) | Maven plugin *implementing* code generation (`generate` goal, default `generate-sources` phase; `inputSpec`, `generatorName`, `configOptions`, `output`). | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Generators > Code generators > `openapi-generator-maven-plugin` > `inputSpec` / `generatorName` | Entry contract plus target selector: the source document path and the named generator (e.g. `java`, `spring`, `python`). | Requirements & Definition | `(root) > Technical Parameter` |
| OpenAPI > Generators > Code generators > `swagger-codegen-maven-plugin` (`io.swagger`) | Predecessor code generator (Swagger Codegen lineage) with the same contract-first direction; superseded by OpenAPI Generator for OAS 3.x. | System Structure | `(root) > Constitutive Technical Object` |
| OpenAPI > Generated client | Client code realizing the described interface for a deployment (exemplar). | System Structure | `(root) > Production Technical Object` |
| OpenAPI > Generated server stub | Server skeleton realizing the described interface for a deployment (exemplar). | System Structure | `(root) > Production Technical Object` |
| OpenAPI > Gateway import | Gateway or mock realizing enforcement/mocking from the document (exemplar). | System Structure | `(root) > Production Technical System` |
| OpenAPI > Contract-first practice | Repeatable pattern: write the document, then generate/validate against it. | Technique | `(root) > Technical Practice` |
| OpenAPI > Code-first practice | Repeatable pattern: annotate code, then emit the document. | Technique | `(root) > Technical Practice` |
| OpenAPI > Linting practice | Repeatable pattern: enforce style and rules on documents (e.g. Spectral). | Technique | `(root) > Technical Practice` |
| OpenAPI > Versioning practice | Repeatable pattern: evolve the contract without breaking consumers. | Lifecycle & Continuity | `(root) > Technical Evolution` |
| OpenAPI > Evolution Swagger-2.0-to-OAS-3.1 | Historical trajectory: Swagger 2.0 → OAS 3.0 → OAS 3.1 (JSON Schema alignment). | Lifecycle & Continuity | `(root) > Technical Evolution` |

## Documentation

> How to document (annotate) an app so the OpenAPI document can be emitted code-first? The attributes below belong to the ASP.NET Swashbuckle annotation library — one *implementing* constitutive object from the decomposition above — not to OAS itself.

1. **[SwaggerOperation]**
    - Used to describe an API operation or endpoint.
    - Allows specifying the operation's HTTP method, path, and summary.
2. **[ProducesResponseType]**
    - Used to specify the possible HTTP response types and status codes for an operation.
3. **[SwaggerResponse]**
    - Used to document a single HTTP response for an operation, including its status code and description.
4. **[SwaggerRequestExample]**
    - Allows defining examples of request payloads for an operation.
5. **[SwaggerResponseExample]**
    - Allows defining examples of response payloads for an operation.
6. **[SwaggerRequestBody]**
    - Used to describe the request body of an operation.
7. **[SwaggerResponseHeader]**
    - Specifies a response header in the Swagger documentation.
8. **[SwaggerOperationFilter]**
    - Allows customizing the operation's Swagger documentation at runtime.
9. **[SwaggerSchemaFilter]**
    - Used for customizing the schema of a model in Swagger documentation.
10. **[SwaggerTag]**
    - Specifies tags for organizing and categorizing operations.
11. **[SwaggerSecurityRequirement]**
    - Defines security requirements for an operation.
12. **[SwaggerSecurity]**
    - Used to describe security schemes and requirements for an API.
13. **[SwaggerIgnore]**
    - Excludes an operation or property from being documented in Swagger.
14. **[FromQuery]**
    - Used to specify that a parameter should be bound from the query string in HTTP requests.
15. **[FromRoute]**
    - Specifies that a parameter should be bound from the route in HTTP requests.
16. **[FromHeader]**
    - Binds a parameter from an HTTP header.
17. **[FromForm]**
    - Specifies that a parameter should be bound from the form data in a POST request.
18. **[ApiVersion]**
    - Specifies the API version for a controller or action.

## Configuration

> `swagger-config.yaml` — configuration of Swagger UI, one *realizing* renderer from the decomposition above, not of OAS itself.

Swagger UI provides several configuration options that allow you to customize its behavior and appearance when documenting your APIs. Here's a list of some common Swagger UI options and their descriptions:

1. **url**:
    - Specifies the URL to the Swagger/OpenAPI definition file (JSON or YAML) that Swagger UI should use for documentation.
2. **urls**:
    - Allows you to provide multiple URL definitions, enabling you to switch between different API versions or services in the same Swagger UI instance.
3. **oauth**:
    - Enables OAuth 2.0 authorization support in Swagger UI, allowing users to authenticate and access secured API endpoints.
4. **validatorUrl**:
    - Specifies the URL of an external Swagger validator service. This is used to validate the Swagger/OpenAPI definition against a schema.
5. **docExpansion**:
    - Controls the initial state of the documentation sections. Options include "list," "full," "none," or "fullOnStartup."
6. **defaultModelRendering**:
    - Defines how models are initially displayed. Options include "model," "schema," or "example."
7. **displayRequestDuration**:
    - Specifies whether to display the request duration (response time) for each API request.
8. **filter**:
    - Allows you to apply a filter to the API operations to display only a subset of endpoints.
9. **operationsSorter**:
    - Controls the sorting of API operations in the UI. Options include "alpha," "method," or a custom function.
10. **tagsSorter**:
    - Defines the sorting of tags in the UI. Options include "alpha" or a custom function.
11. **deepLinking**:
    - Enables deep linking to specific sections of the documentation, which updates the URL as you navigate through the documentation.
12. **showExtensions**:
    - Displays vendor extension fields (fields not part of the official OpenAPI specification) in the UI.
13. **displayOperationId**:
    - Specifies whether to display the operation ID next to each operation in the UI.
14. **defaultModelExpandDepth** and **defaultModelsExpandDepth**:
    - Set the default depth for models and model schemas that are expanded by default.
15. **tryItOutEnabled**:
    - Controls whether the "Try it out" functionality is enabled for making API requests directly from the UI.
16. **showCommonExtensions**:
    - Displays common extensions (fields defined by Swagger/OpenAPI extensions) in the UI.
17. **useRequestInterceptor** and **useResponseInterceptor**:
    - Allows you to specify custom JavaScript functions to intercept and modify API requests and responses.
18. **configUrl**:
    - Specifies a URL to an external configuration file to customize Swagger UI settings.
19. **layout**:
    - Specifies the layout of the UI. Options include "BaseLayout," "StandaloneLayout," or a custom layout class.
20. **onComplete**:
    - A JavaScript callback function that is executed when Swagger UI has finished loading.

These options can be set when configuring Swagger UI in your ASP.NET Core or Node.js application. Depending on your use case and requirements, you can customize Swagger UI to suit your needs by configuring these options accordingly.

## References

- [OpenAPI Specification (spec.openapis.org)](https://spec.openapis.org/oas/latest.html)
- [OpenAPI Initiative](https://www.openapis.org/)
- [Swagger](https://swagger.io/)
- [OpenAPI Generator](https://openapi-generator.tech/)
- [JSON Schema](https://json-schema.org/)
- [Enhance Swagger Documentation with Annotations in ASP.NET core](https://medium.com/@niteshsinghal85/enhance-swagger-documentation-with-annotations-in-asp-net-core-d2981803e299)
- [Documenting Additional API endpoints in Swagger in ASP.Net Core](https://medium.com/@niteshsinghal85/documenting-additional-api-endpoints-in-swagger-in-asp-net-core-59da9c84e4ba)
- [GraphQL](note.html?n=cto/es/multinode/graphql.md)
- [Philosophia Artium Technicarum et Operis](note.html?n=general/philosophia-artium-technicarum-et-operis.md)
