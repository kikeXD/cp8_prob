import random
from matplotlib import pyplot as plt
import numpy as np
import math


ITERATIONS = 10**5


def Uniforme01():
    return random.random()

def UniformeAB(a, b):
    return (b - a) * Uniforme01() + a

def UniformeDiscreta(n):
    return 1 + int(Uniforme01() * n)

def Exponential(l):
    return -1/l * math.log(Uniforme01())

def Ganma(l, a):
    acumulate = 1
    for i in range(a):
        acumulate *= Uniforme01()
    return -1/l * math.log(acumulate)


def PlotUniforme01():
    dict = {}
    for i in range(ITERATIONS):
        n = Uniforme01()

        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    a = [i for i in dict.items()]
    a.sort()

    x = np.arange(-0.3, 1.3, 0.01)
    y = []

    total = 0
    j = 0
    for xi in x:
        while j < len(a) and a[j][0] < xi:
            total += a[j][1]
            j += 1
        y.append(total/ITERATIONS)
            
    plt.plot(x, y)
    plt.show()

def PlotUniformeAB(a, b):
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
            
    plt.plot(x, y)
    plt.show()

def PlotUniformeDiscreta(num):
    dict = {}
    for i in range(ITERATIONS):
        n = UniformeDiscreta(num)

        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    a = [i for i in dict.items()]
    a.sort()

    x = np.arange(0, num, 0.01)
    y = []

    total = 0
    j = 0
    for xi in x:
        while j < len(a) and a[j][0] < xi:
            total += a[j][1]
            j += 1
        y.append(total/ITERATIONS)
            
    plt.plot(x, y)
    plt.show()

def PlotExponential(l):
    dict = {}
    for i in range(ITERATIONS):
        n = Exponential(l)

        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    a = [i for i in dict.items()]
    a.sort()

    x = np.arange(0, 10, 0.01)
    y = []

    total = 0
    j = 0
    for xi in x:
        while j < len(a) and a[j][0] < xi:
            total += a[j][1]
            j += 1
        y.append(total/ITERATIONS)
            
    plt.plot(x, y)
    plt.show()

def PlotGanma(l, a):
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


def main():
    # PlotUniforme01()
    # PlotUniformeAB(4, 10)
    # PlotUniformeDiscreta(5)
    # PlotExponential(0.5)
    PlotGanma(0.5, 10)


if __name__ == '__main__':
    main()
    