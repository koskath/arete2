# Slide 19 of Lecture 13 contains information about the Code Snippet.

# Convolutional base using a common pattern: a stack of Conv2D and MaxPooling2D layers.
# CNN takes tensors of shape (image_height, image_width, color_channels), color_channels refers to
(R,G,B) to support the format of CIFAR images.
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
Kernel
Layer Type Filters Activation
Size Output is flattened and
passed through dense
Conv2D 32 (3,3) ReLU
layers for classification.
This sample network processes 32x32 RGB images,
MaxPooling2D - (2,2) -
extracting features through convolution and
reducing spatial dimensions through pooling.
Conv2D 64 (3,3) ReLU
MaxPooling2D - (2,2) -
Conv2D 64 (3,3) ReLU
