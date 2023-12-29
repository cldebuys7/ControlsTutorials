"""Program 2-5 from Modern Control Engineering - Ogata, 5th Edition (p. 58-59)

This code demonstrates the ability of the Python Control Systems Library (control) to convert state-space for a
Multi-Input Multi-Output (MIMO) system to multiple transfer functions (one for each input-output relationship). This is
a Matlab example from Ogata's book, converted into Python.
"""

import numpy as np
import control as ct

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Program 2-5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
A = np.array([[0, 1], [-25, -4]])
B = np.array([[1, 1], [0, 1]])
C = np.array([[1, 0], [0, 1]])
D = np.array([[0, 0], [0, 0]])

print("Attempting to create this MIMO system will throw an error if you do not have slycot installed properly.")
transferFunction = ct.ss2tf(A, B, C, D)
print("Here are the transfer functions for the different input-output relationships:")
print(transferFunction)

print("We can also recreate the system from the transfer functions. The library warns us of badly condition filter "
      "coefficients (the warning might be \nthe last thing displayed in the console, but rest assured the warning is "
      "caused by the following line):")
system = ct.tf2ss(transferFunction)
print(system)

print("But if get the transfer functions from the the new system, they match the previous ones, so it's probably fine:")
transferFunction2 = ct.ss2tf(system)
print(transferFunction2)