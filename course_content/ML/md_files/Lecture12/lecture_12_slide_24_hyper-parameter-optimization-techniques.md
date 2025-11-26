# Slide 24 of Lecture 12 contains information about the Hyper-parameter Optimization Techniques.

• Random search (RS): like GS.
• Randomly selects a pre-defined number of samples between upper and lower bounds as
candidate hyper-parameter values, and then trains these candidates until defined budget
is exhausted.
• With a limited budget, RS can explore a larger search space than GS.
• Problem: unnecessary function evaluations since it does not exploit previously well-
performing regions.
• Gradient-based optimization: traditional technique.
• After randomly selecting a data point, it moves towards opposite direction of largest
gradient to locate next data point.
• Local optimum can be reached after convergence.
• Gradient-based algorithms have a fast convergence speed to reach local optimum.
• Can use to optimize learning rate in neural networks (NN).
Yang, Li, and Abdallah Shami. "On hyperparameter optimization of machine learning algorithms: Theory and practice."Neurocomputing415 (2020): 295-316.
