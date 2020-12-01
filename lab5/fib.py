import  numpy as np

def fib(n,counter=1):
    A = np.array([[1,1], [1,0]])
    if round(np.log2(n-1)) == counter: return np.dot(A,A)
    B = fib(n, counter+1)
    if counter == 1: return np.dot(B, np.array([[1], [0]]))
    B = np.dot(B,B)
    return B


print(fib(16))
