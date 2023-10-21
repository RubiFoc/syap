import numpy as np


x = 0.24
a = 5.8

part1 = np.arctan(x)**2
part2 = np.sqrt((x+1.43**3))
part3 = (np.cos(np.pi/(2*a)))**3
part4 = np.abs(x-a**1/5)

z = part1 - part2 + part3/part4

print(z)

# Создание матрицы X и вектора Y
X = np.column_stack((np.ones(12), np.arange(2, 14), np.random.randint(60, 83, 12)))
Y = np.random.uniform(13.5, 18.6, 12)

# Вычисление оценок коэффициентов регрессии
XT = X.T  # Транспонирование матрицы X
XTX_inv = np.linalg.inv(np.dot(XT, X))  # (X^T * X)^(-1)
XTY = np.dot(XT, Y)  # X^T * Y
beta_hat = np.dot(XTX_inv, XTY)

print("Оценки коэффициентов регрессии:")
print("beta_0 (интерсепт):", beta_hat[0])
print("beta_1:", beta_hat[1])
print("beta_2:", beta_hat[2])

# Вычисление значений Y с использованием оценок коэффициентов A
Y_predicted = beta_hat[0] + beta_hat[1] * X[:, 1] + beta_hat[2] * X[:, 2]

# Вывод исходных и предсказанных значений Y
print("Исходные значения Y:")
print(Y)
print("Предсказанные значения Y:")
print(Y_predicted)

