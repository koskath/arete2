# Slide 20 of Lecture 12 contains information about the Learning Rate Scheduling.

• Strategies to reduce learning rate during training called learning schedules.
1. Power scheduling: Set learning rate to a function of iteration number t: η(t) = η / (1+t/s)c .
0
(initial learning rate η , power c (set to 1), steps s are hyperparameters).
0
2. Exponential scheduling: Set learning rate to η(t) = η 0.1t/s. Learning rate will gradually
0
drop by a factor of 10 every s steps.
3. Piecewise constant scheduling: Use a constant learning rate for a number of epochs
(e.g., η = 0.1 for 5 epochs), then smaller learning rate for another number of epochs
0
(e.g., η = 0.001 for 50 epochs), and so on.
1
4. Performance scheduling: Measure validation error every N steps (like early stopping) and
reduce learning rate by a factor of λ when error stops dropping.
