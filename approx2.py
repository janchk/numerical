import numpy as np
import numpy.linalg as npl
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import sin
# from sympy import *

def func(x):
    return x - sin(x)

# x = symbols('x', real=True)
# fx = x - sin(x)

# def func(x):
#     return x - math.sin(x)


def getQline(x, m):
    return [np.power(x, i) for i in range(0, m)]


def toLegInterv(x):
    return (rs - ls) * x / 2 + (ls + rs) / 2

ls = -1
rs = 1

def kvadrApproximate():
    n = 20
    m = 4
    aprn = 80
    realn = 200
    x0 = np.linspace(ls, rs, n)
    xr = np.linspace(ls, rs, realn)
    yr = [func(i) for i in xr]
    x1 = np.linspace(ls, rs, aprn)
    y0 = [func(i) for i in x0]


    Q = [getQline(x,m) for x in x0]
    Qt = np.transpose(Q)
    H = np.dot(Qt, Q)
    b = np.dot(Qt, y0)
    a = npl.solve(H, b)
    y1 = np.dot(np.transpose(a), getQline(x1,m))

    plt.plot(x1, y1, 'r')
    plt.plot(xr, yr, 'g:')
    plt.plot(x0, y0, 'b-')
    plt.plot(x0, y0, 'ro')
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title(" x - sin(x) \nApproximation")
    plt.grid(True)
    plt.show()


kvadrApproximate()