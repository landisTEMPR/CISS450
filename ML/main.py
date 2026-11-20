import Activation
import Neuron

def weights(n=10):
    #return [float(_) / n for _ in list(range(0, 10))] + [1.0]
    return [float(_) / n for _ in [x - n for x in list(range(0, 2 * n))]] + [1.0]
            
def brute_force_training(N, training):
    for w0 in weights():
        for w1 in weights():
            for w2 in weights():
                ws = [w0, w1, w2]
                #print(ws)
                N.ws = ws
                found = True
                for t in training:
                    inputs, correct = t
                    output = N(inputs)
                    #print(inputs, output, correct, output == correct)
                    if output != correct:
                        found = False
                if found: break
            if found: break
        if found: break
    if found: 
        return N
    else:
        print("NOT FOUND")
        return None

class NeuralLayer:
    def __init__(self, Neurons):
        self.Neurons = Neurons
    def __call__(self, xs):
        xs = [1] + xs
        outputs = [Neuron(xs) for Neuron in self.Neurons]
        return outputs

class ArtificialNeuralNetwork:
    def __init__(self, NeuralLayers):
        self.NeuralLayers = NeuralLayers
    def __call__(self, xs):
        output = [NeuralLayers(xs) for NeuralLayer in self.NeuralLayers]
        return output

if __name__ == '__main__':
    S = Activation.Sigmoid()
    T = Activation.Threshold(0.5)
    N = Neuron.Neuron(activation=T, n=2)
    #Neuron_and = Neuron.Neuron(activation=T, [0.0, 0.1, 0.4])
    #Neuron_or = Neuron.Neuron(activation=T, [0.0, 0.5, 0.5])

    # OR Gate
    training = [([0, 0], 0),
                ([0, 1], 1),
                ([1, 0], 1),
                ([1, 1], 1)]

    N_OR = brute_force_training(N, training)
    print(N_OR)


    # AND Gate
    training = [([0, 0], 0),
                ([0, 1], 0),
                ([1, 0], 0),
                ([1, 1], 1)]

    N_AND = brute_force_training(N, training)
    print(N_AND)


    # GATE for ~x1 AND x2
    training = [([0, 0], 0),
                ([0, 1], 1),
                ([1, 0], 0),
                ([1, 1], 0)]

    N_AND = brute_force_training(N, training)
    print(N_AND)

    
    # GATE for x1 AND ~x2
    training = [([0, 0], 0),
                ([0, 1], 0),
                ([1, 0], 1),
                ([1, 1], 0)]

    N_AND = brute_force_training(N, training)
    print(N_AND)

    
