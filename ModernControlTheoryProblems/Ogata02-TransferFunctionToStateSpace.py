"""Program 2-2 and 2-3 from Modern Control Engineering - Ogata, 5th Edition (p. 41)

This code demonstrates the ability of the Python Control Systems Library (control) to convert a transfer function into
a state-space system representation and to convert state-space to a transfer function. This is a Matlab example from
Ogata's book, converted into Python. Note that tf2ss() does not have the option to return [A, B, C, D] directly as in
Matlab, but the system object has the matrices. For example, you could use system.A to get A.
"""

import numpy as np
import control as ct

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Program 2-2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# Create the transfer functions, G(s)
numerator1 = [1, 0]
denominator1 = [1, 14, 56, 160]
G_s = ct.tf(numerator1, denominator1)

# convert the transfer function (tf) to state-space (ss) representation
system1 = ct.tf2ss(numerator1, denominator1)
print("The state-space system matrices are given by: ")
print(system1)
# Grab the A matrix, for example
print("We can get the A matrix like so: ")
print("A = ", system1.A)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Program 2-3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
A = np.array([[0, 1, 0], [0, 0, 1], [-5, -25, -5]])
B = np.array([[0], [25], [-120]])
C = np.array([[1, 0, 0]])
D = np.array([[0]])
transferFunction2 = ct.ss2tf(A, B, C, D)
print("The transfer function for Program 2-3 is below. Note that sometimes it gives very small numbers instead of 0 "
      "for some coefficients:")
print(transferFunction2)

# We could have also defined the state-space system using the system matrices and then converted to tf
system2 = ct.ss(A,B,C,D)
transferFunctionFromSys = ct.ss2tf(system2)
print("Here we defined the system and then converted to a transfer function: ")
print(transferFunctionFromSys)