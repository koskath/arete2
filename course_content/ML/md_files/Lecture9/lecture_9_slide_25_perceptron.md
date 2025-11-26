# Slide 25 of Lecture 9 contains information about the Perceptron.

• How is a Perceptron trained?
• Perceptron training algorithm was largely inspired by Hebb’s rule (or Hebbian learning).
• Process:
1. Perceptron is fed one training instance at a time, and for each instance it makes its
predictions.
2. For every output neuron that produced a wrong prediction, it reinforces the connection
weights from the inputs that would have contributed to the correct prediction.
• Heaviside step function used in Perceptrons.
• Common step functions used in Perceptrons (assuming threshold = 0)
signum function extracts
the sign of a real number z.
27
• Perceptron and SGDClassifier both have similar implementation.
