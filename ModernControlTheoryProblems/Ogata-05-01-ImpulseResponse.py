"""Impulse Response of Second-Order Systems from Modern Control Engineering - Ogata, 5th Edition (p. 186-188)

This code demonstrates the ability of the Python Control Systems Library (control) to generate the step response of a
linear system given the state-space system matrices. This is a Matlab example from Ogata's book, converted into Python.
"""

import numpy as np
import control as ct
import matplotlib.pyplot as plt


def create_second_order_transfer_function(wn, zeta):
    num = [wn ** 2]
    den = [1, 2 * zeta * wn, wn ** 2]
    return ct.tf(num, den)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Figure 5-14 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
for zeta in [0.1, 0.2, 0.4, 0.7, 1.0]:
    system = create_second_order_transfer_function(1, zeta)
    time = np.linspace(0, 12, 1000)
    timeReturned, systemOutput = ct.impulse_response(system, time)

    plt.plot(timeReturned, systemOutput, label=r'$\zeta$' + f' = {zeta}')

plt.title('Impulse Response of Second-Order Systems')
plt.legend()
plt.xlabel(r'$\omega_n$t')
plt.ylabel(r'$\frac{c(t)}{\omega_n}$', rotation=0)
plt.xlim(0, 12)
plt.ylim(-1, 1)
plt.grid()
plt.show()
