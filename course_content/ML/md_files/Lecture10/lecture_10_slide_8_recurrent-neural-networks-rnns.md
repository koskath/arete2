# Slide 8 of Lecture 10 contains information about the Recurrent Neural Networks (RNNs).

• RNNs developed to solve learning problems (time series or sequential tasks)
where information about past (i.e., past instants/events) is directly linked to
making future predictions.
• Recurrent Neuron: maintains a memory or a state from past computations.
• Data is looped back into same neuron at every new time instant.
• It takes input as output of previous instant y in addition to its current input
t − 1
at instant x .
t
• The recurrent neuron has two input weights, W and W
xt yt -1
8
