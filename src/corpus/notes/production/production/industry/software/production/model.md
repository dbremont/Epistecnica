---
tags: [note, production]
---

# Model Production  

> **How to Produce Software 2.0 (Model)?**

## Formulation  

> **What is Software 2.0 (Model)?**

Software 2.0 refers to systems where behavior is **not explicitly programmed** but **learned from data** using statistical or neural models. Instead of writing rules, engineers curate datasets, define architectures, and train models whose weights encode the program logic. Examples include large language models, vision systems, recommendation engines, and predictive maintenance models.

## Task Space  

> **Which tasks (problems) are handled in the Technical Domain?**

| **Category** | **Task** | **Description** |
|--------------|--------|----------------|
| **Problem Specification** | Task Framing | Translate business or scientific goals into ML-digestible objectives (e.g., classification, regression, generation). |
| **Data Engineering** | Data Acquisition | Collect, license, or generate raw data relevant to the task. |
| | Data Curation | Clean, label, augment, and version datasets. |
| | Data Validation | Detect schema drift, missing values, outliers, or bias. |
| **Model Engineering** | Architecture Selection | Choose or design neural/network topology (e.g., Transformer, ResNet). |
| | Training Strategy | Define optimization objectives, loss functions, regularization. |
| | Hyperparameter Tuning | Optimize learning rate, batch size, etc., via search or heuristics. |
| **Evaluation & Validation** | Offline Evaluation | Measure performance on held-out data (accuracy, F1, AUC, perplexity, etc.). |
| | Robustness Testing | Evaluate under distribution shift, adversarial inputs, or edge cases. |
| | Bias/Fairness Auditing | Assess demographic or behavioral disparities. |
| **Deployment & Serving** | Model Packaging | Serialize model (e.g., ONNX, TorchScript) with dependencies. |
| | Inference Optimization | Apply quantization, distillation, or compilation (e.g., TensorRT). |
| | API & Integration | Wrap model in service (e.g., REST/gRPC) compatible with product stack. |
| **Monitoring & Maintenance** | Performance Monitoring | Track latency, throughput, error rates in production. |
| | Data/Concept Drift Detection | Monitor input distribution shifts over time. |
| | Retraining Triggering | Automate or schedule model updates based on metrics. |

## Technique Space  

> **Methods or techniques used to address tasks.**

| **Category** | **Technique Type** | **Technique** | **Description** |
|--------------|-------------------|-------------|----------------|
| **Data** | Labeling | Active Learning | Query informative samples for human labeling to reduce cost. |
| | | Weak Supervision | Use heuristics, rules, or distant supervision to generate noisy labels. |
| | Augmentation | Domain Randomization | Synthetically vary inputs (e.g., lighting, noise) to improve generalization. |
| **Modeling** | Architecture | Transformer | Self-attention-based architecture for sequence modeling. |
| | | Diffusion Models | Generative models using iterative denoising. |
| | Training | Contrastive Learning | Learn representations by pulling similar samples together and pushing dissimilar apart. |
| | | Federated Learning | Train models across decentralized devices while preserving privacy. |
| **Optimization** | Search | Bayesian Optimization | Efficient hyperparameter search using probabilistic models. |
| | Pruning | Structured Pruning | Remove channels or layers to reduce model size. |
| **Evaluation** | Metrics | Calibration | Measure confidence vs. accuracy alignment (e.g., ECE). |
| | Testing | Counterfactual Testing | Evaluate model behavior under minimal perturbations. |
| **Deployment** | Serving | Model Batching | Combine multiple requests to improve GPU utilization. |
| | | Canary Deployment | Gradually route traffic to new model versions. |

## Constitutive Technical Object

> **Objects forming parts of the final product, ranging from merely integrated components to fully constitutive elements.**

| **Category**              | **Constitutive Technical Object** | **Description**                                                                 | **Tags**                          |
|--------------------------|----------------------------------|----------------------------------------------------------------------------------|-----------------------------------|
| **Model Artifacts**      | Trained Weights                  | Numeric parameters (e.g., `.pt`, `.h5`) encoding learned behavior.               | `#model` `#artifact`             |
|                          | Model Card                       | Structured documentation of model intent, performance, limitations, and ethics.  | `#governance` `#transparency`    |
| **Data Assets**          | Training Dataset                 | Curated, versioned dataset used for model fitting.                              | `#data` `#lineage`               |
|                          | Feature Schema                   | Specification of input/output feature types, shapes, and valid value ranges.     | `#interface` `#contract`         |
| **Code Components**      | Inference Script                 | Code that loads the model and executes predictions.                             | `#serving` `#runtime`            |
|                          | Pre/Post-processing Logic        | Functions for tokenization, normalization, decoding, or output formatting.       | `#pipeline` `#integration`       |
| **Runtime & Operation**  | Inference Runtime                | Execution environment (e.g., ONNX Runtime, TorchServe, TensorFlow Serving).      | `#serving` `#latency`            |
|                          | Observability Stack              | Monitoring tools (e.g., Prometheus/Grafana for metrics; Evidently/Arize for drift). | `#monitoring` `#reliability`  |
| **Product-Level Objects**| API Contract                     | Formal specification of model service interface (e.g., OpenAPI/Swagger schema).  | `#integration` `#contract`       |

## Production Technical Object (Capital Good)

> **Objects used in the production process.**

| **Category** | **Production Technical Object** | **Description** | **Tags** |
|--------------|-------------------------------|----------------|--------|
| Compute Infrastructure | GPU/TPU Clusters | Hardware accelerators for training/inference. | #compute #scale |
| | Kubernetes/Serverless | Orchestration platforms for model deployment. | #infra #cloud |
| Tooling | ML Pipeline Frameworks | Tools like Kubeflow, TFX, or Metaflow for workflow automation. | #mlops #automation |
| | Feature Stores | Centralized repositories for reusable, versioned features (e.g., Feast, Tecton). | #data #reusability |
| | Experiment Trackers | Systems like MLflow or Weights & Biases to log runs. | #reproducibility #debugging |

## Evaluation Criteria

> **How do we evaluate Success?**

| **Category** | **Criterion** | **Description** |
|--------------|--------------|----------------|
| **Technical Performance** | Predictive Accuracy | Task-specific metric (e.g., BLEU, mAP, RMSE) on validation sets. |
| | Latency & Throughput | Inference speed and requests/sec under load. |
| **Robustness** | Distributional Robustness | Performance on out-of-domain or adversarial examples. |
| | Failure Modes | Frequency and severity of incorrect/confident predictions. |
| **Operational** | Deployment Reliability | Uptime, error rate, rollback frequency. |
| | Retraining Efficiency | Time/cost to refresh model with new data. |
| **Ethical & Compliance** | Fairness | Statistical parity across subgroups. |
| | Explainability | Ability to justify predictions (e.g., SHAP, LIME). |
| | Regulatory Alignment | Compliance with GDPR, AI Act, etc. |

## Sociotechnical Organization  

> **Which sociotechnical organizations are involved in the production process?**

Software 2.0 production requires tight coupling between data scientists, ML engineers, DevOps/SREs, domain experts, compliance officers, and product managers. Coordination is mediated through shared tooling, review processes, and iterative feedback loops between offline and online performance.

### Organizational Model  

| **Organizational Model** | **Description** | **Structure** | **Evaluation** |
|--------------------------|----------------|--------------|---------------|
| **ML Platform Team + Embedded Practitioners** | Centralized ML platform provides tooling; domain teams build models. | Platform team (infra, tooling) + product-aligned ML squads (data, modeling, evaluation). | High reuse, consistent standards; risk of platform bottleneck if not well-staffed. |
| **Full-Stack ML Team** | Cross-functional team owns data → model → serving → monitoring. | Integrated squad with data engineers, ML engineers, SREs, product owner. | Fast iteration, strong ownership; may duplicate effort across teams. |

### Organizational Structure  

| **Structure Model** | **Description** | **Structure** | **Evaluation** |
|---------------------|----------------|--------------|---------------|
| **Hybrid (Platform + Product Pods)** | Combines centralized platform with decentralized execution. | Platform team maintains feature store, training infra, monitoring. Product pods own task-specific pipelines. Clear API contracts between layers. | Scalable, balances standardization and agility. Requires strong interface governance. |
| **Modular Data & Model Factories** | Specialized units for data curation, model training, and validation as services. | Data factory → Model factory → Validation gate → Deployment unit. | Efficient for high-volume model production (e.g., recommendation systems). Less flexible for R&D. |

### Role Space  

| **Category** | **Role** | **Description** |
|--------------|--------|----------------|
| **Operational** | ML Engineer | Designs training/serving pipelines, optimizes inference, ensures reliability. Interfaces with SREs. |
| | SRE / MLOps Engineer | Maintains model monitoring, CI/CD, incident response for ML services. |
| **Technical Experts** | Research Scientist | Develops novel architectures or training methods; often upstream of production. |
| | Data Engineer | Builds data pipelines, maintains feature stores, ensures data quality. |
| **Integrators** | ML Product Manager | Translates business needs into ML requirements; prioritizes trade-offs (latency vs. accuracy). |
| **Safety & Compliance** | AI Ethicist / Auditor | Reviews models for bias, fairness, and regulatory risk. |
| | Compliance Officer | Ensures adherence to legal frameworks (e.g., EU AI Act). |
| **Knowledge Custodians** | ML Architect | Defines system-wide standards (e.g., model format, logging schema). Maintains technical vision. |
| | Documentation Specialist | Authors model cards, data sheets, and operational runbooks. |

## References  

- Karpathy, A. (2017). *Software 2.0*. [https://karpathy.medium.com/software-2-0-a641f2d11d8](https://karpathy.medium.com/software-2-0-a641f2d11d8)  
- Sculley, D. et al. (2015). *Hidden Technical Debt in Machine Learning Systems*. NeurIPS.  
- Mitchell, M. et al. (2019). *Model Cards for Model Reporting*. ACM FAT*.  
- Google. (2023). *MLOps: Continuous Delivery and Automation Pipelines in Machine Learning*.  
- EU AI Act (2024). Regulatory framework for high-risk AI systems.  
- Software Technology
- Technology

- https://lovable.dev/
- https://www.bremontix.xyz/lab/pro/Production/Industry/Software/
- https://bigideasdb.com/
- https://leadsnipe.io/
- https://www.reddit.com/r/micro_saas/
- [An Essay On Personal Programming Workflow](https://www.notion.so/An-Essay-On-Personal-Programming-Workflow-162c0f5171ec80378c25e846231dad0f?pvs=21)
- [Learning System](https://www.notion.so/Learning-System-248c0f5171ec80a692d2ee54ee4fe677?pvs=21)
- https://github.com/janhq/jan?tab=readme-ov-file
- [Platform](https://www.notion.so/Platform-2c3c0f5171ec80b38a7ac3bd6045cc63?pvs=21)
- [Cloud Computing System](https://www.notion.so/Cloud-Computing-System-16ac0f5171ec80ca9211fe13955c602c?pvs=21)
- https://www.reddit.com/r/LocalLLaMA/comments/1phcnyt/vllm_supports_the_new_glm46v_and_glm46vflash/
- https://www.foundertoolkit.org/#pricing
- https://www.specode.ai/
- https://github.com/karpathy/nanochat?tab=readme-ov-file “…”
- https://www.reddit.com/r/LocalLLaMA/comments/1pigb3i/deepseekv32reap_508b_and_345b_checkpoints/
- https://agents.md/