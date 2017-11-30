import numpy as np
from sympy import *

N = 1
x, y, z = symbols('x y z', real=True)
var = [x, y, z]
f = 2*x**2 + (3 + 0.1*N)*y**2 + (4 + 0.1*N)*z**2 + x*y - y*z + x*z + x - 2*y + 3*z + N
# f = x**2 + x * y + y**2 - 2*x + y

A = np.array([[4, 1, 0], [0, 6.2, 1], [1, 0, 8.2]])
b = np.array([[-2], [3], [1]])
start = np.random.randn(3, 1)*10

# A = np.array([[2, 1], [1, 2]])
# b = np.array([[-2], [1]])
# start = np.array([[1], [0]])


# def dist(first, second):
#     a = 0
#     for i in range(0, len(first)-1):
#         a += first[i]**2 + second[i]**2
#     return float(a**1/2)


def grad(A, b, point):
    return np.dot(A, point) + b


def move_stpd(p):
    qi = np.array([[[1], [0], [0]], [[0], [1], [0]], [[0], [0], [1]]])
    p = p
    for q in qi:
        Aq = np.dot(A, q)
        qT = np.transpose(q)
        step = np.dot(qT, np.dot(A, p) + b)/np.dot(qT, Aq)
        p = np.array([x - float(step) * q[i] for i, x in enumerate(p)])
    return p


def move_grad(p):
    q = grad(A, b, p)
    Aq = np.dot(A, q)
    qT = np.transpose(q)
    step = np.dot(qT, q)/np.dot(qT, Aq)
    return np.array([x - float(step)*q[i] for i, x in enumerate(p)])


def fgd(par):
    i = 0
    p = start
    fxyz = 0
    # prev = move_grad(p)
    while True:
        fxyz_old = fxyz
        # prev = p
        if par == 'grad':
            p = move_grad(p)
        else:
            p = move_stpd(p)
        i += 1
        x1,y1,z1 = p[0], p[1], p[2]
        fxyz = (f.subs([(x, x1), (y, y1), (z, z1)]))
        print(fxyz, " ", i)
        if abs(fxyz_old - fxyz) < 10**-6:
            break
# fgd("grad")
fgd("gra")


########################################################################################################################

# def grad_sym(f, var):
#     return np.array([diff(f, i) for i in var])
#
#
# def move_sym(start, step):
#     return np.array([start[i] - step * grad_sym(f, var)[i].subs([(x, start[0]), (y, start[1]), (z, start[2])])
#                      for i, item in enumerate(start)])

# print(move_sym([0, 0, 0], 2))

# d = grad_sym(f, var)
# print(dx)
# x = 0
# ans = [d.subs(,)]
# print(dx.subs([(x, 1), (y, 2), (z, 0)]))
# print(grad(f,var))
# def fgd():
