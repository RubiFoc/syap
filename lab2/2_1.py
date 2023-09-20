class NotWordException(Exception):
    def __init__(self, message="Это не одно слово!"):
        self.message = message
        super().__init__(self.message)


def is_not_word(string: str):
    for i in string:
        if i in '1234567890-/{}\\|,.?!#@$%^&*()_+=':
            return True
    return False


def is_anagram(string1: str, string2: str):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False


def main():
    while True:
        menu = '''
1 - Сверить строки
2 - Выход
'''
        match int(input(menu)):
            case 1:
                try:
                    string1, string2 = input('Введите первое слово для проверки: '),\
                                       input('Введите второе слово для проверки: ')
                    if is_not_word(string1) or is_not_word(string2):
                        raise NotWordException
                    if is_anagram(string1, string2):
                        print('Слова являются анаграммами!')
                    else:
                        print('Слова не являются анаграммами!')
                except NotWordException:
                    print('Введенное не является словом')
            case 2:
                break


main()
