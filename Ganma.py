from macros import *
import numpy as np
import matplotlib.pyplot as plt
import math
from Uniforme01 import *

def Ganma(l, a):
    acumulate = 1
    for i in range(a):
        acumulate *= Uniforme01()
    return -1/l * math.log(acumulate)

def PlotGanmaDistribution(l, a):
    dict = {}
    for i in range(ITERATIONS):
        n = Ganma(l, a)

        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    arr = [i for i in dict.items()]
    arr.sort()

    x = np.arange(0, 50, 0.01)
    y = []

    total = 0
    j = 0
    for xi in x:
        while j < len(arr) and arr[j][0] < xi:
            total += arr[j][1]
            j += 1
        y.append(total/ITERATIONS)
            
    plt.plot(x, y)
    plt.show()