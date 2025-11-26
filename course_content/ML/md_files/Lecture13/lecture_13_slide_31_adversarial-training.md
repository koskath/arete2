# Slide 31 of Lecture 13 contains information about the Adversarial Training.

• Models learns to classify correctly adversarial examples.
• Classifiers uses a loss function to minimize model prediction errors.
• After training, attacker uses loss function to maximize model prediction error
• 1. Compute its gradient with respect to model input
• 2. Take the sign of gradient and multiply it by a threshold
• Normal (top)
• Noisy (middle)
• Adversarial (bottom)
