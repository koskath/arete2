# Slide 14 of Lecture 8 contains information about the Stochastic Gradient (SG).

Stochastic Gradient is an iterative optimization algorithm to minimize averages. The algorithm starts with some initial guess, w0. It generates a new guess by moving in the negative gradient direction for a random training example 'i'. The algorithm repeats to successively refine the guess, again for a random training example 'i'. The gradient cost is independent of 'n', and iterations are 'n' times faster than GD iterations.
