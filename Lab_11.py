x = [-1, 0, 1, 2, 3]
y = [-5, 0, 0.5, 0.86603, 1]

yp = [y[1] - y[0]]
ypp = []

for i in range(1, len(x) - 1):
    yp.append((y[i+1] - y[i-1])/2)
yp.append(y[-1] - y[-2])

for i in range(1, len(x) - 1):
    ypp.append((y[i+1] - 2*y[i] - y[i-1]))

print("Вектор производных таблично заданной функции:", yp)
print("Вектор вторых производных таблично заданной функции:", ypp)