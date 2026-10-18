---
tags: [process-representation]
---

# Generative Adversarial Network (GAN)


## Generate Without Input

A generative model can generate images without a prompt using unsupervised learning techniques such as Generative Adversarial Networks (**GANs**) or Variational Autoencoders (**VAEs**).

In these models, the generative network is trained on a large dataset of images, such as ImageNet or CIFAR, and learns to generate new images based on the patterns and features it observes in the training data. During the training process, the model is not given any specific input or prompt, but rather is trained to generate images that resemble those in the training set.

Once the model has been trained, it can generate new images by sampling from the **latent space of the model**, which is a **low-dimensional representation** of the input images that captures the key features and patterns in the data. By sampling from this latent space and passing the resulting values through the generative network, the model can generate new, never-before-seen images that resemble those in the training set.

It’s worth noting that while a generative model can generate images without a prompt, the quality and diversity of the generated images may vary depending on the complexity and diversity of the training data, as well as the architecture and hyperparameters of the model.

## References

- Lantao Yu, et al.: SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient, AAAI 2017.
- [Generative Adversarial Network](https://en.wikipedia.org/wiki/Generative_adversarial_network)
