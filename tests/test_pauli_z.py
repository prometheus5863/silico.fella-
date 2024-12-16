import numpy as np
from src.qubitpro.qubitpro_sv import qubitpro_sv

def test_pauli_z():
    sim = qubitpro_sv(num_qubits=1)
    Z = np.array([[1, 0], [0, -1]])  # Pauli-Z gate
    sim.apply_gate(Z, [0])
    print("Statevector after Pauli-Z:", sim.state)

if __name__ == "__main__":
    test_pauli_z()
