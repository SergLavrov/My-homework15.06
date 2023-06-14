# 11.16.
# Дан массив целых чисел. Выяснить:

# а) является ли s-й элемент массива положительным числом?
someList = [36, 0, -25, 40, 54, -50]
index = int(input('Enter index s: '))
if index > len(someList):
    print('Error')
elif someList[index] >= 0:
    print('Yes')
else:
    print('No')

# б) является ли k-й элемент массива четным числом ?
someList = [36, -25, 40, 54, -51]
index = int(input('Enter index k: '))
if index > len(someList):
    print('Error')
elif someList[index] % 2 == 0:
    print('Yes')
else:
    print('No')

# в) какой элемент массива больше: k-й или s-й
someList = [36, -25, 40, 54, -51]
index = int(input('Enter index k: '))
index1 = int(input('Enter index s: '))
if index or index1 > len(someList):
    print('Error')
elif someList[index] > someList[index1]:
    print('к больше s')
else:
    print('k меньше s')


# 11.18. Дан массив. Все его элементы:

а) уменьшить на 20
someList = [36, 56, 40, 54, -12]
index = 0
while index < len(someList):
    someList[index] -= 20
    index += 1
print(someList)

# б) умножить на последний элемент;
someList = [36, 56, 40, 54, 2]
lastNumber = someList[-1]
index = 0
while index < len(someList):
    someList[index] *= lastNumber
    index += 1
print(someList)

# в) увеличить на число В.
someList = [36, 56, 40, 54, -12]
number = int(input('Enter number B: '))
index = 0
while index < len(someList):
    someList[index] += number
    index += 1
print(someList)

# 11.21.
# В массиве хранятся сведения о количестве осадков, выпавших за каждый
# день января. Определить общее количество осадков за январь.

someList = [12, 15, 16, 17, 14]
sumOsadki = sum(someList)
print(sumOsadki)


# 11.36.
# Дан массив. Напечатать:

# а) все неотрицательные элементы
someList = [36, 56, -40, 54, -2]
index = 0
while index < len(someList):
    if someList[index] >= 0:
        print(someList[index])
    index += 1

# б) все элементы, не превышающие число 100
someList = [236, 56, -40, 154, -2]
index = 0
while index < len(someList):
    if someList[index] < 100:
        print(someList[index])
    index += 1


# 11.39.
# Дан массив. Напечатать:

а) второй, четвертый и т. д. элементы;
someList = [236, 56, -40, 154, -2, 251, 140, 24]
print(someList[1::2])

б) третий, шестой и т. д. элементы
someList = [236, 56, -40, 154, -2, 251, 140, 24, 15]
print(someList[2::3])


# 11.52. Дан массив целых чисел.
а) Все элементы, оканчивающиеся цифрой 4, уменьшить вдвое.
someList = [36, 56, 44, 54, 2]
index = 0
while index < len(someList):
    if someList[index] % 10 == 4:
        someList[index] /= 2
    index += 1
print(someList)

# б) Все четные элементы заменить на их квадраты, а нечетные удвоить.
someList = [33, 4, 41, 8, 2]
index = 0
while index < len(someList):
    if someList[index] % 2 == 0:
        someList[index] **= 2
    if someList[index] % 2 != 0:
        someList[index] *= 2
    index += 1
print(someList)


# 11.53. Дан массив целых чисел.
# а) Все элементы, кратные числу 10, заменить нулем.

someList = [36, 20, 44, 54, 60]
index = 0
while index < len(someList):
    if someList[index] % 10 == 0:
        someList[index] = '0'
    index += 1
print(someList)








