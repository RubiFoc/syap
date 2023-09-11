# 1. Вывести на экран 1001 простое число. – 2 балла

def is_prime(a: int):
    if a <= 1:
        return False
    if a <= 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    # все простые числа, начиная с 5, могут быть представлены в виде 6k ± 1, где k - натуральное число.
    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return False
        i += 6
    return True


def task():
    counter = 0
    i = 0
    while counter < 1001:
        i += 1
        if is_prime(i):
            print(i)
            counter += 1


task()
