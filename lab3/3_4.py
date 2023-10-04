# 4. Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
# 2000}]
# Подсказка: использовать менеджер контекста

import json

firm_list = []
total_profit = 0
firm_count = 0

with open('firm_data.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split()
    if len(parts) == 4:
        name, ownership, revenue, expenses = parts
        revenue = float(revenue)
        expenses = float(expenses)
        profit = revenue - expenses

        firm_list.append({name: profit})  # Включаем все фирмы в список, даже с отрицательной прибылью
        if profit > 0:
            total_profit += profit
            firm_count += 1

if firm_count > 0:
    average_profit = total_profit / firm_count
else:
    average_profit = 0

result_list = [firm_list, {"average_profit": average_profit}]

with open('firm_data.json', 'w') as json_file:
    json.dump(result_list, json_file)

print("Данные сохранены в файл firm_data.json")
