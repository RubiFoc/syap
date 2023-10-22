import numpy as np
import matplotlib.pyplot as plt


# Определение интервала для параметра a
a_values = np.arange(-5, 12.1, 2.5)

# Создание массива значений функции f(x) для каждого значения a в интервале
x = 3.567
f_values = []
for a in a_values:
    y = (1 / np.tan(x)) ** 3 + 2.24 * a * x
    f_values.append(y)

# Нахождение наибольшего, наименьшего и среднего значения функции, а также количества элементов массива
max_f = max(f_values)
min_f = min(f_values)
avg_f = np.mean(f_values)
num_elements = len(f_values)

# Сортировка массива f_values в зависимости от четности индекса
even_sorted = sorted(f_values, reverse=True)  # Для четных индексов (по убыванию)
odd_sorted = sorted(f_values)  # Для нечетных индексов (по возрастанию)

# Построение графика значений функции
plt.plot(a_values, f_values, label='f(x)')

# График прямой с средним значением функции
avg_line = [avg_f] * len(a_values)
plt.plot(a_values, avg_line, label='Среднее значение', linestyle='--')

plt.xlabel('Значение параметра a')
plt.ylabel('Значение функции f(x)')
plt.title('График функции f(x)')
plt.legend()

plt.show()

# Создание массивов значений x и y
x = np.linspace(-10, 10, 200)  # Диапазон значений x
y = np.linspace(-10, 10, 200)  # Диапазон значений y
X, Y = np.meshgrid(x, y)

# Ограничение диапазона значений X и Y, заменяя отрицательные значения на ноль
X = np.where(X < 0, 0, X)
Y = np.where(Y < 0, 0, Y)

# Функция z = x^0.25 + y^0.25
Z1 = X**0.25 + Y**0.25

# Функция z = x^2 - y^2
Z2 = X**2 - Y**2

# Функция z = 2x + 3y
Z3 = 2*X + 3*Y

# Функция z = 2 + 2x + 2y - x^2 - y^2
Z4 = 2 + 2*X + 2*Y - X**2 - Y**2

# Построение графиков
fig = plt.figure(figsize=(12, 10))

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_title('z = x^0.25 + y^0.25')

ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_title('z = x^2 - y^2')

ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='viridis')
ax3.set_title('z = 2x + 3y')

ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(X, Y, Z4, cmap='viridis')
ax4.set_title('z = 2 + 2x + 2y - x^2 - y^2')

plt.tight_layout()
plt.show()