# ============================================================
# CELL 5: GENERATE PROCESSED CIRCUITS
# ============================================================

from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import CommutativeCancellation

processed_circuits = {}

for q in QUBIT_SIZES:

    # Prepare the circuit in the common gate basis
    circuit = transpile(
        original_circuits[q],
        basis_gates=BASIS_GATES,
        optimization_level=0
    )

    # Apply commutation based gate cancellation
    pass_manager = PassManager([
        CommutativeCancellation()
    ])

    processed_circuits[q] = pass_manager.run(circuit)

    print(
        f"{q} qubits -> processed circuit generated"
    )

print("\nAll processed circuits generated successfully.")
