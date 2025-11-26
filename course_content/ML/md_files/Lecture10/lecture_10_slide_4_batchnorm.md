# Slide 4 of Lecture 10 contains information about the BatchNorm.

• Vanishing gradients problem can be alleviated with better weight initialization, better
optimizers or Batch Normalization[1].
• BatchNorm most successful architectural innovations in deep learning[2].
• BatchNorm aims to stabilize distribution (over a minibatch) of inputs to a given network
layer during training.
• BatchNorm Working: Operation lets model learn optimal scale and mean of each of layer’s
inputs.
1. First add an operation in model just before or after activation function of each hidden
layer. This operation simply zero-center and normalizes each input.
2. Next, scales and shifts result using scaling and shifting vectors [per layer].
1.Sergey Ioffe and Christian Szegedy, “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift,” Proceedings of the 32nd International Conference on Machine Learning (2015): 448–456.
2. Santurkar, Shibani, et al. "How does batch normalization help optimization?."Advances in Neural Information Processing Systems. 2018.
