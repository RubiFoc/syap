# Создайте словарь из строки ' Enjoy every moment' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть
# будут числа, соответствующие количеству вхождений данной буквы в
# строку – 2 балла


def count(string: str):
    a = dict()
    for i in string:
        a[i] = string.count(i)
    return a


def task():
    string = ' Enjoy every moment'
    a = count(string)
    print(a)
    b = count(string.lower())
    print(b)


task()
