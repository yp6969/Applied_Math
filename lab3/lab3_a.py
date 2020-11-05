import numpy as np

w1 = np.array([3,4,28,7,11])
w2 = np.array([1,4,6,8,2])

length = lambda u,v : np.sqrt(sum((u-v)**2))

print(length(w1,w2))

print(np.linalg.norm(w1-w2))
