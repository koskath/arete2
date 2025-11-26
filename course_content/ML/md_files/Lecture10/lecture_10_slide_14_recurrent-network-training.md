# Slide 14 of Lecture 10 contains information about the Recurrent Network Training.

• RNN is trained by backpropagation through time (BPTT).
• Because standard backpropagation cannot work in loop or recurrent structure.
• Training a network using backpropagation involves calculating error gradient,
moving backward from output layer through hidden layers of network and
adjusting network weights.
• However, this operation cannot work in recurrent neuron because we have just one
neural cell with recurrent connections to itself.
• Note: Deep RNN is the way to stack multiple layers of cells.
• Each time step t (called a frame).
14
