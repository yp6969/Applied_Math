import numpy as np
import matplotlib.pyplot as plt

'''
mclauren function
'''
def mclauren():
    x = np.linspace(-10,10,1000)
    dx = x[1] - x[0]
    y = np.zeros(x.shape)

    for n in range(50):
        an = 1/np.math.factorial(n)
        y += an * (x ** n)
        plt.ylim(-2,10)
        plt.plot(x, np.exp(x) , label = 'original')
        plt.plot(x, y, label ='approximation')
        plt.show()
        plt.pause(0.1)


def fourier_approx(fx ,nmax=25, speed=0.5):
    x = np.linspace(-np.pi ,np.pi , 1000)
    y = np.zeros(x.shape)
    dx = x[1] - x[0]
    a0 = (1/np.pi) * np.trapz(fx(x), x, dx)
    y += (a0/2)
    for n in range(1 , nmax):
        an = (1/np.pi) * np.trapz( fx(x) * np.cos(n*x), x, dx)
        bn = (1/np.pi) * np.trapz( fx(x) * np.sin(n*x), x, dx)
        y += an * np.cos(n*x) + bn * np.sin(n*x)

        plt.plot(x, fx(x), label='original')
        plt.plot(x, y, label='approximation')
        plt.show()
        plt.pause(speed)



if __name__ == '__main__':
    x = np.linspace(-np.pi ,np.pi , 1000)
    dx = x[1] - x[0]
    fx = lambda x: x**2
    fourier_approx(fx)
    # mclauren()