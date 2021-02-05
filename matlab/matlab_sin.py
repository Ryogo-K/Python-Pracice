#正弦波のプロットを出力

import matplotlib.pyplot as plt
import math
x = range(0, 360)
y = [math.sin(math.radians(d)) for d in x]
plt.plot(x, y)
plt.show()