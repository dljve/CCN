
"""
Computational Cognitive Neuroscience

Assignment 2

TODO:
     - Reuse the code you developed in Assignment 1 in order to test the influence of network depth on performance.
     - Modify your network to make use of convolutions.
     - Train a deep neural network for 20 epochs consisting of N fully connected layers and 10 units per layer.
     - Compare the performance on training and validation data using networks consisting of N=1, 2 and 3 layers.
     - Visualize and interpret the results.
     - Report your conclusions.
     - Create a network consisting of a convolutional layer, a max pooling layer and one fully connected layer. For the convolutional layers, use 5 output channels, a kernel size of 5, stride of 1 and padding of 0.
     - Again plot the loss.
     - Report your conclusions.
     - Explain in which ways convolution is biologically plausible and biologically implausible.
     - Add additional components to your model (e.g. one of dropout, batch normalization, other activation functions, etc.).
     - Report if your new architecture outperforms the original convnet architecture.
     - Provide a plot and a written explanation of your observed (better/worse) results.


Useful tips:
    To understand the basics of deep learning and convolution, you should read Chapter 6 of http://neuralnetworksanddeeplearning.com.
    For background on convolutions please consult: https://github.com/vdumoulin/conv_arithmetic
    Read the Chainer documentation.

"""

# TODO define deep neural network

# TODO define network consisting of a convolutional layer, a max pooling layer and one fully connected layer.


epochs = 20
units = 10
layers = [1,2,3]

for layer in layers:
    # TODO train neural network
    # TODO test neural network
    pass

# TODO compare performance on train and validation data for each layer
# TODO visualize the performance and comparison

output_channel = 5
kernel_size = 5
stride = 1
padding = 0

# TODO train and test the convolutional network

# TODO plot the loss of the convolutional network

# TODO add additional components to the networks (e.g. one of dropout, batch normalization, other activation functions, etc.).
# TODO plot results


