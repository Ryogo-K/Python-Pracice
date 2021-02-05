#P制御プログラム
import sympy as sp
import matplotlib.pyplot as plt
s = sp.Symbol('s')
#開始値
pos = 0
#目標値
Target = 1
#比例ゲイン
Kp = 20
Ki = 0
Kd = 0
Cs = Kp + (Ki / s) + Kd * s
#制御対象
Ps = 1 / s 
t = sp.Symbol('t', positive = True)
Rs = Target / s
Ys = sp.inverse_laplace_transform(Kp * Rs * Ps / ((Kp * Ps) + 1), s, t)
print(Ys)
x = range(0, 200)
y = []
for i in x:
    y.append(Ys.subs(t, i))
#print(y)
#グラフのプロット
plt.plot(x, y)
#表示
plt.show()