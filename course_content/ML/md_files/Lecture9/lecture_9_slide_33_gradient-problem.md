# Slide 33 of Lecture 9 contains information about the Gradient Problem.

• Vanishing Gradient Problem: When gradients are very small, they can diminish as they are
propagated back through network, leading to minimal or no updates to weights in initial
layers.
• Reasons: Choice of activation functions, NN architecture.
• Solution: Activation Functions: ReLU, Proper weight initialization, Batch Norm.
• Exploding Gradient Problem: When gradients of network's loss with respect to parameters
(weights) become excessively large. The "explosion" of the gradient can lead to numerical
instability and inability of the network to converge to a suitable solution.
• How to check? Monitore gradients and check loss function showing unusually large
fluctuations or becoming NaN.
• Solution: Proper activation function choice, Batch Norm.
36
