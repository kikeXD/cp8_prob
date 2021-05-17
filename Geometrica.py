from macros import *
import numpy as np
import matplotlib.pyplot as plt
import math
from Uniforme01 import *

def Geometrica(p):
    return (math.log(Uniforme01())/math.log(1 - p)) + 1

def GeometricaDensity(x, p):
    return p * math.pow((1 - p), x - 1)

def GeometricaDistributionAnalytic(x, p):
    return 1 - math.pow((1 - p), x - 1)

def GeometricaDistribution(p):
    dict = {}
    for i in range(ITERATIONS):
        n = Geometrica(p)

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


def PlotGeometricaDensity(p):
    lis_simulates = []

    for i in range(SIMULATIONS):
        lis_simulates.append([])
        for j in range(ITERATIONS):
            n = Geometrica(p)
            lis_simulates[i].append(n)
        lis_simulates[i].sort() 

    for i in range(SIMULATIONS):
        plt.hist(lis_simulates[i], BINS, density=True, histtype='step', label=f'Simulación {i + 1}')

    x = lis_simulates[0]
    y = [GeometricaDensity(i, p) for i in x]

    plt.plot(x, y, color='r', label="Densidad real")

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Densidad de v.a. geométrica')

    plt.show()

def PlotGeometricaDistribution(p):
    lis_simulates = []

    for i in range(SIMULATIONS):
        lis_simulates.append(GeometricaDistribution(p))

    for i in range(SIMULATIONS):
        plt.plot(lis_simulates[i][0], lis_simulates[i][1], label=f'Simulación {i + 1}')


    x = lis_simulates[0][0]
    y = [GeometricaDistributionAnalytic(i, p) for i in x]

    plt.plot(x, y, color='r', label="Distribución real")

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Distribución de v.a. geométrica')

    plt.show()

def GeometricaExpectedValue(p):
    result = {}
    total = 0
    for i in range(ITERATIONS):
        total += Geometrica(p)

    result['expected_value_aprox'] = total / ITERATIONS
    result['expected_value_real'] = 1 / p
    result['error'] = abs(result['expected_value_aprox'] - result['expected_value_real'])

    return result