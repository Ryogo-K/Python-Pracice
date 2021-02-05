#ヘヴィサイドの階段関数をプロット
import sympy as sp
from sympy.plotting import plot

sp.var("t")
y = sp.Heaviside(t)
plot(y, (t, -5, 5), xlabel = "t", ylabel = "y")

s = sp.Symbol('s')
t = sp.Symbol('t', positive = True)
a = sp.Symbol('a', real = True)
print(sp.laplace_transform(sp.Heaviside(t), t, s))