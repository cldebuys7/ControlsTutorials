"""Inverted Pendulum Cart from:
https://ctms.engin.umich.edu/CTMS/index.php?example=InvertedPendulum&section=SystemModeling

This code demonstrates the ability of the Python Control Systems Library (control) to convert state-space for a
Multi-Input Multi-Output (MIMO) system to multiple transfer functions (one for each input-output relationship).
"""

import control as ct
import numpy as np
from numpy.linalg import matrix_rank
from matplotlib import pyplot as plt

from PlottingUtilities.Plotters import plotOne, plotMultiple

# define the system
M = 0.5
m = 0.2
b = 0.1
I = 0.006
g = 9.8
l = 0.3

# Denominator for the A and B matrices
den = I * (M + m) + M * m * l ** 2

A = [[0, 1, 0, 0],
     [0, -(I + m * l ** 2) * b / den, (m ** 2 * g * l ** 2) / den, 0],
     [0, 0, 0, 1],
     [0, -(m * l * b) / den, m * g * l * (M + m) / den, 0]]
B = [[0],
     [(I + m * l ** 2) / den],
     [0],
     [m * l / den]]
C = [[1, 0, 0, 0],
     [0, 0, 1, 0]]
D = [[0],
     [0]]

sysStateSpace = ct.ss(A, B, C, D)
transferFunction = ct.ss2tf(sysStateSpace)
print(transferFunction)
cartTF = ct.tf(transferFunction.num[0][0], transferFunction.den[0][0])
pendulumTF = ct.tf(transferFunction.num[1][0], transferFunction.den[1][0])

ct.rlocus(pendulumTF)
co = ct.ctrb(A, B)
controllability = matrix_rank(co)

#############################################################
# simulation the impulse response
#############################################################
time = np.linspace(0, 2, 1000)
timeReturned, systemOutput = ct.impulse_response(sysStateSpace, time)

# plot the impulse response
# plotOne(timeReturned, systemOutput, 'Step Response', 'time [s]', 'Amplitude', '')
plotMultiple([timeReturned, timeReturned], [systemOutput[0][0], systemOutput[1][0]], 'Open Loop Impulse Response',
             'time [s]', 'Amplitude', ['cart [m]', 'pendulum [rad]'])

# Simple PID controller
Kp = 100
Ki = 1
Kd = 20
s = ct.tf('s')
compensatorTF = Kp + Ki / s + Kd * s
closedLoopSystem = ct.feedback(pendulumTF, compensatorTF)
print("Closed Loop System for Pendulum")
print(closedLoopSystem)

time = np.linspace(0, 2, 1000)
timeReturned, closeLoopOutput = ct.impulse_response(closedLoopSystem, time)

# plot the impulse response
plotOne(timeReturned, closeLoopOutput,
        'Pendulum Impulse Response (Kp, Ki, Kd)=(' + str(Kp) + ', ' + str(Ki) + ', ' + str(Kd) + ')', 'time [s]',
        'pendulum angle [rad]', '')

# obtain info about the impulse response
stepInfoData = ct.step_info(closeLoopOutput, timeReturned)
print(stepInfoData)

# What about the cart?
closedLoopSystem = ct.feedback(1, pendulumTF * compensatorTF) * cartTF
print("Closed Loop System for Cart")
print(closedLoopSystem)

timeReturned, closeLoopOutput = ct.impulse_response(closedLoopSystem, time)

# plot the impulse response
plotOne(timeReturned, closeLoopOutput,
        'Cart Impulse Response (Kp, Ki, Kd)=(' + str(Kp) + ', ' + str(Ki) + ', ' + str(Kd) + ')', 'time [s]',
        'cart position [m]', '')

# obtain info about the impulse response
stepInfoData = ct.step_info(closeLoopOutput, timeReturned)
print(stepInfoData)
