# Slide 30 of Lecture 9 contains information about the Backpropagation.

• Backpropagation computes neural network gradient via chain rule.
• Computing gradient is known as “backpropagation”.
• With squared loss, objective function is:
• Usual training procedure: stochastic gradient.
• Compute gradient of random example ‘i’, update both ‘v’ and ‘W’.
• Highly non-convex and can be difficult to tune.
• Backward pass:
• Initialize all hidden layers’ connection weights randomly, or else training will fail.
• For this algorithm to work for MLP’s architecture the step function was replaced with the logistic
(sigmoid) function, σ(z) = 1 / (1 + exp(–z)).
33
*David Rumelhart et al. “Learning Internal Representations by Error Propagation,” (Defense Technical Information Center technical report, September 1985).
