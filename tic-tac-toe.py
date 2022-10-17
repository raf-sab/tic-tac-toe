from random import randrange
from time import sleep


# Вывод поля с координатами
def show_field(f):
    num = '1 2 3'
    print(f"\n{gc}    |   1   |   2   |   3   |\n____|{'_______|'*3}{dc}")
    for row, i in zip(f, num.split()):
        print(f"{gc}    |{'       |'*3}{dc}")
        line = f'{gc}   | {dc}'
        print(f" {gc}{i}  |   {dc}{'  '.join(str(j)+line for j in row)}")
        print(f"{gc}____|{'_______|'*3}{dc}")


# Обработка координат, введенных пользователями
def users_input(f, user):
    x, y = None, None
    user = user.replace('0', 'ⵔ').replace('X', 'ⵝ')
    place = input(f'\nХодит - {user} \nВведите координаты: {rct}')
    while True:
        quit() if place.lower() in ['stop', 'ыещз'] else ''
        place = place.split()
        if len(place) != 2:
            place = input(f'Введите две координаты: {rct}')
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            place = input(f'Введите числа: {rct}')
            continue
        x, y = map(int, place)
        if not all([1 <= x < 4, 1 <= y < 4]):
            place = input(f'ВВведите координаты в диапазоне 1...3: {rct}')
            continue
        if f[x-1][y-1] != ' ':
            place = input(f'Клетка занята, введите свободные координаты: {rct}')
            continue
        break
    return x, y


# Выигрышные позиции
def win(f, user):
    f_list = []
    for j in f:
        f_list += j
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])
    # print(list(indices))
    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            if p[0] == 0 or p[1] == 0 or p[2] == 0:
                f[0][0] = f'{rc}{f[0][0]}{dc}'
            if p[0] == 1 or p[1] == 1 or p[2] == 1:
                f[0][1] = f'{rc}{f[0][1]}{dc}'
            if p[0] == 2 or p[1] == 2 or p[2] == 2:
                f[0][2] = f'{rc}{f[0][2]}{dc}'
            if p[0] == 3 or p[1] == 3 or p[2] == 3:
                f[1][0] = f'{rc}{f[1][0]}{dc}'
            if p[0] == 4 or p[1] == 4 or p[2] == 4:
                f[1][1] = f'{rc}{f[1][1]}{dc}'
            if p[0] == 5 or p[1] == 5 or p[2] == 5:
                f[1][2] = f'{rc}{f[1][2]}{dc}'
            if p[0] == 6 or p[1] == 6 or p[2] == 6:
                f[2][0] = f'{rc}{f[2][0]}{dc}'
            if p[0] == 7 or p[1] == 7 or p[2] == 7:
                f[2][1] = f'{rc}{f[2][1]}{dc}'
            if p[0] == 8 or p[1] == 8 or p[2] == 8:
                f[2][2] = f'{rc}{f[2][2]}{dc}'
            return True
    return False


# Проверка на занятость ячеек (игра с компьютером)
def empty_cell(y, x):
    cell = field[y][x]
    if cell == ' ':
        return True    # ячейка свободна
    else:
        return False   # ячейка занята


# Количесто свободных ячеек (игра с компьютером)
def count_empty_cells():
    count = 0
    for y in field:
        for x in y:
            if x == ' ':
                count += 1
    return count


# Координаты (игра с компьютером)
def comp_set():
    val = randrange(0, count_empty_cells())
    for x in range(3):
        for y in range(3):
            if val > 0:
                if empty_cell(x, y):
                    val -= 1
            else:
                if empty_cell(x, y):
                    field[x][y] = '0'
                    return x, y


# Начало игры
def start():
    print(f'\n{yc}Новая игра:{dc}')
    count = 0
    while True:
        show_field(field)
        if count % 2 == 0:
            user = 'X'
        else:
            user = '0'
        if count < 9:
            if option == '1':
                x, y = users_input(field, user)
                field[x-1][y-1] = user
            else:
                if user == 'X':
                    x, y = users_input(field, user)
                    field[x - 1][y - 1] = user
                else:
                    print('\nХодит - ⵔ (компьютер)')
                    c = comp_set()
                    print(f"Координаты: {c[0] + 1} {c[1] + 1}")
                    sleep(1.5)
        elif count == 9:
            print(f'\n{yc}Ничья{dc}\n')
            break
        # print(field)
        if win(field, user):
            user = user.replace('0', 'ⵔ').replace('X', 'ⵝ')
            show_field(field)
            print(f'\n{yc}Выиграл - {user}{dc}\n')
            break
        count += 1


# Цвета
rct = "\033[31m" + "► " + "\033[0m"        # красный треугольник
yct = "\033[33m" + "▪ " + "\033[0m"        # желтый круг
rc = "\033[31m"                            # красный цвет
yc = "\033[33m"                            # желтый цвет
gc = "\033[32m"                            # зеленый цвет
dc = "\033[0m"                             # цвет дефолтный

option = ''  # вариант игры: 1 - человек-человек, 2 - человек-компьютер
level = ''  # уровень сложности: 1 - легкий, 2 - сложный

print(f'{rc}')
print(f'                                     Tic-Tac-Toe  |  v 1.0  |  Сабиров Рафаиль')
print(f'{gc}')
print('######  ##   #####        ######   #####   #####        ######   ####   ######')
print('######  ##  ######        ######  ######  ######        ######  ######  ######')
print('  ##    ##  ##              ##    ##  ##  ##              ##    ##  ##  ##    ')
print('  ##    ##  ##      ####    ##    ##  ##  ##      ####    ##    ##  ##  ######')
print('  ##    ##  ##      ####    ##    ######  ##      ####    ##    ##  ##  ######')
print('  ##    ##  ##              ##    ######  ##              ##    ##  ##  ##    ')
print('  ##    ##  ######          ##    ##  ##  ######          ##    ######  ######')
print('  ##    ##   #####          ##    ##  ##   #####          ##     ####   ######')
print(f'{dc}')

print(f'{yc}ПРАВИЛА:{dc}')
sleep(0.5)
print(f'{yct}ходы делаются поочередно, первыми ходят - ⵝ')
sleep(0.5)
print(f'{yct}чтобы сделать ход, нужно ввести координаты (строка колонка), например: 1 1')
sleep(0.5)
print(f'{yct}побеждает тот, кто первый выстроит линию из трех своих символов')
sleep(0.5)
print(f'{yct}для досрочного выхода из игры наберите "stop"\n')
sleep(1.5)

while True:
    game = input(f'Начать игру? (Y/N): {rct}').lower()
    quit() if game in ['stop', 'ыещз'] else ''
    if game in ['y', 'н']:
        while option not in ['1', '2']:
            option = input(f'Вариант игры? (1 - человек-человек, 2 - человек-компьютер: {rct}')
            quit() if option in ['stop', 'ыещз'] else ''
            # level = input(f'Уровень сложности? (1 - легкий, 2 - сложный):  {rct}')
            # quit() if level in ['stop', 'ыещз'] else ''
        while option == '2' and level not in ['1', '2']:
            level = input(f'Уровень сложности? (1 - легкий, 2 - сложный):  {rct}')
            quit() if level in ['stop', 'ыещз'] else ''
        if level == '2':
            while option == '2' and level not in ['1']:
                level = input(f'Сложный Уровень будет доступен в следующей версии, выберите пока легкий - 1:  {rct}')
                quit() if level in ['stop', 'ыещз'] else ''
        field = [[' '] * 3 for _ in range(1, 4)]  # поле
        start()
        option = ''
    elif game in ['n', 'т']:
        quit()
