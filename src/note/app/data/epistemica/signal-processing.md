# Signal Processing

> **Signal and Systems**: how signals (data or information) are processed and transformed by systems.
> 

> A **signal** can be thought of as a dataset (a set of variables) representing a phenomenon, entity, or process, typically varying over time or space. It consists of measurements, either uni- or multi-dimensional, indexed by time or  space (maybe both ???).
> 

> **Signal processing** is the analysis, manipulation, and transformation of signals—such as audio, video, or sensor data—to improve, extract, or interpret useful information.
> 

> The problem domain of **signal processing** involves analyzing, transforming, and extracting useful information from signals to improve their interpretation, transmission, and storage across various applications.
> 

> Signal Processing (SP) is a collection of techniques developed over many years to analyze and manipulate signals collected by sensors. These techniques can be applied as standalone tools or integrated within complex systems to achieve real-time objectives.
> 

→ Sensor → Signal Processing → Store or Act.

## Areas

- Audio Processing
- Video Processing
- Image Processing
- Visualization
- Computer Graphics
- Imaging
- Sensing
- Human Computer Interactions
- GUI: Graphical User Interfaces
- …
- Related Areas
    - Acoustics
    - Optics
    - Neurosciences
- Math Modelling
- ML Models

## SP System

> A **signal processing system** is an entity or process that receives one or more signals as input and generates one or more signals as output, often by transforming or analyzing the input signals.
> 

System  Properties:

- **Linearity**: A property determining if a system’s output is a direct, proportional response to input.
- **Time-Invariance**: A system property where the response remains unchanged over time.
- **Causality**: Determines if a system’s output depends only on past and current inputs (not future inputs).
- **Stability**: Whether a bounded input results in a bounded output.

## Signal

List of examples:

- **Voltage signal**: Variations in voltage over time, used in electronics and communication systems.
- **Sound wave**: Variations in air pressure (acoustic signal) captured as audio in microphones, used in music, speech, and sound recognition.
- **Image signal**: A 2D signal where pixel intensity values represent the visual content of an image.
- **Electromagnetic wave**: A signal that propagates through space, such as AM/FM radio broadcasts or cellular signals.
- **ECG (Electrocardiogram) signal**: Electrical signals produced by the heart, used for monitoring heart activity.
- **Temperature signal**: Variation in temperature measured by sensors, used in climate monitoring, weather forecasting, and industrial processes.
- **Light signal**: Light intensity variations, often used in fiber-optic communication or visual displays.
- **Pulse-width modulation (PWM) signal**: A type of signal used in control systems to regulate power delivered to electrical devices.
- **Feedback signal**: A signal that is used to adjust the behavior of a system based on its output.
- **Clock signal**: A time-based signal used to synchronize circuits in digital systems.
- **Seismic wave**: Ground vibrations caused by earthquakes or explosions, measured by seismographs to study the Earth's subsurface.
- **Market price signal**: Fluctuations in the price of goods or assets in an economy, used to indicate demand, supply, and market trends.
- **Wind signal**: Variations in wind speed and direction, used in meteorology for forecasting and climate studies.

## SP Tasks & Processing Methods

> 

| **Task** | **Description** |
| --- | --- |
| **Filtering** | Removing unwanted components or enhancing specific features of a signal. |
| **Transformation** | Conversion of signal properties or format, often from time domain to frequency domain. |
| **Compression** | Reducing the size of a signal for efficient storage or transmission while retaining important data. |
| **Modulation** | Encoding information onto a carrier signal by varying a property such as amplitude or frequency. |
| **Sampling and Quantization** | Converting continuous signals to discrete form, enabling digital processing. |
| **Noise Reduction** | Minimizing noise in a signal without distorting its original content. |
| **Signal Reconstruction** | Rebuilding a signal from sampled or compressed data. |
| **Feature Extraction** | Identifying and extracting important patterns or features from a signal. |
| **Signal Detection** | Identifying the presence of specific signals or patterns in a noisy environment. |
| **Data Transmission** | Encoding and decoding signals for transmission, often with error correction. |
| **Speech Recognition** | Converting spoken language into text or identifying speech patterns for commands. |
| **Speech Synthesis** | Generating human-like speech from text or other data. |
| **Echo Cancellation** | Removing unwanted echoes from a signal, commonly used in telecommunications. |
| **Channel Equalization** | Adjusting signals to compensate for distortions or impairments in the transmission medium. |
| **Signal Analysis** | Studying the properties and characteristics of a signal, including amplitude and frequency. |
| **Speech Enhancement** | Improving the quality of speech signals, especially in noisy environments. |
| **Time Domain Analysis** | Analyzing signals based on how they change over time. |
| **Pattern Recognition** | Identifying and classifying patterns within a signal based on criteria or models. |

## Mathematical & Statistical Tools for SP

> 

| **Tool** | **Description** | **Example** |
| --- | --- | --- |
| **Fourier Transform** | A mathematical transform that decomposes a signal into its constituent frequencies. | Used for converting a time-domain signal into the frequency domain to analyze its frequency components. |
| **Discrete Fourier Transform (DFT)** | A numerical method for calculating the Fourier Transform for discrete signals. | Used in digital signal processing to analyze the frequency content of discrete-time signals. |
| **Fast Fourier Transform (FFT)** | An efficient algorithm to compute the DFT, reducing computation time. | Widely used in audio, image, and communications systems for frequency analysis. |
| **Convolution** | A mathematical operation used to combine two signals, often used for filtering and system analysis. | Used in filtering, where one signal is passed through a system defined by another signal (e.g., filter impulse response). |
| **Cross-Correlation** | A statistical tool that measures the similarity between two signals as a function of time lag. | Used for signal detection, pattern recognition, or to find the time delay between two signals. |
| **Auto-Correlation** | A measure of similarity of a signal with a delayed version of itself. | Used to analyze periodicity in signals, like detecting repetitive patterns in audio or vibration signals. |
| **Wavelet Transform** | A transform used to analyze signals at multiple scales or resolutions. | Used in image compression, signal denoising, and multi-resolution analysis. |
| **Principal Component Analysis (PCA)** | A statistical method for reducing the dimensionality of a signal while retaining most of its variance. | Used in feature extraction, signal compression, and noise reduction. |
| **Kalman Filter** | A recursive algorithm for estimating the state of a dynamic system from noisy measurements. | Used in real-time applications like tracking and navigation. |
| **Wiener Filter** | A filter designed to minimize the mean square error between the estimated and true signal. | Used for noise reduction in signals, especially in communications and image processing. |
| **Linear Regression** | A statistical method for modeling the relationship between a dependent variable and one or more independent variables. | Used in signal prediction or approximation when modeling the relationship between signal components. |
| **Bayesian Inference** | A method of statistical inference that updates the probability of a hypothesis based on new evidence. | Applied in filtering, speech recognition, and adaptive signal processing. |
| **Maximum Likelihood Estimation (MLE)** | A statistical method for estimating parameters of a model that maximizes the likelihood of observed data. | Used for parameter estimation in signal models, such as determining the optimal filter parameters. |
| **Least Squares Optimization** | A mathematical method used to minimize the sum of squared differences between observed and model-predicted values. | Used in signal fitting, system identification, and estimation problems. |
| **Statistical Moments** | Mathematical descriptors of a signal’s distribution, including mean, variance, skewness, and kurtosis. | Used for signal classification and feature extraction in data analysis and machine learning applications. |
| **Empirical Mode Decomposition (EMD)** | A data-driven technique for decomposing a signal into intrinsic mode functions (IMFs) without relying on prior assumptions. | Used for analyzing non-linear and non-stationary signals, such as in biomedical signal processing. |

## Case Studies

> 

| **Application** | **Signal Processing Role** | **Description** |
| --- | --- | --- |
| **Smartphone Audio** | Noise reduction, echo cancellation | DSP filters out background noise and echo during calls for clearer audio. |
| **Medical ECG Monitoring** | Filtering, feature extraction | Removes baseline wander/noise, detects QRS complexes for heart rate analysis. |
| **Wireless Communication (4G/5G)** | Modulation, channel equalization, error correction | Processes and recovers signals over noisy wireless channels. |
| **Vibration Analysis in Motors** | FFT, envelope analysis | Detects bearing faults, imbalance, and misalignment from vibration patterns. |
| **Autonomous Vehicles (LIDAR)** | Signal reconstruction, filtering, object detection | Processes point clouds and reflects to build 3D maps and detect obstacles. |
| **Speech Recognition (Siri/Alexa)** | MFCC feature extraction, pre-emphasis filtering | Prepares audio signals for accurate voice model input and recognition. |
| **Seismic Exploration** | Deconvolution, wavelet transform | Extracts subsurface structures by processing reflected seismic waves. |
| **MRI Imaging** | Fourier transform, image reconstruction | Converts raw k-space data into interpretable 2D/3D medical images. |
| **Digital Cameras / Phones** | Demosaicing, noise reduction, sharpening | Enhances image quality through pixel-level signal manipulation. |
| **Industrial IoT Sensors** | Time-series filtering, anomaly detection | Cleans and monitors real-time sensor data for faults or abnormal behavior. |

## Conceptual Model

Signal Processing: Conceptual Model

## References

- …
