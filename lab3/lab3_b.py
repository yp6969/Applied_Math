import numpy as np

mat = np.random.randint(1,100, size=(30, 30))

# print(mat[np.where(mat%17==0)])
mod_3 = mat[ mat % 3 == 0]
mod_5 = mat[ mat % 5 == 0]

print(list(set().union(mod_3,mod_5)))
print()
print(np.union1d(mod_3,mod_5))

