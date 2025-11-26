# Slide 34 of Lecture 10 contains information about the How it works?.

• Placeholders are nodes whose value is fed in at execution
time (inputs, labels, …).
• Code for:
import tensorflow as tf
b = tf.Variable(tf.zeros((100,)))
W = tf.Variable(tf.random_uniform((784, 100), -1, 1))
x = tf.placeholder(tf.float32, (1, 784))
h = tf.nn.relu(tf.matmul(x, W) + b)
CPU
• Deploy graph with a session
GPU
35
