# Slide 7 of Lecture 12 contains information about the Autoencoder.

• Cost function contains a reconstruction loss that penalizes model when
reconstructions are different from inputs.
• Undercomplete autoencoder where internal representation has a lower
dimensionality than input data.
• An undercomplete autoencoder cannot trivially copy its inputs to codings, and
forced to learn most important features in input data (and drop unimportant
ones).
• If autoencoder uses only linear activations and cost function is mean squared error
(MSE), then it ends up performing Principal Component Analysis (PCA).
7
