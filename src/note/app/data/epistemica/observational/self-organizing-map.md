# Self-organizing Map


Self-Organizing Maps are a type of artificial neural network that can be used for unsupervised learning and data visualization. The basic idea behind SOMs is to map high-dimensional input data onto a low-dimensional grid of neurons, where similar inputs are represented by adjacent neurons. The SOM algorithm involves two main processes: competition and cooperation.

- Competition: In the first step of the SOM algorithm, each input data point is compared to each neuron in the map to find the neuron that best represents that input. This is done using a distance measure such as Euclidean distance or cosine similarity. The neuron with the closest match to the input is known as the winner neuron.
- Cooperation: Once the winner neuron has been identified, its weight vector is adjusted to move closer to the input data point. Additionally, neighboring neurons in the map are also adjusted to move closer to the input, although to a lesser extent than the winner neuron. This is done using a neighborhood function that determines the extent of the adjustment for each neuron.

By repeating this process for many iterations, the SOM algorithm gradually organizes the neurons in the map to form a topological representation of the input data. Neurons that are close to each other in the map represent similar input data, while neurons that are far apart represent dissimilar data.

SOMs have a wide range of applications, including data visualization, clustering, and feature extraction. They are particularly useful for high-dimensional data, where it can be difficult to identify patterns and relationships using traditional methods.

Overall, the main idea behind SOMs is to use competition and cooperation between neurons to create a low-dimensional representation of high-dimensional input data that preserves the topological relationships between data points.

Kohonen, T. (1982). Self-organized formation of topologically correct feature maps. 43(1), 59–69.
