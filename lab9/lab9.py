import numpy as np
import matplotlib.pyplot as plt

def display_surface(func):
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlabel('z')
    plt.tight_layout() # used to show more of the plot - has nothing to do with 3d


    x = np.linspace(-10,10,100)
    y = np.linspace(-10,10,100)
    X, Y = np.meshgrid(x,y)
    ax.plot_surface(X, Y, func(X, Y))
    ax.set_zlim((-10, 10))
    for i in range(360):
        plt.gcf().canvas.draw()
        ax.view_init(elev=30, azim=i)
        plt.pause(0.01)
    plt.show()

def z_func(x, y): return np.cos(x) + np.sin(y)

display_surface(z_func)