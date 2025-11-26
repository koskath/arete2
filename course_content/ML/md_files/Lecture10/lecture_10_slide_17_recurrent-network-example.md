# Slide 17 of Lecture 10 contains information about the Recurrent Network Example.

Built-in RNN layers: keras.layers.SimpleRNN
•
fully-connected RNN where the output from previous timestep is to be fed to next
•
timestep.
inputs = np.random.random([32, 10, 8]).astype(np.float32)
tf.keras.layers.SimpleRNN(
simple_rnn = tf.keras.layers.SimpleRNN(4)
units, activation='tanh', use_bias=True,
kernel_initializer='glorot_uniform',
output = simple_rnn(inputs) # The output has shape `[32, 4]`.
recurrent_initializer='orthogonal',
bias_initializer='zeros', kernel_regularizer=None,
simple_rnn = tf.keras.layers.SimpleRNN(
recurrent_regularizer=None, bias_regularizer=None,
4, return_sequences=True, return_state=True)
activity_regularizer=None,
kernel_constraint=None, recurrent_constraint=None,
# whole_sequence_output has shape `[32, 10, 4]`.
bias_constraint=None,
# final_state has shape `[32, 4]`.
dropout=0.0, recurrent_dropout=0.0,
whole_sequence_output, final_state = simple_rnn(inputs)
return_sequences=False, return_state=False,
go_backwards=False, stateful=False, unroll=False, **kwargs
)
17
https://www.tensorflow.org/api_docs/python/tf/keras/layers/SimpleRNN
