# Задание 1:
# Класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первый метод: создайте переменную и выведите её.
# Второй метод: верните сумму 2-ух глобальных переменных.
# Третий метод: верните результат возведения первой динамической
# переменной во вторую динамическую переменную.
# Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a.
# – 1 балл

class Example:
    static_var1 = 1
    static_var2 = 0

    def __init__(self, dynamic_var1, dynamic_var2):
        self.dynamic_var1 = dynamic_var1
        self.dynamic_var2 = dynamic_var2

    def input_output(self, dynamic_var_1):
        a = dynamic_var_1
        print(a)

    def sum_global(self):
        return self.static_var1 + self.static_var2

    def exponentiation(self):
        return self.dynamic_var1 ** self.dynamic_var2


obj = Example(3, 4)
obj.input_output(100)
print(obj.sum_global())
print(obj.exponentiation())
