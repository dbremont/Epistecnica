---
tags: [note, production]
---

# AI-Based Program Production

> A **Programming Workflow** is the structured sequence of activities, tools, representations, and interactions through which software is designed, written, tested, analyzed, and delivered. It encompasses the end-to-end process by which developers transform requirements or ideas into functioning code, combining human decision-making with automated tooling and computational feedback loops.

> **AI-assisted programming** refers to the use of artificial intelligence tools and models to help developers write, debug, and maintain code more efficiently. It spans a wide range of capabilities, from code completion to full-on code generation, and even system design and testing support.

> 🚨 Note: In contemporary AI discourse, almost everything is called an *agent* — but most of these systems are not. A clear example is the Gemini CLI, which is simply an API wrapper and lacks any agentic autonomy.

> Note: AI is poised to revolutionize software development. We need to create a separate note to address this change.

## Guiding Questions

Process Architecture:

* How should the **software production process** be re-architected in the presence of AI code-generation systems?
* Which phases (requirements engineering, design, implementation, testing, deployment, maintenance) are transformed, compressed, automated, or eliminated?
* What new production models emerge (e.g., prompt-driven development, specification-centric development, AI-supervised pipelines, autonomous agent orchestration)?

**Structural Space of AI-Augmented Production:**

* What is the **state space** of AI-based software production?
* How can this space be formally characterized?

  * What are its primary dimensions? (e.g., autonomy level, human oversight intensity, model dependency, feedback latency, validation mechanism)
  * What are its boundary conditions?
* Which canonical production configurations exist within this space?

**Control and Governance:**

* How does control shift between:

  * Human developers
  * AI models
  * Validation systems
  * Runtime monitoring
* What new forms of supervision, verification, and epistemic assurance are required?

**Economic and Organizational Implications:**

* Does AI-based production shift the unit of productivity from:

  * Line-of-code throughput → specification clarity?
  * Implementation labor → orchestration capability?
* How does this reshape team structure, skill composition, and capital allocation?

**Epistemic Shift:**

* Is software still primarily “written,” or is it increasingly “generated” and “curated”?
* Does this transform the developer’s role from constructor to systems designer, constraint modeler, and validator?

## Feature(s) Space

> What intelligent features will power and enhance the computational tool (software)?
> 

| **Category** | **Feature** | **Description** | **Function** | **Practical Use Case** |
| --- | --- | --- | --- | --- |
| *Core Intelligence* | Adaptive Learning Engine | Continuously refines internal models based on user behavior, feedback, and environmental data. | Enables self-improvement, personalization, and evolving accuracy. | Automatically adapts analytical recommendations based on changing data patterns or workflows. |
| *Data Understanding* | Semantic Model Layer | Extracts, classifies, and connects concepts from structured and unstructured data. | Provides structured understanding and semantic interoperability. | Converts raw documents into a searchable, concept-linked knowledge base. |
| *Reasoning & Inference* | Knowledge Graph Integration | Encodes domain knowledge in graph form to support inference, reasoning, and discovery. | Enables intelligent querying and contextual decision support. | Suggests related entities or insights based on conceptual similarity. |
| *Interaction Intelligence* | Context-Aware Interface | Dynamically adjusts interface and responses based on user goals, context, and task phase. | Improves usability and task alignment. | Adapts displayed panels depending on whether the user is analyzing or editing. |
| *Assistance* | Smart Suggestions | Suggests relevant actions, parameters, or next steps based on context. | Reduces cognitive load and accelerates workflows. | Recommends dataset filters, visualization types, or code completions. |
| *Understanding* | Auto-Tagging | Detects key topics, entities, or patterns automatically. | Improves data organization and retrieval. | Tags datasets, notes, or reports by topic or domain. |
| *Summarization* | Intelligent Summary | Produces concise summaries of complex or lengthy content. | Supports rapid review and decision-making. | Generates a one-page summary of technical documentation. |
| *Organization* | Smart Clustering | Groups related data, files, or tasks automatically. | Simplifies structure and discovery. | Clusters similar research results, logs, or case studies. |
| *Communication* | Context-Aware Chat | Adapts assistance and explanations based on user profile and task. | Provides contextual, human-like support. | Explains model outputs differently for technical vs. managerial users. |
| *Automation* | Workflow Orchestrator | Automates complex, multi-step computational workflows intelligently. | Reduces manual configuration and ensures consistency. | Executes end-to-end pipelines for data cleaning, modeling, and reporting. |
| *Automation* | Auto-Completion | Predicts and completes repetitive patterns or commands. | Increases speed and reduces manual input. | Completes API calls, parameters, or code segments. |
| *Insight* | Trend Detection | Identifies emerging patterns, correlations, or anomalies. | Improves analytical awareness and forecasting. | Detects deviations in performance or user activity trends. |
| *Explainability* | Transparent Insight Module | Provides interpretable explanations for outputs or decisions. | Builds trust and supports auditing. | Displays reasoning traces for predictions in risk assessments. |
| *Optimization* | Resource-Aware Computation | Dynamically manages computation, storage, and scheduling. | Improves efficiency and scalability. | Balances local vs. cloud computation to optimize cost and latency. |
| *Search* | Semantic Search | Interprets meaning beyond keywords for smarter retrieval. | Enhances precision and recall in information access. | Finds conceptually similar documents even with different terminology. |

## Tool

### Form

> What are the presentation forms of AI tools used in a coding workflow?
> 

| **Form** | **Description** | **Instance(s)** | **Notes** |
| --- | --- | --- | --- |
| **IDE Plugin (Extension)** | Integrated into code editors; provides inline suggestions, completions, refactoring, navigation, tests, and code transformation in real time. | GitHub Copilot (VS Code, JetBrains), Cursor IDE, Amazon CodeWhisperer | The dominant interface for day-to-day coding; tightly coupled with developer activity. |
| **CLI Client (Terminal Tool)** | Text-based tool executed from the terminal; ideal for scripting, automation, repo-wide analysis, and non-interactive workflows. | Aider, OpenRouter CLI, DeepSeek CLI, Gemini CLI, Qwen CLI | Enables batch refactoring, automated commits, linting, code search, and file generation. |
| **Web Interface (SaaS Platform)** | Browser-based interface that exposes the model; useful for experimentation, prototyping, design, and high-level reasoning. | OpenAI Chat, Claude Web, Gemini Web, Ollama Cloud | Good for architectural conversations and exploratory coding—not tightly bound to your editor. |
| **Local Model Runtime (SDK / Engine)** | Local inference runtime used inside custom tooling; provides offline or private AI capabilities. | Ollama, GPT4All, LM Studio, LLaMA.cpp runtimes | Used for enterprise, on-device, or air-gapped development; high control, customizable. |
| **API Integration (Programmatic Client)** | Model accessed directly via an API from your own code, scripts, or backend systems. | OpenAI API, Claude API, Gemini API, DeepSeek API | Core building block for creating your own agents and automated development workflows. |
| **CI/CD & DevOps Integration** | AI capabilities embedded in pipelines—test generation, build scripting, deployment checks, IaC generation. | GitHub Actions + Copilot, Aider CI, DevOps LLM plugins | Automates repetitive infra tasks, generates configs, improves testing velocity. |
| **Desktop App (Standalone GUI)** | A self-contained application providing a rich interface for coding help, repo browsing, and code manipulation. | Cursor (standalone mode), Warp AI, JetBrains AI Assistant App | Useful when you prefer a controlled environment over browser-based tools. |
| **Embedded Agent in Tools (Augmented Tooling)** | AI embedded inside traditional dev tools like terminals, shells, debuggers, or linters. | Warp AI Terminal, Fig AI Commands, Bash-AI Assistants | Blends AI into micro-tools instead of full IDE integration. |
| **Repository-Aware Coding Bots** | Tools that operate on entire repositories, with memory, planning, and multi-file refactoring capabilities. | Aider (agent mode), GitHub Copilot Workspace, Claude Artifacts | Bridges the gap between assistant and agent; operates beyond single-file prompts. |

### **IDE Plugin (Extension)**

> Which are the plugin extensions that integrate AI into an IDE to enable AI-assisted coding?
> 

> **Note:** *There does not appear to be an open-source extension that provides a backend-agnostic, model-indirection layer fully separated from the underlying AI model.*
> 

> See https://github.com/continuedev/continue; https://github.com/TabbyML/tabby?tab=readme-ov-file
> 

| **IDE** | **Extension** | **Description** |
| --- | --- | --- |
| **VS Code** | GitHub Copilot | Real-time code completion, refactoring suggestions, chat, and test generation. |
|  | ChatGPT VS Code Extension | Inline explanations, code generation, file edits, and multi-file reasoning. |
|  | Codeium | Free AI completions and chat-based coding assistance. |
|  | Aider (CLI-integrated) | Uses CLI-first workflow but integrates with editor context. |
|  | DeepSeek VS Code Plugin | Fast code suggestions, commit messages, and local reasoning. |
| **JetBrains (IntelliJ, PyCharm, etc.)** | GitHub Copilot for JetBrains | In-IDE completions and coding suggestions. |
|  | JetBrains AI Assistant | Native AI features: chat, code insight, refactoring, doc generation. |
| **Neovim** | Codeium.nvim | AI autocompletion for Neovim. |
|  | Copilot.vim | Copilot integration for Vim/Neovim environments. |
|  | ChatGPT.nvim | Query ChatGPT from within Neovim buffers. |
|  | Avante.nvim / Supermaven.nvim | Fast AI autocompletion alternatives. |
| **Cursor IDE** | Built-in Cursor AI | Entire IDE designed around AI navigation, refactoring, and multi-file edits. |
| **Zed Editor** | Zed AI Assistant | Inline completions, multi-file reasoning, and project-aware operations. |
| **Xcode** | Copilot for Xcode (via plugins) | AI-augmented Swift/Obj-C workflows, completions. |
| **Vim** | Copilot.vim | GitHub Copilot extension for Vim editors. |
| **Eclipse** | ChatGPT for Eclipse | Basic AI code suggestions and documentation generation. |
| **Sublime Text** | Codeium for Sublime | AI completions for Sublime workflows. |

## Provider

> Which are the coding models providers?
> 

| **Model Provider** | **Description** | **Capability Evaluation** | **Pricing** | **Site** |
| --- | --- | --- | --- | --- |
| **OpenAI (GPT-5 / GPT-4.1 / o1)** | General-purpose coding LLMs with strong reasoning, refactoring, debugging, and multi-language capability. | **Very High** | Pay-as-you-go / subscription | openai.com |
| **Anthropic Claude (3.7 Sonnet / Opus)** | Safety-optimized reasoning models; excellent for documentation, code explanation, and repo-scale understanding. | **Very High** | Subscription / enterprise | anthropic.com |
| **GitHub Copilot** | IDE-integrated coding assistant with real-time completions and refactoring. | **High** | Subscription | github.com/features/copilot |
| **Google Gemini (1.5 Pro / CodeGemini)** | Strong code models with huge context windows and GCP integration. | **High** | Pay-as-you-go | ai.google.dev |
| **Meta Llama Code / Code Llama 2** | Open-source coding models for local or enterprise deployment. | **Medium–High** | Free / self-hosting cost | llama.meta.com |
| **Mistral (Codestral / Mistral Large)** | High-performance open-weight models optimized for code. | **High** | Free (open weight) / Paid API | mistral.ai |
| **DeepSeek (Coder / Chat)** | Efficient code-focused models good for diffs, commits, and search. | **Medium–High** | Free / Paid | deepseek.com |
| **xAI (Grok-2)** | Reasoning-strong model with solid coding competence; good for CLI workflows. | **Medium–High** | Subscription | x.ai |
| **Kimi (Moonshot AI)** | Long-context Chinese model useful for repo analysis and documentation. | **Medium–High** | Subscription | kimi.moonshot.cn |
| **Alibaba Qwen (Qwen2.5 / CodeQwen)** | Strong multilingual coding models with open and commercial variants. | **High** | Free / Pay-as-you-go | qwenlm.ai |
| **Zhipu AI (z.ai / GLM / CodeGLM)** | Provider of GLM-family models; supports multilingual code generation, reasoning, and repo analysis. Strong Chinese-language coding support. | **Medium–High** | Pay-as-you-go / enterprise | zhipu.ai |
| **Cohere (Command-R)** | Enterprise reasoning model with good structured code explanation. | **Medium** | Pay-as-you-go | cohere.com |
| **Replit (Replit Code)** | Incremental coding model optimized for browser IDE workflows. | **Medium** | Subscription | replit.com |
| **Ollama (Local runner)** | Platform to run code-capable models locally (Mistral, Llama, Qwen). | Depends on model | Free | ollama.com |


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

- [Specs](https://github.com/dbremont/specs)
- Cases
      - [research-2025-12-BusinessIndex](https://github.com/csiglab/research-2025-12-BusinessIndex)
      - ...
- [A Guide on AI-Assisted Work](https://righteous-guardian-68f.notion.site/A-Guide-on-AI-Assisted-Work-2c1c0f5171ec802f8be1d2b1d6d6c92c?source=copy_link)
- https://github.com/google-gemini/gemini-cli
- https://github.com/All-Hands-AI/OpenHands
- [Agentic System](https://www.notion.so/Agentic-System-1b5c0f5171ec802db3b2f70081ecaf6a?pvs=21)
- https://www.bremontix.xyz/lab/pro/Production/Industry/Software/
- https://simonwillison.net/2022/Oct/29/the-perfect-commit/
- https://en.wikipedia.org/wiki/Category:Virtual_assistants
- https://simonwillison.net/tags/vibe-coding/
- https://simonwillison.net/2025/May/28/automated-tests/
- https://simonwillison.net/2025/Mar/19/vibe-coding/
- https://www.timescale.com/blog/the-emerging-open-source-ai-stack
- https://www.reddit.com/r/ChatGPTCoding/comments/1kw43at/aiassisted_programming_whats_working_for_you/
- https://github.com/features/copilot
- https://jules.google/
- https://aider.chat/
- https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode
- deepseek/deepseek-r1-0528-qwen3-8b / https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode /
- https://openrouter.ai/
- https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- [Learning System](https://www.notion.so/Learning-System-248c0f5171ec80a692d2ee54ee4fe677?pvs=21)
- https://github.com/dbremont/documentorum/blob/main/tool/Aider.md
- https://www.augmentcode.com/
- https://github.com/dbremont/documentorum/blob/main/tool/Copilot.md
- https://github.com/dbremont/documentorum/blob/main/tool/Copilot.md
- https://github.com/google-gemini/gemini-cli
- https://geminicli.com/
- https://github.com/google-gemini/gemini-cli
- https://github.com/QwenLM/qwen-code
- https://news.ycombinator.com/item?id=46197930
- https://news.ycombinator.com/item?id=46231274
- [Code Search](https://www.notion.so/Code-Search-ad65b85fa3714679a57e07c027b91b88?pvs=21)
- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- https://skillsmp.com/
- https://prpm.dev/
- https://github.com/f/prompts.chat
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
- [Code Search](https://www.notion.so/Code-Search-ad65b85fa3714679a57e07c027b91b88?pvs=21)
- https://prompts.chat/
- https://github.com/dbremont/specs
- https://skills.sh/
- https://www.fast.ai/posts/2026-01-28-dark-flow/
