# Computational Learning System


> A machine learning (ML) system uses machine learning algorithms and statistical models to analyze and learn from data. It typically involves processes and tools for collecting, cleaning, and preparing data, training and evaluating machine learning models, and deploying them to make predictions or decisions based on new data.
> 

> **ML Systems** can be used in various applications, such as image recognition, natural language processing, fraud detection, recommendation systems, and autonomous vehicles. Depending on the specific requirements and goals of the project, these systems can be built using various programming languages, frameworks, and tools.
> 

![image.png](data/technica/computation/miscelanea/assets/computational-learning-system/image.png)

![image.png](data/technica/computation/miscelanea/assets/computational-learning-system/image-1.png)

![image.png](data/technica/computation/miscelanea/assets/computational-learning-system/image-2.png)

![image.png](data/technica/computation/miscelanea/assets/computational-learning-system/image-3.png)

![image.png](data/technica/computation/miscelanea/assets/computational-learning-system/image-4.png)

## **Machine Learning (ML) Project**

- Given I Data set X; and an Statement Y?
    - How can you compute the quantity of information that Y provides about X?
    - Example: I a data set from Dominican Republic;  saying tha tthe average person in the dataset is dominican; does add any information.
- How test and control for overfiting?
- ML Projects
    - Data → Eda
    - Models
    - Testing
    - Overfitting Test
    - Insighits
        - Evaluate the Quality of the Insights`
    - Proposals On Those Insights
- …

## ML Workload Taxonomy

> 

| **Category** | **Subcategory** | **Description** |
| --- | --- | --- |
| **Supervised Learning** | Classification | Assigns labels to input data (e.g., spam detection, image recognition). |
|  | Regression | Predicts continuous values (e.g., stock prices, weather forecasting). |
|  | Sequence Modeling | Learns from sequential data (e.g., speech recognition, time-series forecasting). |
| **Unsupervised Learning** | Clustering | Groups similar data points (e.g., K-Means, DBSCAN, hierarchical clustering). |
|  | Dimensionality Reduction | Reduces data complexity while preserving important features (e.g., PCA, t-SNE). |
|  | Anomaly Detection | Identifies rare events or outliers (e.g., fraud detection, network intrusion detection). |
| **Self-Supervised Learning** | Contrastive Learning | Learns representations by comparing positive and negative samples (e.g., SimCLR, MoCo). |
|  | Masked Prediction | Predicts missing parts of input data (e.g., BERT for NLP, MAE for vision). |
| **Reinforcement Learning** | Model-Free RL | Learns actions via trial and error without a predefined model (e.g., Q-Learning, DDPG). |
|  | Model-Based RL | Builds an internal model of the environment to improve learning efficiency. |
|  | Multi-Agent RL | Trains multiple agents interacting in the same environment (e.g., autonomous driving, game AI). |
| **Deep Learning** | Convolutional Neural Networks (CNNs) | Processes grid-like data, such as images (e.g., ResNet, EfficientNet). |
|  | Recurrent Neural Networks (RNNs) | Processes sequential data (e.g., LSTMs, GRUs for speech and time-series). |
|  | Transformers | Uses self-attention mechanisms for NLP and vision tasks (e.g., BERT, GPT, ViTs). |
|  | Generative Models | Generates new data similar to training data (e.g., GANs, VAEs, diffusion models). |
| **AI for Specific Domains** | Natural Language Processing (NLP) | Works with text data for tasks like translation, summarization, and sentiment analysis. |
|  | Computer Vision | Processes visual data for object detection, segmentation, and recognition. |
|  | Speech & Audio Processing | Handles voice recognition, speech synthesis, and audio enhancement. |
|  | Recommender Systems | Provides personalized recommendations (e.g., collaborative filtering, deep learning-based models). |
| **Computational Characteristics** | Compute-Intensive | Requires significant processing power (e.g., deep learning training). |
|  | Memory-Intensive | Uses large amounts of RAM for high-dimensional data (e.g., transformer models). |
|  | Latency-Sensitive | Requires real-time inference (e.g., voice assistants, autonomous driving). |
|  | Parallelism-Oriented | Benefits from GPU acceleration for training and inference. |
| **Hardware Target** | CPU Processing | Suitable for small-scale ML tasks and traditional ML models. |
|  | GPU Processing | Optimized for deep learning training and large-scale inference. |
|  | Edge/Embedded Processing | Runs ML models on IoT and mobile devices with low power consumption. |
|  | Cloud-Based Processing | Utilizes cloud infrastructure for scalable training and inference. |

## Software Stack

> See more in [A Guide to ML Infrastructure Tooling](https://app.notion.com/p/A-Guide-to-ML-Infrastructure-Tooling-224c0f5171ec80638a20ed18642cf12f?pvs=21).
> 

| **Layer** | **Function** | **Key Tools / Frameworks** | **Notes** |
| --- | --- | --- | --- |
| **Data Ingestion** | Load and stream data from various sources | Apache Kafka, Apache NiFi, Flink, Airbyte, AWS Kinesis | Connects to DBs, filesystems, APIs |
| **Data Storage** | Store structured/unstructured data | HDFS, S3, Delta Lake, BigQuery, PostgreSQL | Supports both offline and online pipelines |
| **Data Processing & Feature Engineering** | Transform and prepare features | Pandas, Dask, Spark, DBT, Featuretools, Feast | Can be batch or real-time |
| **Feature Store** | Centralized feature management | Feast, Tecton, Vertex AI Feature Store | Ensures feature consistency between training and inference |
| **Model Development** | Define and prototype ML models | PyTorch, TensorFlow, JAX, scikit-learn, HuggingFace Transformers | Often coupled with notebooks like Jupyter or Colab |
| **Model Training** | Train models at scale | PyTorch Lightning, TensorFlow, XGBoost, Ray, Horovod, SageMaker | May use distributed training or accelerators (GPUs/TPUs) |
| **Experiment Tracking** | Track model versions and metrics | MLflow, Weights & Biases, Neptune.ai, Comet.ml | Essential for reproducibility and collaboration |
| **Model Evaluation & Testing** | Validate model performance | Great Expectations, Evidently AI, Deepchecks | Includes fairness, robustness, and unit tests |
| **Model Packaging** | Prepare model for deployment | ONNX, TorchScript, Docker, BentoML | Model serialization and environment capture |
| **Model Serving** | Real-time or batch inference | TensorFlow Serving, TorchServe, Triton, Seldon Core, BentoML, FastAPI | Supports REST/gRPC and scalable deployment |
| **Model Orchestration** | Workflow automation and scheduling | Airflow, Kubeflow Pipelines, Metaflow, Prefect, Dagster | Manages end-to-end ML pipelines |
| **Model Monitoring** | Track drift, performance, and issues | Arize AI, Fiddler, WhyLabs, Prometheus + Grafana | Monitors for data/model drift, latency, accuracy |
| **Model Management** | Lifecycle and registry | MLflow Model Registry, SageMaker Model Registry, KServe | Track, version, stage, and deploy models |
| **Infrastructure & Ops** | Underlying compute environment | Kubernetes, Docker, Terraform, Ray, Kubeflow | Supports scaling, reproducibility, CI/CD |
| **Security & Governance** | Permissions, privacy, compliance | Vault, OPA, GDPR Tools, data lineage tracking | Especially important in regulated environments |
| Model Optimization & Compilation | ML Compiler / Optimizer | - Converts trained models (e.g., from PyTorch, TensorFlow) into optimized, target-specific code
- Applies kernel fusion, quantization, and auto-tuning
- Generates deployable binaries for CPU, GPU, FPGA, microcontrollers | - XLA (TensorFlow/JAX)- ONNX Runtime + Graph Optimizer- Glow- IREE- TensorRT- OpenVINO |
| Model Registry |  |  |  |
| CI/CD for ML (MLOps) |  |  |  |

## Case Studies

> 
- Intelligent assistants,
- Recommender Systems
- …

## References

- https://en.wikipedia.org/wiki/Machine_learning