from functions import summ, subtraction, multiplying, division, square, exp, factorial, \
    extract_root, extract_root_2, guide, menu, time_to_go, give_result, \
    summ_input, subtraction_input, multiplying_input, division_input, exp_input, square_input, \
    factorial_input, extract_root_input, extract_root_2_input


def calculator():

    # приветствие, вывод гайда и меню

    print('Добро пожаловать в калькулятор!')
    guide()
    while True:
        choice = menu()
        if time_to_go(choice):

            # анализ вводимых данных, вычисления

            if choice == '+':
                num = summ_input()
                a = int(num[0])
                b = int(num[1])
                result = summ(a, b)
                give_result(result)
                continue
            elif choice == '-':
                num = subtraction_input()
                a = int(num[0])
                b = int(num[1])
                result = subtraction(a, b)
                give_result(result)
                continue
            elif choice == '*':
                num = multiplying_input()
                a = int(num[0])
                b = int(num[1])
                result = multiplying(a, b)
                give_result(result)
                continue
            elif choice == '/':
                num = division_input()
                a = int(num[0])
                b = int(num[1])
                result = division(a, b)
                give_result(result)
                continue
            elif choice == '**':
                num = square_input()
                a = int(num)
                result = square(a)
                give_result(result)
                continue
            elif choice == '^':
                num = exp_input()
                a = int(num[0])
                b = int(num[1])
                result = exp(a, b)
                give_result(result)
                continue
            elif choice == '<':
                num = extract_root_2_input()
                a = int(num)
                result = extract_root_2(a)
                give_result(result)
                continue
            elif choice == '<?':
                num = extract_root_input()
                a = int(num[0])
                b = int(num[1])
                result = extract_root(a, b)
                give_result(result)
                continue
            elif choice == '!':
                num = factorial_input()
                a = int(num)
                result = factorial(a)
                give_result(result)
                continue
            else:
                print('\n'
                      'Ваша команда не распознана. Попробуйте ещё раз.'
                      '\n')
                continue
        else:
            break
