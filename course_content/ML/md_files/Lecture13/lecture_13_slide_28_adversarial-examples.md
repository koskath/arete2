# Slide 28 of Lecture 13 contains information about the Adversarial Examples.

• Two types of attacks in DL: White-Box and Black-Box attacks
• White-Box: Attacker has access to training method (data/network initialization/
algorithm/hyperparameter).
• Small perturbations --> bad performance.
• Black-Box attacks: Attacker does not have complete access to network training method.
• We need robust models: weight decay and dropout do not work.
• Approach: Brute force method to generate adversarial examples and train model using them
(Adversarial training).
