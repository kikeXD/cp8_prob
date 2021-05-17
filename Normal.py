from macros import *
import numpy as np
import matplotlib.pyplot as plt
import math
from Uniforme01 import *
from Exponential import *
from UniformeDiscreta import *


def Normal(miu, o_pow2):
    y = Exponential(1)
    u = Uniforme01()

    if u <= math.pow(math.e, (-1 * math.pow(y - 1, 2)) / 2):
        ud = UniformeDiscreta(2)
        if ud == 1:
            y *= -1
        
        return y * math.sqrt(o_pow2) + miu
    
    return Normal(miu, o_pow2)

def NormalDensity(x, miu, o_pow2):
    return (1 / (math.sqrt(2 * math.pi) * math.sqrt(o_pow2)) * math.pow(math.e, -1 * (math.pow(x - miu, 2) / (2 * o_pow2))))

def NormalDistribution(miu, o_pow2):
    dict = {}
    for i in range(ITERATIONS):
        n = Normal(miu, o_pow2)

        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    arr = [i for i in dict.items()]
    arr.sort()

    x = np.arange(arr[0][0], arr[-1][0], 0.01)
    y = []

    total = 0
    j = 0
    for xi in x:
        while j < len(arr) and arr[j][0] < xi:
            total += arr[j][1]
            j += 1
        y.append(total/ITERATIONS)
            
    return (x, y)


def PlotNormalDensity(miu, o_pow2):
    lis_simulates = []

    for i in range(SIMULATIONS):
        lis_simulates.append([])
        for j in range(ITERATIONS):
            n = Normal(miu, o_pow2)
            lis_simulates[i].append(n)
        lis_simulates[i].sort() 

    for i in range(SIMULATIONS):
        plt.hist(lis_simulates[i], BINS, density=True, histtype='step', label=f'Simulación {i + 1}')

    x = lis_simulates[0]
    y = [NormalDensity(i, miu, o_pow2) for i in x]

    plt.plot(x, y, color='r', label="Densidad real")

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Densidad de v.a. normal')

    plt.show()

def PlotNormalDistribution(miu, o_pow2):
    for i in range(SIMULATIONS):
        x, y = NormalDistribution(miu, o_pow2)

        plt.plot(x, y, label=f'Simulación {i + 1}')

    plt.legend()
    plt.ylabel('Probabilidad')
    plt.title('Distribución de v.a. normal')

    plt.show()

def NormalExpectedValue(miu, o_pow2):
    result = {}
    total = 0
    for i in range(ITERATIONS):
        total += Normal(miu, o_pow2)

    result['expected_value_aprox'] = total / ITERATIONS
    result['expected_value_real'] = miu
    result['error'] = abs(result['expected_value_aprox'] - result['expected_value_real'])

    return result