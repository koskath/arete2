# Slide 13 of Lecture 14 contains information about the TL Steps.

Three steps in transfer learning:
1. Select a pre-trained model with prior knowledge for a related task.
2. Configure pre-trained model using two main methods.
I. Freeze pre-trained layers: to preserve source knowledge.
I. Initially set to random values, weights are adjusted during the
training process.
II. Remove last layer of the pre-trained model.
II. Introduce new layers: on top of pre-trained model for new task.
3. Train for target domain.
https://aws.amazon.com/what-is/transfer-learning/
