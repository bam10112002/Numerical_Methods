import numpy as np
i = 0
def a(i):
    return i * 2 + 10
def b(i):
    return 2 * i**2 + 10
def c(i):
    return 10 - 2*i
def d(i):
    return 2 + 10 * i

A = [[b(1), c(1),    0,    0,    0],
     [a(2), b(2), c(2),    0,    0],
     [0,    a(3), b(3), c(3),    0],
     [0,     0,   a(4), b(4), c(4)],
     [0,     0,     0,  a(5), b(5)]]

A2 = [[b(1), c(1),   0,     0,    0,     0,       0,       0,       0,      0],
      [a(2), b(2), c(2),    0,    0,     0,       0,       0,       0,      0],
      [0,    a(3), b(3), c(3),    0,     0,       0,       0,       0,      0],
      [0,       0, a(4), b(4), c(4),     0,       0,       0,       0,      0],
      [0,       0,    0, a(5), b(5),  c(5),       0,       0,       0,      0],
      [0,       0,    0,    0, a(6),  b(6),    c(6),       0,       0,      0],
      [0,       0,    0,    0,    0,  a(7),    b(7),    c(7),       0,      0],
      [0,       0,    0,    0,    0,     0,    a(8),    b(8),    c(8),      0],
      [0,       0,    0,    0,    0,     0,       0,    a(9),    b(9),   c(9)],
      [0,       0,    0,    0,    0,     0,       0,       0,    a(10),  b(10)]]
#
# def generate(size):
#     matrix = np.array(np.array(5))
#     # for i in range(size):
#     #     matrix.append([0]*size)
#     # # matrix = [[0] * size] * size
#     matrix[0][0] = b(1)
#     matrix[0][1] = c(1)
#     for i in range(1, size-1):
#         matrix[i][i-1] = a(i+1)
#         matrix[i][i]   = b(i+1)
#         matrix[i][i+1] = c(i+1)
#     matrix[size-1][size-2] = a(size)
#     matrix[size-1][size-1] = b(size)
#     return matrix

y = [b(1)]
alpha = [-c(1)/y[-1]]
betta = [ d(1)/y[-1]]

for i in range(2, len(A)):
    y.append(b(i) + a(i)*alpha[-1])
    alpha.append(-c(i)/y[-1])
    betta.append((d(i)- a(i)*betta[-1])/y[-1])

y.append(b(len(A)) + a(len(A)) * alpha[-1])
betta.append((d(len(A)) - a(len(A))*betta[-1])/y[-1])

print("A = {}".format(np.array(A)))
print("alpha:", alpha)
print("betta:", betta)

x = [betta[-1]]
for i in range(len(A)-1, 0, -1):
    x.append(alpha[i-1] * x[-1] + betta[i-1])
print("x= ", x)

def myPrint(matrix):
    for row in matrix:
        print(row)

# print(generate(5))