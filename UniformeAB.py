from macros import *
import numpy as np
import matplotlib.pyplot as plt
from Uniforme01 import *

def UniformeAB(a, b):
    return (b - a) * Uniforme01() + a

def UniformeABDensity(x, a, b):
    if x >= a and x <= b:
        return 1 / (b - a)
    return 0

def UniformeABDistributionAnalitic(x, a, b):
    if x >= b:
        return 1
    if x >= a and x <= b:
        return (x - a) / (b - a)
    return 0

def UniformeABDistribution(a, b):
    dict = {}
    for i in range(ITERATIONS):
        n = UniformeAB(a, b)

        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    arr = [i for i in dict.items()]
    arr.sort()

    x = []
    y = []
    total = 0
    
    x = np.arange(a - 1, b + 1, 0.01)
    y = []

    total = 0
    j = 0
    for xi in x:
        while j < len(arr) and arr[j][0] < xi:
            total += arr[j][1]
            j += 1
        y.append(total/ITERATIONS)
            
    return (x, y)


def PlotUniformeABDensity(a, b):
    lis_simulates = []

    for i in range(SIMULATIONS):
        lis_simulates.append([])
        for j in range(ITERATIONS):
            n = UniformeAB(a, b)
            lis_simulates[i].append(n)
        lis_simulates[i].sort() 

    for i in range(SIMULATIONS):
        plt.hist(lis_simulates[i], BINS, density=True, histtype='step', label=f'Simulación {i + 1}')

    x = lis_simulates[0]
    y = [UniformeABDensity(i, a, b) for i in x]

    plt.plot(x, y, color='r', label="Densidad real")

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Densidad de v.a. uniforme ab')
    plt.show()

def PlotUniformeABDistribution(a, b):
    lis_simulates = []

    for i in range(SIMULATIONS):
        lis_simulates.append(UniformeABDistribution(a, b))

    for i in range(SIMULATIONS):
        plt.plot(lis_simulates[i][0], lis_simulates[i][1], label=f'Simulación {i + 1}')

    x = lis_simulates[0][0]
    y = [UniformeABDistributionAnalitic(i, a, b) for i in x]

    plt.plot(x, y, color='r', label="Distribución real")

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Distribución de v.a. uniforme ab')

    plt.show()

def UniformeABExpectedValue(a, b):
    result = {}
    total = 0
    for i in range(ITERATIONS):
        total += UniformeAB(a, b)

    result['expected_value_aprox'] = total / ITERATIONS
    result['expected_value_real'] = (a + b) / 2
    result['error'] = abs(result['expected_value_aprox'] - result['expected_value_real'])

    return result