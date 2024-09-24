from random import randint


def check_number(number):
    a = [1, 2, 3]
    while True:
        number = check(number)
        if number in a:
            return number
        else:
            number = input('некорректные данные ')


def check(number):
    while True:
        try:
            return int(number)
        except ValueError:
            number = input('некорректные данные ')


m = [4, 30]
first = randint(m[0], m[-1])

while True:
    if first == 1:
        print('Вы проиграли')
        exit()
    if first == 1 or first == 21:
        stone = 'камень'
    elif first in [2, 3, 4, 22, 23, 24]:
        stone = 'камня'
    else:
        stone = 'камней'
    user = input(f'Сейчас в куче {first} {stone}, сколько вы хотите '
                 f'убрать(1, 2 или 3 камня)? ')

    user = check_number(user)

    first = first - user
    if first in [2, 3, 4]:
        print('вы проиграли')
        exit()
    if first == 1:
        print('Вы выиграли')
        exit()

    elif first < 1:
        print('Вы выиграли, т.к. в куче нет камней')
        exit()
    else:
        first = first - randint(1, 3)
        if first < 1:
            print('Вы выиграли, т.к. в куче нет камней')
            exit()
