# Slide 37 of Lecture 13 contains information about the Recap: GANs.

GANs are a framework for training generative models.
•
These models learn to map random noise vectors to outputs that resemble a particular data
•
distribution, such as images.
Core idea: To have two neural networks compete against each other:
•
Generator Network: This network takes a random distribution (typically Gaussian) as input and
•
tries to produce realistic-looking samples, such as images.
Discriminator Network: This network takes either a fake image from the generator or a real
•
image from the training set as input.
Each training iteration in a GAN is divided into two phases:
•
Discriminator Training: A batch of real images (labelled as 1) is sampled from the training set
•
and combined with an equal number of fake images (labelled as 0) produced by the generator.
Generator Training: The generator produces another batch of fake images. The discriminator is
•
then used to evaluate these fake images, but this time all the labels are set to 1 (real).
The constant competition between the generator and discriminator can lead to a situation where
•
neither network improves significantly, and the process does not converge to a stable equilibrium.
