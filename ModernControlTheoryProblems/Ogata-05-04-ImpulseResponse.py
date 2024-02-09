"""Program 5-6 from Modern Control Engineering - Ogata, 5th Edition (p. 192-193)

This code demonstrates the ability of the Python Control Systems Library (control) to generate the unit-step response of
second order systems with increasing damping ratio given their transfer functions. This is a Matlab example from Ogata's
book, generated in Python.
"""

import numpy as np
import control as ct
import matplotlib.pyplot as plt


def create_second_order_transfer_function(wn, zeta):
    num = [wn ** 2]
    den = [1, 2 * zeta * wn, wn ** 2]
    return ct.tf(num, den)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2D Plot of Step Response for Increasing Zeta >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
time = np.linspace(0, 10, 1000)
zetaValues = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
plt.figure()

for zeta in zetaValues:
    system = create_second_order_transfer_function(1, zeta)
    timeReturned, systemOutput = ct.step_response(system, time)

    plt.plot(timeReturned, systemOutput, label=r'$\zeta$' + f' = {zeta}')

plt.title('Unit-Step Response of Second-Order Systems')
plt.legend()
plt.xlabel('time (s)')
plt.ylabel('Response')
plt.xlim(0, 10)
plt.grid()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3D Plot of Step Response for Increasing Zeta >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
time = np.linspace(0, 10, 1000)
zetaValues = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

# Create a 2D grid of time and zeta values. Populate the hyperOutput array with the step response of each system.
hyperTime = np.tile(time, (len(zetaValues), 1))
hyperZeta = np.tile(np.array(zetaValues).reshape(-1, 1), (1, len(time)))
hyperOutput = np.zeros((len(zetaValues), len(time)))

for zeta in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    system = create_second_order_transfer_function(1, zeta)
    timeReturned, systemOutput = ct.step_response(system, time)
    hyperOutput[zetaValues.index(zeta)] = systemOutput

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot_surface(hyperTime, hyperZeta, hyperOutput)
ax.set_title('3D Plot of Unit-Step Response of Second-Order Systems')
ax.set_xlabel('time (s)')
ax.set_ylabel(r'$\zeta$')
ax.set_zlabel('Response')
plt.show()
