# Slide 38 of Lecture 14 contains information about the Summary (1/2).

• Federated Learning (FL) is a method to train AI models collaboratively on
decentralised data without the need to share confidential user data.
• FL works by each party downloading a model, training it on their private data,
encrypting model updates, and sending them to a server for aggregation into a
centralised model, which is then sent back for further iterative training.
• Transfer Learning (TL) involves fine-tuning a model pre-trained on one task for
a new, related task, offering time and cost savings.
• Strategies: 1. Transductive TL (transferring knowledge between related
domains with little or no labelled target data), 2. inductive TL (source and
target domains are the same, but tasks differ), and 3. unsupervised TL
(applying when source and target domains are unlabelled).
