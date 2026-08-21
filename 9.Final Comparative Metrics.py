# ============================================================
# CELL 9: FINAL COMPARATIVE METRICS
# ============================================================

results = original_df.merge(
    processed_df,
    on="Qubits",
    suffixes=("_Original", "_Processed")
).merge(
    original_execution_df,
    on="Qubits"
).merge(
    processed_execution_df,
    on="Qubits",
    suffixes=("_Original", "_Processed")
)

# Two-qubit gate reduction
results["Two_Qubit_Gate_Reduction_%"] = (
    (results["Two_Qubit_Gate_Count_Original"]
     - results["Two_Qubit_Gate_Count_Processed"])
    / results["Two_Qubit_Gate_Count_Original"]
) * 100

# Total gate reduction
results["Total_Gate_Reduction_%"] = (
    (results["Gate_Count_Original"]
     - results["Gate_Count_Processed"])
    / results["Gate_Count_Original"]
) * 100

# Circuit depth reduction
results["Circuit_Depth_Reduction_%"] = (
    (results["Circuit_Depth_Original"]
     - results["Circuit_Depth_Processed"])
    / results["Circuit_Depth_Original"]
) * 100

# Execution time improvement
results["Execution_Time_Improvement_%"] = (
    (results["Median_Time_sec_Original"]
     - results["Median_Time_sec_Processed"])
    / results["Median_Time_sec_Original"]
) * 100

display(results)
