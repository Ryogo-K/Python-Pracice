#さまざまな数をラプラス変換する
import sympy as sp

s = sp.Symbol('s')
t = sp.Symbol('t', positive = True)

#1のラプラス変換
print(sp.laplace_transform(1, t, s))
#tのラプラス変換
print(sp.laplace_transform(t, t, s))
#e^atのラプラス変換
a = sp.Symbol('a', real=True)
print(sp.laplace_transform(sp.exp(-a * t), t, s))
