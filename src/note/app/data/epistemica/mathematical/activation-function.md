---
tags: [function, operator]
---

# Activation Function

 : Ridge Function (Ridge%20Function%20100c0f5171ec80d3a104da5c9ccaeee1.md)

> An **activation function in a neural network** is a mathematical function applied to a neuron's output. It introduces nonlinearity, enabling the network to model complex relationships and capture patterns that linear transformations alone cannot.
> 

## Taxonomy

| **Activation Function** | **Mathematical Definition** | **Differentiable** | **Typical Use Case** |
| --- | --- | --- | --- |
| **Binary Step Function** | $f(x) = \begin{cases} 1 & \text{if } x \geq 0 \\ 0 & \text{if } x < 0 \end{cases}$ | No | Early neural networks, simple binary classifiers |
| **Heaviside Step Function** | $H(x) = \begin{cases} 1 & \text{if } x \geq 0 \\ 0 & \text{if } x < 0 \end{cases}$ | No | Control systems, digital signal processing |
| **Sign Function (Signum)** | $\text{sgn}(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{if } x = 0 \\ -1 & \text{if } x < 0 \end{cases}$ | No | Perceptron learning rule, determining sign |
| **Sigmoid Function** | $f(x) = \frac{1}{1 + e^{-x}}$ | Yes | Logistic regression, binary classification |
| **Hyperbolic Tangent (Tanh)** | $f(x) = \tanh(x) = \frac{2}{1 + e^{-2x}} - 1$ | Yes | Hidden layers of neural networks |
| **Rectified Linear Unit (ReLU)** | $f(x) = \max(0, x)$ | Yes | Hidden layers of deep neural networks |
| **Leaky ReLU** | $f(x) = \begin{cases} x & \text{if } x \geq 0 \\ \alpha x & \text{if } x < 0 \end{cases}$ | Yes | Hidden layers of deep neural networks |
| **Parametric ReLU (PReLU)** | $f(x) = \begin{cases} x & \text{if } x \geq 0 \\ \alpha x & \text{if } x < 0 \end{cases}$ | Yes | Hidden layers of deep neural networks |
| **Exponential Linear Unit (ELU)** | $f(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha (e^x - 1) & \text{if } x \leq 0 \end{cases}$ | Yes | Deep neural networks |
| **Scaled Exponential Linear Unit (SELU)** | $f(x) = \lambda \begin{cases} x & \text{if } x > 0 \\ \alpha (e^x - 1) & \text{if } x \leq 0 \end{cases}$ | Yes | Self-normalizing neural networks |
| **Gaussian Error Linear Unit (GELU)** | $f(x) = x \cdot \Phi(x)$ | Yes | Transformer networks, BERT |
| **Softmax Function** | $f(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}}$ | Yes | Output layer of multi-class classification |
| **Swish** | $f(x) = x \cdot \text{sigmoid}(x)$ | Yes | Deep learning models |
| **Mish** | $f(x) = x \cdot \tanh(\text{softplus}(x))$ | Yes | Deep learning models |
| **Softplus** | $f(x) = \log(1 + e^x)$ | Yes | Smooth approximation to ReLU |

## Case Study

### Object Detection

> Pixel intensity combinations rarely map linearly to high-level semantic labels (e.g., “cat” vs “dog”).
> 

> Patterns like edges, textures, rotations, and occlusions require nonlinear transformations (exactly what convolution + activation layers do).
> 

## QA

### How do we know that a given data set is non-linear?

> Fit a linear model to the data and assess how accurately it represents the underlying relationships.
> 

### What’s the role of activation functions in neural computation?

> Activation functions play a central role in neural computation: they allow networks to **represent both linear and non-linear data**, shape internal representations (encodings), and influence the optimization process—with advantages and drawbacks. In essence, activation functions are what make deep learning a form of calculus operating over matrices as data structures.
> 

## References

- [Activation function](https://en.wikipedia.org/wiki/Activation_function)
- [Step function](https://en.wikipedia.org/wiki/Step_function)

[Indicator Function](../observational/indicator-function.md)
