# This is a sample Python script.

import matplotlib.pyplot as plt
import numpy as np

# 1
x = np.linspace(-16, 16, 1000)
y = x ** 2
y2 = -2*x**2 + 4*x + 3

plt.plot(x, y)
plt.plot(x, y2)
plt.show()