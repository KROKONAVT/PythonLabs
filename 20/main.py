print('Введите количество денег')
n = int(input())
print('Введите количество напитков')
k = int(input())

names = [0] * k
prices = [0] * k
volumes = [0] * k

max_volume = -1
max_count = -1
max_n = -1
max_index = -1

print('Введите хар-ки напитков [Название Цена Объем]')
for i in range(0, k):
    names[i], prices[i], volumes[i] = input().split()
    prices[i] = int(prices[i])
    volumes[i] = int(volumes[i])
    
isEnough = False
for i in range(0, k):
    if n >= prices[i]:
        isEnough = True
        break

if isEnough == False:
    print('-1')
else:
    for i in range(0, k):
        volume = 0
        count = 0
        temp = n
        while temp >= prices[i]:
            count += 1
            temp -= prices[i]
            volume += volumes[i]
        if volume > max_volume:
            max_volume = volume
            max_index = i
            max_count = count
            max_n = temp
            
    print(names[max_index], max_count)
    print(max_volume)
    print(max_n)