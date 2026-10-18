# Dynamical Intelligence

> Dynamical intelligence is the capacity of a system to sustain its viability over time by adaptively regulating its state through feedback-driven perception, action, and learning within a dynamic environment.
> 

## Formulation

> A **dynamical intelligence** is a system $S$ characterized by:
> 

**State Space**

- A set of internal states $X \subseteq \mathbb{R}^n$.
- The system evolves over time according to dynamics: $\dot x(t) = f\!\bigl(x(t), u(t), e(t)\bigr)$  where $x(t)\in X$, $u(t)$ are actions, and $e(t)$ are environmental inputs.

**Perception (Information Flow)**

- A mapping from environment to internal states: $y(t) = h\!\bigl(x(t), e(t)\bigr)$ giving the system partial, noisy, or uncertain information about the environment.

**Action (Regulation)**

- A policy or control law that selects actions based on states, observations, or beliefs: $u(t) = \pi\!\bigl(x(t), y(t)\bigr)$

**Objective (Criterion)**

- The system has an implicit or explicit function it tries to minimize or maximize, e.g.:
    - **Control Theory:** stability, error minimization.
    - **Active Inference:** free-energy minimization.
    - **Reinforcement Learning:** expected cumulative reward.
    - **Biological Systems:** viability, survival, reproduction.
- Abstractly: $J = \int_0^\infty L\!\bigl(x(t), u(t), e(t)\bigr)\,dt$ where $L$ encodes costs, rewards, or divergences from expectations.
- $L$ encodes the local rate at which the system gains or loses alignment with its objective, given its state, action, and environment at that moment.

**Adaptation (Learning/Updating)**

- The system modifies parameters $\theta$ of $f, h, \pi$ over time, in response to feedback, to maintain or improve performance: $\theta_{t+1} = \mathcal{U}\!\bigl(\theta_t, x(t), y(t), u(t), e(t)\bigr)$

This update law  $\mathcal{U}$ can be Bayesian (belief updating), gradient-based (RL, control), evolutionary (population dynamics), or heuristic.

**Closure (Self-Maintenance)**

- The system must preserve its operational coherence over time, i.e. remain *viable*.
- Formally: $x(t)\in V\subseteq X \quad \forall t$ where $V$ is a viability kernel — the set of states from which survival/regulation is possible.

# Framework

| Framework | **Description** |
| --- | --- |
| **Cybernetics** | Studies how systems regulate themselves and their environment through feedback loops, focusing on control, communication, and adaptation in both machines and organisms. |
| **Control Theory** | Designs controllers using mathematical models to regulate system behavior and achieve goals like stability, robustness, and optimality. |
| **Active Inference** | A Bayesian framework where agents minimize prediction errors (or free energy) by adjusting beliefs and taking actions that align with sensory inputs. |
| **Reinforcement Learning** | An agent learns by interacting with its environment, receiving rewards or penalties, and maximizing long-term cumulative reward. |
| **Predictive Processing** | A cognitive framework proposing that perception and action are driven by hierarchical prediction-error minimization, closely related to active inference. |
| **Adaptive Control** | A branch of control theory where controllers adjust their parameters dynamically to handle uncertainty and time-varying conditions. |
| **Systems Dynamics** | Models feedback, delays, and nonlinear interactions in complex systems to understand emergent behaviors over time. |
| **Evolutionary Game Theory** | Studies how strategies evolve dynamically in populations under competitive and cooperative pressures, using fitness landscapes and replicator dynamics. |
| **Neural Dynamics** | Investigates how neural systems evolve over time, modeling intelligence as emergent from attractor states, oscillations, and network dynamics. |
| **Swarm Intelligence** | Explains collective intelligence in decentralized multi-agent systems (ants, birds, robots) through local interaction rules that create emergent global behavior. |
| **Distributed Adaptive Systems** | Multi-agent frameworks where agents adapt to environmental feedback and to each other in order to achieve robustness and resilience. |
| **Reservoir Computing** | A neural computation framework that leverages the transient dynamics of high-dimensional systems (e.g., recurrent neural networks, physical substrates) for processing temporal data. |
| **Dynamical Systems Approach to Cognition** | Treats cognition not as symbolic computation but as trajectories in a continuous state space, emphasizing embodiment and real-time interaction. |
| **Viable System Model (VSM)** | A cybernetic organizational framework describing how complex systems remain viable through recursive regulation and adaptation. |

Conceptual Model: Dynamical Intelligence

## References

- [Control Theory](https://www.wikiwand.com/en/Control_theory)
- [Adaptive Control](https://www.wikiwand.com/en/Adaptive_control)
- [Reinformcement Learning and Optimal Control](http://web.mit.edu/dimitrib/www/RLbook.html)
- [Visualizing and Understanding Atari Agents](https://greydanus.github.io/2017/11/01/visualize-atari/)
- [System Identification](https://www.wikiwand.com/en/System_identification)
- Andreas et al. Translating Neuralese. ACL 2017.
- On the interaction between supervision and self-play in emergent communication. ICLR 2020.
- Bahdanau et al. Learning to Understand Goal Specifications by Modelling Reward. ICLR 2019.
- Fu et al. From Language to Goals: Inverse Reinforcement Learning for Vision-Based Instruction Following. ICLR 2019.
- Wang et al. No Metrics Are Perfect: Adversarial Reward Learning for Visual Storytelling. ACL 2018.
- Wang et al. Video Captioning via Hierarchical Reinforcement Learning. CVPR 2018.
- Misra et al. Mapping Instructions and Visual Observations to Actions with Reinforcement Learning. EMNLP 2017.
- Buck et al. Ask the Right Questions: Active Question Reformulation with Reinforcement Learning. ICLR 2018
- S.R.K. Branavan, H. Chen, L. Zettlemoyer and R. Barzilay. Reinforcement Learning for Mapping Instructions to Actions. ACL 2009.
- Karthik Narasimhan, Adam Yala, Regina Barzilay. Improving Information Extraction by Acquiring External Evidence with Reinforcement Learning. EMNLP 2016.
- End-to-End Reinforcement Learning of Dialogue Agents for Information Access. arXiv:1609.00777.
- Text-based Games using Deep Reinforcement Learning. EMNLP2015.
- Jason D. Williams, Geoffrey Zweig. End-to-end LSTM-based dialog control optimized with supervised and reinforcement learning. arXiv:1606.01269.
- Jason D. Williams, Kavosh Asadi, Geoffrey Zweig. Hybrid Code Networks: practical and efficient end-to-end dialog control with supervised and reinforcement learning ACL 2017.
- Branavan, Kushman, Lei, and Barzilay. Learning High-Level Planning from Text. ACL 2012. [pdf]
- [Control Theory](https://en.wikipedia.org/wiki/Control_theory)
- PID Without a PhD (2016) [pdf] ([wescottdesign.com](http://wescottdesign.com/))
[https://news.ycombinator.com/item?id=39506420](https://news.ycombinator.com/item?id=39506420)
- Algorithmic Foundations of Interactive Learning **-** [https://interactive-learning-algos.github.io/](https://interactive-learning-algos.github.io/)
- Watkins, C. J., & Dayan, P. (1992). Q-learning. *Machine Learning*, *8*(3–4), 279–292.
- [**System Identification**](computational-science/system-identification.md)
