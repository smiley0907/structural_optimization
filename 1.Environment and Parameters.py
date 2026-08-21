# ============================================================
# CELL 1: ENVIRONMENT AND EXPERIMENT PARAMETERS
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity

# Workload sizes
QUBIT_SIZES = [3, 5, 7, 9, 11]

# Execution parameters
SHOTS = 1024
WARMUP_RUNS = 2
MEASUREMENT_RUNS = 10

# Common gate basis for structural comparison
BASIS_GATES = ["rz", "sx", "x", "cx"]

# Aer simulator
simulator = AerSimulator()

print("Environment initialized successfully.")
print("Qubit sizes:", QUBIT_SIZES)
print("Shots:", SHOTS)
print("Warm-up runs:", WARMUP_RUNS)
print("Measurement runs:", MEASUREMENT_RUNS)
print("Simulator:", simulator.name)
