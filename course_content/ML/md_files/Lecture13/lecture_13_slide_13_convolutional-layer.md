# Slide 13 of Lecture 13 contains information about the Convolutional Layer.

• Neurons in first convolutional layer are connected
only to pixels in their receptive fields (BUT not to
all pixels).
• Each neuron in second convolutional layer is
connected only to neurons located within a small
rectangle in first layer.
• It allows network to concentrate on small low-level
features in first hidden layer, then assemble them
into larger higher-level features in next hidden layer,
and so on.
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron
