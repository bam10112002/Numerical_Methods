# import numpy as np

A = [[2, 5, 2],[5, 2, -10],[2, -10, 2]]
B = [[1],[2],[-10]]

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


    print(a)

def myPrint(matrix):
    for row in matrix:
        print(row)

one(A)