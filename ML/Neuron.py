import Activation
import random

class Neuron:
    def __init__(self, activation, ws=None, n=None):
        assert isinstance(activation, Activation.Activation)
        self.activation = activation
        if ws == None:
            self.n = n
            self.ws = [random.random() for _ in range(n + 1)]
        else:
            self.n = len(ws)
            self.ws = ws
    def __call__(self, xs):
        A = self.activation
        ws = self.ws
        xs = [1.0] + xs
        z = sum(w * x for (w ,x) in zip(ws, xs))
        return A(z)

        
    def __str__(self):
        return "<Neuron %s %s>" % (self.activation, self.ws)
