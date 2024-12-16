import numpy as np
from src.qubitpro.qubitpro_sv import qubitpro_sv

def test_pauli_x():
    sim = qubitpro_sv(num_qubits=1)
    X = np.array([[0, 1], [1, 0]])  # Pauli-X gate
    sim.apply_gate(X, [0])
    print("Statevector after Pauli-X:", sim.state)

if __name__ == "__main__":
    test_pauli_x()
