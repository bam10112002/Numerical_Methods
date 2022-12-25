import math
import numpy as np
import matplotlib.pyplot as plt

y0 = 0
def f(x,y):
    return -2*x*y+x*math.exp((x**2)*-1)
def fy(x):
    return (np.exp((x**2)*-1) * x**2 )/2

a = 0
b = 1
h = 0.1
x0 = a


# Метод Рунге Кутты
delta = 0
y = [y0]
x_sp = np.linspace(a, b, 100)
y_sp = fy(x_sp)
fig, ax = plt.subplots()
ax.plot(x_sp, y_sp)

for x in np.linspace(a, b, 11):
    k1 = f(x, y[-1])
    k2 = f(x + h/2, y[-1] + h/2*k1)
    k3 = f(x + h/2, y[-1] + h/2*k2)
    k4 = f(x + h  , y[-1] + h*k3)
    y.append(y[-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4))
    delta = max(delta, math.fabs(y[-1]-fy(x)))
    print("x = {}, y = {}, delta = {}".format(x, y[-1], math.fabs(y[-1]-fy(x))))
    plt.scatter(x, y[-1])

print("Максимальная ошибка вычислений", delta)
plt.show()


# Эйлера
delta = 0
y2 = [y0]
for x in np.linspace(a, b, 11):
    y2.append(y2[-1]+h*f(x,y2[-1]))
    print("x = {}, y = {}, delta = {}".format(x, y2[-1], math.fabs(y2[-1] - fy(x))))
    delta = max(delta, math.fabs(y2[-1] - fy(x)))
print("Максимальная ошибка вычислений", delta)


# Эйлера-Коши
delta = 0
y3 = [y0]
for x in np.linspace(a, b, 11):
    # (y[-1] * h * f(x, y2[-1]))
    y3.append(y3[-1] + h/2*(
            f(x,y3[-1]) +
            f(x+h,(y3[-1] + h * f(x, y3[-1])))
            ))
    print("x = {}, y = {}, delta = {}".format(x, y3[-1], math.fabs(y3[-1] - fy(x))))
    delta = max(delta, math.fabs(y3[-1] - fy(x)))
print("Максимальная ошибка вычислений", delta)