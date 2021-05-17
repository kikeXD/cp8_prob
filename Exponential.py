from macros import *
import numpy as np
import matplotlib.pyplot as plt
import math
from Uniforme01 import *

def Exponential(l):
    return -1/l * math.log(Uniforme01())

def ExponentialDensity(x, l):
    if x > 0:
        return l * math.pow(math.e, -1 * l * x)
    return 0

def ExponentialDistributionAnalytic(x, l):
    if x > 0:
        return 1 - math.pow(math.e, -1 * l * x)
    return 0

def ExponentialDistribution(l):
    dict = {}
    for i in range(ITERATIONS):
        n = Exponential(l)

        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    a = [i for i in dict.items()]
    a.sort()

    x = np.arange(a[0][0], a[-1][0], 0.01)
    y = []

    total = 0
    j = 0
    for xi in x:
        while j < len(a) and a[j][0] < xi:
            total += a[j][1]
            j += 1
        y.append(total/ITERATIONS)
            
    return (x, y)


def PlotExponentialDensity(l):
    lis_simulates = []

    for i in range(SIMULATIONS):
        lis_simulates.append([])
        for j in range(ITERATIONS):
            n = Exponential(l)
            lis_simulates[i].append(n)
        lis_simulates[i].sort() 

    for i in range(SIMULATIONS):
        plt.hist(lis_simulates[i], BINS, density=True, histtype='step', label=f'Simulación {i + 1}')

    x = lis_simulates[0]
    y = [ExponentialDensity(i, l) for i in x]

    plt.plot(x, y, color='r', label="Densidad real")

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Densidad de v.a. exponencial')

    plt.show()

def PlotExponentialDistribution(l):
    lis_simulates = []

    for i in range(SIMULATIONS):
        lis_simulates.append(ExponentialDistribution(l))

    for i in range(SIMULATIONS):
        plt.plot(lis_simulates[i][0], lis_simulates[i][1], label=f'Simulación {i + 1}')

    x = lis_simulates[0][0]
    y = [ExponentialDistributionAnalytic(i, l) for i in x]

    plt.plot(x, y, color='r', label="Distribución real")

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Distribución de v.a. exponencial')

    plt.show()

def ExponentialExpectedValue(l):
    result = {}
    total = 0
    for i in range(ITERATIONS):
        total += Exponential(l)

    result['expected_value_aprox'] = total / ITERATIONS
    result['expected_value_real'] = 1 / l
    result['error'] = abs(result['expected_value_aprox'] - result['expected_value_real'])

    return result