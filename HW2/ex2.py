import time
import numpy as np
import matplotlib.pyplot as plt
import random
from numpy import linalg as lin

def similarty(A,B):
    A_t = np.transpose(A)
    inner = lambda x,y: np.trace(x*y)
    return np.absolute(inner(A_t,B))/(lin.norm(A)*lin.norm(B))



X = np.zeros([8,8])
X[ 1, 1:3 ] = 1
X[ 1, 5:7 ] = 1
X[ 3, 3:5 ] = 1
X[ 5:7, 1::5 ] = 1
X[6,2:6] = 1

X2 = [[1 if j==0 else 0 for j in i] for i in X]


Th = 0.7 #threshold
ipN = 0 # normal inner product
L = 8 # len of Xtest
testCnt = 0 # count the number of tests

Xtest = np.zeros((L,L))

while ipN < Th:
    Xtest[1:L - 1, 1:L - 1] = (np.random.rand(L - 2, L - 2)) > 0.6
    Xtest1 = Xtest.astype(float)

    plt.subplot(1, 2, 1)
    plt.title('template face')
    plt.imshow(X, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title('test face')
    plt.imshow(Xtest1, cmap='gray')
    plt.show()

    ipN = similarty(X,Xtest1)

    if ipN>Th:
        print('ipN = ', ipN , 'access premitted')
    else:
        print('ipN = ', ipN , 'access denided')
    testCnt += 1
    time.sleep(0.01)
print('test reached succes after: ',testCnt,'times')