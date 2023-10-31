""" Investigating Inertia Mismatched Systems

System description and equations from:
https://www.automate.org/industry-insights/understanding-the-mysteries-of-inertia-mismatch
"""

import numpy as np
import control as ct
import matplotlib.pyplot as plt

# Define system parameters
J_m = 1.0  # motor inertia (kg·m²) [0.00005]
N_gearbox = 100.0  # Gearbox ratio
J_l = 10000.0 / (N_gearbox ** 2)  # load inertia (kg·m²) [0.5]
b_m = 0.5  # motor damping
b_l = 0.5  # load damping
b = 5.0  # gearbox damping (N·m·s/rad)
k = 10000  # gearbox stiffness (N·m/rad)
w_l_max = 10
w_m_max = w_l_max * N_gearbox * (2 * np.pi * 60)
print('gear ratio = ' + str(N_gearbox))
print('J_l/J_m = ' + str(J_l/J_m))
print('max input speed required = ' + str(w_m_max) + ' RPM')

num_m = [J_l, b + b_l, k]
num_l = [b, k]

den = [J_m * J_l, (J_m + J_l) * b + J_m * b_l + J_l * b_m, (J_m + J_l) * k + b_m * b_l + b * (b_m + b_l),
       (b_m + b_l) * k, 0]

system_l = ct.tf(num_l, den)
system_m = ct.tf(num_m, den)

# Create a torque input
frequency = 5.0  # Frequency of the torque input (Hz)
amplitude = 1.0  # Amplitude of the torque input (N·m) - adjusted for visualization

# Time vector
t = np.linspace(0, 1 / frequency * 5, 1000)  # 5 seconds, 1000 time points

input_signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Simulate the system and obtain the torque output
# time, torque_output = ct.forced_response(system_m, T=t, U=input_signal)
time, torque_output = ct.step_response(system_m, T=t)

plt.figure()
ct.sisotool(system_m)

# Plot the torque response
plt.figure()
# plt.plot(time, input_signal)
plt.plot(time, torque_output)
plt.title('System Torque Response with Inertias J1 and J2 on Either Side of Gearbox')
plt.xlabel('Time (s)')
plt.ylabel('Torque (N·m)')
plt.grid(True)
plt.show()
