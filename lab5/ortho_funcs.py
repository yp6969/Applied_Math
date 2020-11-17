import numpy as np

def find_independent(A):
    # for i in range(m):
    #     A[i:] /= A[i,i]
    #     A[i+1:] -= A[i+1,0]*A[i:]
    #     A[i+2:] -= A[i+2,0]*A[i:]
    redused, idx = gause_jorden(A)
    return mat[idx]

def gause_jorden(mat : np.ndarray, level=0):
    clone = mat.copy()
    m,n = clone.shape
    if m == 0 or n == 0: return clone,[]
    k = None
    for i in range(m):
        if clone[i,0] != 0:
            temp = clone[i]
            clone[i] = clone[0]
            clone[0] = temp
            k = i + level
            break

    if clone[0,0] == 0:
        clone[:,1:], idx = gause_jorden(clone[ :, 1:], level)
        if k is not None:
            idx.append(k)
        return clone, idx
    clone[0] = clone[0] / clone[0,0]

    for i in range(1,m):
        clone[i] = clone[i] - clone[i,0]*clone[0]
    clone[1:, 1:], idx = gause_jorden(clone[1:,1:] , level+1)
    if k is not None:
        idx.append(k)
    return clone , idx

if __name__ == '__main__':
    mat = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    print(find_independent(mat))


# def gram_shmidt():