import random
while True:
    print('Игра Угадай число')
    print('Компьютер загадал число!')
    isLose = True
    a = random.randint(0, 100)
    print(a)
    i = 5
    while i > 0:
        i = i - 1
        b = int(input())
        if b == a:
            isLose = False
            break
        elif b < a:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')
    if isLose:
        print('Вы проиграли. Было загадано: {0}'. format(a))
    else:
        print('Поздравляю! Вы угадали')
    print('Хотите начать сначала ? (1 - ДА)')
    b = int(input())
    if b != 1:
        break
            