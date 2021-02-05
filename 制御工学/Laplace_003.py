#逆ラプラス変換
import sympy as sp
s = sp.Symbol('s')
t = sp.Symbol('t', positive = True)
print(sp.inverse_laplace_transform(1 / ((s + 1) * (s + 2)), s, t))