import numpy as np
import matplotlib.pyplot as plt
import im_functions as im
import sys

def similarity(img1,img2):
    if img1.shape != img2.shape:
        print("images are not the same size", file=sys.stderr)
        return
    if len(img1.shape) == 3: img1 = im.to_black_n_white(img1)
    if len(img2.shape) == 3: img1 = im.to_black_n_white(img2)
    plt.imshow(img1)
    plt.show()
    img1 = np.ravel(img1)
    img2 = np.ravel(img2)

    cmp = np.zeros(img1.shape)
    cmp[img1 == img2] = 1
    return sum(cmp)/len(cmp)