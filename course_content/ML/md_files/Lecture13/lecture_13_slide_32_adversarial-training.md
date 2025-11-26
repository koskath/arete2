# Slide 32 of Lecture 13 contains information about the Adversarial training.

• Adversarial training is process of training a model to correctly classify both
unmodified examples and adversarial examples.
• Adv: robust adversarial examples, generalize performance for original
examples.
• Virtual adversarial training [VAT]* extends idea of adversarial training to semi-
supervised regime and unlabelled examples.
• VAT uses an efficient approximation to maximize the likelihood of the model
while promoting the model’s local distributional smoothness on each training
input data point.
• Traditional adversarial and virtual adversarial training can be interpreted as
regularization strategy and as defence against malicious inputs.
*Takeru Miyato, Shin-ichi Maeda, Masanori Koyama, Ken Nakae, and Shin Ishii. Distributional smoothing with virtual adversarial training. In ICLR, 2016.
