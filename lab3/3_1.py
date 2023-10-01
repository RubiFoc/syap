# 1. Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать в файл F2 только те
# строки из F1, которые начинаются с буквы «А». Подсчитать количество слов
# в F2. – 3 балла

with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (пустая строка для завершения ввода): ")
        if not line:
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    # Читаем строки из F1
    for line in f1:
        # Проверяем, начинается ли строка с буквы "А" (регистронезависимо)
        if line.strip().lower().startswith('а'):
            f2.write(line)

with open('F2.txt', 'r') as f2:
    lines = f2.readlines()
    word_count = sum(len(line.split()) for line in lines)

print(f"Скопировано строк в F2: {len(lines)}")
print(f"Общее количество слов в F2: {word_count}")
