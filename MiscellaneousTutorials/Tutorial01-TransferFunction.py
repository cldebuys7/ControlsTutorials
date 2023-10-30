import control as ct
import matplotlib

# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from PlottingUtilities.Plotters import plotOne, plotMultiple

# define the transfer function
numeratorCoefficients = [1]
denominatorCoefficients = [1, 2, 4]

W = ct.tf(numeratorCoefficients, denominatorCoefficients)
print(W)
##########################################
# simulate the step response
##########################################
time = np.linspace(0, 5, 100)
timeReturned, systemOutput = ct.step_response(W, time)

# plot the step response
# poopyFunction(timeReturned, systemOutput, 'Step Response', 'time [s]', 'output', 'stepResponse.png')
plotOne(timeReturned, systemOutput, 'Step Response', 'time [s]', 'output', '')

##########################################
# simulate the forced response
##########################################
time2 = np.linspace(0, 10, 200)
# input2 = np.sin(2 * time2) + np.ones(time2.shape)
input2 = np.sin(2 * time2)

# plot the input
# plottingFunction(time2, input2, 'Input', 'time [s]', 'input', 'input.png')

# compute the forced response and plot
timeReturned2, systemOutput2 = ct.forced_response(W, time2, input2)
# plottingFunction(timeReturned2, systemOutput2, 'Sinusoid Response', 'time [s]', 'output', 'sinusoidResponse.png')

# plot both trends
xVec = [time2, timeReturned2]
yVec = [input2, systemOutput2]
plotMultiple(xVec, yVec, 'System Response', 'time [s]', 'Amplitude', ['input', 'output'])

# show all the plots
plt.show()
