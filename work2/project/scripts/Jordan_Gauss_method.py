import numpy as np
import copy


def method_Jordan_Gauss(self):
    shape = self.shape
    matrix_E = np.eye(shape[0], shape[1])


    if shape[1] > 1:

        #ищем строку с первый элементом = 1
        if self[0][0] != 1 and self[0][0] != 0:
            for i in range(shape[0]):
                if self[i][0] == 1 or self[i][0] == -1:
                    auxiliary_matrix = copy.copy(self)
                    auxiliary_matrix_e = copy.copy(matrix_E)
                    for k in range(shape[1]):
                        self[0][k] = auxiliary_matrix[i][k]
                        matrix_E[0][k] = auxiliary_matrix_e[i][k]
                        self[i][k] = auxiliary_matrix[0][k]
                        matrix_E[i][k] = auxiliary_matrix_e[0][k]
                    print('Нахождение строки с 1 на первом месте')
                    print(self)
                    print(matrix_E)

    #прямой ход
    # for s in range(shape[0]):
    #     for r in range(shape[1]):


    else:
        print('Операция невозможна')


# проверка первой элемента первой строки на равенство 1
def cast_to_unit(self, matrix_E, num, count_column):
    if self[num][num] != 1:
        first_element = copy.copy(float(self[num][num]))
        for m in range(count_column):
            result = self[num][m] / first_element
            self[num][m] = result
            if matrix_E[num][m] != 0:
                matrix_E[num][m] = matrix_E[num][m] / first_element
    return self, matrix_E

    # проверка  элемента на отрицательность
def cast_to_positive(self, matrix_E, num, count_row, count_column):
    if self[num][num] < 0:
        for l in range(count_column):
            self[num][l] = self[num][l] * (-1)
            if matrix_E[num][l] != 0:
                matrix_E[num][l] = matrix_E[num][l] * (-1)
    return self, matrix_E


# преобразуем массив с целыми числами в тип float
def cast_to_float_matrix(self, count_row, count_column):
    matrix = np.eye(count_row, count_column)
    for p in range(count_row):
        for h in range(count_column):
            res = float(self[p][h])
            matrix[p][h] = res
        self = matrix
    return self,matrix




matrix1 = np.array([[6, 2, 3], [-5, -5, -6], [3, 5, 4]])
print('Первоначальная матрица')
print(matrix1)
method_Jordan_Gauss(matrix1)
