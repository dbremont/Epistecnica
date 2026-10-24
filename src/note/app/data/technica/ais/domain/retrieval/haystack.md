---
tags: [tool]
---

# Haystack

 : LangChain (LangChain%20d86f5323e9e54e7fb972706f313cdb74.md), Retrieval-Augmented Generation (RAG) (Retrieval-Augmented%20Generation%20(RAG)%2013bc0f5171ec80e2bf8bfa0d05235b9a.md)

> The **Haystack LLM** Tool is a modular **NLP framework** that enables scalable, production-ready pipelines for question answering and **retrieval-augmented generation (RAG)** by orchestrating document stores, retrievers, and large language model inference nodes via a graph-based **Directed Acyclic Graph (DAG)** execution engine.
> 

## Use Cases

| **Use Case** | **Description** |
| --- | --- |
| **Open-Domain Question Answering** | Retrieve documents and extract precise answers to user queries |
| **Retrieval-Augmented Generation (RAG)** | Generate answers conditioned on retrieved documents |
| **Semantic Document Search** | Find documents relevant to a semantic query |
| **Multi-Hop Question Answering** | Answer questions requiring reasoning across multiple documents |
| **Document Summarization** | Summarize large collections or single documents |
| **Knowledge Base Construction** | Ingest, index, and query structured/unstructured knowledge |
| **Chatbot / Conversational AI** | Context-aware interactive QA with stateful conversation |
| **Fact Verification** | Validate facts by retrieving evidence and verifying statements |
| **Custom Domain Adaptation** | Fine-tune or evaluate retrievers/readers on domain-specific data |
| **Hybrid Search (Keyword + Semantic)** | Combine keyword and vector retrieval for improved recall |

## **Component**

- **Base abstraction** for all pipeline elements.
- Implements `run()` or `run_batch()` methods.
- Can be anything from a retriever, reader, generator, ranker, summarizer, etc.

## **Pipeline**

- **Execution graph** that connects components using a **Directed Acyclic Graph (DAG)**.
- Encapsulates the data flow and dependencies between components.
- Supports both **graph-based and linear pipelines**.

## **DocumentStore**

- Backend for storing and retrieving documents and metadata.
- Pluggable (e.g., Elasticsearch, FAISS, Weaviate, Pinecone, InMemory).
- Supports vector-based and keyword-based indexing.

## **Retriever**

- Component that **selects relevant documents** from the DocumentStore.
- Types: Sparse (e.g., BM25), Dense (e.g., DPR, SentenceTransformers), Hybrid.

## **Reader / Generator**

- **Reader**: Extractive model (e.g., BERT) that finds answer spans in documents.
- **Generator**: Generative model (e.g., OpenAI, FLAN-T5) that synthesizes answers using retrieved context.

## **Node**

- A specific instance of a Component placed in a Pipeline.
- Has input/output labels for DAG connections.

## **PromptNode / PromptTemplate**

- For LLM-based workflows.
- **PromptNode** wraps LLMs and manages prompt formatting, inference, and response parsing.
- **PromptTemplate** defines parameterized prompts and templates for dynamic query handling.

## **Answer / Document / Label**

- Structured data classes used internally to manage results:
    - **Answer**: model output with text, score, context.
    - **Document**: text and metadata retrieved from the store.
    - **Label**: for training and evaluation, stores ground truth.

## References

- https://github.com/eth-sri/lmql
- https://www.langchain.com/ - Alternative.
- https://haystack.deepset.ai/
