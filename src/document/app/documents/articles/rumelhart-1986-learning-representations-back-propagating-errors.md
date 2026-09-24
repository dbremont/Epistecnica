---
tags: [ml, physical]
---

# Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. Nature, 323(6088), 533–536.


```bash
﻿@article{Rumelhart1986,
  author={Rumelhart, David E.
and Hinton, Geoffrey E.
and Williams, Ronald J.},
  title={Learning representations by back-propagating errors},
  journal={Nature},
  year={1986},
  month={Oct},
  day={01},
  volume={323},
  number={6088},
  pages={533-536},
  abstract={We describe a new learning procedure, back-propagation, for networks of neurone-like units. The procedure repeatedly adjusts the weights of the connections in the network so as to minimize a measure of the difference between the actual output vector of the net and the desired output vector. As a result of the weight adjustments, internal `hidden' units which are not part of the input or output come to represent important features of the task domain, and the regularities in the task are captured by the interactions of these units. The ability to create useful new features distinguishes back-propagation from earlier, simpler methods such as the perceptron-convergence procedure1.},
  issn={1476-4687},
  doi={10.1038/323533a0},
  url={https://doi.org/10.1038/323533a0}
}
```

## Notes

---

> This paper introduces the **back-propagation learning procedure,** adjusts the weights of the connections in the network to minimize the difference between the actual output vector of the network and the desired output vector.
> 

> An **efficient algorithm for computing gradients** of deeply composed functions by propagating error signals backward through the computational graph using the chain rule.
> 

QA:

- **How should backpropagation be conceptualized?** What is the correct mental model for understanding the backpropagation algorithm in neural networks?
    - It’s an **optimization method** - that takes a computation graph - over problem domain - and adjust the parameters in order to **optimize some quality metrics**.
    - …
- **Is the full derivative of the loss function computed?** Does backpropagation compute the entire derivative of the loss function with respect to all parameters, or only specific components such as gradients with respect to weights and biases?
- What is the **computational complexity** of the back prop method?
- **Why did similar methods already exist for optimizing composed functions?**
Several fields had related techniques before neural network backpropagation:
    - **1960s – Control Theory:** Adjoint state method
    - **1970s – Automatic Differentiation:** Reverse-mode differentiation
    - **Optimal Control:** Pontryagin’s Maximum Principle
    - **Numerical Optimization:** Finite-difference gradient estimation
    - …
- 
- **Why was backpropagation considered an innovation if related techniques already existed?**
What specific conceptual or algorithmic contribution made backpropagation important for neural network training?
- **What exactly were the innovations introduced by the backpropagation algorithm?**
For example:
    - Efficient gradient computation for multilayer networks
    - Reuse of intermediate derivatives
    - A recursive error-propagation formulation
- **What is a gradient?**
Formally, what does the gradient represent in the context of optimizing neural networks?
- Technical Observation Set (What can be said about )

Pass 1:

- Weight Adjustments
- Internal Representations → Hidden Units → Inner Features (Represent Regularities of the Input Vector)
- Internal Structure → Source Problem Representation Capability
- What do we mean by learning representations? Why does the perceptron does not learn representations?
- What do we mean by an active neuron? …
- In this paper; the error is computed wrt activations; then with this **info**;  …
- We need to store the previous weights?
- Why used the first and not the second derivative?
- What does the learning rate represents?
- What is “weight space”?
- Why initialize the network with **random weights**?
- Can we get stuck in **“weight space”**?
- Relation of  of weights;  internal units vs  local minima.
- …

```jsx
import math
import random
import json
import time

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

dataset = [
    ([0, 0], 0),
    ([1, 0], 0),
    ([0, 1], 0),
    ([1, 1], 1)
]

def rand():
    return random.uniform(-1, 1)

# Global State
latest_state = {}
STOP_REQUESTED = False # Flag for stopping

def train_network():
    global latest_state, STOP_REQUESTED
    
    # Initialize Weights
    w11, w12, w21, w22 = rand(), rand(), rand(), rand()
    v1, v2 = rand(), rand()
    b1, b2, b3 = rand(), rand(), rand()
    
    learning_rate = 0.5
    epochs = 20000 # Target epochs

    print(f"Training started. Connect via browser to monitor.")

    for epoch in range(epochs):
        # Check stop flag
        if STOP_REQUESTED:
            print("Training stop requested by user.")
            break

        total_loss = 0
        batch_predictions = []

        for inputs, y in dataset:
            x1, x2 = inputs[0], inputs[1]

            # FORWARD PASS
            z1 = w11 * x1 + w12 * x2 + b1
            a1 = sigmoid(z1)
            z2 = w21 * x1 + w22 * x2 + b2
            a2 = sigmoid(z2)
            z3 = v1 * a1 + v2 * a2 + b3
            y_hat = sigmoid(z3)

            # STORE PREDICTION
            batch_predictions.append({
                "input": inputs, "target": y, "output": y_hat
            })

            # LOSS
            loss = -(y * math.log(y_hat + 1e-9) + (1 - y) * math.log(1 - y_hat + 1e-9))
            total_loss += loss

            # BACKPROPAGATION
            delta3 = y_hat - y
            dv1, dv2, db3 = delta3 * a1, delta3 * a2, delta3
            
            delta1 = (v1 * delta3) * sigmoid_derivative(z1)
            delta2 = (v2 * delta3) * sigmoid_derivative(z2)

            dw11, dw12 = delta1 * x1, delta1 * x2
            dw21, dw22 = delta2 * x1, delta2 * x2
            db1, db2 = delta1, delta2

            # UPDATE WEIGHTS
            v1 -= learning_rate * dv1
            v2 -= learning_rate * dv2
            b3 -= learning_rate * db3
            w11 -= learning_rate * dw11
            w12 -= learning_rate * dw12
            w21 -= learning_rate * dw21
            w22 -= learning_rate * dw22
            b1 -= learning_rate * db1
            b2 -= learning_rate * db2

        # UPDATE GLOBAL STATE FOR SERVER
        latest_state = {
            "epoch": epoch,
            "loss": total_loss,
            "weights": {
                "w11": w11, "w12": w12, "w21": w21, "w22": w22,
                "v1": v1, "v2": v2
            },
            "predictions": batch_predictions
        }
        
        # Small delay to prevent CPU lock and make visualization smooth
        time.sleep(0.02)

    # Loop finished (either completed or stopped)
    if not STOP_REQUESTED:
        print("Training completed naturally.")
    else:
        # Send final state update to indicate stopped
        pass
    
# 2. Run Training
train_network()

```

## References

- https://github.com/dbremont/algorithms
- [‣](https://app.notion.com/p/18f5818ff49b4b478ddf8d3d67490a15?pvs=21)
- [‣](https://app.notion.com/p/18bc0f5171ec804ba2d7eb9d810107c2?pvs=21)
- https://en.wikipedia.org/wiki/Backpropagation
- https://en.wikipedia.org/wiki/Partial_derivative
- https://en.wikipedia.org/wiki/Adjoint_state_method
- https://en.wikipedia.org/wiki/Automatic_differentiation
- https://people.idsia.ch/~juergen/who-invented-backpropagation.html
- https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b
