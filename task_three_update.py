number = input('введите число, которое будет суммой цифр\
 трёхзначного числа')

def check(number):
    while True:
        try:
            return int(number)
        except ValueError:
            number = input('некорректные данные ')

number = check(number)

if 1 <= number <= 27:
    container = []
    for three_digit_number in range(100, 1000):
        if sum(map(int, str(three_digit_number))) == number:
            container.append(three_digit_number)
    print(f'Все трёхзначные числа с заданной суммой цифр: {container}')
else: print('Некорректные значения')