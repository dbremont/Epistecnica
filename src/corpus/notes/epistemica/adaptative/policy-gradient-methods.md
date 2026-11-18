---
tags: [note, reinforcement-learning, policy-gradient, optimization, adaptative]
qa:
 - Is the policy a function or a distribution — and what does the answer change about the update?
 - Why does the policy-gradient estimate need a baseline, and what does the baseline not fix?
 - TRPO and PPO both limit how far the policy moves. Is that a stability trick or a statement about trust?
---

# Policy Gradient Methods

> **Policy gradient methods** optimise the policy directly: they parameterise the policy as a differentiable distribution $\pi_\theta(a\mid s)$, measure the expected return of the behaviour it produces, and move the parameters along the gradient of that return. They are the family that optimises *what to do* rather than *how good a state is* — the policy, not the value.

> The reason to optimise the policy directly is that the value-based route has to convert values into actions, and that conversion is trivial only in small discrete action spaces. A policy can be a distribution over a continuous action, a network emitting the parameters of a Gaussian, or a language model emitting a token — and the gradient applies unchanged.

## The policy-gradient theorem

> For a policy $\pi_\theta$ and the objective
> $$J(\theta) = \mathbb{E}_{\tau\sim\pi_\theta}\left[\sum_{t=0}^{T}\gamma^t r_t\right],$$
> the gradient is
> $$\nabla_\theta J(\theta) = \mathbb{E}_{\tau}\left[\sum_{t} \nabla_\theta \log \pi_\theta(a_t\mid s_t)\, G_t\right],$$
> with $G_t$ the return from step $t$. The identity behind it is the log-derivative trick: $\nabla_\theta \pi_\theta = \pi_\theta \nabla_\theta \log \pi_\theta$, so the gradient of an expectation under the policy can be written as an expectation of a gradient under the same policy — a quantity that can be estimated from samples.

> The estimator is unbiased and usable: collect trajectories, compute returns, weight the log-probabilities by them, and step. It needs no model of the environment, and it needs no differentiability of the dynamics or the reward.

## REINFORCE

> The simplest instance: run the policy, compute the return of each trajectory, and update
> $$\theta \leftarrow \theta + \alpha \sum_t \nabla_\theta \log \pi_\theta(a_t\mid s_t)\, G_t.$$
> Actions followed by high returns become more likely; actions followed by low returns become less likely. It works, and it is very noisy: the return of a whole trajectory is one sample, and its variance grows with the horizon.

| Problem | Cause | Remedy |
| --- | --- | --- |
| **High variance** | One return per trajectory, noisy credit assignment | A baseline, an advantage, more samples |
| **Credit assignment** | The return is attributed to every action in the trajectory | Discounting, actor-critic, generalised advantage estimation |
| **Large step sizes** | The update moves the policy distribution far from where the data came from | Trust regions, clipping, KL penalties |
| **Sample inefficiency** | On-policy data is discarded after one update | Off-policy corrections, PPO's reuse, DPO for preferences |

## Baselines and advantages

> Subtract a baseline $b(s)$ from the return: the gradient is unchanged in expectation, because $b$ does not depend on the action, but the variance falls. The natural baseline is the value function $V^\phi(s)$; the result is the **advantage** $A_t = G_t - V^\phi(s_t)$, which asks whether the action was better than what was expected rather than whether the outcome was good in absolute terms.

> The actor-critic architecture follows: an **actor** (the policy) is updated by the policy gradient with an advantage, and a **critic** (the value function) is updated by a regression on returns or by a TD error. The critic is the learned baseline, and its accuracy sets how much of the gradient is signal.

## Trust regions: TRPO and PPO

> A policy-gradient step changes the distribution that generated the data, so a large step can collapse performance and cannot be recovered from with the data already collected. **TRPO** makes the constraint explicit: maximise the surrogate objective subject to a KL bound on how far the new policy may move from the old,
> $$\max_\theta\ \mathbb{E}\left[\frac{\pi_\theta(a\mid s)}{\pi_{\theta_{\text{old}}}(a\mid s)} A\right] \quad \text{s.t.}\quad \mathbb{E}\left[D_{\mathrm{KL}}(\pi_{\theta_{\text{old}}}\|\pi_\theta)\right] \le \delta.$$
> **PPO** replaces the constrained problem with a clipped surrogate,
> $$\mathcal{L}(\theta) = \mathbb{E}\left[\min\left(r_t(\theta)A_t,\ \operatorname{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)A_t\right)\right],$$
> which removes the incentive to move the ratio $r_t = \pi_\theta/\pi_{\theta_{\text{old}}}$ outside a band. It is cheaper than solving the constraint and has become the default in large-scale training, including RLHF.

> The trust region is not merely a trick for stability. It is a statement that the gradient estimate is valid only near the policy that produced the data — and the further the update moves, the less the estimate means.

## Deterministic and maximum-entropy variants

| Variant | Policy | Objective | Why |
| --- | --- | --- | --- |
| **DDPG** | Deterministic $a=\mu_\theta(s)$ | Expected return | Continuous actions without a distribution; a critic supplies the gradient |
| **TD3** | Deterministic, twin critics | Expected return | Reduces the overestimation that DDPG inherits from its critic |
| **SAC** | Stochastic | Return + entropy | The entropy term keeps exploration alive and makes the policy robust to a range of near-optimal actions |

> The entropy bonus in SAC is the maximum-entropy formulation: optimise $\mathbb{E}[r] + \alpha \mathcal{H}(\pi)$, so the policy prefers, among equally good actions, the one that keeps its options open. It is the same move the information-theoretic family makes, applied to the policy distribution itself.

## Where it sits

> Policy gradient is the optimisation machinery of the policy-based and actor-critic families in [Reinforcement Learning](/view.html?p=notes/epistemica/adaptative/reinforcement-learning-rl.md); its objective is the return defined on the [Markov Decision Process](/view.html?p=notes/epistemica/adaptative/markov-decision-processes-mdp.md); and it is the algorithm inside [RLHF](/view.html?p=notes/technica/cybernetics/synthesis/reinforcement-learning-with-human-feedback-rlhf.md), where the policy is a language model and the reward comes from a learned model of human preference.

## References

- [Policy gradient method](https://en.wikipedia.org/wiki/Policy_gradient_method)
- Sutton, R. S., McAllester, D., Singh, S., & Mansour, Y. (1999). Policy gradient methods for reinforcement learning with function approximation. *NeurIPS 12*. — the policy-gradient theorem with function approximation
- Williams, R. J. (1992). Simple statistical gradient-following algorithms for connectionist reinforcement learning. *Machine Learning*, 8, 229–256. — REINFORCE
- Schulman, J., Levine, S., Abbeel, P., Jordan, M., & Moritz, P. (2015). Trust region policy optimization. *ICML*. — TRPO
- Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). Proximal policy optimization algorithms. arXiv:1707.06347 — PPO
- Haarnoja, T., Zhou, A., Abbeel, P., & Levine, S. (2018). Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. *ICML*. — SAC
- [Reinforcement Learning](/view.html?p=notes/epistemica/adaptative/reinforcement-learning-rl.md) — the master note and the algorithm families
- [Markov Decision Process](/view.html?p=notes/epistemica/adaptative/markov-decision-processes-mdp.md) — the objective's formal setting
