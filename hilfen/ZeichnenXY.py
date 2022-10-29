import sys
import math
import matplotlib.pyplot as plt
import numpy as np

#  https://matplotlib.org/stable/gallery/index.html

# Data for plotting
x = np.arange(-2.0, 2.0, 0.01)
y = 0 + np.sin(2 * np.pi * x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()