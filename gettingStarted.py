#https://qiskit.org/documentation/tutorials/circuits/1_getting_started_with_qiskit.html

import numpy as np
from qiskit import *
from qiskit import Aer
from qiskit.visualization import plot_state_city

import matplotlib.pyplot as plt

print("Starting tuto")

# Create a Quantum Circuit acting on a quantum register of three qubits
circ = QuantumCircuit(3)

# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
circ.cx(0, 1)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
# the qubits in a GHZ state.
circ.cx(0, 2)
circ.draw('mpl')


#backend = Aer.get_backend('statevector_simulator')
#job = backend.run(circ)
#result = job.result()
#outputstate = result.get_statevector(circ, decimals=3)
#print(outputstate)
#plot_state_city(outputstate)


sim = Aer.get_backend('aer_simulator')  # this is the simulator we'll use
qobj = assemble(qc_output)  # this turns the circuit into an object our backend can run
result = sim.run(qobj).result()  # we run the experiment and get the result from that experiment
# from the results, we get a dictionary containing the number of times (counts)
# each result appeared
counts = result.get_counts()
# and display it on a histogram
plot_histogram(counts)




print("Done")
plt.show()

