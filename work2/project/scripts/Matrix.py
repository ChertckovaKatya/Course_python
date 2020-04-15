import numpy as np


class Matrix:
    def amount(first_matrix, second_matrix):
        if first_matrix.shape == second_matrix.shape:
            count_row = first_matrix.shape[0]
            count_columns = first_matrix.shape[1]
            final_matrix = np.zeros(count_row, count_columns)
            for i in range(count_row):
                for j in range(count_columns):
                    final_matrix[i][j] = first_matrix[i][j] + second_matrix[i][j]
            return final_matrix
        else:
            print('Матрицы разной размерности')

    def transpose(matrix):
        count_row = matrix.shape[0]
        count_columns = matrix.shape[1]
        final_matrix = np.zeros((count_columns, count_row))
        for i in range(count_columns):
            for j in range(count_row):
                final_matrix[i][j] = matrix[j][i]
        return final_matrix

    def multiplication(first_matrix, second_matrix):
        row_count_first_matrix = first_matrix.shape[0]
        columns_count_first_matrix = first_matrix.shape[1]
        row_count_second_matrix = second_matrix.shape[0]
        columns_count_second_matrix = second_matrix.shape[1]
        if columns_count_first_matrix == row_count_second_matrix:
            final_matrix = np.zeros((row_count_first_matrix, columns_count_second_matrix))
            for i in range(row_count_first_matrix):
                for j in range(columns_count_second_matrix):
                    for k in range(row_count_second_matrix):
                        final_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]

            return final_matrix
        else:
            print("Невозможно посчитать произведение матриц")


    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([[1, 2], [4, 5], [6, 7]])
    print(amount(matrix1, matrix2))
    print(multiplication(matrix1, matrix2))
    print(transpose(matrix2))
