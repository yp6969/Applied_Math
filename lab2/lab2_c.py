import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)

img = plt.imread('./cameraman.png')
plt.subplot(2, 2, 1)
plt.set_cmap('gray')
plt.imshow(img)

img_2 = np.rot90(img)
plt.subplot(2, 2, 2)
plt.set_cmap('gray')
plt.imshow(img_2)

img_3 = np.rot90(img_2)
plt.subplot(2, 2, 3)
plt.set_cmap('gray')
plt.imshow(img_3)

img_4 = np.rot90(img_3)
plt.subplot(2, 2, 4)
plt.set_cmap('gray')
plt.imshow(img_4)
plt.show()





