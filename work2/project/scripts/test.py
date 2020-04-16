import numpy as np
import copy

matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix1)
matrix2 = np.array([[.0, .0, .0], [.0, .0, .0]])

for i in range(0, 2):
    for j in range(0, 3):
        res = float(matrix1[i][j])
        matrix2[i][j] = res

print(matrix2)