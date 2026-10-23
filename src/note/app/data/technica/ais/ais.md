---
tags: []
qa:
  - How can we reason deeply about these kinds of systems? What technical ontology underlies them? What is the nature of these systems (general-purpose, synthetic computation)? Are they even computational systems? Does the concept of computation make sense in this domain?
---

# Active Inference System

> **Note:** Here, *intelligence* refers simply to a **trainable system for solving intractable computational problems**.

> **Machine Intelligence System:** A computational system that either (1) consists of a trained machine learning model or (2) wraps one or more trained machine learning models with additional software components that provide capabilities such as inference, memory, retrieval, planning, tool use, orchestration, or interaction.

> **Machine Active Inference** is preferable to **Machine Learning** because it frames machines as systems that continuously infer, predict, act, and update through feedback, while requiring us to understand their mechanisms **on their own ontological terms rather than projecting human concepts such as intelligence, understanding, or cognition onto them**.

## Formulation

> ...

## Product Space

> Which are the types of Machine Intelligence Systems?

| **Type** | **Subtype** | **Definition** | **Instance(s)** |
| --- | --- | --- | --- |
| **Predictive System** | Classification | Assigns inputs to predefined classes. | Spam classifier, disease diagnosis. |
|  | Regression | Predicts continuous values. | House price prediction, weather forecasting. |
|  | Forecasting | Predicts future states from temporal data. | Demand forecasting, stock prediction. |
|  | Ranking | Produces ordered outputs. | Search ranking, recommendation ranking. |
| **Generative System (GS) (GM)** | Language Generation Model (LGM) | Produces natural language. | ChatGPT, Claude. |
|  | Code Generation | Produces executable source code. | GitHub Copilot, Code Llama. |
|  | Image Generation | Produces images. | Midjourney, Stable Diffusion. |
|  | Audio Generation | Produces speech or music. | ElevenLabs, MusicGen. |
|  | Video Generation | Produces videos. | Sora, Veo. |
|  | 3D Generation | Produces 3D assets. | Tripo AI, DreamGaussian. |
|  | (Mixed) Multimodal  Generation Model (MGM)| | | 
|  | Language Generation Model - Inference-Time Computation (LGM-ITC) | |
| **Conversational System** | Chat Assistant | General conversational interaction. | ChatGPT, Claude. |
|  | Customer Support | Domain-specific support automation. | Banking chatbot, IT helpdesk bot. |
|  | Voice Assistant | Spoken dialogue interface. | Siri, Alexa. |
| **Retrieval System** | Semantic Search | Retrieves semantically relevant documents. | Enterprise search, vector search. |
|  | Question Answering | Retrieves evidence to answer questions. | RAG systems. |
|  | Knowledge Discovery | Finds relationships across information. | Research assistants. |
| **Recommendation System** | Content Recommendation | Recommends media or information. | Netflix, YouTube. |
|  | Product Recommendation | Suggests products. | Amazon recommendations. |
|  | Personalized Ranking | Optimizes user-specific ordering. | News feeds. |
| **Reasoning System** | Logical Reasoning | Performs symbolic inference. | Rule engines. |
|  | Mathematical Reasoning | Solves mathematical problems. | Math-specialized LLMs. |
|  | Scientific Reasoning | Supports scientific hypothesis generation. | Research assistants. |
|  | Legal Reasoning | Reasons over legal documents. | Legal AI assistants. |
| **Planning System** | Task Planning | Produces task sequences. | AI task planners. |
|  | Route Planning | Optimizes navigation. | Google Maps routing. |
|  | Workflow Planning | Plans enterprise workflows. | Process automation. |
| **Decision Support System** | Clinical Decision Support | Supports healthcare decisions. | Medical diagnosis assistants. |
|  | Financial Decision Support | Supports investment or lending. | Credit advisory AI. |
|  | Business Decision Support | Supports operational decisions. | Supply-chain optimization. |
| **Control System** | Robotic Control | Controls robotic motion. | Industrial robots. |
|  | Process Control | Controls industrial processes. | Chemical plant controllers. |
|  | Vehicle Control | Controls autonomous vehicles. | Self-driving systems. |
| **Autonomous Agent** | Software Agent | Executes software tasks autonomously. | OpenAI Operator, coding agents. |
|  | Web Agent | Navigates and operates websites. | Browser automation agents. |
|  | Research Agent | Conducts multi-step research. | Deep research systems. |
|  | Multi-Agent System | Multiple collaborating agents. | Collaborative AI teams. |
| **Perception System** | Computer Vision | Understands images and video. | Object detection. |
|  | Speech Recognition | Transcribes speech. | Whisper. |
|  | Sensor Fusion | Combines multiple sensor streams. | Autonomous vehicles. |
| **Multimodal System** | Vision-Language | Combines text and images. | GPT-4o, Gemini. |
|  | Audio-Language | Combines speech and language. | Voice assistants. |
|  | Unified Multimodal | Integrates text, image, audio, and video. | Modern multimodal foundation models. |
| **Embodied Intelligence System** | Humanoid Robot | General-purpose physical agent. | Figure AI, Optimus. |
|  | Mobile Robot | Autonomous navigation platform. | Warehouse robots. |
|  | Autonomous Vehicle | Self-driving transportation. | Waymo. |
|  | Industrial Robot | Manufacturing automation. | Robotic assembly arms. |
|  | **Agentic System** | | |

## Case Study

| **System** | **Description** | **Classification** |
| --- | --- | --- |
| **OpenClaw** | Self-hosted AI assistant that orchestrates LLMs, tools, memory, MCP servers, and workflows to autonomously perform tasks. | **Agentic Orchestration System** |
| **OpenCode** | AI-powered coding assistant that integrates LLMs into the software development workflow. | **Coding Intelligence System** |
| **ChatGPT** | General-purpose conversational AI with reasoning, coding, multimodal interaction, and tool use. | **Conversational Intelligence System** |
| **Claude Desktop** | Desktop AI assistant with MCP integration, document analysis, and tool invocation. | **Conversational Intelligence System** |
| **GitHub Copilot** | AI pair programmer integrated into development environments. | **Coding Intelligence System** |
| **Cursor** | AI-native code editor with integrated programming assistance. | **Coding Intelligence System** |
| **Perplexity** | AI-native search and answer engine combining retrieval with language generation. | **Retrieval Intelligence System** |
| **Open WebUI** | Self-hosted interface for interacting with local and remote LLMs, agents, and tools. | **LLM Interaction System** |
| **Manus** | Autonomous AI agent capable of planning and executing complex multi-step tasks. | **Agentic Orchestration System** |
| **Lovable** | AI application for generating and iterating on full-stack web applications. | **Software Generation System** |
| **CrewAI** | Multi-agent framework for coordinating specialized AI agents to collaboratively execute workflows. | **Multi-Agent Orchestration System** |
| **AutoGen** | Framework for building collaborative, conversational multi-agent applications. | **Multi-Agent Orchestration System** |
| **LangGraph** | Framework for constructing stateful agent workflows as execution graphs. | **Agent Workflow System** |
| **OpenAI Agents SDK** | Framework for developing AI agents with tool use, handoffs, memory, and structured execution. | **Agent Development Framework** |
| **Flowise** | Visual platform for building LLM, RAG, and agent workflows. | **Agent Workflow System** |
| **Dify** | Platform for building, deploying, and operating AI applications and agents. | **AI Application Platform** |
| **AnythingLLM** | Self-hosted workspace for RAG, document interaction, and AI assistants. | **Knowledge Intelligence System** |
| **LibreChat** | Multi-provider conversational AI interface with tool and agent support. | **LLM Interaction System** |
| **n8n AI Agent** | Workflow automation platform with integrated AI agents and LLM capabilities. | **Agent Workflow System** |
| **Microsoft Copilot** | Enterprise AI assistant integrated across Microsoft products and services. | **Enterprise Intelligence System** |
| **Google Gemini** | General-purpose multimodal conversational AI assistant. | **Conversational Intelligence System** |
| **NotebookLM** | AI-powered notebook for document understanding, synthesis, and question answering. | **Knowledge Intelligence System** |
| **Devin** | Autonomous software engineering agent capable of planning, coding, debugging, and executing development tasks. | **Software Engineering Agent** |
| **Atlassian Rovo** | Enterprise AI platform integrated into Jira, Confluence, and other Atlassian products, providing search, chat, specialized agents, and workflow automation. | **Enterprise AI Harness** or **Agentic Orchestration System** |
|  |  |  |

## Which are the Agent System Software?

| Agent System Software | Description |
| --- | --- |
| **OpenClaw** | Persistent, self-hosted personal agent that can use models, tools, messaging channels, memory, files, browsers, terminals, and scheduled tasks. ([OpenClaw](https://openclaw.ai/?utm_source=chatgpt.com)) |
| **Muse** | Personal AI agent designed to operate across a user's digital environment and perform tasks on the user's behalf. |
| **Instinct** | Personal agent designed to interact with a user's applications, devices, and information environment. |
| **Manus** | General-purpose autonomous agent that decomposes user objectives into multi-step tasks and executes them in a computer environment. ([Manus](https://www.manus.im/blog/openclaw-vs-manus-desktop?utm_source=chatgpt.com)) |
| **Perplexity Computer** | Agentic computer environment capable of orchestrating multiple models and executing multi-step tasks across applications and the web; it also has a local/portable version. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/perplexitys-local-ai-agent-comes-to-windows-but-only-for-rtx-gpus-with-at-least-24gb-of-vram-portable-computer-brings-ai-for-multistep-tasks-to-compatible-pcs?utm_source=chatgpt.com)) |
| **Claude Cowork** | Desktop-oriented agent system from Anthropic that can work with files and applications and execute longer-running tasks rather than merely answer conversationally. ([Reuters](https://www.reuters.com/business/media-telecom/anthropic-fold-claude-ai-features-into-one-interface-launches-document-tools-2026-09-16/?utm_source=chatgpt.com)) |
| **ChatGPT Agent** | General-purpose agent system combining reasoning with browsing, computer interaction, and tool use to perform multi-step tasks. |
| **Google Antigravity** | Agent-first development environment in which software-development agents can plan and execute tasks using an integrated computer environment. |
| **Devin** | Autonomous software-engineering agent that can plan, code, operate development environments, and execute software-development tasks. |
| **Rabbit r1 (RabbitOS)** | Agent-oriented personal-computing system designed to execute actions across services through a natural-language interface. |
| **Genspark Super Agent** | General-purpose agent system capable of carrying out multi-step research, creation, and computer tasks. |
| **Adept** | Agent system focused on allowing AI to operate software through natural-language instructions and computer interaction. |
| **OpenAI Operator** | Computer-use agent designed to interact with websites and execute tasks through a browser/computer interface. |
| **Microsoft Copilot (Copilot Cowork)** | Agentic assistant environment integrated with Microsoft's productivity ecosystem and capable of carrying out multi-step work. |
| **Google Gemini Agent (Gemini computer-use agents)** | Google's agentic systems for reasoning, tool use, application interaction, and task execution. |
| **Amazon Alexa+** | Agentic personal assistant system integrating conversational reasoning with actions across Amazon and connected services. |
| **Siri with Apple Intelligence** | Apple's evolving personal-agent architecture combining personal context, application interaction, and action execution. |
| **Google Assistant / Gemini for Home** | Agentic assistant environment capable of interacting with connected devices and services; Google's Home infrastructure now exposes agent access through MCP. ([The Verge](https://www.theverge.com/tech/996310/google-home-mcp-integration-agentic-ai-smart-home-price-release-date?utm_source=chatgpt.com)) |

## QA

### How to design a system similar to **Rovo?**

### How to install Openclaw?

- `./scripts/docker/setup.sh`
- …

```jsx

==> Docker gateway defaults
Container openclaw-openclaw-gateway-run-b380112dc5be Creating 
Container openclaw-openclaw-gateway-run-b380112dc5be Created 
Pinned gateway.mode=local and gateway.bind=lan for Docker setup.
Set gateway.controlUi.allowedOrigins to ["http://localhost:18789","http://127.0.0.1:18789"] for non-loopback bind.

==> Provider setup (optional)
WhatsApp (QR):
  docker compose -f /home/dbremont/Documents/openclaw/docker-compose.yml run --rm openclaw-cli channels login
Telegram (bot token):
  docker compose -f /home/dbremont/Documents/openclaw/docker-compose.yml run --rm openclaw-cli channels add --channel telegram --token <token>
Discord (bot token):
  docker compose -f /home/dbremont/Documents/openclaw/docker-compose.yml run --rm openclaw-cli channels add --channel discord --token <token>
Docs: https://docs.openclaw.ai/channels

==> Starting gateway
[+] up 1/1
 ✔ Container openclaw-openclaw-gateway-1 Started                                                                                                                                        0.2s
[+]  1/1t 1/11
 ✔ Container openclaw-openclaw-gateway-1 Running                            0.0s
Container openclaw-openclaw-cli-run-5bcef6d769fc Creating 
Container openclaw-openclaw-cli-run-5bcef6d769fc Created 

Gateway running with host port mapping.
Access from tailnet devices via the host's tailnet IP.
Config: /home/dbremont/.openclaw
Workspace: /home/dbremont/.openclaw/workspace
Token: stored in Docker environment/config (not printed).

Commands:
  docker compose -f /home/dbremont/Documents/openclaw/docker-compose.yml logs -f openclaw-gateway
  docker compose -f /home/dbremont/Documents/openclaw/docker-compose.yml exec openclaw-gateway sh -lc 'node dist/index.js health --token "$OPENCLAW_GATEWAY_TOKEN"'
```

- `export OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32)`
- docker composed
- docker compose up -d

### How to monitor Openclaw?

### How to extend Openclaw?

| Extension Point | Technical Role | Changes |
| --- | --- | --- |
| Plugin | Capability expansion | What the system can become |
| Tool | Actuator | What actions it can perform |
| Skill | Procedural knowledge | How it performs tasks |
| Hook | Regulation/control | What actions are allowed |
| Channel | Input boundary | How events enter |
| Model provider | Cognitive substrate | Reasoning capability |
| Memory adapter | State persistence | What it remembers |
| Sandbox | Constraint boundary | Allowed state transitions |

### What is an channel in Openclaw?

```jsx
◇  How channels work ───────────────────────────────────────────────────────────────────────╮
│                                                                                           │
│  Inbound DM safety defaults to pairing: unknown senders get a pairing code first.         │
│  Approve with: openclaw pairing approve <channel> <code>                                  │
│  Open/public DMs require dmPolicy="open" plus allowFrom=["*"].                            │
│  For multi-user DMs, isolate sessions with: openclaw config set session.dmScope           │
│  "per-channel-peer" (or "per-account-channel-peer" for multi-account channels).           │
│  Docs: channels/pairing                                                                   │
│                                                                                           │
│  Feishu: 飞书/Lark enterprise messaging with doc/wiki/drive tools.                        │
│  Google Chat: Google Workspace Chat app with HTTP webhook.                                │
│  Nostr: Decentralized protocol; encrypted DMs via NIP-04.                                 │
│  Microsoft Teams: Teams SDK; enterprise support.                                          │
│  Mattermost: self-hosted Slack-style chat; install the plugin to enable.                  │
│  Nextcloud Talk: Self-hosted chat via Nextcloud Talk webhook bots.                        │
│  Matrix: open protocol; install the plugin to enable.                                     │
│  Raft: Raft CLI wake bridge for human and agent collaboration.                            │
│  LINE: LINE Messaging API webhook bot.                                                    │
│  Zalo: Vietnam-focused messaging platform with Bot API.                                   │
│  ClickClack: self-hosted chat via first-class ClickClack bot tokens.                      │
│  Zalo Personal: Zalo personal account via QR code login.                                  │
│  SMS: Twilio-backed SMS with inbound webhooks and outbound replies.                       │
│  Synology Chat: Connect your Synology NAS Chat to OpenClaw with full agent capabilities.  │
│  Tlon: decentralized messaging on Urbit; install the plugin to enable.                    │
│  Discord: very well supported right now.                                                  │
│  iMessage: Local iMessage/SMS through the imsg bridge, including private API message      │
│  actions when enabled.                                                                    │
│  IRC: classic IRC networks with DM/channel routing and pairing controls.                  │
│  QQ Bot: connect to QQ via official QQ Bot API with group chat and direct message         │
│  support.                                                                                 │
│  Reef: Guarded end-to-end encrypted claw messaging.                                       │
│  Signal: signal-cli linked device with extra setup for the local REST bridge.             │
│  Slack: supported (Socket Mode).                                                          │
│  Telegram: simplest way to get started — register a bot with @BotFather and get going.    │
│  Twitch: Twitch chat integration                                                          │
│  WhatsApp: works with your own number; recommend a separate phone + eSIM.                 │
│  WeCom: Enterprise messaging and documents, scheduling, task tools.                       │
│  Weixin: Personal WeChat messaging via QR-code login.                                     │
│  Zalo ClawBot: Personal Zalo assistant bot via QR-code login — owner-bound, no setup.     │
│  Yuanbao: Tencent Yuanbao AI assistant conversation channel.    
```

### **Which are the benchmark indices for LLM systems?**

- [LiveBench](https://livebench.ai/#/)
- [AI model benchmarks compared — the AW Bench Index · ArtificialWatch](https://artificialwatch.com/benchmarks)
- [Epoch AI](https://epoch.ai/)
- Vals Index

### What is the typology of data format?

```
Raw Data
   ↓
Training Instances
   ↓
JSONL / Parquet / dataset records
   ↓
Tokenization
   ↓
Token Sequences
   ↓
Packing / Batching
   ↓
GPU Tensors
   ↓
Training
```

### Which are the crititism to the terms “Test-Time Compute”?

-  Inference-Time Computation (ITC)

### Which are the crititism to the terms “Language Model”?

> The term `language model`, without any clarification, refers to a broad class of models rather than any specific model. If you mean a generative next-token model, you should use a more specific term rather than appropriating the abstract term `language model`.

## References

- https://martinfowler.com/articles/harness-engineering.html
- https://lilianweng.github.io/posts/2026-07-04-harness/
- https://openclaw.ai/
- https://github.com/crewaiinc/crewai
- https://github.com/assistant-ui/assistant-ui
- https://github.com/open-webui/open-webui
- https://clawhub.ai/
- [Observational](https://app.notion.com/p/Observational-111c0f5171ec801195d6ef963907bf3b?pvs=21)
- [Electronic System](https://app.notion.com/p/Electronic-System-225c0f5171ec8031ab77cac045137d2a?pvs=21)
- [Dynamical Intelligence](https://app.notion.com/p/Dynamical-Intelligence-a41fde247c384e3bb5e561bf55c70f33?pvs=21)
- https://www.interconnects.ai/p/glm-53-how-chinese-labs-keep-stride
- https://docs.ag-ui.com/introduction
- https://github.com/dbremont/mlsys-lab
- [**System Connector**](https://app.notion.com/p/System-Connector-3e1c0f5171ec80a0b7f0e810605aa191?pvs=21)
- https://instinct.com/
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- [System](system/system.md)
- [Evaluation](evaluation/evaluation.md)
- [Operation](operation.md)
- [Robotic System](../robotic-system/robotic-system.md)
- [LLM System Modelling](llm-system-modelling.md)
- [ ]  https://github.com/Tencent/AngelSpec
- [ ]  https://kvcache-ai.github.io/AgentENV/  (Virtulization - Hardware Sharing) - Firecracker vs Docker.
- [ ]  https://github.com/MoonshotAI/MoonEP
- [ ]  https://t3.codes/
