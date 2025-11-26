# Slide 11 of Lecture 12 contains information about the Recurrent & Denoising Autoencoders.

• If you want to build an autoencoder for sequences (such as time series or dimensionality
reduction), then RNNs may be better suited than dense networks.
• Recurrent autoencoder:
• Encoder is typically a sequence-to-vector RNN which compresses input sequence
down to a single vector.
• Decoder is a vector-to-sequence RNN that does reverse.
• Denoising Autoencoders: force autoencoder to learn useful features by adding noise to
its inputs, training it to recover original (noise-free).
• Noise can be pure Gaussian noise added to inputs, or it can be randomly switched-off
inputs (dropout).
• Autoencoders could also be used for feature extraction*.
11
*Pascal Vincent et al., “Extracting and Composing Robust Features with Denoising Autoencoders,” Proceedings of the 25th International Conference on Machine Learning (2008): 1096–1103.
