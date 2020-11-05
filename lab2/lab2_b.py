

import matplotlib.pyplot as plt
import numpy as np
# 2.

img = plt.imread('./cameraman.png')
plt.subplot(1, 2, 1)
plt.set_cmap('gray')
plt.imshow(img)
plt.subplot(1, 2, 2)
x2 = img[::-1]
plt.set_cmap('gray')
plt.imshow(x2)
plt.show()