import numpy as np
import matplotlib.pyplot as plt
import time
''' Fourier synthsis 
a0
an = dependent with n 
m = 
N = 
return the parial sum of order m of fourier series

useg: y = fourierSynthesis(a0, an, bn, func, m, N)
'''

def fourierSynthesis(a0, an, bn, func, m, N):

    x = np.linspace(-np.pi, np.pi, N)
    y = np.zeros(x.size)
    f = eval(func)
    plt.figure(1)
    plt.plot(x,f,'r')

    Sm = np.zeros(x.size) + a0/2  #the partial sum

    for n in range(1,m):
        '''
        calculate the partial sum
        '''
        a_n = eval(an)
        b_n = eval(bn)
        Sm += a_n * np.cos(n * x) + b_n * np.sin(n * x)

        plt.figure(1)
        plt.plot(x,Sm)
        plt.grid(axis = 'both')
        stitle = 'Fourier series partial sum n = ' + str(n)
        plt.title(stitle)
        plt.plot(x,f,'r')

        plt.show()
        time.sleep(0.01)
    return y



'''
test the function
'''
a0 = 0
an = '0'
bn = '(2*(1+(-1)**(n+1))/(np.pi * n))'
func = 'np.sign(x)'
m = 100
N = 1000
y = fourierSynthesis(a0, an, bn, func, m, N)

time.sleep(5)


a0 = 0
an = '0'
bn = '2*((-1)**(n+1))/n'
func = 'x'

y = fourierSynthesis(a0, an, bn, func, m, N)
