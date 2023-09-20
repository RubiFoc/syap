def task():
    matrix = [
        [3, 1, 4],
        [1, 5, 9],
        [2, 6, 5]
    ]

    # Инициализируем переменные для максимального элемента и его индексов
    max_element = matrix[0][0]  # Предполагаем, что первый элемент - максимальный
    max_row = 0
    max_col = 0

    # Проходим по каждому элементу матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_row = i
                max_col = j

    # Выводим индексы первого вхождения максимального элемента
    print(f"Индексы первого вхождения максимального элемента: ({max_row}, {max_col})")

task()