"""
1.8 Zero Matrix
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""

"""
Technique used: Here, we're taking advantage of Python's ability to take 
slices of arrays to easily change the whole row/column.
"""
import numpy as np

matrix_a = np.array([[1,2,3], [4,5,0], [7,8,9],[0,11,12]])

def optimized(matrix):
    M = len(matrix)
    N = len(matrix[0])
    # scan first to see where are the zeros
    idx_zeros = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==0:
                idx_zeros.append([i, j])

    for i in range(M):
        for j in range(N):
            if [i,j] in idx_zeros:
                print(i,j)
                matrix[:, j]=0
                matrix[i, :]=0
    return matrix


if __name__=="__main__":
    print(matrix_a)
    print(optimized(matrix_a))
