import numpy as np
import copy


def method_Jordan_Gauss(self):
    shape = self.shape
    matrix_E = np.eye(shape[0], shape[1])

    if shape[1] > 1:

        # ищем строку с первый элементом = 1
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

        self = cast_to_float_matrix(self, shape[0], shape[1])
        result_cast_to_unit = cast_to_unit(self, matrix_E, 0, shape[1])
        self = result_cast_to_unit[0]
        matrix_E = result_cast_to_unit[1]
        result_cast_to_positive = cast_to_positive(self, matrix_E, 0, shape[1])
        self = result_cast_to_positive[0]
        matrix_E = result_cast_to_positive[1]

        # прямой ход
        for line in range(1, shape[0]):
            for num_row in range(line, shape[0]):
                if self[num_row][line - 1] != 0:
                    divisor = (-1) / copy.copy(self[num_row][line - 1])
                    print('divisor =', divisor)
                    num_str = line - 1
                    for num_column in range(shape[1]):
                        if divisor != 0 and self[num_row][num_column] != 0:
                            self[num_row][num_column] = self[num_row][num_column] * divisor + self[num_str][num_column]
                            print('self[',num_row,'][',num_column,'] = self[',num_row, '][', num_column, ']{',self[num_row][num_column],'} * ', divisor , ' + self[' , num_str, '][' , num_column, ']{',self[num_str][num_column],'}')
                            print(self[num_row][num_column])
                            print(self)
                            matrix_E[num_row][num_column] = matrix_E[num_row][num_column] * divisor + matrix_E[num_str][
                                num_column]
                            print('matrix_E[',num_row,'][',num_column,'] = matrix_E[',num_row,'][',num_column,']{',matrix_E[num_row][num_column],'} * ' ,divisor, ' + matrix_E[',num_str,']['
                                , num_column, ']{',matrix_E[num_str][num_column],'}')
                            print(matrix_E[num_row][num_column])
                            print(matrix_E)
            result_cast_to_unit = cast_to_unit(self, matrix_E, line, shape[1])
            self = result_cast_to_unit[0]
            print(self)
            matrix_E = result_cast_to_unit[1]
            print(matrix_E)
            result_cast_to_positive = cast_to_positive(self, matrix_E, line, shape[1])
            self = result_cast_to_positive[0]
            matrix_E = result_cast_to_positive[1]

        print(self)
        return matrix_E

    #обратный ход
    # for line in range(range[0]-1, 0):


    else:
        print('Операция невозможна')


# проверка первой элемента первой строки на равенство 1
def cast_to_unit(self, matrix_E, num, count_column):
    first_elem = copy.copy(self[num][num])
    if (first_elem != 1.0).all():
        first_element = copy.copy(self[num][num])
        for m in range(count_column):
            if self[num][m] != 0:
                result = self[num][m] / first_element
                self[num][m] = result
            if matrix_E[num][m] != 0:
                result_e = matrix_E[num][m] / first_element
                matrix_E[num][m] = result_e
        return self, matrix_E
    else:
        return self, matrix_E

    # проверка  элемента на отрицательность


def cast_to_positive(self, matrix_E, num, count_column):
    if self[num][num] < 0.0:
        for l in range(count_column):
            self[num][l] = self[num][l] * (-1)
            if matrix_E[num][l] != 0:
                matrix_E[num][l] = matrix_E[num][l] * (-1)
        return self, matrix_E
    else:
        return self, matrix_E


# преобразуем массив с целыми числами в тип float
def cast_to_float_matrix(self, count_row, count_column):
    matrix = np.eye(count_row, count_column)
    for p in range(count_row):
        for h in range(count_column):
            res = float(self[p][h])
            matrix[p][h] = res
    self = matrix
    return self


matrix1 = np.array([[2, 1, -1], [3, 2, -2], [1, -1, 2]])
print('Первоначальная матрица')
print(matrix1)
res = method_Jordan_Gauss(matrix1)
print(res)
