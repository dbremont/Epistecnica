# Computer Vision

- [Computer Graphics](note.html?n=technica/computation/miscelanea/computer-graphics.md)

> Computer Vision is the praxis of interpreting and understanding visual information from the physical world through computational systems, integrating methods from image processing, pattern recognition, machine learning, and artificial intelligence to enable automated perception, reasoning, and decision-making based on visual data.
> 

## Formulation

> What is Computer  Vision? What is the scope of Computer Vision? Which are the related techniques?
> 

> **Computer Vision (CV)** is the interdisciplinary field concerned with enabling machines to acquire, process, analyze, and interpret **visual data from the real world**, with the aim of producing meaningful information or taking automated actions. Its **scope includes understanding** images, video, 3D environments, and multi-modal visual data. CV leverages techniques from **image processing, machine learning, pattern recognition, computer graphics, and signal processing**.
> 

**Scope of Computer Vision:**

- Image understanding (object detection, recognition, segmentation)
- Video analysis (motion tracking, activity recognition)
- 3D vision (depth estimation, reconstruction)
- Scene understanding (semantic and contextual analysis)
- Multimodal perception (combining visual with other sensory data, e.g., LiDAR, infrared)

**Related Techniques:**

- Image filtering and enhancement
- Feature extraction and matching
- Deep learning for vision tasks (CNNs, Transformers)
- Geometric computer vision (epipolar geometry, structure from motion)
- Sensor fusion and multimodal data analysis

## Task Space

| Category | Task | Description |
| --- | --- | --- |
| **Low-Level Vision** | Image Enhancement | Improve image quality, reduce noise, enhance contrast or color fidelity. |
| **Low-Level Vision** | Edge / Feature Detection | Detect boundaries, corners, keypoints for subsequent analysis. |
| **Mid-Level Vision** | Segmentation | Partition an image into meaningful regions (object vs. background, instance segmentation). |
| **Mid-Level Vision** | Object Detection | Identify and localize objects of interest within images or videos. |
| **High-Level Vision** | Recognition / Classification | Assign semantic labels to objects, scenes, or patterns. |
| **High-Level Vision** | Tracking | Follow objects across frames in video sequences. |
| **High-Level Vision** | 3D Reconstruction | Reconstruct 3D shape, structure, or environment from 2D images or multi-view data. |
| **High-Level Vision** | Scene Understanding | Understand context, interactions, and spatial relationships in a scene. |
| **High-Level Vision** | Action (Gesture Recognition) | Detect and classify movements or activities in video streams. |

## Technique Space

| **Category** | **Technique** | **Description** |
| --- | --- | --- |
| **Image Processing (Low-Level)** | Filtering | Convolution, smoothing, Gaussian blur, median filtering for noise reduction. |
|  | Edge Detection | Sobel, Canny, Prewitt for detecting image boundaries. |
|  | Morphological Operations | Dilation, erosion, opening, closing for shape analysis and preprocessing. |
|  | Histogram Processing | Equalization, normalization, and contrast enhancement. |
|  | Color Space Conversion | RGB ↔ HSV, Lab, YUV for color-based processing. |
|  | Image Pyramids | Multi-scale image representation for feature detection and matching. |
| **Feature Extraction (Mid-Level)** | Keypoint Detection | Harris, FAST, Shi-Tomasi for detecting corners or salient points. |
|  | Feature Descriptors | SIFT, SURF, ORB, BRIEF, FREAK for encoding local features. |
|  | Template Matching | Cross-correlation and normalized matching for pattern detection. |
|  | Edge / Contour Analysis | Hough Transform for lines, circles, or general shapes. |
|  | Texture Analysis | LBP, GLCM, wavelet transforms for surface/texture characterization. |
| **Segmentation (Region Analysis)** | Thresholding | Global, adaptive, and Otsu’s thresholding for binary segmentation. |
|  | Region Growing / Merging | Grouping pixels based on similarity for region formation. |
|  | Graph-Based Segmentation | Normalized cuts, minimum cut, and superpixel-based methods. |
|  | Watershed | Marker-based region segmentation using gradient information. |
|  | Neural Segmentation | U-Net, Mask R-CNN, DeepLab for semantic and instance segmentation. |
| **Object Detection (Recognition)** | Haar Cascades | Classical object detection using boosted features. |
|  | HOG + SVM | Histogram of Oriented Gradients for object detection. |
|  | YOLO / SSD / Faster R-CNN | Modern deep learning detectors for real-time and accurate detection. |
|  | Vision Transformers (ViT) | Global-context-aware deep models for recognition tasks. |
|  | Capsule Networks | Representing spatial hierarchies for object recognition. |
| **Tracking (Motion Analysis)** | Optical Flow | Lucas-Kanade, Farneback for pixel motion estimation. |
|  | Kalman Filter | Predict and track moving objects in video sequences. |
|  | Particle Filter / Condensation | Probabilistic tracking under uncertainty. |
|  | SORT / DeepSORT | Modern multi-object tracking with deep features. |
|  | Mean-Shift / CamShift | Object tracking using color histograms. |
| **3D Vision (Geometry)** | Stereo Vision | Depth estimation using epipolar geometry. |
|  | Structure from Motion (SfM) | 3D scene reconstruction from multiple images. |
|  | Multi-View Stereo (MVS) | High-precision dense 3D reconstruction. |
|  | SLAM (Simultaneous Localization and Mapping) | Real-time 3D mapping and localization. |
|  | Point Cloud Processing | ICP, voxel grid, and normal estimation for 3D data. |
| **Deep Learning (Representation)** | CNNs | Convolutional networks for hierarchical feature extraction. |
|  | GANs | Generative models for image synthesis, style transfer, or super-resolution. |
|  | Autoencoders | Unsupervised feature learning and image compression. |
|  | Transformers for Vision | Global context modeling for classification and detection. |
|  | Attention Mechanisms | Focus on important regions in images for better prediction. |
| **Video (Temporal Analysis)** | 3D CNNs | Capture spatiotemporal features in video clips. |
|  | Recurrent Neural Networks | LSTM, GRU for temporal dynamics in videos. |
|  | Action Recognition Networks | I3D, C3D for activity recognition in videos. |
| **Multimodal (Sensor Fusion)** | LiDAR + RGB | Combining depth and color for richer perception. |
|  | RGB-D Processing | Kinect-like sensors for scene understanding. |
|  | Infrared / Thermal Vision | Complementing visible spectrum for low-light detection. |
|  | Radar + Camera Fusion | Autonomous driving applications. |
| **Specialized Techniques** | Super-Resolution | Increasing image resolution using deep or classical methods. |
|  | Image Inpainting / Completion | Filling missing or occluded regions. |
|  | Style Transfer | Neural or classical methods for artistic rendering. |
|  | Anomaly Detection | Detecting defects, unusual patterns, or outliers in images. |
|  | Visual Question Answering (VQA) | Integrating vision and language understanding. |

## References

- [Awesome Deep Vision](https://github.com/kjw0612/awesome-deep-vision)
- [First Principles of Computer Vision](https://fpcv.cs.columbia.edu/)
- https://en.wikipedia.org/wiki/Computer_vision
- https://en.wikipedia.org/wiki/Computational_photography
- https://github.com/roboflow/notebooks
- https://cs231n.stanford.edu/
- https://web.stanford.edu/class/cs231a/
- https://visionbook.mit.edu/
- https://introtocv.github.io/
- https://scenerepresentations.org/courses/2025/spring/advances-in-cv/