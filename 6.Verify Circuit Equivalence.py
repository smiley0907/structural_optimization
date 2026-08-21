# ============================================================
# CELL 6: VERIFY CIRCUIT EQUIVALENCE
# ============================================================

equivalence_results = []

for q in QUBIT_SIZES:

    original_circuit = original_circuits[q].remove_final_measurements(
        inplace=False
    )

    processed_circuit = processed_circuits[q].remove_final_measurements(
        inplace=False
    )

    original_state = Statevector.from_instruction(
        original_circuit
    )

    processed_state = Statevector.from_instruction(
        processed_circuit
    )

    fidelity = state_fidelity(
        original_state,
        processed_state
    )

    equivalence_results.append({
        "Qubits": q,
        "State_Fidelity": fidelity
    })

equivalence_df = pd.DataFrame(equivalence_results)

display(equivalence_df)
