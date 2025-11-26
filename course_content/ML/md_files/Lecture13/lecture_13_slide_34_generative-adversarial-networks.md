# Slide 34 of Lecture 13 contains information about the Generative Adversarial Networks.

•
Each training iteration is divided into two phases:
•
Discriminator training: Batch of real images (label 1) is sampled from training set and is
completed with an equal number of fake images (label 0) produced by the generator.
[Uses binary cross-entropy as loss function].
•
Generator training: Produce another batch of fake images, and once again
discriminator is used to tell whether images are fake or real. Do not add real images in
the batch, and all labels are set to 1 (real).
• SELU (Scaled Exponential Linear Unit) [2017] aims
Never actually sees any real images.
to automatically normalize the output of neurons during
training. [variation of ReLU]
codings_size = 30
discriminator = keras.models.Sequential([
generator = keras.models.Sequential([
keras.layers.Flatten(input_shape=[28, 28]),
keras.layers.Dense(100, activation="selu",
keras.layers.Dense(150, activation="selu"),
input_shape=[codings_size]),
keras.layers.Dense(100, activation="selu"),
keras.layers.Dense(150, activation="selu"),
keras.layers.Dense(1, activation="sigmoid")
keras.layers.Dense(28 * 28, activation="sigmoid"),
])
keras.layers.Reshape([28, 28])
])
gan = keras.models.Sequential([generator, discriminator])
Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron
