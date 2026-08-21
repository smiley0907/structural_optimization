# ============================================================
# CELL 4: ORIGINAL CIRCUIT EXECUTION
# ============================================================

original_execution = []

for q in QUBIT_SIZES:

    circuit = transpile(
        original_circuits[q],
        simulator,
        basis_gates=BASIS_GATES,
        optimization_level=0
    )

    # Warm-up executions
    for _ in range(WARMUP_RUNS):
        simulator.run(
            circuit,
            shots=SHOTS
        ).result()

    # Measured executions
    times = []

    for _ in range(MEASUREMENT_RUNS):
        result = simulator.run(
            circuit,
            shots=SHOTS
        ).result()

        times.append(result.time_taken)

    original_execution.append({
        "Qubits": q,
        "Median_Time_sec": np.median(times),
        "Mean_Time_sec": np.mean(times),
        "Std_Time_sec": np.std(times, ddof=1)
    })

original_execution_df = pd.DataFrame(original_execution)

display(original_execution_df)
