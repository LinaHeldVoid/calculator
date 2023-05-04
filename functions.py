data = [
        'Выберите арифметическую операцию (введите одно из обозначений, указанных в скобках):',
        '(+) - Сложение',
        '(-) - Вычитание',
        '(*) - Умножение',
        '(/) - Деление',
        '(**) - Возведение в квадрат',
        '(^) - Возведение в степень n',
        '(<) - Извлечение квадратного корня',
        '(<?) - Извлечение корня степени n',
        '(!) - Вычисление факториала',
        '(выход) - Выход из программы',
        '',
    ]

instructions = [
        'Схема работы программы следующая:',
        '1) Выберите арифметическую операцию;',
        '2) Введите входные данные по указанию программы;',
        '3) Получите результат вычисления;',
        '4) Для выхода из программы наберите "выход" (в любой момент её работы).',
        '',
    ]


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# удаление лишних символов, которые пользователь может ввести по ошибке
def check_input(line):
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.replace(' ', '')
    return line


# проверка корректности ввода цифр
def check_integer(num):
    symbols = list(num)
    allowed_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    for symbol in symbols:
        if symbol not in allowed_symbols:
            print('Пожалуйста, введите число!')
            return 1
    return


# проверка допустимости числа для вычисления
def check_non_negative(num):
    if int(num) < 0:
        print('Число не может быть отрицательным!')
        return 1
    else:
        return


def check_positive(num):
    if int(num) <= 0:
        print('Число может быть только положительным!')
        return 1
    else:
        return


def check_zero(num):
    if int(num) == 0:
        print('Ноль - недопустимое значение!')
        return 1
    else:
        return


# функции, проводящие анализ вводимых значений и реализующие вычисления
# сложение
def summ(a, b):
    result = a + b
    return result


def summ_input():
    while True:
        a = input('Введите первое слагаемое: ')
        if check_integer(a):
            continue
        else:
            break
    while True:
        b = input('Введите второе слагаемое: ')
        if check_integer(b):
            continue
        else:
            break
    return a, b


# вычитание
def subtraction(a, b):
    result = a - b
    return result


def subtraction_input():
    while True:
        a = input('Введите уменьшаемое: ')
        if check_integer(a):
            continue
        else:
            break
    while True:
        b = input('Введите вычитаемое: ')
        if check_integer(b):
            continue
        else:
            break
    return a, b


# умножение
def multiplying(a, b):
    result = a * b
    return result


def multiplying_input():
    while True:
        a = input('Введите первый множитель: ')
        if check_integer(a):
            continue
        else:
            break
    while True:
        b = input('Введите второй множитель: ')
        if check_integer(b):
            continue
        else:
            break
    return a, b


# деление
def division(a, b):
    result = a / b
    return result


def division_input():
    while True:
        a = input('Введите делимое: ')
        if check_integer(a):
            continue
        else:
            break
    while True:
        b = input('Введите делитель: ')
        if check_integer(b):
            continue
        else:
            break
    return a, b


# возведение в квадрат
def square(a):
    result = a ^ 2
    return result


def square_input():
    while True:
        a = input('Введите основание степени: ')
        if check_integer(a):
            continue
        else:
            break
    return a


# возведение в n-ную степень
def exp(a, b):
    result = a ** b
    return result


def exp_input():
    while True:
        a = input('Введите основание степени: ')
        if check_integer(a):
            continue
        else:
            break
    while True:
        b = input('Введите показатель степени: ')
        if check_integer(b):
            continue
        else:
            break
    return a, b


# извлечение квадратного корня
def extract_root_2(a):
    result = a ** 0.5
    return result


def extract_root_2_input():
    while True:
        a = input('Введите число под корнем: ')
        if check_integer(a):
            continue
        if check_non_negative(a):
            continue
        else:
            break
    return a


# извлечение корня n-ной степени
def extract_root(a, b):
    power = 1/b
    result = a ** power
    return result


def extract_root_input():
    while True:
        a = input('Введите число под корнем: ')
        if check_integer(a):
            continue
        if check_non_negative(a):
            continue
        else:
            break
    while True:
        b = input('Введите показатель корня: ')
        if check_integer(b):
            continue
        if check_zero(b):
            continue
        else:
            break
    return a, b


# факториал числа
def factorial(a):
    result = 1
    while a > 1:
        result *= a
        a -= 1
    return result


def factorial_input():
    while True:
        a = input('Введите число-факториал: ')
        if check_integer(a):
            continue
        if check_non_negative(a):
            continue
        else:
            break
    return a


# вывод гайда по взаимодействию с программой
def guide():
    for line in instructions:
        print(line)


# вывод меню с опциями выбора
def menu():
    for line in data:
        print(line)
    choice = input('Ваш выбор: ')
    return choice


# функции, принимающие числа в нужном количестве
def number_input():
    number = input('Введите число: ')
    return number


def poli_number_input():
    number_1 = input('Введите первое число: ')
    number_2 = input('Введите второе число: ')
    return number_1, number_2


# вывод результатов расчёта
def give_result(result):
    print(f'\n'
          f'Результат выполнения операции: {round(result, 5)}'
          f'\n')


# функция для завершения работы программы
def time_to_go(data):
    data = check_input(data)
    if data.lower() == 'выход':
        print('Благодарим за использование нашего продукта! Приходите ещё;)')
        return
    else:
        return 1
