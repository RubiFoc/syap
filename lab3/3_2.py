# Имеется текстовый файл «Результаты соревнований», строка
# которого содержит в себе информацию: фамилия спортсмена, результат.
# Вывести на экран информацию о том, кто занял первое, второе и третье
# места.
# Пример файла:
# Иванов 2
# Петров 5– 3 балла

with open('Результаты соревнований.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

results = []

for line in lines:
    parts = line.strip().split()
    if len(parts) == 2 and 0 < int(parts[1]) < 4:
        name, result = parts[0], int(parts[1])
        results.append((name, result))

sorted_results = sorted(results, key=lambda x: x[1])

print("Результаты соревнований:")
for name, result in sorted_results:
    print(f"{result} место: {name}")
