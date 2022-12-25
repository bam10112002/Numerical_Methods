import numpy as np

A = np.array([[2, 5, 2],[5, 2, -10],[2, -10, 2]], dtype=float)
B = np.array([[1],[2],[-10]], dtype=float)

A = np.array([[2,5,1], [-1,2,-2], [6,2,1]], dtype=float)
B = np.array([[1],[2],[3]], dtype=float)

def det(a):
    res = 1
    n = len(a)
    for i in range(n):
        # выбираем опорный элемент
        j = max(range(i,n), key=lambda k: abs(a[k][i]))
        if i != j:
            a[i],a[j] = a[j],a[i]
            res *= -1
        # убеждаемся, что матрица не вырожденная
        if a[i][i] == 0:
            return 0
        # det - произведение элементов главной диагонали верхне треугольной матрицы
        res *= a[i][i]

        # обнуляем элементы в текущем столбце
        for j in range(i+1,n):
            b = a[j][i] / a[i][i]
            a[j] = [a[j][k]-b*a[i][k] for k in range(n)]
    return res

def one(a):
    n = len(a)
    for i in range(n):
        # выбираем опорный элемент
        j = max(range(i,n), key=lambda k: abs(a[k][i]))
        if i != j:
            a[i],a[j] = a[j],a[i]
        # обнуляем элементы в текущем столбце
        for j in range(i+1,n):
            b = a[j][i] / a[i][i]
            a[j] = [a[j][k]-b*a[i][k] for k in range(n)]

def minus(A,k,i1,i2):
    for i in range(len(A)):
        A[i1][i] -= k*A[i2][i]

def gaus(A, b):
    det = 1
    # Прямой ход
    for i in range(len(A)):
        # делаем опорный элемент равным 1
        op = A[i][i]
        det *= op
        for k in range(i, len(A)):
            A[i][k] = A[i][k]/op
        b[i][0] /= op

        # зануляем столбец
        for k in range(i+1, len(A)):
            op = A[k][i]/A[i][i]
            for m in range(len(A)):
                A[k][m] -= op * A[i][m]
            b[k][0] -= op*b[i][0]
        print(A)

    x = []
    for i in range(len(A), 0, -1):
        tmp_x = b[i-1][0]
        for j in range(i, len(A)):
            tmp_x -= A[i-1][j] * x[j-i-1]
        x.append(tmp_x)
    x.reverse()
    return x, det

A1 = np.array([[2,3,6], [3,6,2], [6,2,8]], dtype=float)
def inverse (A):
    E = np.eye(len(A), len(A))
    for i in range(len(A)):
        # делаем опорный элемент равным 1
        op = A[i][i]

        for k in range(len(A)):
            A[i][k] = A[i][k]/op
            E[i][k] = E[i][k]/op

        # зануляем столбец
        for k in range(i+1, len(A)):
            op = A[k][i]/A[i][i]
            for m in range(len(A)):
                A[k][m] -= op * A[i][m]
                E[k][m] -= op * E[i][m]
        print("Iter ", i)
        print(A)
        print(E)
    print("Обратный ход")
    for i in range(len(A)-1,0,-1):
        # зануляем столбец
        for k in range(i-1,-1,-1):
            op = A[k][i] / A[i][i]
            for m in range(len(A)):
                A[k][m] -= op * A[i][m]
                E[k][m] -= op * E[i][m]
        print("Iter ", 3-i)
        print(A)
        print(E)
    return E

print("Вычисление неизвестных и определителя методом Гауса")
x,det = gaus(A,B)
print("\n\nОбратная\nПрямой ход")
print("Полученная обратная матрица\n", inverse(A1))
print("x = ", x)
print("det = ", det)
