import numpy as np
import matplotlib.pyplot as plt
import im_functions as im

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = plt.imread('trump_img.png')

    img_b = im.to_black_n_white(img)
    plt.imshow(img_b)
    plt.show()


