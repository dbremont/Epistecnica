---
tags: [note, guia]
---

# A Guide on AI-Assisted Programming

**Contains:** [An Essay On Personal Programming Workflow](/view.html?p=notes/personal/an-essay-on-personal-programming-workflow.md)

> In this note, we will explore the impact of new AI Technical Tools in the Work.
> 

> **Note:** The fill-ins were AI-generated, so they require verification. The previous entry
> 
> 
> **“Project Execution – Autonomous Task Closure”** was incorrect: **Autonomous Task Closure is *not* a task; it is an AI Capability / Automation Level.**
> 

> This is a Generic Note.
> 

> See more in (https://www.bremontix.xyz/lab/pro/Production/Industry/Software/Production/Autoprogram/) - for Programming.
> 

## Index

## Formulation

> **What is task?** Bounded transformation process with goals, inputs, outputs, operations, and constraints.
> 

> **What is a task space?** Multidimensional space of all tasks characterized by cognitive, operational, informational, and uncertainty dimensions.
> 

> **What is the digital task space?** Subspace of tasks executed through digital systems and informational transformations.
> 

> **What is AI-Assisted work?** Human–AI cooperative execution of tasks where AI helps with planning, execution, verification, or optimization.
> 

> **Which is the given level of automation coverage on the Task?** Proportion of a task that can be automated (weighted or unweighted).
> 

> What are the task space automation coverage dynamics? **Automation coverage dynamics** describe **how the level, pattern, and distribution of automation changes over time across the entire task space**, driven simultaneously by technological capability, task structure, and human–system interaction.
> 

## Capability Set

> Which are the **AI** **Capability Space**?
> 

### Dimension

| **Dimension** | **Description** |
| --- | --- |
| **Perception** | Ability to interpret raw inputs (text, images, code, logs, signals) and extract structure, meaning, or entities. |
| **Representation** | Ability to build internal structured forms (embeddings, graphs, schemas) that support reasoning, recall, and transformation. |
| **Modeling & Prediction** | Ability to model patterns, dynamics, and statistical relationships to forecast future states or generate probability distributions. |
| **Reasoning** | Ability to evaluate alternatives, apply logic or constraints, compare options, infer consequences, and make discriminative judgments. |
| **Generation** | Ability to synthesize new content (text, code, images, data) consistent with constraints, style, or target semantics. |
| **Planning** | Ability to construct stepwise procedures, decompose goals, assemble workflows, or design multistage strategies. |
| **Tool Use & Action** | Ability to interact with external systems (APIs, files, terminals, software, UIs) to execute operations on the environment. |
| **Interaction** | Ability to communicate, maintain context, clarify goals, ask questions, and adapt communication to user intent. |
| **Learning** | Ability to adapt to new inputs, preferences, patterns, or examples within a session or environment. |
| **Meta-Reasoning** | Ability to evaluate, critique, refine, verify, or correct its own reasoning and outputs. |
| **Autonomy** *(optional)* | Ability to self-initiate, self-manage, and self-terminate tasks by integrating all other dimensions into independent operation. |

### Capability Space

| **Category** | **Capability** | **Description** | **Instance(s)** |
| --- | --- | --- | --- |
| **Perception** | Text Perception | Extract structure, meaning, or entities from text. | Entity extraction, topic detection, sentiment parsing |
| **Capability** | Visual Perception | Understand images, diagrams, or UI structures. | Object detection, layout parsing, OCR |
| **Capability** | Code Perception | Interpret and analyze code semantics and structure. | AST inference, bug-spotting, pattern detection |
| **Capability** | Signal/Log Perception | Interpret logs, telemetry, or time-series signals. | Log anomaly detection, pattern extraction |
| **Representation** | Embedding Construction | Represent text/images/code in vector space. | Text embeddings, multimodal embeddings |
| **Representation** | Knowledge Structuring | Build internal graphs, schemas, or abstractions. | Knowledge graphs, structural inference |
| **Predictive Modeling** | Sequence Prediction | Predict next tokens, states, or events. | Text continuation, next-step prediction |
| **Predictive Modeling** | Statistical Forecasting | Project future values or trends. | Time-series forecasts, demand prediction |
| **Discriminative Reasoning** | Classification | Assign items to categories. | Spam detection, label assignment |
| **Discriminative Reasoning** | Ranking & Scoring | Prioritize or order options. | Search ranking, relevance scoring |
| **Discriminative Reasoning** | Decision Evaluation | Choose between alternatives under constraints. | “Select best configuration”, risk scoring |
| **Generative Synthesis** | Text Generation | Produce coherent text under constraints. | Summaries, rewrites, drafting |
| **Generative Synthesis** | Code Generation | Create working code from patterns or specs. | Function generation, refactoring |
| **Generative Synthesis** | Image/Media Generation | Produce images or visual assets. | Mockups, diagrams, UI sketches |
| **Transformation** | Data Transformation | Convert, clean, and normalize data. | CSV→JSON, schema mapping |
| **Transformation** | Text/Content Transformation | Restructure content without adding new meaning. | Compression, expansion, translation |
| **Transformation** | Code Transformation | Modify or optimize code. | Refactor, porting, linting |
| **Tool Use & Action** | API Interaction | Call external APIs/services to perform work. | Search APIs, cloud APIs |
| **Tool Use & Action** | System Operations | Modify files, execute commands, operate software. | Terminal actions, file editing |
| **Tool Use & Action** | UI Manipulation | Navigate interfaces and perform actions. | Browser automation, RPA-style workflows |
| **Procedural Planning** | Stepwise Planning | Create multi-step procedures to achieve goals. | “Plan server setup workflow” |
| **Procedural Planning** | Workflow Assembly | Combine subtasks into coherent flows. | Data pipeline planning, research workflows |
| **Strategic Planning** | Goal Decomposition | Break high-level goals into sub-goals. | Project planning, roadmap design |
| **Strategic Planning** | Scenario Simulation | Explore possible futures and strategies. | Policy scenarios, decision trees |
| **Meta-Reasoning** | Self-Critique | Evaluate and correct own outputs. | Error detection, refinement |
| **Meta-Reasoning** | Consistency Checking | Verify logic, constraints, and coherence. | Cross-checking answers |
| **Interaction** | Contextual Dialogue | Maintain multi-step context and adapt responses. | Multi-turn workflows, tutoring |
| **Interaction** | Clarification & Querying | Ask questions to resolve uncertainties. | “What format should the file use?” |
| **Learning & Adaptation** | Few-Shot Adaptation | Learn from small examples in-session. | Pattern generalization from prototypes |
| **Learning & Adaptation** | Preference Learning | Adjust to user-specific styles, constraints. | Personalized output |
| **Autonomy** | Autonomous Task Execution | Execute tasks with minimal supervision. | Automated agents, continuous monitors |
| **Autonomy** | Autonomous Task Closure | Define, plan, execute, validate, and finish tasks. | Fully autonomous workflows |

## Automation Level

| **Level** | **Name** | **Definition** |
| --- | --- | --- |
| **1** | **Assistive Automation** | AI supports isolated subtasks by offering suggestions, generating drafts, checking errors, or accelerating micro-operations. The human performs the core task logic and retains full control. |
| **2** | **Partial Automation** | AI reliably performs well-defined, repeatable segments of the task. The execution is bounded, rule-driven, or pattern-driven. The human manages integration, exceptions, and decisions. |
| **3** | **Flow Automation** | AI executes multistep task sequences according to a predefined or inferred workflow. The system coordinates several segments and handles transitions. Human oversight ensures correctness and handles edge cases. |
| **4** | **End-to-End Automation** | AI completes the entire task from input to output within a defined scope. Human involvement is limited to reviewing the final result, providing approval, or correcting rare failures. |
| **5** | **Autonomous Task Closure** | AI autonomously defines, plans, executes, validates, and closes the task. The system sets its own subtasks and success criteria, monitors execution conditions, adapts dynamically, and signals when the task is complete. Human roles shift to rare escalation or environmental supervision. |

## **Digital Task Space**

> Let’s see the tasks that humans perform in the Digital Space - and the **AI Impact**.
> 

| **Category** | **Task** | **AI Impact** | **Impact Level** |
| --- | --- | --- | --- |
| **Information Retrieval** | Search for information across the web, files, or databases | AI can filter, refine, summarize, pre-rank, and proactively surface results | **2–3** |
| **Information Retrieval** | Query formulation & optimization | AI rewrites queries, identifies missing constraints, generates optimal search expressions | **1–2** |
| **Information Retrieval** | Document triage (skim, sort, cluster) | AI can classify, cluster, and recommend relevant materials | **3–4** |
| **Content Production** | Drafting text (emails, reports, descriptions) | AI generates coherent drafts and style-specific content | **3–4** |
| **Content Production** | Editing, rewriting, summarization | AI can fully transform content based on intent | **4** |
| **Content Production** | Multimedia generation (images, diagrams) | AI creates visual assets from text | **3–4** |
| **Data Processing** | Data cleaning, deduplication, normalization | AI automates structured transformation rules | **3–4** |
| **Data Processing** | Data extraction from text/images | AI performs extraction and structuring | **3** |
| **Data Processing** | Format conversion and schema mapping | AI infers structure and converts autonomously | **3–4** |
| **Software Development** | Code generation (functions, modules) | AI writes significant portions of code | **3–4** |
| **Software Development** | Code refactoring & optimization | AI suggests improvements, applies patterns | **2–3** |
| **Software Development** | Bug detection & debugging guidance | AI identifies issues and suggests fixes | **2–3** |
| **System Operations** | File operations (create, edit, move) | AI performs direct actions via tools | **3–4** |
| **System Operations** | Executing terminal commands | AI generates commands & explains them | **1–2** |
| **System Operations** | Monitoring logs & detecting anomalies | AI autonomously flags issues | **3–4** |
| **Decision Support** | Option evaluation (tools, strategies) | AI evaluates tradeoffs and ranks alternatives | **2–3** |
| **Decision Support** | Risk assessment | AI models outcomes & uncertainties | **2–3** |
| **Decision Support** | Scenario simulation | AI produces multi-path projections | **3** |
| **Knowledge Workflows** | Research planning | AI constructs multi-step workflows | **2–3** |
| **Knowledge Workflows** | Multi-document synthesis | AI produces integrated summaries | **3–4** |
| **Knowledge Workflows** | Framework/ontology creation | AI generates conceptual structures | **2–3** |
| **Communication** | Drafting emails/messages | AI generates content | **3–4** |
| **Communication** | Translating content | AI translates reliably | **4** |
| **Communication** | Meeting notes / call summaries | AI extracts key points | **3–4** |
| **Project Execution** | Task decomposition & sequencing | AI outlines actionable steps | **2–3** |
| **Project Execution** | Workflow automation | AI chains tasks with tools | **3–4** |
| **Project Execution** | Status tracking & reporting | AI monitors progress, generates reports, may close subtasks | **4** |
| **Analysis** | Data interpretation | AI identifies patterns & insights | **2–3** |
| **Analysis** | Analytical writing | AI generates structured analyses | **3–4** |
| **Analysis** | Model evaluation or parameter tuning | AI interprets outputs & suggests changes | **2–3** |
| **User Interaction** | Conversational assistance | AI manages multi-turn context | **3–4** |
| **User Interaction** | Clarifying requirements | AI closes ambiguity gaps | **2–3** |
| **User Interaction** | Adaptive tutoring | AI tailors explanations interactively | **3–4** |
| **Autonomous Operations** | Continuous monitoring & action loops | AI handles ongoing processes | **4–5** |
| **Autonomous Operations** | Self-directed maintenance | AI detects issues & performs corrective actions | **4–5** |
| **Autonomous Operations** | Task execution & validation | AI defines, executes, and closes tasks | **4** |
| **OS UI Navigation** | Window & app management (open, switch, close, arrange) | AI can operate windows, reposition apps, and optimize layouts contextually | **2–3** |
| **OS UI Navigation** | Menu & settings navigation | AI finds the correct UI entry point and executes configuration steps | **2–3** |
| **OS UI Navigation** | File explorer navigation | AI opens locations, filters items, organizes views | **2–3** |
| **OS UI Navigation** | Cross-app orchestration | AI moves data between applications, copies results, performs multi-step UI flows | **3–4** |

## References

- https://github.com/dbremont/documentorum/blob/main/tool/firefox.md
- https://www.bremontix.xyz/lab/pro/Production/Industry/Software/Production/Productivity/
- https://github.com/browser-use/web-ui
- https://github.com/awesome-assistants/awesome-assistants
- https://www.aiawesome.com/
- https://github.com/ai-for-developers/awesome-ai-coding-tools
- https://awesomeaitools.com/
- https://github.com/mahseema/awesome-ai-tools
- https://altern.ai/
- https://n8n.io/
- https://github.com/dbremont/documentorum/blob/main/tool
- [Code Search](https://app.notion.com/p/Code-Search-ad65b85fa3714679a57e07c027b91b88?pvs=21)
- https://www.bremontix.xyz/lab/pro/Production/Industry/Software/Production/Autoprogram/
- https://codespeak.dev/
- (Software Upgrading) https://github.com/alibaba/page-agent
- https://superdesign.dev/
- https://www.designprompts.dev/
