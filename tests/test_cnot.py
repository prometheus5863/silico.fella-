import numpy as np
from src.qubitpro.qubitpro_sv import qubitpro_sv

def test_cnot():
    sim = qubitpro_sv(num_qubits=2)
    X = np.array([[0, 1], [1, 0]])  # Pauli-X gate
    sim.apply_gate(X, [0])  # Set qubit 0 to |1>
    CNOT = None  # Built-in CNOT logic in the simulator
    sim.apply_gate(CNOT, [0, 1])  # Apply CNOT gate with control 0 and target 1
    print("Statevector after CNOT:", sim.state)

if __name__ == "__main__":
    test_cnot()
