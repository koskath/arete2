# Slide 10 of Lecture 11 contains information about the Gated Recurrent Unit (GRU).

• Variants of LSTM cell exists such as GRU (Gated Recurrent Unit (GRU) cell*.
• LSTM and GRU cells are reasons behind success of RNNs.
• GRU cell is a simplified version of LSTM cell.
• Can handle much longer sequences than simple RNNs.
• GRUs combine forget and input gates to decide on what information should be committed to
long-term memory (memory cell) and be left out.
• Combines long and short-term state into a single state vector (h )
t
• Removes output gate and returns state vector h at each time instant.
t
• Implemented in ‘tf.keras.layers.GRU()’.
10
Kyunghyun Cho et al., “Learning Phrase Representations Using RNN Encoder-Decoder for Statistical Machine Translation,” Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing(2014): 1724–1734.
