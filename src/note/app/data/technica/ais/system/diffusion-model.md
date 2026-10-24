---
tags: [probability, process-representation]
---

# Diffusion Model

 : Diffusion Process (Diffusion%20Process%201bcc0f5171ec8043a87ae030be395a30.md)

> A **diffusion model** is a class of generative probabilistic models that parameterize the reverse of a predefined **stochastic diffusion process**, typically a Markov chain, which iteratively transforms a **simple prior distribution** (e.g., Gaussian noise) into a structured **data distribution** by learning the **score function** or **transition probabilities** via **variational inference** or **denoising score matching**.
> 

QA:

- How to represent data using probability?
- What it is an structure data distribution?

## A Definition Deep Dive

Breviarium:

- **Diffusion Process:** Gradually adds noise to the latent representation of an image.
- **Markov Chain:** Forward diffusion follows a Markov process.
- **Prior Distribution:** Starts from Gaussian noise.
- **Reverse Process:** Learned using a UNet trained to estimate noise.
- **Inference:** Runs the reverse process to generate high-quality images from noise.
- **Optimization:** Trained via denoising score matching and ELBO minimization.

### **1. "A diffusion model is a class of generative probabilistic models that parameterize the reverse of a predefined stochastic diffusion process, typically a Markov chain..."**

- In Stable Diffusion, the predefined stochastic diffusion process is **the forward diffusion process** where Gaussian noise is **gradually added** to the latent representation of an image across discrete timesteps tt.
- This process follows a **Markov chain**, meaning each step depends only on the previous one:
    
    q(zt∣zt−1)=N(zt;αtzt−1,(1−αt)I)q(z_t | z_{t-1}) = \mathcal{N}(z_t; \sqrt{\alpha_t} z_{t-1}, (1 - \alpha_t) I)
    

### **2. "...which iteratively transforms a simple prior distribution (e.g., Gaussian noise) into a structured data distribution..."**

- The prior distribution in Stable Diffusion is a **Gaussian noise distribution** in latent space.
- The goal of training is to learn how to **reverse this noise process** to reconstruct structured image representations.
- At inference time, we **sample Gaussian noise** and apply the learned reverse process to transform it into an image.

### **3. "...by learning the score function or transition probabilities..."**

- Stable Diffusion learns to **approximate the score function** (gradient of the log-likelihood of the data) using a **UNet-based deep neural network**.
- Instead of modeling explicit transition probabilities, the model is trained to predict the **noise added at each step** so that it can remove it in the reverse process.

### **4. "...via variational inference or denoising score matching."**

- The model is trained using **denoising score matching**, which minimizes the difference between real and predicted noise at each step:
    
    L=Ezt,ϵ[∣∣ϵ−ϵθ(zt,t,c)∣∣2]L = \mathbb{E}_{z_t, \epsilon} \left[ || \epsilon - \epsilon_\theta(z_t, t, c) ||^2 \right]
    
    where ϵθ\epsilon_\theta is the noise estimator (UNet), and cc is the conditioning input (text embedding from CLIP).
    
- This is equivalent to a **variational inference approach**, as it optimizes the **Evidence Lower Bound (ELBO)** to approximate the true data distribution.

---

## Uses

Diffusion models have numerous applications across various domains, including:

1. **Image Generation & Editing** – Used in generative AI (e.g., DALL·E, Stable Diffusion) to create high-quality images from text prompts or modify existing images.
2. **Video Synthesis** – Generating and interpolating realistic video sequences by modeling temporal dependencies.
3. **Speech Synthesis & Enhancement** – Applied in text-to-speech (TTS) and noise reduction by modeling clean speech from noisy inputs.
4. **Molecular & Drug Design** – Predicting molecular structures and simulating protein folding via generative chemistry.
5. **Anomaly Detection** – Identifying deviations in data distributions, useful in cybersecurity and medical diagnostics.
6. **Super-Resolution & Image Inpainting** – Enhancing low-resolution images or filling in missing regions using learned probability distributions.
7. **Text Generation & Code Completion** – Though less common than transformers, some experimental applications explore natural language modeling.
8. **Reinforcement Learning & Planning** – Modeling state transitions for planning in robotics and decision-making tasks.

## References

- https://en.wikipedia.org/wiki/Diffusion_model
- https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
- https://blog.christianperone.com/2023/09/thoughts-on-riemannian-metrics-and-its-connection-with-diffusion-score-matching-part-i/
- https://diffusion.csail.mit.edu/
- [Diffusion](https://app.notion.com/p/Diffusion-25144b9280f040f09b63a3c1267524a7?pvs=21)
- https://arxiv.org/html/2312.10393v1
- 
- https://diffusion.csail.mit.edu/
