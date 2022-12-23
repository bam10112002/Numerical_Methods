import math
import numpy as np
import scipy as sp

def runge(z1, z2, dx1, dx2, r):
    return z1 + ((z1-z2)/((dx2/dx1)**r-1))
def F(x):
    return x/math.pow(3*x+4, 2)

x0 = -1
x1 = 1

# M1 = 2.5
# hd = (2 * 1e-4)/(x1-x0)/M1

res = 0
resr = 0
dx = 1e-2
splitting = round((x1 - x0)/dx)

for x in np.linspace(x0, x1, splitting):
    res += F(x) * dx
for x in np.linspace(x0, x1, splitting*2):
    resr += F(x) * dx/2

print("Результат методом прямоугольников:", res)
print("Погрешность по сравнению с модулем SciPy:", math.fabs(sp.integrate.quad(F, -1, 1)[0] - res))

print("Результат методом прямоугольников уточненный:", res)
print("Погрешность по сравнению с модулем SciPy:", math.fabs(sp.integrate.quad(F, -1, 1)[0] - runge(resr, res, dx/2, dx ,  1)))
print("\n")

res2 = (F(x0) + F(x1))/2
x = x0 + dx
for i in range(splitting-2):
    res2 += F(x)
    x += dx
res2 *= dx

res2r = (F(x0) + F(x1))/2
x = x0 + dx/2
for i in range(splitting*2-2):
    res2r += F(x)
    x += dx/2
res2r *= dx/2

print("Результат методом трапеций:", res2)
print("Погрешность по сравнению с модулем SciPy:", math.fabs(sp.integrate.quad(F, -1, 1)[0] - res2))


print("Результат методом трапеций уточненный:", res2)
print("Погрешность по сравнению с модулем SciPy:", math.fabs(sp.integrate.quad(F, -1, 1)[0] - runge(res2r, res2, dx/2, dx, 2)))
print("\n\n")


h1 = 1
h2 = 0.5
res3 = F(x1) + F(x0)
x = x0 + h1
for i in range(1, round((x1-x0)/h1)):
    if i % 2 == 0:
        res3 += 2*F(x)
    else:
        res3 += 4 * F(x)
    x += h1
res3 *= h1/3
print("Метод Симпсона ----------------------------------------------")
print("h1: ", res3)
print("Погрешность по сравнению с модулем SciPy:", math.fabs(sp.integrate.quad(F, -1, 1)[0] - res3))


res4 = F(x1) + F(x0)
x = x0 + h2
for i in range(1, round((x1-x0)/h2)):
    if i % 2 == 0:
        res4 += 4*F(x)
    else:
        res4 += 2 * F(x)
    x += h2
res4 *= h2/3
print("h2: ", res4)
print("Погрешность по сравнению с модулем SciPy:", math.fabs(sp.integrate.quad(F, -1, 1)[0] - res4))


print("Уточненные результаты: ", runge(res3, res4, h1, h2, 4))
print("Погрешность по сравнению с модулем SciPy:", math.fabs(sp.integrate.quad(F, -1, 1)[0] - runge(res3, res4, h1, h2, 4)))

