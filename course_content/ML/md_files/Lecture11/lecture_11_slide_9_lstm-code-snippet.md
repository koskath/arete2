# Slide 9 of Lecture 11 contains information about the LSTM Code Snippet.

This slide explains that an LSTM cell can recognize an important input, store it in the long-term state, preserve it until it becomes relevant, and then extract it exactly when needed.
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
The snippet highlights using LSTMCell as an argument and favoring the LSTM layer rather than a SimpleRNN layer, reinforcing the guidance presented on slide 9 and attributed to “Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow” by Aurélien Géron.
