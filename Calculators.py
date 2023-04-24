def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

while True:

    select = input('Select a Operations + - * / : ')

    number_1 = int(input('Enter a First Number : '))
    number_2 = int(input('Enter a First Number : '))

    if select == '+':
       print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif select == '-':
       print(number_1, "-", number_2, '=', sub(number_1, number_2))
    elif select == '*':
       print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif select == '/':
       print(number_1, "/", number_2, '=', divide(number_1, number_2))

    # Next Calculations
    next = input('Lets Do Next Calculations? (yes/no) : ')
    if next == 'no':
        print('Programme End')
        break

