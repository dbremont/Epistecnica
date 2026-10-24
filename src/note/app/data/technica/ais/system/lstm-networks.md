---
tags: [learning-system]
---

# LSTM Networks


An [LSTM (Long Short-Term Memory)](https://en.wikipedia.org/wiki/Long_short-term_memory) network is a type of **Recurrent Neural Network (RNN)** that is designed to handle the vanishing gradient problem that occurs in traditional **RNNs**. **LSTM** networks are particularly useful for processing and predicting sequences of data.

In an **LSTM** network, there are specialized units called “cells” that are responsible for storing and outputting information over time. Each cell contains several gates that control the flow of information into and out of the cell. These gates include:

- **Input gate**: Controls the amount of new information that enters the cell at each time step.
- **Forget gate**: Controls the amount of information that is retained or discarded from the cell’s memory.
- **Output gate**: Controls the amount of information that is outputted from the cell at each time step.

The cell also contains a memory unit that retains information over time. This allows the network to remember relevant information from past time steps and use it to make predictions at future time steps.

The flow of information through an **LSTM** network is as follows:

- The input data is fed into the network at each time step.
- The input gate decides how much of the new input data should be added to the cell’s memory.
- The forget gate decides how much of the current memory should be retained or discarded.
- The memory unit updates its value based on the input data and the previous memory value.
- The output gate decides how much of the memory value should be outputted from the cell.
- The output is then fed into the next layer of the network (if present) or outputted as the final prediction.

By using these gates to control the flow of information, **LSTM** networks are able to effectively handle the vanishing gradient problem and make accurate predictions over long sequences of data.

## References

- Christopher Olah: Understanding LSTM Networks, 2015.
- Ilya Sutskever, Oriol Vinyals, and Quoc V. Le: Sequence to Sequence Learning with Neural Networks, NIPS 2014.
- [Long Short-term Memory](https://www.wikiwand.com/en/Long_short-term_memory)
