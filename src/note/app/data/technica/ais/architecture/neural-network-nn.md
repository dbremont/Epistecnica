---
tags: [learning-system]
---

# Neural Network (NN)


> In this note, we explore a **family** of trainable computational systems, commonly known as neural networks.
> 

> A **neural network** is a computational model inspired by biological neurons, designed to approximate complex functions by learning from data.
> 

When study a $n$ ask yourself:

- What is the structure of the network, and how do its components enable the underlying dynamics that generate meaningful trajectories of representation evolution?
- What types of meaningful inference dynamics can be instantiated by an $X$?
- How many types of states, and memories does this network used in computation?
- How  it this task formulated? (In LLM is next token prediction, etc)

QA:

- What do we mean by representation space?   Zhou, Yufa, et al. "The geometry of reasoning: Flowing logics in representation space." arXiv preprint arXiv:2510.09782 (2025).
- How to think about neural nets?
- What is the nature of the nodes in a nn? What are the types of nodes? Which are the types of models of pieces of structure in a nn?
- How to reason about component connection in NN? As  flow direction or what?
- How to think about optimization? How to think about the dynamics of optimization? Which are the associated areas of research?
- What do we mean by generalization?
- Why certain ‘tasks’ required multiple layer? - See detecting simmetry …
- How to think  deeply about representation?
    - https://arxiv.org/abs/2410.03006
- Connections are the microstructure of a learned function.
    - What is the macro-structure? What does it represents?
- Representation:
    - Neurons does not represents.
    - The entire thing represent thought it’s dynamics.
    - **Downstream** connections interpret it
    - **Previous** connections shape it.
    - **Representation** occurs through action.
- How does training a neural network on multiple tasks affect generalization and other properties such as robustness, representation structure?
    - May tasks in represented by one network - do requires compression that induces abstraction.
- Learning which representations exist (how the tasks are performed) is the main question of mechanistic interpretability.
- What is the impact of weight initialization in training(learning)?
- How to think abut (Homologous Shared Representation (HSR), **Compatible Inter-Layer Representation, Layer-Agnostic Representation**) - or the - internal language of Transformers?

## Meta

> Evaluation Framework.
> 

### **✅** Evaluation

> What is my **epistemic assessment** of this topic? How well do I understand this subject?
> 

> See more in [](https://app.notion.com/p/1cfc0f5171ec80a1ad0ee6cc17ade968?pvs=21) & [](https://app.notion.com/p/250c0f5171ec8010a8d3caa5d0a1266e?pvs=21)
> 

| **Meta-Dimension** | **Note** |
| --- | --- |
| **Note Quality** | … |
| **Completeness** | … |
| **Coherence & Structure** | … |
| **Epistemic Self-Assessment** | … |
| **Should I Reorganize This -in My Content Forest?** |  |
| **What’s my study Strategy? Should I Change It?** |  |

### **🌌** Signature

> A comprehensive list of aspects to cover in order to understand a topic.
> 

> **TCSEE** (**Trainable** **Computational System** → **Evolution** ←→  **Evaluation**): **Random Untrained Template** → Train System.
> 

| Aspect | Description |
| --- | --- |
| **Nucleus (Deepest Essence) 🧬** | What is the deepest essence? |
| **Evidentia (Evidence) 📊** | What proofs, data, or logical arguments support it? How can its claims or performance be verified? |
| **Telos (Intent) 🎯** | What is it for? Toward what end is it directed? What tools does it offer, if any? What outcomes does it aim to achieve? |
| **Gnosis (Understanding) 🧠** | How to grow a **mental represented** (compress, fluid,  hierarchical (depth, abstraction), meta-awareness, flexibility, minimal sensitivity, well-connected) that capture this topic both its declarative aspects and procedural aspects?  How can we develop an **explicit representation & organization** of this topic that supports the growth of a strong **mental representation**? What **previous structure**  must be in place in order to make the growth of the new representation feasible? |
| **Epignosis (Application) 🛠️** | How is this knowledge applied in practice? What advanced skills or insights emerge from mastery? What real-world problems does it solve? |
| **Relatio (Connections) 🔗** | How does this topic relate to other subjects or fields? What are the interdisciplinary connections? |
| **Idoneitas (Suitability) 📐** | How effectively does it achieve its purpose? What metrics prove its value? |
| **Limites (Limits) ⛔** | What are its boundaries? What constraints define its operation? |
| **Contextus (Context) 🌍** | What is the historical, cultural, or situational context in which this study occurs? |
| **Dynamis (Evolution) 🌱** | How might it transform? What emerging influences could redefine it? |
| **Critica (Critique) 🔍** | What are the common criticisms or challenges associated with this topic? How have these been addressed or debated? |
| **Verbum Usus (Language Use) 🗣️** | How is the word/concept used in language and discourse? What are the typical semantic, pragmatic, and stylistic patterns surrounding its use? How do people’s usage contexts, connotations, and variations influence understanding? What shifts or trends in language use reflect its evolving meaning or social significance? |

### 🧠 Mental Representation

> How should we think about $x$?
> 

> See more in [How do different **mental representations** of the same RepTarget impact performance?](https://app.notion.com/p/How-do-different-mental-representations-of-the-same-RepTarget-impact-performance-24ac0f5171ec80dbaea5cc0e93f7647e?pvs=21).
> 

## Formulation

> How to characterize a **Neural Net (Training and Inference)**?
> 

| **Category** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Phenomena** | Observable behaviors or emergent effects produced by the network during training or inference. They arise from interactions among architecture, optimization, and data rather than being explicitly programmed. | generalization, memorization, grokking, in-context learning, emergence of capabilities with scale, feature superposition, polysemantic neurons, monosemantic neurons, attention head specialization (induction heads, copy heads, name-mover heads), circuit formation, representation collapse, representation disentanglement, mode collapse (GANs), catastrophic forgetting, interference between tasks, shortcut learning / spurious correlation learning, double descent, lottery ticket phenomenon, phase transitions during training, implicit bias of gradient descent, neural scaling law emergence, prompt sensitivity, hallucination (LLMs), representation drift during training, neural collapse (classification networks), sparsity emergence, specialization of layers, compositional reasoning emergence, algorithmic behavior emergence (sorting, copying, addition circuits), calibration drift, distribution shift sensitivity |
| **Structure** | The static formal organization of the computational system specifying how computations are arranged and connected. | computational graph, feedforward layers, fully connected layers, convolutional layers, pooling layers (max/avg), normalization layers (BatchNorm, LayerNorm, RMSNorm), residual connections, skip connections, attention blocks, multi-head attention modules, feedforward (MLP) blocks, embedding layers, positional encoding modules (sinusoidal, learned), encoder stacks, decoder stacks, cross-attention modules, recurrent cells (RNN, LSTM, GRU), gating mechanisms, mixture-of-experts routing layers, expert subnetworks, routing networks, diffusion U-Net architectures, upsampling/downsampling blocks, adapter modules, LoRA adapters, classifier heads, projection heads, tokenizers and vocabulary structures |
| **Parameter** | Trainable numerical degrees of freedom that determine the model’s mapping from inputs to outputs. | weight matrices, bias vectors, embedding matrices, token embedding vectors, positional embeddings, attention projection matrices $(W_Q, W_K, W_V, W_O)$, feedforward network weights $(W_1, W_2)$, convolution kernels / filters, recurrent weight matrices $(W_{hh}, W_{xh})$, LSTM gate parameters (input/forget/output gates), GRU gate parameters, mixture-of-experts expert weights, routing network parameters, normalization parameters $(\gamma, \beta)$, adapter weights, LoRA low-rank matrices, diffusion model noise prediction parameters, classifier head weights |
| **State** | Internal values that exist during computation and evolve as the network processes inputs (ephemeral or persistent during inference). | neuron activations, intermediate layer activations, hidden states (RNN), cell state (LSTM), gating activations, token embeddings during inference, residual stream vectors (transformers), feature maps (CNNs), attention score matrices, attention probability distributions, key/value attention caches (autoregressive inference), logits before softmax, output probability distributions, routing decisions (MoE), diffusion latent states, denoising intermediate states, gradient tensors (during training), optimizer internal states (momentum vectors, Adam first/second moments), batch normalization running statistics |
| **Dynamics** | Processes through which states evolve and parameters change during training or inference. | forward propagation, backpropagation, gradient computation via chain rule, stochastic gradient descent (SGD), Adam/RMSProp/Adagrad optimization dynamics, learning rate scheduling, weight decay regularization, dropout stochastic masking, gradient clipping, gradient accumulation, vanishing gradients, exploding gradients, gradient noise effects, saddle-point stagnation, loss landscape traversal, curriculum learning dynamics, teacher forcing in sequence models, diffusion denoising steps, autoregressive token generation dynamics, beam search decoding, top-k sampling, nucleus sampling (top-p), temperature scaling, batch normalization statistics updates, optimizer moment updates |
| **Property** | Quantitative or qualitative attributes describing the model, its representations, or its performance. They characterize the system but are not components or processes. | capacity, expressivity, inductive bias, parameter efficiency, sparsity, robustness, calibration quality, interpretability, compositionality, sample efficiency, scaling behavior, computational complexity, latency, throughput, memory footprint, training stability, generalization gap, invariance / equivariance, Lipschitz smoothness, representation dimensionality, information compression, loss landscape geometry (flat vs sharp minima), conditioning of gradients, noise sensitivity, out-of-distribution robustness |

## Computation Graph

> What is the structure of the **[Trainable Computational System Space](note.html?n=epistemica/observational/computational-learning.md)?** What is the general structure of a neural network? What are its components, and what are the possible variations of these components?
> 

### Basic

$f(x; \theta) = f^{(L)} \circ f^{(L-1)} \circ \cdots \circ f^{(1)}(x)$

- $x \in \mathbb{R}^{n_0}$: input
- $\theta$: set of all weights and biases
    - $W^{(\ell)} \in \mathbb{R}^{n_\ell \times n_{\ell-1}}$: weight matrix
    - $b^{(\ell)} \in \mathbb{R}^{n_\ell}$: bias vector
- $f^{(\ell)}$: function computed at layer $\ell$
- $L$: number of layers (output layer is $L$)

Computation:

- $L$ = loss function (e.g., MSE, cross-entropy)
- $\sigma(\cdot)$ = activation function (e.g., ReLU, sigmoid)
- $z^{(\ell)} = W^{(\ell)} a^{(\ell-1)} + b^{(\ell)}$ = pre-activation values
- $a^{(\ell)} = \sigma^{(\ell)}(z^{(\ell)})$;  activations of layer $l$
- $\delta^l$ = error at layer $l$ (gradient of loss w.r.t. $z^l$)

### Component Type

> Which components make up a neural network? Which are the types of components?
> 

> In this section we will try to describe known components of a NN.
> 

> **Note:** A neural network can be extremely complex, containing many functional components. Here, our intent is simply to create a taxonomy of these parts.
> 

Types:

- Input Encoding
- Representation Encoding
- Neuron-Level
- Layer-Level
- Between-Layer
- Memory (State)
- Output
- Auxiliary

| Category | Component Type | Description | Instances |
| --- | --- | --- | --- |
| **Primitive Computational Elements** | Neuron (Node / Unit) | Elementary processing element that computes an activation from weighted inputs and a non-linear function. | Perceptron, Sigmoid Neuron, ReLU Unit |
|  | Weights (Parameters) | Learnable coefficients that determine the influence of one neuron on another. | Connection Matrix, Kernel Weights, Attention Projection Matrices |
|  | Bias Parameters | Learnable offset values added before activation to shift the response function. | Bias Vector, Threshold Parameter |
| **Network Structural Elements** | Dense Layer | Fully connected layer where each neuron receives input from all neurons in the previous layer. | Fully Connected Layer, Linear Layer |
|  | Convolutional Layer | Applies convolutional filters to extract spatial or temporal features. | Conv1D, Conv2D, Conv3D, Depthwise Convolution |
|  | Pooling Layer | Reduces spatial dimensionality while retaining dominant features. | Max Pooling, Average Pooling, Global Average Pooling |
|  | Recurrent Layer | Maintains hidden state across sequence steps to model temporal dependencies. | Simple RNN, LSTM Layer, GRU Layer |
|  | Embedding Layer | Converts discrete tokens into continuous vector representations. | Word Embedding, Token Embedding, Positional Embedding |
| **Attention Architecture Components** | Attention Module | Mechanism allowing dynamic weighting of input elements when computing representations. | Self-Attention, Cross-Attention, Multi-Head Attention |
|  | Attention Projection Components | Linear projections used to compute compatibility scores between tokens. | Query Matrix (Q), Key Matrix (K), Value Matrix (V) |
|  | Positional Encoding | Injects positional information into sequence representations for order awareness. | Sinusoidal Encoding, Relative Position Encoding, Rotary Position Embeddings (RoPE) |
| **Information Flow Mechanisms** | Residual Connection | Skip pathway adding input to output to improve gradient propagation. | Skip Connection, Shortcut Connection |
|  | Dense Connectivity | Connects each layer to all subsequent layers to enhance feature reuse. | DenseNet Connections |
|  | Gating Mechanism | Controls the flow of information through multiplicative gates. | Input Gate, Forget Gate, Output Gate, Update Gate |
| **Normalization Components** | Normalization Layer | Normalizes intermediate activations to stabilize training and reduce internal covariate shift. | Batch Normalization, Layer Normalization, Instance Normalization, Group Normalization |
| **Regularization Mechanisms** | Dropout Mechanism | Randomly disables neurons during training to prevent co-adaptation and overfitting. | Dropout, Spatial Dropout, DropConnect |
|  | Regularization Term | Penalizes parameter magnitude or complexity within the loss function. | L1 Regularization, L2 Regularization, Weight Decay |
| **Nonlinear Transformation Components** | Activation Function | Applies nonlinear transformation to neuron outputs enabling complex function approximation. | ReLU, Leaky ReLU, PReLU, Sigmoid, Tanh, Softmax |
| **Training Objective Components** | Loss Function | Quantifies discrepancy between predicted output and ground truth. | MSE, MAE, Cross-Entropy, Huber Loss, KL Divergence |
| **Optimization Mechanisms** | Optimizer | Algorithm that updates parameters using gradients to minimize the loss. | SGD, Adam, RMSprop, AdamW |
|  | Learning Rate Scheduler | Strategy that dynamically adjusts the learning rate during training. | Step Decay, Cosine Annealing, Exponential Decay, Warm-up |
| **Architectural Macro-Blocks** | Transformer Block | Composite structure combining attention, feed-forward layers, residual connections, and normalization. | Encoder Block, Decoder Block |
|  | Autoencoder Architecture | Structure designed for representation learning via compression and reconstruction. | Encoder, Decoder, Latent Bottleneck |

| Axis | Purpose | Instance(s) |
| --- | --- | --- |
| Input Encoding | How raw data is represented | One-hot encoding, token embeddings, image patches, spectrograms, graph node features |
| Representation Encoding | Transformation between spaces | Dense/linear layers, convolutions, activation functions (ReLU, GELU), normalization layers (BatchNorm, LayerNorm), dropout |
| Neuron-Level | Computation unit details | Weighted summation, activation functions, LSTM/GRU cell, gating mechanisms, per-neuron attention |
| Layer-Level | Grouped neuron operations | Dense layers, convolutional layers, recurrent layers (RNN, LSTM, GRU), self-attention blocks, **pooling layers**, residual connections, normalization layers |
| Between-Layer | Cross-layer interactions | Multi-head attention, cross-attention, highway connections, mixture-of-experts routing, skip connections |
| Memory (State) | Storage and recall mechanisms | Hidden states (RNN/LSTM/GRU), key-value caches (transformers), external memory (Neural Turing Machines, Memory Networks), short-term buffers |
| Output | Mapping to task-specific outputs | Readout layers, decoders, softmax/sigmoid/tanh outputs, task-specific heads (classification, regression, object detection, language generation) |
| Auxiliary | Structural, meta, or supporting mechanisms | Positional encodings, parameter sharing (weight tying), conditional computation gates, architectural patterns (residual, dense, recursive connections) |

## Weight Space

> Which are the properties of the **Weight Space**? How to think about the **weigh space**? Which are types of properties (Geometric, Topological, etc)?
> 

## Hyperparameter

### Learning Rate

> In machine learning, the **learning rate** is a hyperparameter that controls the step size at each iteration while moving towards a minimum of the loss function during the training of a model.
> 

## Teaching Strategy

> 

## Inference Strategy

> 

## Training

### Evaluation

> 

### Optimization

## Taxonomy

> Representation, Evaluation, Optimization.,
> 

> Note: Every Representation Machine (Architecture)  possible needs there own Optimization Algorithms, and sometimes even you have to be clever on the more abstract concept of the Training Strategy,  not every problem as a clear x → y mapping.
> 

> Note: The years are approximate; please verify them before citing.
> 

| **Model** | **Description** | **Year Introduced** |
| --- | --- | --- |
| **Feedforward Neural Network (FNN)** | A basic neural network where information moves in one direction, from input to output, through hidden layers. Used in tasks like classification and regression. | 1958 |
| **Multilayer Perceptron (MLP)** | A type of FNN with multiple layers of neurons, where each layer is fully connected to the next, commonly used for supervised learning tasks. | 1980s |
| **Convolutional Neural Network (CNN)** | Specializes in processing grid-like data (e.g., images) using convolutional layers to detect spatial hierarchies of features. Common in image recognition. | 1989 |
| **Recurrent Neural Network (RNN)** | Designed for sequential data, where the output of a neuron is influenced by previous time steps. Often used for speech, text, and time series data. | 1986 |
| **Long Short-Term Memory (LSTM)** | A type of RNN that overcomes the vanishing gradient problem, making it suitable for learning long-term dependencies in sequential data. | 1997 |
| **Gated Recurrent Unit (GRU)** | A variation of LSTM, with fewer gates, used for sequential data tasks with similar functionality but reduced computational cost. | 2014 |
| **Autoencoder (AE)** | Unsupervised neural network used for data compression, dimensionality reduction, or feature learning by learning to encode and reconstruct the input data. | 1986 |
| **Generative Adversarial Network (GAN)** | Consists of two networks (a generator and a discriminator) that compete against each other, used in generating realistic synthetic data like images or text. | 2014 |
| **Radial Basis Function Network (RBFN)** | A type of neural network using radial basis functions as activation functions, useful for classification and function approximation. | 1988 |
| **Transformer** | A model architecture primarily used in natural language processing, leveraging self-attention mechanisms to process sequences in parallel, rather than sequentially. | 2017 |
| **Deep Belief Network (DBN)** | A generative model composed of multiple layers of stochastic, latent variables that learns to represent high-level abstractions of data through unsupervised learning. | 2006 |
| **Neural Turing Machine (NTM)** | A neural network with external memory, capable of learning algorithms and tasks that require external storage, such as sorting or copying. | 2014 |

## ❓ QA

### What type of element is a neural net?

> A **neural network** is a parameterized computational formal object that implements a mapping from an input space to an output space.
> 

### What is the ‘meta ontology’ of a neural net? Which are the types of elements deepest categories related to neural nets?

> If you like a trained neural net.
> 

> The utility of this framework becomes clear when decomposing or characterizing a neural network, as it defines the dimensions along which the system can be analyzed.
> 

| Category | Description | Instance(s) |
| --- | --- | --- |
| **Phenomena** | Observable behaviors or emergent effects produced by the network during training or inference. They are not explicitly programmed but arise from system interactions. | generalization, grokking, in-context learning, feature superposition, attention heads specializing |
| **Structure** | The static formal organization of the network that defines how computations are arranged and connected. | layers, computational graph, residual connections, attention blocks, convolutional layers |
| **Parameter** | Trainable numerical degrees of freedom that determine the specific behavior of the network. | weights, biases, embedding matrices, $(W_Q), (W_K), (W_V)$ |
| State | Internal values that exist during computation and evolve as the network processes inputs. | neuron activations, hidden states, attention scores, token embeddings, memory |
| **Dynamics** | The processes through which states evolve and parameters change over time. | forward propagation, recurrent updates, gradient descent training dynamics |
| Property | Quantitative or qualitative attributes that characterize the network, its representations, or its performance. They describe the system but are not themselves components or processes. | capacity, expressivity, sparsity, robustness, interpretability, sample efficiency, scaling behavior |

### How to think deeply about neuron weights (connections)?

> How to think in terms of driving dynamics?
> 

> Weights are one of the primary **“atoms”** that **compose** (**or shape**) the dynamics of the network. Note that they can also be part of more complex computational modules—such as attention mechanisms—which incorporate additional structures to drive meaningful representational evolution trajectories.
> 

> Weights parameterize the operators that shape how representations evolve through the network.
> 

| **Interpretation** | **Description** | **Critique** |
| --- | --- | --- |
| **Linear Coefficients** | Weights act as coefficients in affine transformations ($z = Wx + b$). They scale and combine input features to produce neuron pre-activations. | This view is mathematically correct but shallow; it ignores the nonlinear composition across layers and the global computation implemented by the network. |
| **Feature Detectors** | Weight vectors encode patterns that neurons respond to. A neuron activates strongly when the input aligns with the learned weight vector. | Works well for early layers (e.g., edges in CNNs) but becomes less interpretable in deeper layers where features are highly distributed and compositional. |
| **Hyperplane Orientations** | The weight vector defines the orientation of a decision boundary ($w \cdot x + b = 0$) in representation space. | This interpretation mainly applies to single-layer or linear classifiers. In deep networks, decision boundaries become highly nonlinear and cannot be attributed to individual weight vectors. |
| **Filters** | Weights implement filters that transform signals, particularly clear in convolutional networks where kernels detect edges, textures, or patterns. | This interpretation is architecture-dependent and less useful in non-convolutional models or in very deep layers where filters combine into complex operators. |
| **Coupling Strengths in a Graph** | The neural network can be viewed as a weighted directed graph where weights represent the strength of connections between neurons. | Graph interpretation captures structure but misses the functional semantics of transformations and the nonlinear computations occurring at nodes. |
| **Drivers of Internal Dynamics** | Weights define the update rule governing the evolution of the network state $h_{l+1} = F(h_l)$. They determine trajectories in representation space. | This view captures deep structure but requires dynamical systems analysis; it can be difficult to apply concretely to large architectures. |
| **Parameters of Operators** | Weight matrices parameterize linear operators that transform representations between layers. The network computation is a sequence of operator compositions. | This perspective is precise but abstract; it does not immediately reveal what computation or algorithm the network is implementing. |
| **Memory of Learned Structure** | During training, weights encode statistical regularities from data. They store patterns, correlations, and latent structure learned from the dataset. | "Memory" is metaphorical; weights do not store explicit symbolic knowledge but distributed statistical structure that may be hard to interpret. |
| **Information Routing Parameters** | Weights regulate how signals propagate and mix across the network, determining which features influence later computations. | This explanation captures signal flow but not the internal transformations applied to those signals. |
| **Algorithmic Components (Circuits)** | In mechanistic interpretability, sets of weights form circuits implementing specific computational operations (e.g., induction heads in transformers). | Requires identifying structured weight interactions; individual weights are rarely meaningful without analyzing the full circuit. |

### Which are types of phenomena that appears in neural nets during inference?

| **Category** | **Phenomenon** | **Description** |
| --- | --- | --- |
| 🧠 **Representation Dynamics** | **Feature Emergence** | Intermediate neurons encode latent features not explicitly programmed (e.g., edges → textures → objects). |
|  | **Hierarchical Abstraction** | Deeper layers represent progressively more abstract and semantic information. |
|  | **Distributed Encoding** | Information is represented across many neurons rather than a single unit. |
|  | **Manifold Formation** | Inputs organize into structured manifolds in activation space. |
|  | **Representation Trajectories** | Activations evolve through layers along trajectories in latent space. |
| 🎯 **Attention & Information Routing** | **Selective Attention** | The model dynamically prioritizes relevant tokens or spatial regions. |
|  | **Information Routing** | Signals flow through different internal pathways depending on the input. |
|  | **Contextual Reweighting** | Representations change depending on contextual relationships. |
| ⚙️ **Computation Dynamics** | **Iterative Refinement** | Later layers refine earlier representations. |
|  | **Residual Accumulation** | Residual blocks add incremental corrections to representations. |
|  | **Compositional Computation** | Complex outputs emerge from combinations of learned primitives. |
|  | **Implicit Iteration** | Layer stacking approximates iterative algorithms. |
| 📐 **Geometric Phenomena** | **Dimensional Expansion / Compression** | Representations may expand to higher dimensions then compress near the output. |
|  | **Linearization** | Nonlinear relationships become linearly separable in deeper layers. |
|  | **Feature Alignment** | Representations align with task-relevant directions in latent space. |
|  | **Orthogonalization** | Networks decorrelate internal feature representations. |
| 📊 **Statistical Effects** | **Activation Sparsity** | Only a subset of neurons activate for any input. |
|  | **Activation Saturation** | Nonlinearities cause neuron outputs to saturate. |
|  | **Noise Suppression / Amplification** | Networks suppress irrelevant noise while amplifying signal. |
| 🧩 **Emergent Functional Behavior** | **Pattern Completion** | Missing or partial input information can be reconstructed. |
|  | **Associative Recall** | Similar inputs activate similar internal states. |
|  | **Prototype Formation** | Classes correspond to prototypical latent vectors. |
| 🏗 **Architecture-Specific Effects** | **Attention Head Specialization** | Attention heads specialize in different computational roles. |
|  | **Token Mixing** | Transformers mix information across tokens in context. |
|  | **Spatial Feature Maps** | CNN layers maintain spatially structured feature maps. |
|  | **Temporal State Evolution** | RNNs evolve hidden states over time. |
| 🔬 **Advanced / Research Phenomena** | **Feature Superposition** | Multiple concepts share neurons or latent directions. |
|  | **Circuit Formation** | Subnetworks emerge that perform specific computations. |
|  | **Activation Steering Directions** | Certain latent directions steer outputs toward specific behaviors. |
|  | **Emergent Reasoning Chains** | Multi-step reasoning behavior appears in deep transformers. |
|  | **Representation Collapse** | Representations lose diversity or collapse into low-rank spaces. |
|  | **Phase Transitions** | Sudden capability changes appear as scale or depth increases. |

### Suppose we have two intermediate layers in a deep multilayer neural network. During inference, we pause the forward pass, take the output state of the second layer, and feed it back into the first layer for additional processing. Empirically, this iterative reuse of the layers improves the model’s performance. What should this phenomenon be called?

> 

### How does neural networks represents?

> **Neural networks** represent complex functions by composing simpler, differentiable transformations across multiple layers.
> 

### What makes some neural network architectures better suited to instantiate certain dynamics or capacities to perform specific tasks?

A neural network’s ability to perform certain tasks is not just about **parameter count**, but about:

1. **Inductive bias** → what patterns the architecture can naturally represent.
2. **State persistence** → what temporal or hierarchical dynamics can be maintained.
3. **Computational primitives** → what transformations the network can express easily.
4. **Stability and trainability** → what dynamics can actually be learned in practice.
5. **Modularity and separation of dynamics** → how multiple processes can coexist and interact.

### How does domain  representations emerges  from  neural networks represents?

> See more in [Philosophy](https://app.notion.com/p/Philosophy-ccc223e791024b4181a87d0d2b5d1cec?pvs=21) - Representation.
> 

> From Representation Techniques → Representation of Dataset - Phenomena  - System.
> 

> Representations emerge because the network is forced to find efficient, hierarchical encodings of data that minimize loss. This process is driven by both the structure of the data and the constraints imposed by the network's architecture and training objective.
> 
- **Representations** emerge because *the easiest way for the network to minimize the loss is to **build internal abstractions** about the data*.
- Representations that ***compress*** and ***organize*** the data structure make it easier for the final layer to map input → correct output.
- The network is finding a ***reparametrization*** of the input space where the supervised task (classification, prediction) becomes simpler.
- Neural networks develop internal representations because building abstractions is the path of least resistance for minimizing loss on complex tasks.
- **Mechanisms Behind Representation Learning**
    - **Distributed Representations**: Features are encoded across many neurons (not just one), allowing combinatorial expressivity.
    - **Disentanglement**: Ideally, different neurons or directions in activation space correspond to interpretable factors (e.g., "color," "shape," or "topic").
    - **Invariance and Equivariance**:
        - Some layers become invariant to irrelevant variations (e.g., a cat classifier ignoring background noise).
        - Others remain equivariant (e.g., preserving spatial relationships in convolutional networks).
    - **Nonlinearity:** Activation functions (ReLU, Sigmoid) enable modeling nonlinear relationships.
- Advanced Representations
    - **Convolutional Nets (CNNs):** Spatial hierarchies via shared weights.
    - **Recurrent Nets (RNNs):** Temporal sequences via memory (hidden states).
    - Graph Neural Networks (GNNs):   	Node roles, relationship types
    - **Transformers:** Context-aware representations via attention.
    - **Vision Transformers (ViT): 	Patch-level global features**
    - **Diffusion Model**: Diffusion models assume that "realistic data" can be built up incrementally from noise, by progressively filling in structure. Progressive Denoising  (Data is not just "one thing" — it's a **path through representation space**.)
- **Hierarchy**
    - **Early layers** tend to extract low-level features. (In images: edges, colors, simple textures. In language: common n-grams, part-of-speech patterns.)
    - Middle layers **combine features into mid-level patterns**  (Shapes, simple objects for images. Phrases, syntactic structures for text.)
    - **Deeper layers** encode higher-level abstract concepts. (Faces, categories, object relationships in vision. Semantic meaning, intent, or logic structures in language.)
- **Why Do They Work?**
    - **Statistical Efficiency**: The network learns features that compress input data in a way useful for downstream tasks.
    - The emergence of representations is related to **information** **bottleneck theory**:
    The idea is that networks balance between preserving information and compressing it, retaining only what is relevant for the task.
    - It also connects to ideas from **manifold learning**: The network may unwrap, stretch, or flatten the data manifold to make tasks easier.
    - **Compositionality**: Deeper layers build complex features from simpler ones, mirroring how real-world data is structured.
    - **Inductive Biases**: Architectural choices (e.g.,  convolutions for images, attention for sequences) guide the network  toward useful representations.

### Do diffusion models represent a breakthrough in representation learning  or are they primarily an architectural refinement?

> Diffusion models are *primarily an architectural refinement* rather than a *fundamental breakthrough in representation learning* like recurrent neural networks (RNNs) were.
> 

Representation learning is about discovering good internal data structures (embeddings, features) from raw input. **Breakthroughs** in representation learning typically introduce fundamentally new ways of *organizing information* internally, not just *generating* or *mapping* inputs to outputs.

- **RNNs (and later LSTMs, GRUs)** *were* a major breakthrough: they introduced **stateful, sequential memory** that could *accumulate representations* over time, letting models internally represent sequences, grammars, or temporal dependencies. This expanded what could be learned and represented.
- **Diffusion models**, on the other hand, are largely a *new generative method*:
    - They learn to *gradually denoise* a latent representation into a structured sample.
    - Their strength is in *progressive refinement* and *modeling high-dimensional distributions* in a stable and efficient way.
    - But the *internal representation* is still largely based on traditional architectures (CNNs, UNets, sometimes Transformers) — **the diffusion process controls how generation happens**, not fundamentally *what kinds of representations are learned*.

In other words, **diffusion models innovated in *how to model distributions and generate samples*, not in *what kinds of features or embeddings the model can learn***.

(Contrast this with something like **transformers**, which *were* a real breakthrough in representation learning, because attention mechanisms gave models a new, flexible way to relate all parts of an input.)

### How to visualize the representations of neural networks?

- **Visualization**: When people use techniques like t-SNE or PCA to plot internal activations, you can often see clusters form that correspond to different classes or concepts.
- **Probing**: Train a simple classifier on internal activations. They often already contain "almost everything" you need to predict important properties.
- **Linear Separability** increases through the layers: raw data is hard to separate, but activations in deep layers are often easily separated by simple hyperplanes.

### What do we mean by “neural nets learn distributed representations”?

> Distributed representation: Each neuron contributes to multiple features, and each feature is encoded by the pattern of activations across many neurons.
> 
> 
> **Distributed computation:** Neural network transformations—such as recognizing a face or generating a sentence—are performed as **distributed operations across many neurons**, rather than as simple, localized functions.
> 

**Consequences:**

- **Compositionality:** Complex features emerge from combinations of simpler patterns.
- **Parallelism:** Computation is spread across many units, allowing high-dimensional processing.
- **Robustness & flexibility:** Damage or noise in individual neurons affects performance gracefully rather than catastrophically.

**Case:**

- In image recognition, the concept of a “cat” is not encoded by a single neuron. Instead, it emerges from the combined activations of neurons detecting edges, textures, shapes, and patterns across the layer.

### Which are type of spaces that arise in a NN Study?

| Space | What Lives in the Space | Dimension | What It Is Used To Study |
| --- | --- | --- | --- |
| **Input Space** | Raw data vectors | $\mathbb{R}^n$ | Data geometry, distribution, feature structure |
| **Output Space** | Predictions or targets | $\mathbb{R}^k$ | Classification/regression behavior |
| **Weight Space (Parameter Space)** | Model parameters | $\mathbb{R}^p$ | Optimization, loss landscape |
| **Activation Space (Hidden State Space)** | Internal neuron activations | varies per layer | Representation learning |
| **Feature Space / Representation Space** | Learned embeddings | lower dimensional manifold | Semantic structure of data |
| **Loss Landscape Space** | Loss values over parameters | scalar field over weight space | Optimization geometry |
| **Gradient Space** | Gradients of loss wrt parameters | same dimension as weights | Training dynamics |
| **Function Space** | All functions the network can represent | infinite-dimensional | Expressivity and approximation theory |
| **Hypothesis Space** | Set of candidate models | large function family | Statistical learning theory |
| **Data Manifold** | Low-dimensional manifold inside input space | intrinsic dimension $d \ll n$ | Generalization |
| **Trajectory Space** | Paths taken by parameters during training | curves in weight space | Optimization dynamics |
| **Kernel Space** | Similarity structures between inputs | induced by kernels | Neural Tangent Kernel theory |
| **Latent Space** | Compressed representation used by models | moderate dimension | generative models, embeddings |

### (Compression, Survive Variability) How do we think about generalization?

> **Generalization** is the ability of a model, system, or agent to produce correct or useful outputs on inputs or situations that it has not encountered during training or prior experience. It reflects the extent to which learned patterns capture underlying regularities rather than overfitting to idiosyncrasies of observed data.
> 

> Can you capture the **deepest insight about a task** - ignore the noise - and be able used it to performance in unseeing territory.
> 

> Can we take what you have learn and use it in novel situations, can you recognize novel situation, can you know your limit.
> 

> Generalization is not a static property of a network or dataset; it emerges from the **interaction between the network’s architecture, the training dynamics, and the structure of the data**, producing functions that reflect underlying patterns rather than memorized noise.
> 

> **Generalization is compression** of information about the training data down to task-relevant structures, either in representations or in parameters.
In other words, a neural network generalizes because it abstracts and distills patterns, discarding details that don’t matter for the task.
> 

> **Flat minima** and implicit compression make neural networks **robust and generalizable**, which mirrors Taleb’s principles: systems that survive variability, discard fragility, and retain essential structure are more likely to endure and succeed.
> 

### Why certain ‘tasks’ required multiple layers?

> One step is not sufficient to figure everything out; sometimes multiple steps are required.
> 

**Why (for some tasks)**:

- Inner Structural Dependencies:  Nested Abstractions, Long-range dependencies, compositional relations, recursive structures, …
- Non-Linear Domains Origins,
- Compositional Generative Processes Origins,  the data has been generated - via  a set of sequential transformations, recursive structures.

## References

- [Cognitive](https://app.notion.com/p/Cognitive-8292b945586b49d3b3e2c3323d8bb53a?pvs=21)
- [Guia Mayor](https://app.notion.com/p/Guia-Mayor-cce02f04c4724677ba46b314151134db?pvs=21)
- [Representation](https://app.notion.com/p/Representation-16fc0f5171ec80c6bb5fc675d075f9b1?pvs=21)
- [A Guide to Study](https://app.notion.com/p/A-Guide-to-Study-c24ba1c6d4084de1b741ff4fef7a1749?pvs=21)
- [A Guide to Language and Cognition](https://app.notion.com/p/A-Guide-to-Language-and-Cognition-1aac0f5171ec804794dbc97bc4999e9c?pvs=21)
- Ryon, John W. "Neuron Networks as Hamiltonian Dynamic Systems."
- Nielsen, M. A. (2015). Neural Networks and Deep Learning (Vol. 25). Determination press San Francisco, CA, USA.
- Hinton, G. E. (1984). Distributed Representations.
- Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1985). Learning Internal Representations by Error Propagation.
- Bengio, Y., Courville, A., & Vincent, P. (2012). Representation Learning: A Review and New Perspectives. 35(8), 1798–1828.
- Scholkopf, B., Locatello, F., Bauer, S., Ke, N. R., Kalchbrenner, N., Goyal, A., & Bengio, Y. (2021). Towards Causal Representation Learning. 109(5), 612–634.
- Gidaris, S., Singh, P., & Komodakis, N. (2018). Unsupervised Representation Learning by Predicting Image Rotations.
- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). Language Models are Unsupervised Multitask Learners.
- Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2022). Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task.
- Elman, Jeffrey L. “Finding structure in time.” Cognitive science 14.2 (1990): 179-211.
- Lake, Brenden M., et al. “Building machines that learn and think like people.” Behavioral and brain sciences 40 (2017): e253.
- Liang, Weixin, James Zou, and Zhou Yu. “Alice: Active learning with contrastive natural language explanations.” arXiv preprint arXiv:2009.10259 (2020).
- Coleman et al. Selection via proxy: Efficient data selection via deep learning. ICLR 2020.
- Andreas. Measuring Compositionality in Representation Learning. ICLR 2019.
- Sebastian Ruder. An Overview of Multi-Task Learning in Deep Neural Networks.
- Tao Lei, Regina Barzilay, and Tommi Jaakkola. Rationalizing Neural Predictions. EMNLP 2016.
- Hal Daume III and Daniel Marcu. Learning as Search Optimization. ICML 2005.
- Schmidhuber, J. (2014). Deep Learning in Neural Networks: An Overview. https://doi.org/10.1016/j.neunet.2014.09.003
- Parr, T., & Howard, J. (2018). The Matrix Calculus You Need For Deep Learning. https://doi.org/10.48550/arxiv.1802.01528
- [A Visual and Interactive Guide to the Basics of Neural Networks](https://jalammar.github.io/visual-interactive-guide-basics-neural-networks/)
- [A Visual And Interactive Look at Basic Neural Network Math](https://jalammar.github.io/feedforward-neural-networks-visual-interactive/)
- [The Neural Network Zoo](https://www.asimovinstitute.org/neural-network-zoo/)
- [Feedforward Neural Network](https://en.wikipedia.org/wiki/Feedforward_neural_network)
- [Dissipative Hamiltonian Neural Networks](https://greydanus.github.io/2022/01/25/dissipative-hnns/)
- [Piecewise-constant Neural ODEs](https://greydanus.github.io/2021/06/11/piecewise-nodes/)
- [Self-classifying MNIST Digits](https://greydanus.github.io/2020/08/27/selforg-mnist/)
- [Differentiable Memory and the Brain](https://greydanus.github.io/2017/02/27/differentiable-memory-and-the-brain/)
- [A Bird’s Eye View of Synthetic Gradients](https://greydanus.github.io/2016/11/26/synthetic-gradients/)
- [The Art of Regularization](https://greydanus.github.io/2016/09/05/regularization/)
- [Deep Learning Research](https://www.youtube.com/playlist?list=PLUmpJyzF-3OX6gLtVa9zO5JeAoOtZKrYL)
- [Speculations Concerning the First Ultraintelligent Machine](https://www.sciencedirect.com/science/article/abs/pii/S0065245808604180)
- [Why does gradient descent work?](https://thepalindrome.substack.com/p/why-does-gradient-descent-work)
- [From deep to long learning?](https://news.ycombinator.com/item?id=35502187)
- [Deep Learning Foundations to Stable Diffusion](https://news.ycombinator.com/item?id=35449831)
- [Exercises in Machine Learning](https://arxiv.org/pdf/2206.13446.pdf)
- [A Cookbook of Self-Supervised Learning](https://arxiv.org/abs/2304.12210)
- Ng, A., & Jordan, M. (2001). On discriminative vs. generative classifiers: A comparison of logistic regression and naive bayes. 14.
- Trask, A. W. (2019). Grokking Deep Learning. Simon and Schuster.
- Ng, A., & Jordan, M. (2001). On discriminative vs. generative classifiers: A comparison of logistic regression and naive bayes. 14.
- Neural network training makes beautiful fractals
[https://news.ycombinator.com/item?id=39349992](https://news.ycombinator.com/item?id=39349992)
- How do neural networks learn? ([phys.org](http://phys.org/))
[https://news.ycombinator.com/item?id=39744669](https://news.ycombinator.com/item?id=39744669)
- Neural Networks are not Turing Machines/Turing Complete
[https://twitter.com/MLStreetTalk/status/1774473007248871660](https://twitter.com/MLStreetTalk/status/1774473007248871660)
- Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position
[https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf](https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf)
- [Feed Foward](https://www.wikiwand.com/en/Feedforward_neural_network)
- [Computation Graph](note.html?n=epistemica/observational/computation-graph.md)
- [Learning rate](https://en.wikipedia.org/wiki/Learning_rate)
- [Setting the learning rate of your neural network](https://www.jeremyjordan.me/nn-learning-rate/)
- https://en.wikipedia.org/wiki/History_of_artificial_neural_networks
- [ ]  [‣](https://app.notion.com/p/10e598edb79081f5a46dc9df134d37f7?pvs=21)
- [**Neuron**](https://app.notion.com/p/Neuron-95cc41fef358466386d0c7967d6e74ec?pvs=21)
- [ ]  https://en.wikipedia.org/wiki/History_of_artificial_neural_networks#cite_note-lin19703-28
- [ ]  https://arxiv.org/abs/2212.11279
- [ ]  https://github.com/KellerJordan/Muon
- [ ]  https://kellerjordan.github.io/posts/muon/
- [ ]  https://arxiv.org/abs/2502.16982
- [ ]  https://en.wikipedia.org/wiki/Layer_(deep_learning)
- Ribeiro, Marco Tulio, Sameer Singh, and Carlos Guestrin. "" Why should i trust you?" Explaining the predictions of any classifier." Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining. 2016.
- Avrim Blum and Tom Mitchell: Combining Labeled and Unlabeled Data with Co-Training, 1998.
- [What is Pooling in Deep Learning?](https://www.kaggle.com/questions-and-answers/59502)
- https://en.wikipedia.org/wiki/History_of_artificial_neural_networks
- https://stats.stackexchange.com/questions/506610/what-exactly-is-a-representation-in-the-context-of-machine-learning
- https://arxiv.org/abs/2410.03006v1
- https://www.nature.com/articles/s41467-023-36583-0
- https://www.nature.com/articles/s41586-024-07799-x?fromPaywallRec=false
- https://arxiv.org/abs/1810.11750
- https://en.wikipedia.org/wiki/Multi-task_learning
- https://arxiv.org/abs/1206.5538
- https://en.wikipedia.org/wiki/Information_bottleneck_method
- https://arxiv.org/abs/2402.10450v2
- [Transformer](note.html?n=technica/ais/architecture/transformer/transformer.md)
- [An Essay on Representation in Computationally Synthesized Systems](https://app.notion.com/p/An-Essay-on-Representation-in-Computationally-Synthesized-Systems-320c0f5171ec805ab65ac0e60ba9dc06?pvs=21)
- https://en.wikipedia.org/wiki/Weight_initialization
