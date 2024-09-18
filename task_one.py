begin = input('введите меньший номер билета')
end = input('введите больший номер билета')
number_of_tickets = 0

while not begin.isdigit():
    begin = input("Повторите ввод начального номера")

while not len(begin) == 6:
    begin = input("Повторите ввод начального номера")
begin = int(begin)

while not end.isdigit():
    end = input("Повторите ввод последнего номера")

while not len(end) == 6:
    end = input("Повторите ввод последнего номера")
end = int(end)

for number in range(begin, end + 1):
    number = str(number)
    if int(number[0]) + int(number[1]) + int(number[2]) == \
            int(number[3]) + int(number[4]) + int(number[5]):
        number_of_tickets += 1
        print(number)
if number_of_tickets == 0:
    print('Вы некорректно ввели данные')
else:
    print(f'Количество счастливых билетов: {number_of_tickets}')
