import random

def IsSorted(arr: list, mode: bool) -> bool:
    isGood = True
    if mode == True:
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i + 1]:
                isGood = False
                break
    else:
        for i in range(0, len(arr)-1):
            if arr[i] < arr[i + 1]:
                isGood = False
                break
    return isGood

def BozoSortList(arr: list, mode = True) -> list:
    n = len(arr)
    while IsSorted(arr, mode) == False:
        second_index = first_index = random.randint(0, n-1)
        while first_index == second_index:
            second_index = random.randint(0, n-1)
        arr[first_index], arr[second_index] = arr[second_index], arr[first_index]
    return arr
    
def BozoSortListOfLists(arr: list, mode = True) -> list:
    target = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            target.append(arr[i][j])
    return BozoSortList(target, mode)
    
def BozoSort4(f: int, s: int, t: int, mode = True) -> list:
    target = [f, s, t]
    return BozoSortList(target, mode)

print('Введите количество элементов n')
n = int(input())
sqr_n = n ** (1/2)
if sqr_n != int(sqr_n):
    print('Корень из n должен быть целым числом')
    exit()
print('Введите n чисел')
arr = list(map(int, input().split()))
if len(arr) != n:
    print('Введено неверное количество элементов')
    exit()

arr2 = []
i = 0
row = []
for element in arr:
    row.append(element)
    i +=1
    if i % sqr_n == 0:
        arr2.append(row)
        row = []
        i = 0

f = arr[0]
s = arr[1]
t = arr[2]

print(' '.join(map(str, BozoSortList(arr, True))))
print(' '.join(map(str, BozoSortList(arr, False))))
print(' '.join(map(str, BozoSortListOfLists(arr2, True))))
print(' '.join(map(str, BozoSortListOfLists(arr2, False))))
print(' '.join(map(str, BozoSort4(f,s,t, True))))
print(' '.join(map(str, BozoSort4(f,s,t, False))))