# Slide 12 of Lecture 12 contains information about the Recap.

Autoencoders learn to copy their inputs to their outputs by converting inputs into an
•
efficient latent representation and then outputting something close to the original inputs.
Structure: An autoencoder is composed of two main parts:
•
Encoder (or recognition network): Converts inputs to a latent representation.
•
Decoder (or generative network): Converts the internal representation back to
•
outputs.
The cost function of an autoencoder contains a reconstruction loss that penalises the
•
model when the reconstructions differ from the inputs.
An autoencoder has the same architecture as a Multilayer Perceptron (MLP), except that
•
the number of neurons in the output layer must be equal to the number of inputs.
A recurrent autoencoder typically has an encoder that is a sequence-to-vector RNN
•
compressing the input sequence into a single vector, and a decoder that is a vector-to-
sequence RNN doing the reverse.
Applications: Autoencoders are useful for dimensionality reduction (good for visualization)
•
12
