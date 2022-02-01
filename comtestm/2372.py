import numpy as np
h, w = list(map(int, input().split()))
matrix = []

for i in range(h):
    matrix.append(list(map(int, input().split())))


matrix = np.array(matrix).T

for i in range(w):
    for j in range(h):
        print(matrix[i][j], end=' ')
    print()
