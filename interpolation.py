import numpy as np
import matplotlib.pyplot as plt
import math

ls = -1
rs = 1


def f(x):
    return x - math.sin(x) - 0.25


def h(x):
    return abs(x) * f(x)


def Lagrange(x, y, t):
    z = 0
    for j, yj in enumerate(y):
        p1 = 1
        p2 = 1
        for i, xi in enumerate(x):
            if i != j:
                p1 *= (t - x[i])
                p2 *= (x[j] - xi)
        z += yj * p1 / p2
    return z


def nodes(a, b, n):
    return [((b - a) * math.cos(((2 * i + 1) * math.pi)/(2 * n + 2)) + (b + a))/2 for i in range(0, n)]


def fst(nodes_num):
    x0 = np.linspace(ls, rs, num=1000)
    y0 = [f(i) for i in x0]  # Vanilla

    x = np.linspace(ls, rs, num=nodes_num)

    y = [f(i) for i in x]
    y1 = [Lagrange(x, y, i) for i in x]
    x1 = nodes(ls, rs, nodes_num)  # formula 3.2
    y2 = [Lagrange(x1, y, i) for i in x1]

    plt.plot(x, y1, 'g--', linewidth=1)  # fixed
    plt.plot(x, y2, 'b:')  # optimal
    plt.plot(x0, y0, 'r', linewidth=1)  # function
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title(" y = x - sin(x) - 0.25 \nInterpolation with %d dots" % nodes_num)
    plt.grid(True)
    plt.show()


def scnd(nodes_num):
    x = np.linspace(ls, rs, num=nodes_num)
    y = [h(i) for i in x]
    x_p = np.linspace(ls, rs, num=100)
    y1 = [Lagrange(x, y, i) for i in x_p]
    x1 = np.multiply(nodes(ls, rs, len(x_p)), 1)
    y2 = [Lagrange(x1, y1, i) for i in x1]

    plt.plot(x_p, y1, 'r')  # module with fixed step
    plt.plot(x_p, y2, 'b--')  # module with optimal step
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title(" y = x - sin(x) - 0.25 \nInterpolation with a %d dots" % nodes_num)
    plt.grid(True)
    plt.show()


# fst(10)
scnd(20)