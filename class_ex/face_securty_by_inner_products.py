import numpy as np
import matplotlib.pyplot as plt
import time

X = np.zeros([8,8])
X[ 1, 1:3 ] = 1
X[ 1, 5:7 ] = 1
X[ 3, 3:5 ] = 1
X[ 5:7, 1::5 ] = 1
X[6,2:6] = 1

plt.imshow(X, cmap='gray')


ipN = 0
L = 8
Th = 0.8 # threshold

Xtest = np.zeros([L,L])
while ipN<Th:
    Xtest[1:L-1,1:L-1] = (np.random.rand(L-2,L-2)) > 0.6
    Xtest1 = Xtest.astype(float)


    # plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(Xtest1, cmap='gray')
    plt.title('test face')

    plt.subplot(1, 2, 2)
    plt.imshow(X, cmap='gray')
    plt.title('template')
    plt.show()


    ip = sum(sum(X*Xtest1))
    print('ip = ', ip)

    N = sum(sum(X))
    Ntest = sum(sum(Xtest1))
    if Ntest >= 1.8*N:
        print('Ntest= ' , Ntest,'access denided, call security')
        break
    ipN = ip/N
    if ipN>Th:
        print('ipN = ', ipN , 'access premitted')
    else:
        print('ipN = ', ipN , 'access denided')
    print('um Xtest1 = ', sum(sum(Xtest1)))

    time.sleep(0.01)
