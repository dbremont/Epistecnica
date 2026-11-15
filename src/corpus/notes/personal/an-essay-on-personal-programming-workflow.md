---
tags: [note, guia]
---

# An Essay On Personal Programming Workflow

**Contains:** [A Guide on AI-Assisted Programming](/view.html?p=notes/personal/a-guide-on-ai-assisted-programming.md)

> A **Programming Workflow** is the structured sequence of activities, tools, representations, and interactions through which software is designed, written, tested, analyzed, and delivered. It encompasses the end-to-end process by which developers transform requirements or ideas into functioning code, combining human decision-making with automated tooling and computational feedback loops.
> 

> **AI-assisted programming** refers to the use of artificial intelligence tools and models to help developers write, debug, and maintain code more efficiently. It spans a wide range of capabilities, from code completion to full-on code generation, and even system design and testing support.
> 

> 🚨 Note: In contemporary AI discourse, almost everything is called an *agent* — but most of these systems are not. A clear example is the Gemini CLI, which is simply an API wrapper and lacks any agentic autonomy.
> 

> For AI Assisted ( https://www.bremontix.xyz/lab/pro/Production/Industry/Software/Production/Autoprogram/).
> 

## Index

## Task Space

> What is the task **space of programming**?
> 

| **Category** | **Representative Tasks** | **Tool(s)** | **AI Impact Level** |
| --- | --- | --- | --- |
| **Understanding & Specification** | Requirements analysis, domain modeling, feasibility studies | ChatGPT / Claude (analysis), UML generators, Requirements Assistants | **1–2** |
| **System Design** | Architecture design, API design, data modeling | ChatGPT / Claude (design), Mermaid, Swagger/OpenAPI generators | **1–2** |
| **Coding** | Code authoring, scaffolding, refactoring | GitHub Copilot, GPT-5 Code, Cursor IDE, Amazon CodeWhisperer | **3** |
| **Debugging** | Bug localization, log analysis, test generation | GPT-5 Debug Assist, Copilot Debug, ChatGPT Log Analyzer | **2–3** |
| **Performance Engineering** | Profiling, optimization, tuning | GPT-5 Perf Assist, Perf/Trace analyzers, AI profiler interpreters | **1–2** |
| **Tooling / Dev Environment** | CI/CD, build pipelines, environment setup | GPT-5 DevOps, Copilot CLI, AI YAML/Infra generators | **2–3** |
| **Collaboration** | Code review, documentation, knowledge transfer | GPT-5 Review Assistant, Copilot PR Review, ChatGPT Tech Writer | **2–3** |
| **Maintenance** | Legacy code understanding, dependency upgrades, refactoring at scale | GPT-5 Code Explain, Repo Summaries, Patch Assistants | **2** |
| **Operations** | Infrastructure configuration, monitoring, incident response | GPT-5 Ops Agent, AI Observability Assistants, K8s/Infra generators | **2–3** |
| **Verification** | Test generation, formal spec checks, contract validation | GPT-5 TestGen, AI Static Analyzers, Spec Assistants | **1–2** |
| **Prototyping** | Rapid creation of minimal features, mock APIs, UI prototypes | ChatGPT / Claude (rapid prototyping), Copilot Generate | **2–3** |
| **Security** | Vulnerability detection, code scanning, dependency risks | AI SAST/DAST tools, GitHub Advanced Security + Copilot, GPT-5 Sec Assist | **1–2** |
| **Product Validation** | Behavior validation, scenario simulation, requirement-to-test mapping | GPT-5 Behavior Sim, Test Mapping Assistants | **1–2** |
| **…** | Additional future or domain-specific tasks | — | — |
|  | Code Search |  |  |
| Monitoring | … |  |  |

| **Category** | **Task** | **Description** | **Level** | **Tools** |
| --- | --- | --- | --- | --- |
| **Problem Understanding & Specification** | Requirements Understanding | Interpreting user needs, constraints, domain rules | 1–2 |  |
| **Problem Understanding & Specification** | Domain Modeling | Identifying entities, relations, invariants | 1–2 |  |
| **Problem Understanding & Specification** | Feasibility Analysis | Evaluating complexity, constraints, tradeoffs | 1 |  |
| **System Design** | Architectural Design | Layering, modularization, software patterns | 2 |  |
| **System Design** | API Design | Defining endpoints, schemas, contracts | 1–2 |  |
| **System Design** | Data Modeling | Designing schemas and data flows | 2 |  |
| **System Design** | Algorithm Selection | Choosing algorithmic strategies | 1–2 |  |
| **Implementation** | Code Authoring | Writing functions, classes, modules | **3** |  |
| **Implementation** | Refactoring | Improving structure without changing behavior | 2–3 |  |
| **Implementation** | Pattern Application | Implementing idioms, templates, architectural patterns | 2–3 |  |
| **Implementation** | Boilerplate Generation | Project setup, scaffolding | **3** |  |
| **Implementation** | Low-Level Implementation | Memory mgmt, bit ops, perf-sensitive code | 1–2 |  |
| **Debugging & Verification** | Static Debugging | Reading code, detecting logical bugs | 2–3 |  |
| **Debugging & Verification** | Dynamic Debugging | Analyzing breakpoints, traces, logs | 2–3 |  |
| **Debugging & Verification** | Test Case Generation | Unit/integration test generation | **3** |  |
| **Debugging & Verification** | Formal Specification | Writing invariants & contracts | 1–2 |  |
| **Debugging & Verification** | Verification | Checking correctness | 1–2 |  |
| **Performance Engineering** | Profiling | Measuring CPU, memory, IO behavior | 2 |  |
| **Performance Engineering** | Optimization | Improving runtime or resource use | 2 |  |
| **Performance Engineering** | Resource Tuning | Threads, caches, buffers | 1–2 |  |
| **Tooling & Environment** | Dev Environment Setup | Editors, runtimes, toolchains | 2 |  |
| **Tooling & Environment** | Build Pipeline | CI/CD configuration | 2–3 |  |
| **Tooling & Environment** | Dependency Management | Versioning, library selection | 1–2 |  |
| **Collaboration** | Code Review | Reviewing diffs & PRs | 2–3 |  |
| **Collaboration** | Documentation | Writing docs, READMEs, guides | **3** |  |
| **Collaboration** | Knowledge Transfer | Summarizing repos & onboarding | 2–3 |  |
| **Maintenance & Evolution** | Legacy Code Reading | Understanding old or unfamiliar codebases | 2–3 |  |
| **Maintenance & Evolution** | Dependency Upgrades | Safe migration & version upgrades | 2 |  |
| **Maintenance & Evolution** | De-risking | Identifying fragile or complex code hotspots | 2–3 |  |
| **Deployment & Operations** | Infrastructure Config | Terraform, K8s, IaC provisioning | **3** |  |
| **Deployment & Operations** | Monitoring | Logs, traces, alerts interpretation | 2–3 |  |
| **Deployment & Operations** | Incident Response | Diagnosing outages & failures | 2 |  |

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

## References

- ‣https://github.com/google-gemini/gemini-cli
- https://github.com/All-Hands-AI/OpenHands
- [Agentic System](https://app.notion.com/p/Agentic-System-1b5c0f5171ec802db3b2f70081ecaf6a?pvs=21)
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
- [https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
- deepseek/deepseek-r1-0528-qwen3-8b / [https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode) /
- https://openrouter.ai/
- https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- [System](https://app.notion.com/p/System-248c0f5171ec80a692d2ee54ee4fe677?pvs=21)
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
- [Code Search](https://app.notion.com/p/Code-Search-ad65b85fa3714679a57e07c027b91b88?pvs=21)
