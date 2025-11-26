# Slide 19 of Lecture 12 contains information about the Learning Rate Scheduling.

• Good learning rate is very important.
• If you set it much too high, training may diverge (“Gradient Descent”)
• If you set it too low, training will eventually converge to optimum, at cost of
very long time.
• Find a good learning rate by:
• Training model for a few hundred iterations, exponentially increasing learning
rate from a very small value to a very large value.
• Next look at learning curve and pick a learning rate slightly lower than one at
which learning curve starts shooting back up.
• Reinitialize model and train it with that learning rate.
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron, 2019
