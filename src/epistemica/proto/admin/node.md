# Note Creation

> Let’s produce a set of nodes for the element specified in the `Work Description` section that follows the `Schema`, under the constraints and objectives specified in the document.

## Work Description

- Decision Theory: A set of explanatory frameworks and practical tools for guiding decision-making.
- Decision-Making: The set of processes related to the task of making a decision.

## Goal Set

- To construct a rigorous, domain-general conceptual structure taxonomy that formally characterizes epistemic practice as a structured system of knowledge acquisition, encoding, transformation, validation, and application—independent of any specific computational tooling implementation.
- Relational Ontology Goal: Construct a comprehensive edge-type framework that captures all structural, operational, normative, dynamic, and infrastructural relations within epistemic practice.
- Knowledge Systems Modeling Goal: Provide a formal foundation for modeling how epistemic agents and institutions generate, maintain, and evolve knowledge.
- To systematically learn from other epistemic agents by modeling how they parse, represent, validate, critique, correct, and refine artifacts that refer to reality.
- Study tools, and mechanisms, and other dimenios to be a better epistemic agent.
- To develop structured methods for detecting epistemic failure modes such as bias, distortion, uncertainty, invalid inference, and representational limitations.
- To identify and formalize best practices for observation, inference, validation, and knowledge correction across disciplines.
- To study epistemic tools, reasoning mechanisms, methodological frameworks, and cognitive strategies in order to improve epistemic performance.
- To master core epistemic tool set domains including mathematics, logic, statistics, computation, scientific methodology, systems theory, modeling, simulation, measurement science, and domain-specific analytical frameworks in order to maximize epistemic capability.
- Note: That epistemic artifact (are description of the world) - they are not parametrized description - but descriptions - that can be valiaded - not a theoretical tool Structural Causal Model (SCM) is a artifact but Structural Caussaling Modelling is the tool toolset.

## Formulation

> Which are the sets of concept that characterize  epistemic practice? How to capture all of this concept in a database?

| **Category** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Reality** | The ontological substrate comprising the actual states, structures, processes, entities, and causal dynamics that exist independently (or partially independently) of any observer’s representation. Reality constitutes the ultimate source domain from which observations are extracted, against which epistemic artifacts are validated, and whose structure constrains possible knowledge. It includes both observable and unobservable phenomena, latent mechanisms, causal architectures, and state trajectories across time. | Physical systems, biological organisms, chemical reactions, social institutions, computational systems, economic systems, ecological networks, latent variables, hidden causal mechanisms, dynamical state spaces, material processes, environmental structures. |
| **Observation Interface & Recoding** | The sensorimotor boundary + inscription process that transduces a Domain Snapshot into a persistent encoded artifact. Includes transduction, sampling, quantization, encoding, and storage. | CMOS sensor + ADC + JPEG + SD card; thermocouple + data logger + CSV file; human retina + V1 cortex + working memory. |
|  **Concrete Epistemic Artifact** | Structured object and **specific object** that encodes claims, constraints, or distributions over reality; the primary carrier of semantic content. | ***Zero free parameters**** – every coefficient, distribution, variable, and functional form is concretely specified. | Yes – can be evaluated as correct/incorrect against reality. | `y = 2.3x + 1.7` (fitted linear model); specific CSV file `[2.1, 3.4, 5.6]`; a particular DAG with all edges and functional forms fixed. - Propositions, numbers, datasets, differential equations, probabilistic models, Hypergraphs, property encoding, |
| **Epistemic Blueprint** | Encoding format or substrate in which artifacts are expressed; constrains manipulation and interpretation. | Directed Acyclic Graph (DAG), Structural Equation (functional notation), Polynomial Equation, … |
| **Epistemic Agent** | Entity that performs epistemic operations by applying tools to artifacts. | Scientist, analyst, research institution, machine learning system, automated pipeline |
| **Epistemic Process (Activity)** | Ordered sequence of tool applications over time; defines the dynamics of knowledge construction. | Scientific method, Bayesian updating loop, training pipeline, experimental cycle |
| **Epistemic Standard** | Normative criteria used to evaluate validity, correctness, or acceptability of artifacts and processes. | Logical consistency, statistical significance, reproducibility, robustness, falsifiability |
| **Encoding Substrate** | Segment of reality that the epistemic practice targets or models. | Physical systems, biological systems, social systems, computational systems |
| **Epistemic Constraint** | Limitation that bounds what can be known or inferred within the system. | Noise, limited data, computational complexity, identifiability issues, measurement error, ignorance, intractability, stochasticity, higher-order stochasticity, chaos, nonlinearity, uncertainty propagation, and observational limitations. |
| **Epistemic Infrastructure** | Supporting environment that enables storage, computation, measurement, and communication of artifacts. | Sensors, laboratories, software systems, databases, notebooks, scientific publications |
| **Epistemic Feedback** | Signal from reality (or from another artifact) that resists or confirms prior predictions or actions; primary driver of learning and error correction. | Prediction error (residual), unexpected observation, failed intervention, successful replication, sensor saturation, model divergence, comparison between two Domain Snapshots taken at different times. |
| **Epistemic Act** | Primitive, non‑decomposable operation performed by an agent: attending, discriminating, remembering, anticipating, intervening, comparing, observing (which invokes Observation Encoding). | Attending to a sensor reading, detecting a difference, recalling an observation, emitting a prediction, pressing a measurement probe, judging similarity, encoding a raw signal into a digital value. |
| **Epistemic Principle** | Foundational normative, structural, or strategic rule that governs how epistemic agents should construct, validate, organize, or revise knowledge. Principles shape the selection of standards, tools, and processes by defining the underlying logic of inquiry. | Empiricism, falsifiability, parsimony (Occam’s Razor), Bayesian coherence, causal reasoning, reproducibility, predictive adequacy, reductionism, systems thinking, explanatory power, measurement invariance |
| **Epistemic Strategy** | Adaptive, context-dependent planning logic that governs how epistemic agents allocate resources, sequence inquiry, navigate uncertainty, and select investigative pathways to achieve epistemic objectives under real-world constraints. Strategies operationalize principles into executable inquiry architectures by determining search order, decomposition methods, validation sequencing, exploration/exploitation balance, and intervention priorities. | Exploratory data analysis before formal modeling; hypothesis-first experimentation; reductionist decomposition; systems-level integrative analysis; sequential Bayesian updating; active learning; robustness-first validation; coarse-to-fine modeling; simulation-before-deployment; high-throughput screening; falsification-driven testing; divide-and-conquer investigation; iterative refinement; uncertainty minimization; adversarial stress testing; hierarchical model building. |
| **Epistemic Framework** | Abstract conceptual, inferential, and formal systems that structure how epistemic agents interpret observations, organize knowledge, generate explanations, and reason about reality. Frameworks define the overarching cognitive architecture within which principles, operators, and artifacts are selected and deployed. | Logic, causal inference, Bayesian reasoning, statistical reasoning, systems theory, cybernetics, information theory, mechanistic modeling, optimization theory, game theory, control theory, reductionist frameworks, complexity science, decision theory |
| **Epistemic Operator** | Formal or procedural mechanism used to construct, transform, representation form ( abstract artifact)or validate epistemic artifacts. | Algebraic manipulation, statistical inference, optimization algorithms, simulation methods, measurement procedures,  generic or abstract class of artifact or let’s called it by representational form. |
| **Meta-Epistemic Layer** | Supporting material, energetic, social, and institutional environment that enables storage, computation, measurement, and communication of artifacts over time. | Sensors (thermocouples, cameras), laboratories (clean rooms), software systems (Jupyter, Git), databases, scientific publications, power grid, funding agencies, data repositories. |

## Rules

> Use this rules to guide the process of identication of concept that drives - underlies - explain or are used the epistemic practice of agents.

| Rule                                                        | Definition (Operational Form)                                                                                                                                         | Primary Distinction Axis           |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **1. Classify by epistemic function**                       | Assign each element to a single primary epistemic role (artifact, tool, Artifact Form (Artifact Blueprint), agent, act, process, principle, standard, constraint, infrastructure, domain). | Global functional typing           |
| **2. Artifact vs Operator separation**                          | An Epistemic Artifact is a fully instantiated, truth-apt representation of a specific domain that contains zero free parameters (no placeholders, unspecified coefficients, or unbound variables) and exists as a concrete particular rather than a class, set, or schema; whereas an Epistemic Operator is a procedure, algorithm, or method that actively transforms, infers, evaluates, or produces such representations without itself being a representation. | Representation vs operation        |
| **3. Principle vs Standard separation**                     | Principle = foundational explanatory constraint; Standard = operationalized evaluative criterion derived from principles.                                             | Foundational vs normative          |
| **4. Act vs Process separation**                            | Act = atomic epistemic operation; Process = ordered composition of acts with temporal structure.                                                                      | Atomic vs composite temporality    |
| **5. Artifact form as a distinct category**                | Encoding forms are syntactic/structural systems that define representational validity but do not assert truths or perform operations.                                 | Meta-representational substrate    |
| **6. Artifact form are inert; tools are active**           | Encoding forms define valid expressions; tools execute transformations, inference, or validation over those expressions.                                              | Syntax vs computation              |
| **7. Artifact requires instantiation within Artifact Form (Artifact Blueprint)** | An artifact exists only when an encoding form is populated with domain-referential, truth-evaluable content.                                                          | Structural instantiation condition |
| **8. Domain is ontologically independent**                  | The target domain exists independently of its representations and must be identified separately from epistemic constructs.                                            | Ontology vs representation         |
| **9. Infrastructure as enabling substrate**                 | Infrastructure consists of physical/computational systems enabling epistemic operations without encoding domain content.                                              | Support vs content                 |
| **10. Constraints as epistemic limits**                     | Constraints are conditions that restrict possible states of knowledge or valid inference, not descriptive claims.                                                     | Limitation vs representation       |
| **11. Feedback as corrective mechanism**                    | Feedback is any process that evaluates and adjusts epistemic outputs based on error or deviation.                                                                     | Correction dynamics                |
| **12. Prevent category collapse (no drift)**                | An entity must not simultaneously belong to multiple primary epistemic categories under the same role.                                                                | Mutual exclusivity                 |
| **13. Explicit relational modeling required**               | All epistemic relations (causal, inferential, compositional) must be explicitly represented, not implied.                                                             | Structural explicitness            |
| **14. Structural interrogation of candidates**              | Classification requires checking decomposability, referentiality, and operational behavior.                                                                           | Validation criteria                |
| **15. Artifact requires empirical or domain grounding**     | Artifacts must refer to or model a concrete or well-defined domain state, not abstract templates.                                                                     | Grounding condition                |
| **16. Tools must transform or produce artifacts**           | A valid tool must output, modify, evaluate, or generate epistemic artifacts as its primary function.                                                                  | Operational closure                |
| **17. Artifact vs Artifact Form** | The artifact form - one it's abstract - cannot not be constrated with reality - and the other it.|
|**17 If any cannot be associated with a category list them as unclasify.**|...|

### Edge Type

> Which are the edged types?

| **Relation Family** | **Relation Type** | **Description** | **Relation Signature** | **Use** |
| --- | --- | --- | --- | --- |
| Representational | observes | Captures or measures a domain snapshot through perception or instrumentation. | Observation Interface → Domain Snapshot | Empirical sensing, experiments, perception systems |
| Representational | encodes | Transduces observations into persistent epistemic artifacts. | Observation Interface / Agent → Epistemic Artifact | Data acquisition, memory, recording |
| Representational | expresses_in | Instantiates an artifact in a specific representational substrate or encoding format. | Epistemic Artifact → Encoding Format | Formal notation, code, schemas |
| Representational | formalizes | Converts raw, implicit, or informal content into structured epistemic representation. | Operator / Agent → Epistemic Artifact | Ontologies, models, formal systems |
| Representational | abstracts_from | Extracts generalized structures or principles from lower-level artifacts. | Artifact / Theory → Lower-Level Artifact | Theory building, pattern extraction |
| Structural | composed_of | Defines constituent internal components, operations, or stages of an entity. | Operator / Process / Artifact → Subcomponent | Operator architecture, workflow decomposition |
| Structural | has_parameter | Specifies formal adjustable variables or governing parameters. | Operator / Model → Parameter | Configuration, tuning, optimization |
| Structural | has_input | Defines required epistemic inputs. | Operator / Process → Input Artifact | Pipeline specification |
| Structural | has_output | Defines produced outputs. | Operator / Process → Output Artifact | Output specification |
| Structural | implements_principle | Operationalizes an underlying formal or mathematical principle. | Operator → Principle | Fourier methods, Bayesian inference |
| Operational | uses | Agent or higher-order system employs a tool. | Agent / Operator → Operator | Scientific inquiry, automation |
| Operational | performs | Agent executes a process. | Agent → Process | Research, experimentation |
| Operational | acts_on | Operator, act, or process manipulates an artifact or domain. | Operator / Process / Act → Artifact / Domain | Data processing, intervention |
| Operational | produces | Generates a new artifact or epistemic output. | Agent / Operator / Process → Artifact | Model creation, inference products |
| Operational | transforms | Converts one artifact into another epistemic state. | Operator / Process → Artifact | Signal processing, inference |
| Operational | predicts | Produces projected future epistemic claims. | Model / Artifact → Future State | Forecasting, simulation |
| Operational | decomposes | Breaks an artifact into constituent analyzable components. | Operator → Artifact Components | Fourier analysis, PCA |
| Operational | integrates | Combines multiple epistemic sources into unified artifacts. | Operator / Process → Unified Artifact | Fusion, synthesis |
| Operational | estimates | Infers latent states, parameters, or distributions. | Operator / Process → Estimated Artifact | Bayesian methods, econometrics |
| Normative - Validation | conforms_to | Satisfies standards or evaluative criteria. | Artifact / Operator / Process → Standard | Scientific validity |
| Normative - Validation | evaluated_by | Subject is assessed by evaluative mechanism. | Artifact / Process → Standard / Operator | Benchmarking, review |
| Normative - Validation | validates | Confirms adequacy or correctness. | Process / Evidence → Artifact | Verification, replication |
| Normative - Validation | refutes | Disconfirms or falsifies a claim. | Evidence / Feedback → Artifact | Falsification |
| Normative - Validation | supports | Provides evidential reinforcement. | Evidence / Artifact → Artifact | Justification |
| Constraint | is_bounded_by | Subject exists under limiting conditions. | Artifact / Operator / Process → Constraint | Complexity, uncertainty |
| Constraint | constrains | Restricts epistemic operation, expressibility, or validity. | Constraint / Format → Subject | Formal, practical, methodological limitations |
| Constraint | distorts | Introduces systematic deviation or corruption. | Constraint → Artifact / Observation | Bias, noise |
| Constraint | depends_on | Requires enabling conditions. | Subject → Dependency | Infrastructure, quality prerequisites |
| Dynamic - Feedback | triggers | Feedback initiates epistemic adaptation. | Feedback → Process / Artifact | Revision, anomaly correction |
| Dynamic - Feedback | updates | Revises epistemic state based on new evidence. | Evidence / Feedback → Artifact / Process | Learning, Bayesian updating |
| Dynamic - Feedback | feeds_back_to | Recursive return of output into prior stages. | Output → Prior Process | Adaptive loops |
| Dynamic - Feedback | iterates_on | Repeatedly refines prior artifacts or processes. | Process → Prior Artifact / Process | Continuous improvement |
| Dynamic - Feedback | evolves_into | Develops into more advanced epistemic form. | Artifact / Process → Advanced Artifact / Process | Theory maturation |
| Infrastructure | provides | Supplies enabling material, computational, or sensory resources. | Infrastructure → Agent / Operator / Process | Labs, compute systems |
| Infrastructure | hosts | Sustains persistent epistemic systems or agents. | Institution / Infrastructure → Agent / System | Universities, organizations |
| Infrastructure | stores | Preserves epistemic artifacts over time. | Infrastructure → Artifact | Archives, repositories |
| Infrastructure | communicates | Transmits artifacts across epistemic agents. | Infrastructure / Artifact → Agent / Community | Journals, APIs |
| Infrastructure | standardizes | Establishes shared representational or methodological conventions. | Institution / Infrastructure → Standard / Format | Protocols, schemas |
| Meta-Epistemic | monitors | Tracks epistemic system quality or performance. | Meta-System → E |  |

> Note: The specific components will be formulated in the subsequent sections.

### Sample Dataset

```json
[
  {
    "id": "standard_04",
    "name": "Law of Large Numbers",
    "category": "Epistemic Standard",
    "inheritanceLevel": 1,
    "description": "Convergence of averages",
    "functionalRoles": ["norm"],
    "realityDomains": [],
    "historicalContext": {
      "summary": "",
      "chronology": []
    },
    "specific": {},
    "relationships": [
      {
        "relationshipType": "subtype_of",
        "targetNodeId": "cat_standard",
        "attributes": {}
      }
    ],
    "metadata": {
      "tags": ["stochastic", "convergence", "statistics", "theory"],
      "confidenceScore": 1.0,
      "sourceReference": "curated",
      "createdAt": "",
      "auditTrail": []
    }
  },
  {
    "id": "process_05",
    "name": "Abduction",
    "category": "Epistemic Process (Activity)",
    "inheritanceLevel": 1,
    "description": "Abduction is an epistemic process aimed at inferring and ranking candidate explanations for a given set of observations, based on how likely those observations would be under each hypothesis in a space of possible worlds.",
    "functionalRoles": ["process"],
    "realityDomains": [],
    "historicalContext": {
      "summary": "",
      "chronology": []
    },
    "specific": {},
    "relationships": [
      {
        "relationshipType": "subtype_of",
        "targetNodeId": "cat_process",
        "attributes": {}
      }
    ],
    "metadata": {
      "tags": ["#activity"],
      "confidenceScore": 1.0,
      "sourceReference": "curated",
      "createdAt": "",
      "auditTrail": []
    }
  }
]
```

## Schemna

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/conceptual-structure-node.schema.json",
  "title": "Conceptual Structure Typing Node Schema",
  "description": "Schema for representing the concepts used to parse and represent the epistemic practice of agents.",
  "type": "object",
  "required": [
    "id",
    "name",
    "category",
    "inheritanceLevel",
    "description",
    "functionalRoles",
    "realityDomains",
    "historicalContext",
    "specific",
    "relationships",
    "metadata",
    "references"
  ],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for the node."
    },
    "name": {
      "type": "string",
      "description": "Canonical name of the conceptual structure."
    },
    "category": {
      "type": "string",
      "enum": [
        "reality",
        "observationInterface",
        "concreteEpistemicArtifact",
        "epistemicBlueprint",
        "epistemicAgent",
        "epistemicProcess",
        "epistemicStandard",
        "epistemicDomain",
        "epistemicConstraint",
        "epistemicInfrastructure",
        "epistemicFeedback",
        "epistemicAct",
        "epistemicPrinciple",
        "epistemicStrategy",
        "epistemicFramework",
        "epistemicOperator",
        "metaEpistemicLayer"
      ],
      "description": "Ontological classification of the epistemic node."
    },
    "inheritanceLevel": {
      "type": "integer",
      "minimum": 0,
      "description": "Depth within conceptual or taxonomic inheritance hierarchy."
    },
    "description": {
      "type": "string",
      "description": "Formal description of the structure."
    },
    "longDescription": {
      "type": "string",
      "description": "Extended technical exposition providing deeper ontological, operational, historical, and epistemic detail beyond the primary description field. Intended for comprehensive conceptual analysis, ambiguity resolution, and advanced interpretive documentation."
    },
    "functionalRoles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Primary functional roles served by this node."
    },
    "realityDomains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Domains of reality or systems in which this node operates."
    },
    "historicalContext": {
      "type": "object",
      "required": [
        "summary",
        "chronology"
      ],
      "properties": {
        "summary": {
          "type": "string"
        },
        "chronology": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "year",
              "event",
              "associatedContext"
            ],
            "properties": {
              "year": {
                "type": "number"
              },
              "event": {
                "type": "string"
              },
              "associatedContext": {
                "type": "string"
              }
            },
            "additionalProperties": false
          }
        }
      },
      "additionalProperties": false
    },
    "specific": {
      "type": "object",
      "description": "Category-specific extension fields."
    },
    "relationships": {
      "type": "array",
      "description": "Typed edges connecting this node to others.",
      "items": {
        "type": "object",
        "required": [
          "relationshipType",
          "targetNodeId",
          "description"
        ],
        "properties": {
          "relationshipFamily": {
            "type": "string",
            "enum": [
              "representational",
              "structural",
              "operational",
              "normativeValidation",
              "constraint",
              "dynamicFeedback",
              "infrastructure",
              "metaEpistemic"
            ]
          },
          "relationshipType": {
            "type": "string",
            "enum": [
              "observes",
              "encodes",
              "expresses_in",
              "formalizes",
              "abstracts_from",
              "composed_of",
              "has_parameter",
              "has_input",
              "has_output",
              "implements_principle",
              "uses",
              "performs",
              "acts_on",
              "produces",
              "transforms",
              "predicts",
              "decomposes",
              "integrates",
              "estimates",
              "conforms_to",
              "evaluated_by",
              "validates",
              "refutes",
              "supports",
              "is_bounded_by",
              "constrains",
              "distorts",
              "depends_on",
              "triggers",
              "updates",
              "feeds_back_to",
              "iterates_on",
              "evolves_into",
              "provides",
              "hosts",
              "stores",
              "communicates",
              "standardizes",
              "monitors",
              "governs",
              "audits",
              "optimizes"
            ]
          },
          "targetNodeId": {
            "type": "string"
          },
          "description": {
            "type": "string"
          }
        }
      }
    },
    "metadata": {
      "type": "object",
      "required": [
        "tags",
        "confidenceScore",
        "sourceReference",
        "createdAt",
        "auditTrail"
      ],
      "properties": {
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "categoryAmbiguity": {
          "type": "object",
          "description": "Captures alternative plausible category classifications when the node spans multiple epistemic layers or exhibits ontological ambiguity.",
          "required": [
            "isAmbiguous",
            "primaryJustification",
            "alternativeCategories"
          ],
          "properties": {
            "isAmbiguous": {
              "type": "boolean",
              "description": "Whether this concept plausibly belongs to multiple categories."
            },
            "primaryJustification": {
              "type": "string",
              "description": "Rationale for selecting the primary category over alternatives."
            },
            "alternativeCategories": {
              "type": "array",
              "description": "Other plausible epistemic categories for this node.",
              "items": {
                "type": "object",
                "required": [
                  "category",
                  "justification",
                  "confidence"
                ],
                "properties": {
                  "category": {
                    "type": "string",
                    "enum": [
                      "reality",
                      "observationInterface",
                      "concreteEpistemicArtifact",
                      "epistemicBlueprint",
                      "epistemicAgent",
                      "epistemicProcess",
                      "epistemicStandard",
                      "epistemicDomain",
                      "epistemicConstraint",
                      "epistemicInfrastructure",
                      "epistemicFeedback",
                      "epistemicAct",
                      "epistemicPrinciple",
                      "epistemicStrategy",
                      "epistemicFramework",
                      "epistemicOperator",
                      "metaEpistemicLayer"
                    ]
                  },
                  "justification": {
                    "type": "string"
                  },
                  "confidence": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 1
                  }
                },
                "additionalProperties": false
              }
            }
          },
          "additionalProperties": false
        },
        "confidenceScore": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "sourceReference": {
          "type": "string"
        },
        "createdAt": {
          "type": "string",
          "format": "date-time"
        },
        "auditTrail": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "reviewDate",
              "reviewNote"
            ],
            "properties": {
              "reviewDate": {
                "type": "string",
                "format": "date"
              },
              "reviewNote": {
                "type": "string"
              }
            },
            "additionalProperties": false
          }
        }
      },
      "additionalProperties": false
    },
    "references": {
      "type": "array",
      "description": "External references, citations, papers, books, standards, repositories, datasets, or knowledge sources associated with the conceptual node.",
      "items": {
        "type": "object",
        "required": [
          "title",
          "description"
        ],
        "properties": {
          "title": {
            "type": "string",
            "description": "Canonical title or name of the reference."
          },
          "link": {
            "type": "string",
            "format": "uri",
            "description": "Optional URL, DOI, repository link, or other resolvable reference identifier."
          },
          "description": {
            "type": "string",
            "description": "Short explanation of the relevance or contribution of the reference."
          }
        },
        "additionalProperties": false
      }
    }
  },
  "allOf": [
    {
      "if": {
        "properties": {
          "category": {
            "const": "reality"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/c"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "observationInterface"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/observationInterfaceSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "concreteEpistemicArtifact"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/concreteEpistemicArtifactSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicBlueprint"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicBlueprintSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicAgent"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicAgentSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicProcess"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicProcessSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicStandard"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicStandardSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicDomain"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicDomainSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicConstraint"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicConstraintSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicInfrastructure"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicInfrastructureSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicFeedback"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicFeedbackSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicAct"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicActSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicPrinciple"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicPrincipleSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicStrategy"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicStrategySpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicFramework"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicFrameworkSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "epistemicOperator"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/epistemicOperatorSpecific"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "category": {
            "const": "metaEpistemicLayer"
          }
        }
      },
      "then": {
        "properties": {
          "specific": {
            "$ref": "#/$defs/metaEpistemicLayerSpecific"
          }
        }
      }
    }
  ],
  "$defs": {
    "realitySpecific": {
      "type": "object",
      "required": [
        "ontologicalClass",
        "observability",
        "temporalProfile",
        "levelOfExistence",
        "conceptEvaluationNote"
      ],
      "properties": {
        "ontologicalClass": {
          "type": "string",
          "enum": [
            "Ontic.Existential.Substantive",
            "Ontic.Existential.Processual",
            "Ontic.Existential.Entity",
            "Ontic.Existential.Mechanism",
            "Ontic.Dynamical.Event",
            "Ontic.Dynamical.Process",
            "Ontic.Dynamical.Stochastic",
            "Ontic.Dynamical.EventStream",
            "Ontic.Dynamical.MixtureEventStream",
            "Ontic.Dynamical.Phenomena",
            "Ontic.Dynamical.Epiphenomena",
            "Ontic.Agency.Agent",
            "Synontic.Property",
            "Synontic.Aspect",
            "Synontic.StateModel",
            "Synontic.VariableAspect"
          ],
          "description": "Primary ontological class from the controlled vocabulary."
        },
        "observability": {
          "type": "string",
          "enum": [
            "observable",
            "latent",
            "partiallyObservable"
          ],
          "description": "Directness of epistemic access."
        },
        "temporalProfile": {
          "type": "string",
          "enum": [
            "endurant",
            "perdurant",
            "transient"
          ],
          "description": "How the entity exists in time."
        },
        "levelOfExistence": {
          "type": "string",
          "enum": [
            "zero-order",
            "first-order",
            "second-order",
            "third-order"
          ],
          "description": "Position in the representation hierarchy."
        },
        "conceptEvaluationNote": {
          "type": "string",
          "description": "Free-text epistemic evaluation of the concept as a tool."
        }
      },
      "additionalProperties": false
    },
    "observationInterfaceSpecific": {
      "type": "object",
      "required": [
        "transductionMethod",
        "samplingMethod",
        "encodingMethod"
      ],
      "properties": {
        "transductionMethod": {
          "type": "string"
        },
        "samplingMethod": {
          "type": "string"
        },
        "encodingMethod": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "concreteEpistemicArtifactSpecific": {
      "type": "object",
      "required": [
        "modality",
        "structure",
        "truthEvaluability",
        "noiseModel"
      ],
      "properties": {
        "modality": {
          "type": "string",
          "enum": [
            "sensorimotor",
            "computational",
            "cognitive",
            "institutional"
          ]
        },
        "structure": {
          "type": "string"
        },
        "truthEvaluability": {
          "type": "boolean"
        },
        "noiseModel": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicBlueprintSpecific": {
      "type": "object",
      "required": [
        "representationType",
        "formalism",
        "expressiveLimits"
      ],
      "properties": {
        "representationType": {
          "type": "string"
        },
        "formalism": {
          "type": "string"
        },
        "expressiveLimits": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "additionalProperties": false
    },
    "epistemicAgentSpecific": {
      "type": "object",
      "required": [
        "agentType",
        "capabilities",
        "autonomyLevel",
        "goalStructure"
      ],
      "properties": {
        "agentType": {
          "type": "string",
          "enum": [
            "human",
            "machine",
            "hybridSystem",
            "institution"
          ]
        },
        "capabilities": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "autonomyLevel": {
          "type": "string"
        },
        "goalStructure": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicProcessSpecific": {
      "type": "object",
      "required": [
        "processType",
        "inputs",
        "outputs",
        "validationMethod"
      ],
      "properties": {
        "processType": {
          "type": "string"
        },
        "inputs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "outputs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "validationMethod": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicStandardSpecific": {
      "type": "object",
      "required": [
        "standardType",
        "complianceCriteria",
        "measurementBasis"
      ],
      "properties": {
        "standardType": {
          "type": "string"
        },
        "complianceCriteria": {
          "type": "string"
        },
        "measurementBasis": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicDomainSpecific": {
      "type": "object",
      "required": [
        "domainScope",
        "knowledgeBoundaries",
        "primaryObjects"
      ],
      "properties": {
        "domainScope": {
          "type": "string"
        },
        "knowledgeBoundaries": {
          "type": "string"
        },
        "primaryObjects": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "additionalProperties": false
    },
    "epistemicConstraintSpecific": {
      "type": "object",
      "required": [
        "constraintType",
        "boundedResource",
        "failureMode"
      ],
      "properties": {
        "constraintType": {
          "type": "string"
        },
        "boundedResource": {
          "type": "string"
        },
        "failureMode": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicInfrastructureSpecific": {
      "type": "object",
      "required": [
        "infrastructureType",
        "storageMechanism",
        "communicationMode"
      ],
      "properties": {
        "infrastructureType": {
          "type": "string"
        },
        "storageMechanism": {
          "type": "string"
        },
        "communicationMode": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicFeedbackSpecific": {
      "type": "object",
      "required": [
        "feedbackType",
        "signalSource",
        "adaptationTarget"
      ],
      "properties": {
        "feedbackType": {
          "type": "string"
        },
        "signalSource": {
          "type": "string"
        },
        "adaptationTarget": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicActSpecific": {
      "type": "object",
      "required": [
        "actType",
        "intent",
        "target",
        "outcome"
      ],
      "properties": {
        "actType": {
          "type": "string"
        },
        "intent": {
          "type": "string"
        },
        "target": {
          "type": "string"
        },
        "outcome": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicPrincipleSpecific": {
      "type": "object",
      "required": [
        "principleType",
        "formalStatement",
        "applicability"
      ],
      "properties": {
        "principleType": {
          "type": "string"
        },
        "formalStatement": {
          "type": "string"
        },
        "applicability": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicStrategySpecific": {
      "type": "object",
      "required": [
        "strategyType",
        "optimizationGoal",
        "decisionHeuristic"
      ],
      "properties": {
        "strategyType": {
          "type": "string"
        },
        "optimizationGoal": {
          "type": "string"
        },
        "decisionHeuristic": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicFrameworkSpecific": {
      "type": "object",
      "required": [
        "frameworkType",
        "coreAssumptions",
        "integrationScope"
      ],
      "properties": {
        "frameworkType": {
          "type": "string"
        },
        "coreAssumptions": {
          "type": "string"
        },
        "integrationScope": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "epistemicOperatorSpecific": {
      "type": "object",
      "required": [
        "operatorType",
        "transformationRule",
        "operandType"
      ],
      "properties": {
        "operatorType": {
          "type": "string"
        },
        "transformationRule": {
          "type": "string"
        },
        "operandType": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "metaEpistemicLayerSpecific": {
      "type": "object",
      "required": [
        "reflectionScope",
        "governanceRole",
        "recursiveDepth"
      ],
      "properties": {
        "reflectionScope": {
          "type": "string"
        },
        "governanceRole": {
          "type": "string"
        },
        "recursiveDepth": {
          "type": "integer",
          "minimum": 1
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```
