import sympy as sp
import matplotlib.pyplot as plt
from control.matlab import *

s = sp.Symbol('s')
t = sp.Symbol('t', positive = True)
sp.init_printing()

#y = sp.expand(sp.inverse_laplace_transform((4*s+12)/((s+1)*(s+2)), s, t))
y =sp. expand(sp.inverse_laplace_transform(s*(s+4)*(s+1)/(s*(s+1)*(s+2)), s, t))
print(y)

sp.plot(y, (t, 0, 10), xlabel = "t", ylabel = "y(t)", ylim = (0, 4))

'''
import sympy as sp
s = sp.Symbol('s')
t = sp.Symbol('t', positive=True)
sp.init_printing()

y =sp. expand(sp.inverse_laplace_transform(s*(s+4)*(s+1)/(s*(s+1)*(s+2)), s, t))
print(y)
sp.plot(y, (t,0,10))
'''