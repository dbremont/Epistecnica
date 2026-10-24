---
tags: [interaction-action-actuator]
---

# Model Context Protocol (MCP)

 : Retrieval-Augmented Generation (RAG) (Retrieval-Augmented%20Generation%20(RAG)%2013bc0f5171ec80e2bf8bfa0d05235b9a.md)

> In this node we will make sense of the `Model Context Protocol (MCP)`  and the the bigger technical element - that is part of.
> 

> MCP is not an isolated technical object but a constituent element of a larger Production Technical System. The system comprises the LLM, the MCP protocol, MCP clients and servers, tool providers, resource providers, and the external technical systems with which they interact.
> 

## Breviarium

> It is a standard protocol that an LLM uses to interact with a variety of underlying systems through a protocol-compliant interaction layer. The LLM communicates with an abstract system - that talk to particular ones - similar to `LSP`.
> 

> Note:  **MCP-Compliant (Interaction Layer)** can aggregate several underlying elements - systems .
> 

```jsx
          ┌──────────────┐
          │     User     │
          └─────────────┘
                  │
                  │
                  ▼
         ┌──────────────────┐
         │    MCP Host      │ ◄──── (LLL Orchectration Layer,
         │  (e.g., Cursor)  │        memory, and JSON-RPC transport)
         └─▼──────────────▼─┘
           │              │
           │ (Native API) │ (JSON-RPC over Stdio/HTTP)
           ▼              ▼
    ┌──────────────┐   [ Model Context Protocol Layer ]
    │  LLM Model   │              │
    │ (Text In/Out)│     ┌────────┴────────┬──────────────────┐
    └──────────────┘     ▼                 ▼                  ▼
                    ┌──────────┐     ┌───────────┐     ┌──────────────┐
                    │  Server  │     │  Server   │     │  Aggregator  │
                    │ (GitHub) │     │(Postgres) │     │   (Custom)   │
                    └────┬─────┘     └─────┬─────┘     └──────┬───────┘
                         │                 │                  │
                         ▼                 ▼                  ▼
                    ┌──────────┐     ┌───────────┐     ┌──────────────┐
                    │Source    │     │Enterprise │     │Image, Audio, │
                    │Code (Git)│     │Data (SQL) │     │Media APIs    │
                    └──────────┘     └───────────┘     └──────────────┘
```

### Model Context Protocol Functionality Set

| **Category** | **Functionality** | **Description** |
| --- | --- | --- |
| Discovery | Capability Discovery | Discover the tools, resources, and prompts exposed by an MCP server. |
| Resource Access | Resource Retrieval | Read structured or unstructured resources such as files, documents, database objects, or API responses. |
| Tool Invocation | Tool Execution | Invoke executable operations provided by external systems. |
| Prompt Management | Prompt Provision | Retrieve reusable prompts or prompt templates supplied by the server. |
| Context Management | Context Provision | Supply additional contextual information required for reasoning or task execution. |
| Communication | Standardized Messaging | Exchange requests and responses using the MCP protocol. |
| Integration | External System Integration | Connect AI systems to databases, repositories, APIs, file systems, and enterprise applications. |
| Security | Authentication & Authorization | Authenticate clients and enforce access-control policies. |
| State Management | Session Context | Maintain conversational or execution context across interactions when supported. |
| Result Exchange | Structured Responses | Return structured, machine-readable results that the AI can reason over. |
| Error Handling | Error Reporting | Communicate failures and diagnostic information in a standardized format. |
| Extensibility | Capability Extension | Allow new tools, resources, and prompts to be added without changing the protocol. |

### **Technical System Structure**

| Category | Element | Description |
| --- | --- | --- |
| Actor | User | Human interacting with the AI system. |
| Intelligent Component | LLM / AI | Performs reasoning, planning, and tool orchestration. |
| Communication Protocol | Model Context Protocol (MCP) | Standard protocol through which the LLM discovers and invokes external capabilities. |
| Integration Layer | MCP Server | Implements the MCP specification and exposes tools, resources, and prompts to the LLM. |
| Integration Pattern | Aggregation Server | An MCP server that federates multiple underlying systems behind a single MCP endpoint. |
| Data Source | Database | Structured enterprise data accessed through the MCP server. |
| Source Control | Git Repository | Source code repositories (e.g., GitHub, GitLab). |
| Storage | Filesystem | Documents, configuration files, logs, and other file-based resources. |
| External System | REST API | Business applications and web services exposed through API connectors. |
| External System | Media Services | Image, audio, video, or document processing services. |
| Enterprise System | Business Systems | ERP, CRM, financial systems, identity providers, and other enterprise applications. |
|  | **Transport** |  |
|  | **Message Structure** |  |
|  | **Message Structure** |  |
|  | **Context Management** |  |

## **Model Context Protocol (MCP) Server**

> It seeds in-front of the LLM;  and can apply the changes of the LLM.
> 

> **Manages context-aware communication between clients and large language models (LLMs)** — preserving conversation history, handling memory, applying system-level instructions, and optionally coordinating with multiple backend models.
> 

## Competing Production Technical Element Set

| **Approach** | **Key Examples** | **Core Mechanism** | **Strengths** | **Limitations** | **Use Cases** |
| --- | --- | --- | --- | --- | --- |
| **Direct Interaction** |  |  |  |  |  |
| **Native Model Tool Calling** | OpenAI Functions, Anthropic Tool Use | Model outputs structured JSON/API calls natively during inference. | Low latency; seamless model integration; no external dependencies. | Vendor lock-in; limited to specific models; no cross-model standardization. | Simple API integrations; single-model workflows. |
| **Agent Frameworks** | LangChain Agents, LlamaIndex Tools | Orchestrates tool calls via reasoning loops (ReAct, Plan-and-Execute). | Flexible; supports complex multi-step tasks; extensible tool ecosystem. | High latency; brittle error handling; steep learning curve. | Multi-step reasoning; dynamic tool chaining. |
| **Function Calling Libraries** | DSPy, Guidance, Outlines | Constrains model output generation using schemas/grammars for reliable tool calls. | Deterministic outputs; model-agnostic; reduces hallucination. | Requires prompt engineering; limited to pre-defined tools; less dynamic. | Structured data extraction; constrained APIs. |
| **API Gateway Orchestration** | Azure API Management, Kong AI Gateway | External gateway validates/reroutes model-generated API calls to tools. | Security controls; monitoring; model-agnostic; scales independently. | Adds infrastructure complexity; indirect model-tool communication. | Enterprise deployments; security-sensitive apps. |
| **Webhook-Based Systems** | Zapier, Make (Integromat) | Triggers tool calls via HTTP webhooks from model outputs. | No-code integration; vast pre-built connectors; event-driven. | Limited to HTTP-based tools; no real-time context sharing. | Workflow automation; SaaS integrations. |
| **Fine-Tuned Tool Models** | Gorilla, Toolformer | Models fine-tuned to generate accurate tool calls/API syntax. | High accuracy for specific tools; reduces prompt engineering. | Tool-specific; requires retraining for new tools; costly. | Specialized domains (e.g., APIs, code generation). |
| **Multi-Agent Systems** | AutoGen, CrewAI, MetaGPT | Multiple agents collaborate, using tools to solve subtasks. | Handles complex problems; parallel execution; role specialization. | Coordination overhead; resource-intensive; unpredictable behavior. | Complex workflows; collaborative tasks. |
| **Semantic Kernels** | Microsoft Semantic Kernel, OpenAI Assistants | Plugins/tools bound to models via kernel with memory/context management. | Stateful sessions; persistent context; vendor-neutral (partially). | Limited to supported frameworks; less transparent than MCP. | Conversational apps; stateful workflows. |
| **Custom SDKs** | Hugging Face Transformers Agents, IBM Granite | Framework-specific tool registries with model adapters. | Optimized for specific ecosystems; rich tool libraries. | Fragmented standards; interoperability challenges. | Model-specific deployments; research. |

## Final Use Case Set

> Interaction with other systems.
> 

| Final Use Case | Description |
| --- | --- |
| Query Data | Retrieve information from databases and other structured data sources. |
| Access Knowledge | Read documents, files, repositories, and other information resources. |
| Execute Actions | Perform operations through external tools and services. |
| Analyze Systems | Analyze logs, metrics, traces, source code, or other technical artifacts. |
| Generate Artifacts | Produce reports, documentation, code, or other outputs. |
| Automate Workflows | Coordinate multiple tools and systems to accomplish a task. |
| Monitor Systems | Observe the state and health of technical systems. |
| Support Decision-Making | Provide recommendations based on integrated information from multiple systems. |

## QA

### Do LLMs natively include support for functioning as an MCP client?

> Usually not:
> 

| Component | Role |
| --- | --- |
| **LLM model** | Generates completions (text, image, etc.), no built-in MCP logic |
| **MCP client** | Interfaces between model and MCP server; handles protocol operations |
| **MCP server** | Exposes tools, resources, prompts that the LLM can use |

## References

- https://github.com/dbremont/mlsys-lab/blob/main/case/mcp-lab/README.md
- https://github.com/crystaldba/postgres-mcp
- https://mcpservers.org/
- https://www.cherry-ai.com/
- https://openrouter.ai/
- https://github.com/open-webui/open-webui
- https://lmstudio.ai/
- https://github.com/modelcontextprotocol
- https://fastapi.tiangolo.com/
- https://github.com/QwenLM/Qwen-Agent
- https://github.com/modelcontextprotocol/servers
- https://huggingface.co/Qwen/Qwen3-8B
- https://docs.vllm.ai/en/latest/#
- https://blog.stackademic.com/everything-you-need-to-know-about-the-model-context-protocol-mcp-from-anthropic-84acdb3c1a2f
- https://news.ycombinator.com/item?id=42237424
- https://news.ycombinator.com/item?id=42867050
- https://github.com/QwenLM/Qwen-Agent
- https://k33g.hashnode.dev/understanding-the-model-context-protocol-mcp
- https://jan.ai/docs

- [ ]  Qwen
    - [x]  Ollama
    - [ ]  https://lmstudio.ai/
    - [ ]  https://qwenlm.github.io/blog/qwen3/
    - [ ]  Model Protocol

- [ ]  https://github.com/continuedev/continue
- [ ]  [https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)
- [ ]  https://python.langchain.com/docs/concepts/tool_calling/
