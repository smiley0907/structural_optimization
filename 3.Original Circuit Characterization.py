# ============================================================
# CELL 3: ORIGINAL CIRCUIT CHARACTERIZATION
# ============================================================

original_results = []

for q in QUBIT_SIZES:

    # Convert to a common gate basis
    circuit = transpile(
        original_circuits[q],
        basis_gates=BASIS_GATES,
        optimization_level=0
    )

    # Total gate count
    total_gates = circuit.size()

    # Two-qubit gate count
    two_qubit_gates = sum(
        instruction.operation.num_qubits == 2
        for instruction in circuit.data
    )

    # Two-qubit gate ratio
    two_qubit_ratio = (
        (two_qubit_gates / total_gates) * 100
        if total_gates > 0 else 0
    )

    # Circuit depth
    depth = circuit.depth()

    original_results.append({
        "Qubits": q,
        "Gate_Count": total_gates,
        "Two_Qubit_Gate_Count": two_qubit_gates,
        "Two_Qubit_Gate_Ratio_%": two_qubit_ratio,
        "Circuit_Depth": depth
    })

original_df = pd.DataFrame(original_results)

display(original_df)
