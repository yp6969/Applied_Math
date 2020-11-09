import numpy as np
import matplotlib.pyplot as plt
import im_functions as im
import similarity as sim

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(sys.argv)
    img = plt.imread('trump_img.jpg')
    img_b = im.to_black_n_white(img)
    plt.imshow(img_b)

    yair1 = plt.imread('yair1.png')
    yair2 = plt.imread('yair2.png')
    # print(sim.similarity(yair1,yair2))
    plt.show()

