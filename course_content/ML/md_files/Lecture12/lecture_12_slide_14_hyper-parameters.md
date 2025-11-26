# Slide 14 of Lecture 12 contains information about the Hyper-parameters.

• NNs have several hyperparameters: learning rate, weight of regularization.
• “Hyperparameter” regulate design of model.
• Different from more fundamental parameters representing weights of connections in NN.
• Primary model parameters weights are optimized with backpropagation only.
• After fixing the hyperparameters either manually or with the use of a tuning phase.
• Hyperparameters should not be tuned using same data (SGD).
• Portion of data is held out as validation data.
• Performance of model is tested on validation set with various choices of
hyperparameters.
• Ensures not overfit of training data set.
Yang, Li, and Abdallah Shami. "On hyperparameter optimization of machine learning algorithms: Theory and practice."Neurocomputing415 (2020): 295-316.
