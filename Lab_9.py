import math
import numpy as np
import matplotlib.pyplot as plt
N = 4
Nc = 2
Ng = 10
a = Nc
b = Nc + N
def F(x):
    return Ng*x + np.sin(x)

x_list = np.linspace(a, b, N)
y_list = []
for x in x_list:
    y_list.append(F(x))


# x_list = np.linspace(-4, 4, 9)
# y_list = []
# def F(x):
#     return x*np.sin(x)
# for x in x_list:
#     y_list.append(F(x))

h = x_list[1] - x_list[0]
print("X = ", x_list)
print("Y = ", y_list)

P = [0]
Q = [0]

for i in range(2,len(x_list)):
    Y = (y_list[i] - y_list[i-1])/h - (y_list[i-1] - y_list[i-2])/h
    Q.append((6 * Y - Q[-1] * h)/(4*h+P[-1]*h))
    P.append(-h/(4*h+P[-1]*h))

print("P = ", P)
print("Q = ", Q)

m = [0]
for i in range(len(x_list) - 1):
    m.append(P[-i] * m[-1] + Q[-i])
m.append(0)
m.pop(0)
print("m = ", m)

def S(i, x):
    return  m[i] * ((x - x_list[i-1]) ** 3) / (6*h) + \
            m[i-1] * ((x_list[i] - x) ** 3) / (6*h) + \
            (y_list[i] - m[i]*h**2/6) * (x - x_list[i-1])/h + \
            (y_list[i-1] - m[i-1]*h**2/6) * (x_list[i] - x)/h


fig, ax = plt.subplots()

for i in range(len(x_list)):
    plt.scatter(x_list[i], y_list[i])

for i in range(1, len(x_list)):
    x_sp = np.linspace(x_list[i-1], x_list[i], 100)
    y_sp = S(i, np.linspace(x_list[i-1], x_list[i], 100))
    ax.plot(x_sp, y_sp)

x_func = np.linspace(x_list[0], x_list[-1], 1000)
y_func = F(x_func)
ax.plot(x_func, y_func)

plt.show()

delta = 0
for i in range(1, len(x_list)):
    x_l = np.linspace(x_list[i-1], x_list[i], 100)
    y_l = S(i, np.linspace(x_list[i-1], x_list[i], 100))
    y_lf = F(x_l)
    for yl, yf in zip(y_l, y_lf):
        delta = max(delta, math.fabs(yl-yf))
print("delta = ", delta)

