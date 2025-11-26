# Slide 36 of Lecture 13 contains information about the Deep Convolutional GANs: DCGANs.

•
DCGANs (2015): Based on deeper convolutional nets for larger images.
•
Guidelines to building DCGANs:
•
Replace any pooling layers with strided convolutions (discriminator) and transposed
convolutions (generator).
•
Use Batch Normalization in both generator and discriminator, except in generator’s
output layer and discriminator’s input layer.
•
Remove fully connected hidden layers for deeper architectures.
•
Use ReLU activation in generator for all layers except output layer, which should use
tanh.
•
Use leaky ReLU activation in discriminator for all layers.
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron
