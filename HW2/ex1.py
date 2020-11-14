'''
yair pinhas
'''

import numpy as np
import random
from numpy import linalg as lin

def norm(v,p):
    if p == np.inf:
        return max(v)
    return sum((np.absolute(v))**p)**(1/p)



def main():
    #a:
    v = np.array([1,-2,3,1,5])
    p = random.randint(1,10)
    print('the',p ,'-th norm ||v|| =', norm(v,p), 'compare to the inf norm = ', norm(v,np.inf))
    #b:
    v2 = np.array([1,5,2,-2,-1,7])
    print('the unit vector Vi: ', v2/norm(v2,2))

    w1 = np.array([1,3,-2,-3,5])
    w2 = np.array([0,7,-15,2,7])
    print('the distans is:', norm(w1-w2,2))



if __name__ == '__main__':
    main()