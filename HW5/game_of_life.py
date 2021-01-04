import numpy as np
import matplotlib.pyplot as plt

def mat_neigbors_update(A):
    up = A[-1: , :]
    up = np.append(up , A[:-1,:] , axis=0)

    down = A[1:,:]
    down = np.append(down , A[:1,:] , axis=0)

    right = A[:,-1:]
    right = np.append(right,  A[:, :-1] , axis=1)

    left = A[:,1:]
    left = np.append(left,  A[:, :1] , axis=1)

    u_left = up[:,1:]
    u_left = np.append(u_left, up[:, :1], axis=1)

    u_right = up[:, -1:]
    u_right = np.append(u_right, up[:, :-1], axis=1)

    d_left = down[:, 1:]
    d_left = np.append(d_left, down[:, :1], axis=1)

    d_right = down[:, -1:]
    d_right = np.append(d_right, down[:, :-1], axis=1)

    return (up + down + left + right + u_left + u_right + d_left + d_right)




def evolution(A,B, min , max):
    for i in range(len(A)):
        for j in range(len(A)):
            if B[i,j] == max : A[i,j] = 1
            elif B[i,j] > max or B[i,j] < min: A[i,j] = 0
    return A

def glider(A):
    A[1, 1] = 1
    A[2, 0] = 1
    A[3, 0:3] = 1

def Pulsar(A):

    X = np.zeros((17, 17))
    X[2, 4:7] = 1
    X[4:7, 7] = 1
    X += X.T
    X += X[:, ::-1]
    X += X[::-1, :]
    A[20:37 , 20:37] = X


def Unbounded (A):
    unbounded = [[1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1],
                 [0, 1, 1, 0, 1],
                 [1, 0, 1, 0, 1]]
    X = np.zeros((30, 40))
    X[15:20, 18:23] = unbounded
    A[100:130 , 100:140] = X


def game_of_life(min = 2 , max = 3 , dens_0 = 66):
    size = 256
    Live_mat = np.zeros((size,size))

# initiate
    Unbounded(Live_mat)
    glider(Live_mat)
    Pulsar(Live_mat)



    Neighbors_mat = mat_neigbors_update(Live_mat)
    dens = dens_0

    while(dens > 0 ):
        plt.clf()
        plt.imshow(Live_mat , cmap='hot')
        plt.colorbar()
        plt.show(block=False)
        plt.pause(0.01)
        Live_mat = evolution(Live_mat,Neighbors_mat , min, max)
        Neighbors_mat = mat_neigbors_update(Live_mat)
        dens = sum(sum(Live_mat))

    plt.show()



game_of_life()