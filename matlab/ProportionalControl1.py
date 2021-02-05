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

x = range(1, 5)
y = []
for i in x:
    print(i, end = "\r")
    print(sp.inverse_laplace_transform(Kp * Rs * Ps / ((Kp * Ps) + 1), s, t))
#print(y)
#グラフのプロット
plt.plot(x, y)
#表示
plt.show()