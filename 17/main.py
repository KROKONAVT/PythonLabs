red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
last_k = [-1] * 12
numbers_total = [0] * 37
input_counter = 0

while True:
    current_index = input_counter % 12
    print('Введите число')
    num = int(input())
    if(num < 0):
        break
    elif num > 36:
        print('Некорректный ввод')
        continue
    last_k[current_index] = num
    if last_k[current_index] < 0:
        exit()
    
    numbers_last_k = [0] * 37
    black_counter = 0
    red_counter = 0
    numbers_total[last_k[current_index]] += 1
    
    for i in range(0, 12):
        if last_k[i] < 0:
            continue
        numbers_last_k[last_k[i]] += 1
        for j in range(0, len(red_numbers)):
            if last_k[i] == red_numbers[j]:
                red_counter += 1
                break
        for j in range(0, len(black_numbers)):
            if last_k[i] == black_numbers[j]:
                black_counter += 1
                break
    
    max_count = 0
    for i in range(0, len(numbers_total)):
        if numbers_total[i] > max_count:
            max_count = numbers_total[i]
    
    for i in range(0, len(numbers_total)):
        if numbers_total[i] == max_count:
            print(i, end = ' ')
    
    print()
    
    for i in range(0, len(numbers_last_k)):
        if numbers_last_k[i] == 0:
            print(i, end = ' ')
    
    print()
    print(red_counter, black_counter, end = '\n\n')

    input_counter += 1