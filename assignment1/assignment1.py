# -*- coding: utf-8 -*-
"""
Computational Cognitive Neuroscience

Assignment 1

TODO:
    Plot the decrease in training and test loss over epochs. 
    Submit your code as a documented Jupyter notebook, which includes your figure. 
    For development, it is advised to first implement your work in PyCharm and then port your code to a notebook.
"""

import chainer.functions as F
import chainer.links as L
from chainer import Chain
from chainer import iterators, optimizers
from chainer import report, training
from chainer.training import extensions
import utils

train, test = utils.get_mnist(n_train=100, n_test=100, n_dim=1, with_label=True)

# Batch size 32
train_iter = iterators.SerialIterator(train, batch_size=32, shuffle=True)
test_iter = iterators.SerialIterator(test, batch_size=32, repeat=False, shuffle=False)


class MLP(Chain):
    def __init__(self, n_units, n_out):
        super(MLP, self).__init__()
        with self.init_scope():
            self.l1 = L.Linear(None, n_units)
            self.l2 = L.Linear(None, n_out)

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        y = self.l2(h1)
        return y


class Classifier(Chain):
    def __init__(self,predictor):
        super(Classifier, self).__init__()
        
    def __call__(self, x, t):
        y = self.predictor(x)
        loss = F.softmax_cross_entropy(y, t)
        accuracy = F.accuracy(y, t)
        report({'loss': loss, 'accuracy' : accuracy}, self)
        return loss


model = L.Classifier(MLP(10, 10))  # the input size, 784, is inferred
optimizer = optimizers.SGD()
optimizer.setup(model)

updater = training.StandardUpdater(train_iter, optimizer)
trainer = training.Trainer(updater, (20, 'epoch'), out='result')
trainer.extend(extensions.Evaluator(test_iter, model))
trainer.extend(extensions.LogReport())
#trainer.extend(extensions.PlotReport(['main/accuracy'],'iteration'))
#trainer.extend(extensions.PrintReport(['epoch', 'main/accuracy', 'validation/main/accuracy']))
trainer.extend(extensions.PlotReport(['main/loss', 'validation/main/loss'], 'epoch'))
trainer.extend(extensions.ProgressBar())
trainer.run()