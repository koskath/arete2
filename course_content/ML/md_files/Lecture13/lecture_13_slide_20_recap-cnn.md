# Slide 20 of Lecture 13 contains information about the Recap: CNN.

CNN consists of Convolutional layer, Pooling layer, and Fully connected layer.
•
Convolutional layer is made up of filters (convolution kernels) and feature maps.
•
Key considerations for designing a convolutional layer include:
•
Filter size: A neuron’s weights can be represented as a small image size, which is
•
its receptive field.
Stride of filter: determines how many pixel steps the filter takes when moving
•
across the image (a stride of 1 is typical).
Pooling layers typically follow one or more convolutional layers.
•
Goal is to reduce the feature map size from the convolutional layer.
•
All neurons within a feature map share the same parameters.
•
Training Process:
•
Forward Propagation: No learning occurs in the pooling layers.
•
Backpropagation: Network's weights are adjusted based on the error in its
•
predictions. convolutional layers require a huge amount of RAM.
