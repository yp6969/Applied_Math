import numpy as np

# def save():

mat = np.random.randint(1, 100, size=(10, 10)) * 1j
np.savetxt('random_bin.npy' , mat)

loaded = np.load('random_bin.npy')

def txt():
    mat = np.random.randint(1,100 , size=(10,10)) * 1j
    print(mat)
    np.savetxt('random_mat.txt' , mat , '%02d')
    old_mat = np.loadtxt('random_mat.txt' , np.complex)


if __name__ == '__main__':
    txt();