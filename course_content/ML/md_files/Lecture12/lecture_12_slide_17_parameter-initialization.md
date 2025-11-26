# Slide 17 of Lecture 12 contains information about the Parameter Initialization.

• Parameter initialization is crucial to NN performance:
• Can’t initialize weights in same layer to same value, or they will stay same.
• Can’t initialize weights too large, it will take too long to learn.
• A traditional random initialization:
• Initialize bias variables to 0.
• Sample from standard normal, divided by 105(0.00001*randn).
• w = .00001*randn(k,1)
• Performing multiple initializations does not seem to be important.
• Popular approach from 10 years ago:
• Initialize with deep unsupervised model (like “autoencoders”)
