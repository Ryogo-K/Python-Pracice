from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np

def plot_set(fig_ax, *args):
    fig_ax.set_xlabel(args[0])
    fig_ax.set_ylabel(args[1])
    fig_ax.grid(ls=":")
    if len(args) == 3:
        fig_ax.legend(loc = args[2])

fig, ax = plt.subplots(figsize = (8, 6))

P = tf([0, 1], [1, 1, 1])

freq = 1
Td = np.arange(0, 30, 0.01)
u = np.sin(freq * Td)
y, t, x0 = lsim(P, u, Td, 0)

ax.plot(t, u, ls = '--', label = 'u', color = 'k')
ax.plot(t, y, label = 'y', color = 'k')
plot_set (ax, 't', "u, y")
plt.show()