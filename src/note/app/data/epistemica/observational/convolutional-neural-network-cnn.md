---
tags: [learning-system, neural-network-learning-system]
---

# Convolutional Neural Network (CNN)


A [**Convolutional Neural Network (CNN)**](https://en.wikipedia.org/wiki/Convolutional_neural_network) is a type of deep neural network that is specifically designed for processing data with a grid-like structure, such as images or videos. CNNs are widely used in computer vision applications, such as object detection and recognition, image segmentation, and facial recognition.

The key feature of a **CNN** is the use of convolutional layers. These layers apply a set of learnable filters (also known as **kernels**) to the input image or feature map, computing a set of activations known as feature maps. Each filter is designed to detect a particular pattern or feature in the input, such as edges, curves, or corners. By using multiple filters, the CNN can learn to detect increasingly complex features in the input image.

After the **convolutional layers**, the output is typically passed through one or more pooling layers. These layers reduce the spatial dimensionality of the feature maps by subsampling or max-pooling, while preserving the most salient features. This helps to reduce the computational complexity of the network and prevent overfitting.

Finally, the output of the **pooling layers** is passed through one or more fully connected layers, which perform a nonlinear mapping from the high-level feature representations to the desired output (e.g., a classification label).

One of the key advantages of **CNNs** is their ability to learn hierarchical representations of the input, with each layer detecting increasingly complex and abstract features. This makes CNNs particularly effective for tasks such as object recognition, where the network must learn to identify objects based on their local features and their global context in the image.

**CNNs** are typically trained using stochastic gradient descent with backpropagation, a variant of the gradient descent algorithm that computes the gradients of the loss function with respect to the network parameters and updates them accordingly. With sufficient training data and computational resources, CNNs can achieve state-of-the-art performance on a wide range of computer vision tasks.

## References

- Jonas Gehring, et al.: Convolutional Sequence to Sequence Learning, 2017.
- Nal Kalchbrenner, Edward Grefenstette, Phil Blunsom. A Convolutional Neural Network for Modelling Sentences. ACL2014. [pdf]
- [Convolutional Neural Network](https://www.wikiwand.com/en/Convolutional_neural_network)
