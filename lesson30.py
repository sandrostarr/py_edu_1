import random


def game():
    var = random.randint(0, 100)
    my_str = 0
    counter = 0
    while my_str != var:
        my_str = int(input('Введите число: '))
        counter += 1
        if my_str > var:
            print('Введённое число больше заданного. Попробуйте ещё раз')
        elif my_str < var:
            print('Введённое число меньше заданного. Попробуйте ещё раз')
        else:
            print(f'Введённое число верно и равно {my_str}')
    print(f'Количество попыток: {counter}')
    play = input('Если хотите сыграть ещё раз, нажмите y. Если нет, то нажмите n: ')

    if play == 'y':
        game()
    else:
        print('Хорошего дня')


game()