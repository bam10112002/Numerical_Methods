import numpy as np
def norma(matrix):
    max = -1
    for i in range(len(matrix)):
        sum1 = 0
        sum2 = 0
        for j in range(len(matrix)):
            sum1 += matrix[i][j]
            sum2 += matrix[j][i]
        if sum1 > max:
            max = sum1
        if sum2 > max:
            max = sum2
    return max

def normaVec(vec):
    max = -1
    for num in vec:
        if num > max:
            max = num
    return max


Nc = 2
Ng = 10
A = np.array([[Nc+10 , Ng    , 1    ],
              [Ng    , 10+Nc , 3    ],
              [1     , 3     , Ng+4 ]])

C = np.array([[Ng   ],
              [Nc+10],
              [0    ]])

A = np.array([[20,+4,-8],[-3,15,5],[6,3,-18]])
C = [1,-2,3]

def compare(curr, prev):
    eps = 1e-4
    for i in range(len(curr)):
        if abs(curr[i] - prev[i]) > eps:
            return True
        return False


# проверка главной диагонали на нули
for i in range(len(A)):
    if (A[i][i] == 0):
        print("error a[i][i] musnt be 0")

# Выразим неизвесные
alpha_matrix = np.zeros((len(A), len(A)))
beta_matrix = np.zeros((len(A), 1))
for i in range(len(A)):
    for j in range(len(A)):
        if i != j:
            alpha_matrix[i][j] = -A[i][j] / A[i][i]

    for i in range(len(A)):
        beta_matrix[i] = C[i] / A[i][i]


# Проверка на норму
if norma(alpha_matrix) >= 1:
    print("error norma mast be < 1")


print("\n\nМетод простой итерации:")
# https://www.youtube.com/watch?v=4s9GxRY_DNM
eps = True
iter = 1
x_matrix = np.copy(beta_matrix)
while(eps):
    x_p = np.copy(x_matrix)
    x_matrix = beta_matrix + np.dot(alpha_matrix, x_p)
    e = (np.linalg.norm(alpha_matrix, np.inf)**iter/(1-np.linalg.norm(alpha_matrix, np.inf))) * \
            np.linalg.norm(beta_matrix, np.inf)
    if np.linalg.norm(alpha_matrix) >= 1:
        e = (np.linalg.norm(alpha_matrix, np.inf)**iter/(1-np.linalg.norm(alpha_matrix, np.inf))) * np.linalg.norm(x_matrix - x_p)
    if e < 1e-5:
        break

    print("iter: ", iter, " x = ", x_matrix.transpose()[0], "e = ", e)
    iter += 1
print("Решение методом простой итерации")
print(x_matrix.transpose()[0])



print("\n\nМетод Зейндаля:");
eps = True
iter = 1
x_matrix = np.copy(beta_matrix)
while(eps):
    x_prev = np.copy(x_matrix)
    x_matrix[0] = alpha_matrix[0][0]*x_matrix[0] + alpha_matrix[0][1]*x_matrix[1] + alpha_matrix[0][2]*x_matrix[2] + beta_matrix[0]
    x_matrix[1] = alpha_matrix[1][0]*x_matrix[0] + alpha_matrix[1][1]*x_matrix[1] + alpha_matrix[1][2]*x_matrix[2] + beta_matrix[1]
    x_matrix[2] = alpha_matrix[2][0]*x_matrix[0] + alpha_matrix[2][1]*x_matrix[1] + alpha_matrix[2][2]*x_matrix[2] + beta_matrix[2]
    eps = compare(x_matrix, x_prev)
    print("iter: ", iter, " ", x_matrix.transpose()[0])
    iter += 1

print("Решение методом Зейндала")
print(x_matrix.transpose()[0])