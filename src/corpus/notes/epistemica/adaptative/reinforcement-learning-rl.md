---
tags: [note]
---

# Reinforcement Learning (RL)


> Reinforcement Learning (RL) is a typed of machine learning where an agent learns to make decisions by interacting with an environment to maximize cumulative rewards over time.
> 

> **Reinforcement learning** can be performed without explicit reward signals; however, this does not imply the absence of general evaluation metrics.
> 

## Structure

| **Component** | **Description** |
| --- | --- |
| **Agent** | The learner or decision-maker that interacts with the environment to achieve a goal. |
| **Environment** | The external system with which the agent interacts. It provides states and rewards to the agent. |
| **State (S)** | A representation of the current situation or configuration of the environment. |
| **Action (A)** | A decision or move taken by the agent that affects the environment. |
| **Reward (R)** | A feedback signal from the environment indicating the success or failure of an action. |
| **Policy (π)** | A strategy or rule that the agent uses to decide actions based on the current state. |
| **Value Function (V/Q)** | Estimates the expected cumulative reward from a state (V) or state-action pair (Q). |
| **Exploration vs Exploitation** | The trade-off between exploring new actions and exploiting known rewarding actions. |
| **Markov Decision Process (MDP)** | A mathematical framework for modeling decision-making in RL. |
| **Bellman Equation** | A recursive equation used to compute the **value function** in RL. |
| **Learning** | Methods used to train the agent, such as Q-Learning, Policy Gradients, or Deep Q-Networks (DQN). |
| **Model-Based vs. Model-Free** | Whether the agent learns a model of the environment or not. |
| **Exploration vs Exploitation** | The trade-off between trying new actions (exploration) and using known rewarding actions (exploitation). |

## Formulations

> 

| **Version** | **Description** |
| --- | --- |
| **Multi-Armed Bandit (MAB)** | A single-state problem where the agent chooses actions (arms) to maximize immediate rewards. |
| **Contextual Bandit** | Extends MAB by adding context (state) to each decision, but no state transitions. |
| **Markov Decision Process (MDP)** | A full RL problem with states, actions, rewards, and state transitions. |
| **Partially Observable MDP (POMDP)** | Extends MDP to cases where the agent cannot fully observe the state (partial observability). |
| **Inverse Reinforcement Learning (IRL)** | The agent learns the reward function by observing expert behavior. |
| **Hierarchical Reinforcement Learning (HRL)** | Breaks down the problem into sub-tasks or hierarchies for more efficient learning. |
| **Multi-Agent Reinforcement Learning (MARL)** | Extends RL to environments with multiple agents interacting and learning. |
| **General Reinforcement Learning (General RL)** | The most general form of RL, encompassing all possible environments and complexities. |

## How to reason about RL

> Reinforcement learning is a **control problem stated as an inference problem**: an agent chooses actions, the environment answers with a new state and a reward, and the agent updates the rule that chooses. Everything else — value functions, baselines, trust regions, entropy — is machinery for making that update stable and efficient.

The loop, once:

```text
state s_t ──▶ policy π(a | s) ──▶ action a_t ──▶ environment ──▶ reward r_t, state s_{t+1}
   ▲                                                                   │
   └───────────────────── update the policy ◀───────────────────────────┘
```

> The objective is the expected discounted return of the policy's own behaviour:
> $$J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}\left[\sum_{t=0}^{T} \gamma^t r_t\right],$$
> where $\tau$ is a trajectory sampled under the policy with parameters $\theta$. Two questions organise the whole field: **what is the policy** (a table, a network, a distribution, a deterministic map) and **how is it updated** (a gradient estimate, a Bellman backup, a population, a trust region). The families below are answers to the second question.

## Policy and Parameters

> Almost every modern RL algorithm fixes the policy's **structure** and learns only its **parameters**. The architecture is a design decision made before training — a network depth, a distribution family, a state representation — and the algorithm is the rule that moves the weights.

| Component | Fixed or learned? |
| --- | --- |
| **Policy architecture** (the computational blueprint) | Usually **fixed** |
| **Parameters** (weights, biases, embeddings) | **Learned** |
| **State and action representation** | Fixed by the problem formulation |
| **Reward function** | Fixed by the task (or learned in inverse RL) |
| **Exploration schedule and update rule** | Fixed hyperparameters, sometimes adapted |

> The distinction matters because it bounds what RL can do: RL cannot invent a representation or a reward, only fit the parameters of the one it is given. A change of architecture is a different problem, not a better-trained one.

## The Gradient Update

> For a stochastic policy $\pi_\theta(a\mid s)$, the policy-gradient theorem gives
> $$\nabla_\theta J(\theta) = \mathbb{E}_{\tau}\left[\sum_t \nabla_\theta \log \pi_\theta(a_t\mid s_t)\, G_t\right],$$
> where $G_t$ is the return from step $t$ (or an advantage estimate, or a critic's value). The log-derivative rewrites *how the objective changes* as *how the action probabilities change*, weighted by how good the outcome was — so the update is a weighted maximum-likelihood step on the actions the agent actually took.

> The estimate is unbiased and high-variance: one trajectory is one sample. Every practical variant is a variance reduction — a baseline, an advantage, a critic, a trust region, an entropy bonus — or a bias–variance trade made explicit.

## Algorithm Families

| Family | Primary objective | Trainable component | Optimisation signal | Update mechanism |
| --- | --- | --- | --- | --- |
| **REINFORCE** | Maximise expected cumulative reward | Policy | Monte Carlo returns | Policy gradient |
| **Actor-Critic (A2C/A3C)** | Maximise expected cumulative reward | Policy + value function | Advantage estimate | Policy gradient |
| **TRPO** | Maximise reward while limiting policy change | Policy | Advantage estimate | Trust-region optimisation |
| **PPO** | Maximise a clipped surrogate objective | Policy + value function | Advantage estimate | Clipped policy gradient |
| **DQN** | Learn the optimal action-value function | Q-network | Temporal-difference error | Gradient descent |
| **Double DQN** | Reduce Q-value overestimation | Q-network | TD error | Gradient descent |
| **DDPG** | Maximise expected return | Deterministic policy + critic | Deterministic policy gradient | Gradient descent |
| **TD3** | Improve deterministic policy learning | Policy + twin critics | TD error + deterministic gradient | Gradient descent |
| **SAC** | Maximise reward and policy entropy | Policy + critics | Entropy-regularised objective | Gradient descent |
| **Evolution Strategies** | Maximise fitness/reward | Policy parameters | Population fitness | Mutation + selection |

> The table reads in two directions. Down the **policy** column it separates what is learned: a policy, a value function, or both. Down the **signal** column it separates where the learning signal comes from: sampled returns, an advantage, a TD error, a population. The methods that follow — model-based, hierarchical, multi-agent, imitation — are combinations of these columns, not a fifth source of signal.

## Limits

> While Reinforcement Learning (RL) is powerful and gaining traction, especially for its high leverage through feedback over explicit supervision, it has key limitations. RL relies on sparse scalar signals at the end of long trajectories, which seems inefficient—especially as tasks grow in complexity and duration. Unlike humans, who reflect and extract multiple lessons per experience ("what went well, what didn’t, what to try next"), RL lacks a structured review mechanism that produces explicit guidance. A promising direction is to augment RL with meta-cognitive processes—e.g., using a language model to reflect on rollouts, extract textual "lessons," and update behavior accordingly. This mirrors human learning and could be more scalable and general than traditional reward-based RL. Such mechanisms may be uniquely suited to LLMs and represent new learning paradigms beyond current game/robotics-focused RL.
> 

## References

- [Policy Gradient Methods](/view.html?p=notes/epistemica/adaptative/policy-gradient-methods.md) — the gradient machinery behind the policy-based families
- [Markov Decision Processes (MDP)](/view.html?p=notes/epistemica/adaptative/markov-decision-processes-mdp.md) — the formal object the loop samples
- [Optimal Control](/view.html?p=notes/epistemica/adaptative/optimal-control-theory.md) · [Model Predictive Control](/view.html?p=notes/epistemica/adaptative/model-predictive-control-mpc.md) — the control-theory reading of the same problem
- [Active Inference](/view.html?p=notes/epistemica/adaptative/active-inference.md) — the Bayesian statement of the objective
- [RLHF](/view.html?p=notes/technica/cybernetics/synthesis/reinforcement-learning-with-human-feedback-rlhf.md) — the LLM post-training application
- https://en.wikipedia.org/wiki/Reinforcement_learning
- [General Reinforcement Learning in the Browser](https://github.com/aslanides/aixijs)
- [Introduction to Reinforcement Learning](https://www.youtube.com/watch?v=xMZE-9WECQE)
    - [Colab](https://colab.research.google.com/github/psc-g/intro_to_rl/blob/master/Introduction_to_reinforcement_learning.ipynb)
- https://lilianweng.github.io/posts/2018-02-19-rl-overview/
- https://en.wikipedia.org/wiki/Reinforcement_learning
- [https://news.ycombinator.com/item?id=43269330](https://news.ycombinator.com/item?id=43269330)
- https://arxiv.org/abs/2110.06394
- [https://proceedings.mlr.press/v119/jin20d/jin20d.pdf](https://proceedings.mlr.press/v119/jin20d/jin20d.pdf)  Reward-Free Exploration for Reinforcement Learning.
