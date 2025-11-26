# Slide 6 of Lecture 11 contains information about the LSTM Components.

• Forget gate: Regulate how much of information in long-term state is persisted across time
instants.
• Note: Components of LSTM cells are fully connected NNs.
• Variants of RNs with memory cells are peephole connections and gated recurrent units.
• Output gate: controls how much information to output from cell at a time instant.
• Control value of h (short-term state) and y (output at time t).
t t
Notations:
• Previous cell state (c −1)
t
• Previous hidden state (h −1)
t
• Current input x .
t
6
