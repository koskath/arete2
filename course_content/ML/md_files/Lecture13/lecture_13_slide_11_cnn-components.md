# Slide 11 of Lecture 13 contains information about the CNN Components.

• Feature Maps are output matrix of a filter in a convolutional layer.
• Expose patterns of input image (such as horizontal lines, vertical lines).
• Multiple filters = Multiple feature maps.
• Deeper CNN: Inputs to a deeper convolutional layer are feature maps of previous layer.
• Pooling layer summarizes image features learned in previous network layers.
• Pooling Layer: follow one or more convolutional layers.
• Common type of pooling layer is Max pooling layer.
• Goal: to reduce feature map of convolutional layer.
If we have a 32×32 RGB image and
apply 32 filters, we get 32 feature
maps.
Reason: Each filter processes the
image to extract different features,
resulting in a separate feature map
for each filter.
