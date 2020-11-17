
#
# A = [1,2,34,6,5,4]
# p = []
# type(A)
#
#
# cnt=0
#
# for i in range(len(A)+1):
#     if cnt == 0:
#         p.append(None)
#     else:
#         j=0
#         while( j+i < len(A)+1):
#             p.append()
#             j+=1
#     cnt+=1
# print(p)
def merge(A , B):
    i,j = 0
    M = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            M.append(A[i]) ; i+=1
        else: M.append(B[j]) ; j+=1
    for

def mergesort(A):
    if len(A) == 1: return
    mergesort(A[:len(A)/2])
    mergesort(A[len(A)/2+1:])
    merge()
    return

A = [5,3,7,2,8]
print(mergesort(A))