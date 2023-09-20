class CustomException(Exception):
    ...


def task():
    try:
        a = 1/0

    except ZeroDivisionError:
        print('Деление на ноль')

    try:
        b = (1, 2, 3)
        a = int(b)
    except TypeError:
        print('TypeError')

    try:
        a = 1
        if a == 1:
            raise CustomException
    except CustomException:
        print('Custom')

    try:
        a = int(input('Введите число'))
    except ValueError:
        print('ValueError')
    finally:
        print('Finally')


task()

