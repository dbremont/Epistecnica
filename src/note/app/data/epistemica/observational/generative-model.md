# Generative Model


> **Generative models** generate instances by learning the **underlying distribution of the data** and then using that learned distribution to create new data points.
> 

> It encompasses **various ways** to represent and **understand how data is structured** and how different data points relate to one another.
> 

> Note: It represents the underlying data generation process.
> 

> Generative modeling is a subfield of machine learning focused on **learning the underlying probability distribution of data** to **generate new samples** that resemble the training data. It contrasts with **discriminative modeling** (which learns boundaries between classes) and **representation learning** (which extracts useful features).
> 

**Key Tasks:**

- **Generation** (e.g., creating fake faces with GANs).
- **Density estimation** (e.g., detecting anomalies by estimating p(x)p(x)).
- **Data imputation** (filling in missing values).
- **Conditional generation** (e.g., text-to-image models like DALL·E).

## Model

| **Generative Model** | **Description** | **Applications** | **Key Concepts** |
| --- | --- | --- | --- |
| **Generative Adversarial Networks (GANs)** | Consists of a generator and a discriminator that compete to improve data generation. | Image synthesis, data augmentation, style transfer. | Generator, Discriminator, Adversarial Training. |
| **Variational Autoencoders (VAEs)** | Uses an encoder to map data to a latent space and a decoder to reconstruct it, with a focus on learning distributions. | Image generation, anomaly detection, data imputation. | Encoder, Decoder, Latent Space, Variational Inference. |
| **Normalizing Flows** | Employs invertible transformations to map data from a simple distribution to a complex one. | Density estimation, data generation, probabilistic modeling. | Invertible Neural Networks, Change of Variables. |
| **Restricted Boltzmann Machines (RBMs)** | A type of stochastic neural network that learns a probability distribution over its set of inputs. | Dimensionality reduction, feature learning, collaborative filtering. | Hidden Units, Visible Units, Contrastive Divergence. |
| **Deep Belief Networks (DBNs)** | Stacked RBMs where each layer learns a representation of the input data. | Feature learning, unsupervised learning, pre-training. | Layer-wise Training, Greedy Layer-Wise Training. |
| **Autoregressive Models** | Models where each data point is generated based on previous data points in a sequence. | Sequential data generation, time series forecasting. | Autoregression, Conditional Distribution. |
| **Flow-based Models** | Use normalizing flows to model complex data distributions with tractable likelihoods. | Image generation, density modeling. | Invertible Transformations, Likelihood-Based Learning. |
| **PixelCNN/PixelSNAIL** | Generates images pixel by pixel, conditioned on previously generated pixels. | Image synthesis, texture generation. | Pixel-wise Generation, Convolutional Networks. |
| **Diffusion Models** | Generate data by iteratively denoising a noisy version of the data, learning the data distribution through noise removal. | Image generation, data synthesis. | Denoising Process, Score Matching. |
| **Energy-Based Models** | Defines a probability distribution through an energy function, learning to generate samples by minimizing energy. | Data generation, anomaly detection. | Energy Function, Markov Chains.\ |

## References

- https://en.wikipedia.org/wiki/Generative_model
