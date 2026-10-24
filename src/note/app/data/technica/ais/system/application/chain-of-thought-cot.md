---
tags: [inference]
---

# Chain-of-thought (CoT)

 : Attention (Attention%2018ac0f5171ec80e7a4d4ea0eaf61508d.md)

> How to even think - or frame ‘Chain-of-thought (CoT)’? What type of element is it? It is a technique? It is a class of techniques?
> 

> Why chain of though even works? - An explanation of this can be recasted in terms of the context? How the context affects the next token?
> 

## Technique Set

> Which are the specific CoT techniques? Which underlies their implementation?
> 

| **Technique** | **Description** | **Implementation** |
| --- | --- | --- |
| Standard CoT | Generate intermediate reasoning before answering | Prompt model to produce step-by-step reasoning |
| Zero-Shot CoT | Elicit reasoning without examples | Add phrases such as "Think step by step" |
| Few-Shot CoT | Teach reasoning through examples | Provide worked reasoning examples in the prompt |
| Auto-CoT | Automatically generate CoT exemplars | Generate and reuse reasoning examples |
| Least-to-Most Prompting | Solve simple subproblems before harder ones | Break task into ordered subproblems |
| Plan-and-Solve | Create a plan before reasoning | Generate plan → execute plan |
| Skeleton-of-Thought | Create high-level outline first | Generate skeleton → expand sections |
| Self-Consistency | Generate multiple reasoning chains and aggregate | Sample multiple CoTs and choose majority answer |
| Tree of Thoughts (ToT) | Explore multiple reasoning branches as a tree | Generate candidate thoughts, score them, expand promising nodes |
| Graph of Thoughts (GoT) | Explore and connect reasoning states as a graph | Reuse and merge reasoning states across paths |
| Program of Thoughts (PoT) | Use executable code as reasoning medium | Generate code fragments and execute them |
| ReAct | Interleave reasoning and actions | Thought → Action → Observation cycles |
| Reflexion | Critique and improve previous reasoning | Generate answer → critique → revise |
| Verification-Based CoT | Explicitly verify reasoning steps | Generate solution then verify it |
| Debate / Multi-Agent CoT | Multiple agents reason and critique each other | Independent chains followed by comparison |
| Selection-Inference (STaR-like methods) | Learn from successful reasoning traces | Keep successful traces and retrain/use them |
| Monte Carlo Tree Search CoT | Search over reasoning paths using MCTS | Rollouts, scoring, backpropagation of rewards |
| Retrieval-Augmented CoT | Inject external knowledge into reasoning | Retrieve documents during reasoning |
| Tool-Augmented CoT | Use external systems during reasoning | Call calculators, databases, APIs, solvers |

## Reasoning Strategy

```jsx
Reasoning Strategy
│
└── Explicit Intermediate Reasoning
        │
        ├── Chain-of-Thought Prompting
        ├── Least-to-Most Prompting
        ├── Tree of Thoughts
        ├── Graph of Thoughts
        ├── Program of Thoughts
        └── Self-Consistency
```

## References

- https://github.com/Timothyxxx/Chain-of-ThoughtsPapers
- https://arxiv.org/abs/2201.11903
