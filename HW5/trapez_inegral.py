import numpy as np
import matplotlib.pyplot as plt

def fourierEstComplex(m,N,func,xl,xr):
    """
    fourierEstComplex computes a partial sum of fourier series
    for a given function on the interval [a,b]. The Fourier coefficients
    cn are calculated numerically. The function returns a vector, which is
    the Fourier complex series estimate of the (sampled) function using
    the partial sum.
    Input arguments: m - partial sum order
    xl - the left delimiter of the section (of the x axis [default –pi])
    xr - the right delimiter of the section (of the x %axis [default pi])
    N - number of points on the x axis.
    func - a string containing the function for which % the series is
    computed.
    The function returns the vecotr y - the partial sum of the Fourier
    series
    Usage: y = fourierEstComplex(m, N, func, xl, xr)
    Example: y=fourierEstComplex(150,10000,'x.^2', -1, 1);
    """
    x = np.linspace(xl, xr , N)
    f = eval(func)
    h = (xr - xl) / N
    dx = xr - xl
    trapez = lambda f_x: 0.5 * h * (f_x[0] + 2 * sum(f_x[1:-2]) + f_x[-1]) # calculating the inregral

    # calculate c_0
    c_0 = (1/dx) * trapez(f)
    fourier_func = np.zeros(x.shape , dtype=np.complex)
    fourier_func += c_0

    for n in range(1,m):
        plt.clf()

        n *= -1

        g_x = f * np.exp(-(2 * np.pi * 1j * n * x)/dx)
        c_n = (1/dx) * trapez(g_x)
        fourier_func += c_n * np.exp((2 * np.pi * 1j * n * x)/dx)
        n *= -1

        g_x = f * np.exp(-(2 * np.pi * 1j * n * x) / dx)
        c_n = (1 / dx) * trapez(g_x)
        fourier_func += c_n * np.exp((2 * np.pi * 1j * n * x) / dx)

        plt.plot(x, f, label='original')
        plt.plot(x, fourier_func, label='approximation')
        plt.show(block=False)
        plt.pause(0.1)


y = fourierEstComplex(150 ,10000, 'x**(1/3)' , 0 , 2)