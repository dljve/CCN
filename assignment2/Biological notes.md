# Biological plausibility
Convlutional neural networks are known to be inspired by nature. 
The idea behind a convolutional layer is that neurons in the visual cortex have a specific area that they respond to; the receptive field.
Implementing this in a neural network causes that there are less neurons connected to each other, thus shrinking the amount of weights that need to be optimized in backpropagation.
To do that, however, it is necessary to find a way for multiple neuron outputs to be combined into one neuron input in the next layer.
This can, theoretically, be done in various ways, but the current preference is for a convolution.
To further decrease the number of parameters necessary to train in the neural network, the same convolution is used over the entire picture.
The choice of convultion is substatiated by the notion that a convolution mimics the acticity of a neuron.
This means that the result of the convolutional layer in terms of activation is very similar to that of normal input neurons that have the same activation.
The difference is that the convolutaional layer activation contains more detailed information than the, e.g. rbg, activation at the input level.

Thus the use of convolutions in deep neural networks is biologically plausible in the sense that it has a receptive field and neurons are combined in a sense that the output of the convolutional layer mimics neural activation.

However, there can still be a phylosophical debate about to what extend the convolution calculation itself is a good representation of what happens in the brain.
Mathematically, it is possible to generate infinite different functions with the same input and output as a given function, so we can never really know for sure when looking soley at input-output behaviour.
Nevertheless, the current solution is a simple and elegant interpretation of what happens in the brain, on some level.
Considering that nature tends to find the simplest mathematical solution to a problem, it would not be suprising if this is close to the real solution of image processing in the brain.
Only with more research we can determine definitively whether convolution is biologically plausible or not.
