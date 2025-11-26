# Slide 15 of Lecture 12 contains information about the Challenges Hyper-parameter Optimization.

• Function evaluations can be extremely expensive for large models (e.g., in deep
learning), complex machine learning pipelines, or large datasets.
• Configuration space is often complex (comprising a mix of continuous, categorical and
conditional hyperparameters) and high-dimensional (not always clear which
hyperparameters to optimize).
• No access to a gradient of hyperparameter loss function. Other properties of target
function often used in classical optimization do not typically apply (such as convexity and
smoothness).
• One cannot directly optimize for generalization performance as training datasets are of
limited size.
F. Hutter et al. (eds.), Automated Machine Learning, The Springer Series on Challenges in Machine Learning, https://doi.org/10.1007/978-3-030-05318-5_1
