# Slide 10 of Lecture 12 contains information about the Convolution Autoencoder.

• If you want to build an autoencoder for images, you need to build a convolutional
autoencoder.
• Encoder is a regular CNN composed of convolutional layers and pooling
layers.
• It reduces spatial dimensionality of inputs (i.e., height and width)
while increasing depth (i.e., number of feature maps).
• Decoder must do reverse (upscale image and reduce its depth back to
original dimensions), and for this use transpose convolutional layers.
10
