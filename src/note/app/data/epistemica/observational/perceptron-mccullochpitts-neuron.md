---
tags: [learning-system]
---

# Perceptron (McCulloch–Pitts Neuron)

 : Multilayer Perceptron (MLP)  (Multilayer%20Perceptron%20(MLP)%2081e6777b58b74892af6f68d2bd821e02.md)

> The **perceptron** is a basic artificial neural network model that simulates the functioning of a single neuron, capable of making binary classification decisions based on weighted inputs and an activation function.
> 

> A **perceptron** learns a function with the following scheme $f : X \to \{-1, +1\}$ represented as $f = \text{sgn}(w \cdot x)$, where $X = \{0,1\}^n$ or $X = \mathbb{R}^n$,  $w \in \mathbb{R}^n$.
> 

> Invented by [Warren McCulloch](https://en.wikipedia.org/wiki/Warren_McCulloch) and [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts); implemented by  [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt).
> 

> **Limitations**: The **Perceptron** is limited by its **inability to solve non-linearly separable problems**, lack of probabilistic outputs, sensitivity to learning rate, convergence issues for non-linear data, and overall simplicity, which restricts its capacity to model complex patterns and relationships.
> 

> https://github.com/dbremont/algorithms/blob/main/models/basic/perceptron.ipynb
> 

![](https://miro.medium.com/v2/resize:fit:1068/1*Z1_IgFO1c6tq4Tz1iwJraw.png)

## Learning Algorithm

> The **perceptron** learning algorithm is an iterative algorithm that adjusts the weights of a **perceptron** model based on the misclassifications of training examples, aiming to find the optimal set of weights that allows **Linear classifier** for accurate classification.
> 

**Weight** updates:

$*w_{i+1} ← w_i + η ⋅ (y_i − \hat{y_i}) ⋅ x_i*$

In this formula, $*w_i*$ represents the weight of the $*i_\text{th}*$ feature, *η* is the learning rate, $*y*$ is the desired output, predicted is the predicted output, and $*x_i*$ is the $*i_\text{th}*$ input feature. The weight update formula adjusts the weights of the **Perceptron** based on the prediction error and the input value.

## Proof of Convergence

> The **Perceptron Convergence Theorem** states that if the training data is **linearly separable**,
 the perceptron algorithm will converge to a set of weights that correctly classify all training examples in a **finite number of steps**.
> 

| **Proof Strategy** | **Key Idea** | **Steps** | **Strength** |
| --- | --- | --- | --- |
| **Geometric Approach** | Analyze the angle and distance between the weight vector and data points. | Show the weight vector aligns with the optimal hyperplane by reducing the angle between $\mathbf{w}$ and $\mathbf{x}$ with each update. | Intuitive and visually interpretable. |
| **Algebraic Approach** | Use dot products to measure progress in aligning $\mathbf{w}$  with correctly classified points. | Demonstrate bounds on the growth of $||\mathbf{w}\|^2$ and show convergence using these bounds. | Compact and mathematically rigorous. |
| **Margin-Based Proof** | Use the minimum margin $\gamma$ between the decision boundary and data points. | Define the margin $\gamma$, link it to the weight updates, and bound the total number of updates required for convergence. | Closely related to modern concepts like SVMs. |
| **Iterative Inequality Reduction** | Measure progress via an error metric and prove it decreases iteratively. | Define a potential function (e.g., $\mathbf{w} \cdot \mathbf{w}^*$), show it increases monotonically until misclassification stops. | Clear and methodical, step-by-step. |
| **Energy Function Method** | Use a decreasing energy function to ensure convergence. | Define an energy function (e.g., squared distance between $\mathbf{w}$ and optimal hyperplane) and show it decreases with each weight update. | Analogous to methods in physics and optimization. |
| **Probabilistic Proofs** | Bound the number of updates using probabilistic arguments. | Assume a probability distribution over data points and show convergence happens with high probability in a finite number of steps. | Useful for stochastic and non-deterministic cases. |
| **Dual Representation and Convex Optimization** | Represent weight updates in terms of dual variables and link to convex optimization. | Express weights as a linear combination of inputs and show dual formulation enforces convergence under linear separability. | Connects to more advanced learning algorithms. |

Proof: [Perceptron Convergence Theorem](../mathematical/perceptron-convergence-theorem.md)

## Training

> The Perceptron is a single-layer neural network, meaning it can only learn linear decision boundaries. It cannot capture more complex relationships or patterns in the data.
> 

> The performance and convergence of the Perceptron **are susceptible to the choice of learning rate**. A learning rate that is too high can cause the algorithm to overshoot, while a learning rate that is too low can result in slow convergence.
> 

| **Training Method** | **Description** | **Key Characteristics** | **Advantages** | **Limitations** |
| --- | --- | --- | --- | --- |
| **Perceptron Learning Rule** | Adjusts weights based on misclassified examples to minimize classification errors. | Weight update: $\Delta \mathbf{w} = \eta (y_{\text{true}} - y_{\text{pred}}) \mathbf{x}$. | Guarantees convergence for linearly separable data; simple and interpretable rule. | Fails for non-linearly separable data; sensitive to the order of inputs. |
| **Standard Perceptron** | Iteratively adjusts weights based on misclassified samples. | Updates weights when an error occurs; uses a fixed learning rate $\eta$. | Simple and guarantees convergence for linearly separable data. | Does not handle non-linearly separable data; sensitive to data order. |
| **Batch Perceptron** | Updates weights after processing the entire dataset in one iteration (epoch). | Computes cumulative updates based on all misclassified examples in the dataset. | Reduces sensitivity to the order of data; more stable updates. | Slower convergence; computationally expensive for large datasets. |
| **Hebbian Learning** | Updates weights based on the correlation between inputs and outputs. | Weight update: $\Delta w_i = \eta x_i y$, where `y` is the desired output. | Biologically inspired; simple rule; strengthens associations between correlated inputs. | Not error-driven; does not directly minimize classification errors. |
| **Delta Rule (Widrow-Hoff)** | Minimizes the squared error between predicted and desired outputs. | Gradient descent-based update: $\Delta \mathbf{w} = \eta (y_{\text{true}} - y_{\text{pred}}) \mathbf{x}$. | Effective for learning linearly separable problems; closely related to modern optimization. | Requires continuous output values; not suitable for binary classification with step functions. |
| **Pocket Algorithm** | Keeps the best-performing weights observed so far during training. | Tracks the lowest error weights even if training data is not linearly separable. | Works for both linearly separable and non-separable data. | Slower convergence; requires additional memory for storing best weights. |
| **Average Perceptron** | Computes the average of all weight vectors throughout training. | Uses the average weight vector to make predictions instead of the final weight vector. | Reduces the effect of noisy updates; improves generalization performance. | Requires additional storage for averaging; less interpretable final model. |
| **Kernel Perceptron** | Extends the perceptron to handle non-linearly separable data using kernels. | Applies kernel functions to map data into higher-dimensional spaces. | Enables handling of non-linear problems; no explicit feature transformation required. | Computationally expensive; depends on choice of kernel. |
| **Multi-Class Perceptron** | Extends the perceptron to classify multiple classes. | Uses a one-vs-rest or one-vs-one strategy for multi-class problems. | Handles multi-class problems effectively. | Requires separate models for each class pair; scales poorly with many classes. |
| **Margin Perceptron** | Updates weights only if the classification margin is below a certain threshold. | Introduces a margin parameter to improve robustness. | Ensures a margin of separation, leading to better generalization. | Requires tuning of the margin parameter; still fails on non-separable data. |
| **Stochastic Perceptron** | Updates weights after processing each data point individually. | Weight updates occur immediately after each misclassified data point. | Fast and computationally efficient for large datasets. | Can result in noisy updates; may require multiple epochs to converge. |
| **Voted Perceptron** | Tracks all weight vectors encountered during training and assigns votes to them. | Final prediction is made based on a weighted majority vote of all recorded weight vectors. | Improves accuracy and generalization; robust to noise. | Requires storing multiple weight vectors; computationally intensive for inference. |
| **Perceptron with Decay** | Reduces the learning rate over time during training. | Gradually decreases η\eta to stabilize updates as training progresses. | Balances fast convergence initially with stability later; reduces overshooting. | Needs careful tuning of decay schedule; may converge too slowly if decay is too aggressive. |

## Perceptron Learning Rule

> 

## References

- [Norm](../mathematical/norm.md)
- https://en.wikipedia.org/wiki/Perceptron
- [The Perceptron](https://jontysinai.github.io/jekyll/update/2017/11/11/the-perceptron.html)
- 
- [Activation Function](../mathematical/activation-function.md)
- [Understanding the Perceptron](https://www.bobbywlindsey.com/2019/10/06/understanding-the-perceptron/)
- [Perceptron Learning Rule Convergence Theorem](http://www.cs.ubbcluj.ro/~csatol/kozgaz_mestint/4_neuronhalo/PerceptConvProof.pdf)
- [Perceptrons - The Most Basic Form of a Neural Network](https://news.ycombinator.com/item?id=11890000)
- https://websites.umass.edu/brain-wars/1957-the-birth-of-cognitive-science/the-perceptron-a-perceiving-and-recognizing-automaton/
- 
- [‣](https://app.notion.com/p/ea1666a3efa04b3a8bb3005b488ba81c?pvs=21) [**The Perceptron Paper]**
- [‣](https://app.notion.com/p/608ca6c4622442a39d3cc59da46e823c?pvs=21) [Simulating in a Physical Computer of the Perceptron (McCulloch and Pitts Neuron)]
- [‣](https://app.notion.com/p/01e644a67f62465db34117013cbd9d24?pvs=21)
- [‣](https://app.notion.com/p/65416621ca894165a37955503ce841d7?pvs=21) [**The Book**]
- [‣](https://app.notion.com/p/f1a01c0740234e1792095e1998c930ee?pvs=21)
