import numpy as np
import scipy as sp
import math as mt
import matplotlib.pyplot as plt

Ng = 2
Nc = 10
a = Ng + Nc

x_list = [-2.5 * a, -1.5 * a, -0.5 * a, 0.5 * a, 1.5 * a]
y_list = [84 - Ng, 73 - Ng * 2, 63 - Ng * 3, 55 - Ng * 4, 47 - Ng * 5]

x_list = [-2, -1, 0, 1, 2]
y_list = [3, 4, 2, 1, 1]

x4 = 0
x3 = 0
x2 = 0
x1 = 0
x2_y1 = 0
x1_y1 = 0
y1 = 0

for i in range(len(x_list)):
    x4 += mt.pow(x_list[i], 4)
    x3 += mt.pow(x_list[i], 3)
    x2 += mt.pow(x_list[i], 2)
    x1 += x_list[i]
    x2_y1 += mt.pow(x_list[i], 2) * y_list[i]
    x1_y1 += x_list[i] * y_list[i]
    y1 += y_list[i]

# Решение СЛАУ апрксимирующего многочлена второй степени
A = np.array([[x4, x3, x2],
              [x3, x2, x1],
              [x2, x1, len(x_list)]])
B = np.array([x2_y1, x1_y1, y1])
x = sp.linalg.solve(A, B.T)

print("P(x) =", round(x[0], 4), "* x^2 +", round(x[1], 4), "* x +", round(x[2], 4))
def P2(a, b, c, x):
    return a * x ** 2 + b * x + c

# Вывод графика
x_sp = np.linspace(-2, 2, 100)
y_sp = (x[0] * x_sp ** 2 + x[1] * x_sp + x[2])
fig, ax = plt.subplots()
for i in range(len(x_list)):
    plt.scatter(x_list[i], y_list[i])
ax.plot(x_sp, y_sp)

# Высчитываем квадратическую невязка
discrepancy = 0
for i in range(len(y_list)):
    discrepancy += (P2(x[0], x[1], x[2], x_list[i]) - y_list[i]) ** 2

print("Discrepancy = ", round(discrepancy, 4))

# Решение СЛАУ апрксимирующего многочлена первой степени
A = np.array([[x2, x1],
              [x1, len(x_list)]])
B = np.array([x1_y1, y1])
x2 = sp.linalg.solve(A, B.T)
print("P1(x) =", round(x2[0], 4), "* x +", round(x2[1], 4))

fig2, ax2 = plt.subplots()
x_sp = np.linspace(-2, 2, 100)
y_sp = (x2[0] * x_sp + x2[1])
ax2.plot(x_sp, y_sp)
for i in range(len(x_list)):
    plt.scatter(x_list[i], y_list[i])
plt.show()
def P1(a, b, x):
    return a * x + b


for i in range(len(y_list)):
    discrepancy += (P1(x2[0], x2[1], x_list[i]) - y_list[i]) ** 2
print("Discrepancy = ", round(discrepancy, 4))
