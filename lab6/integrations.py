import numpy as np
import matplotlib.pyplot as plt

def integrate(func, a, b, nrects):
    """
    :param func: the function to integrate
    :param a: start of the integration; should be lower than b
    :param b: end of the integration; should be higher than a
    :param nrects: number of rectangles to sum
    :return: the value of the integrated function between a and b
    """
    dx = (b-a)/nrects
    riman_sum = 0
    for i in np.arange(a,b,dx):
        riman_sum += func(i)*dx
    return riman_sum



def integration_animation(func, a, b, nmax, speed):
    """
    :param func: the function to integrate
    :param a: start of integration
    :param b: end of integration
    :param nmax: stop after nmax rectangles
    :param speed: speed of the animation in seconds
    """
    n=1
    xx = np.linspace(a, b, 1000)

    for j in range(n,nmax):
        plt.clf()
        plt.plot(xx, func(xx))
        dx = (b-a)/n
        for i in np.arange(a,b,dx):
            plt.plot([i,i], [0,func(i)],color='b')
            plt.plot([i+dx,i+dx], [0,func(i)],color='b')
            plt.plot([i,i+dx], [func(i),func(i)],color='b')
            plt.plot([i,i+dx], [func(i),func(i)],color='b')
            plt.show(block=False)
        n+=1
        plt.pause(0.05)



def f(x): return x**2
integration_animation(f,0,3,80,0.1)





