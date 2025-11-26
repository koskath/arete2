# Slide 12 of Lecture 13 contains information about the Choosing "Correct" Kernel Size.

• Kernel size determines the receptive field of each convolutional operation.
• kernel size should be chosen based on the data characteristics.
• Detection of fine-grained details --> smaller kernel sizes [capture local information].
• Detection of larger patterns --> larger kernel sizes [capture global information].
• Smaller input sizes works well with smaller kernel sizes.
• Larger input sizes can accommodate larger kernel sizes [resource intensive].
• Stacking multiple layers with small kernel sizes can help preserve information.
• Very large kernel sizes may result in over smoothing or loss of fine-grained details.
