import math
import numpy as np
import matplotlib.pyplot as plt

Ng = 10
Nc = 2
x_list = [-2, -1, 0, 1, 2]
y_list = [Nc, Ng, -1, Nc, Ng]

x_list = [0, 1, 2, 3]
y_list = [-5, -6, 3, 28]


def phi1(x):
    return ((x - x_list[1]) * (x - x_list[2]) * (x - x_list[3])) / \
        ((x_list[0] - x_list[1]) * (x_list[0] - x_list[2]) * (x_list[0] - x_list[3]))


def phi2(x):
    return ((x - x_list[0]) * (x - x_list[2]) * (x - x_list[3])) / \
        ((x_list[1] - x_list[0]) * (x_list[1] - x_list[2]) * (x_list[1] - x_list[3]))


def phi3(x):
    return ((x - x_list[0]) * (x - x_list[1]) * (x - x_list[3])) / \
        ((x_list[2] - x_list[0]) * (x_list[2] - x_list[1]) * (x_list[2] - x_list[3]))


def phi4(x):
    return ((x - x_list[0]) * (x - x_list[1]) * (x - x_list[2])) / \
        ((x_list[3] - x_list[0]) * (x_list[3] - x_list[1]) * (x_list[3] - x_list[2]))


def L(x):
    return y_list[0] * phi1(x) + y_list[1] * phi2(x) + y_list[2] * phi3(x) + y_list[3] * phi4(x)


def check():
    for i in range(4):
        if (y_list[i] - L(x_list[i])) < 1e-5:
            print("Check:", i, "  set y = ", y_list[i], "\tcalculated y = ", L(x_list[i]),
                  "\tdelta = ", math.fabs(y_list[i] - L(x_list[i])))
        else:
            print("Some error in x = ", x_list[i], "\ty = ", y_list[i])

print("{} * phi1(x) + {} * phi2(x) + {} * phi3(x) + {} * phi4(x)".format(y_list[0],y_list[1], y_list[2], y_list[3]))
print("phi1 = (x- {})*(x- {})*(x- {})/{}".format(x_list[1],x_list[2],x_list[3], ((x_list[0] - x_list[1]) * (x_list[0] - x_list[2]) * (x_list[0] - x_list[3]))))
print("phi2 = (x- {})*(x- {})*(x- {})/{}".format(x_list[0],x_list[2],x_list[3], ((x_list[1] - x_list[0]) * (x_list[1] - x_list[2]) * (x_list[1] - x_list[3]))))
print("phi3 = (x- {})*(x- {})*(x- {})/{}".format(x_list[0],x_list[1],x_list[3], ((x_list[2] - x_list[0]) * (x_list[2] - x_list[1]) * (x_list[2] - x_list[3]))))
print("phi4 = (x- {})*(x- {})*(x- {})/{}".format(x_list[0],x_list[2],x_list[1], ((x_list[3] - x_list[0]) * (x_list[3] - x_list[1]) * (x_list[3] - x_list[2]))))
print("Интерполяционный многочлен Лагранжа: ")
check()


# Многочлен ньтона
def dy(x_ind: list):
    if len(x_ind) > 2:
        return (dy(x_ind[1:]) - dy(x_ind[:-1])) / (x_list[x_ind[-1]] - x_list[x_ind[0]])
    elif len(x_ind) == 2:
        return (y_list[x_ind[1]] - y_list[x_ind[0]]) / (x_list[x_ind[1]] - x_list[x_ind[0]])
    else:
        return y_list[x_ind[0]]


def newton(x:int):
    res = 0
    for i in range(len(x_list)):
        tmp = 1
        ll = []
        for j in range(i):
            tmp *= x - x_list[j]
            ll.append(j)
        ll.append(i)
        tmp *= dy(ll)
        res += tmp
    return res


def checkN():
    for i in range(4):
        if (y_list[i] - newton(x_list[i])) < 1e-5:
            print("Check:", i, "  set y = ", y_list[i], "\tcalculated y = ", L(x_list[i]),
                  "\tdelta = ", math.fabs(y_list[i] - L(x_list[i])))
        else:
            print("Some error in x = ", x_list[i], "\ty = ", y_list[i])

print("\nИнтерполяционный многочлен ньютона: ")
print("N = {}+{} * (x-{}) + {}*(x-{})*(x-{}) + {}*(x-{})*(x-{})*(x-{})".format(dy([0]), dy([0,1]), x_list[0], dy([0,1,2]),
                                                                                x_list[0], x_list[1], dy([0,1,2,3]),
                                                                                x_list[0],  x_list[1], x_list[2]))
checkN()

x_sp = np.linspace(0, 3, 100)
y_sp = L(x_sp)
x_sp2 = np.linspace(0, 3, 100)
y_sp2 = newton(x_sp)
fig, ax = plt.subplots()
ax.plot(x_sp, y_sp)
ax.plot(x_sp2, y_sp2)
for i in range(len(x_list)):
    plt.scatter(x_list[i], y_list[i])
plt.show()
