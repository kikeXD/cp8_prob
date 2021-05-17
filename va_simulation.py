from UniformeAB import *
from UniformeDiscreta import *
from Geometrica import *
from Exponential import *
from Ganma import *
from Normal import *

def main():
    print('Uniforme discreta:')
    num = 5
    print(UniformeDiscretaExpectedValue(num))
    PlotUniformeDiscretaDistribution(num)
    print('-------------')

    print('Geométrica:')
    p = 1/10
    print(GeometricaExpectedValue(p))
    PlotGeometricaDensity(p)
    PlotGeometricaDistribution(p)
    print('-------------')

    print('Uniforme AB:')
    a = 4
    b = 10
    print(UniformeABExpectedValue(a, b))
    PlotUniformeABDensity(a, b)
    PlotUniformeABDistribution(a, b)
    print('-------------')

    print('Exponencial:')
    l = 0.5
    print(ExponentialExpectedValue(l))
    PlotExponentialDensity(l)
    PlotExponentialDistribution(l)
    print('-------------')

    print('Normal:')
    miu = 0
    o_pow2 = 1
    print(NormalExpectedValue(miu, o_pow2))
    PlotNormalDensity(miu, o_pow2)
    PlotNormalDistribution(miu, o_pow2)
    print('-------------')


if __name__ == '__main__':
    main()
    