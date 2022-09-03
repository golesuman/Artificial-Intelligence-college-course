import numpy as np
from layer import Layer
class Dense(Layer):
    def __init__(self, input_size, output_size) -> None:
        self.weights = np.random.randn(output_size, input_size)
        self.bias = np.random.randn(output_size, 1)
    
    def forward(self, input):
        self.input = input
        return np.dot(self.weights , self.input) + self.bias
    
    def backward(self, output_gradient, learning_rate):
        weight_gradients = np.dot(output_gradient, self.input.T)
        self.weights -= learning_rate * weight_gradients
        self.bias -= learning_rate * output_gradient
        return np.dot(self.weights, output_gradient)