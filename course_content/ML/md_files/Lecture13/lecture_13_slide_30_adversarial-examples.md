# Slide 30 of Lecture 13 contains information about the Adversarial Examples.

• Fast Gradient Sign Method (FGSM) effective method to generate adversarial images.
1. Take input image --> Make prediction (using CNN).
2. Compute loss of prediction based on true class label.
3. Calculate gradients of loss with respect to input image.
4. Compute gradient sign --> Use to construct adversarial image (output).
Goodfellow et al. Explaining and Harnessing Adversarial Examples
