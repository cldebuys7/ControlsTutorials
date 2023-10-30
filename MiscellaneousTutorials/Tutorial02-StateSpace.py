import control as ct
import matplotlib

# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from PlottingUtilities.Plotters import plotOne, plotMultiple

# define the system
#   xdot = Ax + Bu
#      y = Cx + Du
A = np.array([[0, 1], [-4, -2]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# create a state space model
sysStateSpace = ct.ss(A, B, C, D)
print(sysStateSpace)

# generate a transfer function for this system
transferFunction1 = ct.ss2tf(sysStateSpace)
# transferFunction1 = ct.ss2tf(A,B,C,D)
print(transferFunction1)

# generate a state space model from the transfer function (model may be shifted but is equivalent)
sysStateSpace2 = ct.tf2ss(transferFunction1)
print(sysStateSpace2)

#############################################################
# simulation the step response
#############################################################
time = np.linspace(0, 5, 100)
timeReturned, systemOutput = ct.step_response(sysStateSpace, time)

# plot the step response
plotOne(timeReturned, systemOutput, 'Step Response', 'time [s]', 'Amplitude', '')

# obtain info about the step response
stepInfoData = ct.step_info(sysStateSpace)
print(stepInfoData)

# compute natural frequencies, damping ratios, poles & zeros, and pole-zero map
ct.damp(sysStateSpace, doprint=True)
ct.poles(sysStateSpace)
ct.zeros(sysStateSpace)
plt.figure(figsize=(8, 6))
ct.pzmap(sysStateSpace)

# Similar to Matlab SISO tool. Plots bode plots, root locus, and step response.
ct.sisotool(sysStateSpace)

#############################################################
# discretize the state-space model
#############################################################
sampleTime = 0.5
# discretize the system dynamics
#   'zoh' - zero order hold
#   'bilinear' - bilinear
discreteSystemZOH = ct.sample_system(sysStateSpace, sampleTime, method='zoh')
print(discreteSystemZOH)

# check is the system is in discrete time
discreteSystemZOH.isdtime()
print(discreteSystemZOH)

# compute the step response
time2 = np.linspace(0, 5, np.int32(np.floor(5 / sampleTime) + 1))
timeReturned2, systemOutput2 = ct.step_response(discreteSystemZOH, time2)
# plotOne(timeReturned2,systemOutput2,'Step Response of Discrete System','time [s]','Amplitude','')
plotMultiple([timeReturned, timeReturned2], [systemOutput, systemOutput2],
             'Step Response (Zero Order Hold): Sample Time = ' + str(sampleTime) + ' s', 'time [s]', 'Amplitude',
             ['continuous', 'discrete'])

discreteSystemBilinear = ct.sample_system(sysStateSpace, sampleTime, method='bilinear')
timeReturned3, systemOutput3 = ct.step_response(discreteSystemBilinear, time2)
plotMultiple([timeReturned, timeReturned3], [systemOutput, systemOutput3],
             'Step Response (Bilinear Transform): Sample Time = ' + str(sampleTime) + ' s', 'time [s]', 'Amplitude',
             ['continuous', 'discrete'])

# plt.show()
