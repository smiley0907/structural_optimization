# ============================================================
# CELL 7: PROCESSED CIRCUIT CHARACTERIZATION
# ============================================================

processed_results = []

for q in QUBIT_SIZES:

    circuit = processed_circuits[q]

    total_gates = circuit.size()

    two_qubit_gates = sum(
        instruction.operation.num_qubits == 2
        for instruction in circuit.data
    )

    two_qubit_ratio = (
        (two_qubit_gates / total_gates) * 100
        if total_gates > 0 else 0
    )

    depth = circuit.depth()

    processed_results.append({
        "Qubits": q,
        "Gate_Count": total_gates,
        "Two_Qubit_Gate_Count": two_qubit_gates,
        "Two_Qubit_Gate_Ratio_%": two_qubit_ratio,
        "Circuit_Depth": depth
    })

processed_df = pd.DataFrame(processed_results)

display(processed_df)
