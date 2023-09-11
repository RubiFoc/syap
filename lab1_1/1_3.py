# Введите одномерный целочисленный список. Найдите наибольший
# нечетный элемент. Найдите минимальный по модулю элемент списка.
# – 1 балл

def find_highest_odd(a: list, n: int):
    highest_odd = a[0]
    for i in range(2, n, 2):
        if highest_odd <= a[i]:
            highest_odd = a[i]
    return highest_odd


def find_minimal_absolute(a: list):
    temp = abs(a[0])
    for i in a:
        if abs(temp) >= abs(i):
            temp = i
    return temp


def task():
    while input('Введите n, чтобы выйти: ') != 'n':
        n = int(input('Введите размер списка: '))
        list1 = list()
        for i in range(n):
            num = int(input('Введите число под номером ' + str(i+1) + ': '))
            list1.append(num)  # Изменено: использование метода append для добавления элемента в список

        highest_odd = find_highest_odd(list1, n)
        minimal_absolute = find_minimal_absolute(list1)
        print(f"Самое большое нечётное: {highest_odd},\nСамый минимальный модуль: {minimal_absolute}")


task()
