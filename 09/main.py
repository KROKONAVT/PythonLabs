import math
print('Введите первое время')
[h1, m1] = map(int, input().split(':'))
print('Введите второе время')
[h2, m2] = map(int, input().split(':'))
if h1 < 0 or h1 > 23 or h2 < 0 or h2 > 23 or m1 < 0 or m1 > 59 or m2 < 0 or m2 > 59:
    print('Некорректный ввод')
    exit()
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
if math.fabs(t1 - t2) < 16:
    print('Встреча состоится')
else:
    print('Встреча не состоится')
