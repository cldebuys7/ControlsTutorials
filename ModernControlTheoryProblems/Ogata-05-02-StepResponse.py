"""Programs 5-1 and 5-2 from Modern Control Engineering - Ogata, 5th Edition (p. 186-188)

This code demonstrates the ability of the Python Control Systems Library (control) to generate the step response of a
linear system given the state-space system matrices. This is a Matlab example from Ogata's book, converted into Python.
"""

import numpy as np
import control as ct
import matplotlib.pyplot as plt

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Program 5-1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
A = np.array([[-1.0, -1.0], [6.5, 0.0]])
B = np.array([[1.0, 1.0], [0.0, 1.0]])
C = np.array([[1.0, 0.0], [0, 1]])
D = np.array([[0.0, 0.0], [0.0, 0.0]])

system = ct.ss(A, B, C, D)

time = np.linspace(0, 12, 1000)
timeReturned, systemOutput = ct.step_response(system, time)

print("This system has 4 transfer functions, so there are 4 step responses. They do not seem to be in the same order "
      "as Matlab's output (U1 and U2 are swapped), but the overall system is equivalent.")
plt.figure(figsize=(12, 9))
plt.suptitle('Step Response of the 2x2 System')

plt.subplot(2, 2, 1)
plt.plot(timeReturned, systemOutput[0][1])
plt.title('U1 to Y1')
plt.ylabel('Amplitude')
plt.grid(visible=True)

plt.subplot(2, 2, 2)
plt.plot(timeReturned, systemOutput[0][0])
plt.title('U2 to Y1')
plt.grid(visible=True)

plt.subplot(2, 2, 3)
plt.plot(timeReturned, systemOutput[1][1])
plt.title('U1 to Y2')
plt.xlabel('time [s]')
plt.ylabel('Amplitude')
plt.grid(visible=True)

plt.subplot(2, 2, 4)
plt.plot(timeReturned, systemOutput[1][0])
plt.title('U2 to Y2')
plt.xlabel('time [s]')
plt.grid(visible=True)

plt.show()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Program 5-2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
time1, output1 = ct.step_response(system, time, input=1)
time2, output2 = ct.step_response(system, time, input=0)

plt.figure(figsize=(12, 9))
plt.suptitle('Step Response of the 2x2 System')

plt.subplot(2, 1, 1)
plt.plot(time1, output1[0][0], label='Y1 from U1')
plt.plot(time1, output1[1][0], label='Y2 from U1')
plt.legend()
plt.ylabel('Amplitude')
plt.grid(visible=True)

plt.subplot(2, 1, 2)
plt.plot(time2, output2[0][0], label='Y1 from U2')
plt.plot(time2, output2[1][0], label='Y2 from U2')
plt.legend()
plt.ylabel('Amplitude')
plt.xlabel('time [s]')
plt.grid(visible=True)

plt.show()
