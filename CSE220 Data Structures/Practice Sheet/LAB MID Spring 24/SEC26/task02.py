import numpy as np

def print_matrix(m):
    row, col = m.shape
    for i in range(row):
        c = 1
        print('|', end='')
        for j in range(col):
            c += 1
            if len(str(m[i][j])) == 1:
                print(' ', m[i][j], end='  |')
                c += 6
            else:
                print(' ', m[i][j], end=' |')
                c += 6
        print()
        print('-' * (c - col))

def add_matrices(matrix_1, matrix_2):
    row, col = matrix_1.shape
    result_matrix = np.zeros((row, col), dtype=int)

    for i in range(row):
        for j in range(col):
            result_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]

    return result_matrix

matrix_1 = np.array([[7, 4],
                    [5, 1],
                    [3, 3]])

matrix_2 = np.array([[5, 4],
                    [8, 2],
                    [1, 0]])

result_matrix = add_matrices(matrix_1, matrix_2)
print_matrix(result_matrix)

print("\n##########################\n")

matrix_1 = np.array([[3, 3, 2, 6]])

matrix_2 = np.array([[4, 5, 2, 3]])

result_matrix = add_matrices(matrix_1, matrix_2)
print_matrix(result_matrix)