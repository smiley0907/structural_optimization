# ============================================================
# CELL 8: PROCESSED CIRCUIT EXECUTION
# ============================================================

processed_execution = []

for q in QUBIT_SIZES:

    circuit = transpile(
        processed_circuits[q],
        simulator,
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

    processed_execution.append({
        "Qubits": q,
        "Median_Time_sec": np.median(times),
        "Mean_Time_sec": np.mean(times),
        "Std_Time_sec": np.std(times, ddof=1)
    })

processed_execution_df = pd.DataFrame(processed_execution)

display(processed_execution_df)
