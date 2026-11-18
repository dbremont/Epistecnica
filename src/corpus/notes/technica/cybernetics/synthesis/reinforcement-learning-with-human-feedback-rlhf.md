---
tags: [note, training, reinforcement-learning, rlhf, llm, post-training]
qa:
 - Is RLHF teaching the model something new or selecting behaviour the base model already contains?
 - What is the maximum a post-training stage can add — and is there a cap at all?
 - Why is a KL penalty to the reference model part of the objective rather than a regulariser?
---

# Reinforcement Learning with Human Feedback (RLHF)

> **RLHF** trains a language model against a reward signal learned from human preferences: the model generates responses, people (or a model standing in for them) rank the responses, a reward model is fitted to those rankings, and the language model is optimised — usually with a policy-gradient method — to produce responses the reward model scores highly.

> The technical core is borrowed directly from [Reinforcement Learning](/view.html?p=notes/epistemica/adaptative/reinforcement-learning-rl.md): the policy is the language model, the action is a token, the trajectory is a response, and the reward is a scalar that arrives at the end. What is new is the reward — not a game score or a control objective, but a learned model of what people prefer.

## The pipeline

| Stage | What is trained | Signal | What it fixes |
| --- | --- | --- | --- |
| **Pretraining** | The base model | Next-token prediction on a corpus | Capability and the latent behaviours everything later selects from |
| **Supervised fine-tuning** | The model | Human-written demonstrations | The response format and the instruction-following prior |
| **Reward modelling** | A separate reward model | Pairwise human preferences | A scalar that stands for "better" — usually a Bradley–Terry fit on comparisons |
| **RL fine-tuning** | The policy (the model) | Reward-model score, with a KL penalty | Behaviour that scores well without drifting from the reference |

> The KL term is not decoration. Without it the policy optimises the reward model, and the reward model is an imperfect proxy: the policy finds the inputs that fool it. The objective is
> $$\mathbb{E}_{x,\,y\sim\pi_\theta}\left[r_\phi(x,y) - \beta\, D_{\mathrm{KL}}\left(\pi_\theta(y\mid x)\,\|\,\pi_{\text{ref}}(y\mid x)\right)\right],$$
> where $r_\phi$ is the reward model and $\pi_{\text{ref}}$ the frozen reference. The penalty keeps the model near the distribution the reward model was trained to judge, and $\beta$ sets how much reward is worth how much drift.

## The algorithm choices

| Method | How it learns from preferences | Data | Character |
| --- | --- | --- | --- |
| **PPO** | Policy gradient with a clipped ratio, reward from the reward model, KL to the reference | On-policy rollouts | The classical RLHF workhorse; stable, expensive, many moving parts |
| **DPO** | A closed-form objective on preference pairs, no reward model and no rollouts | Offline preference pairs | Cheaper and simpler; the implicit reward is what the policy itself implies |
| **RLAIF** | The same pipeline with a model as the labeller | AI preferences | Scales the labelling; inherits the labeller's biases |
| **RLVR** | Reward from a verifier that can check the answer — tests, proofs, exact match | Rollouts against a checker | The reasoning-model route, where the reward is objective but only for checkable tasks |

> The RL method is a policy-gradient method: PPO is the clipped surrogate described in [Policy Gradient Methods](/view.html?p=notes/epistemica/adaptative/policy-gradient-methods.md), with the language model as the stochastic policy. DPO removes the RL loop entirely by differentiating through the preference likelihood, which is why it is attractive when rollouts are the cost.

## The policy and its fixed structure

> The same framing as in RL applies, and it is the key to the limits. The **architecture** of the model — its layers, its tokenizer, its attention pattern — is fixed before post-training; post-training learns **parameters** (and sometimes a small adapter). So RLHF can select, sharpen and re-weight behaviours the base model can already represent, but it cannot add a capability the architecture and the pretraining distribution do not support.

| Component | Fixed or learned in RLHF? |
| --- | --- |
| Base architecture and tokenizer | Fixed |
| Pretrained weights | Usually frozen or lightly updated |
| Policy parameters (full or LoRA) | Learned |
| Reward model | Learned separately, then frozen |
| KL coefficient and sampling temperature | Fixed hyperparameters |

## What post-training can add — and the cap question

> There is no agreed maximum, and any single number should be treated as a conjecture. The useful way to state the question is in terms of what the reward can measure and what the base model can express.

| Candidate limit | Mechanism | What it predicts |
| --- | --- | --- |
| **Reward hacking / Goodhart** | The policy optimises the proxy, not the preference | Gains plateau or reverse as the reward model is over-optimised; the KL coefficient is the brake |
| **Reward-model coverage** | The reward model is trained on a finite comparison set | Improvements outside that distribution are not reliably rewarded |
| **Verifier coverage** | RLVR rewards only checkable answers | Strong gains on maths and code, weak transfer to open-ended tasks |
| **Entropy collapse** | The policy concentrates on high-reward modes | Diversity falls; the model becomes brittle and repetitive |
| **Base-model capability** | The behaviour must be representable in the pretrained weights | RL elicits and sharpens; it rarely creates a capability the model could not express |
| **Data and compute** | RL gains scale with rollouts and reward-model quality | Diminishing returns, with a scaling behaviour that differs from pretraining |

> The empirical debate is between two readings. One says post-training is mostly **elicitation**: the base model already contains the behaviour, and RL selects it — which predicts a ceiling set by the base model and the reward's coverage. The other says post-training is **capability formation**: long RL on verifiable tasks teaches new reasoning strategies, which predicts gains that continue with compute. The reasoning models are the test case, and the evidence so far supports both readings on different tasks. A survey of the scaling evidence is [Wolfe's *RL scaling laws*](https://cameronrwolfe.substack.com/p/rl-scaling-laws); the honest summary is that the cap is task-dependent, not a constant.

> What the field agrees on is the shape: gains are largest where the reward is objective (a verifier), the task is within the base model's reach, and the KL budget is tuned; they shrink where the reward is a learned proxy of a subjective preference, which is exactly where Goodhart lives.

## References

- [Reinforcement Learning](/view.html?p=notes/epistemica/adaptative/reinforcement-learning-rl.md) — the master note and the algorithm families
- [Policy Gradient Methods](/view.html?p=notes/epistemica/adaptative/policy-gradient-methods.md) — PPO, the algorithm inside the classical pipeline
- [LLM System Modelling](/view.html?p=notes/technica/cybernetics/theory/llm-system-modelling.md) — the model the post-training stage modifies
- Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS 35*. — InstructGPT, the canonical RLHF pipeline
- Christiano, P., et al. (2017). Deep reinforcement learning from human preferences. *NeurIPS 30*. — the preference-reward method
- Rafailov, R., et al. (2023). Direct preference optimization: Your language model is secretly a reward model. *NeurIPS 36*. — DPO
- [Wolfe, C. R. — RL scaling laws](https://cameronrwolfe.substack.com/p/rl-scaling-laws) — the scaling evidence and the open cap question
- [RLHF from scratch](https://github.com/ashworks1706/rlhf-from-scratch) — an implementation walk-through
