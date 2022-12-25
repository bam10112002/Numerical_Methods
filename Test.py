n = int(input('Enter number of unknowns: '))
a = [[13, 5, 2], [5, 13, -10], [2, -10, 13]]
a_1 = [[13, 5, 2], [5, 13, -10], [2, -10, 13]]
a_2 = [[13, 5, 2], [5, 13, -10], [2, -10, 13]]
b = [1, 13, -10]
e = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# inverse a_1
indices = list(range(n))
for fd in range(n):
    fd_sc = 1.0 / a_1[fd][fd]
    for j in range(n):
        a_1[fd][j] *= fd_sc
        e[fd][j] *= fd_sc
    for i in indices[0:fd] + indices[fd + 1:]:
        # *** skip row with fd in it.
        cr_sc = a_1[i][fd]  # cr stands for "current row".
        for j in range(n):
            # cr - crScaler * fdRow, but one element at a time.
            a_1[i][j] = a_1[i][j] - cr_sc * a_1[fd][j]
            e[i][j] = e[i][j] - cr_sc * e[fd][j]

print('Inversed matrix: ')
for i in range(3):
    for j in range(3):
        print(e[i][j], end=' ')
    print()

#

# determinant
for fd in range(n):
    for i in range(fd+1, n):
        if a_2[fd][fd] == 0:
            a_2[fd][fd] = 1.0e-18
        cr_cs = a[i][fd] / a_2[fd][fd]
        for j in range(n):
            a_2[i][j] = a_2[i][j] - cr_cs * a_2[fd][j]

det = 1.0
for i in range(n):
    det *= a_2[i][i]

print('Determinant of the matrix equals ', det)
#

# equations
fd_cd = 0
aug_a = [[13, 5, 2, 1], [5, 13, -10, 13], [2, -10, 13, -10]]
a_3 = [[13, 5, 2], [5, 13, -10], [2, -10, 13]]
b = [1, 13, -10]

for fd in range(n):
    fd_sc = 1.0 / a_3[fd][fd]
    for j in range(n):
        a_3[fd][j] *= fd_sc
    b[fd] *= fd_sc

    for i in indices[0:fd] + indices[fd+1:]:
        cr_cs = a_3[i][fd]
        for j in range(n):
            a_3[i][j] = a_3[i][j] - cr_sc * a_3[fd][j]
        b[i] = b[i] - cr_sc * b[fd]

print('X root:')
for i in range(n):
    print(b[i])