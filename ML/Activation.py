import math

class Activation:
    def __init__(self):
        pass
    def __call__(self, z):
        pass
    def __str__(self):
        pass

    
class Sigmoid(Activation):
    def __init__(self):
        Activation.__init__(self)
    def __call__(self, z):
        return 1.0 / (1.0 + math.exp(-z))
    def __str__(self):
        return "Sigmoid"
    

class Threshold(Activation):
    def __init__(self, alpha):
        Activation.__init__(self)
        self.alpha = alpha
    def __call__(self, z):
        if z < self.alpha: return 0.
        else: return 1.
    def __str__(self):
        return f"Threshold({self.alpha})"
    

if __name__ == '__main__':
    S = Sigmoid()
    print(S)
    print(f"Sigmoid(0) = {S(0.)}")
    print(f"Sigmoid(99) = {S(99)}")
    print(f"Sigmoid(-99) = {S(-99)}")
    T = Threshold(0.5)
    print(T)
    print(f"Threshold(0.3) = {T(0.3)}")
    print(f"Threshold(0.3) = {T(0.7)}")
