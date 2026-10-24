# Retrieval-Augmented Generation (RAG)

 : Haystack (Haystack%20209c0f5171ec808db37cc911f5455e94.md), LangChain (LangChain%20d86f5323e9e54e7fb972706f313cdb74.md), Language Modelling (LM) (Language%20Modelling%20(LM)%20ecd681eb6e99416a90313abf6fd23665.md), Model Context Protocol (MCP) (Model%20Context%20Protocol%20(MCP)%20203c0f5171ec80e4b835d4434cfa1e4f.md)

> How to extend a LLM?
> 

> Retrieval-Augmented Generation (RAG) enhances language model outputs by **retrieving relevant documents** from an external corpus during inference. This augments the model’s internal knowledge with dynamic, up-to-date, or domain-specific content. RAG marginalizes over retrieved contexts—i.e., it considers multiple possible contexts probabilistically—allowing the model to generate responses grounded in retrieved evidence, **all within the model’s context length.**
> 

## QA

- RAG Architecture & Principles
    - What is the core idea behind RAG and how does it differ from traditional QA systems?
    - What are the main components of a RAG pipeline, and how do they interact?
    - Explain the difference between early fusion and late fusion in the context of RAG.
    - How does a RAG system handle hallucinations differently from a standalone LLM?
    - What is marginal likelihood in RAG, and why is it used?
- Retrieval Mechanism
    - What are dense vs sparse retrievers, and what are trade-offs between them?
    - How is vector similarity computed in dense retrieval?
    - Describe how you would construct and maintain a knowledge base (KB) for RAG.
    - How would you handle retrieval when dealing with multi-lingual or domain-specific data?
    - How do you optimize retrieval quality in a hybrid (dense + sparse) setup?
- Generator Design
    - How does the context length limitation of the generator affect RAG performance?
    - How do you prepare the input to the generator (concatenation strategies, chunk formatting)?
    - How can the generator be made robust to noisy or conflicting documents?
    - What are some architectural choices for generators (e.g., BART, T5, GPT-style)?
- Training and Fine-tuning
    - How do you jointly train a retriever and a generator in a RAG system?
    - What is the loss function used for training a RAG model end-to-end?
    - How do you implement negative sampling in retriever training?
    - How do you mitigate mode collapse in dense retriever training?
- Deployment & Scaling
    - What vector stores can be used to scale RAG in production?
    - How do you keep a production RAG system’s knowledge base up to date?
    - What caching or batching strategies help improve inference efficiency in RAG systems?
    - How do you handle document versioning or re-indexing in a deployed RAG system?
- Evaluation
    - How do you evaluate a RAG system quantitatively?
    - What metrics are used for retriever quality vs. generator quality?
    - What does faithfulness mean in RAG evaluation, and how can you measure it?
    - How do you use human evaluation to improve a RAG pipeline?
- Explain the difference between RAG-token and RAG-sequence.
- How does GraphRAG work, and what problem does it solve?
- How can you distill a RAG model into a standalone generator?
- What are some approaches to reduce latency in RAG systems?
- How do you integrate structured data (e.g., databases or knowledge graphs) into a RAG pipeline?
- [Retrieval–Generation Coupling] In end-to-end differentiable RAG training, how do you backpropagate the generator loss through the retriever’s encoder, and what approximations are typically made?
- [Retrieval Representation Alignment] Describe the challenge of representation collapse in dual-encoder retrieval systems. What are advanced methods to maintain embedding expressiveness during training?
- [Context Injection Strategy] You retrieve $k$ documents, but your generator can only attend to a subset due to token limits. How do you design a policy or architecture that learns which documents to condition on, and what are the tradeoffs between score-based truncation, learned routing, and Mixture of Experts?
- [Multi-hop and Compositional Retrieval] Formalize a multi-hop retrieval pipeline for compositional questions using RAG. How do you model dependencies between hops, and what are the risks of exposure bias during training?
- Derive the full marginal likelihood for a RAG model where both retriever and generator are learned, and discuss its variational approximation using Monte Carlo sampling.
- Propose a method for token-level attribution in a RAG model — i.e., how to identify which retrieved document contributed to which generated token. How would this inform faithfulness evaluation?
- You're incrementally updating your KB and retriever while preserving previously learned retrieval behavior. What mechanisms (e.g., rehearsal, distillation, EWC) do you propose to avoid forgetting, and how would you adapt them for dense retrieval?
- How would you design a differentiable retriever with hard negative mining that scales to a corpus of 10B+ documents in a continual learning setting? Include architectural and training considerations.
- Explain how asymmetric dual encoders (query vs document encoders with different architectures) affect retrieval quality and latency in a RAG system. Under what conditions is asymmetry desirable?
- How can contrastive loss for retrieval collapse into trivial solutions? How would you diagnose and address this in a large-scale retrieval pretraining setup?
- How would you architect a streaming RAG system that retrieves context on-the-fly during token generation? What trade-offs emerge between latency, document truncation, and retrieval fidelity?
- What are the failure modes of RAG in zero-shot generalization across domains (e.g., law to medicine)? How would you design adaptive retrieval components that mitigate these failures in a real-time system?
- In a setting with continuous updates to the corpus (e.g., news or market data), how would you implement asynchronous re-indexing while preserving consistency across retriever and generator versions?
- How does the system inject the context into the generator? What format does it use? Does it use embeddings or just plain text chunks?

## Goal

> Large language models struggle to recall factual information outside their training data. RAG addresses this by integrating retrieval at inference time, enabling factual grounding in up-to-date corpora.
> 

## Key Idea

> 📚 **Knowledge Externalization**
> 
- RAG externalizes knowledge by relying on an external corpus $\mathcal{D}$, stored and indexed in a vector space.
- The retriever selects relevant documents **on the fly**, as opposed to relying on knowledge encoded in LLM parameters.

## Structure

RAG is composed of **two modular components**, typically wired in a pipeline:

- A **retriever** $R: \mathcal{Q} \rightarrow \mathcal{C}^k$ that maps a query to top-*k* candidate contexts.
- A **generator** $G: (\mathcal{Q}, \mathcal{C}^k) \rightarrow \mathcal{Y}$ that conditions on those contexts to produce output.

These modules can be:

- Trainable or fixed
- Dense, sparse, or hybrid
- Local or API-based

## Inference Pipeline

```
      ┌───────────────────────────┐
      │        User Query         │
      └────────────┬──────────────┘
                   │
       [1] Encode Query (q ∈ ℝᵈ)
                   │
                   ▼
     ┌────────────────────────────┐
     │   Dense/Sparse Retriever   │ ◄── Access to large corpus D
     └────────────────────────────┘
                   │
     Top-k context docs: {d₁, d₂, ..., d_k}
                   │
     [2] Chunk + Format Context
                   │
                   ▼
     ┌────────────────────────────┐
     │    LLM Context Assembly    │
     │     Prompt = [Query + C]   │
     └────────────────────────────┘
                   │
     [3] Conditional Generation
                   ▼
     ┌────────────────────────────┐
     │  Language Model Inference  │
     │       (e.g., GPT, T5)      │
     └────────────────────────────┘
                   │
               Output y

```

### 1. **Query Embedding and Retrieval**

- The user submits a query $q \in \mathcal{Q}$
- The query is embedded into a dense vector space: $v_q = f_{\text{encoder}}(q)$
- Top-*k* documents $\{d_i\} \in \mathcal{D}$ are retrieved using a similarity function: $\text{sim}(v_q, v_{d_i}) = \cos(v_q, v_{d_i}) \quad \text{or} \quad \text{BM25}(q, d_i)$

### 2. **Context Construction / Context Injection**

- Retrieved documents are:
    - Chunked (e.g., by paragraph, windowed sliding window)
    - Cleaned and ranked
- These chunks are assembled into a **prompt**:   $\text{Prompt}(q, \{d_i\}) = [\texttt{CONTEXT: } d_1 \ldots d_k \ \texttt{QUERY: } q]$
- This context **must fit within the model’s token limit**, making RAG **context-aware but bounded**.

### 3. **LLM Inference**

- The generator $G$ conditions on the full prompt: $y = G(q, \{d_i\})$
- Output is generated via autoregressive decoding (GPT) or seq2seq decoding (T5/BART): $y = \arg\max_{y} P(y \mid q, \{d_i\})$

### 🔁 Enhancements

- **Reranker**: Applies deep re-ranking to retrieved results (e.g., cross-encoder).
- **Feedback Loop**: Collects human feedback for retrieval/generation quality.
- **Memory / History**: For chat, maintains long-term state using retrieval cache or vector memory.
- **Multi-hop**: Iteratively refines queries based on intermediate retrievals.

## RAG System Architecture

| Component | Implementation Examples |
| --- | --- |
| Retriever | FAISS, ElasticSearch, Milvus, BM25, DPR |
| Embedding | OpenAI, Cohere, SentenceTransformers |
| Generator | GPT-4, Claude, LLaMA, Mistral, T5, FLAN-T5 |
| Chunking | Recursive text splitter, overlap, semantic |
| Ranking (opt.) | Cross-encoders, rerankers (BGE, Cohere, etc.) |

## Embedding

> See more in [**Embedding**](https://app.notion.com/p/Embedding-f47ac9d5aa264a5e90408da8292d9671?pvs=21).
> 

> https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
> 

> **Embeddings** are vectors (lists of numbers) that represent text in a continuous, dense, and high-dimensional space where **semantically similar** texts are **close** together.
> 

For example:

- `"apple"` and `"banana"` → close in vector space (they're both fruits)
- `"apple"` and `"laptop"` → more distant (different meanings)

🧩 **How Embeddings Work in RAG**

1. **Embed the Documents (Offline Step):**
    - You use a model (e.g., OpenAI’s `text-embedding-3-small`) to turn all your documents or chunks into embeddings.
    - These vectors are stored in a **vector database** (e.g., FAISS, Weaviate, Pinecone).
2. **Embed the Query (At Runtime):**
    - When the user asks a question, the system generates an embedding for that query.
3. **Retrieve Matching Documents:**
    - The system compares the query embedding to the stored document embeddings using **cosine similarity** or **dot product**.
    - It retrieves the **top-k most relevant documents**.
4. **Generate the Answer:**
    - The retrieved documents are passed to a language model along with the query.
    - The model generates an answer using both the query and the retrieved context.

### Embedding Dimension

> What is the max length per document? or Token Limits?
> 

**What If Document Is Longer?**

If a document is longer than the model's token limit, you have a few options:

- **Chunking**: Break the document into smaller chunks (e.g., paragraphs or sliding windows).
- **Hierarchical Embedding**: Embed each chunk and then combine (e.g., average, weighted sum, or another model to compress).
- **Summarization + Embedding**: Summarize the document and then embed the summary.

## Uses

> 

| **Domain** | **Use Case** | **Description** | **Typical Data Sources** | **Key Benefits** |
| --- | --- | --- | --- | --- |
| **Enterprise Search** | Internal document QA | Answer employee queries from internal docs (HR, policies, manuals) | PDFs, DOCX, Confluence, SharePoint | Reduces support load, improves internal knowledge access |
| **Customer Support** | Chatbot with product manuals | Assist users with troubleshooting using documentation | Product manuals, support KBs, CRM logs | 24/7 self-service, higher resolution rate |
| **Healthcare** | Medical assistant for clinical support | Help doctors access guidelines or research for decision support | PubMed, UpToDate, clinical protocols | Reduces time-to-info, improves evidence-based care |
| **Legal** | Legal research assistant | Retrieve relevant statutes, precedents, contracts | Legal corpora, firm’s internal databases | Speeds up legal research, contextualizes law to cases |
| **Education** | Tutor using textbook + lecture material | Personalized tutoring using course-specific materials | Textbooks, lecture notes, slides | Adaptive learning, relevant explanations |
| **Research & Science** | Literature-based question answering | Aid researchers with up-to-date answers grounded in papers | ArXiv, PubMed, Springer, Elsevier | Accurate, citation-linked insights |
| **Finance** | Market intelligence assistant | Summarize and answer questions from reports or filings | SEC filings, earnings calls, analyst reports | Real-time synthesis of market data |
| **E-commerce** | Product comparison and Q&A | Retrieve specs, reviews, and policies to answer shopper questions | Product databases, user reviews, FAQs | Boosts conversion, reduces abandoned carts |
| **HR / Talent** | Resume + JD matching | Match applicants to roles based on resumes and job descriptions | CVs, job postings, internal competency models | Enhances hiring accuracy, reduces recruiter time |
| **Codebases** | Dev assistant over large code repos | Answer dev questions grounded in actual source code | GitHub repos, documentation, API refs | Boosts productivity, helps onboarding |
| **Cybersecurity** | Threat intelligence assistant | Summarize CVEs, threat reports, and detection logic | MITRE ATT&CK, CVE feeds, vendor advisories | Informs SOC teams rapidly, aids incident response |
| **Real Estate** | Property + regulation assistant | Summarize zoning laws and property features | Public records, zoning maps, listings | Aids buyer/seller decisions, saves analyst time |
| **Compliance** | Policy adherence assistant | Verify internal decisions against policy or regulation | Policy documents, audit trails, legal codes | Lowers risk, boosts process transparency |
| **Manufacturing** | Technical documentation assistant | Retrieve design specs, machine manuals, part instructions | CAD docs, blueprints, repair manuals | Reduces downtime, supports maintenance |

## Alternatives

| **Approach** | **Core Idea** | **Strengths** | **Limitations** | **Examples / Tools** |
| --- | --- | --- | --- | --- |
| **Fine-tuning / Instruction-tuning** | Embed knowledge into the model weights through training on curated datasets | High performance on known domains, low latency | Expensive, static knowledge | Alpaca, Dolly, BioMedLM |
| **Tool-augmented LLMs** | LLM calls external tools or APIs for tasks like search, math, DB query | Flexible, accurate for real-time tasks | Requires orchestration layer, complex to scale | Toolformer, ReAct, LangChain Agents |
| **External Memory (e.g., MemGPT)** | LLM interacts with structured memory systems that evolve over time | Stateful, supports long-term memory | Needs complex memory management logic | MemGPT, LangGraph |
| **Structured Prompting (Schema-Guided)** | Prompts with embedded schemas, graphs, or decision trees | Better controllability, more verifiable outputs | Limited generality | JSON schema prompts, Chain-of-Thought |
| **Knowledge Graph + LLM** | Use knowledge graphs for fact retrieval and validation | High accuracy, interpretable | Building and maintaining KG is labor-intensive | GraphRAG, KG-Augmented QA |
| **Database-Augmented Generation** | Query SQL/NoSQL databases via natural language | Precise over structured data | Needs schema alignment and secure DB access | Text-to-SQL, DataCopilot |
| **Program Synthesis + Execution** | LLM generates code/scripts to get the answer | High precision, interpretable | Vulnerable to code hallucination | OpenAI Code Interpreter, Gorilla |
| **Multi-hop Retrieval + Reasoning** | Decompose queries and retrieve evidence step by step | Good for complex questions | Prone to compounding errors | HotpotQA, Decompose-then-Retrieve |
| **Human-in-the-loop Systems** | Use LLMs with human validation or correction | Reliable outputs in critical domains | High latency and cost | Legal/Gov workflows, medical systems |
| **Distillation from RAG to Standalone** | Train a smaller model to mimic RAG responses | Lightweight at inference time | Lower adaptability to new contexts | RAG distillation papers |
| **Active Retrieval / Query Reformulation** | LLM dynamically improves queries for better retrieval | Higher-quality context selection | Needs sophisticated retriever integration | HyDE, IRCoT |
| **Multi-modal RAG** | Use image/audio/video embeddings as retrievable chunks | Broader applicability, richer context | Challenging vector store setup, cross-modal alignment | LLaVA-RAG, CLIP + RAG |

## Case Studies

> 
- [ ]  Internal Knowledge Search (Databricks, Klarna, Salesforce)
- [ ]  BloombergGPT + RAG Tools
- [ ]  Legal & Contract Analysis (Thomson Reuters, CaseText)
- [ ]  https://github.com/RUC-NLPIR/FlashRAG
- [ ]  https://arxiv.org/abs/2208.03299

## Limits & Challenges

> RAG extends access, not cognition.
> 
- **Context Window Limit**: The generator can only process a finite number of tokens (e.g., 4k–128k).
- **Chunking Heuristics**: Input documents must be split into semantically meaningful, size-constrained chunks.
- **Latency Bottlenecks**: Retrieval and generation introduce compound latency.
- **Retrieval Accuracy**: Irrelevant or low-quality chunks can degrade generation performance.

## QA

### How does the system inject the context into the generator? What format does it use? Does it use embeddings or just plain text chunks?

> In **Retrieval-Augmented Generation (RAG)**, the system injects context into the generator using **plain text chunks**, not embeddings.
> 

## References

- https://github.com/onyx-dot-app/onyx
- https://github.com/infiniflow/ragflow
- https://github.com/deepset-ai/haystack
- https://github.com/RUC-NLPIR/FlashRAG
- https://github.com/FareedKhan-dev/all-rag-techniques
- https://huggingface.co/docs/transformers/en/model_doc/rag
- https://en.wikipedia.org/wiki/LangChain
- [What is retrieval-augmented generation?](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)
- https://www.llamaindex.ai/
- https://www.reddit.com/r/LocalLLaMA/comments/173ant0/has_anyone_tried_rag_with_smaller_models/
- https://arxiv.org/abs/2005.11401v4
- https://arxiv.org/abs/2501.06713
- https://arxiv.org/abs/2501.09223
