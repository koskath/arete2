# Slide 23 of Lecture 14 contains information about the RL Workflow.

• Create Agent: Consists of policy and training algorithm.
o Represent policy using NNs or look-up tables.
o NN are good candidates for large state/action spaces and complex problems.
• Training: Set up training options (like stopping
criteria) and train agent to tune policy.
• Make sure to validate trained policy after training.
• If necessary, revisit design choices like reward
signal and policy architecture and train again.
• Overall, RL is sample inefficient; training can take anywhere from minutes to days
depending on the application.
https://se.mathworks.com/discovery/reinforcement-learning.html
