# Slide 6 of Lecture 10 contains information about the BatchNorm.

• Batch Normalization is tricky to use in RNNs but sufficient for other nets.
• Gradient Clipping* is often used RNNs to mitigate exploding gradients problem.
• Gradient Clipping clips the gradients during backpropagation so that they never exceed
some threshold.
• Gradient clipping does not help with vanishing gradients.
• BN acts like a regularizer reducing need for other regularization techniques (such as
dropout).
• BN adds runtime penalty to neural network.
• Training is rather slow because each epoch takes much more time when BN in use.
*Pascanu, Razvan, Tomas Mikolov, and Yoshua Bengio. "On the difficulty of training recurrent neural networks."International conference on machine learning. 2013.
