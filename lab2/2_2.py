def function(a):
    if str(a).isnumeric():
        print(''.join(reversed(str(a))))
    if isinstance(a, tuple):
        print('Количество элементов кортежа:', len(a))
    elif isinstance(a, list):
        total_sum = 0
        for i in a:
            if i == 0:
                break
            total_sum += i
        print('Сумма элементов списка:', total_sum)
    elif isinstance(a, str):
        number_of_words = len(a.split())
        print(f"Количество слов: {number_of_words}")

        character_count = {}
        for char in a:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

        most_common_character = max(character_count, key=character_count.get)
        most_common_character_count = character_count[most_common_character]
        print("Символ, который встречается чаще всего:", most_common_character)
        print("Количество его вхождений:", most_common_character_count)


def task():
    function((1, 2, 3, 4))
    function([1, 2, 3, 4])
    function(1234)
    function('Enjoy every moment')


task()
