import itertools as it

result = []

print('Введите количество символов')
cur_len = int(input())
if cur_len < 1 or cur_len > 8:
    print('Некорректный ввод')
    exit()
print('Введите символы')
alphabet = input()

if cur_len > len(alphabet):
    for i in list(it.product(alphabet, repeat=cur_len)):
        result.append(''.join(map(str, i)))
        
    i = 0
    while i < len(result):
        isGood = False
        for j in range(0, cur_len-1):
            for k in range(j + 1, cur_len):
                if result[i][j] != result[i][k]:
                    isGood = True
                    break
            if isGood == True:
                break
        if isGood == False:
            result.remove(result[i])
            i -= 1
        i += 1
        
    for i in range(0, len(result)):
        print(result[i], end = ' ')
else:
    for i in list(it.permutations(alphabet, cur_len)):
        print(''.join(map(str, i)), end = ' ')