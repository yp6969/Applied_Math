import numpy as np
import matplotlib.pyplot as plt
import im_functions as im
import similarity as sim
import sys

if __name__ == '__main__':
    try:
        img2 = plt.imread(sys.argv[1])
    except IOError:
        print("File",sys.argv[1]," does not exist" , file=sys.stderr)
        exit(1)

    img1 = plt.imread('circle128x128.png')
    plt.subplot(1, 2, 1)
    plt.imshow(img1)

    plt.subplot(1, 2, 2)
    plt.imshow(img2)

    plt.show()

    print("similarity:",sim.similarity(img1, img2))
    print("similarity (inner product):",sim.similarity2(img1, img2))