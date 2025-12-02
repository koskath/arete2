# Slide 10 of Lecture 8 contains information about the GD: Local Minimum.

The algorithm starts with w0 as an initial guess. It generates a new guess by moving in the negative gradient direction. It decreases 'f' if the "step size" α0 is small enough, where α is the learning rate. We decrease α0 if it increases 'f'. The algorithm repeats to successively refine the guess. It stops if not making progress. Under weak conditions, the algorithm converges to a 'w' with ∇f(w) = 0, where 'f' is bounded, ∇f doesn't change arbitrarily fast, and αt is small and constant.
