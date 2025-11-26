# Slide 5 of Lecture 14 contains information about the How does FL works?.

1. Multiple people remotely share their data to collaboratively train a model.
2. Each party downloads model from a server, usually a pre-trained model.
3. Train it on their private data, then summarize and encrypt model’s new
configuration.
4. Model updates are sent back to server, decrypted, averaged, and integrated
into centralized model.
5. Collaborative training continues (iteratively) until model is fully trained.
https://research.ibm.com/blog/what-is-federated-learning
