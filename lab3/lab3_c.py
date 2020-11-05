import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('picture.jpg')

img2 = np.array(img)

print(img2)
for i in range(len(img)):
    for j in range(len(img[0])):
        r,g,b = img2[i,j]
        img2[i,j] = b,g,r



# plt.figure()
# plt.subplot(1,2,1)
plt.imshow(img2)
plt.imsave('image.png',img2)
plt.show()

