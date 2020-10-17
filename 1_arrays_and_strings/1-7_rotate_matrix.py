"""
1.7 Rotate Matrix
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
"""

"""
Technique used: Implement matrix rotation in layers, e.g. for 4x4 matrix:
temp = matrix[0][0]
matrix[0][0] = matrix[3][0]
matrix[3][0] = matrix[3][3]
matrix[3][3] = matrix[0][3]
matrix[0][3] = temp

followed by:
temp = matrix[0][1]
matrix[0][1] = matrix[2][0]
matrix[2][0] = matrix[3][2]
matrix[3][2] = matrix[1][3]
matrix[1][3] = temp

and so on, layer by layer closer to the center of the matrix.
"""


import numpy as np

matrix_a = np.array([[1,2,3], [4,5,6], [7,8,9]])
matrix_b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])

def brute_force(matrix_in):
    """
    Time complexity wise, we can't do better than O(n^2), as we need to see each element of the matrix.
    Space complexity wise, this is not good as we need to create another matrix, which is O(n^2)
    """
    N = len(matrix_in)
    matrix_out = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            matrix_out[i][j] = matrix_in[j][N-i-1]

    return matrix_out

def optimized(matrix):
    """
    Good space complexity as we modify the matrix in-place.
    """
    N = len(matrix)
    for layer in range(int(N/2)):
        first = layer
        last = N-layer-1
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last-i+first][first]
            matrix[last-i+first][first] = matrix[last][last-i+first]
            matrix[last][last-i+first] = matrix[i][last]
            matrix[i][last] = top

    return matrix

if __name__=="__main__":
    print(optimized(matrix_a))
    print(optimized(matrix_b))


