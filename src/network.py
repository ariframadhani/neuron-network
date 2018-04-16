import numpy as np


class NeuronNetwork:
    pass


def sigmoid(z):
    return 1 / (1 + np.exp(-z))
