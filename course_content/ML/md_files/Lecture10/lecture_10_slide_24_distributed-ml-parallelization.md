# Slide 24 of Lecture 10 contains information about the Distributed ML: Parallelization.

•
Parallelization methods in DL: data, model and pipeline. Hybrid as well.
• In data parallelism, a number of
machines loads an identical copy
of a DL model.
• Training data split into non-
overlapping chunks and fed into
model replicas of workers for
training.
• Each worker performs training on
its training data, which leads to
updates of model parameters.
• Hence, model parameters
between workers need to be
synchronized.
24
Mayer, Ruben, and Hans-Arno Jacobsen. "Scalable deep learning on distributed infrastructures: Challenges, techniques, and tools."ACM Computing Surveys (CSUR)53.1 (2020): 1-37.
