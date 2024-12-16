import numpy as np
from src.qubitpro.qubitpro_sv import qubitpro_sv

def test_hadamard():
    sim = qubitpro_sv(num_qubits=1)
    H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
    sim.apply_gate(H, [0])
    print("Statevector after Hadamard", sim.state)
if __name__ == "__main__":
    test_hadamard()
