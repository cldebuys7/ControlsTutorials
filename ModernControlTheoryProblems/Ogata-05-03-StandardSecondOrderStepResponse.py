"""Programs 5-3 through 5-5 from Modern Control Engineering - Ogata, 5th Edition (p. 189-191)

This code demonstrates the ability of the Python Control Systems Library (control) to generate the impulse response of
a second order systems given its transfer functions. This is a Matlab example from Ogata's book, generated in Python.
"""

import numpy as np
import control as ct
import matplotlib.pyplot as plt


def create_second_order_transfer_function(wn, zeta):
    num = [wn ** 2]
    den = [1, 2 * zeta * wn, wn ** 2]
    return ct.tf(num, den)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Program 5-3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
wn = 5
zeta = 0.4
transfer_function = create_second_order_transfer_function(wn, zeta)
print(transfer_function)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Program 5-4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
t, y = ct.step_response(transfer_function)
plt.figure()
plt.plot(t, y)
plt.title('Unit-Step Response of G(s) = 25/(s^2 + 4s + 25)')
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.grid()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Program 5-5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
# This is the same as above. The only difference is that the time vector is created manually.
t = np.linspace(0, 3, 300)
t, y = ct.step_response(transfer_function, t)
plt.figure()
plt.plot(t, y)
plt.title('Unit-Step Response of G(s) = 25/(s^2 + 4s + 25)')
plt.xlabel('time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
