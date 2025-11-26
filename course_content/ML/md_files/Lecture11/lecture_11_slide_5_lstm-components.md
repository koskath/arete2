# Slide 5 of Lecture 11 contains information about the LSTM Components.

• Extra components enable RNN to remember and store important events from distant past.
• Input gate: controls what information gets stored in long-term state/memory cell (c).
• There is another gate that regulates information flowing into input gate.
• This gate analyzes current input to LSTM cell, x and previous short-term state (h −1).
t t
5
Notations: ​Previous cell state (c−1)​, Previous hidden state (h−1)​, Current input x.
t t t
