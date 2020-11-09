import numpy as np
import matplotlib.pyplot as plt

def to_black_n_white(img):
    # shape = img.shape
    img_b = np.average(img , axis=-1)
    print(np.shape(img_b))
    avg = 256/2
    # for i in range(shape[0]):
    #     for j in range(shape[1]):
    #         avg = np.average(img[i,j]) / 255
    #         if avg >= 0.5:
    #             img_b[i,j] = 1
    #         else: img_b[i,j] = 0
    img_b[img_b < avg] = 0
    img_b[img_b >= avg] = 1
    return img_b
