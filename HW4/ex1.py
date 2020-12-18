'''
yair pinhas 307926048
'''
import numpy as np
import matplotlib.pyplot as plt

'''
# 1
'''
def fourier_approx(f: str, cn: str, xSize= 1000, m= 100):
    '''
     ploting the fourier complax function e^x

     :param f: (str) function
     :param cn: (str) the coefficients of f
     :param xSize: the x_axis
     :param m: max len of cn
     :return:
    '''
    x = np.linspace(-np.pi ,np.pi , xSize)
    n = 0
    c0 = eval(cn)
    f_ = eval(f)
    y = np.zeros(x.shape, dtype=np.complex)
    y += c0

    dx = x[1] - x[0]
    for n in range(1 , m):
        plt.clf()
        c_n_pluse = eval(cn)
        y += c_n_pluse * np.exp(1j * n * x)

        n *= -1
        c_n_minus = eval(cn)
        y += c_n_minus * np.exp(1j * n * x)
        plt.plot(x, f_, label='original')
        plt.plot(x, y, label='approximation')
        plt.show()
        plt.pause(0.1)



'''
# 2 , 3
ploting the exp(x)  and exp(-|x|) by complax fourier aproximation
'''
if __name__ == '__main__':

    c_n = '(1 / (2 * np.pi)) * (((1 - ((-1)**n) * np.exp(-np.pi)) / (1 - 1j * n)) + ((1 - ((-1)**n) * np.exp(-np.pi)) / (1 + 1j * n)))'
    f = 'np.exp(-np.abs(x))'
    fourier_approx(f, c_n)

    c_n = '(((-1)**n) * (np.exp(np.pi) - np.exp(-np.pi))) / (2 * np.pi * (1 - 1j*n))'
    f = 'np.exp(x)'
    fourier_approx(f, c_n)
