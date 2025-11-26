# Slide 9 of Lecture 11 contains information about the LSTM Code Snippet.

LSTM cell can recognize an important input, store it in long-term state, preserve it for
if it is needed and extract it whenever it is needed.
model = keras.models.Sequential([
model = keras.models.Sequential([
keras.layers.RNN(keras.layers.LSTMCell(20),
keras.layers.LSTM(20, return_sequences=True,
return_sequences=True,
input_shape=[None, 1]),
input_shape=[None, 1]),
keras.layers.LSTM(20, return_sequences=True),
keras.layers.RNN(keras.layers.LSTMCell(20),
keras.layers.TimeDistributed(keras.layers.Dense(10)) ])
return_sequences=True),
keras.layers.TimeDistributed(keras.layers.Dense(10))
])
LSTMCell as an argument
Using LSTM layer NOT SimpleRNN layer
9
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron
