from mpmath import *
from sympy import *
import math
import matplotlib.pyplot as plt
import numpy as np
x = symbols('x', real=True)
fx = x - sin(x)

def lnx(n):
    return 1/(fac(n)*2**n) * diff(((1-x**2)**n), x, n)


def ck(n):
    c = integrate(fx*lnx(n), (x, -1, 1))/integrate(lnx(n)**2, (x, -1, 1))
    c = c.subs([(sin(1), math.sin(1)), (cos(1), math.cos(1))])
    return c


def qn(n):
    q = 0
    for i in range(n+1):
        q += lnx(i)*ck(i)
        print(lnx(i)*ck(i))
    print(q)
    return q

qs = qn(3)
xr = np.arange(-1, 1, 0.1)
xr1 = np.arange(-1, 1, 0.2)
# plt.subplot(211)
# plt.title("orig")
plt.plot(xr, [fx.subs(x, xl) for xl in xr], 'b')

# plt.subplot(212)
# plt.title("approximated")
plt.plot(xr, [qs.subs(x, xl) for xl in xr], 'r:')
plt.show()
