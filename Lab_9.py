import math

import numpy as np

N = 4
Nc = 2
Ng = 10
a = Nc
b = Nc + N
def F(x):
    return Ng*x + math.sin(x)

x_list = np.linspace(a, b, N)
y_list = []
for x in x_list:
    y_list.append(F(x))







