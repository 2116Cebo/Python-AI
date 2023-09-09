import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
class ArtificialNeuron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()
    def forward(self, input_data):
        weighted_sum = np.dot(input_data, self.weights) + self.bias
        output = sigmoid(weighted_sum)
        return output
if __name__ == "__main__":
    input_data = np.array([0.5, 0.3, 0.2])
    neuron = ArtificialNeuron(input_size=3)
    output = neuron.forward(input_data)
    print("Output: ", output)
