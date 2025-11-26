# Slide 22 of Lecture 12 contains information about the Hyper-parameters.

• Make random sample of hyperparameters uniformly within grid range.
• Logarithms of hyperparameters are sampled uniformly rather than hyperparameters
themselves (regularization rate and learning rate).
• Ex: instead of sampling learning rate (alpha) between 0.1 and 0.001, first sample log(α)
uniformly between −1 and −3, and then exponentiate it to power of 10.
• Common to search in logarithmic space
