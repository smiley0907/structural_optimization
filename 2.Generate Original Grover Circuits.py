# ============================================================
# CELL 2: GENERATE ORIGINAL GROVER CIRCUITS
# ============================================================

def create_grover_circuit(num_qubits):
    qc = QuantumCircuit(num_qubits)

    # Create equal superposition
    qc.h(range(num_qubits))

    # Number of Grover iterations
    iterations = max(
        1,
        int(np.floor((np.pi / 4) * np.sqrt(2 ** num_qubits)))
    )

    for _ in range(iterations):

        # Oracle
        qc.x(range(num_qubits))
        qc.h(num_qubits - 1)

        qc.mcx(
            list(range(num_qubits - 1)),
            num_qubits - 1
        )

        qc.h(num_qubits - 1)
        qc.x(range(num_qubits))

        # Diffusion operator
        qc.h(range(num_qubits))
        qc.x(range(num_qubits))
        qc.h(num_qubits - 1)

        qc.mcx(
            list(range(num_qubits - 1)),
            num_qubits - 1
        )

        qc.h(num_qubits - 1)
        qc.x(range(num_qubits))
        qc.h(range(num_qubits))

    qc.measure_all()

    return qc


original_circuits = {
    q: create_grover_circuit(q)
    for q in QUBIT_SIZES
}

print("Original Grover circuits generated successfully.")

for q in QUBIT_SIZES:
    print(
        f"{q} qubits -> "
        f"{original_circuits[q].num_qubits} qubits"
    )
