# Игра крестики-нолики
size = 3
field = [['-' for i in range(size)] for j in range(size)]
f = True
order = 1


def check_win():
    f = 0
    for i in range(0, size):
        if field[i][0] == field[i][1] == field[i][2] and field[i][0] != '-':
            f += 1

    for i in range(0, size):
        if field[0][i] == field[1][i] == field[2][i] and field[0][i] != '-':
            f += 1

    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != '-':
        f += 1

    if field[0][2] == field[1][1] == field[2][0] and field[0][2] != '-':
        f += 1
    win = True if f > 0 else False
    return win

while f:
    p = 'x' if order % 2 == 1 else 'o'
    choice = input(f' Ход: {order}. Игрок: {p.upper()} введите координаты строки и столца через пробел (от 0 до {size - 1}): ')
    step = list(map(int, (choice.split())))
    while (step[0] > size - 1) or (step[1] > size - 1):
        choice = input(
            f' Недопустимый ход - за рамками игрового поля \n Игрок: {p.upper()} введите заново координаты строки и столца через пробел (от 0 до {size - 1}): ')
        step = list(map(int, (choice.split())))

    while field[step[0]][step[1]] != '-':
        choice = input(
            f' Недопустимый ход - поле уже занято \n Игрок: {p.upper()} введите заново координаты строки и столца  через пробел (от 0 до {size - 1}): ')
        step = list(map(int, (choice.split())))
    field[step[0]][step[1]] = p
    check_win()
    order += 1
    print('Текущие положение:')
    for i in field:
        for j in i:
            print(j, end=' ')
        print()
    if check_win():
        print(f'Конец игры. Выиграл игрок - {p.upper()}!')
        f = False
    if f and order == 10:
        f = False
        print(f'Конец игры. Ничья!')