import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

def plotOne(x, y, title, xLabel, yLabel, fileName):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linewidth=4)
    plt.title(title, fontsize=14)
    plt.xlabel(xLabel, fontsize=14)
    plt.ylabel(yLabel, fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.grid(visible=True)
    if (fileName != ''):
        plt.savefig(fileName, dpi=600)


def plotMultiple(xArray, yArray, title, xLabel, yLabel, legendEntries):
    plt.figure(figsize=(8, 6))

    for i in range(len(xArray)):
        plt.plot(xArray[i], yArray[i], linewidth=4)

    plt.title(title, fontsize=14)
    plt.xlabel(xLabel, fontsize=14)
    plt.ylabel(yLabel, fontsize=14)
    plt.legend(legendEntries)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.grid(visible=True)