import numpy as np
import matplotlib.pyplot as plt


def neighbors(A,i,j):
    size = len(A)
    sum_neighbors = sum([A[(i+1) % size , k % size] for k in range(j-1, j+2)])
    sum_neighbors += sum([A[(i-1) % size , k % size] for k in range(j-1, j+2)])
    sum_neighbors += A[i,(j-1) % size]
    sum_neighbors += A[i,(j+1) % size]
    return sum_neighbors


def mat_neigbors_update(A):
    return np.array([[neighbors(A,i,j) for j in range(len(A[0]))] for i in range(len(A))])


def evolution(A,B):
    for i in range(len(A)):
        for j in range(len(A)):
            if B[i,j] == 3 : A[i,j] = 1
            elif B[i,j] > 3 or B[i,j] < 2: A[i,j] = 0
    return A


def game_of_life(min = 0 , max = 8 , dens_0 = 20):
    size = 100
    Live_mat = np.zeros((size,size))

    Live_mat[1 , 1] = 1
    Live_mat[2 , 0] = 1
    Live_mat[3 , 0:3] = 1

    Neighbors_mat = mat_neigbors_update(Live_mat)
    dens = dens_0
    while(dens > 0 ):

        plt.imshow(Live_mat , cmap='hot')
        plt.pause(0.1)

        Live_mat = evolution(Live_mat,Neighbors_mat)
        Neighbors_mat = mat_neigbors_update(Live_mat)
    plt.show()




game_of_life()