# Slide 10 of Lecture 13 contains information about the Design Convolutional layer.

• Considerations to design convolutional layer:
• Filter size: Neuron’s weights can be represented as a small image size of receptive
field.
• Filters are small matrix used to detect patterns in an image.
• Different filters detect edges, textures, and shapes.
• A n×n filter slides over image and performs dot product (convolution).
• Stride of filter: [Step Size] determines how many pixel steps filter makes when moving
from one image activation to another (default 1).
• Padding for input layer: Zero padding is used to pad borders of image pixels with a
defined layer of zeros.
• Larger stride --> smaller feature map (less details, faster)
