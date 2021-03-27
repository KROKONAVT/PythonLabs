print('Введите количество банкнот')
a = int(input())
isBad = False
print('Введите номера банкнот через пробел')
numbers = list(input().split())
if len(numbers) != a:
    print('Неправильный ввод')
else:
    for i in range(0, len(numbers)):
        if len(numbers[i]) != 9:
            continue
        else:
            if numbers[i][0] == 'a' and numbers[i][4] == '5' and numbers[i][5] == '5' and numbers[i][6] == '6' and numbers[i][7] == '6' and numbers[i][8] == '1':
                print(numbers[i],end =' ')
                isBad = True
if isBad == False:
    print("-1")