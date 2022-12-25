import numpy as np
import math
from numpy import linalg

def MyMax(matrix):
    max = matrix[1][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and math.fabs(matrix[i][j]) > max and matrix[i][j] != 0:
                max = math.fabs(matrix[i][j])
    return max

A = np.array([[17, 1, 1], [1, 17, 2], [1, 2, 4]])
A_copy = np.copy(A)
a_list = [A_copy]

V = np.eye(len(A_copy), dtype=float)
iter = 0
prevErr = 10000
while MyMax(a_list[-1]) > 1e-3:
    max = -1
    k = -1
    m = -1
    for i in range(len(a_list[-1])):
        for j in range(0, i):
            if a_list[-1][i][j] > max:
                max = a_list[-1][i][j]
                m = i
                k = j
    phi = math.atan(2 * a_list[-1][k][m] / (a_list[-1][k][k] - a_list[-1][m][m])) / 2

    H = np.eye(len(a_list[-1]), len(A))
    H[k][k] = H[m][m] = math.cos(phi)
    H[m][k] = math.sin(phi)
    H[k][m] = -math.sin(phi)
    V = np.matmul(V, H)
    a_list.append(np.copy((linalg.inv(H).dot(a_list[-1])).dot(H)))
    iter += 1
    # if (prevErr - MyMax(a_list[-1]) == 0):
    #     break
    print(iter)
    prevErr = MyMax(a_list[-1])

lam = []
vec = []
for i in range(len(a_list[-1])):
    lam.append(a_list[-1][i][i])
    vec.append(np.array([V[0][i], V[1][i], V[2][i]]))
    print("собственное число:", lam[-1])
    print("Собственный вектор:", vec[-1])
    print("Проверка:", A.dot(vec[-1]) - vec[-1] * lam[-1])
    print()

print("Максимальная ошибка вычислений: ", MyMax(a_list[-1]))