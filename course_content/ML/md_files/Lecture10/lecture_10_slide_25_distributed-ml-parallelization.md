# Slide 25 of Lecture 10 contains information about the Distributed ML: Parallelization.

•
Model parallelism: DL model is split, and each worker loads a different part of DL model for
training.
•
Worker(s) hold input layer of DL model are fed with training data.
•
In forward pass, they compute their output signal which is propagated to workers that hold
next layer of DL model.
•
In backpropagation pass, gradients are computed starting at workers that hold output layer
of DL model, propagating to workers that hold input layers of DL model.
25
Mayer, Ruben, and Hans-Arno Jacobsen. "Scalable deep learning on distributed infrastructures: Challenges, techniques, and tools."ACM Computing Surveys (CSUR)53.1 (2020): 1-37.
