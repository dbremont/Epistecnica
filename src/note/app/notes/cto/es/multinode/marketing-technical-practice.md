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

> Boundary: this table decomposes one Marketing Technical Practice ensemble instance (domain, requirements, knowledge, agents, systems, techniques, control, lifecycle); deployment-specific values and named vendors appear only in rows marked exemplar.
>
> Stopping rule: a row is terminal when it names a concrete tool, file, config attribute, measured value, or named actor.
>
> Identity: Instance Tree Path is the stable identifier of each row; every path in this table is unique.
>
> Verbs: a tool *implements* the practice; a running campaign, pipeline, or deployment *realizes* it.

| Instance Tree Path | Description | Technical Category | Technical Element Type Tree Path |
|---|---|---|---|
| **Marketing Technical Practice** | Demand-generation ensemble: systems, techniques, knowledge, and agents operating on audiences, channels, and content. | Composite | `(root) > Technical Element Set` |
| Marketing Technical Practice > Membership criterion | Rule distinguishing members from non-members: all elements required to move a contact from capture to customer. | Composite | `(root) > Technical Element Set` |
| Marketing Technical Practice > Organizing principle | Shared demand-generation capability under a shared consent regime. | Composite | `(root) > Technical Element Set` |
| Marketing Technical Practice > Email Direct Practice | Nested element set: the email-channel ensemble (systems, techniques, and rules) within the practice. | Composite | `(root) > Technical Element Set` |
| Marketing Technical Practice > Marketing Technical Domain | Bounded field: acquisition, conversion, and retention pursued under budget, consent, and deliverability bounds. | Technical Context | `(root) > Technical Domain` |
| Marketing Technical Practice > Acquisition Problem | Discrepancy between current and desired qualified-contact volume at acceptable cost (exemplar values per deployment). | Technical Context | `(root) > Technical Problem` |
| Marketing Technical Practice > Acquisition Problem > CAC ceiling | Maximum acceptable acquisition cost per customer (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Acquisition Problem > Qualified-contact volume target | Formalized contact-volume objective at acceptable cost (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Requirement` |
| Marketing Technical Practice > Conversion Problem | Discrepancy between current and desired contact-to-customer rate under funnel and latency conditions. | Technical Context | `(root) > Technical Problem` |
| Marketing Technical Practice > Conversion Problem > Contact-to-customer rate target | Formalized conversion objective per funnel (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Requirement` |
| Marketing Technical Practice > Conversion Problem > Funnel latency budget | Maximum tolerable lag from first contact to conversion (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Retention Problem | Discrepancy between current and desired repeat-purchase or renewal rate. | Technical Context | `(root) > Technical Problem` |
| Marketing Technical Practice > Retention Problem > Repeat-purchase rate target | Formalized retention objective per cohort (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Requirement` |
| Marketing Technical Practice > Retention Problem > Churn-rate ceiling | Maximum tolerable cohort churn per period (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Demand Purpose | Intended ultimate effect: qualified pipeline and revenue from addressable audiences. | Technical Context | `(root) > Technical Purpose` |
| Marketing Technical Practice > Demand Purpose > Pipeline target | Formalized qualified-pipeline objective per period (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Requirement` |
| Marketing Technical Practice > Demand Purpose > Revenue target | Formalized revenue objective attributed to the practice (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Requirement` |
| Marketing Technical Practice > Consent Constraint | Bound on action imposed by consent regimes and platform policies (e.g. GDPR opt-in, ad-platform approval). | Technical Context | `(root) > Technical Constraint` |
| Marketing Technical Practice > Consent Constraint > GDPR opt-in regime | Consent bound: prior opt-in for electronic outreach in scope. | Technical Context | `(root) > Technical Constraint` |
| Marketing Technical Practice > Consent Constraint > CAN-SPAM requirements | US commercial-email bound: identification, opt-out mechanism, postal address. | Technical Context | `(root) > Technical Constraint` |
| Marketing Technical Practice > Consent Constraint > Ad-platform approval policy | Platform-side bound on creatives and claims (exemplar: Meta, Google Ads). | Technical Context | `(root) > Technical Constraint` |
| Marketing Technical Practice > Budget Constraint | Bound on action imposed by spend caps and cost-per-acquisition ceilings (exemplar values per deployment). | Technical Context | `(root) > Technical Constraint` |
| Marketing Technical Practice > Budget Constraint > Spend cap | Authorized spend ceiling per campaign or period (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Budget Constraint > LTV:CAC floor | Minimum acceptable lifetime-value to acquisition-cost ratio (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Audience Resource | Addressable contacts and segments consumed and cultivated by campaigns (exemplar lists per deployment). | Technical Context | `(root) > Technical Resource` |
| Marketing Technical Practice > Audience Resource > `suppression-list.csv` | Exclusion file: unsubscribed, bounced, and do-not-contact entries (exemplar). | System Structure | `(root) > Technical Configuration` |
| Marketing Technical Practice > Audience Resource > Segment lists | Named contact cohorts consumed by campaigns (exemplar lists per deployment). | Technical Context | `(root) > Technical Resource` |
| Marketing Technical Practice > Content Resource | Creative and copy assets consumed across channels (exemplar items per deployment). | Technical Context | `(root) > Technical Resource` |
| Marketing Technical Practice > Content Resource > Asset library items | Approved creatives and copy blocks available for assembly (exemplar items per deployment). | Technical Context | `(root) > Technical Resource` |
| Marketing Technical Practice > Content Resource > UTM schema | Naming convention for source, medium, and campaign tracking parameters. | Requirements & Definition | `(root) > Technical Specification` |
| Marketing Technical Practice > Attribution Knowledge | Accumulated models and rules for crediting touchpoints with outcomes (e.g. last-touch, multi-touch, lift). | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Attribution Knowledge > Last-touch model | Single-credit rule assigning conversion to the final touchpoint. | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Attribution Knowledge > Multi-touch model | Weighted-credit rule distributing conversion across touchpoints. | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Attribution Knowledge > Incrementality readout | Lift measured against a holdout group (exemplar readout per deployment). | Technical Control | `(root) > Technical Evaluation` |
| Marketing Technical Practice > Deliverability Knowledge | Know-how governing inbox, push, and ad-policy acceptance (e.g. SPF/DKIM/DMARC alignment, list hygiene). | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Deliverability Knowledge > SPF/DKIM/DMARC alignment | Authentication rules establishing sender legitimacy. | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Deliverability Knowledge > List hygiene practice | Repeatable pattern: pruning invalid and disengaged contacts. | Technique | `(root) > Technical Practice` |
| Marketing Technical Practice > Deliverability Knowledge > Bounce handling rules | Hard/soft bounce classification with retry-or-suppress logic. | Knowledge & Methodology | `(root) > Technical Principle` |
| Marketing Technical Practice > Experimentation Strategy | Context-sensitive regime for sequencing tests and allocating traffic (e.g. A/B, holdouts, ramp-ups). | Knowledge & Methodology | `(root) > Technical Strategy` |
| Marketing Technical Practice > Experimentation Strategy > A/B design | Two-variant comparison under randomized assignment. | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Experimentation Strategy > Holdout design | Withheld-control comparison measuring incrementality. | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Experimentation Strategy > Geo-split design | Region-level comparison where contact randomization is infeasible. | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Experimentation Strategy > Ramp-up rule | Traffic-allocation schedule limiting blast radius (exemplar schedule per deployment). | Knowledge & Methodology | `(root) > Technical Principle` |
| Marketing Technical Practice > M3AAWG | Messaging anti-abuse institution governing sending best practice. | Knowledge & Methodology | `(root) > Technical Institution` |
| Marketing Technical Practice > IAB | Advertising-standards institution governing formats, transparency, and consent frameworks. | Knowledge & Methodology | `(root) > Technical Institution` |
| Marketing Technical Practice > Supervisory authority | Data-protection enforcement institution (exemplar authority per deployment). | Knowledge & Methodology | `(root) > Technical Institution` |
| Marketing Technical Practice > Ad-platform policy governance | Platform-side rule-making governing creatives, claims, and audiences (exemplar: Meta, Google Ads). | Knowledge & Methodology | `(root) > Technical Institution` |
| Marketing Technical Practice > IAB TCF consent string | Standard encoding of consent state passed to vendors. | Requirements & Definition | `(root) > Technical Standard` |
| Marketing Technical Practice > ads.txt / sellers.json | Standards declaring authorized sellers of ad inventory. | Requirements & Definition | `(root) > Technical Standard` |
| Marketing Technical Practice > RFC 7489 DMARC | Standard aligning authentication results with sender policy. | Requirements & Definition | `(root) > Technical Standard` |
| Marketing Technical Practice > Permission-first principle | General rule: no outreach without a consent basis. | Knowledge & Methodology | `(root) > Technical Principle` |
| Marketing Technical Practice > Deliverability-before-volume principle | General rule: reputation constrains scale. | Knowledge & Methodology | `(root) > Technical Principle` |
| Marketing Technical Practice > Test-before-scale principle | General rule: no full rollout without a readout. | Knowledge & Methodology | `(root) > Technical Principle` |
| Marketing Technical Practice > Suppression-before-send principle | General rule: exclusion check precedes every dispatch. | Knowledge & Methodology | `(root) > Technical Principle` |
| Marketing Technical Practice > Data-minimization principle | General rule: collect only attributes segments consume. | Knowledge & Methodology | `(root) > Technical Principle` |
| Marketing Technical Practice > Funnel framework | Overarching logic staging the journey (awareness, interest, desire, action). | Knowledge & Methodology | `(root) > Technical Framework` |
| Marketing Technical Practice > RACE framework | Overarching logic planning reach, act, convert, and engage phases. | Knowledge & Methodology | `(root) > Technical Framework` |
| Marketing Technical Practice > Deliverability labor | Purposive human effort tending warmup, lists, and reputation (exemplar per deployment). | Agents & Competence | `(root) > Technical Labor` |
| Marketing Technical Practice > Sender reputation | Characteristic attributable to a sending identity (exemplar score per deployment). | Mechanism & Capability | `(root) > Technical Property` |
| Marketing Technical Practice > List quality | Degree to which a list holds valid, engaged contacts (exemplar per deployment). | Mechanism & Capability | `(root) > Technical Quality` |
| Marketing Technical Practice > Marketing Operator | Human agent executing techniques through tools, budgets, and calendars (exemplar actors per deployment). | Agents & Competence | `(root) > Technical Agent` |
| Marketing Technical Practice > Marketing Operator > Deliverability competence | Acquired capacity to sustain placement and sender reputation (exemplar holder per deployment). | Agents & Competence | `(root) > Technical Competence` |
| Marketing Technical Practice > Marketing Operator > Platform certification | Vendor credential for a delivery or ad platform (exemplar per deployment). | Agents & Competence | `(root) > Technical Competence` |
| Marketing Technical Practice > Marketing Operator > Campaign calendar | Time-bound plan assigning campaigns to slots (exemplar per deployment). | Requirements & Definition | `(root) > Technical Specification` |
| Marketing Technical Practice > Campaign Pipeline | Automated agent executing scheduled acts: segmentation, send, sync, and measurement (exemplar per deployment). | Agents & Competence | `(root) > Technical Agent` |
| Marketing Technical Practice > Campaign Pipeline > Segmentation job | Scheduled computation rebuilding segment membership. | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Pipeline > Send job | Scheduled act dispatching messages to a segment (exemplar run per deployment). | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Pipeline > Audience-sync job | Scheduled propagation of segments to ad platforms (exemplar run per deployment). | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Pipeline > Measurement job | Scheduled collection of delivery and conversion events. | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Pipeline > Schedule | Cron expression fixing job cadence (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > CRM System | Production system of record for contacts, consent, and lifecycle stage. | System Structure | `(root) > Production Technical System` |
| Marketing Technical Practice > CRM System > Contact record | Constitutive object holding one addressable contact. | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > CRM System > Contact record > Contact attribute schema | Field contract: identifiers, consent flags, lifecycle stage. | Requirements & Definition | `(root) > Technical Specification` |
| Marketing Technical Practice > CRM System > Contact record > Dedupe mechanism | Merge logic resolving duplicate identities. | Mechanism & Capability | `(root) > Technical Mechanism` |
| Marketing Technical Practice > CRM System > Consent record | Constitutive object holding opt-in evidence per contact (exemplar entries per deployment). | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > CRM System > Consent record > Opt-in timestamp | Proof-of-consent attribute (exemplar values per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > CRM System > Lifecycle stage | Stage marker moving contacts from lead to customer (exemplar stages per deployment). | System Structure | `(root) > Technical Configuration` |
| Marketing Technical Practice > CRM System > Lifecycle stage > Stage-transition automation | Rule-driven moves on behavior or operator acts. | Mechanism & Capability | `(root) > Technical Mechanism` |
| Marketing Technical Practice > CRM System > Forms API | Capture boundary for web-originated contacts. | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > CRM System > Import API | Bulk-ingestion boundary for lists (exemplar files per deployment). | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > CRM System > HubSpot CRM | Exemplar production CRM implementing the system. | System Structure | `(root) > Production Technical Object` |
| Marketing Technical Practice > CRM System > Salesforce | Exemplar production CRM implementing the system. | System Structure | `(root) > Production Technical Object` |
| Marketing Technical Practice > Audience Platform | System constituting segments from contact attributes and behaviors. | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Audience Platform > Segment definition | Named cohort rule over attributes and behaviors (exemplar per deployment). | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Audience Platform > Segment definition > Membership rule | Boolean and temporal predicate deciding inclusion (exemplar per deployment). | Requirements & Definition | `(root) > Technical Specification` |
| Marketing Technical Practice > Audience Platform > Segment definition > Refresh cadence | Recompute interval keeping membership current (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Audience Platform > Attribute schema | Contract of profile fields available to segments. | Requirements & Definition | `(root) > Technical Specification` |
| Marketing Technical Practice > Audience Platform > Behavior-event catalog | Named events (page view, purchase, lapse) feeding segments. | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Audience Platform > Segment (Twilio Segment) | Exemplar customer-data platform implementing the platform. | System Structure | `(root) > Production Technical Object` |
| Marketing Technical Practice > Content System | System producing and assembling content assets for channels. | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Content System > Template library | Reusable layouts for messages and pages (exemplar items per deployment). | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Content System > Personalization tokens | Placeholders resolved per contact at send time. | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Content System > Approval flow | Ordered review acts before release (exemplar per deployment). | Technique | `(root) > Technical Activity` |
| Marketing Technical Practice > Content System > CMS template builder | Exemplar tool implementing assembly (exemplar per deployment). | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Delivery Infrastructure | Infrastructure realizing sends and placements across email, push, paid, and social endpoints (exemplar). | System Structure | `(root) > Technical Architecture` |
| Marketing Technical Practice > Delivery Infrastructure > Email endpoint | Channel endpoint for mailbox delivery. | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Delivery Infrastructure > Email endpoint > ESP | Exemplar sending provider (e.g. SendGrid). | System Structure | `(root) > Production Technical Object` |
| Marketing Technical Practice > Delivery Infrastructure > Email endpoint > Sending domain | Authenticated domain that reputation attaches to (exemplar per deployment). | System Structure | `(root) > Technical Configuration` |
| Marketing Technical Practice > Delivery Infrastructure > Email endpoint > IP warmup schedule | Ramp plan for new sending IPs (exemplar per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Delivery Infrastructure > Push endpoint | Channel endpoint for device notifications. | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Delivery Infrastructure > Paid endpoint | Channel endpoint for auctioned placements. | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Delivery Infrastructure > Paid endpoint > Ad-platform connector | Sync boundary pushing audiences and pulling delivery (exemplar: Meta, Google Ads). | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Delivery Infrastructure > Paid endpoint > Audience sync | Propagation of segments into platform custom audiences (exemplar run per deployment). | System Relations | `(root) > Technical Interaction` |
| Marketing Technical Practice > Delivery Infrastructure > Social endpoint | Channel endpoint for organic social placement (exemplar per deployment). | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Tracking Interface | Boundary through which behavior is captured into the ensemble. | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Tracking Interface > Tracking pixel | Client-side capture tag on pages and mail (exemplar deployment). | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Tracking Interface > Conversions API | Server-side event boundary bypassing client loss (exemplar deployment). | System Structure | `(root) > Technical Interface` |
| Marketing Technical Practice > Tracking Interface > UTM parameters | Source, medium, and campaign attributes on links (exemplar values per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Tracking Interface > Event catalog | Contract of tracked conversion events. | Requirements & Definition | `(root) > Technical Specification` |
| Marketing Technical Practice > CRM-to-ESP send dependency | Relation in which delivery requires contact and suppression state from the CRM. | System Relations | `(root) > Technical Dependency` |
| Marketing Technical Practice > Pipeline-to-CRM dependency | Relation in which scheduled jobs require CRM reads and writes. | System Relations | `(root) > Technical Dependency` |
| Marketing Technical Practice > Delivery-to-suppression check | Relation in which every dispatch requires a suppression-list lookup. | System Relations | `(root) > Technical Dependency` |
| Marketing Technical Practice > Paid-to-policy interaction | Relation through which placements are approved or rejected under platform policy. | System Relations | `(root) > Technical Interaction` |
| Marketing Technical Practice > Tracking-to-attribution interaction | Relation through which captured events feed attribution credit. | System Relations | `(root) > Technical Interaction` |
| Marketing Technical Practice > Audience Targeting Practice | Repeatable pattern integrating segmentation, targeting, and measurement across channels. | Technique | `(root) > Technical Practice` |
| Marketing Technical Practice > Audience Targeting Practice > Define activity | Authoring the segment predicate (exemplar per deployment). | Technique | `(root) > Technical Activity` |
| Marketing Technical Practice > Audience Targeting Practice > Validate activity | Checking coverage and overlap before publish. | Technique | `(root) > Technical Activity` |
| Marketing Technical Practice > Audience Targeting Practice > Publish activity | Releasing the segment to targeting and sync. | Technique | `(root) > Technical Activity` |
| Marketing Technical Practice > Audience Targeting Practice > Segmentation Technique | Generalized method for partitioning audiences by attributes and behaviors. | Technique | `(root) > General Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Segmentation Technique > Criterion types | Demographic, behavioral, and firmographic selectors. | Knowledge & Methodology | `(root) > Technical Knowledge` |
| Marketing Technical Practice > Audience Targeting Practice > Segmentation Technique > Cohort segmentation operation | Situated application of segmentation to a particular cohort and campaign (exemplar per deployment). | Technique | `(root) > Operative Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Segmentation Technique > Cohort segmentation operation > Apply criterion act | Setting one selector value on the cohort (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Segmentation Technique > Cohort segmentation operation > Set threshold act | Fixing the inclusion cutoff for the cohort (exemplar value per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Segmentation Technique > Scoring model | Technique embodied in the platform establishing how contacts are ranked (e.g. lead score, send-time optimization). | Technique | `(root) > Constitutive Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Targeting Operation | Situated application of targeting to a channel placement by an operator or pipeline (exemplar per deployment). | Technique | `(root) > Operative Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Targeting Operation > Select segment act | Binding a published segment to a placement (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Targeting Operation > Bind placement act | Reserving the channel slot for the segment (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Targeting Operation > Set budget cap act | Fixing the spend ceiling for the binding (exemplar value per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Targeting Operation > Launch act | Releasing the binding into operation (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Targeting console & API | Boundary and means through which the operator or pipeline encodes targeting intent (e.g. ESP dashboard + API, ad-manager + bulk sheet — exemplar). | Technique | `(root) > Technical Interface & Actuation` |
| Marketing Technical Practice > Audience Targeting Practice > Nurture Technique | Generalized method for sequencing messages that move contacts down-funnel. | Technique | `(root) > General Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Nurture Technique > Drip operation | Situated sequence of timed messages for one cohort (exemplar per deployment). | Technique | `(root) > Operative Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Nurture Technique > Drip operation > Wait-step act | Holding a contact until the next timed message (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Nurture Technique > Drip operation > Branch-on-behavior act | Routing a contact on an opened, clicked, or lapsed event (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Retargeting Technique | Generalized method for re-engaging prior visitors or cart abandoners. | Technique | `(root) > General Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Retargeting Technique > Pool-build operation | Situated assembly of the retargeting pool for one placement (exemplar per deployment). | Technique | `(root) > Operative Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Retargeting Technique > Pool-build operation > Burn-list act | Removing converters from the pool (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Lookalike Technique | Generalized method for expanding reach from a seed audience (exemplar platform builder per deployment). | Technique | `(root) > General Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Lookalike Technique > Seed-size parameter | Seed audience volume the model expands from (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Audience Targeting Practice > Lookalike Technique > Similarity threshold | Minimum resemblance for inclusion in the expansion (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Audience Targeting Practice > Personalization Technique | Generalized method for resolving content per contact at send time. | Technique | `(root) > General Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Personalization Technique > Render-per-contact act | Assembling tokens and blocks for one recipient (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Bid Management Technique | Generalized method for pricing paid placements under caps. | Technique | `(root) > General Technique Type` |
| Marketing Technical Practice > Audience Targeting Practice > Bid Management Technique > Bid-adjust act | Raising or lowering a bid on performance signals (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Audience Targeting Practice > Bid Management Technique > Frequency cap | Maximum impressions per contact per period (exemplar value per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Experimentation Practice | Repeatable pattern: hypothesis, holdout, measurement, and rollout of campaign variants. | Technique | `(root) > Technical Practice` |
| Marketing Technical Practice > Experimentation Practice > Hypothesis | Falsifiable claim about variant effect (exemplar per deployment). | Requirements & Definition | `(root) > Technical Specification` |
| Marketing Technical Practice > Experimentation Practice > Variant | Divergent content or bid under test (exemplar per deployment). | System Structure | `(root) > Constitutive Technical Object` |
| Marketing Technical Practice > Experimentation Practice > Randomization unit | Contact- or geo-level assignment grain (exemplar per deployment). | Requirements & Definition | `(root) > Technical Parameter` |
| Marketing Technical Practice > Experimentation Practice > Guardrail metrics | Non-regression indicators watched during tests (exemplar set per deployment). | Technical Control | `(root) > Technical Feedback` |
| Marketing Technical Practice > Experimentation Practice > Experiment readout | Measured lift with uncertainty (exemplar per deployment). | Technical Control | `(root) > Technical Evaluation` |
| Marketing Technical Practice > Experimentation Practice > Pre-registration standard | Norm fixing hypothesis and metrics before launch. | Requirements & Definition | `(root) > Technical Standard` |
| Marketing Technical Practice > Experimentation Practice > Significance standard | Norm fixing the confidence level for readout claims (e.g. 95% — exemplar). | Requirements & Definition | `(root) > Technical Standard` |
| Marketing Technical Practice > Experimentation Practice > Holdout maintenance | Activity preserving holdout purity against leakage. | Lifecycle & Continuity | `(root) > Technical Maintenance` |
| Marketing Technical Practice > Experimentation Practice > Landing Test Technique | Generalized method for testing page variants behind a campaign. | Technique | `(root) > General Technique Type` |
| Marketing Technical Practice > Experimentation Practice > Landing Test Technique > Page-variant act | Publishing one page variant under test (exemplar per deployment). | Technique | `(root) > Technical Act` |
| Marketing Technical Practice > Campaign Activity | Temporally extended sequence: brief, build, launch, monitor, and close a campaign (exemplar). | Technique | `(root) > Technical Activity` |
| Marketing Technical Practice > Campaign Activity > Brief task | Scoping audience, message, and success criteria (exemplar per deployment). | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Activity > Brief task > Campaign brief | Decision artifact authorizing production (exemplar per deployment). | Requirements & Definition | `(root) > Technical Specification` |
| Marketing Technical Practice > Campaign Activity > Build task | Assembling segments, content, and bindings (exemplar per deployment). | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Activity > QA task | Verifying links, tokens, lists, and caps before launch. | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Activity > QA task > QA checklist | Conformance artifact gating launch (exemplar per deployment). | Technical Control | `(root) > Verification` |
| Marketing Technical Practice > Campaign Activity > Launch task | Releasing the campaign into operation (exemplar per deployment). | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Activity > Monitor task | Watching funnel feedback against guardrails. | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Campaign Activity > Close task | Archiving assets and recording learnings (exemplar per deployment). | Technique | `(root) > Technical Task` |
| Marketing Technical Practice > Funnel Feedback | Information about intervention effects enabling adjustment (e.g. delivery, open, click, conversion rates). | Technical Control | `(root) > Technical Feedback` |
| Marketing Technical Practice > Funnel Feedback > Delivery rate | Share of dispatched messages accepted by the channel (exemplar per deployment). | Technical Control | `(root) > Technical Feedback` |
| Marketing Technical Practice > Funnel Feedback > Open rate | Share of delivered messages opened (exemplar per deployment). | Technical Control | `(root) > Technical Feedback` |
| Marketing Technical Practice > Funnel Feedback > Click rate | Share of opened messages clicked through (exemplar per deployment). | Technical Control | `(root) > Technical Feedback` |
| Marketing Technical Practice > Funnel Feedback > Conversion rate | Share of clicks completing the target act (exemplar per deployment). | Technical Control | `(root) > Technical Feedback` |
| Marketing Technical Practice > Funnel Feedback > CAC | Realized acquisition cost per customer (exemplar per deployment). | Mechanism & Capability | `(root) > Technical Performance` |
| Marketing Technical Practice > Funnel Feedback > ROAS | Realized return on ad spend (exemplar per deployment). | Mechanism & Capability | `(root) > Technical Performance` |
| Marketing Technical Practice > Attribution Evaluation | Systematic determination of which touchpoints drove outcomes under the chosen model. | Technical Control | `(root) > Technical Evaluation` |
| Marketing Technical Practice > Attribution Evaluation > Attribution readout | Touchpoint credit under the chosen model (exemplar per deployment). | Technical Control | `(root) > Technical Evaluation` |
| Marketing Technical Practice > Attribution Evaluation > Validation against holdout | Check of attributed credit versus experimental lift. | Technical Control | `(root) > Validation` |
| Marketing Technical Practice > Blocklisting | State in which a sending domain or IP is listed and placement collapses (exemplar per deployment). | Technical Control | `(root) > Technical Failure` |
| Marketing Technical Practice > Deliverability collapse | State in which inbox placement falls below usable levels (exemplar per deployment). | Technical Control | `(root) > Technical Failure` |
| Marketing Technical Practice > Audience-sync breakage | State in which segment propagation to ad platforms stalls (exemplar per deployment). | Technical Control | `(root) > Technical Failure` |
| Marketing Technical Practice > Suppression failure risk | Possibility and consequence of dispatching to excluded contacts. | Technical Control | `(root) > Technical Risk` |
| Marketing Technical Practice > Volume-vs-deliverability trade-off | Relationship in which higher send volume constrains placement quality. | Technical Control | `(root) > Technical Trade-off` |
| Marketing Technical Practice > PII retention policy | Rules bounding how long contact data is kept (exemplar per deployment). | Technical Control | `(root) > Technical Security` |
| Marketing Technical Practice > CRM access control | Role-based bounds on who reads and writes contact data (exemplar per deployment). | Technical Control | `(root) > Technical Security` |
| Marketing Technical Practice > Campaign Lifecycle | Temporal trajectory from brief through production, operation, measurement, and retirement (exemplar). | Lifecycle & Continuity | `(root) > Technical Lifecycle` |
| Marketing Technical Practice > Campaign Lifecycle > Brief approval gate | Decision point authorizing production (exemplar per deployment). | Lifecycle & Continuity | `(root) > Technical Lifecycle` |
| Marketing Technical Practice > Campaign Lifecycle > QA gate | Decision point authorizing launch (exemplar per deployment). | Lifecycle & Continuity | `(root) > Technical Lifecycle` |
| Marketing Technical Practice > Campaign Lifecycle > Sunset | Retirement of assets and placements (exemplar per deployment). | Lifecycle & Continuity | `(root) > Technical Lifecycle` |
| Marketing Technical Practice > Evolution blast-to-automation-to-orchestration | Historical trajectory: batch blasts → triggered automation → AI-orchestrated journeys. | Lifecycle & Continuity | `(root) > Technical Evolution` |
| Marketing Technical Practice > Third-party cookie deprecation | Condition in which browser tracking identifiers lose viability, forcing server-side capture. | Lifecycle & Continuity | `(root) > Technical Obsolescence` |
| Marketing Technical Practice > Sender-reputation maintenance | Activity preserving sending-identity standing (warmup tending, complaint watching). | Lifecycle & Continuity | `(root) > Technical Maintenance` |
| Marketing Technical Practice > List re-engagement | Activity restoring lapsed contacts or pruning them (exemplar per deployment). | Lifecycle & Continuity | `(root) > Technical Maintenance` |

## References

- [Philosophia Artium Technicarum et Operis](note.html?n=general/philosophia-artium-technicarum-et-operis.md)
- [Marketing Science (companion note)](note.html?n=general/marketing-science.md)
- [M3AAWG Messaging Best Practices](https://www.m3aawg.org/)
- [IAB Transparency & Consent Framework](https://iabtechlab.com/)
- [RFC 7489 DMARC](https://www.rfc-editor.org/rfc/rfc7489.html)
