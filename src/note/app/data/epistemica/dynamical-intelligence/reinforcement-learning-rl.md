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

## **Learning**

> 

| **Category** | **Algorithm** | **Description** |
| --- | --- | --- |
| **Value-Based** | Q-Learning | Learns Q-values using Bellman updates and a max over future actions. |
|  | SARSA | Learns Q-values using the actual next action taken (on-policy variant). |
|  | DQN | Uses deep neural networks to approximate Q-values in discrete action spaces. |
| **Policy-Based** | REINFORCE | Monte Carlo policy gradient method that updates policy based on return. |
|  | PPO | Uses clipped objective to improve training stability in policy gradient. |
|  | TRPO | Trust region optimization of policies to ensure stable updates. |
| **Actor-Critic** | A2C (Advantage Actor-Critic) | Learns both a policy (actor) and value function (critic) synchronously. |
|  | A3C (Asynchronous A2C) | Parallel agents update global policy asynchronously to stabilize training. |
|  | DDPG | Off-policy actor-critic for continuous actions using deterministic policies. |
|  | SAC | Stochastic off-policy actor-critic maximizing both reward and entropy. |
|  | TD3 | Twin critics and delayed policy updates to reduce overestimation in DDPG. |
| **Model-Based** | Dyna-Q | Integrates planning, acting, and learning using a learned model. |
| (Planning/Learning) | MBPO | Uses model rollouts in model-based policy optimization. |
|  | PETS | Probabilistic ensemble models with trajectory sampling for planning. |
|  | MuZero | Learns dynamics, value, and policy functions directly from raw observations. |
| **Model-Free** | Q-Learning, PPO, DDPG | Learns optimal behavior directly from experience without modeling environment. |
| **On-Policy** | SARSA, PPO, A2C | Learns using samples from the current policy (data policy = behavior policy). |
| **Off-Policy** | Q-Learning, DQN, DDPG, SAC | Learns from data collected under a different policy (e.g., replay buffer). |
| **Deterministic Policy** | DDPG, TD3 | Outputs a single action per state; useful for continuous control tasks. |
| **Stochastic Policy** | PPO, REINFORCE, SAC | Outputs a distribution over actions; supports exploration naturally. |
| **Discrete Action Space** | Q-Learning, DQN, PPO | Designed for tasks with a finite set of actions (e.g., game moves). |
| **Continuous Action Space** | DDPG, SAC, TD3 | Operates in high-dimensional continuous control environments (e.g., robotics). |
| **Evolutionary Methods** | Genetic Algorithms | Uses mutation, crossover, and selection to evolve policies. |
|  | NES (Natural Evolution Strategies) | Gradient-based black-box optimization using evolution. |
|  | CMA-ES | Covariance matrix adaptation evolution strategy for policy search. |
| **Hierarchical RL** | Options Framework | Temporal abstraction via macro-actions (options). |
|  | FeUdal Networks | Hierarchical architecture where high-level managers direct low-level workers. |
| **Multi-Agent RL** | MADDPG | Multi-agent version of DDPG with centralized training and decentralized exec. |
|  | QMIX | Decomposes joint Q-values into individual agent utilities. |
|  | COMA | Counterfactual baseline for actor-critic in multi-agent settings. |
| **Imitation / Inverse RL** | IRL (Inverse RL) | Infers reward function from expert demonstrations. |
|  | GAIL | Uses adversarial training to learn policies from expert behavior. |
|  | Behavioral Cloning | Supervised learning of actions directly from expert trajectories. |
|  |  |  |
| **Reward-Free** | Pure exploration, Intrinsic motivation and Imitation. |  |

## Limits

> While Reinforcement Learning (RL) is powerful and gaining traction, especially for its high leverage through feedback over explicit supervision, it has key limitations. RL relies on sparse scalar signals at the end of long trajectories, which seems inefficient—especially as tasks grow in complexity and duration. Unlike humans, who reflect and extract multiple lessons per experience ("what went well, what didn’t, what to try next"), RL lacks a structured review mechanism that produces explicit guidance. A promising direction is to augment RL with meta-cognitive processes—e.g., using a language model to reflect on rollouts, extract textual "lessons," and update behavior accordingly. This mirrors human learning and could be more scalable and general than traditional reward-based RL. Such mechanisms may be uniquely suited to LLMs and represent new learning paradigms beyond current game/robotics-focused RL.
> 

## References

- https://en.wikipedia.org/wiki/Reinforcement_learning
- [General Reinforcement Learning in the Browser](https://github.com/aslanides/aixijs)
- [Introduction to Reinforcement Learning](https://www.youtube.com/watch?v=xMZE-9WECQE)
    - [Colab](https://colab.research.google.com/github/psc-g/intro_to_rl/blob/master/Introduction_to_reinforcement_learning.ipynb)
- https://lilianweng.github.io/posts/2018-02-19-rl-overview/
- https://en.wikipedia.org/wiki/Reinforcement_learning
- [https://news.ycombinator.com/item?id=43269330](https://news.ycombinator.com/item?id=43269330)
- https://arxiv.org/abs/2110.06394
- [https://proceedings.mlr.press/v119/jin20d/jin20d.pdf](https://proceedings.mlr.press/v119/jin20d/jin20d.pdf)  Reward-Free Exploration for Reinforcement Learning.
