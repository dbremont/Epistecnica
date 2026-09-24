# Zhang, A., Lipton, Z. C., Li, M., & Smola, A. J. (2023). Dive into Deep Learning. Cambridge University Press.

```python
@book{zhang2023dive,
    title={Dive into Deep Learning},
    author={Zhang, Aston and Lipton, Zachary C. and Li, Mu and Smola, Alexander J.},
    publisher={Cambridge University Press},
    note={\url{https://D2L.ai}},
    year={2023}
}
```

## Notes

---

> …
> 

## Introduction

> See more in https://d2l.ai/chapter_introduction/index.html
> 

> Data Representation: Fixed Length; Variable Length, …
> 

> ML = Model + Model Evaluation (Objective Function) + Training Mechanism — or, how to evolve the model and improve its performance.
> 

> The training mechanism in ML is a **discrete dynamical system** that updates model parameters iteratively, guiding the model toward better performance.
> 

Viewing training as a dynamical system allows use of mathematical tools from **dynamical systems theory** to study:

- Convergence behavior.
- Stability of solutions.
- Effects of learning rate and noise.
- Possibility of cycles or chaotic dynamics in optimization.

Structure of a **Computational Learning System**:

1. The *data* that we can learn from.
2. A *model* of how to transform the data.
3. An *objective function* that quantifies how well (or badly) the model is doing.
4. An *algorithm* to adjust the model’s parameters to optimize the objective function.

Terminology:

| **Term** | **Description** |
| --- | --- |
| **Variable** | A quantity that can vary; general term for both inputs and outputs. |
| **Feature** | An individual measurable property or characteristic used as input to a model. |
| **Attribute** | Often used interchangeably with "feature"; common in data mining. |
| **Observation** | A single data point or row in a dataset (also called a "sample"). |
| **Instance** | One example or input; typically used in ML (e.g., one image, one patient record). |
| **Label** | The output or target value associated with an instance, in supervised learning. |
| **Target** | Synonym for "label"; the value the model is trying to predict. |
| **Response** | Common in statistics; the dependent variable (Y). |
| **Predictor** | Independent variable used to predict the response. |
| **Covariate** | An independent variable in statistics, especially in regression or ANOVA. |
| **Input** | General term for data fed into a model or function. |
| **Output** | The model's prediction or response. |
| **Dimension** | One axis in the feature space; the number of features = number of dimensions. |

 **ML Problems**

| **ML Problem Type** | **Model Structure** | **Evaluation (Loss) Function** | **Training Method** | **Goal** |
| --- | --- | --- | --- | --- |
| **Regression** | Linear models, Neural networks | Mean Squared Error (MSE), MAE | Gradient Descent, SGD | Predict continuous numerical output |
| **Classification** | Logistic regression, SVM, NN | Cross-Entropy, Hinge loss | Gradient Descent, SGD | Predict discrete class labels |
| **Clustering** | K-means, Gaussian Mixture Models | Within-cluster sum of squares, Likelihood | EM algorithm, Lloyd’s algorithm | Group data into clusters |
| **Dimensionality Reduction** | PCA, Autoencoders | Reconstruction error | Gradient Descent, SVD | Reduce data dimensionality |
| **Sequence Modeling** | RNNs, LSTMs, Transformers | Cross-Entropy, CTC Loss | Backpropagation Through Time | Model sequential data (text, speech) |
| **Reinforcement Learning** | Policy networks, Q-networks | Expected cumulative reward | Policy gradients, Q-learning | Learn optimal actions via reward |
| **Generative Modeling** | GANs, VAEs | Adversarial loss, ELBO | Alternating optimization | Generate new data samples |

## Preliminaries

> …
> 
- [ ]  **Data Manipulation**: Introduction to Pytorch.
- [ ]  **Data Preprocessing**:  Loading dataset, data preparation and pytorch convertions.
- [ ]  **Linear Algebra**: Scalar, Vector, Matrix, Tensor, Properties of Tensor Arithmetic, Reduction, Non-reductoin Sum, Dot Product, Matrix-Vector Product, Matrix-Matrix Product, Norm.
- [ ]  **Calculus**: Deriviate Operator,  Partial Derivative, Gradient, Chain Rule.
- [ ]  **Automatic Differentiation**:  Computation Graph, Autograd, Detaching Computation.
- [ ]  **Probability and Statistics**:  Probability Model, Event, Event Space, Random Variable, Conditional Probability, Expected Value, …
- [ ]  **Documentation**:  (https://docs.pytorch.org/docs/stable/index.html) and (https://docs.pytorch.org/tutorials/beginner/basics/intro.html).

## Linear Neural Networks for Regression

## Linear Neural Networks for Classification

## Multilayer Perceptrons

## Builder’s Guide

## Convolutional Neural Networks

## Modern Convolutional Neural Networks

## Recurrent Neural Networks

## Modern Recurrent Neural Networks

## Attention Mechanisms and Transformers

## Optimization Algorithms

## Computational Performance

## Computer Vision

## Natural Language Processing: Pretraining

## Natural Language Processing: Applications

## Reinforcement Learning

## Gaussian Processes

## Hyperparameter Optimization

## Generative Adversarial Networks

## Recommender Systems

## Mathematics for Deep Learning

## Tools for Deep Learning

## References

- https://d2l.ai/index.html
- [Domingos, P. (2012). A few useful things to know about machine learning. Communications of the ACM, 55(10), 78–87.](Domingos,%20P%20(2012)%20A%20few%20useful%20things%20to%20know%20abo%2010e598edb7908112be05c456b201c80e.md)
- Abadi, M., Barham, P., Chen, J., Chen, Z., Davis, A., Dean, J., … et al. (2016). TensorFlow: a system for large-scale machine learning. 12th USENIX Symposium on Operating Systems Design and Implementation (OSDI 16) (pp. 265–283).
- Abdel-Hamid, O., Mohamed, A.-R., Jiang, H., Deng, L., Penn, G., & Yu, D. (2014). Convolutional neural networks for speech recognition. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 22(10), 1533–1545.
- Ahmed, A., Aly, M., Gonzalez, J., Narayanamurthy, S., & Smola, A. J. (2012). Scalable inference in latent variable models. Proceedings of the Fifth ACM International Conference on Web Search and Data Mining (pp. 123–132).
- Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: a next-generation hyperparameter optimization framework. Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining.
- Alayrac, J.-B., Donahue, J., Luc, P., Miech, A., Barr, I., Hasson, Y., … et al. (2022). Flamingo: a visual language model for few-shot learning. ArXiv:2204.14198.
- Alsallakh, B., Kokhlikyan, N., Miglani, V., Yuan, J., & Reblitz-Richardson, O. (2020). Mind the PAD – CNNs can develop blind spots. ArXiv:2010.02178.
- Anil, R., Dai, A. M., Firat, O., Johnson, M., Lepikhin, D., Passos, A., … et al. (2023). PaLM 2 Technical Report. ArXiv:2305.10403.
- Anil, R., Gupta, V., Koren, T., Regan, K., & Singer, Y. (2020). Scalable second-order optimization for deep learning. ArXiv:2002.09018.
- Aronszajn, N. (1950). Theory of reproducing kernels. Transactions of the American Mathematical Society, 68(3), 337–404.
- Ba, J. L., Kiros, J. R., & Hinton, G. E. (2016). Layer normalization. ArXiv:1607.06450.
- Baevski, A., & Auli, M. (2018). Adaptive input representations for neural language modeling. International Conference on Learning Representations.
- Bahdanau, D., Cho, K., & Bengio, Y. (2014). Neural machine translation by jointly learning to align and translate. ArXiv:1409.0473.
- Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., … et al. (2022). Constitutional AI: harmlessness from AI feedback. ArXiv:2212.08073.
- Baptista, R., & Poloczek, M. (2018). Bayesian optimization of combinatorial structures. Proceedings of the 35th International Conference on Machine Learning.
- Bardenet, R., Brendel, M., Kégl, B., & Sebag, M. (2013). Collaborative hyperparameter tuning. Proceedings of the 30th International Conference on Machine Learning (ICML'13).
- Bay, H., Tuytelaars, T., & Van Gool, L. (2006). SURF: Speeded up robust features. European Conference on Computer Vision (pp. 404–417).
- Bellman, R. (1966). Dynamic programming. Science, 153, 34–37.
- Bellman, R. (1952). On the theory of dynamic programming. Proceedings of the National Academy of Sciences, 38(8), 716–719.
- Bellman, R. (1957). A Markovian decision process. Journal of Mathematics and Mechanics, 6(5), 679–684. URL: [http://www.jstor.org/stable/](http://www.jstor.org/stable/)
- Bellman, R. (1957). Dynamic Programming. Dover Publications.
- Beltagy, I., Peters, M. E., & Cohan, A. (2020). Longformer: the long-document transformer. ArXiv:2004.05150.
- Bengio, Y., Ducharme, R., Vincent, P., & Jauvin, C. (2003). A neural probabilistic language model. Journal of Machine Learning
- Bengio, Y., Simard, P., & Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. IEEE Transactions on
- Bergstra, J., Bardenet, R., Bengio, Y., & Kégl, B. (2011). Algorithms for hyper-parameter optimization. Advances in Neural Information
- Bergstra, J., Breuleux, O., Bastien, F., Lamblin, P., Pascanu, R., Desjardins, G., … Bengio, Y. (2010). Theano: a CPU and GPU math
- Beutel, A., Murray, K., Faloutsos, C., & Smola, A. J. (2014). CoBaFi: collaborative Bayesian filtering. Proceedings of the 23rd
- Bishop, C. M. (1995). Training with noise is equivalent to Tikhonov regularization. Neural Computation, 7(1), 108–116.
- Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.
- Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. Journal of Political Economy, 81, 637–654.
- Bodla, N., Singh, B., Chellappa, R., & Davis, L. S. (2017). Soft-NMS-improving object detection with one line of code. Proceedings of
- Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). Enriching word vectors with subword information. Transactions of the
- Bollobás, B. (1999). Linear Analysis. Cambridge University Press.
- Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., … et al. (2021). On the opportunities and risks of
- Bottou, L. (2010). Large-scale machine learning with stochastic gradient descent. Proceedings of COMPSTAT'2010 (pp. 177–186). Springer.
- Bottou, L., & Le Cun, Y. (1988). SN: a simulator for connectionist models. Proceedings of NeuroNimes 88 (pp. 371–382). Nimes, France.
- Boucheron, S., Bousquet, O., & Lugosi, G. (2005). Theory of classification: a survey of some recent advances. ESAIM: Probability and
- Bowman, S. R., Angeli, G., Potts, C., & Manning, C. D. (2015). A large annotated corpus for learning natural language inference.
- Boyd, S., & Vandenberghe, L. (2004). Convex Optimization. Cambridge, England: Cambridge University Press.
- Bradley, R. A., & Terry, M. E. (1952). Rank analysis of incomplete block designs: I. The method of paired comparisons. Biometrika, 39(3/
- Brown, N., & Sandholm, T. (2017). Libratus: the superhuman AI for no-limit poker. IJCAI (pp. 5226–5228).
- Brown, P. F., Cocke, J., Della Pietra, S. A., Della Pietra, V. J., Jelinek, F., Lafferty, J., … Roossin, P. S. (1990). A statistical
- Brown, P. F., Cocke, J., Della Pietra, S. A., Della Pietra, V. J., Jelinek, F., Mercer, R. L., & Roossin, P. (1988). A statistical
- Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., … et al. (2020). Language models are few-shot learners.
- Buslaev, A., Iglovikov, V. I., Khvedchenya, E., Parinov, A., Druzhinin, M., & Kalinin, A. A. (2020). Albumentations: Fast and flexible
- Campbell, M., Hoane Jr, A. J., & Hsu, F.-h. (2002). Deep blue. Artificial Intelligence, 134(1-2), 57–83.
- Canny, J. (1987). A computational approach to edge detection. Readings in Computer Vision (pp. 184–203). Elsevier.
- Cer, D., Diab, M., Agirre, E., Lopez-Gazpio, I., & Specia, L. (2017). SemEval-2017 Task 1: semantic textual similarity multilingual and
- Chan, W., Jaitly, N., Le, Q. V., & Vinyals, O. (2015). Listen, attend and spell. ArXiv:1508.01211.
- Chen, L., Lu, K., Rajeswaran, A., Lee, K., Grover, A., Laskin, M., … Mordatch, I. (2021). Decision transformer: reinforcement learning
- Chen, T., Li, M., Li, Y., Lin, M., Wang, N., Wang, M., … Zhang, Z. (2015). MXNET: a flexible and efficient machine learning library for
- Cheng, J., Dong, L., & Lapata, M. (2016). Long short-term memory-networks for machine reading. Proceedings of the 2016 Conference on
- Chetlur, S., Woolley, C., Vandermersch, P., Cohen, J., Tran, J., Catanzaro, B., & Shelhamer, E. (2014). CuDNN: Efficient primitives for
- Cho, K., Van Merriënboer, B., Bahdanau, D., & Bengio, Y. (2014). On the properties of neural machine translation: Encoder–decoder
- Cho, K., Van Merriënboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., & Bengio, Y. (2014). Learning phrase
- Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Roberts, A., … et al. (2022). PaLM: scaling language modeling with
- Chung, J., Gulcehre, C., Cho, K., & Bengio, Y. (2014). Empirical evaluation of gated recurrent neural networks on sequence modeling.
- Clark, K., Luong, M.-T., Le, Q. V., & Manning, C. D. (2020). ELECTRA: pre-training text encoders as discriminators rather than
- Collobert, R., Weston, J., Bottou, L., Karlen, M., Kavukcuoglu, K., & Kuksa, P. (2011). Natural language processing (almost) from
- Cordonnier, J.-B., Loukas, A., & Jaggi, M. (2020). On the relationship between self-attention and convolutional layers. International
- Cover, T., & Thomas, J. (1999). Elements of Information Theory. John Wiley & Sons.
- Csiszár, I. (2008). Axiomatic characterizations of information measures. Entropy, 10(3), 261–273.
- Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. Mathematics of Control, Signals and Systems, 2(4), 303–314.
- Dalal, N., & Triggs, B. (2005). Histograms of oriented gradients for human detection. 2005 IEEE Computer Society Conference on Computer
- De Cock, D. (2011). Ames, Iowa: alternative to the Boston housing data as an end of semester regression project. Journal of Statistics
- Dean, J., Corrado, G. S., Monga, R., Chen, K., Devin, M., Le, Q. V., … et al. (2012). Large scale distributed deep networks.
- DeCandia, G., Hastorun, D., Jampani, M., Kakulapati, G., Lakshman, A., Pilchin, A., … Vogels, W. (2007). Dynamo: Amazon's highly
- Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., & Fei-Fei, L. (2009). Imagenet: a large-scale hierarchical image database. 2009 IEEE
- Der Kiureghian, A., & Ditlevsen, O. (2009). Aleatory or epistemic? does it matter? Structural Safety, 31(2), 105–112.
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of deep bidirectional transformers for language
- Dinh, L., Krueger, D., & Bengio, Y. (2014). NICE: non-linear independent components estimation. ArXiv:1410.8516.
- Dinh, L., Sohl-Dickstein, J., & Bengio, S. (2017). Density estimation using real NVP. International Conference on Learning
- Doersch, C., Gupta, A., & Efros, A. A. (2015). Unsupervised visual representation learning by context prediction. Proceedings of the
- Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., … et al. (2021). An image is worth 16 x 16
- Duchi, J., Hazan, E., & Singer, Y. (2011). Adaptive subgradient methods for online learning and stochastic optimization. Journal of
- Dumoulin, V., & Visin, F. (2016). A guide to convolution arithmetic for deep learning. ArXiv:1603.07285.
- Dwivedi, V. P., & Bresson, X. (2020). A generalization of transformer networks to graphs. ArXiv:2012.09699.
- Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. L. (2015). Preserving statistical validity in adaptive data
- Elman, J. L. (1990). Finding structure in time. Cognitive Science, 14(2), 179–211.
- Elsken, T., Metzen, J. H., & Hutter, F. (2018). Neural architecture search: a ssurvey. ArXiv:1808.05377 [[stat.ML](http://stat.ml/)].
- Fechner, G. T. (1860). Elemente der Psychophysik. Vol. 2. Breitkopf u. Härtel.
- Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch transformers: scaling to trillion parameter models with simple and efficient
- Fernando, R. (2004). GPU Gems: Programming Techniques, Tips, and Tricks for Real-Time Graphics. Addison-Wesley.
- Feurer, M., & Hutter, F. (2018). Hyperparameter ptimization. Automatic Machine Learning: Methods, Systems, Challenges. Springer.
- Feurer, M., Letham, B., Hutter, F., & Bakshy, E. (2022). Practical transfer learning for Bayesian optimization. ArXiv:1802.02219 [stat.
- Field, D. J. (1987). Relations between the statistics of natural images and the response properties of cortical cells. JOSA A, 4(12),
- Fisher, R. A. (1925). Statistical Methods for Research Workers. Oliver & Boyd.
- Flammarion, N., & Bach, F. (2015). From averaging to acceleration, there is only a step-size. Conference on Learning Theory (pp.
- Forrester, A. I., Sóbester, A., & Keane, A. J. (2007). Multi-fidelity optimization via surrogate modelling. Proceedings of the Royal
- Franceschi, L., Donini, M., Frasconi, P., & Pontil, M. (2017). Forward and reverse gradient-based hyperparameter optimization.
- Frankle, J., & Carbin, M. (2018). The lottery ticket hypothesis: finding sparse, trainable neural networks. ArXiv:1803.03635.
- Frazier, P. I. (2018). A tutorial on Bayesian optimization. ArXiv:1807.02811.
- Freund, Y., & Schapire, R. E. (1996). Experiments with a new boosting algorithm. Proceedings of the International Conference on Machine
- Friedman, J. H. (1987). Exploratory projection pursuit. Journal of the American Statistical Association, 82(397), 249–266.
- Frostig, R., Johnson, M. J., & Leary, C. (2018). Compiling machine learning programs via high-level tracing. Proceedings of Systems for
- Fukushima, K. (1982). Neocognitron: a self-organizing neural network model for a mechanism of visual pattern recognition. Competition
- Gardner, J., Pleiss, G., Weinberger, K. Q., Bindel, D., & Wilson, A. G. (2018). GPyTorch: blackbox matrix–matrix Gaussian process
- Garg, S., Balakrishnan, S., Kolter, Z., & Lipton, Z. (2021). RATT: leveraging unlabeled data to guarantee generalization. International
- Gatys, L. A., Ecker, A. S., & Bethge, M. (2016). Image style transfer using convolutional neural networks. Proceedings of the IEEE
- Gauss, C. F. (1809). Theoria motus corporum coelestum. Werke. Königlich Preussische Akademie der Wissenschaften.
- Gibbs, J. W. (1902). Elementary Principles of Statistical Mhanics. Scribner's.
- Ginibre, J. (1965). Statistical ensembles of complex, quaternion, and real matrices. Journal of Mathematical Physics, 6(3), 440–449.
- Girshick, R. (2015). Fast R-CNN. Proceedings of the IEEE International Conference on Computer Vision (pp. 1440–1448).
- Girshick, R., Donahue, J., Darrell, T., & Malik, J. (2014). Rich feature hierarchies for accurate object detection and semantic
- Glorot, X., & Bengio, Y. (2010). Understanding the difficulty of training deep feedforward neural networks. Proceedings of the 13th
- Goh, G. (2017). Why momentum really works. Distill. URL: [http://distill.pub/2017/momentum](http://distill.pub/2017/momentum)
- Goldberg, D., Nichols, D., Oki, B. M., & Terry, D. (1992). Using collaborative filtering to weave an information tapestry.
- Golub, G. H., & Van Loan, C. F. (1996). Matrix Computations. Johns Hopkins University Press.
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press. [http://www.deeplearningbook.org](http://www.deeplearningbook.org/).
- Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., … Bengio, Y. (2014). Generative adversarial nets.
- Gotmare, A., Keskar, N. S., Xiong, C., & Socher, R. (2018). A closer look at deep learning heuristics: learning rate restarts, warmup
- Goyal, A., Bochkovskiy, A., Deng, J., & Koltun, V. (2021). Non-deep networks. ArXiv:2110.07641.
- Graham, B. (2014). Fractional max-pooling. ArXiv:1412.6071.
- Graves, A. (2013). Generating sequences with recurrent neural networks. ArXiv:1308.0850.
- Graves, A., Liwicki, M., Fernández, S., Bertolami, R., Bunke, H., & Schmidhuber, J. (2008). A novel connectionist system for
- Graves, A., & Schmidhuber, J. (2005). Framewise phoneme classification with bidirectional LSTM and other neural network architectures.
- Griewank, A. (1989). On automatic differentiation. Mathematical Programming: Recent Developments and Applications (pp. 83–107). Kluwer.
- Gulati, A., Qin, J., Chiu, C.-C., Parmar, N., Zhang, Y., Yu, J., … et al. (2020). Conformer: convolution-augmented transformer for
- Gunawardana, A., & Shani, G. (2015). Evaluating recommender systems. Recommender Systems Handbook (pp. 265–308). Springer.
- Guo, H., Tang, R., Ye, Y., Li, Z., & He, X. (2017). Deepfm: a factorization-machine based neural network for ctr prediction.
- Guyon, I., Gunn, S., Nikravesh, M., & Zadeh, L. A. (2008). Feature Extraction: Foundations and Applications. Springer.
- Hadjis, S., Zhang, C., Mitliagkas, I., Iter, D., & Ré, C. (2016). Omnivore: an optimizer for multi-device deep learning on CPUs and
- Hartley, R., & Zisserman, A. (2000). Multiple View Geometry in Computer Vision. Cambridge University Press.
- Hartley, R. I., & Kahl, F. (2009). Global optimization through rotation space search. International Journal of Computer Vision, 82(1),
- He, K., Chen, X., Xie, S., Li, Y., Dollár, P., & Girshick, R. (2022). Masked autoencoders are scalable vision learners. Proceedings of
- He, K., Gkioxari, G., Dollár, P., & Girshick, R. (2017). Mask R-CNN. Proceedings of the IEEE International Conference on Computer
- He, K., Zhang, X., Ren, S., & Sun, J. (2015). Delving deep into rectifiers: surpassing human-level performance on ImageNet
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. Proceedings of the IEEE Conference on
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). Identity mappings in deep residual networks. European Conference on Computer Vision (pp.
- He, X., & Chua, T.-S. (2017). Neural factorization machines for sparse predictive analytics. Proceedings of the 40th International ACM
- He, X., Liao, L., Zhang, H., Nie, L., Hu, X., & Chua, T.-S. (2017). Neural collaborative filtering. Proceedings of the 26th
- Hebb, D. O. (1949). The Organization of Behavior. Wiley.
- Hendrycks, D., & Gimpel, K. (2016). Gaussian error linear units (GELUs). ArXiv:1606.08415.
- Hennessy, J. L., & Patterson, D. A. (2011). Computer Architecture: A Quantitative Approach. Elsevier.
- Herlocker, J. L., Konstan, J. A., Borchers, A., & Riedl, J. (1999). An algorithmic framework for performing collaborative filtering.
- Hidasi, B., Karatzoglou, A., Baltrunas, L., & Tikk, D. (2015). Session-based recommendations with recurrent neural networks. ArXiv:1511.
- Ho, J., Jain, A., & Abbeel, P. (2020). Denoising diffusion probabilistic models. Advances in Neural Information Processing Systems, 33,
- Hochreiter, S., Bengio, Y., Frasconi, P., & Schmidhuber, J. (2001). Gradient flow in recurrent nets: the difficulty of learning
- Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8), 1735–1780.
- Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., … et al. (2022). Training compute-optimal large
- Howard, A., Sandler, M., Chu, G., Chen, L.-C., Chen, B., Tan, M., … Adam, H. (2019). Searching for MobileNetV3. Proceedings of the IEEE/
- Hoyer, P. O., Janzing, D., Mooij, J. M., Peters, J., & Schölkopf, B. (2009). Nonlinear causal discovery with additive noise models.
- Hu, J., Shen, L., & Sun, G. (2018). Squeeze-and-excitation networks. Proceedings of the IEEE Conference on Computer Vision and Pattern
- Hu, Y., Koren, Y., & Volinsky, C. (2008). Collaborative filtering for implicit feedback datasets. 2008 8th IEEE International
- Hu, Z., Lee, R. K.-W., Aggarwal, C. C., & Zhang, A. (2022). Text style transfer: a review and experimental evaluation. SIGKDD Explor.
- Huang, C.-Z. A., Vaswani, A., Uszkoreit, J., Simon, I., Hawthorne, C., Shazeer, N., … Eck, D. (2018). Music transformer: generating
- Huang, G., Liu, Z., Van Der Maaten, L., & Weinberger, K. Q. (2017). Densely connected convolutional networks. Proceedings of the IEEE
- Huang, Z., Xu, W., & Yu, K. (2015). Bidirectional LSTM–CRF models for sequence tagging. ArXiv:1508.01991.
- Hubel, D. H., & Wiesel, T. N. (1959). Receptive fields of single neurones in the cat's striate cortex. Journal of Physiology, 148(3),
- Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex.
- Hubel, D. H., & Wiesel, T. N. (1968). Receptive fields and functional architecture of monkey striate cortex. Journal of Physiology, 195
- Hutter, F., Hoos, H., & Leyton-Brown, K. (2011). Sequential model-based optimization for general algorithm configuration. Proceedings
- Hutter, F., Kotthoff, L., & Vanschoren, J. (Eds.) (2019). Automated Machine Learning: Methods, Systems, Challenges. Springer.
- Ioffe, S. (2017). Batch renormalization: towards reducing minibatch dependence in batch-normalized models. Advances in Neural
- Ioffe, S., & Szegedy, C. (2015). Batch normalization: accelerating deep network training by reducing internal covariate shift.
- Izmailov, P., Podoprikhin, D., Garipov, T., Vetrov, D., & Wilson, A. G. (2018). Averaging weights leads to wider optima and better
- Jacot, A., Gabriel, F., & Hongler, C. (2018). Neural tangent kernel: convergence and generalization in neural networks. Advances in
- Jaeger, H. (2002). Tutorial on training recurrent neural networks, covering BPPT, RTRL, EKF and the “echo state network” approach.
- Jamieson, K., & Talwalkar, A. (2016). Non-stochastic best arm identification and hyperparameter optimization. Proceedings of the 17th
- Jenatton, R., Archambeau, C., González, J., & Seeger, M. (2017). Bayesian optimization with tree-structured dependencies. Proceedings
- Jia, X., Song, S., He, W., Wang, Y., Rong, H., Zhou, F., … et al. (2018). Highly scalable deep learning training system with
- Jia, Y., Shelhamer, E., Donahue, J., Karayev, S., Long, J., Girshick, R., … Darrell, T. (2014). Caffe: convolutional architecture for
- Joshi, M., Chen, D., Liu, Y., Weld, D. S., Zettlemoyer, L., & Levy, O. (2020). SpanBERT: improving pre-training by representing and
- Jouppi, N. P., Young, C., Patil, N., Patterson, D., Agrawal, G., Bajwa, R., … et al. (2017). In-datacenter performance analysis of a
- Kalchbrenner, N., Grefenstette, E., & Blunsom, P. (2014). A convolutional neural network for modelling sentences. ArXiv:1404.2188.
- Kalman, B. L., & Kwasny, S. C. (1992). Why tanh: choosing a sigmoidal function. Proceedings of the International Joint Conference on
- Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., … Amodei, D. (2020). Scaling laws for neural language
- Karnin, Z., Koren, T., & Somekh, O. (2013). Almost optimal exploration in multi-armed bandits. Proceedings of the 30th International
- Karras, T., Aila, T., Laine, S., & Lehtinen, J. (2017). Progressive growing of GANs for improved quality, stability, and variation.
- Kim, J., El-Khamy, M., & Lee, J. (2017). Residual LSTM: design of a deep recurrent architecture for distant speech recognition.
- Kim, Y. (2014). Convolutional neural networks for sentence classification. ArXiv:1408.5882.
- Kimeldorf, G. S., & Wahba, G. (1971). Some results on Tchebycheffian spline functions. J. Math. Anal. Appl., 33, 82–95.
- Kingma, D. P., & Ba, J. (2014). Adam: a method for stochastic optimization. ArXiv:1412.6980.
- Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes. International Conference on Learning Representations (ICLR).
- Kipf, T. N., & Welling, M. (2016). Semi-supervised classification with graph convolutional networks. ArXiv:1609.02907.
- Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Large language models are zero-shot reasoners. [arxiv.org/abs/2205](http://arxiv.org/abs/2205).
- Koller, D., & Friedman, N. (2009). Probabilistic Graphical Models: Principles and Techniques. MIT Press.
- Kolmogorov, A. (1933). Sulla determinazione empirica di una legge di distribuzione. Inst. Ital. Attuari, Giorn., 4, 83–91.
- Kolter, Z. (2008). Linear algebra review and reference. Available online: [http://cs229.stanford.edu/section/cs229-linalg.pdf](http://cs229.stanford.edu/section/cs229-linalg.pdf).
- Koren, Y., Bell, R., & Volinsky, C. (2009). Matrix factorization techniques for recommender systems. Computer, pp. 30–37.
- Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. Advances in
- Kung, S. Y. (1988). VLSI Array Processors. Prentice Hall.
- Kuzovkin, I., Vicente, R., Petton, M., Lachaux, J.-P., Baciu, M., Kahane, P., … Aru, J. (2018). Activations of deep convolutional
- Lan, Z., Chen, M., Goodman, S., Gimpel, K., Sharma, P., & Soricut, R. (2019). ALBERT: a lite BERT for self-supervised learning of
- Lavin, A., & Gray, S. (2016). Fast algorithms for convolutional neural networks. Proceedings of the IEEE Conference on Computer Vision
- Le, Q. V. (2013). Building high-level features using large scale unsupervised learning. Proceedings of the IEEE International
- LeCun, Y., Bengio, Y., & et al. (1995). Convolutional networks for images, speech, and time series. The Handbook of Brain Theory and
- LeCun, Y., Boser, B., Denker, J. S., Henderson, D., Howard, R. E., Hubbard, W., & Jackel, L. D. (1989). Backpropagation applied to
- LeCun, Y., Bottou, L., Orr, G., & Muller, K.-R. (1998). Efficient backprop. Neural Networks: Tricks of the Trade. Springer.
- LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). Gradient-based learning applied to document recognition. Proceedings of the
- LeCun, Y., Jackel, L., Bottou, L., Brunot, A., Cortes, C., Denker, J., … et al. (1995). Comparison of learning algorithms for
- Legendre, A. M. (1805). Mémoire sur les Opérations Trigonométriques: dont les Résultats Dépendent de la Figure de la Terre. F. Didot.
- Lewis, M., Liu, Y., Goyal, N., Ghazvininejad, M., Mohamed, A., Levy, O., … Zettlemoyer, L. (2019). BART: denoising sequence-to-sequence
- Lewkowycz, A., Andreassen, A., Dohan, D., Dyer, E., Michalewski, H., Ramasesh, V., … et al. (2022). Solving quantitative reasoning
- Li, L., Jamieson, K., Rostamizadeh, A., Gonina, K., Hardt, M., Recht, B., & Talwalkar, A. (2018). Massively parallel hyperparameter
- Li, M. (2017). Scaling Distributed Machine Learning with System and Algorithm Co-design (Doctoral dissertation). PhD Thesis, CMU.
- Li, M., Andersen, D. G., Park, J. W., Smola, A. J., Ahmed, A., Josifovski, V., … Su, B.-Y. (2014). Scaling distributed machine learning
- Li, M., Zhang, T., Chen, Y., & Smola, A. J. (2014). Efficient mini-batch training for stochastic optimization. Proceedings of the 20th
- Liaw, R., Liang, E., Nishihara, R., Moritz, P., Gonzalez, J., & Stoica, I. (2018). Tune: a research platform for distributed model
- Lin, M., Chen, Q., & Yan, S. (2013). Network in network. ArXiv:1312.4400.
- Lin, T.-Y., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017). Focal loss for dense object detection. Proceedings of the IEEE
- Lin, Y., Lv, F., Zhu, S., Yang, M., Cour, T., Yu, K., … others. (2010). ImageNet classification: fast descriptor coding and large-scale
- Lin, Z., Feng, M., Santos, C. N. d., Yu, M., Xiang, B., Zhou, B., & Bengio, Y. (2017). A structured self-attentive sentence embedding.
- Lipton, Z. C., Berkowitz, J., & Elkan, C. (2015). A critical review of recurrent neural networks for sequence learning. ArXiv:1506.
- Lipton, Z. C., Kale, D. C., Elkan, C., & Wetzel, R. (2016). Learning to diagnose with LSTM recurrent neural networks. International
- Lipton, Z. C., & Steinhardt, J. (2018). Troubling trends in machine learning scholarship. Communications of the ACM, 17, 45–77.
- Liu, D. C., & Nocedal, J. (1989). On the limited memory BFGS method for large scale optimization. Mathematical Programming, 45(1),
- Liu, H., Simonyan, K., & Yang, Y. (2018). DARTS: differentiable architecture search. ArXiv:1806.09055.
- Liu, W., Anguelov, D., Erhan, D., Szegedy, C., Reed, S., Fu, C.-Y., & Berg, A. C. (2016). SSD: single shot multibox detector. European
- Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., … Stoyanov, V. (2019). RoBERTa: a robustly optimized BERT pretraining
- Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., … Guo, B. (2021). Swin transformer: hierarchical vision transformer using
- Liu, Z., Mao, H., Wu, C.-Y., Feichtenhofer, C., Darrell, T., & Xie, S. (2022). A convNet for the 2020s. ArXiv:2201.03545.
- Long, J., Shelhamer, E., & Darrell, T. (2015). Fully convolutional networks for semantic segmentation. Proceedings of the IEEE
- Loshchilov, I., & Hutter, F. (2016). SGDR: stochastic gradient descent with warm restarts. ArXiv:1608.03983.
- Lowe, D. G. (2004). Distinctive image features from scale-invariant keypoints. International Journal of Computer Vision, 60(2), 91–110.
- Luo, P., Wang, X., Shao, W., & Peng, Z. (2018). Towards understanding regularization in batch normalization. ArXiv:1809.00846.
- Maas, A. L., Daly, R. E., Pham, P. T., Huang, D., Ng, A. Y., & Potts, C. (2011). Learning word vectors for sentiment analysis.
- Mack, Y.-P., & Silverman, B. W. (1982). Weak and strong uniform consistency of kernel regression estimates. Zeitschrift für
- MacKay, D. J. (2003). Information Theory, Inference and Learning Algorithms. Cambridge University Press.
- Maclaurin, D., Duvenaud, D., & Adams, R. (2015). Gradient-based hyperparameter optimization through reversible learning. Proceedings of
- Mangasarian, O. L. (1965). Linear and nonlinear separation of patterns by linear programming. Oper. Res., 13, 444-452.
- Mangram, M. E. (2013). A simplified perspective of the Markowitz portfolio theory. Global Journal of Business Research, 7(1), 59–70.
- Matthews, A. G. d. G., Rowland, M., Hron, J., Turner, R. E., & Ghahramani, Z. (2018). Gaussian process behaviour in wide deep neural
- McCann, B., Bradbury, J., Xiong, C., & Socher, R. (2017). Learned in translation: Contextualized word vectors. Advances in Neural
- McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. Bulletin of Mathematical
- McMahan, H. B., Holt, G., Sculley, D., Young, M., Ebner, D., Grady, J., … et al. (2013). Ad click prediction: a view from the trenches.
- Mead, C. (1980). Introduction to VLSI systems. IEE Proceedings I-Solid-State and Electron Devices, 128(1), 18.
- Merity, S., Xiong, C., Bradbury, J., & Socher, R. (2016). Pointer sentinel mixture models. ArXiv:1609.07843.
- Micchelli, C. A. (1984). Interpolation of scattered data: distance matrices and conditionally positive definite functions.
- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. ArXiv:1301.3781.
- Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words and phrases and their
- Miller, G. A. (1995). WordNet: a lexical database for English. Communications of the ACM, 38(11), 39–41.
- Mirhoseini, A., Pham, H., Le, Q. V., Steiner, B., Larsen, R., Zhou, Y., … Dean, J. (2017). Device placement optimization with
- Mnih, V., Heess, N., Graves, A., & others. (2014). Recurrent models of visual attention. Advances in Neural Information Processing
- Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., & Riedmiller, M. (2013). Playing Atari with deep
- Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., … et al. (2015). Human-level control through deep
- Moon, T., Smola, A., Chang, Y., & Zheng, Z. (2010). Intervalrank: isotonic regression with listwise and pairwise constraints.
- Morey, R. D., Hoekstra, R., Rouder, J. N., Lee, M. D., & Wagenmakers, E.-J. (2016). The fallacy of placing confidence in confidence
- Morozov, V. A. (1984). Methods for Solving Incorrectly Posed Problems. Springer.
- Nadaraya, E. A. (1964). On estimating regression. Theory of Probability & its Applications, 9(1), 141–142.
- Nair, V., & Hinton, G. E. (2010). Rectified linear units improve restricted Boltzmann machines. ICML.
- Nakkiran, P., Kaplun, G., Bansal, Y., Yang, T., Barak, B., & Sutskever, I. (2021). Deep double descent: where bigger models and more
- Naor, M., & Reingold, O. (1999). On the construction of pseudorandom permutations: Luby–Rackoff revisited. Journal of Cryptology, 12
- Neal, R. M. (1996). Bayesian Learning for Neural Networks. Springer.
- Nesterov, Y. (2018). Lectures on Convex Optimization. Springer.
- Nesterov, Y., & Vial, J.-P. (2000). Confidence level solutions for stochastic programming. Automatica, 44(6), 1559–1568.
- Neyman, J. (1937). Outline of a theory of statistical estimation based on the classical theory of probability. Philosophical
- Norelli, A., Fumero, M., Maiorca, V., Moschella, L., Rodolà, E., & Locatello, F. (2022). ASIF: coupled data turns unimodal models to
- Novak, R., Xiao, L., Lee, J., Bahri, Y., Yang, G., Hron, J., … Sohl-Dickstein, J. (2018). Bayesian deep convolutional networks with
- Novikoff, A. B. J. (1962). On convergence proofs on perceptrons. Proceedings of the Symposium on the Mathematical Theory of Automata
- Olshausen, B. A., & Field, D. J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural
- Ong, C. S., Smola, A., & Williamson, R. (2005). Learning the kernel with hyperkernels. Journal of Machine Learning Research, 6,
- OpenAI. (2023). GPT-4 Technical Report. ArXiv:2303.08774.
- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., … et al. (2022). Training language models to follow
- Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). BLEU: a method for automatic evaluation of machine translation. Proceedings of
- Parikh, A. P., Täckström, O., Das, D., & Uszkoreit, J. (2016). A decomposable attention model for natural language inference.
- Park, T., Liu, M.-Y., Wang, T.-C., & Zhu, J.-Y. (2019). Semantic image synthesis with spatially-adaptive normalization. Proceedings of
- Parzen, E. (1957). On consistent estimates of the spectrum of a stationary time series. Annals of Mathematical Statistics, 28, 329–348.
- Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., … et al. (2019). PyTorch: an imperative style, high-performance
- Paulus, R., Xiong, C., & Socher, R. (2017). A deep reinforced model for abstractive summarization. ArXiv:1705.04304.
- Penedo, G., Malartic, Q., Hesslow, D., Cojocaru, R., Cappelli, A., Alobeidli, H., … Launay, J. (2023). The RefinedWeb dataset for
- Pennington, J., Schoenholz, S., & Ganguli, S. (2017). Resurrecting the sigmoid in deep learning through dynamical isometry: theory and
- Pennington, J., Socher, R., & Manning, C. (2014). GloVe: global vectors for word representation. Proceedings of the 2014 Conference on
- Peters, J., Janzing, D., & Schölkopf, B. (2017). Elements of Causal Inference: Foundations and Learning Algorithms. MIT Press.
- Peters, M., Ammar, W., Bhagavatula, C., & Power, R. (2017). Semi-supervised sequence tagging with bidirectional language models.
- Peters, M., Neumann, M., Iyyer, M., Gardner, M., Clark, C., Lee, K., & Zettlemoyer, L. (2018). Deep contextualized word
- Petersen, K. B., & Pedersen, M. S. (2008). The Matrix Cookbook. Technical University of Denmark.
- Pleiss, G., Chen, D., Huang, G., Li, T., Van Der Maaten, L., & Weinberger, K. Q. (2017). Memory-efficient implementation of densenets.
- Polyak, B. T. (1964). Some methods of speeding up the convergence of iteration methods. USSR Computational Mathematics and Mathematical
- Prakash, A., Hasan, S. A., Lee, K., Datla, V., Qadir, A., Liu, J., & Farri, O. (2016). Neural paraphrase generation with stacked
- Qin, C., Zhang, A., Zhang, Z., Chen, J., Yasunaga, M., & Yang, D. (2023). Is ChatGPT a general-purpose natural language processing task
- Quadrana, M., Cremonesi, P., & Jannach, D. (2018). Sequence-aware recommender systems. ACM Computing Surveys, 51(4), 66.
- Quinlan, J. R. (1993). C4.5: Programs for Machine Learning. Elsevier.
- Rabiner, L., & Juang, B.-H. (1993). Fundamentals of Speech Recognition. Prentice-Hall.
- Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., … et al. (2021). Learning transferable visual models from
- Radford, A., Metz, L., & Chintala, S. (2015). Unsupervised representation learning with deep convolutional generative adversarial
- Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018). Improving language understanding by generative pre-training. OpenAI.
- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019). Language models are unsupervised multitask learners.
- Radosavovic, I., Johnson, J., Xie, S., Lo, W.-Y., & Dollár, P. (2019). On network design spaces for visual recognition. Proceedings of
- Radosavovic, I., Kosaraju, R. P., Girshick, R., He, K., & Dollár, P. (2020). Designing network design spaces. Proceedings of the IEEE/
- Rae, J. W., Borgeaud, S., Cai, T., Millican, K., Hoffmann, J., Song, F., … et al. (2021). Scaling language models: methods, analysis &
- Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., … Liu, P. J. (2020). Exploring the limits of transfer learning
- Rajpurkar, P., Zhang, J., Lopyrev, K., & Liang, P. (2016). SQuAD: 100,000+ questions for machine comprehension of text. ArXiv:1606.
- Ramachandran, P., Parmar, N., Vaswani, A., Bello, I., Levskaya, A., & Shlens, J. (2019). Stand-alone self-attention in vision models.
- Ramachandran, P., Zoph, B., & Le, Q. V. (2017). Searching for activation functions. ArXiv:1710.05941.
- Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., & Chen, M. (2022). Hierarchical text-conditional image generation with clip latents.
- Ramón y Cajal, Santiago, & Azoulay, L. (1894). Les Nouvelles Idées sur la Structure du Système Nerveux chez l'Homme et chez les
- Ranzato, M.-A., Boureau, Y.-L., Chopra, S., & LeCun, Y. (2007). A unified energy-based framework for unsupervised learning. Artificial
- Rasmussen, C. E., & Williams, C. K. (2006). Gaussian Processes for Machine Learning. MIT Press.
- Reddi, S. J., Kale, S., & Kumar, S. (2019). On the convergence of Adam and beyond. ArXiv:1904.09237.
- Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016). You only look once: unified, real-time object detection. Proceedings of
- Redmon, J., & Farhadi, A. (2018). YOLOv3: an incremental improvement. ArXiv:1804.02767.
- Reed, S., & De Freitas, N. (2015). Neural programmer-interpreters. ArXiv:1511.06279.
- Reed, S., Zolna, K., Parisotto, E., Colmenarejo, S. G., Novikov, A., Barth-Maron, G., … et al. (2022). A generalist agent. ArXiv:2205.
- Ren, S., He, K., Girshick, R., & Sun, J. (2015). Faster R-CNN: towards real-time object detection with region proposal networks.
- Rendle, S. (2010). Factorization machines. 2010 IEEE International Conference on Data Mining (pp. 995–1000).
- Rendle, S., Freudenthaler, C., Gantner, Z., & Schmidt-Thieme, L. (2009). BPR: Bayesian personalized ranking from implicit feedback.
- Revels, J., Lubin, M., & Papamarkou, T. (2016). Forward-mode automatic differentiation in Julia. ArXiv:1607.07892.
- Rezende, D. J., Mohamed, S., & Wierstra, D. (2014). Stochastic backpropagation and approximate inference in deep generative models.
- Riesenhuber, M., & Poggio, T. (1999). Hierarchical models of object recognition in cortex. Nature Neuroscience, 2(11), 1019–1025.
- Rockafellar, R. T. (1970). Convex Analysis. Princeton University Press.
- Rolnick, D., Veit, A., Belongie, S., & Shavit, N. (2017). Deep learning is robust to massive label noise. ArXiv:1705.10694.
- Rudin, W. (1973). Functional Analysis. McGraw-Hill.
- Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1988). Learning representations by back-propagating errors. Cognitive Modeling, 5
- Russakovsky, O., Deng, J., Huang, Z., Berg, A. C., & Fei-Fei, L. (2013). Detecting avocados to zucchinis: what have we done, and where
- Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., … et al. (2015). ImageNet large scale visual recognition
- Russell, S. J., & Norvig, P. (2016). Artificial Intelligence: A Modern Approach. Pearson Education Limited.
- Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E., … et al. (2022). Photorealistic text-to-image diffusion models with
- Salinas, D., Seeger, M., Klein, A., Perrone, V., Wistuba, M., & Archambeau, C. (2022). Syne Tune: a library for large scale
- Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter.
- Sanh, V., Webson, A., Raffel, C., Bach, S. H., Sutawika, L., Alyafeai, Z., … et al. (2021). Multitask prompted training enables
- Santurkar, S., Tsipras, D., Ilyas, A., & Madry, A. (2018). How does batch normalization help optimization? Advances in Neural
- Sarwar, B. M., Karypis, G., Konstan, J. A., & Riedl, J. (2001). Item-based collaborative filtering recommendation algorithms.
- Scao, T. L., Fan, A., Akiki, C., Pavlick, E., Ilić, S., Hesslow, D., … et al. (2022). BLOOM: a 176B-parameter open-access multilingual
- Schein, A. I., Popescul, A., Ungar, L. H., & Pennock, D. M. (2002). Methods and metrics for cold-start recommendations. Proceedings of
- Schuhmann, C., Beaumont, R., Vencu, R., Gordon, C., Wightman, R., Cherti, M., … et al. (2022). LAION-5B: an open large-scale dataset
- Schuster, M., & Paliwal, K. K. (1997). Bidirectional recurrent neural networks. IEEE Transactions on Signal Processing, 45(11),
- Schölkopf, B., Herbrich, R., & Smola, A. J. (2001). Helmbold, D. P., & Williamson, B. (Eds.). A generalized representer theorem.
- Schölkopf, B., Burges, C., & Vapnik, V. (1996). Incorporating invariances in support vector learning machines. International Conference
- Schölkopf, B., & Smola, A. J. (2002). Learning with Kernels: Support Vector Machines, Regularization, Optimization, and Beyond. MIT
- Sedhain, S., Menon, A. K., Sanner, S., & Xie, L. (2015). Autorec: autoencoders meet collaborative filtering. Proceedings of the 24th
- Sennrich, R., Haddow, B., & Birch, A. (2015). Neural machine translation of rare words with subword units. ArXiv:1508.07909.
- Sergeev, A., & Del Balso, M. (2018). Horovod: fast and easy distributed deep learning in TensorFlow. ArXiv:1802.05799.
- Shannon, C. E. (1948). A mathematical theory of communication. The Bell System Technical Journal, 27(3), 379–423.
- Shao, H., Yao, S., Sun, D., Zhang, A., Liu, S., Liu, D., … Abdelzaher, T. (2020). ControlVAE: controllable variational autoencoder.
- Shaw, P., Uszkoreit, J., & Vaswani, A. (2018). Self-attention with relative position representations. ArXiv:1803.02155.
- Shoeybi, M., Patwary, M., Puri, R., LeGresley, P., Casper, J., & Catanzaro, B. (2019). Megatron-LM: training multi-billion parameter
- Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., Van Den Driessche, G., … et al. (2016). Mastering the game of Go with deep
- Silverman, B. W. (1986). Density Estimation for Statistical and Data Analysis. Chapman and Hall.
- Simard, P. Y., LeCun, Y. A., Denker, J. S., & Victorri, B. (1998). Transformation invariance in pattern recognition – tangent distance
- Simonyan, K., & Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. ArXiv:1409.1556.
- Sindhwani, V., Sainath, T. N., & Kumar, S. (2015). Structured transforms for small-footprint deep learning. ArXiv:1510.01722.
- Sivic, J., & Zisserman, A. (2003). Video Google: a text retrieval approach to object matching in videos. Proceedings of the IEEE
- Smith, S., Patwary, M., Norick, B., LeGresley, P., Rajbhandari, S., Casper, J., … et al. (2022). Using DeepSpeed and Megatron to train
- Smola, A., & Narayanamurthy, S. (2010). An architecture for parallel topic models. Proceedings of the VLDB Endowment, 3(1-2), 703–710.
- Snoek, J., Larochelle, H., & Adams, R. (2012). Practical Bayesian optimization of machine learning algorithms. Advances in Neural
- Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., & Ganguli, S. (2015). Deep unsupervised learning using nonequilibrium
- Song, Y., & Ermon, S. (2019). Generative modeling by estimating gradients of the data distribution. Advances in Neural Information
- Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-based generative modeling through
- Speelpenning, B. (1980). Compiling fast partial derivatives of functions given by algorithms (Doctoral dissertation). University of
- Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid, A., Fisch, A., … et al. (2022). Beyond the imitation game: quantifying and
- Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). Dropout: a simple way to prevent neural networks
- Srivastava, R. K., Greff, K., & Schmidhuber, J. (2015). Highway networks. ArXiv:1505.00387.
- Strang, G. (1993). Introduction to Linear Algebra. Wellesley–Cambridge Press.
- Su, X., & Khoshgoftaar, T. M. (2009). A survey of collaborative filtering techniques. Advances in Artificial Intelligence, 2009.
- Sukhbaatar, S., Weston, J., & Fergus, R. (2015). End-to-end memory networks. Advances in Neural Information Processing Systems (pp.
- Sutskever, I., Martens, J., Dahl, G., & Hinton, G. (2013). On the importance of initialization and momentum in deep learning.
- Sutskever, I., Vinyals, O., & Le, Q. V. (2014). Sequence to sequence learning with neural networks. Advances in Neural Information
- Szegedy, C., Ioffe, S., Vanhoucke, V., & Alemi, A. A. (2017). Inception-v4, Inception-ResNet and the impact of residual connections on
- Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., … Rabinovich, A. (2015). Going deeper with convolutions.
- Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., & Wojna, Z. (2016). Rethinking the Inception architecture for computer vision.
- Tallec, C., & Ollivier, Y. (2017). Unbiasing truncated backpropagation through time. ArXiv:1705.08209.
- Tan, M., & Le, Q. (2019). EfficientNet: rethinking model scaling for convolutional neural networks. International Conference on Machine
- Tang, J., & Wang, K. (2018). Personalized top-n sequential recommendation via convolutional sequence embedding. Proceedings of the
- Taskar, B., Guestrin, C., & Koller, D. (2004). Max-margin Markov networks. Advances in Neural Information Processing Systems, 16, 25.
- Tay, Y., Dehghani, M., Bahri, D., & Metzler, D. (2020). Efficient transformers: a survey. ArXiv:2009.06732.
- Taylor, R., Kardas, M., Cucurull, G., Scialom, T., Hartshorn, A., Saravia, E., … Stojnic, R. (2022). Galactica: a large language model
- Teye, M., Azizpour, H., & Smith, K. (2018). Bayesian uncertainty estimation for batch normalized deep networks. ArXiv:1802.06455.
- Thomee, B., Shamma, D. A., Friedland, G., Elizalde, B., Ni, K., Poland, D., … Li, L.-J. (2016). Yfcc100m: the new data in multimedia
- Tieleman, T., & Hinton, G. (2012). Divide the gradient by a running average of its recent magnitude. COURSERA: Neural Networks for
- Tikhonov, A. N., & Arsenin, V. Y. (1977). Solutions of Ill-Posed Problems. W.H. Winston.
- Tolstikhin, I. O., Houlsby, N., Kolesnikov, A., Beyer, L., Zhai, X., Unterthiner, T., … et al. (2021). MLP-mixer: an all-MLP
- Torralba, A., Fergus, R., & Freeman, W. T. (2008). 80 million tiny images: a large data set for nonparametric object and scene
- Touvron, H., Cord, M., Douze, M., Massa, F., Sablayrolles, A., & Jégou, H. (2021). Training data-efficient image transformers &
- Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, T., … et al. (2023a). LLaMA: open and efficient foundation
- Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., … et al. (2023b). LLaMA 2: open foundation and fine-tuned
- Tsoumakas, G., & Katakis, I. (2007). Multi-label classification: an overview. International Journal of Data Warehousing and Mining, 3
- Turing, A. (1950). Computing machinery and intelligence. Mind, 59(236), 433.
- Töscher, A., Jahrer, M., & Bell, R. M. (2009). The bigchaos solution to the Netflix grand prize.
- Uijlings, J. R., Van De Sande, K. E., Gevers, T., & Smeulders, A. W. (2013). Selective search for object recognition. International
- Vapnik, V. (1995). The Nature of Statistical Learning Theory. New York: Springer.
- Vapnik, V. (1998). Statistical Learning Theory. New York: John Wiley and Sons.
- Vapnik, V., & Chervonenkis, A. (1964). A note on one class of perceptrons. Automation and Remote Control, 25.
- Vapnik, V., & Chervonenkis, A. (1968). Uniform convergence of frequencies of occurence of events to their probabilities. Dokl. Akad.
- Vapnik, V., & Chervonenkis, A. (1971). On the uniform convergence of relative frequencies of events to their probabilities. Theory
- Vapnik, V., & Chervonenkis, A. (1981). The necessary and sufficient conditions for the uniform convergence of averages to their
- Vapnik, V., & Chervonenkis, A. (1991). The necessary and sufficient conditions for consistency in the empirical risk minimization
- Vapnik, V. N., & Chervonenkis, A. Y. (1974). Ordered risk minimization. Automation and Remote Control, 35, 1226–1235, 1403–1412.
- Vapnik, V. (1992). Principles of risk minimization for learning theory. Advances in Neural Information Processing Systems (pp. 831–838).
- Vapnik, V., Levin, E., & Le Cun, Y. (1994). Measuring the VC-dimension of a learning machine. Neural Computation, 6(5), 851–876.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … Polosukhin, I. (2017). Attention is all you need.
- Wahba, G. (1990). Spline Models for Observational Data. SIAM.
- Waibel, A., Hanazawa, T., Hinton, G., Shikano, K., & Lang, K. J. (1989). Phoneme recognition using time-delay neural networks. IEEE
- Wang, H., Zhang, A., Zheng, S., Shi, X., Li, M., & Wang, Z. (2022). Removing batch normalization boosts adversarial training.
- Wang, L., Li, M., Liberty, E., & Smola, A. J. (2018). Optimal message scheduling for aggregation. Networks, 2(3), 2–3.
- Wang, Q., Li, B., Xiao, T., Zhu, J., Li, C., Wong, D. F., & Chao, L. S. (2019). Learning deep transformer models for machine
- Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., & Zhou, D. (2023). Self-consistency improves chain of thought reasoning in language
- Wang, Y., Davidson, A., Pan, Y., Wu, Y., Riffel, A., & Owens, J. D. (2016). Gunrock: a high-performance graph processing library on the
- Warstadt, A., Singh, A., & Bowman, S. R. (2019). Neural network acceptability judgments. Transactions of the Association for
- Wasserman, L. (2013). All of Statistics: A Concise Course in Statistical Inference. Springer.
- Watkins, C. J., & Dayan, P. (1992). Q-learning. Machine Learning, 8(3–4), 279–292.
- Watson, G. S. (1964). Smooth regression analysis. Sankhyā: The Indian Journal of Statistics, Series A, pp. 359–372.
- Wei, J., Bosma, M., Zhao, V. Y., Guu, K., Yu, A. W., Lester, B., … Le, Q. V. (2021). Finetuned language models are zero-shot learners.
- Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., … et al. (2022). Emergent abilities of large language models.
- Wei, J., Wang, X., Schuurmans, D., Bosma, M., Chi, E., Le, Q., & Zhou, D. (2022). Chain of thought prompting elicits reasoning in large
- Welling, M., & Teh, Y. W. (2011). Bayesian learning via stochastic gradient Langevin dynamics. Proceedings of the 28th International
- Wengert, R. E. (1964). A simple automatic derivative evaluation program. Communications of the ACM, 7(8), 463–464.
- Werbos, P. J. (1990). Backpropagation through time: what it does and how to do it. Proceedings of the IEEE, 78(10), 1550–1560.
- Wigner, E. P. (1958). On the distribution of the roots of certain symmetric matrices. Ann. Math. (pp. 325–327).
- Wilson, A. G., & Izmailov, P. (2020). Bayesian deep learning and a probabilistic perspective of generalization. Advances in Neural
- Wistuba, M., Rawat, A., & Pedapati, T. (2019). A survey on neural architecture search. ArXiv:1905.01392 [cs.LG].
- Wistuba, M., Schilling, N., & Schmidt-Thieme, L. (2018). Scalable Gaussian process-based transfer surrogates for hyperparameter
- Wolpert, D. H., & Macready, W. G. (1995). No free lunch theorems for search. Technical Report SFI-TR-95-02-010, Santa Fe Institute.
- Wood, F., Gasthaus, J., Archambeau, C., James, L., & Teh, Y. W. (2011). The sequence memoizer. Communications of the ACM, 54(2), 91–98.
- Wu, B., Wan, A., Yue, X., Jin, P., Zhao, S., Golmant, N., … Keutzer, K. (2018). Shift: a zero flop, zero parameter alternative to
- Wu, Y., Schuster, M., Chen, Z., Le, Q. V., Norouzi, M., Macherey, W., … et al. (2016). Google's neural machine translation system:
- Xiao, H., Rasul, K., & Vollgraf, R. (2017). Fashion-MNIST: a novel image dataset for benchmarking machine learning algorithms.
- Xiao, L., Bahri, Y., Sohl-Dickstein, J., Schoenholz, S., & Pennington, J. (2018). Dynamical isometry and a mean field theory of CNNs:
- Xie, S., Girshick, R., Dollár, P., Tu, Z., & He, K. (2017). Aggregated residual transformations for deep neural networks. Proceedings
- Xiong, R., Yang, Y., He, D., Zheng, K., Zheng, S., Xing, C., … Liu, T. (2020). On layer normalization in the transformer architecture.
- Xiong, W., Wu, L., Alleva, F., Droppo, J., Huang, X., & Stolcke, A. (2018). The Microsoft 2017 conversational speech recognition
- Yamaguchi, K., Sakamoto, K., Akabane, T., & Fujimoto, Y. (1990). A neural network for speaker-independent isolated word recognition.
- Yang, Z., Hu, Z., Deng, Y., Dyer, C., & Smola, A. (2016). Neural machine translation with recurrent attention modeling. ArXiv:1607.
- Yang, Z., Moczulski, M., Denil, M., De Freitas, N., Smola, A., Song, L., & Wang, Z. (2015). Deep fried convnets. Proceedings of the
- Ye, M., Yin, P., Lee, W.-C., & Lee, D.-L. (2011). Exploiting geographical influence for collaborative point-of-interest recommendation.
- You, Y., Gitman, I., & Ginsburg, B. (2017). Large batch training of convolutional networks. ArXiv:1708.03888.
- Yu, J., Xu, Y., Koh, J. Y., Luong, T., Baid, G., Wang, Z., … Wu, Y. (2022). Scaling autoregressive models for content-rich
- Zaheer, M., Reddi, S., Sachan, D., Kale, S., & Kumar, S. (2018). Adaptive methods for nonconvex optimization. Advances in Neural
- Zeiler, M. D. (2012). ADADELTA: an adaptive learning rate method. ArXiv:1212.5701.
- Zeiler, M. D., & Fergus, R. (2013). Stochastic pooling for regularization of deep convolutional neural networks. ArXiv:1301.3557.
- Zhang, A., Tay, Y., Zhang, S., Chan, A., Luu, A. T., Hui, S. C., & Fu, J. (2021). Beyond fully-connected layers with quaternions:
- Zhang, C., Bengio, S., Hardt, M., Recht, B., & Vinyals, O. (2021). Understanding deep learning (still) requires rethinking
- Zhang, S., Yao, L., Sun, A., & Tay, Y. (2019). Deep learning based recommender system: a survey and new perspectives. ACM Computing
- Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., … et al. (2022). OPT: open pre-trained transformer language models.
- Zhang, W., Tanida, J., Itoh, K., & Ichioka, Y. (1988). Shift-invariant pattern recognition neural network and its optical architecture.
- Zhang, Y., Sun, P., Jiang, Y., Yu, D., Yuan, Z., Luo, P., … Wang, X. (2021). ByteTrack: multi-object tracking by associating every
- Zhang, Z., Zhang, A., Li, M., & Smola, A. (2023). Automatic chain of thought prompting in large language models. International
- Zhang, Z., Zhang, A., Li, M., Zhao, H., Karypis, G., & Smola, A. (2023). Multimodal chain-of-thought reasoning in language models.
- Zhao, Z.-Q., Zheng, P., Xu, S.-t., & Wu, X. (2019). Object detection with deep learning: a review. IEEE Transactions on Neural Networks
- Zhou, D., Schärli, N., Hou, L., Wei, J., Scales, N., Wang, X., … Chi, E. (2023). Least-to-most prompting enables complex reasoning in
- Zhu, J.-Y., Park, T., Isola, P., & Efros, A. A. (2017). Unpaired image-to-image translation using cycle-consistent adversarial
- Zhu, Y., Kiros, R., Zemel, R., Salakhutdinov, R., Urtasun, R., Torralba, A., & Fidler, S. (2015). Aligning books and movies: towards
- Zoph, B., & Le, Q. V. (2016). Neural architecture search with reinforcement learning. ArXiv:1611.01578.
