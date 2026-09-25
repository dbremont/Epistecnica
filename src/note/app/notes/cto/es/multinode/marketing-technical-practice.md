# Marketing Technical Practice

> Marketing Technical Practice is the organized technical ensemble — systems, techniques, knowledge, agents, and content operations — through which demand generation is pursued by intervention on audiences, channels, and content systems.

## Formulation

### What technical element type does this technical instance belong to?

**Marketing Technical Practice belongs to the `Technical Element Set` technical element type — containing a `Technical Domain` reading.**

More specifically:

```text
Technical Element Set
└── Marketing Technical Practice (demand-generation ensemble)
    └── Marketing Technical Domain (bounded field: acquisition, conversion, retention)
```

It is an Element Set because it is a coherent, bounded collection of heterogeneous elements — production systems (CRM, CDP, ad delivery, content systems), techniques (segmentation, targeting, experimentation), knowledge (attribution models, deliverability rules), agents (operators, pipelines), and institutions (consent regimes, ad-platform policies) — organized around one realized capability: generating and capturing demand. It contains a Technical Domain reading because that ensemble operates on a bounded field of technical reality defined by problems (acquire, convert, retain under budget and consent constraints), purposes (pipeline and revenue), phenomena (traffic, funnels, deliverability, attribution), and intervention targets (audiences, channels, content systems). Persuasion itself is framed here as intervention on those targets, not as an epistemic practice; the modeling side lives in the companion note.

### What is this technical instance?

> Marketing Technical Practice is a demand-generation technical ensemble instance: operators and pipelines operating CRM, audience, content, delivery, and measurement systems through targeting, experimentation, and optimization techniques, under consent, budget, and deliverability constraints, to move audiences from contact to customer.

### What is the recursive instance decomposition of this technical instance?

> Boundary: this table decomposes one Marketing Technical Practice ensemble instance (domain, requirements, knowledge, agents, systems, techniques, control, lifecycle); deployment-specific values appear only in rows marked exemplar.
>
> Stopping rule: a row is terminal when it names a concrete tool, file, config attribute, measured value, or named actor.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a tool *implements* the practice; a running campaign, pipeline, or deployment *realizes* it.

| Instance Tree Path | Description | Technical Category | Technical Element Type Tree Path |
|---|---|---|---|
| **Marketing Technical Practice** | Demand-generation ensemble: systems, techniques, knowledge, and agents operating on audiences, channels, and content. | Composite | `(root) > Technical Element Set` |
| Marketing Technical Practice > Marketing Technical Domain | Bounded field: acquisition, conversion, and retention pursued under budget, consent, and deliverability bounds. | Technical Context | `(root) > Technical Domain` |
| Marketing Technical Practice > Acquisition Problem | Discrepancy between current and desired qualified-contact volume at acceptable cost (exemplar values per deployment). | Technical Context | `(root) > Technical Problem` |
| Marketing Technical Practice > Conversion Problem | Discrepancy between current and desired contact-to-customer rate under funnel and latency conditions. | Technical Context | `(root) > Technical Problem` |
| Marketing Technical Practice > Demand Purpose | Intended ultimate effect: qualified pipeline and revenue from addressable audiences. | Technical Context | `(root) > Technical Purpose` |
| Marketing Technical Practice > Consent Constraint | Bound on action imposed by consent regimes and platform policies (e.g. GDPR opt-in, ad-platform approval). | Technical Context | `(root) > Technical Constraint` |
| Marketing Technical Practice > Budget Constraint | Bound on action imposed by spend caps and cost-per-acquisition ceilings (exemplar values per deployment). | Technical Context | `(root) > Technical Constraint` |
| Marketing Technical Practice > Audience Resource | Addressable contacts and segments consumed and cultivated by campaigns (exemplar lists per deployment). | Technical Context | `(root) > Technical Resource` |
| Marketing Technical Practice > Content Resource | Creative and copy assets consumed across channels (exemplar items per deployment). | Technical Context | `(root) > Technical Resource` |
| Marketing Technical Practice > Attribution Knowledge | Accumulated models and rules for crediting touchpoints with outcomes (e.g. last-touch, multi-touch, lift). | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Deliverability Knowledge | Know-how governing inbox, push, and ad-policy acceptance (e.g. SPF/DKIM/DMARC alignment, list hygiene). | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Experimentation Strategy | Context-sensitive regime for sequencing tests and allocating traffic (e.g. A/B, holdouts, ramp-ups). | Knowledge & Methodology | `(root) > Technical Strategy` |
| Marketing Technical Practice > Marketing Operator | Human agent executing techniques through tools, budgets, and calendars (exemplar actors per deployment). | Agents & Competence | `(root) > Technical Agent` |
| Marketing Technical Practice > Campaign Pipeline | Automated agent executing scheduled acts: segmentation, send, sync, and measurement (exemplar per deployment). | Agents & Competence | `(root) > Technical Agent` |
| Marketing Technical Practice > CRM System | Production system of record for contacts, consent, and lifecycle stage (e.g. HubSpot, Salesforce — exemplar). | System Structure | `(root) > Production Technical System` |
| Marketing Technical Practice > Audience Platform | System constituting segments from contact attributes and behaviors (e.g. CDP audience builder — exemplar). | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Content System | System producing and assembling content assets for channels (e.g. CMS, template builder — exemplar). | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Delivery Infrastructure | Infrastructure realizing sends and placements across email, push, paid, and social endpoints (exemplar). | System Structure | `(root) > Technical Architecture` |
| Marketing Technical Practice > Tracking Interface | Boundary through which behavior is captured into the ensemble (e.g. tracking pixel, conversions API — exemplar). | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Segmentation Technique | Generalized method for partitioning audiences by attributes and behaviors. | Technique | `(root) > General Technique Type` |
| Marketing Technical Practice > Targeting Act | Situated application of a segment to a channel placement by an operator or pipeline (exemplar). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Experimentation Practice | Repeatable pattern: hypothesis, holdout, measurement, and rollout of campaign variants. | Technique | `(root) > Technical Practice` |
| Marketing Technical Practice > Campaign Activity | Temporally extended sequence: brief, build, launch, monitor, and close a campaign (exemplar). | Technique | `(root) > Technical Activity` |
| Marketing Technical Practice > Funnel Feedback | Information about intervention effects enabling adjustment (e.g. delivery, open, click, conversion rates). | Technical Control | `(root) > Technical Feedback` |
| Marketing Technical Practice > Attribution Evaluation | Systematic determination of which touchpoints drove outcomes under the chosen model. | Technical Control | `(root) > Technical Evaluation` |
| Marketing Technical Practice > Campaign Lifecycle | Temporal trajectory from brief through production, operation, measurement, and retirement (exemplar). | Lifecycle & Continuity | `(root) > Technical Lifecycle` |

## References

- [Philosophia Artium Technicarum et Operis](note.html?n=general/philosophia-artium-technicarum-et-operis.md)
- [Marketing Science (companion note)](note.html?n=general/marketing-science.md)
