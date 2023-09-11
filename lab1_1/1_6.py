def sum(c_1, c_2):
    sum1 = 0
    sum2 = 0
    for i in c_1:
        sum1 += i

    for i in c_2:
        sum2 += i

    if sum1 > sum2:
        print('Сумма первого кортежа больше: ' + str(sum1))
    else:
        print('Сумма второго кортежа больше: ' + str(sum2))


def task():
    c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
    c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
    sum(c_1, c_2)
    print('Кортеж 1: максимальное (индекс): ' + str(c_1.index(max(c_1))))
    print('Кортеж 1: минимальное (индекс): ' + str(c_1.index(min(c_1))))
    print('Кортеж 2: максимальное (индекс): ' + str(c_2.index(max(c_2))))
    print('Кортеж 2: минимальное (индекс): ' + str(c_2.index(min(c_2))))


task()
