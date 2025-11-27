Algorithm:

Start with some initial guess, \( w^0 \).

- Generate new guess by moving in negative gradient direction: 
  \[
  w' = w^0 - \alpha^0 \nabla f_i(w^0)
  \]
  - For a random training example ‘i’.

- Repeat successively refine
  - For a random training example ‘i’.
  \[
  w^{t+1} = w^t - \alpha^t \nabla f_i(w^t) \quad \text{for } t = 1, 2, 3, \ldots
  \]