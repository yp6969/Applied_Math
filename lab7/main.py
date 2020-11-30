import numpy as np
import matplotlib.pyplot as plt

def findRes(complex, n):
    res = np.zeros(n , dtype=np.complex)
    r = np.abs(complex)
    angle = np.angle(complex)
    for i in range(n):
        res[i] = r**(1/n)*(np.cos((angle+2*np.pi *i)/n) + 1j*np.sin((angle+2*np.pi*i)/n))
    return res

R = findRes(7+5j , 5)

plt.polar(np.angle(R) , np.abs(R), linewidth=0 , marker="x")
# plt.plot(R.real , R.imag)
plt.show()