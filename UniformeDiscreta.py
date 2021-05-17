from macros import *
import numpy as np
import matplotlib.pyplot as plt
from Uniforme01 import *

def UniformeDiscreta(n):
    return 1 + int(Uniforme01() * n)

def UniformeDiscretaDistribution(num):
    dict = {}
    for i in range(ITERATIONS):
        n = UniformeDiscreta(num)

        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    a = [i for i in dict.items()]
    a.sort()

    x = np.arange(0, num + 1, 0.01)
    y = []

    total = 0
    j = 0
    for xi in x:
        while j < len(a) and a[j][0] < xi:
            total += a[j][1]
            j += 1
        y.append(total/ITERATIONS)
            
    return (x, y)


def PlotUniformeDiscretaDistribution(num):
    lis_simulates = []

    for i in range(SIMULATIONS):
        lis_simulates.append(UniformeDiscretaDistribution(num))

    for i in range(SIMULATIONS):
        plt.plot(lis_simulates[i][0], lis_simulates[i][1], label=f'Simulación {i + 1}')

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Distribución de v.a. uniforme discreta')

    plt.show()

def UniformeDiscretaExpectedValue(num):
    result = {}
    total = 0
    for i in range(ITERATIONS):
        total += UniformeDiscreta(num)

    result['expected_value_aprox'] = total / ITERATIONS
    result['expected_value_real'] = (num + 1) / 2
    result['error'] = abs(result['expected_value_aprox'] - result['expected_value_real'])

    return result