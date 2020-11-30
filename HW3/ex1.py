import numpy as np
from numpy import linalg as lin

# gram shmidet algorithem
def gram_shmidet(A):
    n = len(A)
    R = np.zeros((n,n))
    Q = np.zeros((n,n))
    for j in range(n):
        v = A[:,j]
        for i in range(j-1):
            R[i,j] = np.inner(Q[:,i] , v)
            v = v - R[i,j] * Q[:,i]
        R[j,j] = lin.norm(v)
        Q[:,j] = v/R[j,j]
    return Q

A = np.array([[1,0,0],
              [0,1,0],
              [1,1,1]])
a = gram_shmidet(A)
print(a)
print(np.inner(a[:,1] , a[:,2]))