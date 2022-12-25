import math
import math as mp
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def fx(x):
    return (x ** 3) / 10 + x / 2 + 2 * 10


def fxx(x):
    return (3 * (x ** 2)) / 10 + 1 / 2

def fxxx(x):
    return 3*x/5


i = 0
x_p = (int)(input("Введите начальную точку: "))
while fx(x_p) * fxxx(x_p) < 0:
    print("error in f(x) * fxx(x) < 0")
    x_p = (int)(input("Введите начальную точку: "))

while True:
    i += 1
    x = x_p - fx(x_p) / fxx(x_p)
    if math.fabs(x_p - x) < 1e-4:
        break
    x_p = x


print("Решение полученное методом ньютона:", x)
print("Итераций - ", i)

# Метод простых итераций
def g(x):
    return -mp.pow(5 * x + 200, 1 / 3)


def gx(x):
    return (10 * x) / 3 / mp.pow(mp.pow(5 * x + 200, 2), 1 / 3)


a = -4
b = -7
q = -10000
x0 = 0
for x in np.linspace(a, b, 1000):
    if q > gx(x):
        x0 = x
        q = max(gx(x), q)

x = [x0, g(x0)]
if gx(x0) >= 1 and gx(x0) * math.fabs(x[-1] - x[-2])/(1-gx(x0)) >= 1:
    print("errr gx(x) > 1")

while True:
    x.append(g(x[-1]))
    if math.fabs(2*x[-2] - x[-1] - x[-3]) == 0:
        break
    if (x[-1] - x[-2])**2 / math.fabs(2*x[-2] - x[-1] - x[-3]) < 1e-4 \
            and math.fabs(fx(x[-1])) < 1e-4 \
            and q * math.fabs(x[-1] - x[-2])/(1-q) < 1e-4:
        break

print("Решение полученне методом простых итераций", x[-1])
print("Итераций - ", len(x))

x_sp = np.linspace(-10, 10, 100)
y_sp = fx(x_sp)
fig, ax = plt.subplots()
ax.plot(x_sp, y_sp)
plt.show()
