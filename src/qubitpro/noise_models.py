import numpy as np

class DepolarizingNoise:
    @staticmethod
    def apply(state, probability):
        dim = len(state)
        identity = np.eye(dim) / dim
        noisy_state = (1 - probability) * state + probability * identity
        return noisy_state
